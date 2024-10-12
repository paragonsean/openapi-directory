# FilesComApi.ClickwrapEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **String** | Body text of Clickwrap (supports Markdown formatting). | [optional] 
**id** | **Number** | Clickwrap ID | [optional] 
**name** | **String** | Name of the Clickwrap agreement (used when selecting from multiple Clickwrap agreements.) | [optional] 
**useWithBundles** | **String** | Use this Clickwrap for Bundles? | [optional] 
**useWithInboxes** | **String** | Use this Clickwrap for Inboxes? | [optional] 
**useWithUsers** | **String** | Use this Clickwrap for User Registrations?  Note: This only applies to User Registrations where the User is invited to your Files.com site using an E-Mail invitation process where they then set their own password. | [optional] 



## Enum: UseWithBundlesEnum


* `none` (value: `"none"`)

* `available` (value: `"available"`)

* `require` (value: `"require"`)





## Enum: UseWithInboxesEnum


* `none` (value: `"none"`)

* `available` (value: `"available"`)

* `require` (value: `"require"`)





## Enum: UseWithUsersEnum


* `none` (value: `"none"`)

* `require` (value: `"require"`)




