

# SubjectAltNames

SubjectAltNames corresponds to a more modern way of listing what the asserted identity is in a certificate (i.e., compared to the \"common name\" in the distinguished name).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customSans** | [**List&lt;X509Extension&gt;**](X509Extension.md) | Contains additional subject alternative name values. For each custom_san, the &#x60;value&#x60; field must contain an ASN.1 encoded UTF8String. |  [optional] |
|**dnsNames** | **List&lt;String&gt;** | Contains only valid, fully-qualified host names. |  [optional] |
|**emailAddresses** | **List&lt;String&gt;** | Contains only valid RFC 2822 E-mail addresses. |  [optional] |
|**ipAddresses** | **List&lt;String&gt;** | Contains only valid 32-bit IPv4 addresses or RFC 4291 IPv6 addresses. |  [optional] |
|**uris** | **List&lt;String&gt;** | Contains only valid RFC 3986 URIs. |  [optional] |



