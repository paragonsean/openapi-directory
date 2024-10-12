

# Call


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**cadence** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**calledPerson** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | Datetime of when the call was created |  [optional] |
|**crmActivity** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**disposition** | **String** | Result of the call |  [optional] |
|**duration** | **Integer** | Length of the call in seconds |  [optional] |
|**id** | **Integer** | ID of Call |  [optional] |
|**note** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**recordings** | [**List&lt;EmbeddedRecordingResource&gt;**](EmbeddedRecordingResource.md) | The recordings for this this call and their status |  [optional] |
|**sentiment** | **String** | Outcome of the conversation |  [optional] |
|**step** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**to** | **String** | Phone number that received the call |  [optional] |
|**updatedAt** | **OffsetDateTime** | Datetime of when the call was last updated |  [optional] |
|**user** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |



