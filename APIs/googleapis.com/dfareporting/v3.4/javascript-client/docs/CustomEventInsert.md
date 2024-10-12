# CampaignManager360Api.CustomEventInsert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmDimensions** | [**CampaignManagerIds**](CampaignManagerIds.md) |  | [optional] 
**dv3Dimensions** | [**DV3Ids**](DV3Ids.md) |  | [optional] 
**insertEventType** | **String** | The type of event to insert. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#customEventInsert\&quot;. | [optional] 
**matchId** | **String** | The match ID field. A match ID is your own first-party identifier that has been synced with Google using the match ID feature in Floodlight. This field is mutually exclusive with mobileDeviceId, and at least one of the two fields is required. | [optional] 
**mobileDeviceId** | **String** | The mobile device ID. This field is mutually exclusive with matchId, and at least one of the two fields is required. | [optional] 



## Enum: InsertEventTypeEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `IMPRESSION` (value: `"IMPRESSION"`)

* `CLICK` (value: `"CLICK"`)




