# DracoonApi.UpdateUploadShareRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultCountry** | **String** | Country shorthand symbol (cf. ISO 3166-2) | [optional] 
**expiration** | [**ObjectExpiration**](ObjectExpiration.md) |  | [optional] 
**filesExpiryPeriod** | **Number** | Number of days after which uploaded files expire | [optional] 
**internalNotes** | **String** | &amp;#128640; Since v4.11.0  Internal notes | [optional] 
**maxSize** | **Number** | Maximal total size of uploaded files (in bytes) | [optional] 
**maxSlots** | **Number** | Maximal amount of files to upload | [optional] 
**name** | **String** | Alias name | [optional] 
**notes** | **String** | User notes | [optional] 
**notifyCreator** | **Boolean** | &amp;#128679; Deprecated since v4.20.0  Notify creator on every upload. | [optional] 
**password** | **String** | Password | [optional] 
**receiverLanguage** | **String** | Language tag for messages to receiver | [optional] 
**resetFilesExpiryPeriod** | **Boolean** | Set &#39;true&#39; to reset &#39;filesExpiryPeriod&#39; for Upload Share | [optional] 
**resetMaxSize** | **Boolean** | Set &#39;true&#39; to reset &#39;maxSize&#39; for Upload Share | [optional] 
**resetMaxSlots** | **Boolean** | Set &#39;true&#39; to reset &#39;maxSlots&#39; for Upload Share | [optional] 
**resetPassword** | **Boolean** | Set &#39;true&#39; to reset &#39;password&#39; for Upload Share. | [optional] 
**showCreatorName** | **Boolean** | Show creator first and last name. | [optional] 
**showCreatorUsername** | **Boolean** | Show creator email address. | [optional] 
**showUploadedFiles** | **Boolean** | Allow display of already uploaded files | [optional] 
**textMessageRecipients** | **[String]** | List of recipient FQTNs  E.123 / E.164 Format | [optional] 


