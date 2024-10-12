

# CheckValuePropertyBatchOperation

Represents a PropertyBatchOperation that compares the value of the property with the expected value. The CheckValuePropertyBatchOperation is generally used as a precondition for the write operations in the batch. Note that if one PropertyBatchOperation in a PropertyBatch fails, the entire batch fails and cannot be committed in a transactional manner.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**value** | [**PropertyValue**](PropertyValue.md) |  |  |



