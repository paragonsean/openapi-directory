# AppVeyorRestApi.UserAccountSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failedBuildNotification** | [**BuildNotificationFrequency**](BuildNotificationFrequency.md) |  | 
**failedDeploymentNotification** | [**DeploymentNotificationFrequency**](DeploymentNotificationFrequency.md) |  | 
**notifyWhenBuildStatusChangedOnly** | **Boolean** | Note that this value is &#x60;true&#x60; on user creation, but behaves as &#x60;false&#x60; when not specified on update.  | [optional] [default to false]
**notifyWhenDeploymentStatusChangedOnly** | **Boolean** | Note that this value is &#x60;true&#x60; on user creation, but behaves as &#x60;false&#x60; when not specified on update.  | [optional] [default to false]
**successfulBuildNotification** | [**BuildNotificationFrequency**](BuildNotificationFrequency.md) |  | 
**successfulDeploymentNotification** | [**DeploymentNotificationFrequency**](DeploymentNotificationFrequency.md) |  | 


