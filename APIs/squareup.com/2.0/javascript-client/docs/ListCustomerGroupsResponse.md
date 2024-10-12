# SquareConnectApi.ListCustomerGroupsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **String** | A pagination cursor to retrieve the next set of results for your original query to the endpoint. This value is present only if the request succeeded and additional results are available.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). | [optional] 
**errors** | [**[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 
**groups** | [**[CustomerGroup]**](CustomerGroup.md) | A list of customer groups belonging to the current seller. | [optional] 


