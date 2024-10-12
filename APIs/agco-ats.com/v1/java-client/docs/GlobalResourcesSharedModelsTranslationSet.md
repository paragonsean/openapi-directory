

# GlobalResourcesSharedModelsTranslationSet

A set of strings submitted for translation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**List&lt;GlobalResourcesSharedModelsTranslationSetAttribute&gt;**](GlobalResourcesSharedModelsTranslationSetAttribute.md) | Attributes of the Translation Set |  [optional] |
|**fileIDs** | **List&lt;String&gt;** | IDs for files related to this translation set. For example, the original and processed files |  |
|**id** | **Integer** | The id of the TranslationSet. |  [optional] |
|**inDate** | **OffsetDateTime** | Read Only. The date the translation set was returned. |  [optional] |
|**notes** | **String** | Notes on the TranslationSet |  [optional] |
|**outDate** | **OffsetDateTime** | Read Only. The date the translation set was sent out. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | An enum indicating the state of the translation set |  |
|**translationRequestID** | **Integer** | Read Only. The Id of the TranslationRequest which generated this translation set. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| OUT_FOR_PROCESSING | &quot;OutForProcessing&quot; |
| PROCESSING | &quot;Processing&quot; |
| PENDING_APPROVAL | &quot;PendingApproval&quot; |
| OUT_FOR_TRANSLATION | &quot;OutForTranslation&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| COMPLETED | &quot;Completed&quot; |



