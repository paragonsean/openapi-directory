# VMwareCloudSimple.PrivateCloudProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilityZoneId** | **String** | Availability Zone id, e.g. \&quot;az1\&quot; | [optional] 
**availabilityZoneName** | **String** | Availability Zone name, e.g. \&quot;Availability Zone 1\&quot; | [optional] 
**clustersNumber** | **Number** | Number of clusters | [optional] 
**createdBy** | **String** | User&#39;s emails who created cloud | [optional] 
**createdOn** | **Date** | When private cloud was created | [optional] 
**dnsServers** | **[String]** | Array of DNS servers | [optional] 
**expires** | **String** | Expiration date of PC | [optional] 
**nsxType** | **String** | Nsx Type, e.g. \&quot;Advanced\&quot; | [optional] 
**placementGroupId** | **String** | Placement Group id, e.g. \&quot;n1\&quot; | [optional] 
**placementGroupName** | **String** | Placement Group name | [optional] 
**privateCloudId** | **String** | Id of a private cloud | [optional] 
**resourcePools** | [**[ResourcePool]**](ResourcePool.md) | The list of Resource Pools | [optional] 
**state** | **String** | Private Cloud state, e.g. \&quot;operational\&quot; | [optional] 
**totalCpuCores** | **Number** | Number of cores | [optional] 
**totalNodes** | **Number** | Number of nodes | [optional] 
**totalRam** | **Number** | Memory size | [optional] 
**totalStorage** | **Number** | Disk space in TB | [optional] 
**type** | **String** | Virtualization type e.g. \&quot;vSphere\&quot; | [optional] 
**vSphereVersion** | **String** | e.g. \&quot;6.5u2\&quot; | [optional] 
**vcenterFqdn** | **String** | FQDN for vcenter access | [optional] 
**vcenterRefid** | **String** | Vcenter ip address | [optional] 
**virtualMachineTemplates** | [**[VirtualMachineTemplate]**](VirtualMachineTemplate.md) | The list of Virtual Machine Templates | [optional] 
**virtualNetworks** | [**[VirtualNetwork]**](VirtualNetwork.md) | The list of Virtual Networks | [optional] 
**vrOpsEnabled** | **Boolean** | Is Vrops enabled/disabled | [optional] 


