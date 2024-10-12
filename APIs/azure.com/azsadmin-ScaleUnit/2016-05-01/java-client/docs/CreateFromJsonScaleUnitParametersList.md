

# CreateFromJsonScaleUnitParametersList

A list of input data that allows for creating the new scale unit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterName** | **String** | Cluster name for the new scale unit. |  [optional] |
|**infrastructureNetwork** | [**NetworkDefinitionParameter**](NetworkDefinitionParameter.md) |  |  [optional] |
|**netQosPriority** | **Integer** | The network QOS priority setting. |  [optional] |
|**physicalNodes** | [**List&lt;DeploymentJsonPhysicalNodeParameters&gt;**](DeploymentJsonPhysicalNodeParameters.md) | List of nodes in the scale unit. |  [optional] |
|**softwareBgpAsn** | **String** | The software ASN for the cluster&#39;s rack. |  [optional] |
|**storageNetwork** | [**NetworkDefinitionParameter**](NetworkDefinitionParameter.md) |  |  [optional] |
|**torSwitchBgpAsn** | **String** | The ASN for the cluster&#39;s rack TOR. |  [optional] |
|**torSwitchBgpPeerIp** | **List&lt;String&gt;** | The list of IP addresses used for TOR communication. |  [optional] |



