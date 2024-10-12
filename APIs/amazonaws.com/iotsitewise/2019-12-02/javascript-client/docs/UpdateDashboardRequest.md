# AwsIoTSiteWise.UpdateDashboardRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboardName** | **String** | A new friendly name for the dashboard. | 
**dashboardDescription** | **String** | A new description for the dashboard. | [optional] 
**dashboardDefinition** | **String** | The new dashboard definition, as specified in a JSON literal. For detailed information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html\&quot;&gt;Creating dashboards (CLI)&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. | 
**clientToken** | **String** | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] 


