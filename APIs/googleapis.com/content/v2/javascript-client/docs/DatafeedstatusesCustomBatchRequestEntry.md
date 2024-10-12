# ContentApiForShopping.DatafeedstatusesCustomBatchRequestEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batchId** | **Number** | An entry ID, unique within the batch request. | [optional] 
**country** | **String** | The country for which to get the datafeed status. If this parameter is provided then language must also be provided. Note that for multi-target datafeeds this parameter is required. | [optional] 
**datafeedId** | **String** | The ID of the data feed to get. | [optional] 
**language** | **String** | The language for which to get the datafeed status. If this parameter is provided then country must also be provided. Note that for multi-target datafeeds this parameter is required. | [optional] 
**merchantId** | **String** | The ID of the managing account. | [optional] 
**method** | **String** | The method of the batch entry. Acceptable values are: - \&quot;&#x60;get&#x60;\&quot;  | [optional] 


