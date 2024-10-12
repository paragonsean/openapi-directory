

# ManagedCertificate

Configuration and state of a Managed Certificate. Certificate Manager provisions and renews Managed Certificates automatically, for as long as it's authorized to do so.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationAttemptInfo** | [**List&lt;AuthorizationAttemptInfo&gt;**](AuthorizationAttemptInfo.md) | Output only. Detailed state of the latest authorization attempt for each domain specified for managed certificate resource. |  [optional] [readonly] |
|**dnsAuthorizations** | **List&lt;String&gt;** | Immutable. Authorizations that will be used for performing domain authorization. |  [optional] |
|**domains** | **List&lt;String&gt;** | Immutable. The domains for which a managed SSL certificate will be generated. Wildcard domains are only supported with DNS challenge resolution. |  [optional] |
|**issuanceConfig** | **String** | Immutable. The resource name for a CertificateIssuanceConfig used to configure private PKI certificates in the format &#x60;projects/_*_/locations/_*_/certificateIssuanceConfigs/_*&#x60;. If this field is not set, the certificates will instead be publicly signed as documented at https://cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#caa. |  [optional] |
|**provisioningIssue** | [**ProvisioningIssue**](ProvisioningIssue.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the managed certificate resource. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PROVISIONING | &quot;PROVISIONING&quot; |
| FAILED | &quot;FAILED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |



