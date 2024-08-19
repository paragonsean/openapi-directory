

# UpdateGeofenceCollectionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Updates the description for the geofence collection. |  [optional] |
|**pricingPlan** | [**PricingPlanEnum**](#PricingPlanEnum) | No longer used. If included, the only allowed value is &lt;code&gt;RequestBasedUsage&lt;/code&gt;. |  [optional] |
|**pricingPlanDataSource** | **String** | This parameter is no longer used. |  [optional] |



## Enum: PricingPlanEnum

| Name | Value |
|---- | -----|
| REQUEST_BASED_USAGE | &quot;RequestBasedUsage&quot; |
| MOBILE_ASSET_TRACKING | &quot;MobileAssetTracking&quot; |
| MOBILE_ASSET_MANAGEMENT | &quot;MobileAssetManagement&quot; |



