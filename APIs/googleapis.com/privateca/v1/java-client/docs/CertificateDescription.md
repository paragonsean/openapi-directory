

# CertificateDescription

A CertificateDescription describes an X.509 certificate or CSR that has been issued, as an alternative to using ASN.1 / X.509.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aiaIssuingCertificateUrls** | **List&lt;String&gt;** | Describes lists of issuer CA certificate URLs that appear in the \&quot;Authority Information Access\&quot; extension in the certificate. |  [optional] |
|**authorityKeyId** | [**KeyId**](KeyId.md) |  |  [optional] |
|**certFingerprint** | [**CertificateFingerprint**](CertificateFingerprint.md) |  |  [optional] |
|**crlDistributionPoints** | **List&lt;String&gt;** | Describes a list of locations to obtain CRL information, i.e. the DistributionPoint.fullName described by https://tools.ietf.org/html/rfc5280#section-4.2.1.13 |  [optional] |
|**publicKey** | [**PublicKey**](PublicKey.md) |  |  [optional] |
|**subjectDescription** | [**SubjectDescription**](SubjectDescription.md) |  |  [optional] |
|**subjectKeyId** | [**KeyId**](KeyId.md) |  |  [optional] |
|**x509Description** | [**X509Parameters**](X509Parameters.md) |  |  [optional] |



