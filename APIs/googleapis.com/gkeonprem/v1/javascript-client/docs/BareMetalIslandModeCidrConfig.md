# AnthosOnPremApi.BareMetalIslandModeCidrConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**podAddressCidrBlocks** | **[String]** | Required. All pods in the cluster are assigned an RFC1918 IPv4 address from these ranges. This field cannot be changed after creation. | [optional] 
**serviceAddressCidrBlocks** | **[String]** | Required. All services in the cluster are assigned an RFC1918 IPv4 address from these ranges. This field is mutable after creation starting with version 1.15. | [optional] 


