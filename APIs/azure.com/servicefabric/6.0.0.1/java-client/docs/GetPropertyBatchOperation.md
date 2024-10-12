

# GetPropertyBatchOperation

Represents a PropertyBatchOperation that gets the specified property if it exists.  Note that if one PropertyBatchOperation in a PropertyBatch fails,  the entire batch fails and cannot be committed in a transactional manner. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includeValue** | **Boolean** | Whether or not to return the property value with the metadata.  True if values should be returned with the metadata; False to return only property metadata.  |  [optional] |



