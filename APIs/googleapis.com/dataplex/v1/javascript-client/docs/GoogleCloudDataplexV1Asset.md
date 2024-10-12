# CloudDataplexApi.GoogleCloudDataplexV1Asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when the asset was created. | [optional] [readonly] 
**description** | **String** | Optional. Description of the asset. | [optional] 
**discoverySpec** | [**GoogleCloudDataplexV1AssetDiscoverySpec**](GoogleCloudDataplexV1AssetDiscoverySpec.md) |  | [optional] 
**discoveryStatus** | [**GoogleCloudDataplexV1AssetDiscoveryStatus**](GoogleCloudDataplexV1AssetDiscoveryStatus.md) |  | [optional] 
**displayName** | **String** | Optional. User friendly display name. | [optional] 
**labels** | **{String: String}** | Optional. User defined labels for the asset. | [optional] 
**name** | **String** | Output only. The relative resource name of the asset, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}. | [optional] [readonly] 
**resourceSpec** | [**GoogleCloudDataplexV1AssetResourceSpec**](GoogleCloudDataplexV1AssetResourceSpec.md) |  | [optional] 
**resourceStatus** | [**GoogleCloudDataplexV1AssetResourceStatus**](GoogleCloudDataplexV1AssetResourceStatus.md) |  | [optional] 
**securityStatus** | [**GoogleCloudDataplexV1AssetSecurityStatus**](GoogleCloudDataplexV1AssetSecurityStatus.md) |  | [optional] 
**state** | **String** | Output only. Current state of the asset. | [optional] [readonly] 
**uid** | **String** | Output only. System generated globally unique ID for the asset. This ID will be different if the asset is deleted and re-created with the same name. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the asset was last updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `CREATING` (value: `"CREATING"`)

* `DELETING` (value: `"DELETING"`)

* `ACTION_REQUIRED` (value: `"ACTION_REQUIRED"`)




