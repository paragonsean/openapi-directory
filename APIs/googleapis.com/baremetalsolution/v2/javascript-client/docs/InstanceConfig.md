# BareMetalSolutionApi.InstanceConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNetworksEnabled** | **Boolean** | If true networks can be from different projects of the same vendor account. | [optional] 
**clientNetwork** | [**NetworkAddress**](NetworkAddress.md) |  | [optional] 
**hyperthreading** | **Boolean** | Whether the instance should be provisioned with Hyperthreading enabled. | [optional] 
**id** | **String** | A transient unique identifier to idenfity an instance within an ProvisioningConfig request. | [optional] 
**instanceType** | **String** | Instance type. [Available types](https://cloud.google.com/bare-metal/docs/bms-planning#server_configurations) | [optional] 
**kmsKeyVersion** | **String** | Name of the KMS crypto key version used to encrypt the initial passwords. The key has to have ASYMMETRIC_DECRYPT purpose. | [optional] 
**logicalInterfaces** | [**[GoogleCloudBaremetalsolutionV2LogicalInterface]**](GoogleCloudBaremetalsolutionV2LogicalInterface.md) | List of logical interfaces for the instance. The number of logical interfaces will be the same as number of hardware bond/nic on the chosen network template. Filled if InstanceConfig.multivlan_config is true. | [optional] 
**name** | **String** | The name of the instance config. | [optional] 
**networkConfig** | **String** | The type of network configuration on the instance. | [optional] 
**networkTemplate** | **String** | Server network template name. Filled if InstanceConfig.multivlan_config is true. | [optional] 
**osImage** | **String** | OS image to initialize the instance. [Available images](https://cloud.google.com/bare-metal/docs/bms-planning#server_configurations) | [optional] 
**privateNetwork** | [**NetworkAddress**](NetworkAddress.md) |  | [optional] 
**sshKeyNames** | **[String]** | Optional. List of names of ssh keys used to provision the instance. | [optional] 
**userNote** | **String** | User note field, it can be used by customers to add additional information for the BMS Ops team . | [optional] 



## Enum: NetworkConfigEnum


* `NETWORKCONFIG_UNSPECIFIED` (value: `"NETWORKCONFIG_UNSPECIFIED"`)

* `SINGLE_VLAN` (value: `"SINGLE_VLAN"`)

* `MULTI_VLAN` (value: `"MULTI_VLAN"`)




