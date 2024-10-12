# VMwareEngineApi.IpRange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**externalAddress** | **String** | The name of an &#x60;ExternalAddress&#x60; resource. The external address must have been reserved in the scope of this external access rule&#39;s parent network policy. Provide the external address name in the form of &#x60;projects/{project}/locations/{location}/privateClouds/{private_cloud}/externalAddresses/{external_address}&#x60;. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-address&#x60;. | [optional] 
**ipAddress** | **String** | A single IP address. For example: &#x60;10.0.0.5&#x60;. | [optional] 
**ipAddressRange** | **String** | An IP address range in the CIDR format. For example: &#x60;10.0.0.0/24&#x60;. | [optional] 


