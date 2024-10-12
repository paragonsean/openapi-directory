# RebillyRestApi.PostKycDocumentMatchesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containsImage** | **Boolean** | Flag that indicates if there is an image that contains a face on it. | [optional] 
**dateOfBirth** | **Date** | The date of birth found on the document, null if not found. | [optional] 
**expiryDate** | **Date** | The expiry date found on the document, null if not found. | [optional] 
**firstName** | **String** | The customer first name if it was matched, null otherwise. | [optional] 
**hasMinimalAge** | **Boolean** | Checks the minimal age, 21+ for USA and 18+ for all other countries. Null if dateOfBirth could not be determined. | [optional] [readonly] 
**isIdentityDocument** | **Boolean** | Flag that indicates if this looks like and ID. | [optional] 
**isPublishedOnline** | **Boolean** | If there is an exact match found online. | [optional] 
**issueDate** | **Date** | The issued date found on the document, null if not found. | [optional] 
**lastName** | **String** | The customer last name if it was matched, null otherwise. | [optional] 
**nationality** | **String** | The nationality found on the document, null otherwise. | [optional] 
**city** | **String** | The customer city if it was matched, null otherwise. | [optional] 
**date** | **Date** | The date on the document proving the document is recent. | [optional] 
**line1** | **String** | The customer address if it was matched, null otherwise. | [optional] 
**phone** | **String** | The phone of the company or agency that sent the document. | [optional] 
**postalCode** | **String** | The customer postal code if it was matched, null otherwise. | [optional] 
**region** | **String** | The customer region if it was matched, null otherwise. | [optional] 
**uniqueWords** | **Number** | The number of unique words in the document. | [optional] 
**uniqueWordsResult** | **Boolean** | Flag that indicates if the unique words passed the threshold. | [optional] [readonly] 
**wordCount** | **Number** | The number of words in the document. | [optional] 
**wordCountResult** | **Boolean** | Flag that indicates if the word count passed the threshold. | [optional] [readonly] 


