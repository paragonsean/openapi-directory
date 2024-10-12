

# IdentityMatches


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containsImage** | **Boolean** | Flag that indicates if there is an image that contains a face on it. |  [optional] |
|**dateOfBirth** | **OffsetDateTime** | The date of birth found on the document, null if not found. |  [optional] |
|**expiryDate** | **OffsetDateTime** | The expiry date found on the document, null if not found. |  [optional] |
|**firstName** | **String** | The customer first name if it was matched, null otherwise. |  [optional] |
|**hasMinimalAge** | **Boolean** | Checks the minimal age, 21+ for USA and 18+ for all other countries. Null if dateOfBirth could not be determined. |  [optional] [readonly] |
|**isIdentityDocument** | **Boolean** | Flag that indicates if this looks like and ID. |  [optional] |
|**isPublishedOnline** | **Boolean** | If there is an exact match found online. |  [optional] |
|**issueDate** | **OffsetDateTime** | The issued date found on the document, null if not found. |  [optional] |
|**lastName** | **String** | The customer last name if it was matched, null otherwise. |  [optional] |
|**nationality** | **String** | The nationality found on the document, null otherwise. |  [optional] |



