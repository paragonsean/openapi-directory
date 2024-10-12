

# As2OutgoingMessageEntity

List As2 Outgoing Messages

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityLog** | **String** | JSON Structure of the activity log. |  [optional] |
|**as2From** | **String** | AS2 FROM |  [optional] |
|**as2PartnerId** | **Integer** | Id of the AS2 Partner associated with this message. |  [optional] |
|**as2StationId** | **Integer** | Id of the AS2 Station associated with this message. |  [optional] |
|**as2To** | **String** | AS2 TO |  [optional] |
|**attachmentFilename** | **String** | Filename of the file being sent. |  [optional] |
|**bodySize** | **String** | Encrypted Payload Body Size |  [optional] |
|**createdAt** | **OffsetDateTime** | Message creation date/time |  [optional] |
|**date** | **String** | Date Header |  [optional] |
|**encryptedUri** | **String** | URL to download the encrypted signed smime that is to sent as AS2 body |  [optional] |
|**httpHeaders** | **Object** | HTTP Headers sent with this message. |  [optional] |
|**httpResponseCode** | **String** | HTTP Response Code received for this message |  [optional] |
|**httpResponseHeaders** | **Object** | HTTP Headers received for this message. |  [optional] |
|**httpTransmissionDuration** | **Double** | HTTP transmission duration in seceonds |  [optional] |
|**id** | **Integer** | Id of the AS2 Partner. |  [optional] |
|**mdnMessageIdMatched** | **Boolean** | MDN message id matched? |  [optional] |
|**mdnMicMatched** | **Boolean** | MDN MIC matched? |  [optional] |
|**mdnProcessingSuccess** | **Boolean** | MDN disposition indicate a successful processing? |  [optional] |
|**mdnReceived** | **Boolean** | Did the partner give a response body? |  [optional] |
|**mdnResponseUri** | **String** | URL to download the http response body |  [optional] |
|**mdnSignatureVerified** | **Boolean** | MDN signature verified? |  [optional] |
|**mdnValid** | **Boolean** | Is the response in MDN format? |  [optional] |
|**messageId** | **String** | AS2 Message Id |  [optional] |
|**mic** | **String** | AS2 Message Integrity Check SHA1 |  [optional] |
|**micSha256** | **String** | AS2 Message Integrity Check SHA256 |  [optional] |
|**processingResult** | [**ProcessingResultEnum**](#ProcessingResultEnum) | Result of processing. |  [optional] |
|**processingResultDescription** | **String** | Result of processing description. |  [optional] |
|**rawUri** | **String** | URL to download the original file contents |  [optional] |
|**smimeSignedUri** | **String** | URL to download the file contents as smime with signature |  [optional] |
|**smimeUri** | **String** | URL to download the file contents encoded as smime |  [optional] |
|**uuid** | **String** | UUID assigned to this message. |  [optional] |



## Enum: ProcessingResultEnum

| Name | Value |
|---- | -----|
| NOT_STARTED | &quot;not_started&quot; |
| SEND_FAILED | &quot;send_failed&quot; |
| SEND_SUCCESS | &quot;send_success&quot; |
| SEND_SUCCESS_MDN_INVALID | &quot;send_success_mdn_invalid&quot; |
| SEND_SUCCESS_MIC_MISMATCH | &quot;send_success_mic_mismatch&quot; |
| SEND_SUCCESS_MESSAGE_ID_MISMATCH | &quot;send_success_message_id_mismatch&quot; |
| SEND_SUCCESS_SIGNATURE_MISMATCH | &quot;send_success_signature_mismatch&quot; |
| SEND_SUCCESS_PROCESSING_FAILURE | &quot;send_success_processing_failure&quot; |
| SEND_FAILED_UNKNOWN_HOST | &quot;send_failed_unknown_host&quot; |
| SEND_FAILED_BAD_HTTP_RESPONSE_CODE | &quot;send_failed_bad_http_response_code&quot; |
| SEND_FAILED_SSL_ERROR | &quot;send_failed_ssl_error&quot; |
| SEND_FAILED_CONNECTION_REFUSED | &quot;send_failed_connection_refused&quot; |



