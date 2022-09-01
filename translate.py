import six
from google.cloud import translate_v2 as translate
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd 


def getGCPTranslateClient():
   client = translate.Client.from_service_account_json("../Auth-keys/AccentureServices-3dc6668d043d.json") #, project='accentureservices'
   return client
   

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = getGCPTranslateClient()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)
    print(u"Text: {}".format(result["input"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    
    return result["translatedText"]

    



def main():
  df = pd.read_excel('sales-translations-1229.xlsx')  
  df2 = df.copy()

  for index, row in df.iterrows():
     result = translate_text('pt',row['Label'])
     print( result )
     df2['Translation1'][index] = result

  df2.to_excel("output.xlsx")  



if __name__ == '__main__':
    main()

