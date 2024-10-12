# LuisAuthoringClient.PhraseListFeatureInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isExchangeable** | **Boolean** | An exchangeable phrase list feature are serves as single feature to the LUIS underlying training algorithm. It is used as a lexicon lookup feature where its value is 1 if the lexicon contains a given word or 0 if it doesn’t. Think of an exchangeable as a synonyms list. A non-exchangeable phrase list feature has all the phrases in the list serve as separate features to the underlying training algorithm. So, if you your phrase list feature contains 5 phrases, they will be mapped to 5 separate features. You can think of the non-exchangeable phrase list feature as an additional bag of words that you are willing to add to LUIS existing vocabulary features. Think of a non-exchangeable as set of different words. Default value is true. | [optional] 
**phrases** | **String** | A list of comma-separated values. | [optional] 
**enabledForAllModels** | **Boolean** | Indicates if the feature is enabled for all models in the application. | [optional] 
**id** | **Number** | A six-digit ID used for Features. | [optional] 
**isActive** | **Boolean** | Indicates if the feature is enabled. | [optional] 
**name** | **String** | The name of the Feature. | [optional] 


