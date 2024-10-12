

# UsableSubnetwork

UsableSubnetwork resource returns the subnetwork name, its associated network and the primary CIDR range.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipCidrRange** | **String** | The range of internal addresses that are owned by this subnetwork. |  [optional] |
|**network** | **String** | Network Name. Example: projects/my-project/global/networks/my-network |  [optional] |
|**secondaryIpRanges** | [**List&lt;UsableSubnetworkSecondaryRange&gt;**](UsableSubnetworkSecondaryRange.md) | Secondary IP ranges. |  [optional] |
|**statusMessage** | **String** | A human readable status message representing the reasons for cases where the caller cannot use the secondary ranges under the subnet. For example if the secondary_ip_ranges is empty due to a permission issue, an insufficient permission message will be given by status_message. |  [optional] |
|**subnetwork** | **String** | Subnetwork Name. Example: projects/my-project/regions/us-central1/subnetworks/my-subnet |  [optional] |



