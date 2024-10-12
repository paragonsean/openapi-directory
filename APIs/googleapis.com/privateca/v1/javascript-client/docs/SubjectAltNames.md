# CertificateAuthorityApi.SubjectAltNames

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customSans** | [**[X509Extension]**](X509Extension.md) | Contains additional subject alternative name values. For each custom_san, the &#x60;value&#x60; field must contain an ASN.1 encoded UTF8String. | [optional] 
**dnsNames** | **[String]** | Contains only valid, fully-qualified host names. | [optional] 
**emailAddresses** | **[String]** | Contains only valid RFC 2822 E-mail addresses. | [optional] 
**ipAddresses** | **[String]** | Contains only valid 32-bit IPv4 addresses or RFC 4291 IPv6 addresses. | [optional] 
**uris** | **[String]** | Contains only valid RFC 3986 URIs. | [optional] 


