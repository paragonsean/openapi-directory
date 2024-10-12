# KubernetesEngineApi.MasterAuthorizedNetworksConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidrBlocks** | [**[CidrBlock]**](CidrBlock.md) | cidr_blocks define up to 50 external networks that could access Kubernetes master through HTTPS. | [optional] 
**enabled** | **Boolean** | Whether or not master authorized networks is enabled. | [optional] 
**gcpPublicCidrsAccessEnabled** | **Boolean** | Whether master is accessbile via Google Compute Engine Public IP addresses. | [optional] 


