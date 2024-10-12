

# GlobalResourcesSharedModelsStringTranslation

A translation of a string in a specific language

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorId** | **Integer** | The id of the user to last edit thie translation |  [optional] |
|**languageId** | **Integer** | The id of the language of the translation |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the translation |  [optional] |
|**stringId** | **String** | The id of the string that is translated |  [optional] |
|**stringValue** | **String** | The translated string |  |
|**timestamp** | **byte[]** | A value indicating the last modification of this translation. Read Only. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ORIGINAL | &quot;Original&quot; |
| REQUESTED | &quot;Requested&quot; |
| PROCESSING | &quot;Processing&quot; |
| PROCESSED | &quot;Processed&quot; |
| VALIDATED | &quot;Validated&quot; |
| INVALIDATED | &quot;Invalidated&quot; |
| REQUEST_PENDING | &quot;RequestPending&quot; |
| CREATE_PENDING | &quot;CreatePending&quot; |



