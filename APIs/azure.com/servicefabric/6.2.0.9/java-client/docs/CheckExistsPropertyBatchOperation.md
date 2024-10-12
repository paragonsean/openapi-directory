

# CheckExistsPropertyBatchOperation

Represents a PropertyBatchOperation that compares the Boolean existence of a property with the Exists argument. The PropertyBatchOperation operation fails if the property's existence is not equal to the Exists argument. The CheckExistsPropertyBatchOperation is generally used as a precondition for the write operations in the batch. Note that if one PropertyBatchOperation in a PropertyBatch fails, the entire batch fails and cannot be committed in a transactional manner.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exists** | **Boolean** | Whether or not the property should exist for the operation to pass. |  |



