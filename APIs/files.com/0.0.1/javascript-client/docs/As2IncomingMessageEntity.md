# FilesComApi.As2IncomingMessageEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityLog** | **String** | JSON Structure of the activity log. | [optional] 
**as2From** | **String** | AS2 FROM header of message | [optional] 
**as2PartnerId** | **Number** | Id of the AS2 Partner associated with this message. | [optional] 
**as2StationId** | **Number** | Id of the AS2 Station associated with this message. | [optional] 
**as2To** | **String** | AS2 TO header of message | [optional] 
**attachmentFilename** | **String** | Filename of the file being received. | [optional] 
**bodySize** | **String** | Encrypted Payload Body Size | [optional] 
**contentType** | **String** | Content Type header of the incoming message. | [optional] 
**createdAt** | **Date** | Message creation date/time | [optional] 
**date** | **String** | Date Header | [optional] 
**encryptedUri** | **String** | URL to download the encrypted signed smime that is to sent as AS2 body | [optional] 
**hexRecipientSerial** | **String** | Incoming Message Recipient(the Client Cert used to encrypt this message)&#39;s serial in hex format. | [optional] 
**httpHeaders** | **Object** | HTTP Headers sent with this message. | [optional] 
**httpResponseCode** | **String** | HTTP Response Code sent for this message | [optional] 
**httpResponseHeaders** | **Object** | HTTP Headers sent for this message. | [optional] 
**id** | **Number** | Id of the AS2 Partner. | [optional] 
**ip** | **String** | IP Address of the Sender | [optional] 
**mdnResponseUri** | **String** | URL to download the http response body | [optional] 
**messageDecrypted** | **Boolean** | Message decrypted successfully? | [optional] 
**messageId** | **String** | AS2 Message Id | [optional] 
**messageMdnReturned** | **Boolean** | MDN returned? | [optional] 
**messageProcessingSuccess** | **Boolean** | Message processed successfully? | [optional] 
**messageReceived** | **Boolean** | Message body received? | [optional] 
**messageSignatureVerified** | **Boolean** | Message signature verified? | [optional] 
**mic** | **String** | AS2 Message Integrity Check | [optional] 
**micAlgo** | **String** | AS2 Message Integrity Check Algorithm Used | [optional] 
**processingResult** | **String** | Result of processing. | [optional] 
**processingResultDescription** | **String** | Result of processing description. | [optional] 
**rawUri** | **String** | URL to download the original file contents | [optional] 
**recipientIssuer** | **String** | Incoming Message Recipient(the Client Cert used to encrypt this message)&#39;s issuer | [optional] 
**recipientSerial** | **String** | Incoming Message Recipient(the Client Cert used to encrypt this message)&#39;s serial | [optional] 
**smimeSignedUri** | **String** | URL to download the file contents as smime with signature | [optional] 
**smimeUri** | **String** | URL to download the file contents encoded as smime | [optional] 
**subject** | **String** | AS2 Subject Header | [optional] 
**uuid** | **String** | UUID assigned to this message. | [optional] 



## Enum: ProcessingResultEnum


* `not_started` (value: `"not_started"`)

* `unable_to_find_station` (value: `"unable_to_find_station"`)

* `unable_to_find_partner` (value: `"unable_to_find_partner"`)

* `unable_to_validate_signature` (value: `"unable_to_validate_signature"`)

* `decrypt_fail` (value: `"decrypt_fail"`)

* `file_save_fail` (value: `"file_save_fail"`)

* `success` (value: `"success"`)




