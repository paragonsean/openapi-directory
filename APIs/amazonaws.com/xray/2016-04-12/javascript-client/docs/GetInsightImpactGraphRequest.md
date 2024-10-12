# AwsXRay.GetInsightImpactGraphRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insightId** | **String** | The insight&#39;s unique identifier. Use the GetInsightSummaries action to retrieve an InsightId. | 
**startTime** | **Date** | The estimated start time of the insight, in Unix time seconds. The StartTime is inclusive of the value provided and can&#39;t be more than 30 days old. | 
**endTime** | **Date** | The estimated end time of the insight, in Unix time seconds. The EndTime is exclusive of the value provided. The time range between the start time and end time can&#39;t be more than six hours.  | 
**nextToken** | **String** | Specify the pagination token returned by a previous request to retrieve the next page of results.  | [optional] 


