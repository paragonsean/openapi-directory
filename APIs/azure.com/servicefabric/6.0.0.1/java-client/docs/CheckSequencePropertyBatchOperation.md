

# CheckSequencePropertyBatchOperation

Compares the Sequence Number of a property with the SequenceNumber argument.  A property's sequence number can be thought of as that property's version.  Every time the property is modified, its sequence number is increased.  The sequence number can be found in a property's metadata.  The comparison fails if the sequence numbers are not equal.  CheckSequencePropertyBatchOperation is generally used as a precondition for the write operations in the batch.  Note that if one PropertyBatchOperation in a PropertyBatch fails,  the entire batch fails and cannot be committed in a transactional manner. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sequenceNumber** | **String** | The expected sequence number. |  |



