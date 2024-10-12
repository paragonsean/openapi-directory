# DataLakeStoreAccountManagementClient.UpdateDataLakeStoreAccountProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultGroup** | **String** | The default owner group for all new folders and files created in the Data Lake Store account. | [optional] 
**encryptionConfig** | [**UpdateEncryptionConfig**](UpdateEncryptionConfig.md) |  | [optional] 
**firewallAllowAzureIps** | **String** | The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced. | [optional] 
**firewallRules** | [**[UpdateFirewallRuleWithAccountParameters]**](UpdateFirewallRuleWithAccountParameters.md) | The list of firewall rules associated with this Data Lake Store account. | [optional] 
**firewallState** | **String** | The current state of the IP address firewall for this Data Lake Store account. Disabling the firewall does not remove existing rules, they will just be ignored until the firewall is re-enabled. | [optional] 
**newTier** | **String** | The commitment tier to use for next month. | [optional] 
**trustedIdProviderState** | **String** | The current state of the trusted identity provider feature for this Data Lake Store account. Disabling trusted identity provider functionality does not remove the providers, they will just be ignored until this feature is re-enabled. | [optional] 
**trustedIdProviders** | [**[UpdateTrustedIdProviderWithAccountParameters]**](UpdateTrustedIdProviderWithAccountParameters.md) | The list of trusted identity providers associated with this Data Lake Store account. | [optional] 
**virtualNetworkRules** | [**[UpdateVirtualNetworkRuleWithAccountParameters]**](UpdateVirtualNetworkRuleWithAccountParameters.md) | The list of virtual network rules associated with this Data Lake Store account. | [optional] 



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




