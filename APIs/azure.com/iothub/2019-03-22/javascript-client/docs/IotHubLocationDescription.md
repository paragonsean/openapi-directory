# IotHubClient.IotHubLocationDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **String** | The name of the Azure region | [optional] 
**role** | **String** | The role of the region, can be either primary or secondary. The primary region is where the IoT hub is currently provisioned. The secondary region is the Azure disaster recovery (DR) paired region and also the region where the IoT hub can failover to. | [optional] 



## Enum: RoleEnum


* `primary` (value: `"primary"`)

* `secondary` (value: `"secondary"`)




