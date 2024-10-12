

# OpsItem

<p>Operations engineers and IT professionals use Amazon Web Services Systems Manager OpsCenter to view, investigate, and remediate operational work items (OpsItems) impacting the performance and health of their Amazon Web Services resources. OpsCenter is integrated with Amazon EventBridge and Amazon CloudWatch. This means you can configure these services to automatically create an OpsItem in OpsCenter when a CloudWatch alarm enters the ALARM state or when EventBridge processes an event from any Amazon Web Services service that publishes events. Configuring Amazon CloudWatch alarms and EventBridge events to automatically create OpsItems allows you to quickly diagnose and remediate issues with Amazon Web Services resources from a single console.</p> <p>To help you diagnose issues, each OpsItem includes contextually relevant information such as the name and ID of the Amazon Web Services resource that generated the OpsItem, alarm or event details, alarm history, and an alarm timeline graph. For the Amazon Web Services resource, OpsCenter aggregates information from Config, CloudTrail logs, and EventBridge, so you don't have to navigate across multiple console pages during your investigation. For more information, see <a href=\"https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html\">OpsCenter</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdBy** | [**String**](String.md) |  |  [optional] |
|**opsItemType** | [**String**](String.md) |  |  [optional] |
|**createdTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**lastModifiedBy** | [**String**](String.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**notifications** | [**List**](List.md) |  |  [optional] |
|**priority** | [**Integer**](Integer.md) |  |  [optional] |
|**relatedOpsItems** | [**List**](List.md) |  |  [optional] |
|**status** | [**OpsItemStatus**](OpsItemStatus.md) |  |  [optional] |
|**opsItemId** | [**String**](String.md) |  |  [optional] |
|**version** | [**String**](String.md) |  |  [optional] |
|**title** | [**String**](String.md) |  |  [optional] |
|**source** | [**String**](String.md) |  |  [optional] |
|**operationalData** | [**Map**](Map.md) |  |  [optional] |
|**category** | [**String**](String.md) |  |  [optional] |
|**severity** | [**String**](String.md) |  |  [optional] |
|**actualStartTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**actualEndTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**plannedStartTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**plannedEndTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**opsItemArn** | [**String**](String.md) |  |  [optional] |



