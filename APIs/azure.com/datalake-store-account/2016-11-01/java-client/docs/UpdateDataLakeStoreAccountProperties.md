

# UpdateDataLakeStoreAccountProperties

Data Lake Store account properties information to be updated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultGroup** | **String** | The default owner group for all new folders and files created in the Data Lake Store account. |  [optional] |
|**encryptionConfig** | [**UpdateEncryptionConfig**](UpdateEncryptionConfig.md) |  |  [optional] |
|**firewallAllowAzureIps** | [**FirewallAllowAzureIpsEnum**](#FirewallAllowAzureIpsEnum) | The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced. |  [optional] |
|**firewallRules** | [**List&lt;UpdateFirewallRuleWithAccountParameters&gt;**](UpdateFirewallRuleWithAccountParameters.md) | The list of firewall rules associated with this Data Lake Store account. |  [optional] |
|**firewallState** | [**FirewallStateEnum**](#FirewallStateEnum) | The current state of the IP address firewall for this Data Lake Store account. Disabling the firewall does not remove existing rules, they will just be ignored until the firewall is re-enabled. |  [optional] |
|**newTier** | [**NewTierEnum**](#NewTierEnum) | The commitment tier to use for next month. |  [optional] |
|**trustedIdProviderState** | [**TrustedIdProviderStateEnum**](#TrustedIdProviderStateEnum) | The current state of the trusted identity provider feature for this Data Lake Store account. Disabling trusted identity provider functionality does not remove the providers, they will just be ignored until this feature is re-enabled. |  [optional] |
|**trustedIdProviders** | [**List&lt;UpdateTrustedIdProviderWithAccountParameters&gt;**](UpdateTrustedIdProviderWithAccountParameters.md) | The list of trusted identity providers associated with this Data Lake Store account. |  [optional] |
|**virtualNetworkRules** | [**List&lt;UpdateVirtualNetworkRuleWithAccountParameters&gt;**](UpdateVirtualNetworkRuleWithAccountParameters.md) | The list of virtual network rules associated with this Data Lake Store account. |  [optional] |



## Enum: FirewallAllowAzureIpsEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: FirewallStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: NewTierEnum

| Name | Value |
|---- | -----|
| CONSUMPTION | &quot;Consumption&quot; |
| COMMITMENT_1_TB | &quot;Commitment_1TB&quot; |
| COMMITMENT_10_TB | &quot;Commitment_10TB&quot; |
| COMMITMENT_100_TB | &quot;Commitment_100TB&quot; |
| COMMITMENT_500_TB | &quot;Commitment_500TB&quot; |
| COMMITMENT_1_PB | &quot;Commitment_1PB&quot; |
| COMMITMENT_5_PB | &quot;Commitment_5PB&quot; |



## Enum: TrustedIdProviderStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



