

# CreateNetworkSiteRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilityZone** | **String** | The Availability Zone that is the parent of this site. You can&#39;t change the Availability Zone after you create the site. |  [optional] |
|**availabilityZoneId** | **String** | The ID of the Availability Zone that is the parent of this site. You can&#39;t change the Availability Zone after you create the site. |  [optional] |
|**clientToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Run_Instance_Idempotency.html\&quot;&gt;How to ensure idempotency&lt;/a&gt;. |  [optional] |
|**description** | **String** | The description of the site. |  [optional] |
|**networkArn** | **String** | The Amazon Resource Name (ARN) of the network. |  |
|**networkSiteName** | **String** | The name of the site. You can&#39;t change the name after you create the site. |  |
|**pendingPlan** | [**CreateNetworkSiteRequestPendingPlan**](CreateNetworkSiteRequestPendingPlan.md) |  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** |  The tags to apply to the network site.  |  [optional] |



