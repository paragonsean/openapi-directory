

# FirewallStatus

Detailed information about the current status of a <a>Firewall</a>. You can retrieve this for a firewall by calling <a>DescribeFirewall</a> and providing the firewall name and ARN.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**FirewallStatusValue**](FirewallStatusValue.md) |  |  |
|**configurationSyncStateSummary** | [**ConfigurationSyncState**](ConfigurationSyncState.md) |  |  |
|**syncStates** | [**Map**](Map.md) |  |  [optional] |
|**capacityUsageSummary** | [**FirewallStatusCapacityUsageSummary**](FirewallStatusCapacityUsageSummary.md) |  |  [optional] |



