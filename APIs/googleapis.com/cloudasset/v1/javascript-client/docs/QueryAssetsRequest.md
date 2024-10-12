# CloudAssetApi.QueryAssetsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobReference** | **String** | Optional. Reference to the query job, which is from the &#x60;QueryAssetsResponse&#x60; of previous &#x60;QueryAssets&#x60; call. | [optional] 
**outputConfig** | [**QueryAssetsOutputConfig**](QueryAssetsOutputConfig.md) |  | [optional] 
**pageSize** | **Number** | Optional. The maximum number of rows to return in the results. Responses are limited to 10 MB and 1000 rows. By default, the maximum row count is 1000. When the byte or row count limit is reached, the rest of the query results will be paginated. The field will be ignored when [output_config] is specified. | [optional] 
**pageToken** | **String** | Optional. A page token received from previous &#x60;QueryAssets&#x60;. The field will be ignored when [output_config] is specified. | [optional] 
**readTime** | **String** | Optional. Queries cloud assets as they appeared at the specified point in time. | [optional] 
**readTimeWindow** | [**TimeWindow**](TimeWindow.md) |  | [optional] 
**statement** | **String** | Optional. A SQL statement that&#39;s compatible with [BigQuery SQL](https://cloud.google.com/bigquery/docs/introduction-sql). | [optional] 
**timeout** | **String** | Optional. Specifies the maximum amount of time that the client is willing to wait for the query to complete. By default, this limit is 5 min for the first query, and 1 minute for the following queries. If the query is complete, the &#x60;done&#x60; field in the &#x60;QueryAssetsResponse&#x60; is true, otherwise false. Like BigQuery [jobs.query API](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query#queryrequest) The call is not guaranteed to wait for the specified timeout; it typically returns after around 200 seconds (200,000 milliseconds), even if the query is not complete. The field will be ignored when [output_config] is specified. | [optional] 


