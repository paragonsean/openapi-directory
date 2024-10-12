# ManagedLabsClient.EnvironmentSettingProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurationState** | **String** | Describes the user&#39;s progress in configuring their environment setting | [optional] 
**description** | **String** | Describes the environment and its resource settings | [optional] 
**lastChanged** | **Date** | Time when the template VM was last changed. | [optional] [readonly] 
**lastPublished** | **Date** | Time when the template VM was last sent for publishing. | [optional] [readonly] 
**latestOperationResult** | [**LatestOperationResult**](LatestOperationResult.md) |  | [optional] 
**provisioningState** | **String** | The provisioning status of the resource. | [optional] 
**publishingState** | **String** | Describes the readiness of this environment setting | [optional] [readonly] 
**resourceSettings** | [**ResourceSettings**](ResourceSettings.md) |  | 
**title** | **String** | Brief title describing the environment and its resource settings | [optional] 
**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). | [optional] 



## Enum: ConfigurationStateEnum


* `NotApplicable` (value: `"NotApplicable"`)

* `Completed` (value: `"Completed"`)





## Enum: PublishingStateEnum


* `Draft` (value: `"Draft"`)

* `Publishing` (value: `"Publishing"`)

* `Published` (value: `"Published"`)

* `PublishFailed` (value: `"PublishFailed"`)

* `Scaling` (value: `"Scaling"`)




