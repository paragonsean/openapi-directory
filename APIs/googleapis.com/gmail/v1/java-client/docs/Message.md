

# Message

An email message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**historyId** | **String** | The ID of the last history record that modified this message. |  [optional] |
|**id** | **String** | The immutable ID of the message. |  [optional] |
|**internalDate** | **String** | The internal message creation timestamp (epoch ms), which determines ordering in the inbox. For normal SMTP-received email, this represents the time the message was originally accepted by Google, which is more reliable than the &#x60;Date&#x60; header. However, for API-migrated mail, it can be configured by client to be based on the &#x60;Date&#x60; header. |  [optional] |
|**labelIds** | **List&lt;String&gt;** | List of IDs of labels applied to this message. |  [optional] |
|**payload** | [**MessagePart**](MessagePart.md) |  |  [optional] |
|**raw** | **byte[]** | The entire email message in an RFC 2822 formatted and base64url encoded string. Returned in &#x60;messages.get&#x60; and &#x60;drafts.get&#x60; responses when the &#x60;format&#x3D;RAW&#x60; parameter is supplied. |  [optional] |
|**sizeEstimate** | **Integer** | Estimated size in bytes of the message. |  [optional] |
|**snippet** | **String** | A short part of the message text. |  [optional] |
|**threadId** | **String** | The ID of the thread the message belongs to. To add a message or draft to a thread, the following criteria must be met: 1. The requested &#x60;threadId&#x60; must be specified on the &#x60;Message&#x60; or &#x60;Draft.Message&#x60; you supply with your request. 2. The &#x60;References&#x60; and &#x60;In-Reply-To&#x60; headers must be set in compliance with the [RFC 2822](https://tools.ietf.org/html/rfc2822) standard. 3. The &#x60;Subject&#x60; headers must match.  |  [optional] |



