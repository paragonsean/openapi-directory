

# FirewallRuleConfigAddresses

Allowed IPv4 or IPv6 addresses. A Rule can have up to 255 addresses or networks listed across its IPv4 and IPv6 arrays. A network and a single IP are treated as equivalent when accounting for this limit. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipv4** | **List&lt;String&gt;** | A list of IPv4 addresses or networks. Must be in IP/mask format. |  [optional] |
|**ipv6** | **List&lt;String&gt;** | A list of IPv6 addresses or networks. Must be in IP/mask format. |  [optional] |



