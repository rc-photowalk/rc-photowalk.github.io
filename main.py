import os
import glob
import templates
from os.path import join as pj

img_root = 'images'

prompts = [
    'Something beautiful',
    'An animal',
    'A flower',
    'Something with texture',
    'Something that makes you happy',
    'Something with lines',
    'Someone laughing',
    'A reflection',
    'A portrait',
    'A sign',
]

photographers = [
    'Bijhan',
    'Cam',
    'Esther',
    'Jonathan',
    'Josh',
    'Melanie_Nelson',
    'Rachel_John',
    'Shirley_Aiden',
    'Victoria_William',
    'YJ',
    'Zach',
]

def make_entry(photographer, prompt_i, photo_i=0):
    full_path = '/'.join([img_root, photographer, 'fulls', '%02d-%02d.jpg' % (prompt_i, photo_i)])
    thumb_path = '/'.join([img_root, photographer, 'thumbs', '%02d-%02d.jpg' % (prompt_i, photo_i)])

    if not os.path.exists(full_path):
        full_path = '/'.join([img_root, photographer, 'fulls', '%02d-%02d.jpeg' % (prompt_i, photo_i)])
        thumb_path = '/'.join([img_root, photographer, 'thumbs', '%02d-%02d.jpeg' % (prompt_i, photo_i)])

    photographer = photographer.replace('_', ' & ')
    return templates.entry % ('/' + full_path, '/' + thumb_path, photographer, prompts[prompt_i-1])

# make the front page
entries = [
    make_entry('Cam', 1),
    make_entry('Bijhan', 5),
    make_entry('Esther', 3, 1),
    make_entry('Jonathan', 5, 6),
    make_entry('Josh', 6),
    make_entry('Melanie_Nelson', 2, 1),
    make_entry('Rachel_John', 10, 1),
    make_entry('Shirley_Aiden', 8),
    make_entry('Victoria_William', 8, 1),
    make_entry('YJ', 3),
    make_entry('Zach', 8),
]

entries_str = ''
for entry in entries:
    entries_str += entry

with open('index.html', 'w') as f:
    f.write(templates.page % ('Photo Walk', entries_str))

# make the prompt-specific pages
for prompt_i, prompt in enumerate(prompts):
    entries = []
    for img_path in glob.glob(pj(img_root, '*', 'fulls', '%02d-*' % (prompt_i+1))):
        tokens = img_path.split(os.path.sep)
        photographer = tokens[1]
        photo_i = int(tokens[-1].split('.')[0].split('-')[1])
        entries.append(make_entry(photographer, prompt_i+1, photo_i))

    entries_str = ''
    for entry in entries:
        entries_str += entry

    with open('prompt_%02d.html' % prompt_i, 'w') as f:
        f.write(templates.page % (prompt, entries_str))

# make the photographer-specific pages
for photographer_i, photographer in enumerate(photographers):
    entries = []
    for img_path in glob.glob(pj(img_root, photographer, 'fulls', '*')):
        tokens = img_path.split(os.path.sep)
        prompt_i = int(tokens[-1].split('.')[0].split('-')[0]) - 1
        photo_i = int(tokens[-1].split('.')[0].split('-')[1])
        entries.append(make_entry(photographer, prompt_i+1, photo_i))

    entries_str = ''
    for entry in entries:
        entries_str += entry

    with open('photographer_%02d.html' % photographer_i, 'w') as f:
        f.write(templates.page % (photographer.replace('_', ' & '), entries_str))