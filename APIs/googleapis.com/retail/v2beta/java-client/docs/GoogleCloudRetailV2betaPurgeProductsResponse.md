

# GoogleCloudRetailV2betaPurgeProductsResponse

Response of the PurgeProductsRequest. If the long running operation is successfully done, then this message is returned by the google.longrunning.Operations.response field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**purgeCount** | **String** | The total count of products purged as a result of the operation. |  [optional] |
|**purgeSample** | **List&lt;String&gt;** | A sample of the product names that will be deleted. Only populated if &#x60;force&#x60; is set to false. A max of 100 names will be returned and the names are chosen at random. |  [optional] |



