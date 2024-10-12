

# ListDeviceCodesRequest



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information. |  [optional] |
|**locationId** | **String** | If specified, only returns DeviceCodes of the specified location. Returns DeviceCodes of all locations if empty. |  [optional] |
|**productType** | **String** | If specified, only returns DeviceCodes targeting the specified product type. Returns DeviceCodes of all product types if empty. |  [optional] |
|**status** | **List&lt;String&gt;** | If specified, returns DeviceCodes with the specified statuses. Returns DeviceCodes of status &#x60;PAIRED&#x60; and &#x60;UNPAIRED&#x60; if empty. |  [optional] |



