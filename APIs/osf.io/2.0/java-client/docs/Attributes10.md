

# Attributes10

The properties of the node entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | The category of the node, as selected by project contributors. |  |
|**collection** | **Boolean** | Whether or not this node represents a collection. This value should always be &#x60;false&#x60;. This field may be deprecated in future versions. |  [optional] [readonly] |
|**currentUserCanComment** | **Boolean** | Whether or not the current user has permission to post comments on this node. Comments on nodes can be set to allow all users to comment (if public) or restricted to only allow comments from contributors. |  [optional] [readonly] |
|**currentUserPermissions** | **List&lt;String&gt;** | A list of strings representing the permissions for the current user on this node. Valid permissions are \&quot;admin\&quot;, \&quot;read\&quot;, and \&quot;write\&quot;. |  [optional] [readonly] |
|**dateCreated** | **OffsetDateTime** | The time at which the node was created, as an iso8601 formatted timestamp. |  [optional] [readonly] |
|**dateModified** | **OffsetDateTime** | The time at which the node was last modified, as an iso8601 formatted timestamp. |  [optional] [readonly] |
|**description** | **String** | The description of the node. |  [optional] |
|**fork** | **Boolean** | Whether or not this node represents a fork of another node. |  [optional] [readonly] |
|**forkedDate** | **OffsetDateTime** | If this node is a fork of another node, the time at which the node was created, as an iso8601 formatted timestamp. |  [optional] [readonly] |
|**nodeLicense** | **String** | A dictionary containing the metadata (copyright year and holder) associated with the node license (required for certain license types). |  [optional] |
|**preprint** | **Boolean** | Whether or not a preprint has been created from this node, or if this node was created for a preprint. |  [optional] [readonly] |
|**_public** | **Boolean** | Whether or not the node is publicly visible. This field is only editable by project administrators. |  [optional] |
|**registration** | **Boolean** | Whether or not the node represents a registration. This value should always be &#x60;false&#x60;. This field may be deprecated in future versions. |  [optional] [readonly] |
|**tags** | **List&lt;String&gt;** | A list of strings that describe this node, as entered by project contributors. |  [optional] |
|**templateFrom** | **String** | The unique ID of the node from which this node was templated, if this node was created from a template. |  [optional] |
|**title** | **String** | The title of the node. |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| ANALYSIS | &quot;analysis&quot; |
| COMMUNICATION | &quot;communication&quot; |
| DATA | &quot;data&quot; |
| HYPOTHESIS | &quot;hypothesis&quot; |
| INSTRUMENTATION | &quot;instrumentation&quot; |
| METHODS_AND_MEASURES | &quot;methods and measures&quot; |
| PROCEDURE | &quot;procedure&quot; |
| PROJECT | &quot;project&quot; |
| SOFTWARE | &quot;software&quot; |
| OTHER | &quot;other&quot; |



