# ApiManagementClient.ApiManagementServiceBaseProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalLocations** | [**[AdditionalLocation]**](AdditionalLocation.md) | Additional datacenter locations of the API Management service. | [optional] 
**certificates** | [**[CertificateConfiguration]**](CertificateConfiguration.md) | List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10. | [optional] 
**createdAtUtc** | **Date** | Creation UTC date of the API Management service.The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard. | [optional] [readonly] 
**customProperties** | **{String: String}** | Custom properties of the API Management service. Setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168&#x60; will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2). Setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11&#x60; can be used to disable just TLS 1.1 and setting &#x60;Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10&#x60; can be used to disable TLS 1.0 on an API Management service. | [optional] 
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




