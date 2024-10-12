# AppServicePlansApiClient.AppServicePlansListVnets200ResponseInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certBlob** | **Blob** | A certificate file (.cer) blob containing the public key of the private key used to authenticate a  Point-To-Site VPN connection. | [optional] 
**certThumbprint** | **String** | The client certificate thumbprint. | [optional] [readonly] 
**dnsServers** | **String** | DNS servers to be used by this Virtual Network. This should be a comma-separated list of IP addresses. | [optional] 
**resyncRequired** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if a resync is required; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] [readonly] 
**routes** | [**[AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner]**](AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner.md) | The routes that this Virtual Network connection uses. | [optional] [readonly] 
**vnetResourceId** | **String** | The Virtual Network&#39;s resource ID. | [optional] 


