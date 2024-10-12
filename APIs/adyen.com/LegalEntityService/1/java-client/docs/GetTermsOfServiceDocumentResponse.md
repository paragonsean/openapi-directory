

# GetTermsOfServiceDocumentResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**document** | **String** | The Terms of Service document in Base64-encoded format. |  [optional] |
|**id** | **String** | The unique identifier of the legal entity. |  [optional] |
|**language** | **String** | The language used for the Terms of Service document, specified by the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code. Possible value: **en** for English. |  [optional] |
|**termsOfServiceDocumentId** | **String** | The unique identifier of the Terms of Service document. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of Terms of Service.  Possible values: *  **adyenForPlatformsManage** *  **adyenIssuing** *  **adyenForPlatformsAdvanced** *  **adyenCapital** *  **adyenAccount** *  **adyenCard** *  **adyenFranchisee** *  **adyenPccr**   |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADYEN_ACCOUNT | &quot;adyenAccount&quot; |
| ADYEN_CAPITAL | &quot;adyenCapital&quot; |
| ADYEN_CARD | &quot;adyenCard&quot; |
| ADYEN_FOR_PLATFORMS_ADVANCED | &quot;adyenForPlatformsAdvanced&quot; |
| ADYEN_FOR_PLATFORMS_MANAGE | &quot;adyenForPlatformsManage&quot; |
| ADYEN_FRANCHISEE | &quot;adyenFranchisee&quot; |
| ADYEN_ISSUING | &quot;adyenIssuing&quot; |
| ADYEN_PCCR | &quot;adyenPccr&quot; |



