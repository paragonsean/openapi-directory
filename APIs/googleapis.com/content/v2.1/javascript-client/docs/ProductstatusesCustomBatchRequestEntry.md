# ContentApiForShopping.ProductstatusesCustomBatchRequestEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batchId** | **Number** | An entry ID, unique within the batch request. | [optional] 
**destinations** | **[String]** | If set, only issues for the specified destinations are returned, otherwise only issues for the Shopping destination. | [optional] 
**includeAttributes** | **Boolean** | Deprecated: Setting this field has no effect and attributes are never included. | [optional] 
**merchantId** | **String** | The ID of the managing account. | [optional] 
**method** | **String** | The method of the batch entry. Acceptable values are: - \&quot;&#x60;get&#x60;\&quot;  | [optional] 
**productId** | **String** | The ID of the product whose status to get. | [optional] 


