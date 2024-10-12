# YouTubeAnalyticsApi.QueryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columnHeaders** | [**[ResultTableColumnHeader]**](ResultTableColumnHeader.md) | This value specifies information about the data returned in the &#x60;rows&#x60; fields. Each item in the &#x60;columnHeaders&#x60; list identifies a field returned in the &#x60;rows&#x60; value, which contains a list of comma-delimited data. The &#x60;columnHeaders&#x60; list will begin with the dimensions specified in the API request, which will be followed by the metrics specified in the API request. The order of both dimensions and metrics will match the ordering in the API request. For example, if the API request contains the parameters &#x60;dimensions&#x3D;ageGroup,gender&amp;metrics&#x3D;viewerPercentage&#x60;, the API response will return columns in this order: &#x60;ageGroup&#x60;, &#x60;gender&#x60;, &#x60;viewerPercentage&#x60;. | [optional] 
**errors** | [**Errors**](Errors.md) |  | [optional] 
**kind** | **String** | This value specifies the type of data included in the API response. For the query method, the kind property value will be &#x60;youtubeAnalytics#resultTable&#x60;. | [optional] 
**rows** | **[[Object]]** | The list contains all rows of the result table. Each item in the list is an array that contains comma-delimited data corresponding to a single row of data. The order of the comma-delimited data fields will match the order of the columns listed in the &#x60;columnHeaders&#x60; field. If no data is available for the given query, the &#x60;rows&#x60; element will be omitted from the response. The response for a query with the &#x60;day&#x60; dimension will not contain rows for the most recent days. | [optional] 


