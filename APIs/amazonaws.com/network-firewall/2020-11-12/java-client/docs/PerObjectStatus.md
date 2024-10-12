

# PerObjectStatus

Provides configuration status for a single policy or rule group that is used for a firewall endpoint. Network Firewall provides each endpoint with the rules that are configured in the firewall policy. Each time you add a subnet or modify the associated firewall policy, Network Firewall synchronizes the rules in the endpoint, so it can properly filter network traffic. This is part of a <a>SyncState</a> for a firewall.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**syncStatus** | [**PerObjectSyncStatus**](PerObjectSyncStatus.md) |  |  [optional] |
|**updateToken** | [**String**](String.md) |  |  [optional] |



