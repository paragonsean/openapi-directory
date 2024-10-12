# AwsXRay.GetInsightSummariesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**states** | [**[InsightState]**](InsightState.md) | The list of insight states.  | [optional] 
**groupARN** | **String** | The Amazon Resource Name (ARN) of the group. Required if the GroupName isn&#39;t provided. | [optional] 
**groupName** | **String** | The name of the group. Required if the GroupARN isn&#39;t provided. | [optional] 
**startTime** | **Date** | The beginning of the time frame in which the insights started. The start time can&#39;t be more than 30 days old. | 
**endTime** | **Date** | The end of the time frame in which the insights ended. The end time can&#39;t be more than 30 days old. | 
**maxResults** | **Number** | The maximum number of results to display. | [optional] 
**nextToken** | **String** | Pagination token. | [optional] 


