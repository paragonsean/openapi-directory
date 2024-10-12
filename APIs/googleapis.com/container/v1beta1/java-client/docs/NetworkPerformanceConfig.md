

# NetworkPerformanceConfig

Configuration of all network bandwidth tiers

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**externalIpEgressBandwidthTier** | [**ExternalIpEgressBandwidthTierEnum**](#ExternalIpEgressBandwidthTierEnum) | Specifies the network bandwidth tier for the NodePool for traffic to external/public IP addresses. |  [optional] |
|**totalEgressBandwidthTier** | [**TotalEgressBandwidthTierEnum**](#TotalEgressBandwidthTierEnum) | Specifies the total network bandwidth tier for the NodePool. |  [optional] |



## Enum: ExternalIpEgressBandwidthTierEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TIER_UNSPECIFIED&quot; |
| _1 | &quot;TIER_1&quot; |



## Enum: TotalEgressBandwidthTierEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TIER_UNSPECIFIED&quot; |
| _1 | &quot;TIER_1&quot; |



