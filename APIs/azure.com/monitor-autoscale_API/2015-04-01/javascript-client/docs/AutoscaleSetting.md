# MonitorManagementClient.AutoscaleSetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | the enabled flag. Specifies whether automatic scaling is enabled for the resource. The default value is &#39;true&#39;. | [optional] [default to true]
**name** | **String** | the name of the autoscale setting. | [optional] 
**notifications** | [**[AutoscaleNotification]**](AutoscaleNotification.md) | the collection of notifications. | [optional] 
**profiles** | [**[AutoscaleProfile]**](AutoscaleProfile.md) | the collection of automatic scaling profiles that specify different scaling parameters for different time periods. A maximum of 20 profiles can be specified. | 
**targetResourceUri** | **String** | the resource identifier of the resource that the autoscale setting should be added to. | [optional] 


