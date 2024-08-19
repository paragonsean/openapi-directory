

# UpdateMapRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configurationUpdate** | [**UpdateMapRequestConfigurationUpdate**](UpdateMapRequestConfigurationUpdate.md) |  |  [optional] |
|**description** | **String** | Updates the description for the map resource. |  [optional] |
|**pricingPlan** | [**PricingPlanEnum**](#PricingPlanEnum) | No longer used. If included, the only allowed value is &lt;code&gt;RequestBasedUsage&lt;/code&gt;. |  [optional] |



## Enum: PricingPlanEnum

| Name | Value |
|---- | -----|
| REQUEST_BASED_USAGE | &quot;RequestBasedUsage&quot; |
| MOBILE_ASSET_TRACKING | &quot;MobileAssetTracking&quot; |
| MOBILE_ASSET_MANAGEMENT | &quot;MobileAssetManagement&quot; |



