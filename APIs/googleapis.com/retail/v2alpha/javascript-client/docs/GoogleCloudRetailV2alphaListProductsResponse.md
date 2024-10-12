# VertexAiSearchForRetailApi.GoogleCloudRetailV2alphaListProductsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | A token that can be sent as ListProductsRequest.page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 
**products** | [**[GoogleCloudRetailV2alphaProduct]**](GoogleCloudRetailV2alphaProduct.md) | The Products. | [optional] 
**totalSize** | **Number** | The total count of matched Products irrespective of pagination. The total number of Products returned by pagination may be less than the total_size that matches. This field is ignored if ListProductsRequest.require_total_size is not set or ListProductsRequest.page_token is not empty. | [optional] 


