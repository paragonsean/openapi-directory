

# BatchWriteResponse

The result of applying a batch of mutations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitTimestamp** | **String** | The commit timestamp of the transaction that applied this batch. Present if &#x60;status&#x60; is &#x60;OK&#x60;, absent otherwise. |  [optional] |
|**indexes** | **List&lt;Integer&gt;** | The mutation groups applied in this batch. The values index into the &#x60;mutation_groups&#x60; field in the corresponding &#x60;BatchWriteRequest&#x60;. |  [optional] |
|**status** | [**Status**](Status.md) |  |  [optional] |



