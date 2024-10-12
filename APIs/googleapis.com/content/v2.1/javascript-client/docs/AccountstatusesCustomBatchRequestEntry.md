# ContentApiForShopping.AccountstatusesCustomBatchRequestEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The ID of the (sub-)account whose status to get. | [optional] 
**batchId** | **Number** | An entry ID, unique within the batch request. | [optional] 
**destinations** | **[String]** | If set, only issues for the specified destinations are returned, otherwise only issues for the Shopping destination. | [optional] 
**merchantId** | **String** | The ID of the managing account. | [optional] 
**method** | **String** | The method of the batch entry. Acceptable values are: - \&quot;&#x60;get&#x60;\&quot;  | [optional] 


