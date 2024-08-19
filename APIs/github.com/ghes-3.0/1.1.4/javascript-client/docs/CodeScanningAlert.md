# GitHubV3RestApi.CodeScanningAlert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | The time that the alert was created in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 
**dismissedAt** | **Date** | The time that the alert was dismissed in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 
**dismissedBy** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**dismissedReason** | [**CodeScanningAlertDismissedReason**](CodeScanningAlertDismissedReason.md) |  | 
**htmlUrl** | **String** | The GitHub URL of the alert resource. | [readonly] 
**instances** | **Object** |  | [optional] 
**instancesUrl** | **String** | The REST API URL for fetching the list of instances for an alert. | [readonly] 
**mostRecentInstance** | [**CodeScanningAlertInstance**](CodeScanningAlertInstance.md) |  | 
**number** | **Number** | The security alert number. | [readonly] 
**rule** | [**CodeScanningAlertRule**](CodeScanningAlertRule.md) |  | 
**state** | [**CodeScanningAlertState**](CodeScanningAlertState.md) |  | 
**tool** | [**CodeScanningAnalysisTool**](CodeScanningAnalysisTool.md) |  | 
**url** | **String** | The REST API URL of the alert resource. | [readonly] 


