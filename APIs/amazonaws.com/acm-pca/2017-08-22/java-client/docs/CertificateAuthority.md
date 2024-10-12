

# CertificateAuthority

Contains information about your private certificate authority (CA). Your private CA can issue and revoke X.509 digital certificates. Digital certificates verify that the entity named in the certificate <b>Subject</b> field owns or controls the public key contained in the <b>Subject Public Key Info</b> field. Call the <a href=\"https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html\">CreateCertificateAuthority</a> action to create your private CA. You must then call the <a href=\"https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCertificate.html\">GetCertificateAuthorityCertificate</a> action to retrieve a private CA certificate signing request (CSR). Sign the CSR with your Amazon Web Services Private CA-hosted or on-premises root or subordinate CA certificate. Call the <a href=\"https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html\">ImportCertificateAuthorityCertificate</a> action to import the signed certificate into Certificate Manager (ACM). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  [optional] |
|**ownerAccount** | [**String**](String.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastStateChangeAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**type** | [**CertificateAuthorityType**](CertificateAuthorityType.md) |  |  [optional] |
|**serial** | [**String**](String.md) |  |  [optional] |
|**status** | [**CertificateAuthorityStatus**](CertificateAuthorityStatus.md) |  |  [optional] |
|**notBefore** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**notAfter** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**failureReason** | [**FailureReason**](FailureReason.md) |  |  [optional] |
|**certificateAuthorityConfiguration** | [**CertificateAuthorityCertificateAuthorityConfiguration**](CertificateAuthorityCertificateAuthorityConfiguration.md) |  |  [optional] |
|**revocationConfiguration** | [**CertificateAuthorityRevocationConfiguration**](CertificateAuthorityRevocationConfiguration.md) |  |  [optional] |
|**restorableUntil** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**keyStorageSecurityStandard** | [**KeyStorageSecurityStandard**](KeyStorageSecurityStandard.md) |  |  [optional] |
|**usageMode** | [**CertificateAuthorityUsageMode**](CertificateAuthorityUsageMode.md) |  |  [optional] |



