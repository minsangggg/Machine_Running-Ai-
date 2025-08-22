import meilisearch
client=meilisearch.Client('http://127.0.0.1:7700', 'yrU4Nyoa7R5YK3okInM9OfZ4Br8T9SGz4mQC8wnJ-4Q ')

def stock_search(query):
    return client.index('nasdaq').search('appl')