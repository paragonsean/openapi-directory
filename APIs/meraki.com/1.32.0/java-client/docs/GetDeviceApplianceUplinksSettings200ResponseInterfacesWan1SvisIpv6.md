

# GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1SvisIpv6

IPv6 settings for static/dynamic mode.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Static address that will override the one(s) received by SLAAC. |  [optional] |
|**assignmentMode** | [**AssignmentModeEnum**](#AssignmentModeEnum) | The assignment mode for this SVI. Applies only when PPPoE is disabled. |  [optional] |
|**gateway** | **String** | Static gateway that will override the one received by autoconf. |  [optional] |
|**nameservers** | [**GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1SvisIpv4Nameservers**](GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1SvisIpv4Nameservers.md) |  |  [optional] |



## Enum: AssignmentModeEnum

| Name | Value |
|---- | -----|
| DYNAMIC | &quot;dynamic&quot; |
| STATIC | &quot;static&quot; |



