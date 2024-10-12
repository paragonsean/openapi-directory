

# ListDeviceCodesResponse



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | A pagination cursor to retrieve the next set of results for your original query to the endpoint. This value is present only if the request succeeded and additional results are available.  See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information. |  [optional] |
|**deviceCodes** | [**List&lt;DeviceCode&gt;**](DeviceCode.md) | The queried DeviceCode. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |



