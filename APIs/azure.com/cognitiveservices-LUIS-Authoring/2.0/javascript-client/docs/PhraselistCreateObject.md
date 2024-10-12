# LuisAuthoringClient.PhraselistCreateObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isExchangeable** | **Boolean** | An interchangeable phrase list feature serves as a list of synonyms for training. A non-exchangeable phrase list serves as separate features for training. So, if your non-interchangeable phrase list contains 5 phrases, they will be mapped to 5 separate features. You can think of the non-interchangeable phrase list as an additional bag of words to add to LUIS existing vocabulary features. It is used as a lexicon lookup feature where its value is 1 if the lexicon contains a given word or 0 if it doesn’t.  Default value is true. | [optional] [default to true]
**name** | **String** | The Phraselist name. | [optional] 
**phrases** | **String** | List of comma-separated phrases that represent the Phraselist. | [optional] 


