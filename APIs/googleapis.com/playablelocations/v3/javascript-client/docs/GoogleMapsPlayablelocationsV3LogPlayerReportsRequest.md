# PlayableLocationsApi.GoogleMapsPlayablelocationsV3LogPlayerReportsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientInfo** | [**GoogleMapsUnityClientInfo**](GoogleMapsUnityClientInfo.md) |  | [optional] 
**playerReports** | [**[GoogleMapsPlayablelocationsV3PlayerReport]**](GoogleMapsPlayablelocationsV3PlayerReport.md) | Required. Player reports. The maximum number of player reports that you can log at once is 50. | [optional] 
**requestId** | **String** | Required. A string that uniquely identifies the log player reports request. This allows you to detect duplicate requests. We recommend that you use UUIDs for this value. The value must not exceed 50 characters. You should reuse the &#x60;request_id&#x60; only when retrying a request in the case of a failure. In that case, the request must be identical to the one that failed. | [optional] 


