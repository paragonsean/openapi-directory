# MerakiDashboardApi.GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1SvisIpv6

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | Static address that will override the one(s) received by SLAAC. | [optional] 
**assignmentMode** | **String** | The assignment mode for this SVI. Applies only when PPPoE is disabled. | [optional] 
**gateway** | **String** | Static gateway that will override the one received by autoconf. | [optional] 
**nameservers** | [**GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1SvisIpv4Nameservers**](GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1SvisIpv4Nameservers.md) |  | [optional] 



## Enum: AssignmentModeEnum


* `dynamic` (value: `"dynamic"`)

* `static` (value: `"static"`)




