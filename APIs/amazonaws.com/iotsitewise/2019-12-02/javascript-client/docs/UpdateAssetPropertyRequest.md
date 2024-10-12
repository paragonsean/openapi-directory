# AwsIoTSiteWise.UpdateAssetPropertyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**propertyAlias** | **String** | &lt;p&gt;The alias that identifies the property, such as an OPC-UA server data stream path (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\&quot;&gt;Mapping industrial data streams to asset properties&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you omit this parameter, the alias is removed from the property.&lt;/p&gt; | [optional] 
**propertyNotificationState** | **String** | &lt;p&gt;The MQTT notification state (enabled or disabled) for this asset property. When the notification state is enabled, IoT SiteWise publishes property value updates to a unique MQTT topic. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interact-with-other-services.html\&quot;&gt;Interacting with other services&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you omit this parameter, the notification state is set to &lt;code&gt;DISABLED&lt;/code&gt;.&lt;/p&gt; | [optional] 
**clientToken** | **String** | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] 
**propertyUnit** | **String** | The unit of measure (such as Newtons or RPM) of the asset property. If you don&#39;t specify a value for this parameter, the service uses the value of the &lt;code&gt;assetModelProperty&lt;/code&gt; in the asset model. | [optional] 



## Enum: PropertyNotificationStateEnum


* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)




