

# FirewallDevices

Associates a Firewall with a Linode service. A Firewall can be assigned to a single Linode service at a time. Additional disabled Firewalls can be assigned to a service, but they cannot be enabled if another active Firewall is already assigned to the same service. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | When this Device was created.  |  [optional] [readonly] |
|**entity** | [**FirewallDevicesEntity**](FirewallDevicesEntity.md) |  |  [optional] |
|**id** | **Integer** | The Device&#39;s unique ID  |  [optional] |
|**updated** | **OffsetDateTime** | When this Device was last updated.  |  [optional] [readonly] |



