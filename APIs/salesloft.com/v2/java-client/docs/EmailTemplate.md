

# EmailTemplate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | **Object** | Links to attachments and tags resources for this email template. |  [optional] |
|**archivedAt** | **OffsetDateTime** | Datetime of when the email template was archived, if archived |  [optional] |
|**body** | **String** | Sanitized body of the email template without email signature |  [optional] |
|**bodyPreview** | **String** | A plain text version of the first 100 characters of the body of the email template |  [optional] |
|**cadenceTemplate** | **Boolean** | Whether this email template is only used on a cadence step. These templates are not visible in the SalesLoft application template list. If false, this email template is visible in the SalesLoft application, and may be used when composing an email or creating a cadence step. |  [optional] |
|**clickTrackingEnabled** | **Boolean** | Whether click tracking is enabled for this email template |  [optional] |
|**counts** | [**EmailTemplateCounts**](EmailTemplateCounts.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | Datetime of when the email template was created |  [optional] |
|**groups** | [**List&lt;EmbeddedResource&gt;**](EmbeddedResource.md) | Groups to which this template is assigned, if any |  [optional] |
|**id** | **Integer** | ID of email template |  [optional] |
|**lastUsedAt** | **OffsetDateTime** | Datetime of when the email template was last used |  [optional] |
|**openTrackingEnabled** | **Boolean** | Whether open tracking is enabled for this email template |  [optional] |
|**shared** | **Boolean** | Whether this email template is visible to team members (shared) |  [optional] |
|**subject** | **String** | Subject of the email template |  [optional] |
|**tags** | **List&lt;String&gt;** | All tags applied to this email template |  [optional] |
|**teamTemplate** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**templateOwner** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**title** | **String** | Title of the email template |  [optional] |
|**updatedAt** | **OffsetDateTime** | Datetime of when the email template was last updated |  [optional] |



