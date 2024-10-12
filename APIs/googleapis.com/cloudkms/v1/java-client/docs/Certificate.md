

# Certificate

A Certificate represents an X.509 certificate used to authenticate HTTPS connections to EKM replicas.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**issuer** | **String** | Output only. The issuer distinguished name in RFC 2253 format. Only present if parsed is true. |  [optional] [readonly] |
|**notAfterTime** | **String** | Output only. The certificate is not valid after this time. Only present if parsed is true. |  [optional] [readonly] |
|**notBeforeTime** | **String** | Output only. The certificate is not valid before this time. Only present if parsed is true. |  [optional] [readonly] |
|**parsed** | **Boolean** | Output only. True if the certificate was parsed successfully. |  [optional] [readonly] |
|**rawDer** | **byte[]** | Required. The raw certificate bytes in DER format. |  [optional] |
|**serialNumber** | **String** | Output only. The certificate serial number as a hex string. Only present if parsed is true. |  [optional] [readonly] |
|**sha256Fingerprint** | **String** | Output only. The SHA-256 certificate fingerprint as a hex string. Only present if parsed is true. |  [optional] [readonly] |
|**subject** | **String** | Output only. The subject distinguished name in RFC 2253 format. Only present if parsed is true. |  [optional] [readonly] |
|**subjectAlternativeDnsNames** | **List&lt;String&gt;** | Output only. The subject Alternative DNS names. Only present if parsed is true. |  [optional] [readonly] |



