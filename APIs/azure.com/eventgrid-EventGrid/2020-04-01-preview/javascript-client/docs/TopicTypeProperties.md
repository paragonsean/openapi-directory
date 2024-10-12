# EventGridManagementClient.TopicTypeProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the topic type. | [optional] 
**displayName** | **String** | Display Name for the topic type. | [optional] 
**provider** | **String** | Namespace of the provider of the topic type. | [optional] 
**provisioningState** | **String** | Provisioning state of the topic type | [optional] 
**resourceRegionType** | **String** | Region type of the resource. | [optional] 
**sourceResourceFormat** | **String** | Source resource format. | [optional] 
**supportedLocations** | **[String]** | List of locations supported by this topic type. | [optional] 



## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Canceled` (value: `"Canceled"`)

* `Failed` (value: `"Failed"`)





## Enum: ResourceRegionTypeEnum


* `RegionalResource` (value: `"RegionalResource"`)

* `GlobalResource` (value: `"GlobalResource"`)




