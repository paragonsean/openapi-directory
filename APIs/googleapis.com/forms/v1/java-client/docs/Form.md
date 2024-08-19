

# Form

A Google Forms document. A form is created in Drive, and deleting a form or changing its access protections is done via the [Drive API](https://developers.google.com/drive/api/v3/about-sdk).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**formId** | **String** | Output only. The form ID. |  [optional] [readonly] |
|**info** | [**Info**](Info.md) |  |  [optional] |
|**items** | [**List&lt;Item&gt;**](Item.md) | Required. A list of the form&#39;s items, which can include section headers, questions, embedded media, etc. |  [optional] |
|**linkedSheetId** | **String** | Output only. The ID of the linked Google Sheet which is accumulating responses from this Form (if such a Sheet exists). |  [optional] [readonly] |
|**responderUri** | **String** | Output only. The form URI to share with responders. This opens a page that allows the user to submit responses but not edit the questions. |  [optional] [readonly] |
|**revisionId** | **String** | Output only. The revision ID of the form. Used in the WriteControl in update requests to identify the revision on which the changes are based. The format of the revision ID may change over time, so it should be treated opaquely. A returned revision ID is only guaranteed to be valid for 24 hours after it has been returned and cannot be shared across users. If the revision ID is unchanged between calls, then the form has not changed. Conversely, a changed ID (for the same form and user) usually means the form has been updated; however, a changed ID can also be due to internal factors such as ID format changes. |  [optional] [readonly] |
|**settings** | [**FormSettings**](FormSettings.md) |  |  [optional] |



