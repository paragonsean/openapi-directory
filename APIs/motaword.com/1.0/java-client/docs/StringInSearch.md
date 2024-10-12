

# StringInSearch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileId** | **Long** |  |  [optional] |
|**internalProjectId** | **Long** |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** | the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z |  [optional] |
|**projectId** | **Long** |  |  [optional] |
|**searchScore** | **Float** |  |  [optional] |
|**source** | **String** |  |  [optional] |
|**status** | **StringTranslationState** |  |  [optional] |
|**stringId** | **Long** |  |  [optional] |
|**target** | **String** |  |  [optional] |
|**targets** | **List&lt;String&gt;** |  |  [optional] |
|**tmName** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | String search result typ from ZNT. Options are LOCAL_PROJECT, IMPORTED_TM. Imported TM results should probably not be visible to end users. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LOCAL_PROJECT | &quot;LOCAL_PROJECT&quot; |
| IMPORTED_TM | &quot;IMPORTED_TM&quot; |



