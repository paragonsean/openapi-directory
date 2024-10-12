

# OrganizationSecretScanningAlert


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The time that the alert was created in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. |  [optional] [readonly] |
|**htmlUrl** | **URI** | The GitHub URL of the alert resource. |  [optional] [readonly] |
|**locationsUrl** | **URI** | The REST API URL of the code locations for this alert. |  [optional] |
|**number** | **Integer** | The security alert number. |  [optional] [readonly] |
|**repository** | [**SimpleRepository**](SimpleRepository.md) |  |  [optional] |
|**resolution** | **SecretScanningAlertResolution** |  |  [optional] |
|**resolvedAt** | **OffsetDateTime** | The time that the alert was resolved in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. |  [optional] |
|**resolvedBy** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  [optional] |
|**secret** | **String** | The secret that was detected. |  [optional] |
|**secretType** | **String** | The type of secret that secret scanning detected. |  [optional] |
|**state** | **SecretScanningAlertState** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** | The time that the alert was last updated in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. |  [optional] [readonly] |
|**url** | **URI** | The REST API URL of the alert resource. |  [optional] [readonly] |



