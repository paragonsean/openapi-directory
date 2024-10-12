

# ChaosReport

Contains detailed Chaos report. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chaosParameters** | [**ChaosParameters**](ChaosParameters.md) |  |  [optional] |
|**continuationToken** | **String** | The continuation token parameter is used to obtain next set of results. The continuation token is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token is not included in the response. |  [optional] |
|**history** | [**List&lt;ChaosEventWrapper&gt;**](ChaosEventWrapper.md) | An list of Chaos events that were generated during the time range passed into the GetChaosReport API call. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of the Chaos run.  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| RUNNING | &quot;Running&quot; |
| STOPPED | &quot;Stopped&quot; |



