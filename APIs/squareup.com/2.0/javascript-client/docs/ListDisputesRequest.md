# SquareConnectApi.ListDisputesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **String** | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). | [optional] 
**locationId** | **String** | The ID of the location for which to return a list of disputes. If not specified, the endpoint returns all open disputes (the dispute status is not &#x60;INQUIRY_CLOSED&#x60;, &#x60;WON&#x60;, or &#x60;LOST&#x60;) associated with all locations. | [optional] 
**states** | **[String]** | The dispute states to filter the result. If not specified, the endpoint returns all open disputes (the dispute status is not &#x60;INQUIRY_CLOSED&#x60;, &#x60;WON&#x60;, or &#x60;LOST&#x60;). | [optional] 


