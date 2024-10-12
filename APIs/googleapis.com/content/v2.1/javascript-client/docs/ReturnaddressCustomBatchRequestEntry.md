# ContentApiForShopping.ReturnaddressCustomBatchRequestEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batchId** | **Number** | An entry ID, unique within the batch request. | [optional] 
**merchantId** | **String** | The Merchant Center account ID. | [optional] 
**method** | **String** | Method of the batch request entry. Acceptable values are: - \&quot;&#x60;delete&#x60;\&quot; - \&quot;&#x60;get&#x60;\&quot; - \&quot;&#x60;insert&#x60;\&quot;  | [optional] 
**returnAddress** | [**ReturnAddress**](ReturnAddress.md) |  | [optional] 
**returnAddressId** | **String** | The return address ID. This should be set only if the method is &#x60;delete&#x60; or &#x60;get&#x60;. | [optional] 


