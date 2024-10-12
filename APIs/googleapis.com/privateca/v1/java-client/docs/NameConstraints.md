

# NameConstraints

Describes the X.509 name constraints extension, per https://tools.ietf.org/html/rfc5280#section-4.2.1.10

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**critical** | **Boolean** | Indicates whether or not the name constraints are marked critical. |  [optional] |
|**excludedDnsNames** | **List&lt;String&gt;** | Contains excluded DNS names. Any DNS name that can be constructed by simply adding zero or more labels to the left-hand side of the name satisfies the name constraint. For example, &#x60;example.com&#x60;, &#x60;www.example.com&#x60;, &#x60;www.sub.example.com&#x60; would satisfy &#x60;example.com&#x60; while &#x60;example1.com&#x60; does not. |  [optional] |
|**excludedEmailAddresses** | **List&lt;String&gt;** | Contains the excluded email addresses. The value can be a particular email address, a hostname to indicate all email addresses on that host or a domain with a leading period (e.g. &#x60;.example.com&#x60;) to indicate all email addresses in that domain. |  [optional] |
|**excludedIpRanges** | **List&lt;String&gt;** | Contains the excluded IP ranges. For IPv4 addresses, the ranges are expressed using CIDR notation as specified in RFC 4632. For IPv6 addresses, the ranges are expressed in similar encoding as IPv4 addresses. |  [optional] |
|**excludedUris** | **List&lt;String&gt;** | Contains the excluded URIs that apply to the host part of the name. The value can be a hostname or a domain with a leading period (like &#x60;.example.com&#x60;) |  [optional] |
|**permittedDnsNames** | **List&lt;String&gt;** | Contains permitted DNS names. Any DNS name that can be constructed by simply adding zero or more labels to the left-hand side of the name satisfies the name constraint. For example, &#x60;example.com&#x60;, &#x60;www.example.com&#x60;, &#x60;www.sub.example.com&#x60; would satisfy &#x60;example.com&#x60; while &#x60;example1.com&#x60; does not. |  [optional] |
|**permittedEmailAddresses** | **List&lt;String&gt;** | Contains the permitted email addresses. The value can be a particular email address, a hostname to indicate all email addresses on that host or a domain with a leading period (e.g. &#x60;.example.com&#x60;) to indicate all email addresses in that domain. |  [optional] |
|**permittedIpRanges** | **List&lt;String&gt;** | Contains the permitted IP ranges. For IPv4 addresses, the ranges are expressed using CIDR notation as specified in RFC 4632. For IPv6 addresses, the ranges are expressed in similar encoding as IPv4 addresses. |  [optional] |
|**permittedUris** | **List&lt;String&gt;** | Contains the permitted URIs that apply to the host part of the name. The value can be a hostname or a domain with a leading period (like &#x60;.example.com&#x60;) |  [optional] |



