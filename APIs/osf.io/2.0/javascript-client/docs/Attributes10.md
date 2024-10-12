# OsfApiv2Documentation.Attributes10

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The category of the node, as selected by project contributors. | 
**collection** | **Boolean** | Whether or not this node represents a collection. This value should always be &#x60;false&#x60;. This field may be deprecated in future versions. | [optional] [readonly] 
**currentUserCanComment** | **Boolean** | Whether or not the current user has permission to post comments on this node. Comments on nodes can be set to allow all users to comment (if public) or restricted to only allow comments from contributors. | [optional] [readonly] 
**currentUserPermissions** | **[String]** | A list of strings representing the permissions for the current user on this node. Valid permissions are \&quot;admin\&quot;, \&quot;read\&quot;, and \&quot;write\&quot;. | [optional] [readonly] 
**dateCreated** | **Date** | The time at which the node was created, as an iso8601 formatted timestamp. | [optional] [readonly] 
**dateModified** | **Date** | The time at which the node was last modified, as an iso8601 formatted timestamp. | [optional] [readonly] 
**description** | **String** | The description of the node. | [optional] 
**fork** | **Boolean** | Whether or not this node represents a fork of another node. | [optional] [readonly] 
**forkedDate** | **Date** | If this node is a fork of another node, the time at which the node was created, as an iso8601 formatted timestamp. | [optional] [readonly] 
**nodeLicense** | **String** | A dictionary containing the metadata (copyright year and holder) associated with the node license (required for certain license types). | [optional] 
**preprint** | **Boolean** | Whether or not a preprint has been created from this node, or if this node was created for a preprint. | [optional] [readonly] 
**_public** | **Boolean** | Whether or not the node is publicly visible. This field is only editable by project administrators. | [optional] 
**registration** | **Boolean** | Whether or not the node represents a registration. This value should always be &#x60;false&#x60;. This field may be deprecated in future versions. | [optional] [readonly] 
**tags** | **[String]** | A list of strings that describe this node, as entered by project contributors. | [optional] 
**templateFrom** | **String** | The unique ID of the node from which this node was templated, if this node was created from a template. | [optional] 
**title** | **String** | The title of the node. | 



## Enum: CategoryEnum


* `analysis` (value: `"analysis"`)

* `communication` (value: `"communication"`)

* `data` (value: `"data"`)

* `hypothesis` (value: `"hypothesis"`)

* `instrumentation` (value: `"instrumentation"`)

* `methods and measures` (value: `"methods and measures"`)

* `procedure` (value: `"procedure"`)

* `project` (value: `"project"`)

* `software` (value: `"software"`)

* `other` (value: `"other"`)




