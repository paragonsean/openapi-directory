# ApiManagementClient.ApiManagementServiceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publisherEmail** | **String** | Publisher email. | 
**publisherName** | **String** | Publisher name. | 
**additionalLocations** | [**[AdditionalLocation]**](AdditionalLocation.md) | Additional datacenter locations of the API Management service. | [optional] 
**certificates** | [**[CertificateConfiguration]**](CertificateConfiguration.md) | List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10. | [optional] 
**createdAtUtc** | **Date** | Creation UTC date of the API Management service.The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard. | [optional] [readonly] 
**customProperties** | **{String: String}** | Custom properties of the API Management service.&lt;/br&gt;Setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168&#x60; will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2).&lt;/br&gt;Setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11&#x60; can be used to disable just TLS 1.1.&lt;/br&gt;Setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10&#x60; can be used to disable TLS 1.0 on an API Management service.&lt;/br&gt;Setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11&#x60; can be used to disable just TLS 1.1 for communications with backends.&lt;/br&gt;Setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10&#x60; can be used to disable TLS 1.0 for communications with backends.&lt;/br&gt;Setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2&#x60; can be used to enable HTTP2 protocol on an API Management service.&lt;/br&gt;Not specifying any of these properties on PATCH operation will reset omitted properties&#39; values to their defaults. For all the settings except Http2 the default value is &#x60;True&#x60; if the service was created on or before April 1st 2018 and &#x60;False&#x60; otherwise. Http2 setting&#39;s default value is &#x60;False&#x60;.&lt;/br&gt;&lt;/br&gt;You can disable any of next ciphers by using settings &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.[cipher_name]&#x60;: TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA. For example, &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TLS_RSA_WITH_AES_128_CBC_SHA256&#x60;:&#x60;false&#x60;. The default value is &#x60;true&#x60; for them. | [optional] 
**enableClientCertificate** | **Boolean** | Property only meant to be used for Consumption SKU Service. This enforces a client certificate to be presented on each request to the gateway. This also enables the ability to authenticate the certificate in the policy on the gateway. | [optional] [default to false]
**gatewayRegionalUrl** | **String** | Gateway URL of the API Management service in the Default Region. | [optional] [readonly] 
**gatewayUrl** | **String** | Gateway URL of the API Management service. | [optional] [readonly] 
**hostnameConfigurations** | [**[HostnameConfiguration]**](HostnameConfiguration.md) | Custom hostname configuration of the API Management service. | [optional] 
**managementApiUrl** | **String** | Management API endpoint URL of the API Management service. | [optional] [readonly] 
**notificationSenderEmail** | **String** | Email address from which the notification will be sent. | [optional] 
**portalUrl** | **String** | Publisher portal endpoint Url of the API Management service. | [optional] [readonly] 
**privateIPAddresses** | **[String]** | Private Static Load Balanced IP addresses of the API Management service in Primary region which is deployed in an Internal Virtual Network. Available only for Basic, Standard and Premium SKU. | [optional] [readonly] 
**provisioningState** | **String** | The current provisioning state of the API Management service which can be one of the following: Created/Activating/Succeeded/Updating/Failed/Stopped/Terminating/TerminationFailed/Deleted. | [optional] [readonly] 
**publicIPAddresses** | **[String]** | Public Static Load Balanced IP addresses of the API Management service in Primary region. Available only for Basic, Standard and Premium SKU. | [optional] [readonly] 
**scmUrl** | **String** | SCM endpoint URL of the API Management service. | [optional] [readonly] 
**targetProvisioningState** | **String** | The provisioning state of the API Management service, which is targeted by the long running operation started on the service. | [optional] [readonly] 
**virtualNetworkConfiguration** | [**VirtualNetworkConfiguration**](VirtualNetworkConfiguration.md) |  | [optional] 
**virtualNetworkType** | **String** | The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only. | [optional] [default to &#39;None&#39;]



## Enum: VirtualNetworkTypeEnum


* `None` (value: `"None"`)

* `External` (value: `"External"`)

* `Internal` (value: `"Internal"`)




