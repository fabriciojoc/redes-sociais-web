import nltk
import json

BLOG_DATA = "./feed.json"

blog_data = json.loads(open(BLOG_DATA).read())

for post in blog_data:
    # EOS Detection
    sentences = nltk.tokenize.sent_tokenize(post['description'])
    # Tokenization
    tokens = []
    for s in sentences:
        tokens.append(nltk.tokenize.word_tokenize(s))
    # POS Tagging
    pos_tagged_tokens = []
    for t in tokens:
        pos_tagged_tokens.append(nltk.pos_tag(t))
    # Flatten the list since we're not using sentence structure
    # and sentences are guaranteed to be separated by a special
    # POS tuple such as ('.', '.')
    tagged_tokens = []
    for sent in pos_tagged_tokens:
        for token in sent:
            if token[0].lower() not in nltk.corpus.stopwords.words('portuguese'):
                tagged_tokens.append(token)
    all_entity_chunks = []
    previous_pos = None
    current_entity_chunk = []
    for (token, pos) in tagged_tokens:
        if pos == previous_pos and pos.startswith('NN'):
            current_entity_chunk.append(token)
        elif pos.startswith('NN'):
            if current_entity_chunk != []:
                # Note that current_entity_chunk could be a duplicate when appended,
                # so frequency analysis again becomes a consideration
                all_entity_chunks.append((' '.join(current_entity_chunk), pos))
            current_entity_chunk = [token]
        previous_pos = pos
    # Store the chunks as an index for the document
    # and account for frequency while we're at it...
    post['entities'] = {}
    for c in all_entity_chunks:
        post['entities'][c] = post['entities'].get(c, 0) + 1
    # For example, we could display just the title-cased entities
    print post['title']
    print '-' * len(post['title'])
    proper_nouns = []
    for (entity, pos) in post['entities']:
        if entity.istitle():
            print '\t%s (%s)' % (entity, post['entities'][(entity, pos)])
    print
