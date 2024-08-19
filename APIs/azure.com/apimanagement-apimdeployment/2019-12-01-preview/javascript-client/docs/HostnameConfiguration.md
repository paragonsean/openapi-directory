# ApiManagementClient.HostnameConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | [**CertificateInformation**](CertificateInformation.md) |  | [optional] 
**certificatePassword** | **String** | Certificate Password. | [optional] 
**defaultSslBinding** | **Boolean** | Specify true to setup the certificate associated with this Hostname as the Default SSL Certificate. If a client does not send the SNI header, then this will be the certificate that will be challenged. The property is useful if a service has multiple custom hostname enabled and it needs to decide on the default ssl certificate. The setting only applied to Proxy Hostname Type. | [optional] [default to false]
**encodedCertificate** | **String** | Base64 Encoded certificate. | [optional] 
**hostName** | **String** | Hostname to configure on the Api Management service. | 
**keyVaultId** | **String** | Url to the KeyVault Secret containing the Ssl Certificate. If absolute Url containing version is provided, auto-update of ssl certificate will not work. This requires Api Management service to be configured with MSI. The secret should be of type *application/x-pkcs12* | [optional] 
**negotiateClientCertificate** | **Boolean** | Specify true to always negotiate client certificate on the hostname. Default Value is false. | [optional] [default to false]
**type** | **String** | Hostname type. | 



## Enum: TypeEnum


* `Proxy` (value: `"Proxy"`)

* `Portal` (value: `"Portal"`)

* `Management` (value: `"Management"`)

* `Scm` (value: `"Scm"`)

* `DeveloperPortal` (value: `"DeveloperPortal"`)




