# CertificateAuthorityApi.SubordinateConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificateAuthority** | **String** | Required. This can refer to a CertificateAuthority that was used to create a subordinate CertificateAuthority. This field is used for information and usability purposes only. The resource name is in the format &#x60;projects/_*_/locations/_*_/caPools/_*_/certificateAuthorities/_*&#x60;. | [optional] 
**pemIssuerChain** | [**SubordinateConfigChain**](SubordinateConfigChain.md) |  | [optional] 


