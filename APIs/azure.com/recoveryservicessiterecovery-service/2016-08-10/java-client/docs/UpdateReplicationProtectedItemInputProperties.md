

# UpdateReplicationProtectedItemInputProperties

Update protected item input properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableRDPOnTargetOption** | **String** | The selected option to enable RDP\\SSH on target vm after failover. String value of {SrsDataContract.EnableRDPOnTargetOption} enum. |  [optional] |
|**licenseType** | [**LicenseTypeEnum**](#LicenseTypeEnum) | License type. |  [optional] |
|**providerSpecificDetails** | [**UpdateReplicationProtectedItemProviderInput**](UpdateReplicationProtectedItemProviderInput.md) |  |  [optional] |
|**recoveryAvailabilitySetId** | **String** | The target availability set id. |  [optional] |
|**recoveryAzureVMName** | **String** | Target azure VM name given by the user. |  [optional] |
|**recoveryAzureVMSize** | **String** | Target Azure Vm size. |  [optional] |
|**selectedRecoveryAzureNetworkId** | **String** | Target Azure Network Id. |  [optional] |
|**vmNics** | [**List&lt;VMNicInputDetails&gt;**](VMNicInputDetails.md) | The list of vm nic details. |  [optional] |



## Enum: LicenseTypeEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| NO_LICENSE_TYPE | &quot;NoLicenseType&quot; |
| WINDOWS_SERVER | &quot;WindowsServer&quot; |



