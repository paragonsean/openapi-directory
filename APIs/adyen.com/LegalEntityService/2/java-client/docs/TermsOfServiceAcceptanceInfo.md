

# TermsOfServiceAcceptanceInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptedBy** | **String** | The unique identifier of the user that accepted the Terms of Service. |  [optional] |
|**acceptedFor** | **String** | The unique identifier of the legal entity for which the Terms of Service are accepted. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date when the Terms of Service were accepted. |  [optional] |
|**id** | **String** | An Adyen-generated reference for the accepted Terms of Service. |  [optional] |
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



