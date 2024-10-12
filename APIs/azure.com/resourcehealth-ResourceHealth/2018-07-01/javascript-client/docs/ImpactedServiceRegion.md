# MicrosoftResourceHealth.ImpactedServiceRegion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**impactedRegion** | **String** | Impacted region name. | [optional] 
**impactedSubscriptions** | **[String]** | List subscription impacted by the service health event. | [optional] 
**lastUpdateTime** | **Date** | It provides the Timestamp for when the last update for the service health event. | [optional] 
**status** | **String** | Current status of event in the region. | [optional] 
**updates** | [**[Update]**](Update.md) | List of updates for given service health event. | [optional] 



## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `Resolved` (value: `"Resolved"`)




