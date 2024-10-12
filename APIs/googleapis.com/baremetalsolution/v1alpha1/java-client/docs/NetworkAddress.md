

# NetworkAddress

A network.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | IP address to be assigned to the server. |  [optional] |
|**existingNetworkId** | **String** | Name of the existing network to use. Will be of the format at--vlan for pre-intake UI networks like for eg, at-123456-vlan001 or any user-defined name like for eg, my-network-name for networks provisioned using intake UI. The field is exclusively filled only in case of an already existing network. Mutually exclusive with network_id. |  [optional] |
|**networkId** | **String** | Name of the network to use, within the same ProvisioningConfig request. This represents a new network being provisioned in the same request. Can have any user-defined name like for eg, my-network-name. Mutually exclusive with existing_network_id. |  [optional] |



