

# CodeScanningAlertItems


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**classification** | **CodeScanningAlertClassification** |  |  |
|**createdAt** | **OffsetDateTime** | The time that the alert was created in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. |  [readonly] |
|**dismissedAt** | **OffsetDateTime** | The time that the alert was dismissed in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. |  [readonly] |
|**dismissedBy** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**dismissedReason** | **CodeScanningAlertDismissedReason** |  |  |
|**htmlUrl** | **URI** | The GitHub URL of the alert resource. |  [readonly] |
|**instance** | [**CodeScanningAlertInstance**](CodeScanningAlertInstance.md) |  |  |
|**number** | **Integer** | The security alert number. |  [readonly] |
|**rule** | [**CodeScanningAlertRuleSummary**](CodeScanningAlertRuleSummary.md) |  |  |
|**state** | **CodeScanningAlertState** |  |  |
|**tool** | [**CodeScanningAnalysisTool**](CodeScanningAnalysisTool.md) |  |  |
|**url** | **URI** | The REST API URL of the alert resource. |  [readonly] |



