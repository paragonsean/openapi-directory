# FilesComApi.As2OutgoingMessageEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityLog** | **String** | JSON Structure of the activity log. | [optional] 
**as2From** | **String** | AS2 FROM | [optional] 
**as2PartnerId** | **Number** | Id of the AS2 Partner associated with this message. | [optional] 
**as2StationId** | **Number** | Id of the AS2 Station associated with this message. | [optional] 
**as2To** | **String** | AS2 TO | [optional] 
**attachmentFilename** | **String** | Filename of the file being sent. | [optional] 
**bodySize** | **String** | Encrypted Payload Body Size | [optional] 
**createdAt** | **Date** | Message creation date/time | [optional] 
**date** | **String** | Date Header | [optional] 
**encryptedUri** | **String** | URL to download the encrypted signed smime that is to sent as AS2 body | [optional] 
**httpHeaders** | **Object** | HTTP Headers sent with this message. | [optional] 
**httpResponseCode** | **String** | HTTP Response Code received for this message | [optional] 
**httpResponseHeaders** | **Object** | HTTP Headers received for this message. | [optional] 
**httpTransmissionDuration** | **Number** | HTTP transmission duration in seceonds | [optional] 
**id** | **Number** | Id of the AS2 Partner. | [optional] 
**mdnMessageIdMatched** | **Boolean** | MDN message id matched? | [optional] 
**mdnMicMatched** | **Boolean** | MDN MIC matched? | [optional] 
**mdnProcessingSuccess** | **Boolean** | MDN disposition indicate a successful processing? | [optional] 
**mdnReceived** | **Boolean** | Did the partner give a response body? | [optional] 
**mdnResponseUri** | **String** | URL to download the http response body | [optional] 
**mdnSignatureVerified** | **Boolean** | MDN signature verified? | [optional] 
**mdnValid** | **Boolean** | Is the response in MDN format? | [optional] 
**messageId** | **String** | AS2 Message Id | [optional] 
**mic** | **String** | AS2 Message Integrity Check SHA1 | [optional] 
**micSha256** | **String** | AS2 Message Integrity Check SHA256 | [optional] 
**processingResult** | **String** | Result of processing. | [optional] 
**processingResultDescription** | **String** | Result of processing description. | [optional] 
**rawUri** | **String** | URL to download the original file contents | [optional] 
**smimeSignedUri** | **String** | URL to download the file contents as smime with signature | [optional] 
**smimeUri** | **String** | URL to download the file contents encoded as smime | [optional] 
**uuid** | **String** | UUID assigned to this message. | [optional] 



## Enum: ProcessingResultEnum


* `not_started` (value: `"not_started"`)

* `send_failed` (value: `"send_failed"`)

* `send_success` (value: `"send_success"`)

* `send_success_mdn_invalid` (value: `"send_success_mdn_invalid"`)

* `send_success_mic_mismatch` (value: `"send_success_mic_mismatch"`)

* `send_success_message_id_mismatch` (value: `"send_success_message_id_mismatch"`)

* `send_success_signature_mismatch` (value: `"send_success_signature_mismatch"`)

* `send_success_processing_failure` (value: `"send_success_processing_failure"`)

* `send_failed_unknown_host` (value: `"send_failed_unknown_host"`)

* `send_failed_bad_http_response_code` (value: `"send_failed_bad_http_response_code"`)

* `send_failed_ssl_error` (value: `"send_failed_ssl_error"`)

* `send_failed_connection_refused` (value: `"send_failed_connection_refused"`)




