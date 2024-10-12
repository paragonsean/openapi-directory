

# DocumentDelete

A Document has been deleted. May be the result of multiple writes, including updates, the last of which deleted the Document. Multiple DocumentDelete messages may be returned for the same logical delete, if multiple targets are affected.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**document** | **String** | The resource name of the Document that was deleted. |  [optional] |
|**readTime** | **String** | The read timestamp at which the delete was observed. Greater or equal to the &#x60;commit_time&#x60; of the delete. |  [optional] |
|**removedTargetIds** | **List&lt;Integer&gt;** | A set of target IDs for targets that previously matched this entity. |  [optional] |



