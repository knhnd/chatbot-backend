import pickle

mydict = {
    'test' : 'ChatBot Works!',
    'sample' : 'How are you?',
    'hello' : 'Hello, World!',
    'おはよう' : 'おはようございます！コーヒーでもどうですか？',
    'こんにちは' : 'こんにちは！お昼は何をたべましたか？',
    'こんばんは' : 'こんばんは、いい夜をお過ごしください。',
    'except' : 'すみません、よくわかりませんでした。'
}

with open('mydict.pkl', mode='wb') as f:
    pickle.dump(mydict, f)