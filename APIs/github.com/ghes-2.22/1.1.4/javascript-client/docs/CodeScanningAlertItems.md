# GitHubV3RestApi.CodeScanningAlertItems

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | [**CodeScanningAlertClassification**](CodeScanningAlertClassification.md) |  | 
**createdAt** | **Date** | The time that the alert was created in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 
**dismissedAt** | **Date** | The time that the alert was dismissed in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 
**dismissedBy** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**dismissedReason** | [**CodeScanningAlertDismissedReason**](CodeScanningAlertDismissedReason.md) |  | 
**htmlUrl** | **String** | The GitHub URL of the alert resource. | [readonly] 
**instance** | [**CodeScanningAlertInstance**](CodeScanningAlertInstance.md) |  | 
**number** | **Number** | The security alert number. | [readonly] 
**rule** | [**CodeScanningAlertRuleSummary**](CodeScanningAlertRuleSummary.md) |  | 
**state** | [**CodeScanningAlertState**](CodeScanningAlertState.md) |  | 
**tool** | [**CodeScanningAnalysisTool**](CodeScanningAnalysisTool.md) |  | 
**url** | **String** | The REST API URL of the alert resource. | [readonly] 


