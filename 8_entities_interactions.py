import nltk
import json
import os


BLOG_DATA = "./feed.json"

HTML_TEMPLATE = """<html>
    <head>
        <title>%s</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    </head>
    <body>%s</body>
</html>"""


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

    # Display output as markup with entities presented in bold text

    post['markup'] = []

    for sentence_idx in range(len(post['sentences'])):

        s = post['sentences'][sentence_idx]
        for (term, _) in post['entity_interactions'][sentence_idx]:
            s = s.replace(term, '<strong>%s</strong>' % (term, ))

        post['markup'] += [s]

    filename = post['title'].replace("?", "") + '.entity_interactions.html'
    f = open(os.path.join('./entities_interactions', filename), 'w')
    html = HTML_TEMPLATE % (post['title'] + ' Interactions',
                            ' '.join(post['markup']),)
    f.write(html.encode('utf-8'))
    f.close()

    print "Data written to", f.name
