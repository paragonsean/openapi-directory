

# UpdateAssetModelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetModelName** | **String** | A unique, friendly name for the asset model. |  |
|**assetModelDescription** | **String** | A description for the asset model. |  [optional] |
|**assetModelProperties** | [**List&lt;AssetModelProperty&gt;**](AssetModelProperty.md) | &lt;p&gt;The updated property definitions of the asset model. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html\&quot;&gt;Asset properties&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can specify up to 200 properties per asset model. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html\&quot;&gt;Quotas&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; |  [optional] |
|**assetModelHierarchies** | [**List&lt;AssetModelHierarchy&gt;**](AssetModelHierarchy.md) | &lt;p&gt;The updated hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html\&quot;&gt;Asset hierarchies&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can specify up to 10 hierarchies per asset model. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html\&quot;&gt;Quotas&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; |  [optional] |
|**assetModelCompositeModels** | [**List&lt;AssetModelCompositeModel&gt;**](AssetModelCompositeModel.md) | The composite asset models that are part of this asset model. Composite asset models are asset models that contain specific properties. Each composite model has a type that defines the properties that the composite model supports. Use composite asset models to define alarms on this asset model. |  [optional] |
|**clientToken** | **String** | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. |  [optional] |



