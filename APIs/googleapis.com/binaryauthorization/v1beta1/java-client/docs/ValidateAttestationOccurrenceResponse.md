

# ValidateAttestationOccurrenceResponse

Response message for ValidationHelperV1.ValidateAttestationOccurrence.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**denialReason** | **String** | The reason for denial if the Attestation couldn&#39;t be validated. |  [optional] |
|**result** | [**ResultEnum**](#ResultEnum) | The result of the Attestation validation. |  [optional] |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| RESULT_UNSPECIFIED | &quot;RESULT_UNSPECIFIED&quot; |
| VERIFIED | &quot;VERIFIED&quot; |
| ATTESTATION_NOT_VERIFIABLE | &quot;ATTESTATION_NOT_VERIFIABLE&quot; |



