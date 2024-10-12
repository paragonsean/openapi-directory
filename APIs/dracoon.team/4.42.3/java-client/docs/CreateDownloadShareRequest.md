

# CreateDownloadShareRequest

Request model for creating a Download Share

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creatorLanguage** | **String** | &amp;#128679; Deprecated since v4.20.0  Language tag for messages to creator |  [optional] |
|**expiration** | [**ObjectExpiration**](ObjectExpiration.md) |  |  [optional] |
|**fileKey** | [**FileKey**](FileKey.md) |  |  [optional] |
|**internalNotes** | **String** | &amp;#128640; Since v4.11.0  Internal notes |  [optional] |
|**keyPair** | [**UserKeyPairContainer**](UserKeyPairContainer.md) |  |  [optional] |
|**mailBody** | **String** | &amp;#128679; Deprecated since v4.11.0  Notification email content |  [optional] |
|**mailRecipients** | **String** | &amp;#128679; Deprecated since v4.11.0  CSV string of recipient email addresses |  [optional] |
|**mailSubject** | **String** | &amp;#128679; Deprecated since v4.11.0  Notification email subject |  [optional] |
|**maxDownloads** | **Integer** | Max allowed downloads |  [optional] |
|**name** | **String** | Alias name  (default: name of the shared node) |  [optional] |
|**nodeId** | **Long** | Source node ID |  |
|**notes** | **String** | User notes |  [optional] |
|**notifyCreator** | **Boolean** | &amp;#128679; Deprecated since v4.20.0  Notify creator on every download. |  [optional] |
|**password** | **String** | Access password, not allowed for encrypted shares |  [optional] |
|**receiverLanguage** | **String** | Language tag for messages to receiver |  [optional] |
|**sendMail** | **Boolean** | &amp;#128679; Deprecated since v4.11.0  Notify recipients via email  Please use &#x60;POST /shares/downloads/{share_id}/email&#x60; API instead. |  [optional] |
|**sendSms** | **Boolean** | &amp;#128679; Deprecated since v4.11.0  Send share password via SMS  Please use &#x60;textMessageRecipients&#x60; attribute instead. |  [optional] |
|**showCreatorName** | **Boolean** | Show creator first and last name. |  [optional] |
|**showCreatorUsername** | **Boolean** | Show creator email address. |  [optional] |
|**smsRecipients** | **String** | &amp;#128679; Deprecated since v4.11.0  CSV string of recipient MSISDNs |  [optional] |
|**textMessageRecipients** | **List&lt;String&gt;** | &amp;#128640; Since v4.11.0  List of recipient FQTNs  E.123 / E.164 Format |  [optional] |



