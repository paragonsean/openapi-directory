

# QueuedResponse

The response received after a [render request](#render-asset) is submitted. The render task is queued for rendering and a unique render id is returned.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | &#x60;Created&#x60;, &#x60;Bad Request&#x60; or an error message. |  |
|**response** | [**QueuedResponseData**](QueuedResponseData.md) |  |  |
|**success** | **Boolean** | &#x60;true&#x60; if successfully queued, else &#x60;false&#x60;. |  |



