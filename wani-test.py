import wanikani_api.client as client

wk_api = None
with open("wanikani-api-key.txt", "r") as key:
    wk_api = client.Client(key.readline())

user_info = wk_api.user_information()
print(user_info)

vocabulary = wk_api.subjects(types="vocabulary", fetch_all=True)
for vocab in vocabulary:
    # print(vocab.__dict__)
    print(vocab.slug, end=" ")
    for reading in vocab.readings:
        print(reading.reading)
print("# vocab: ", len(vocabulary))
