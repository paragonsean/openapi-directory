

# RoutingVPC

RoutingVPC contains information about the VPC networks associated with the spokes of a Network Connectivity Center hub.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requiredForNewSiteToSiteDataTransferSpokes** | **Boolean** | Output only. If true, indicates that this VPC network is currently associated with spokes that use the data transfer feature (spokes where the site_to_site_data_transfer field is set to true). If you create new spokes that use data transfer, they must be associated with this VPC network. At most, one VPC network will have this field set to true. |  [optional] [readonly] |
|**uri** | **String** | The URI of the VPC network. |  [optional] |



