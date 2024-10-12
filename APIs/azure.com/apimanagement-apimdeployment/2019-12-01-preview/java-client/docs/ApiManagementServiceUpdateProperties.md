

# ApiManagementServiceUpdateProperties

Properties of an API Management service resource description.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**publisherEmail** | **String** | Publisher email. |  [optional] |
|**publisherName** | **String** | Publisher name. |  [optional] |
|**additionalLocations** | [**List&lt;AdditionalLocation&gt;**](AdditionalLocation.md) | Additional datacenter locations of the API Management service. |  [optional] |
|**apiVersionConstraint** | [**ApiVersionConstraint**](ApiVersionConstraint.md) |  |  [optional] |
|**certificates** | [**List&lt;CertificateConfiguration&gt;**](CertificateConfiguration.md) | List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10. |  [optional] |
|**createdAtUtc** | **OffsetDateTime** | Creation UTC date of the API Management service.The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard. |  [optional] [readonly] |
|**customProperties** | **Map&lt;String, String&gt;** | Custom properties of the API Management service.&lt;/br&gt;Setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168&#x60; will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2).&lt;/br&gt;Setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11&#x60; can be used to disable just TLS 1.1.&lt;/br&gt;Setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10&#x60; can be used to disable TLS 1.0 on an API Management service.&lt;/br&gt;Setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11&#x60; can be used to disable just TLS 1.1 for communications with backends.&lt;/br&gt;Setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10&#x60; can be used to disable TLS 1.0 for communications with backends.&lt;/br&gt;Setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2&#x60; can be used to enable HTTP2 protocol on an API Management service.&lt;/br&gt;Not specifying any of these properties on PATCH operation will reset omitted properties&#39; values to their defaults. For all the settings except Http2 the default value is &#x60;True&#x60; if the service was created on or before April 1st 2018 and &#x60;False&#x60; otherwise. Http2 setting&#39;s default value is &#x60;False&#x60;.&lt;/br&gt;&lt;/br&gt;You can disable any of next ciphers by using settings &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.[cipher_name]&#x60;: TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA. For example, &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TLS_RSA_WITH_AES_128_CBC_SHA256&#x60;:&#x60;false&#x60;. The default value is &#x60;true&#x60; for them.  Note: next ciphers can&#39;t be disabled since they are required by Azure CloudService internal components: TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384,TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256,TLS_RSA_WITH_AES_256_GCM_SHA384 |  [optional] |
|**developerPortalUrl** | **String** | DEveloper Portal endpoint URL of the API Management service. |  [optional] [readonly] |
|**disableGateway** | **Boolean** | Property only valid for an Api Management service deployed in multiple locations. This can be used to disable the gateway in master region. |  [optional] |
|**enableClientCertificate** | **Boolean** | Property only meant to be used for Consumption SKU Service. This enforces a client certificate to be presented on each request to the gateway. This also enables the ability to authenticate the certificate in the policy on the gateway. |  [optional] |
|**gatewayRegionalUrl** | **String** | Gateway URL of the API Management service in the Default Region. |  [optional] [readonly] |
|**gatewayUrl** | **String** | Gateway URL of the API Management service. |  [optional] [readonly] |
|**hostnameConfigurations** | [**List&lt;HostnameConfiguration&gt;**](HostnameConfiguration.md) | Custom hostname configuration of the API Management service. |  [optional] |
|**managementApiUrl** | **String** | Management API endpoint URL of the API Management service. |  [optional] [readonly] |
|**notificationSenderEmail** | **String** | Email address from which the notification will be sent. |  [optional] |
|**portalUrl** | **String** | Publisher portal endpoint Url of the API Management service. |  [optional] [readonly] |
|**privateIPAddresses** | **List&lt;String&gt;** | Private Static Load Balanced IP addresses of the API Management service in Primary region which is deployed in an Internal Virtual Network. Available only for Basic, Standard and Premium SKU. |  [optional] [readonly] |
|**provisioningState** | **String** | The current provisioning state of the API Management service which can be one of the following: Created/Activating/Succeeded/Updating/Failed/Stopped/Terminating/TerminationFailed/Deleted. |  [optional] [readonly] |
|**publicIPAddresses** | **List&lt;String&gt;** | Public Static Load Balanced IP addresses of the API Management service in Primary region. Available only for Basic, Standard and Premium SKU. |  [optional] [readonly] |
|**scmUrl** | **String** | SCM endpoint URL of the API Management service. |  [optional] [readonly] |
|**targetProvisioningState** | **String** | The provisioning state of the API Management service, which is targeted by the long running operation started on the service. |  [optional] [readonly] |
|**virtualNetworkConfiguration** | [**VirtualNetworkConfiguration**](VirtualNetworkConfiguration.md) |  |  [optional] |
|**virtualNetworkType** | [**VirtualNetworkTypeEnum**](#VirtualNetworkTypeEnum) | The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only. |  [optional] |



## Enum: VirtualNetworkTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| EXTERNAL | &quot;External&quot; |
| INTERNAL | &quot;Internal&quot; |



