

# GetNetworkSwitchAccessPolicies200ResponseInnerRadiusCriticalAuth

Critical auth settings for when authentication is rejected by the RADIUS server

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataVlanId** | **Integer** | VLAN that clients who use data will be placed on when RADIUS authentication fails. Will be null if hostMode is Multi-Auth |  [optional] |
|**suspendPortBounce** | **Boolean** | Enable to suspend port bounce when RADIUS servers are unreachable |  [optional] |
|**voiceVlanId** | **Integer** | VLAN that clients who use voice will be placed on when RADIUS authentication fails. Will be null if hostMode is Multi-Auth |  [optional] |



