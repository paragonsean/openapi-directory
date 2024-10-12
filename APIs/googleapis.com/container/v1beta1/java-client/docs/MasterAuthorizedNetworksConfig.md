

# MasterAuthorizedNetworksConfig

Configuration options for the master authorized networks feature. Enabled master authorized networks will disallow all external traffic to access Kubernetes master through HTTPS except traffic from the given CIDR blocks, Google Compute Engine Public IPs and Google Prod IPs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cidrBlocks** | [**List&lt;CidrBlock&gt;**](CidrBlock.md) | cidr_blocks define up to 10 external networks that could access Kubernetes master through HTTPS. |  [optional] |
|**enabled** | **Boolean** | Whether or not master authorized networks is enabled. |  [optional] |
|**gcpPublicCidrsAccessEnabled** | **Boolean** | Whether master is accessbile via Google Compute Engine Public IP addresses. |  [optional] |



