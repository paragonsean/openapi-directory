

# PersonalDocumentData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expirationDate** | **String** | The expiry date of the document,   in ISO-8601 YYYY-MM-DD format. For example, **2000-01-31**. |  [optional] |
|**issuerCountry** | **String** | The country where the document was issued, in the two-character  [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **NL**. |  [optional] |
|**issuerState** | **String** | The state where the document was issued (if applicable). |  [optional] |
|**number** | **String** | The number in the document. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the document. Possible values: **ID**, **DRIVINGLICENSE**, **PASSPORT**, **SOCIALSECURITY**, **VISA**.  To delete an existing entry for a document &#x60;type&#x60;, send only the &#x60;type&#x60; field in your request.  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DRIVINGLICENSE | &quot;DRIVINGLICENSE&quot; |
| ID | &quot;ID&quot; |
| PASSPORT | &quot;PASSPORT&quot; |
| SOCIALSECURITY | &quot;SOCIALSECURITY&quot; |
| VISA | &quot;VISA&quot; |



