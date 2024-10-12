

# LdapsSettings

Secure LDAP Settings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateNotAfter** | **OffsetDateTime** | NotAfter DateTime of configure ldaps certificate. |  [optional] [readonly] |
|**certificateThumbprint** | **String** | Thumbprint of configure ldaps certificate. |  [optional] [readonly] |
|**externalAccess** | [**ExternalAccessEnum**](#ExternalAccessEnum) | A flag to determine whether or not Secure LDAP access over the internet is enabled or disabled. |  [optional] |
|**externalAccessIpAddress** | **String** | External access ip address. |  [optional] [readonly] |
|**ldaps** | [**LdapsEnum**](#LdapsEnum) | A flag to determine whether or not Secure LDAP is enabled or disabled. |  [optional] |
|**pfxCertificate** | **String** | The certificate required to configure Secure LDAP. The parameter passed here should be a base64encoded representation of the certificate pfx file. |  [optional] |
|**pfxCertificatePassword** | **String** | The password to decrypt the provided Secure LDAP certificate pfx file. |  [optional] |
|**publicCertificate** | **String** | Public certificate used to configure secure ldap. |  [optional] [readonly] |



## Enum: ExternalAccessEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: LdapsEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



