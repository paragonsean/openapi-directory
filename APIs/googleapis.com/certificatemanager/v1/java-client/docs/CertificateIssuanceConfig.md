

# CertificateIssuanceConfig

CertificateIssuanceConfig specifies how to issue and manage a certificate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateAuthorityConfig** | [**CertificateAuthorityConfig**](CertificateAuthorityConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. The creation timestamp of a CertificateIssuanceConfig. |  [optional] [readonly] |
|**description** | **String** | One or more paragraphs of text description of a CertificateIssuanceConfig. |  [optional] |
|**keyAlgorithm** | [**KeyAlgorithmEnum**](#KeyAlgorithmEnum) | Required. The key algorithm to use when generating the private key. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Set of labels associated with a CertificateIssuanceConfig. |  [optional] |
|**lifetime** | **String** | Required. Workload certificate lifetime requested. |  [optional] |
|**name** | **String** | A user-defined name of the certificate issuance config. CertificateIssuanceConfig names must be unique globally and match pattern &#x60;projects/_*_/locations/_*_/certificateIssuanceConfigs/_*&#x60;. |  [optional] |
|**rotationWindowPercentage** | **Integer** | Required. Specifies the percentage of elapsed time of the certificate lifetime to wait before renewing the certificate. Must be a number between 1-99, inclusive. |  [optional] |
|**updateTime** | **String** | Output only. The last update timestamp of a CertificateIssuanceConfig. |  [optional] [readonly] |



## Enum: KeyAlgorithmEnum

| Name | Value |
|---- | -----|
| KEY_ALGORITHM_UNSPECIFIED | &quot;KEY_ALGORITHM_UNSPECIFIED&quot; |
| RSA_2048 | &quot;RSA_2048&quot; |
| ECDSA_P256 | &quot;ECDSA_P256&quot; |



