

# UpdateDownloadShareRequest

Request model for updating a Download Share

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultCountry** | **String** | Country shorthand symbol (cf. ISO 3166-2) |  [optional] |
|**expiration** | [**ObjectExpiration**](ObjectExpiration.md) |  |  [optional] |
|**internalNotes** | **String** | &amp;#128640; Since v4.11.0  Internal notes |  [optional] |
|**maxDownloads** | **Integer** | Max allowed downloads |  [optional] |
|**name** | **String** | Alias name |  [optional] |
|**notes** | **String** | User notes |  [optional] |
|**notifyCreator** | **Boolean** | &amp;#128679; Deprecated since v4.20.0  Notify creator on every download. |  [optional] |
|**password** | **String** | Access password, not allowed for encrypted shares |  [optional] |
|**receiverLanguage** | **String** | Language tag for messages to receiver |  [optional] |
|**resetMaxDownloads** | **Boolean** | Set &#39;true&#39; to reset &#39;maxDownloads&#39; for Download Share. |  [optional] |
|**resetPassword** | **Boolean** | Set &#39;true&#39; to reset &#39;password&#39; for Download Share. |  [optional] |
|**showCreatorName** | **Boolean** | Show creator first and last name. |  [optional] |
|**showCreatorUsername** | **Boolean** | Show creator email address. |  [optional] |
|**textMessageRecipients** | **List&lt;String&gt;** | List of recipient FQTNs  E.123 / E.164 Format |  [optional] |



