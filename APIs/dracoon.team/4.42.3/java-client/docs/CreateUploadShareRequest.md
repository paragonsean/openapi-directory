

# CreateUploadShareRequest

Request model for creating an Upload Share

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creatorLanguage** | **String** | &amp;#128679; Deprecated since v4.20.0  Language tag for messages to creator |  [optional] |
|**expiration** | [**ObjectExpiration**](ObjectExpiration.md) |  |  [optional] |
|**filesExpiryPeriod** | **Integer** | Number of days after which uploaded files expire |  [optional] |
|**internalNotes** | **String** | &amp;#128640; Since v4.11.0  Internal notes |  [optional] |
|**mailBody** | **String** | &amp;#128679; Deprecated since v4.11.0  Notification email content |  [optional] |
|**mailRecipients** | **String** | &amp;#128679; Deprecated since v4.11.0  CSV string of recipient email addresses |  [optional] |
|**mailSubject** | **String** | &amp;#128679; Deprecated since v4.11.0  Notification email subject |  [optional] |
|**maxSize** | **Long** | Maximal total size of uploaded files (in bytes) |  [optional] |
|**maxSlots** | **Integer** | Maximal amount of files to upload |  [optional] |
|**name** | **String** | Alias name  (default: name of the shared node) |  [optional] |
|**notes** | **String** | User notes |  [optional] |
|**notifyCreator** | **Boolean** | &amp;#128679; Deprecated since v4.20.0  Notify creator on every upload. |  [optional] |
|**password** | **String** | Password |  [optional] |
|**receiverLanguage** | **String** | Language tag for messages to receiver |  [optional] |
|**sendMail** | **Boolean** | &amp;#128679; Deprecated since v4.11.0  Notify recipients via email  Please use &#x60;POST /shares/uploads/{share_id}/email&#x60; API instead. |  [optional] |
|**sendSms** | **Boolean** | &amp;#128679; Deprecated since v4.11.0  Send share password via SMS  Please use &#x60;textMessageRecipients&#x60; attribute instead. |  [optional] |
|**showCreatorName** | **Boolean** | &amp;#128640; Since v4.11.0  Show creator first and last name. |  [optional] |
|**showCreatorUsername** | **Boolean** | &amp;#128640; Since v4.11.0  Show creator email address. |  [optional] |
|**showUploadedFiles** | **Boolean** | Allow display of already uploaded files |  [optional] |
|**smsRecipients** | **String** | &amp;#128679; Deprecated since v4.11.0  CSV string of recipient MSISDNs |  [optional] |
|**targetId** | **Long** | Target room or folder ID |  |
|**textMessageRecipients** | **List&lt;String&gt;** | &amp;#128640; Since v4.11.0  List of recipient FQTNs  E.123 / E.164 Format |  [optional] |



