

# GoogleAdsSearchads360V0ResourcesGeoTargetConstant

A geo target constant.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canonicalName** | **String** | Output only. The fully qualified English name, consisting of the target&#39;s name and that of its parent and country. |  [optional] [readonly] |
|**countryCode** | **String** | Output only. The ISO-3166-1 alpha-2 country code that is associated with the target. |  [optional] [readonly] |
|**id** | **String** | Output only. The ID of the geo target constant. |  [optional] [readonly] |
|**name** | **String** | Output only. Geo target constant English name. |  [optional] [readonly] |
|**parentGeoTarget** | **String** | Output only. The resource name of the parent geo target constant. Geo target constant resource names have the form: &#x60;geoTargetConstants/{parent_geo_target_constant_id}&#x60; |  [optional] [readonly] |
|**resourceName** | **String** | Output only. The resource name of the geo target constant. Geo target constant resource names have the form: &#x60;geoTargetConstants/{geo_target_constant_id}&#x60; |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. Geo target constant status. |  [optional] [readonly] |
|**targetType** | **String** | Output only. Geo target constant target type. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| REMOVAL_PLANNED | &quot;REMOVAL_PLANNED&quot; |



