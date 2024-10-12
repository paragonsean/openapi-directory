# FilesComApi.BundleEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clickwrapBody** | **String** | Legal text that must be agreed to prior to accessing Bundle. | [optional] 
**clickwrapId** | **Number** | ID of the clickwrap to use with this bundle. | [optional] 
**code** | **String** | Bundle code.  This code forms the end part of the Public URL. | [optional] 
**createdAt** | **Date** | Bundle created at date/time | [optional] 
**description** | **String** | Public description | [optional] 
**dontSeparateSubmissionsByFolder** | **Boolean** | Do not create subfolders for files uploaded to this share. Note: there are subtle security pitfalls with allowing anonymous uploads from multiple users to live in the same folder. We strongly discourage use of this option unless absolutely required. | [optional] 
**expiresAt** | **Date** | Bundle expiration date/time | [optional] 
**formFieldSet** | [**FormFieldSetEntity**](FormFieldSetEntity.md) |  | [optional] 
**hasInbox** | **Boolean** | Does this bundle have an associated inbox? | [optional] 
**id** | **Number** | Bundle ID | [optional] 
**inboxId** | **Number** | ID of the associated inbox, if available. | [optional] 
**maxUses** | **Number** | Maximum number of times bundle can be accessed | [optional] 
**note** | **String** | Bundle internal note | [optional] 
**passwordProtected** | **Boolean** | Is this bundle password protected? | [optional] 
**pathTemplate** | **String** | Template for creating submission subfolders. Can use the uploader&#39;s name, email address, ip, company, and any custom form data. | [optional] 
**paths** | **[String]** | A list of paths in this bundle.  For performance reasons, this is not provided when listing bundles. | [optional] 
**permissions** | **String** | Permissions that apply to Folders in this Share Link. | [optional] 
**previewOnly** | **Boolean** | Restrict users to previewing files only? | [optional] 
**requireRegistration** | **Boolean** | Show a registration page that captures the downloader&#39;s name and email address? | [optional] 
**requireShareRecipient** | **Boolean** | Only allow access to recipients who have explicitly received the share via an email sent through the Files.com UI? | [optional] 
**sendEmailReceiptToUploader** | **Boolean** | Send delivery receipt to the uploader. Note: For writable share only | [optional] 
**skipCompany** | **Boolean** | BundleRegistrations can be saved without providing company? | [optional] 
**skipEmail** | **Boolean** | BundleRegistrations can be saved without providing email? | [optional] 
**skipName** | **Boolean** | BundleRegistrations can be saved without providing name? | [optional] 
**url** | **String** | Public URL of Share Link | [optional] 
**userId** | **Number** | Bundle creator user ID | [optional] 
**username** | **String** | Bundle creator username | [optional] 
**watermarkAttachment** | [**ImageEntity**](ImageEntity.md) |  | [optional] 
**watermarkValue** | **Object** | Preview watermark settings applied to all bundle items. Uses the same keys as Behavior.value | [optional] 



## Enum: PermissionsEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)

* `read_write` (value: `"read_write"`)

* `full` (value: `"full"`)

* `none` (value: `"none"`)

* `preview_only` (value: `"preview_only"`)




