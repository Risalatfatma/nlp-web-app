import paralleldots
paralleldots.set_api_key('T6jBrNU2jb8Uf68kwf4ccOWSkaEvLMPd46uxquvrynY')


def ner(text):
    ner = paralleldots.ner(text)
    return ner


def sentiment_analysis(text):
    sentiment_analysis = paralleldots.sentiment(text)
    return sentiment_analysis


def abuse_detection(text):
    abuse_detection = paralleldots.abuse(text)
    return abuse_detection

