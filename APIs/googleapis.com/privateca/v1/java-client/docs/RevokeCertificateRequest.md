

# RevokeCertificateRequest

Request message for CertificateAuthorityService.RevokeCertificate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reason** | [**ReasonEnum**](#ReasonEnum) | Required. The RevocationReason for revoking this certificate. |  [optional] |
|**requestId** | **String** | Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| REVOCATION_REASON_UNSPECIFIED | &quot;REVOCATION_REASON_UNSPECIFIED&quot; |
| KEY_COMPROMISE | &quot;KEY_COMPROMISE&quot; |
| CERTIFICATE_AUTHORITY_COMPROMISE | &quot;CERTIFICATE_AUTHORITY_COMPROMISE&quot; |
| AFFILIATION_CHANGED | &quot;AFFILIATION_CHANGED&quot; |
| SUPERSEDED | &quot;SUPERSEDED&quot; |
| CESSATION_OF_OPERATION | &quot;CESSATION_OF_OPERATION&quot; |
| CERTIFICATE_HOLD | &quot;CERTIFICATE_HOLD&quot; |
| PRIVILEGE_WITHDRAWN | &quot;PRIVILEGE_WITHDRAWN&quot; |
| ATTRIBUTE_AUTHORITY_COMPROMISE | &quot;ATTRIBUTE_AUTHORITY_COMPROMISE&quot; |



