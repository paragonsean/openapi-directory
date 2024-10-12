# AwsIoTSiteWise.DisassociateAssetsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hierarchyId** | **String** | The ID of a hierarchy in the parent asset&#39;s model. Hierarchies allow different groupings of assets to be formed that all come from the same asset model. You can use the hierarchy ID to identify the correct asset to disassociate. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html\&quot;&gt;Asset hierarchies&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. | 
**childAssetId** | **String** | The ID of the child asset to disassociate. | 
**clientToken** | **String** | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] 


