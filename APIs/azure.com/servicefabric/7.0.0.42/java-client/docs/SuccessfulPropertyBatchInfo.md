

# SuccessfulPropertyBatchInfo

Derived from PropertyBatchInfo. Represents the property batch succeeding. Contains the results of any \"Get\" operations in the batch.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | **Object** | A map containing the properties that were requested through any \&quot;Get\&quot; property batch operations. The key represents the index of the \&quot;Get\&quot; operation in the original request, in string form. The value is the property. If a property is not found, it will not be in the map. |  [optional] |



