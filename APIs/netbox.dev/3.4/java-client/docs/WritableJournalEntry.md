

# WritableJournalEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignedObject** | **Object** |  |  [optional] [readonly] |
|**assignedObjectId** | **Integer** |  |  |
|**assignedObjectType** | **String** |  |  |
|**comments** | **String** |  |  |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**createdBy** | **Integer** |  |  [optional] |
|**customFields** | **Object** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**kind** | [**KindEnum**](#KindEnum) |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| INFO | &quot;info&quot; |
| SUCCESS | &quot;success&quot; |
| WARNING | &quot;warning&quot; |
| DANGER | &quot;danger&quot; |



