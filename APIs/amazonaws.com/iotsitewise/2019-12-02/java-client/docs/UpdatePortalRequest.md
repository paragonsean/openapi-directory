

# UpdatePortalRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**portalName** | **String** | A new friendly name for the portal. |  |
|**portalDescription** | **String** | A new description for the portal. |  [optional] |
|**portalContactEmail** | **String** | The Amazon Web Services administrator&#39;s contact email address. |  |
|**portalLogoImage** | [**UpdatePortalRequestPortalLogoImage**](UpdatePortalRequestPortalLogoImage.md) |  |  [optional] |
|**roleArn** | **String** | The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of a service role that allows the portal&#39;s users to access your IoT SiteWise resources on your behalf. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html\&quot;&gt;Using service roles for IoT SiteWise Monitor&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. |  |
|**clientToken** | **String** | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. |  [optional] |
|**notificationSenderEmail** | **String** | The email address that sends alarm notifications. |  [optional] |
|**alarms** | [**CreatePortalRequestAlarms**](CreatePortalRequestAlarms.md) |  |  [optional] |



