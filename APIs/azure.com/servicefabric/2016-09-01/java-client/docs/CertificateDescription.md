

# CertificateDescription

Certificate details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**thumbprint** | **String** | Thumbprint of the primary certificate |  |
|**thumbprintSecondary** | **String** | Thumbprint of the secondary certificate |  [optional] |
|**x509StoreName** | [**X509StoreNameEnum**](#X509StoreNameEnum) | The local certificate store location |  [optional] |



## Enum: X509StoreNameEnum

| Name | Value |
|---- | -----|
| ADDRESS_BOOK | &quot;AddressBook&quot; |
| AUTH_ROOT | &quot;AuthRoot&quot; |
| CERTIFICATE_AUTHORITY | &quot;CertificateAuthority&quot; |
| DISALLOWED | &quot;Disallowed&quot; |
| MY | &quot;My&quot; |
| ROOT | &quot;Root&quot; |
| TRUSTED_PEOPLE | &quot;TrustedPeople&quot; |
| TRUSTED_PUBLISHER | &quot;TrustedPublisher&quot; |



