

# CreateDataLakeStoreAccountProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultGroup** | **String** | The default owner group for all new folders and files created in the Data Lake Store account. |  [optional] |
|**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  |  [optional] |
|**encryptionState** | [**EncryptionStateEnum**](#EncryptionStateEnum) | The current state of encryption for this Data Lake Store account. |  [optional] |
|**firewallAllowAzureIps** | [**FirewallAllowAzureIpsEnum**](#FirewallAllowAzureIpsEnum) | The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced. |  [optional] |
|**firewallRules** | [**List&lt;CreateFirewallRuleWithAccountParameters&gt;**](CreateFirewallRuleWithAccountParameters.md) | The list of firewall rules associated with this Data Lake Store account. |  [optional] |
|**firewallState** | [**FirewallStateEnum**](#FirewallStateEnum) | The current state of the IP address firewall for this Data Lake Store account. |  [optional] |
|**newTier** | [**NewTierEnum**](#NewTierEnum) | The commitment tier to use for next month. |  [optional] |
|**trustedIdProviderState** | [**TrustedIdProviderStateEnum**](#TrustedIdProviderStateEnum) | The current state of the trusted identity provider feature for this Data Lake Store account. |  [optional] |
|**trustedIdProviders** | [**List&lt;CreateTrustedIdProviderWithAccountParameters&gt;**](CreateTrustedIdProviderWithAccountParameters.md) | The list of trusted identity providers associated with this Data Lake Store account. |  [optional] |
|**virtualNetworkRules** | [**List&lt;CreateVirtualNetworkRuleWithAccountParameters&gt;**](CreateVirtualNetworkRuleWithAccountParameters.md) | The list of virtual network rules associated with this Data Lake Store account. |  [optional] |



## Enum: EncryptionStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



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



