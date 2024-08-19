

# CodeScanningAlert


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The time that the alert was created in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. |  [readonly] |
|**dismissedAt** | **OffsetDateTime** | The time that the alert was dismissed in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. |  [readonly] |
|**dismissedBy** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**dismissedReason** | **CodeScanningAlertDismissedReason** |  |  |
|**fixedAt** | **OffsetDateTime** | The time that the alert was no longer detected and was considered fixed in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. |  [optional] [readonly] |
|**htmlUrl** | **URI** | The GitHub URL of the alert resource. |  [readonly] |
|**instancesUrl** | **URI** | The REST API URL for fetching the list of instances for an alert. |  [readonly] |
|**mostRecentInstance** | [**CodeScanningAlertInstance**](CodeScanningAlertInstance.md) |  |  |
|**number** | **Integer** | The security alert number. |  [readonly] |
|**rule** | [**CodeScanningAlertRule**](CodeScanningAlertRule.md) |  |  |
|**state** | **CodeScanningAlertState** |  |  |
|**tool** | [**CodeScanningAnalysisTool**](CodeScanningAnalysisTool.md) |  |  |
|**updatedAt** | **OffsetDateTime** | The time that the alert was last updated in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. |  [optional] [readonly] |
|**url** | **URI** | The REST API URL of the alert resource. |  [readonly] |



