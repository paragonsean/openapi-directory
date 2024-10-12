

# DataLakeStoreAccountProperties

Data Lake Store account properties information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentTier** | [**CurrentTierEnum**](#CurrentTierEnum) | The commitment tier in use for the current month. |  [optional] [readonly] |
|**defaultGroup** | **String** | The default owner group for all new folders and files created in the Data Lake Store account. |  [optional] [readonly] |
|**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  |  [optional] |
|**encryptionProvisioningState** | [**EncryptionProvisioningStateEnum**](#EncryptionProvisioningStateEnum) | The current state of encryption provisioning for this Data Lake Store account. |  [optional] [readonly] |
|**encryptionState** | [**EncryptionStateEnum**](#EncryptionStateEnum) | The current state of encryption for this Data Lake Store account. |  [optional] [readonly] |
|**firewallAllowAzureIps** | [**FirewallAllowAzureIpsEnum**](#FirewallAllowAzureIpsEnum) | The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced. |  [optional] [readonly] |
|**firewallRules** | [**List&lt;FirewallRule&gt;**](FirewallRule.md) | The list of firewall rules associated with this Data Lake Store account. |  [optional] [readonly] |
|**firewallState** | [**FirewallStateEnum**](#FirewallStateEnum) | The current state of the IP address firewall for this Data Lake Store account. |  [optional] [readonly] |
|**newTier** | [**NewTierEnum**](#NewTierEnum) | The commitment tier to use for next month. |  [optional] [readonly] |
|**trustedIdProviderState** | [**TrustedIdProviderStateEnum**](#TrustedIdProviderStateEnum) | The current state of the trusted identity provider feature for this Data Lake Store account. |  [optional] [readonly] |
|**trustedIdProviders** | [**List&lt;TrustedIdProvider&gt;**](TrustedIdProvider.md) | The list of trusted identity providers associated with this Data Lake Store account. |  [optional] [readonly] |
|**virtualNetworkRules** | [**List&lt;VirtualNetworkRule&gt;**](VirtualNetworkRule.md) | The list of virtual network rules associated with this Data Lake Store account. |  [optional] [readonly] |
|**accountId** | **UUID** | The unique identifier associated with this Data Lake Store account. |  [optional] [readonly] |
|**creationTime** | **OffsetDateTime** | The account creation time. |  [optional] [readonly] |
|**endpoint** | **String** | The full CName endpoint for this account. |  [optional] [readonly] |
|**lastModifiedTime** | **OffsetDateTime** | The account last modified time. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning status of the Data Lake Store account. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The state of the Data Lake Store account. |  [optional] [readonly] |



## Enum: CurrentTierEnum

| Name | Value |
|---- | -----|
| CONSUMPTION | &quot;Consumption&quot; |
| COMMITMENT_1_TB | &quot;Commitment_1TB&quot; |
| COMMITMENT_10_TB | &quot;Commitment_10TB&quot; |
| COMMITMENT_100_TB | &quot;Commitment_100TB&quot; |
| COMMITMENT_500_TB | &quot;Commitment_500TB&quot; |
| COMMITMENT_1_PB | &quot;Commitment_1PB&quot; |
| COMMITMENT_5_PB | &quot;Commitment_5PB&quot; |



## Enum: EncryptionProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |



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



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| FAILED | &quot;Failed&quot; |
| CREATING | &quot;Creating&quot; |
| RUNNING | &quot;Running&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| PATCHING | &quot;Patching&quot; |
| SUSPENDING | &quot;Suspending&quot; |
| RESUMING | &quot;Resuming&quot; |
| DELETING | &quot;Deleting&quot; |
| DELETED | &quot;Deleted&quot; |
| UNDELETING | &quot;Undeleting&quot; |
| CANCELED | &quot;Canceled&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| SUSPENDED | &quot;Suspended&quot; |



