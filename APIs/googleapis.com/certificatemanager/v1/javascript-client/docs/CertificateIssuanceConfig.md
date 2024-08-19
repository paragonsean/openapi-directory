# CertificateManagerApi.CertificateIssuanceConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificateAuthorityConfig** | [**CertificateAuthorityConfig**](CertificateAuthorityConfig.md) |  | [optional] 
**createTime** | **String** | Output only. The creation timestamp of a CertificateIssuanceConfig. | [optional] [readonly] 
**description** | **String** | One or more paragraphs of text description of a CertificateIssuanceConfig. | [optional] 
**keyAlgorithm** | **String** | Required. The key algorithm to use when generating the private key. | [optional] 
**labels** | **{String: String}** | Set of labels associated with a CertificateIssuanceConfig. | [optional] 
**lifetime** | **String** | Required. Workload certificate lifetime requested. | [optional] 
**name** | **String** | A user-defined name of the certificate issuance config. CertificateIssuanceConfig names must be unique globally and match pattern &#x60;projects/_*_/locations/_*_/certificateIssuanceConfigs/_*&#x60;. | [optional] 
**rotationWindowPercentage** | **Number** | Required. Specifies the percentage of elapsed time of the certificate lifetime to wait before renewing the certificate. Must be a number between 1-99, inclusive. | [optional] 
**updateTime** | **String** | Output only. The last update timestamp of a CertificateIssuanceConfig. | [optional] [readonly] 



## Enum: KeyAlgorithmEnum


* `KEY_ALGORITHM_UNSPECIFIED` (value: `"KEY_ALGORITHM_UNSPECIFIED"`)

* `RSA_2048` (value: `"RSA_2048"`)

* `ECDSA_P256` (value: `"ECDSA_P256"`)




