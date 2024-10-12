# RebillyRestApi.AddressMatches

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **String** | The customer city if it was matched, null otherwise. | [optional] 
**date** | **Date** | The date on the document proving the document is recent. | [optional] 
**firstName** | **String** | The customer first name if it was matched, null otherwise. | [optional] 
**lastName** | **String** | The customer last name if it was matched, null otherwise. | [optional] 
**line1** | **String** | The customer address if it was matched, null otherwise. | [optional] 
**phone** | **String** | The phone of the company or agency that sent the document. | [optional] 
**postalCode** | **String** | The customer postal code if it was matched, null otherwise. | [optional] 
**region** | **String** | The customer region if it was matched, null otherwise. | [optional] 
**uniqueWords** | **Number** | The number of unique words in the document. | [optional] 
**uniqueWordsResult** | **Boolean** | Flag that indicates if the unique words passed the threshold. | [optional] [readonly] 
**wordCount** | **Number** | The number of words in the document. | [optional] 
**wordCountResult** | **Boolean** | Flag that indicates if the word count passed the threshold. | [optional] [readonly] 


