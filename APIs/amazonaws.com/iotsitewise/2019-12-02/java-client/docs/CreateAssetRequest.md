

# CreateAssetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetName** | **String** | A friendly name for the asset. |  |
|**assetModelId** | **String** | The ID of the asset model from which to create the asset. |  |
|**clientToken** | **String** | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | A list of key-value pairs that contain metadata for the asset. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\&quot;&gt;Tagging your IoT SiteWise resources&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. |  [optional] |
|**assetDescription** | **String** | A description for the asset. |  [optional] |



