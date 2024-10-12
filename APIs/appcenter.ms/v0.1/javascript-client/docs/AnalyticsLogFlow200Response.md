# AppCenterClient.AnalyticsLogFlow200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exceededMaxLimit** | **Boolean** | indicates if the number of available logs are more than the max allowed return limit(100). | [optional] 
**lastReceivedLogTimestamp** | **Date** | the timestamp of the last log received. This value can be used as the start time parameter in the consecutive API call. | [optional] 
**logs** | [**[AnalyticsLogFlow200ResponseLogsInner]**](AnalyticsLogFlow200ResponseLogsInner.md) | the list of logs | 


