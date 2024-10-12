

# ConfigurationInsertVersion


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoResponse** | **Boolean** | Defines whether or not the service should respond with processed results automatically. Default: false |  |
|**callback** | **String** | Defines a callback URL for automatic data responding |  |
|**categoriesThreshold** | **Double** | Defines low threshold for strength score of user categories to be reported in the output. Default: 0.45 |  |
|**charsThreshold** | **Integer** | Defines the threshold for alphanumeric characters in the text in percent. Default: 80 |  |
|**collection** | [**ConfigurationCollectionSection**](ConfigurationCollectionSection.md) |  |  |
|**document** | [**ConfigurationDocumentSection**](ConfigurationDocumentSection.md) |  |  |
|**entitiesThreshold** | **Integer** | Defines low threshold for evidence score of named and user entities to be reported in the output. |  |
|**isPrimary** | **Boolean** | Identifies whether the current configuration is primary or not. Default: false |  |
|**language** | **String** | Defines target language that will be used for task processing. Default: English |  |
|**name** | **String** | Configuration name |  |
|**oneSentence** | **Boolean** | Leads the service to consider the entire document as single sentence. Default: false |  |
|**processHtml** | **Boolean** | Leads the service to clean HTML tags before processing. Default: false |  |



