

# BareMetalAdminIslandModeCidrConfig

BareMetalAdminIslandModeCidrConfig specifies the cluster CIDR configuration while running in island mode.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**podAddressCidrBlocks** | **List&lt;String&gt;** | Required. All pods in the cluster are assigned an RFC1918 IPv4 address from these ranges. This field cannot be changed after creation. |  [optional] |
|**serviceAddressCidrBlocks** | **List&lt;String&gt;** | Required. All services in the cluster are assigned an RFC1918 IPv4 address from these ranges. This field cannot be changed after creation. |  [optional] |



