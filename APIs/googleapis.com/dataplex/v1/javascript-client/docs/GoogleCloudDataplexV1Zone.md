# CloudDataplexApi.GoogleCloudDataplexV1Zone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetStatus** | [**GoogleCloudDataplexV1AssetStatus**](GoogleCloudDataplexV1AssetStatus.md) |  | [optional] 
**createTime** | **String** | Output only. The time when the zone was created. | [optional] [readonly] 
**description** | **String** | Optional. Description of the zone. | [optional] 
**discoverySpec** | [**GoogleCloudDataplexV1ZoneDiscoverySpec**](GoogleCloudDataplexV1ZoneDiscoverySpec.md) |  | [optional] 
**displayName** | **String** | Optional. User friendly display name. | [optional] 
**labels** | **{String: String}** | Optional. User defined labels for the zone. | [optional] 
**name** | **String** | Output only. The relative resource name of the zone, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}. | [optional] [readonly] 
**resourceSpec** | [**GoogleCloudDataplexV1ZoneResourceSpec**](GoogleCloudDataplexV1ZoneResourceSpec.md) |  | [optional] 
**state** | **String** | Output only. Current state of the zone. | [optional] [readonly] 
**type** | **String** | Required. Immutable. The type of the zone. | [optional] 
**uid** | **String** | Output only. System generated globally unique ID for the zone. This ID will be different if the zone is deleted and re-created with the same name. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the zone was last updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `CREATING` (value: `"CREATING"`)

* `DELETING` (value: `"DELETING"`)

* `ACTION_REQUIRED` (value: `"ACTION_REQUIRED"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `RAW` (value: `"RAW"`)

* `CURATED` (value: `"CURATED"`)




