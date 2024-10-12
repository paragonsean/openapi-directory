# AnthosOnPremApi.VmwareSeesawConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableHa** | **Boolean** | Enable two load balancer VMs to achieve a highly-available Seesaw load balancer. | [optional] 
**group** | **String** | Required. In general the following format should be used for the Seesaw group name: seesaw-for-[cluster_name]. | [optional] 
**ipBlocks** | [**[VmwareIpBlock]**](VmwareIpBlock.md) | Required. The IP Blocks to be used by the Seesaw load balancer | [optional] 
**masterIp** | **String** | Required. MasterIP is the IP announced by the master of Seesaw group. | [optional] 
**stackdriverName** | **String** | Name to be used by Stackdriver. | [optional] 
**vms** | **[String]** | Names of the VMs created for this Seesaw group. | [optional] 


