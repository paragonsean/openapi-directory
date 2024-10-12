

# GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1SvisIpv4

IPv4 settings for static/dynamic mode.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | IP address and subnet mask when in static mode. |  [optional] |
|**assignmentMode** | [**AssignmentModeEnum**](#AssignmentModeEnum) | The assignment mode for this SVI. Applies only when PPPoE is disabled. |  [optional] |
|**gateway** | **String** | Gateway IP address when in static mode. |  [optional] |
|**nameservers** | [**GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1SvisIpv4Nameservers**](GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1SvisIpv4Nameservers.md) |  |  [optional] |



## Enum: AssignmentModeEnum

| Name | Value |
|---- | -----|
| DYNAMIC | &quot;dynamic&quot; |
| STATIC | &quot;static&quot; |



