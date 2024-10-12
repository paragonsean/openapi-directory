# DisplayVideo360Api.LocationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiserId** | **String** | Required. Immutable. The unique ID of the advertiser the location list belongs to. | [optional] 
**displayName** | **String** | Required. The display name of the location list. Must be UTF-8 encoded with a maximum size of 240 bytes. | [optional] 
**locationListId** | **String** | Output only. The unique ID of the location list. Assigned by the system. | [optional] [readonly] 
**locationType** | **String** | Required. Immutable. The type of location. All locations in the list will share this type. | [optional] 
**name** | **String** | Output only. The resource name of the location list. | [optional] [readonly] 



## Enum: LocationTypeEnum


* `UNSPECIFIED` (value: `"TARGETING_LOCATION_TYPE_UNSPECIFIED"`)

* `PROXIMITY` (value: `"TARGETING_LOCATION_TYPE_PROXIMITY"`)

* `REGIONAL` (value: `"TARGETING_LOCATION_TYPE_REGIONAL"`)




