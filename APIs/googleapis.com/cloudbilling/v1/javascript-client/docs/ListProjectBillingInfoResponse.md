# CloudBillingApi.ListProjectBillingInfoResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | A token to retrieve the next page of results. To retrieve the next page, call &#x60;ListProjectBillingInfo&#x60; again with the &#x60;page_token&#x60; field set to this value. This field is empty if there are no more results to retrieve. | [optional] 
**projectBillingInfo** | [**[ProjectBillingInfo]**](ProjectBillingInfo.md) | A list of &#x60;ProjectBillingInfo&#x60; resources representing the projects associated with the billing account. | [optional] 


