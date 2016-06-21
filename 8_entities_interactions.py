import nltk
import json

BLOG_DATA = "./feed.json"

def extract_interactions(txt):
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

    entity_interactions = []
    for sentence in pos_tagged_tokens:

        all_entity_chunks = []
        previous_pos = None
        current_entity_chunk = []

        for (token, pos) in sentence:

            if pos == previous_pos and pos.startswith('NN'):
                current_entity_chunk.append(token)
            elif pos.startswith('NN'):
                if current_entity_chunk != []:
                    all_entity_chunks.append((' '.join(current_entity_chunk),
                            pos))
                current_entity_chunk = [token]

            previous_pos = pos

        if len(all_entity_chunks) > 1:
            entity_interactions.append(all_entity_chunks)
        else:
            entity_interactions.append([])

    assert len(entity_interactions) == len(sentences)

    return dict(entity_interactions=entity_interactions,
                sentences=sentences)

blog_data = json.loads(open(BLOG_DATA).read())

# Display selected interactions on a per-sentence basis

for post in blog_data:

    post.update(extract_interactions(post['description']))

    print post['title']
    print '-' * len(post['title'])
    for interactions in post['entity_interactions']:
        print '; '.join([i[0] for i in interactions])
    print
