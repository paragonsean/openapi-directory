# VertexAiSearchForRetailApi.GoogleCloudRetailV2alphaPredictResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributionToken** | **String** | A unique attribution token. This should be included in the UserEvent logs resulting from this recommendation, which enables accurate attribution of recommendation model performance. | [optional] 
**missingIds** | **[String]** | IDs of products in the request that were missing from the inventory. | [optional] 
**results** | [**[GoogleCloudRetailV2alphaPredictResponsePredictionResult]**](GoogleCloudRetailV2alphaPredictResponsePredictionResult.md) | A list of recommended products. The order represents the ranking (from the most relevant product to the least). | [optional] 
**validateOnly** | **Boolean** | True if the validateOnly property was set in the request. | [optional] 


