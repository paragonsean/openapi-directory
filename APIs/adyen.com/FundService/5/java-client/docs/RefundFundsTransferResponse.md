

# RefundFundsTransferResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**invalidFields** | [**List&lt;ErrorFieldType&gt;**](ErrorFieldType.md) | Contains field validation errors that would prevent requests from being processed. |  [optional] |
|**merchantReference** | **String** | The value supplied by the executing user when initiating the transfer refund; may be used to link multiple transactions. |  [optional] |
|**message** | **String** | The message of the response. |  [optional] |
|**originalReference** | **String** | A PSP reference of the original fund transfer. |  [optional] |
|**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. |  [optional] |
|**resultCode** | **String** | The result code. |  [optional] |



