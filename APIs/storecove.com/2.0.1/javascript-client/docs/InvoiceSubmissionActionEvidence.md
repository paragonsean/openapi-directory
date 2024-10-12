# StorecoveApi.InvoiceSubmissionActionEvidence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receiverResponse** | **String** | The response the receiver sent. | [optional] 
**transmissionDatetime** | **String** | The DateTime of the transmission, as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z. | [optional] 
**transmissionResult** | **String** | The result of this transmission. | [optional] 
**transmissionType** | **String** | How the document was transmitted. | [optional] 
**transmittedDocument** | **String** | The document that was transmitted. | [optional] 



## Enum: TransmissionResultEnum


* `unknown` (value: `"unknown"`)

* `accepted` (value: `"accepted"`)

* `rejected` (value: `"rejected"`)

* `send_error` (value: `"send_error"`)

* `internal_error` (value: `"internal_error"`)





## Enum: TransmissionTypeEnum


* `email` (value: `"email"`)

* `edi` (value: `"edi"`)

* `as2` (value: `"as2"`)

* `peppol` (value: `"peppol"`)

* `sandbox` (value: `"sandbox"`)




