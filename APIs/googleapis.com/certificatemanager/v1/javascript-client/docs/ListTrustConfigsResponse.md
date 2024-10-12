# CertificateManagerApi.ListTrustConfigsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | If there might be more results than those appearing in this response, then &#x60;next_page_token&#x60; is included. To get the next set of results, call this method again using the value of &#x60;next_page_token&#x60; as &#x60;page_token&#x60;. | [optional] 
**trustConfigs** | [**[TrustConfig]**](TrustConfig.md) | A list of TrustConfigs for the parent resource. | [optional] 
**unreachable** | **[String]** | Locations that could not be reached. | [optional] 


