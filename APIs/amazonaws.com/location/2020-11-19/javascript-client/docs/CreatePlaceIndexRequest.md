# AmazonLocationService.CreatePlaceIndexRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataSource** | **String** | &lt;p&gt;Specifies the geospatial data provider for the new place index.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This field is case-sensitive. Enter the valid values as shown. For example, entering &lt;code&gt;HERE&lt;/code&gt; returns an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Valid values include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Esri&lt;/code&gt; – For additional information about &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/esri.html\&quot;&gt;Esri&lt;/a&gt;&#39;s coverage in your region of interest, see &lt;a href&#x3D;\&quot;https://developers.arcgis.com/rest/geocode/api-reference/geocode-coverage.htm\&quot;&gt;Esri details on geocoding coverage&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Grab&lt;/code&gt; – Grab provides place index functionality for Southeast Asia. For additional information about &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/grab.html\&quot;&gt;GrabMaps&lt;/a&gt;&#39; coverage, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/grab.html#grab-coverage-area\&quot;&gt;GrabMaps countries and areas covered&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Here&lt;/code&gt; – For additional information about &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/HERE.html\&quot;&gt;HERE Technologies&lt;/a&gt;&#39; coverage in your region of interest, see &lt;a href&#x3D;\&quot;https://developer.here.com/documentation/geocoder/dev_guide/topics/coverage-geocoder.html\&quot;&gt;HERE details on goecoding coverage&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you specify HERE Technologies (&lt;code&gt;Here&lt;/code&gt;) as the data provider, you may not &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location-places/latest/APIReference/API_DataSourceConfiguration.html\&quot;&gt;store results&lt;/a&gt; for locations in Japan. For more information, see the &lt;a href&#x3D;\&quot;http://aws.amazon.com/service-terms/\&quot;&gt;Amazon Web Services Service Terms&lt;/a&gt; for Amazon Location Service.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For additional information , see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/what-is-data-provider.html\&quot;&gt;Data providers&lt;/a&gt; on the &lt;i&gt;Amazon Location Service Developer Guide&lt;/i&gt;.&lt;/p&gt; | 
**dataSourceConfiguration** | [**CreatePlaceIndexRequestDataSourceConfiguration**](CreatePlaceIndexRequestDataSourceConfiguration.md) |  | [optional] 
**description** | **String** | The optional description for the place index resource. | [optional] 
**indexName** | **String** | &lt;p&gt;The name of the place index resource. &lt;/p&gt; &lt;p&gt;Requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be a unique place index resource name.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;No spaces allowed. For example, &lt;code&gt;ExamplePlaceIndex&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
**pricingPlan** | **String** | No longer used. If included, the only allowed value is &lt;code&gt;RequestBasedUsage&lt;/code&gt;. | [optional] 
**tags** | **{String: String}** | &lt;p&gt;Applies one or more tags to the place index resource. A tag is a key-value pair that helps you manage, identify, search, and filter your resources.&lt;/p&gt; &lt;p&gt;Format: &lt;code&gt;\&quot;key\&quot; : \&quot;value\&quot;&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Restrictions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Maximum 50 tags per resource.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Each tag key must be unique and must have exactly one associated value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Maximum key length: 128 Unicode characters in UTF-8.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Maximum value length: 256 Unicode characters in UTF-8.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - &#x3D; . _ : / @&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot use \&quot;aws:\&quot; as a prefix for a key.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 



## Enum: PricingPlanEnum


* `RequestBasedUsage` (value: `"RequestBasedUsage"`)

* `MobileAssetTracking` (value: `"MobileAssetTracking"`)

* `MobileAssetManagement` (value: `"MobileAssetManagement"`)




