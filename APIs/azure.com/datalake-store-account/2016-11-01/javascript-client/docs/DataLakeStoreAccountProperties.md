# DataLakeStoreAccountManagementClient.DataLakeStoreAccountProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentTier** | **String** | The commitment tier in use for the current month. | [optional] [readonly] 
**defaultGroup** | **String** | The default owner group for all new folders and files created in the Data Lake Store account. | [optional] [readonly] 
**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  | [optional] 
**encryptionProvisioningState** | **String** | The current state of encryption provisioning for this Data Lake Store account. | [optional] [readonly] 
**encryptionState** | **String** | The current state of encryption for this Data Lake Store account. | [optional] [readonly] 
**firewallAllowAzureIps** | **String** | The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced. | [optional] [readonly] 
**firewallRules** | [**[FirewallRule]**](FirewallRule.md) | The list of firewall rules associated with this Data Lake Store account. | [optional] [readonly] 
**firewallState** | **String** | The current state of the IP address firewall for this Data Lake Store account. | [optional] [readonly] 
**newTier** | **String** | The commitment tier to use for next month. | [optional] [readonly] 
**trustedIdProviderState** | **String** | The current state of the trusted identity provider feature for this Data Lake Store account. | [optional] [readonly] 
**trustedIdProviders** | [**[TrustedIdProvider]**](TrustedIdProvider.md) | The list of trusted identity providers associated with this Data Lake Store account. | [optional] [readonly] 
**virtualNetworkRules** | [**[VirtualNetworkRule]**](VirtualNetworkRule.md) | The list of virtual network rules associated with this Data Lake Store account. | [optional] [readonly] 
**accountId** | **String** | The unique identifier associated with this Data Lake Store account. | [optional] [readonly] 
**creationTime** | **Date** | The account creation time. | [optional] [readonly] 
**endpoint** | **String** | The full CName endpoint for this account. | [optional] [readonly] 
**lastModifiedTime** | **Date** | The account last modified time. | [optional] [readonly] 
**provisioningState** | **String** | The provisioning status of the Data Lake Store account. | [optional] [readonly] 
**state** | **String** | The state of the Data Lake Store account. | [optional] [readonly] 



## Enum: CurrentTierEnum


* `Consumption` (value: `"Consumption"`)

* `Commitment_1TB` (value: `"Commitment_1TB"`)

* `Commitment_10TB` (value: `"Commitment_10TB"`)

* `Commitment_100TB` (value: `"Commitment_100TB"`)

* `Commitment_500TB` (value: `"Commitment_500TB"`)

* `Commitment_1PB` (value: `"Commitment_1PB"`)

* `Commitment_5PB` (value: `"Commitment_5PB"`)





## Enum: EncryptionProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Succeeded` (value: `"Succeeded"`)





## Enum: EncryptionStateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: FirewallAllowAzureIpsEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: FirewallStateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: NewTierEnum


* `Consumption` (value: `"Consumption"`)

* `Commitment_1TB` (value: `"Commitment_1TB"`)

* `Commitment_10TB` (value: `"Commitment_10TB"`)

* `Commitment_100TB` (value: `"Commitment_100TB"`)

* `Commitment_500TB` (value: `"Commitment_500TB"`)

* `Commitment_1PB` (value: `"Commitment_1PB"`)

* `Commitment_5PB` (value: `"Commitment_5PB"`)





## Enum: TrustedIdProviderStateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: ProvisioningStateEnum


* `Failed` (value: `"Failed"`)

* `Creating` (value: `"Creating"`)

* `Running` (value: `"Running"`)

* `Succeeded` (value: `"Succeeded"`)

* `Patching` (value: `"Patching"`)

* `Suspending` (value: `"Suspending"`)

* `Resuming` (value: `"Resuming"`)

* `Deleting` (value: `"Deleting"`)

* `Deleted` (value: `"Deleted"`)

* `Undeleting` (value: `"Undeleting"`)

* `Canceled` (value: `"Canceled"`)





## Enum: StateEnum


* `Active` (value: `"Active"`)

* `Suspended` (value: `"Suspended"`)




