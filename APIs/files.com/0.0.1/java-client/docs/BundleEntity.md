

# BundleEntity

Create Bundle

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clickwrapBody** | **String** | Legal text that must be agreed to prior to accessing Bundle. |  [optional] |
|**clickwrapId** | **Integer** | ID of the clickwrap to use with this bundle. |  [optional] |
|**code** | **String** | Bundle code.  This code forms the end part of the Public URL. |  [optional] |
|**createdAt** | **OffsetDateTime** | Bundle created at date/time |  [optional] |
|**description** | **String** | Public description |  [optional] |
|**dontSeparateSubmissionsByFolder** | **Boolean** | Do not create subfolders for files uploaded to this share. Note: there are subtle security pitfalls with allowing anonymous uploads from multiple users to live in the same folder. We strongly discourage use of this option unless absolutely required. |  [optional] |
|**expiresAt** | **OffsetDateTime** | Bundle expiration date/time |  [optional] |
|**formFieldSet** | [**FormFieldSetEntity**](FormFieldSetEntity.md) |  |  [optional] |
|**hasInbox** | **Boolean** | Does this bundle have an associated inbox? |  [optional] |
|**id** | **Integer** | Bundle ID |  [optional] |
|**inboxId** | **Integer** | ID of the associated inbox, if available. |  [optional] |
|**maxUses** | **Integer** | Maximum number of times bundle can be accessed |  [optional] |
|**note** | **String** | Bundle internal note |  [optional] |
|**passwordProtected** | **Boolean** | Is this bundle password protected? |  [optional] |
|**pathTemplate** | **String** | Template for creating submission subfolders. Can use the uploader&#39;s name, email address, ip, company, and any custom form data. |  [optional] |
|**paths** | **List&lt;String&gt;** | A list of paths in this bundle.  For performance reasons, this is not provided when listing bundles. |  [optional] |
|**permissions** | [**PermissionsEnum**](#PermissionsEnum) | Permissions that apply to Folders in this Share Link. |  [optional] |
|**previewOnly** | **Boolean** | Restrict users to previewing files only? |  [optional] |
|**requireRegistration** | **Boolean** | Show a registration page that captures the downloader&#39;s name and email address? |  [optional] |
|**requireShareRecipient** | **Boolean** | Only allow access to recipients who have explicitly received the share via an email sent through the Files.com UI? |  [optional] |
|**sendEmailReceiptToUploader** | **Boolean** | Send delivery receipt to the uploader. Note: For writable share only |  [optional] |
|**skipCompany** | **Boolean** | BundleRegistrations can be saved without providing company? |  [optional] |
|**skipEmail** | **Boolean** | BundleRegistrations can be saved without providing email? |  [optional] |
|**skipName** | **Boolean** | BundleRegistrations can be saved without providing name? |  [optional] |
|**url** | **String** | Public URL of Share Link |  [optional] |
|**userId** | **Integer** | Bundle creator user ID |  [optional] |
|**username** | **String** | Bundle creator username |  [optional] |
|**watermarkAttachment** | [**ImageEntity**](ImageEntity.md) |  |  [optional] |
|**watermarkValue** | **Object** | Preview watermark settings applied to all bundle items. Uses the same keys as Behavior.value |  [optional] |



## Enum: PermissionsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |
| READ_WRITE | &quot;read_write&quot; |
| FULL | &quot;full&quot; |
| NONE | &quot;none&quot; |
| PREVIEW_ONLY | &quot;preview_only&quot; |



