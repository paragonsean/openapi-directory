# LuisAuthoringClient.PhraselistUpdateObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isActive** | **Boolean** | Indicates if the Phraselist is enabled. | [optional] [default to true]
**isExchangeable** | **Boolean** | An exchangeable phrase list feature are serves as single feature to the LUIS underlying training algorithm. It is used as a lexicon lookup feature where its value is 1 if the lexicon contains a given word or 0 if it doesn’t. Think of an exchangeable as a synonyms list. A non-exchangeable phrase list feature has all the phrases in the list serve as separate features to the underlying training algorithm. So, if you your phrase list feature contains 5 phrases, they will be mapped to 5 separate features. You can think of the non-exchangeable phrase list feature as an additional bag of words that you are willing to add to LUIS existing vocabulary features. Think of a non-exchangeable as set of different words. Default value is true. | [optional] [default to true]
**name** | **String** | The Phraselist name. | [optional] 
**phrases** | **String** | List of comma-separated phrases that represent the Phraselist. | [optional] 


