

# PutPropertyBatchOperation

Puts the specified property under the specified name. Note that if one PropertyBatchOperation in a PropertyBatch fails, the entire batch fails and cannot be committed in a transactional manner.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customTypeId** | **String** | The property&#39;s custom type id. Using this property, the user is able to tag the type of the value of the property. |  [optional] |
|**value** | [**PropertyValue**](PropertyValue.md) |  |  |



