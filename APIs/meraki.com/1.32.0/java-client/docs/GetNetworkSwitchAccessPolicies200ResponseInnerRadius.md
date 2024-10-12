

# GetNetworkSwitchAccessPolicies200ResponseInnerRadius

Object for RADIUS Settings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**criticalAuth** | [**GetNetworkSwitchAccessPolicies200ResponseInnerRadiusCriticalAuth**](GetNetworkSwitchAccessPolicies200ResponseInnerRadiusCriticalAuth.md) |  |  [optional] |
|**failedAuthVlanId** | **Integer** | VLAN that clients will be placed on when RADIUS authentication fails. Will be null if hostMode is Multi-Auth |  [optional] |
|**reAuthenticationInterval** | **Integer** | Re-authentication period in seconds. Will be null if hostMode is Multi-Auth |  [optional] |



