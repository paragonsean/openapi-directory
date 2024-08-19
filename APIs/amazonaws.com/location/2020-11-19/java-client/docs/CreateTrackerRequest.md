

# CreateTrackerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | An optional description for the tracker resource. |  [optional] |
|**eventBridgeEnabled** | **Boolean** | &lt;p&gt;Whether to enable position &lt;code&gt;UPDATE&lt;/code&gt; events from this tracker to be sent to EventBridge.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You do not need enable this feature to get &lt;code&gt;ENTER&lt;/code&gt; and &lt;code&gt;EXIT&lt;/code&gt; events for geofences with this tracker. Those events are always sent to EventBridge.&lt;/p&gt; &lt;/note&gt; |  [optional] |
|**kmsKeyId** | **String** | A key identifier for an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html\&quot;&gt;Amazon Web Services KMS customer managed key&lt;/a&gt;. Enter a key ID, key ARN, alias name, or alias ARN. |  [optional] |
|**positionFiltering** | [**PositionFilteringEnum**](#PositionFilteringEnum) | &lt;p&gt;Specifies the position filtering for the tracker resource.&lt;/p&gt; &lt;p&gt;Valid values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TimeBased&lt;/code&gt; - Location updates are evaluated against linked geofence collections, but not every location update is stored. If your update frequency is more often than 30 seconds, only one update per 30 seconds is stored for each unique device ID. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DistanceBased&lt;/code&gt; - If the device has moved less than 30 m (98.4 ft), location updates are ignored. Location updates within this area are neither evaluated against linked geofence collections, nor stored. This helps control costs by reducing the number of geofence evaluations and historical device positions to paginate through. Distance-based filtering can also reduce the effects of GPS noise when displaying device trajectories on a map. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AccuracyBased&lt;/code&gt; - If the device has moved less than the measured accuracy, location updates are ignored. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is ignored if the device has moved less than 15 m. Ignored location updates are neither evaluated against linked geofence collections, nor stored. This can reduce the effects of GPS noise when displaying device trajectories on a map, and can help control your costs by reducing the number of geofence evaluations. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This field is optional. If not specified, the default value is &lt;code&gt;TimeBased&lt;/code&gt;.&lt;/p&gt; |  [optional] |
|**pricingPlan** | [**PricingPlanEnum**](#PricingPlanEnum) | No longer used. If included, the only allowed value is &lt;code&gt;RequestBasedUsage&lt;/code&gt;. |  [optional] |
|**pricingPlanDataSource** | **String** | This parameter is no longer used. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | &lt;p&gt;Applies one or more tags to the tracker resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.&lt;/p&gt; &lt;p&gt;Format: &lt;code&gt;\&quot;key\&quot; : \&quot;value\&quot;&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Restrictions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Maximum 50 tags per resource&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Each resource tag must be unique with a maximum of one value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Maximum key length: 128 Unicode characters in UTF-8&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Maximum value length: 256 Unicode characters in UTF-8&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - &#x3D; . _ : / @. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot use \&quot;aws:\&quot; as a prefix for a key.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**trackerName** | **String** | &lt;p&gt;The name for the tracker resource.&lt;/p&gt; &lt;p&gt;Requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Contain only alphanumeric characters (A-Z, a-z, 0-9) , hyphens (-), periods (.), and underscores (_).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be a unique tracker resource name.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;No spaces allowed. For example, &lt;code&gt;ExampleTracker&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |



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



