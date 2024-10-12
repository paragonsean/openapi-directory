# UpdateManagement.SoftwareUpdateConfigurationCollectionItemProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **Date** | Creation time of the software update configuration, which only appears in the response. | [optional] [readonly] 
**frequency** | **String** | Gets or sets the frequency of the schedule. | [optional] 
**lastModifiedTime** | **Date** | Last time software update configuration was modified, which only appears in the response. | [optional] [readonly] 
**nextRun** | **Date** | ext run time of the update. | [optional] 
**provisioningState** | **String** | Provisioning state for the software update configuration, which only appears in the response. | [optional] [readonly] 
**startTime** | **Date** | the start time of the update. | [optional] 
**updateConfiguration** | [**CollectionItemUpdateConfiguration**](CollectionItemUpdateConfiguration.md) |  | [optional] 



## Enum: FrequencyEnum


* `OneTime` (value: `"OneTime"`)

* `Day` (value: `"Day"`)

* `Hour` (value: `"Hour"`)

* `Week` (value: `"Week"`)

* `Month` (value: `"Month"`)

* `Minute` (value: `"Minute"`)




