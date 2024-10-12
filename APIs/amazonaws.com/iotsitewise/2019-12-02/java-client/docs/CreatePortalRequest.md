

# CreatePortalRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**portalName** | **String** | A friendly name for the portal. |  |
|**portalDescription** | **String** | A description for the portal. |  [optional] |
|**portalContactEmail** | **String** | The Amazon Web Services administrator&#39;s contact email address. |  |
|**clientToken** | **String** | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. |  [optional] |
|**portalLogoImageFile** | [**CreatePortalRequestPortalLogoImageFile**](CreatePortalRequestPortalLogoImageFile.md) |  |  [optional] |
|**roleArn** | **String** | The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of a service role that allows the portal&#39;s users to access your IoT SiteWise resources on your behalf. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html\&quot;&gt;Using service roles for IoT SiteWise Monitor&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. |  |
|**tags** | **Map&lt;String, String&gt;** | A list of key-value pairs that contain metadata for the portal. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\&quot;&gt;Tagging your IoT SiteWise resources&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. |  [optional] |
|**portalAuthMode** | [**PortalAuthModeEnum**](#PortalAuthModeEnum) | &lt;p&gt;The service to use to authenticate users to the portal. Choose from the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SSO&lt;/code&gt; – The portal uses IAM Identity Center (successor to Single Sign-On) to authenticate users and manage user permissions. Before you can create a portal that uses IAM Identity Center, you must enable IAM Identity Center. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-get-started.html#mon-gs-sso\&quot;&gt;Enabling IAM Identity Center&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. This option is only available in Amazon Web Services Regions other than the China Regions.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;IAM&lt;/code&gt; – The portal uses Identity and Access Management to authenticate users and manage user permissions.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can&#39;t change this value after you create a portal.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;SSO&lt;/code&gt; &lt;/p&gt; |  [optional] |
|**notificationSenderEmail** | **String** | &lt;p&gt;The email address that sends alarm notifications.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html\&quot;&gt;IoT Events managed Lambda function&lt;/a&gt; to manage your emails, you must &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html\&quot;&gt;verify the sender email address in Amazon SES&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt; |  [optional] |
|**alarms** | [**CreatePortalRequestAlarms**](CreatePortalRequestAlarms.md) |  |  [optional] |



## Enum: PortalAuthModeEnum

| Name | Value |
|---- | -----|
| IAM | &quot;IAM&quot; |
| SSO | &quot;SSO&quot; |



