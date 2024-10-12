

# InvoiceSubmissionActionEvidence


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**receiverResponse** | **String** | The response the receiver sent. |  [optional] |
|**transmissionDatetime** | **String** | The DateTime of the transmission, as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z. |  [optional] |
|**transmissionResult** | [**TransmissionResultEnum**](#TransmissionResultEnum) | The result of this transmission. |  [optional] |
|**transmissionType** | [**TransmissionTypeEnum**](#TransmissionTypeEnum) | How the document was transmitted. |  [optional] |
|**transmittedDocument** | **String** | The document that was transmitted. |  [optional] |



## Enum: TransmissionResultEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| ACCEPTED | &quot;accepted&quot; |
| REJECTED | &quot;rejected&quot; |
| SEND_ERROR | &quot;send_error&quot; |
| INTERNAL_ERROR | &quot;internal_error&quot; |



## Enum: TransmissionTypeEnum

| Name | Value |
|---- | -----|
| EMAIL | &quot;email&quot; |
| EDI | &quot;edi&quot; |
| AS2 | &quot;as2&quot; |
| PEPPOL | &quot;peppol&quot; |
| SANDBOX | &quot;sandbox&quot; |



