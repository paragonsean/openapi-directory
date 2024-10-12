

# Feed

An asset feed used to export asset updates to a destinations. An asset feed filter controls what updates are exported. The asset feed must be created within a project, organization, or folder. Supported destinations are: Pub/Sub topics.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetNames** | **List&lt;String&gt;** | A list of the full names of the assets to receive updates. You must specify either or both of asset_names and asset_types. Only asset updates matching specified asset_names or asset_types are exported to the feed. Example: &#x60;//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1&#x60;. For a list of the full names for supported asset types, see [Resource name format](/asset-inventory/docs/resource-name-format). |  [optional] |
|**assetTypes** | **List&lt;String&gt;** | A list of types of the assets to receive updates. You must specify either or both of asset_names and asset_types. Only asset updates matching specified asset_names or asset_types are exported to the feed. Example: &#x60;\&quot;compute.googleapis.com/Disk\&quot;&#x60; For a list of all supported asset types, see [Supported asset types](/asset-inventory/docs/supported-asset-types). |  [optional] |
|**condition** | [**Expr**](Expr.md) |  |  [optional] |
|**contentType** | [**ContentTypeEnum**](#ContentTypeEnum) | Asset content type. If not specified, no content but the asset name and type will be returned. |  [optional] |
|**feedOutputConfig** | [**FeedOutputConfig**](FeedOutputConfig.md) |  |  [optional] |
|**name** | **String** | Required. The format will be projects/{project_number}/feeds/{client-assigned_feed_identifier} or folders/{folder_number}/feeds/{client-assigned_feed_identifier} or organizations/{organization_number}/feeds/{client-assigned_feed_identifier} The client-assigned feed identifier must be unique within the parent project/folder/organization. |  [optional] |
|**relationshipTypes** | **List&lt;String&gt;** | A list of relationship types to output, for example: &#x60;INSTANCE_TO_INSTANCEGROUP&#x60;. This field should only be specified if content_type&#x3D;RELATIONSHIP. * If specified: it outputs specified relationship updates on the [asset_names] or the [asset_types]. It returns an error if any of the [relationship_types] doesn&#39;t belong to the supported relationship types of the [asset_names] or [asset_types], or any of the [asset_names] or the [asset_types] doesn&#39;t belong to the source types of the [relationship_types]. * Otherwise: it outputs the supported relationships of the types of [asset_names] and [asset_types] or returns an error if any of the [asset_names] or the [asset_types] has no replationship support. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types. |  [optional] |



## Enum: ContentTypeEnum

| Name | Value |
|---- | -----|
| CONTENT_TYPE_UNSPECIFIED | &quot;CONTENT_TYPE_UNSPECIFIED&quot; |
| RESOURCE | &quot;RESOURCE&quot; |
| IAM_POLICY | &quot;IAM_POLICY&quot; |
| ORG_POLICY | &quot;ORG_POLICY&quot; |
| ACCESS_POLICY | &quot;ACCESS_POLICY&quot; |
| OS_INVENTORY | &quot;OS_INVENTORY&quot; |
| RELATIONSHIP | &quot;RELATIONSHIP&quot; |



