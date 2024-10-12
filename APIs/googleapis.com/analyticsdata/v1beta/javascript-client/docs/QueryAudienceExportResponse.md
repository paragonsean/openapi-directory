# GoogleAnalyticsDataApi.QueryAudienceExportResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audienceExport** | [**AudienceExport**](AudienceExport.md) |  | [optional] 
**audienceRows** | [**[V1betaAudienceRow]**](V1betaAudienceRow.md) | Rows for each user in an audience export. The number of rows in this response will be less than or equal to request&#39;s page size. | [optional] 
**rowCount** | **Number** | The total number of rows in the AudienceExport result. &#x60;rowCount&#x60; is independent of the number of rows returned in the response, the &#x60;limit&#x60; request parameter, and the &#x60;offset&#x60; request parameter. For example if a query returns 175 rows and includes &#x60;limit&#x60; of 50 in the API request, the response will contain &#x60;rowCount&#x60; of 175 but only 50 rows. To learn more about this pagination parameter, see [Pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination). | [optional] 


