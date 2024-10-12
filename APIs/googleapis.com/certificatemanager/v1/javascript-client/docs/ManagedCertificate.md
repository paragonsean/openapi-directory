# CertificateManagerApi.ManagedCertificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationAttemptInfo** | [**[AuthorizationAttemptInfo]**](AuthorizationAttemptInfo.md) | Output only. Detailed state of the latest authorization attempt for each domain specified for managed certificate resource. | [optional] [readonly] 
**dnsAuthorizations** | **[String]** | Immutable. Authorizations that will be used for performing domain authorization. | [optional] 
**domains** | **[String]** | Immutable. The domains for which a managed SSL certificate will be generated. Wildcard domains are only supported with DNS challenge resolution. | [optional] 
**issuanceConfig** | **String** | Immutable. The resource name for a CertificateIssuanceConfig used to configure private PKI certificates in the format &#x60;projects/_*_/locations/_*_/certificateIssuanceConfigs/_*&#x60;. If this field is not set, the certificates will instead be publicly signed as documented at https://cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#caa. | [optional] 
**provisioningIssue** | [**ProvisioningIssue**](ProvisioningIssue.md) |  | [optional] 
**state** | **String** | Output only. State of the managed certificate resource. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PROVISIONING` (value: `"PROVISIONING"`)

* `FAILED` (value: `"FAILED"`)

* `ACTIVE` (value: `"ACTIVE"`)




