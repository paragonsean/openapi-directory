# ComputeManagementClient.DedicatedHostProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoReplaceOnFailure** | **Boolean** | Specifies whether the dedicated host should be replaced automatically in case of a failure. The value is defaulted to &#39;true&#39; when not provided. | [optional] 
**hostId** | **String** | A unique id generated and assigned to the dedicated host by the platform. &lt;br&gt;&lt;br&gt; Does not change throughout the lifetime of the host. | [optional] [readonly] 
**instanceView** | [**DedicatedHostInstanceView**](DedicatedHostInstanceView.md) |  | [optional] 
**licenseType** | [**DedicatedHostLicenseType**](DedicatedHostLicenseType.md) |  | [optional] 
**platformFaultDomain** | **Number** | Fault domain of the dedicated host within a dedicated host group. | [optional] 
**provisioningState** | **String** | The provisioning state, which only appears in the response. | [optional] [readonly] 
**provisioningTime** | **Date** | The date when the host was first provisioned. | [optional] [readonly] 
**virtualMachines** | [**[SubResourceReadOnly]**](SubResourceReadOnly.md) | A list of references to all virtual machines in the Dedicated Host. | [optional] [readonly] 


