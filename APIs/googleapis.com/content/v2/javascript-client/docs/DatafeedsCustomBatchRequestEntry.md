# ContentApiForShopping.DatafeedsCustomBatchRequestEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batchId** | **Number** | An entry ID, unique within the batch request. | [optional] 
**datafeed** | [**Datafeed**](Datafeed.md) |  | [optional] 
**datafeedId** | **String** | The ID of the data feed to get, delete or fetch. | [optional] 
**merchantId** | **String** | The ID of the managing account. | [optional] 
**method** | **String** | The method of the batch entry. Acceptable values are: - \&quot;&#x60;delete&#x60;\&quot; - \&quot;&#x60;fetchNow&#x60;\&quot; - \&quot;&#x60;get&#x60;\&quot; - \&quot;&#x60;insert&#x60;\&quot; - \&quot;&#x60;update&#x60;\&quot;  | [optional] 


