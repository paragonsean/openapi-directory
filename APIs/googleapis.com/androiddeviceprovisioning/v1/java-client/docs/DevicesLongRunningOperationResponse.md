

# DevicesLongRunningOperationResponse

Tracks the status of a long-running operation to claim, unclaim, or attach metadata to devices. To learn more, read [Long‑running batch operations](/zero-touch/guides/how-it-works#operations).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**perDeviceStatus** | [**List&lt;OperationPerDevice&gt;**](OperationPerDevice.md) | The processing status for each device in the operation. One &#x60;PerDeviceStatus&#x60; per device. The list order matches the items in the original request. |  [optional] |
|**successCount** | **Integer** | A summary of how many items in the operation the server processed successfully. Updated as the operation progresses. |  [optional] |



