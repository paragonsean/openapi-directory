

# IdentificationData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardNumber** | **String** | The card number of the document that was issued (AU only). |  [optional] |
|**expiryDate** | **String** | The expiry date of the document, in YYYY-MM-DD format. |  [optional] |
|**issuerCountry** | **String** | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the document was issued. For example, **US**. |  [optional] |
|**issuerState** | **String** | The state or province where the document was issued (AU only). |  [optional] |
|**nationalIdExempt** | **Boolean** | Applies only to individuals in the US. Set to **true** if the individual does not have an SSN. To verify their identity, Adyen will require them to upload an ID document. |  [optional] |
|**number** | **String** | The number in the document. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of identity data. For **individual**, the &#x60;type&#x60; value is **nationalIdNumber**. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NATIONAL_ID_NUMBER | &quot;nationalIdNumber&quot; |



