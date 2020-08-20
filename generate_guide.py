import re
import os
import yaml
import xml.etree.ElementTree as et

from glob import glob
from collections import defaultdict
from jinja2 import Template

ESCAPE_CHARACTERS = {
    '&':'&amp;',
    '<':'&lt;',
    '>':'&gt;',
    '"':'&quot;',
    "'":'&apos;',
    '<\\':'&lt\\',
    '>\\':'&gt\\'

}

def main():

    # Create a store of what has been processed.
    store = defaultdict(lambda: defaultdict(list))

    # Iterate through all the files in /source
    for xml_path in glob('./source/*.xml'):

        # Parse file
        parsed = parse_entry(xml_path)

        if parsed['include']: # Switch to turn on/off questions.

            # Save as markdown
            convert_to_markdown(parsed)

            # Add to TOC
            category = parsed['category']
            subcategory = parsed['subcategory']
            slug = parsed['slug']
            filepath = f'{category.lower().replace(" ", "_")}/{subcategory.lower().replace(" ", "_")}/{slug}'
            store[category][subcategory].append(filepath)

    # Build TOC
    toc = build_toc(store)

    # Save TOC
    save_toc(toc)

    # Create landing pages 
    # For now these are just titles but we might add something more.
    for cat, d in store.items(): 
        for subcat, _ in d.items():
            with open(f'guide/{cat.lower().replace(" ", "_")}/{subcat.lower().replace(" ", "_")}/index.md','w') as f:
                f.write(f'# {subcat}' + '\n\n ```{tableofcontents}\n```')


def build_toc(entry_store:dict):
    """Build the TOC using the stored entries."""

    complete = [{'file': 'intro', 'numbered': False},
                {'part':'Introduction',
                 'chapters':[
                     {'file': 'about'},
                     {'file': 'interview_tips'},
                     {'file': 'resources'},
                     {'file': 'contribute'},
                 ]}]
    for cat, d in entry_store.items():
        base = {'part': cat,
                'chapters': []}
        for subcat, l in d.items():
            subbase = {'file': f'{cat.lower().replace(" ", "_")}/{subcat.lower().replace(" ", "_")}/index',
                    'numbered': True,
                    'sections': [{'file':f} for f in l]}
            base['chapters'].append(subbase)
        complete.append(base)

    return complete


def save_toc(toc_dict:dict, toc_path:str='./guide/_toc.yml'):
    """Saves the TOC to YAML."""

    with open(toc_path, 'w') as f:
        f.write(yaml.dump(toc_dict))


def convert_to_markdown(entry:dict, template_path:str='./templates/onepage.md.jinja'):
    """Use a parsed entry to save as markdown using the jinja template."""
    
    with open(template_path) as f:
        tmpl = Template(f.read())
    page = tmpl.render(**entry)

    folder = entry['category'].lower().replace(' ', '_')
    subfolder = entry['subcategory'].lower().replace(' ', '_')
    slug = entry['slug']
    filepath = f'guide/{folder}/{subfolder}'

    if not os.path.exists(filepath):
        os.makedirs(filepath)

    with open(os.path.join(filepath,f'{slug}.md'),'w') as f:
        f.write(page)


def parse_entry(filepath:str):
    """Parse a question entry from (almost) XML"""

    # Load the XML as string
    with open(filepath, 'r') as f:
        entry = f.read()

    # Ensure that the question and answers comply with XML schema.
    for tag in ['answer','question']:
        entry = sanitise_content(entry, tag)

    # Load XML
    root = et.ElementTree(et.fromstring(entry)).getroot()

    # Store as dictionary
    parsed = parse_xml(root)

    return parsed


def sanitise_content(entry:str, tag:str):
    """Sanitise the content so it can be parsed by the XML Parser."""

    pattern = re.compile(f'<{tag}>(.*)</{tag}>', re.MULTILINE | re.DOTALL)
    result = re.search(pattern, entry)

    # start, end = [(m.start(0), m.end(0)) for m in result][0]
    start, end = result.span()
    shift = len(tag)
    start = start + shift + 2
    end = end - shift - 3

    text = result.group()
    text = text[shift+2:-(shift+3)]
    
    for char, rep in ESCAPE_CHARACTERS.items():
        text = text.replace(char, rep)

    entry = entry[:start] + text + entry[end:]

    return entry


def parse_xml(root:et.ElementTree):
    """Parse the XML tree to return an equivalent dict."""

    parsed = {}

    for value in ['title', 'slug', 'date', 'category', 'subcategory', 'question', 'answer', 'difficulty']:
        parsed[value] = root.find(value).text

    parsed['interviews'] = [x.text for x in root.findall('interview')]
    parsed['links'] = {x.get('name'):x.text for x in root.findall('link')}
    parsed['include'] = bool(root.find('include').text)

    if parsed['answer'].strip('\n') == '':
        parsed['answer'] = None

    return parsed

if __name__ == "__main__":
    main()