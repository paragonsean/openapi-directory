

# SearchUserActivityRequest

The request to fetch User Report from Reporting API `userActivity:get` call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityTypes** | [**List&lt;ActivityTypesEnum&gt;**](#List&lt;ActivityTypesEnum&gt;) | Set of all activity types being requested. Only acvities matching these types will be returned in the response. If empty, all activies will be returned. |  [optional] |
|**dateRange** | [**DateRange**](DateRange.md) |  |  [optional] |
|**pageSize** | **Integer** | Page size is for paging and specifies the maximum number of returned rows. Page size should be &gt; 0. If the value is 0 or if the field isn&#39;t specified, the request returns the default of 1000 rows per page. |  [optional] |
|**pageToken** | **String** | A continuation token to get the next page of the results. Adding this to the request will return the rows after the pageToken. The pageToken should be the value returned in the nextPageToken parameter in the response to the [SearchUserActivityRequest](#SearchUserActivityRequest) request. |  [optional] |
|**user** | [**User**](User.md) |  |  [optional] |
|**viewId** | **String** | Required. The Analytics [view ID](https://support.google.com/analytics/answer/1009618) from which to retrieve data. Every [SearchUserActivityRequest](#SearchUserActivityRequest) must contain the &#x60;viewId&#x60;. |  [optional] |



## Enum: List&lt;ActivityTypesEnum&gt;

| Name | Value |
|---- | -----|
| ACTIVITY_TYPE_UNSPECIFIED | &quot;ACTIVITY_TYPE_UNSPECIFIED&quot; |
| PAGEVIEW | &quot;PAGEVIEW&quot; |
| SCREENVIEW | &quot;SCREENVIEW&quot; |
| GOAL | &quot;GOAL&quot; |
| ECOMMERCE | &quot;ECOMMERCE&quot; |
| EVENT | &quot;EVENT&quot; |



