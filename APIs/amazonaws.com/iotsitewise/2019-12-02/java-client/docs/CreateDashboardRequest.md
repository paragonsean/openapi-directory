

# CreateDashboardRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**projectId** | **String** | The ID of the project in which to create the dashboard. |  |
|**dashboardName** | **String** | A friendly name for the dashboard. |  |
|**dashboardDescription** | **String** | A description for the dashboard. |  [optional] |
|**dashboardDefinition** | **String** | The dashboard definition specified in a JSON literal. For detailed information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html\&quot;&gt;Creating dashboards (CLI)&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. |  |
|**clientToken** | **String** | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | A list of key-value pairs that contain metadata for the dashboard. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\&quot;&gt;Tagging your IoT SiteWise resources&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. |  [optional] |



