# OpenChannelMarketApi.Ownership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | The id of the app that is owned | 
**customData** | **Object** | A custom JSON object that you can create and attach to this record | [optional] 
**date** | **Number** | The date (in millis) of when this app was owned | 
**developerId** | **String** | The id of the developer for this app | 
**expires** | **Number** | The date (in millis) of when this app ownership expires | [optional] 
**model** | [**Model**](Model.md) |  | 
**ownershipId** | **String** | The id of this ownership | 
**ownershipStatus** | **String** | The current ownership status for this app | 
**ownershipType** | **String** | The current ownership type for this app | 
**uninstallDate** | **Number** | The date (in millis) of when this app was uninstalled | [optional] 
**userId** | **String** | The id of the user that owns this app | 



## Enum: OwnershipStatusEnum


* `pending` (value: `"pending"`)

* `active` (value: `"active"`)

* `uninstalled` (value: `"uninstalled"`)

* `cancelled` (value: `"cancelled"`)





## Enum: OwnershipTypeEnum


* `full` (value: `"full"`)

* `subscription` (value: `"subscription"`)

* `trial` (value: `"trial"`)




