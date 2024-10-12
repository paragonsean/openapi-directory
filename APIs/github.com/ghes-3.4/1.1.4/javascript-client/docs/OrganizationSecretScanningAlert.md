# GitHubV3RestApi.OrganizationSecretScanningAlert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | The time that the alert was created in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] [readonly] 
**htmlUrl** | **String** | The GitHub URL of the alert resource. | [optional] [readonly] 
**locationsUrl** | **String** | The REST API URL of the code locations for this alert. | [optional] 
**number** | **Number** | The security alert number. | [optional] [readonly] 
**repository** | [**SimpleRepository**](SimpleRepository.md) |  | [optional] 
**resolution** | [**SecretScanningAlertResolution**](SecretScanningAlertResolution.md) |  | [optional] 
**resolvedAt** | **Date** | The time that the alert was resolved in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
**resolvedBy** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**secret** | **String** | The secret that was detected. | [optional] 
**secretType** | **String** | The type of secret that secret scanning detected. | [optional] 
**state** | [**SecretScanningAlertState**](SecretScanningAlertState.md) |  | [optional] 
**updatedAt** | **Date** | The time that the alert was last updated in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] [readonly] 
**url** | **String** | The REST API URL of the alert resource. | [optional] [readonly] 


