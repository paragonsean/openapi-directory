

# UpdateTrackerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Updates the description for the tracker resource. |  [optional] |
|**eventBridgeEnabled** | **Boolean** | &lt;p&gt;Whether to enable position &lt;code&gt;UPDATE&lt;/code&gt; events from this tracker to be sent to EventBridge.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You do not need enable this feature to get &lt;code&gt;ENTER&lt;/code&gt; and &lt;code&gt;EXIT&lt;/code&gt; events for geofences with this tracker. Those events are always sent to EventBridge.&lt;/p&gt; &lt;/note&gt; |  [optional] |
|**positionFiltering** | [**PositionFilteringEnum**](#PositionFilteringEnum) | &lt;p&gt;Updates the position filtering for the tracker resource.&lt;/p&gt; &lt;p&gt;Valid values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TimeBased&lt;/code&gt; - Location updates are evaluated against linked geofence collections, but not every location update is stored. If your update frequency is more often than 30 seconds, only one update per 30 seconds is stored for each unique device ID. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DistanceBased&lt;/code&gt; - If the device has moved less than 30 m (98.4 ft), location updates are ignored. Location updates within this distance are neither evaluated against linked geofence collections, nor stored. This helps control costs by reducing the number of geofence evaluations and historical device positions to paginate through. Distance-based filtering can also reduce the effects of GPS noise when displaying device trajectories on a map. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AccuracyBased&lt;/code&gt; - If the device has moved less than the measured accuracy, location updates are ignored. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is ignored if the device has moved less than 15 m. Ignored location updates are neither evaluated against linked geofence collections, nor stored. This helps educe the effects of GPS noise when displaying device trajectories on a map, and can help control costs by reducing the number of geofence evaluations. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**pricingPlan** | [**PricingPlanEnum**](#PricingPlanEnum) | No longer used. If included, the only allowed value is &lt;code&gt;RequestBasedUsage&lt;/code&gt;. |  [optional] |
|**pricingPlanDataSource** | **String** | This parameter is no longer used. |  [optional] |



## Enum: PositionFilteringEnum

| Name | Value |
|---- | -----|
| TIME_BASED | &quot;TimeBased&quot; |
| DISTANCE_BASED | &quot;DistanceBased&quot; |
| ACCURACY_BASED | &quot;AccuracyBased&quot; |



## Enum: PricingPlanEnum

| Name | Value |
|---- | -----|
| REQUEST_BASED_USAGE | &quot;RequestBasedUsage&quot; |
| MOBILE_ASSET_TRACKING | &quot;MobileAssetTracking&quot; |
| MOBILE_ASSET_MANAGEMENT | &quot;MobileAssetManagement&quot; |



