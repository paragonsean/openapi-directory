

# SubordinateConfig

Describes a subordinate CA's issuers. This is either a resource name to a known issuing CertificateAuthority, or a PEM issuer certificate chain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateAuthority** | **String** | Required. This can refer to a CertificateAuthority that was used to create a subordinate CertificateAuthority. This field is used for information and usability purposes only. The resource name is in the format &#x60;projects/_*_/locations/_*_/caPools/_*_/certificateAuthorities/_*&#x60;. |  [optional] |
|**pemIssuerChain** | [**SubordinateConfigChain**](SubordinateConfigChain.md) |  |  [optional] |



