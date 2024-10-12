

# CreateMapRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_configuration** | [**CreateMapRequestConfiguration**](CreateMapRequestConfiguration.md) |  |  |
|**description** | **String** | An optional description for the map resource. |  [optional] |
|**mapName** | **String** | &lt;p&gt;The name for the map resource.&lt;/p&gt; &lt;p&gt;Requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be a unique map resource name. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;No spaces allowed. For example, &lt;code&gt;ExampleMap&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |
|**pricingPlan** | [**PricingPlanEnum**](#PricingPlanEnum) | No longer used. If included, the only allowed value is &lt;code&gt;RequestBasedUsage&lt;/code&gt;. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | &lt;p&gt;Applies one or more tags to the map resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.&lt;/p&gt; &lt;p&gt;Format: &lt;code&gt;\&quot;key\&quot; : \&quot;value\&quot;&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Restrictions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Maximum 50 tags per resource&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Each resource tag must be unique with a maximum of one value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Maximum key length: 128 Unicode characters in UTF-8&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Maximum value length: 256 Unicode characters in UTF-8&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - &#x3D; . _ : / @. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot use \&quot;aws:\&quot; as a prefix for a key.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |



## Enum: PricingPlanEnum

| Name | Value |
|---- | -----|
| REQUEST_BASED_USAGE | &quot;RequestBasedUsage&quot; |
| MOBILE_ASSET_TRACKING | &quot;MobileAssetTracking&quot; |
| MOBILE_ASSET_MANAGEMENT | &quot;MobileAssetManagement&quot; |



