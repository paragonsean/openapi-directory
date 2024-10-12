# CertificateAuthorityApi.NameConstraints

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**critical** | **Boolean** | Indicates whether or not the name constraints are marked critical. | [optional] 
**excludedDnsNames** | **[String]** | Contains excluded DNS names. Any DNS name that can be constructed by simply adding zero or more labels to the left-hand side of the name satisfies the name constraint. For example, &#x60;example.com&#x60;, &#x60;www.example.com&#x60;, &#x60;www.sub.example.com&#x60; would satisfy &#x60;example.com&#x60; while &#x60;example1.com&#x60; does not. | [optional] 
**excludedEmailAddresses** | **[String]** | Contains the excluded email addresses. The value can be a particular email address, a hostname to indicate all email addresses on that host or a domain with a leading period (e.g. &#x60;.example.com&#x60;) to indicate all email addresses in that domain. | [optional] 
**excludedIpRanges** | **[String]** | Contains the excluded IP ranges. For IPv4 addresses, the ranges are expressed using CIDR notation as specified in RFC 4632. For IPv6 addresses, the ranges are expressed in similar encoding as IPv4 addresses. | [optional] 
**excludedUris** | **[String]** | Contains the excluded URIs that apply to the host part of the name. The value can be a hostname or a domain with a leading period (like &#x60;.example.com&#x60;) | [optional] 
**permittedDnsNames** | **[String]** | Contains permitted DNS names. Any DNS name that can be constructed by simply adding zero or more labels to the left-hand side of the name satisfies the name constraint. For example, &#x60;example.com&#x60;, &#x60;www.example.com&#x60;, &#x60;www.sub.example.com&#x60; would satisfy &#x60;example.com&#x60; while &#x60;example1.com&#x60; does not. | [optional] 
**permittedEmailAddresses** | **[String]** | Contains the permitted email addresses. The value can be a particular email address, a hostname to indicate all email addresses on that host or a domain with a leading period (e.g. &#x60;.example.com&#x60;) to indicate all email addresses in that domain. | [optional] 
**permittedIpRanges** | **[String]** | Contains the permitted IP ranges. For IPv4 addresses, the ranges are expressed using CIDR notation as specified in RFC 4632. For IPv6 addresses, the ranges are expressed in similar encoding as IPv4 addresses. | [optional] 
**permittedUris** | **[String]** | Contains the permitted URIs that apply to the host part of the name. The value can be a hostname or a domain with a leading period (like &#x60;.example.com&#x60;) | [optional] 


