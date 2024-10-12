

# CreateOriginEndpointRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**originEndpointName** | **String** | The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and must be unique for your account in the AWS Region and channel. You can&#39;t use spaces in the name. You can&#39;t change the name after you create the endpoint. |  |
|**containerType** | [**ContainerTypeEnum**](#ContainerTypeEnum) | The type of container to attach to this origin endpoint. A container type is a file format that encapsulates one or more media streams, such as audio and video, into a single file. You can&#39;t change the container type after you create the endpoint. |  |
|**segment** | [**CreateOriginEndpointRequestSegment**](CreateOriginEndpointRequestSegment.md) |  |  [optional] |
|**description** | **String** | Enter any descriptive text that helps you to identify the origin endpoint. |  [optional] |
|**startoverWindowSeconds** | **Integer** | The size of the window (in seconds) to create a window of the live stream that&#39;s available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days). |  [optional] |
|**hlsManifests** | [**List&lt;CreateHlsManifestConfiguration&gt;**](CreateHlsManifestConfiguration.md) | An HTTP live streaming (HLS) manifest configuration. |  [optional] |
|**lowLatencyHlsManifests** | [**List&lt;CreateLowLatencyHlsManifestConfiguration&gt;**](CreateLowLatencyHlsManifestConfiguration.md) | A low-latency HLS manifest configuration. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | &lt;p&gt;A comma-separated list of tag key:value pairs that you define. For example:&lt;/p&gt; &lt;p&gt; &lt;code&gt;\&quot;Key1\&quot;: \&quot;Value1\&quot;,&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt;\&quot;Key2\&quot;: \&quot;Value2\&quot;&lt;/code&gt; &lt;/p&gt; |  [optional] |



## Enum: ContainerTypeEnum

| Name | Value |
|---- | -----|
| TS | &quot;TS&quot; |
| CMAF | &quot;CMAF&quot; |



