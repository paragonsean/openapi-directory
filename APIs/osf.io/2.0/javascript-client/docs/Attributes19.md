# OsfApiv2Documentation.Attributes19

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The category of the registered node. | [optional] [readonly] 
**collection** | **Boolean** | Whether or not this registration represents a collection. This value should always be &#x60;false&#x60;. This field may be deprecated in future versions. | [optional] [readonly] 
**currentUserCanComment** | **Boolean** | Whether or not the current user has permission to post comments on this registration. Comments on registrations can be set to allow all users to comment or restricted to only contributors. | [optional] [readonly] 
**currentUserPermissions** | **[String]** | A list of strings representing the permissions for the current user on this registration. Valid permissions are \&quot;admin\&quot;, \&quot;read\&quot;, and \&quot;write\&quot;. | [optional] [readonly] 
**dateCreated** | **Date** | The time at which the registered node was created, as an iso8601 formatted timestamp. | [optional] [readonly] 
**dateModified** | **Date** | The time at which the registered node was last modified, as an iso8601 formatted timestamp. | [optional] [readonly] 
**dateRegistered** | **Date** | The time at which this registration was created, as an iso8601 formatted timestamp. | [optional] [readonly] 
**dateWithdrawn** | **Date** | The time at which this registration was withdrawn, as an iso8601 formatted timestamp. | [optional] [readonly] 
**description** | **String** | The description of the registered node. | [optional] [readonly] 
**embargoEndDate** | **Date** | The time at which the embargo on this registration will be lifted and the registration will become public, as an iso8601 formatted timestamp. | [optional] [readonly] 
**fork** | **Boolean** | Whether or not this registration represents a fork of another node. | [optional] [readonly] 
**nodeLicense** | **String** | A dictionary containing the metadata (copyright year and holder) associated with the registered node license (required for certain license types). | [optional] [readonly] 
**pendingEmbargoApproval** | **Boolean** | Whether or not the embargo associated with this registration is pending approval from project administrators. | [optional] [readonly] 
**pendingRegistrationApproval** | **Boolean** | Whether or not the registration is pending approval from project administrators. | [optional] [readonly] 
**pendingWithdrawal** | **Boolean** | Whether or not the registration is pending approval for withdrawal from project administrators. | [optional] [readonly] 
**preprint** | **Boolean** | Whether or not a preprint has been created from this node, or if this node was created for a preprint. | [optional] [readonly] 
**_public** | **Boolean** | Whether or not the registration is publicly visible. | [optional] 
**registeredMeta** | **String** | A dictionary with supplemental registration questions and responses. | [optional] [readonly] 
**registration** | **Boolean** | Whether or not this is a registration. This value should always be &#x60;true&#x60;. This field may be deprecated in future versions. | [optional] [readonly] 
**registrationSupplement** | **String** | The title of the registration schema this registration conforms to. | [optional] [readonly] 
**tags** | **[String]** | A list of strings that describe the registered node. | [optional] [readonly] 
**templateFrom** | **String** | The unique ID of the node from which the registered node was templated, if the registered node was created from a template. | [optional] [readonly] 
**title** | **String** | The title of the registered node. | [optional] [readonly] 
**withdrawalJustification** | **String** | The reasoning for why this registration was withdrawn, as entered by the administrator that initiated the withdrawal. | [optional] [readonly] 
**withdrawn** | **Boolean** | Whether or not this registration has been withdrawn. | [optional] [readonly] 



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




