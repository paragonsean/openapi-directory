

# DocumentChange

A Document has changed. May be the result of multiple writes, including deletes, that ultimately resulted in a new value for the Document. Multiple DocumentChange messages may be returned for the same logical change, if multiple targets are affected.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**document** | [**Document**](Document.md) |  |  [optional] |
|**removedTargetIds** | **List&lt;Integer&gt;** | A set of target IDs for targets that no longer match this document. |  [optional] |
|**targetIds** | **List&lt;Integer&gt;** | A set of target IDs of targets that match this document. |  [optional] |



