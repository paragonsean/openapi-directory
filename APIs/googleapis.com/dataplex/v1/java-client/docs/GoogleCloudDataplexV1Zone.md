

# GoogleCloudDataplexV1Zone

A zone represents a logical group of related assets within a lake. A zone can be used to map to organizational structure or represent stages of data readiness from raw to curated. It provides managing behavior that is shared or inherited by all contained assets.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetStatus** | [**GoogleCloudDataplexV1AssetStatus**](GoogleCloudDataplexV1AssetStatus.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time when the zone was created. |  [optional] [readonly] |
|**description** | **String** | Optional. Description of the zone. |  [optional] |
|**discoverySpec** | [**GoogleCloudDataplexV1ZoneDiscoverySpec**](GoogleCloudDataplexV1ZoneDiscoverySpec.md) |  |  [optional] |
|**displayName** | **String** | Optional. User friendly display name. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. User defined labels for the zone. |  [optional] |
|**name** | **String** | Output only. The relative resource name of the zone, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}. |  [optional] [readonly] |
|**resourceSpec** | [**GoogleCloudDataplexV1ZoneResourceSpec**](GoogleCloudDataplexV1ZoneResourceSpec.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Current state of the zone. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Immutable. The type of the zone. |  [optional] |
|**uid** | **String** | Output only. System generated globally unique ID for the zone. This ID will be different if the zone is deleted and re-created with the same name. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time when the zone was last updated. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| CREATING | &quot;CREATING&quot; |
| DELETING | &quot;DELETING&quot; |
| ACTION_REQUIRED | &quot;ACTION_REQUIRED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| RAW | &quot;RAW&quot; |
| CURATED | &quot;CURATED&quot; |



