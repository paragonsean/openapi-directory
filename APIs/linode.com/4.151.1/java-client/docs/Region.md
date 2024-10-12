

# Region

An area where Linode services are available.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capabilities** | **List&lt;String&gt;** | A list of capabilities of this region.  |  [optional] [readonly] |
|**country** | **String** | The country where this Region resides. |  [optional] [readonly] |
|**id** | **String** | The unique ID of this Region. |  [optional] [readonly] |
|**label** | **String** | Detailed location information for this Region, including city, state or region, and country. |  [optional] [readonly] |
|**resolvers** | [**RegionResolvers**](RegionResolvers.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | This region&#39;s current operational status.  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;ok&quot; |
| OUTAGE | &quot;outage&quot; |



