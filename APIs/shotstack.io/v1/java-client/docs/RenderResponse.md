

# RenderResponse

The response received after a [render status request](#get-render-status) is submitted. The response includes  details about status of a render and the output URL.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | &#x60;OK&#x60; or an error message. |  |
|**response** | [**RenderResponseData**](RenderResponseData.md) |  |  |
|**success** | **Boolean** | &#x60;true&#x60; if status available, else &#x60;false&#x60;. |  |



