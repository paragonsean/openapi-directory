# CertificateAuthorityApi.RevokeCertificateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **String** | Required. The RevocationReason for revoking this certificate. | [optional] 
**requestId** | **String** | Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). | [optional] 



## Enum: ReasonEnum


* `REVOCATION_REASON_UNSPECIFIED` (value: `"REVOCATION_REASON_UNSPECIFIED"`)

* `KEY_COMPROMISE` (value: `"KEY_COMPROMISE"`)

* `CERTIFICATE_AUTHORITY_COMPROMISE` (value: `"CERTIFICATE_AUTHORITY_COMPROMISE"`)

* `AFFILIATION_CHANGED` (value: `"AFFILIATION_CHANGED"`)

* `SUPERSEDED` (value: `"SUPERSEDED"`)

* `CESSATION_OF_OPERATION` (value: `"CESSATION_OF_OPERATION"`)

* `CERTIFICATE_HOLD` (value: `"CERTIFICATE_HOLD"`)

* `PRIVILEGE_WITHDRAWN` (value: `"PRIVILEGE_WITHDRAWN"`)

* `ATTRIBUTE_AUTHORITY_COMPROMISE` (value: `"ATTRIBUTE_AUTHORITY_COMPROMISE"`)




