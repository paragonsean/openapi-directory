

# PrivateCloudProperties

Properties of private

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilityZoneId** | **String** | Availability Zone id, e.g. \&quot;az1\&quot; |  [optional] |
|**availabilityZoneName** | **String** | Availability Zone name, e.g. \&quot;Availability Zone 1\&quot; |  [optional] |
|**clustersNumber** | **Integer** | Number of clusters |  [optional] |
|**createdBy** | **String** | User&#39;s emails who created cloud |  [optional] |
|**createdOn** | **OffsetDateTime** | When private cloud was created |  [optional] |
|**dnsServers** | **List&lt;String&gt;** | Array of DNS servers |  [optional] |
|**expires** | **String** | Expiration date of PC |  [optional] |
|**nsxType** | **String** | Nsx Type, e.g. \&quot;Advanced\&quot; |  [optional] |
|**placementGroupId** | **String** | Placement Group id, e.g. \&quot;n1\&quot; |  [optional] |
|**placementGroupName** | **String** | Placement Group name |  [optional] |
|**privateCloudId** | **UUID** | Id of a private cloud |  [optional] |
|**resourcePools** | [**List&lt;ResourcePool&gt;**](ResourcePool.md) | The list of Resource Pools |  [optional] |
|**state** | **String** | Private Cloud state, e.g. \&quot;operational\&quot; |  [optional] |
|**totalCpuCores** | **Integer** | Number of cores |  [optional] |
|**totalNodes** | **Integer** | Number of nodes |  [optional] |
|**totalRam** | **Integer** | Memory size |  [optional] |
|**totalStorage** | **BigDecimal** | Disk space in TB |  [optional] |
|**type** | **String** | Virtualization type e.g. \&quot;vSphere\&quot; |  [optional] |
|**vSphereVersion** | **String** | e.g. \&quot;6.5u2\&quot; |  [optional] |
|**vcenterFqdn** | **String** | FQDN for vcenter access |  [optional] |
|**vcenterRefid** | **String** | Vcenter ip address |  [optional] |
|**virtualMachineTemplates** | [**List&lt;VirtualMachineTemplate&gt;**](VirtualMachineTemplate.md) | The list of Virtual Machine Templates |  [optional] |
|**virtualNetworks** | [**List&lt;VirtualNetwork&gt;**](VirtualNetwork.md) | The list of Virtual Networks |  [optional] |
|**vrOpsEnabled** | **Boolean** | Is Vrops enabled/disabled |  [optional] |



