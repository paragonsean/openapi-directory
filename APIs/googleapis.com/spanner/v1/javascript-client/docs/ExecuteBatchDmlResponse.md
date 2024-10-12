# CloudSpannerApi.ExecuteBatchDmlResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resultSets** | [**[ResultSet]**](ResultSet.md) | One ResultSet for each statement in the request that ran successfully, in the same order as the statements in the request. Each ResultSet does not contain any rows. The ResultSetStats in each ResultSet contain the number of rows modified by the statement. Only the first ResultSet in the response contains valid ResultSetMetadata. | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 


