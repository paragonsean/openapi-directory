

# ConfigurationDocumentSection


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoCategoriesLimit** | **Integer** | Limits the number of auto categories the service responds. Default: 5 |  |
|**conceptTopicsLimit** | **Integer** | Limits the number of concept topics the service responds. Default: 5 |  |
|**detectLanguage** | **Boolean** | Switches on language detection feature. Default: true |  |
|**entityThemesLimit** | **Integer** | Limits the number of entity themes the service responds. Default: 0 |  |
|**intentions** | **Boolean** | Switches on intentions detection feature. Default: false |  |
|**modelSentiment** | **Boolean** | Switches on/off model-based sentiment feature. Default: false |  |
|**namedEntitiesLimit** | **Integer** | Limits the number of named entities the service responds. Default: 5 |  |
|**namedMentionsLimit** | **Integer** | Limits the number of named entity related mentions. Default: 0 |  |
|**namedOpinionsLimit** | **Integer** | Limits the number of named entity opinions the service responds. Default: 0 |  |
|**namedRelationsLimit** | **Integer** | Limits the number of named entity relations the service responds. Default: 0 |  |
|**phrasesLimit** | **Integer** | Limits the number of responded sentiment-bearing phrases for document. Default: 0 |  |
|**posTypes** | [**PosTypesEnum**](#PosTypesEnum) | Defines parts-of-speech which will be responded by the server |  |
|**possiblePhrasesLimit** | **Integer** | Limits the number of responded possible phrases which may affect on sentiment score extraction. Default: 0 |  |
|**queryTopicsLimit** | **Integer** | Limits the number of query topics the service responds. Default: 5 |  |
|**summaryLimit** | **Integer** | Limits the number of sentences for the document summary feature. Default: 3 |  |
|**themeMentionsLimit** | **Integer** | Limits the number of document and entity related theme mentions. Default: 0 |  |
|**themesLimit** | **Integer** | Limits the number of document themes the service responds. Default: 0 |  |
|**userEntitiesLimit** | **Integer** | Limits the number of user entities the service responds. Default: 5 |  |
|**userMentionsLimit** | **Integer** | Limits the number of user entity related mentions. Default: 0 |  |
|**userOpinionsLimit** | **Integer** | Limits the number of concept topics the service responds. Default: 0 |  |
|**userRelationsLimit** | **Integer** | Limits the number of user entity relations the service responds. Default: 0 |  |



## Enum: PosTypesEnum

| Name | Value |
|---- | -----|
| ALL | &quot;All&quot; |
| NOUN | &quot;Noun&quot; |
| VERB | &quot;Verb&quot; |
| ADJECTIVE | &quot;Adjective&quot; |
| DETERMINER | &quot;Determiner&quot; |
| MISC | &quot;Misc&quot; |
| TWITTER | &quot;Twitter&quot; |
| CHINESE | &quot;Chinese&quot; |



