# AppServiceEnvironmentsApiClient.AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Allow or Deny access for this IP range. | [optional] 
**description** | **String** | IP restriction rule description. | [optional] 
**ipAddress** | **String** | IP address the security restriction is valid for. It can be in form of pure ipv4 address (required SubnetMask property) or CIDR notation such as ipv4/mask (leading bit match). For CIDR, SubnetMask property must not be specified. | [optional] 
**name** | **String** | IP restriction rule name. | [optional] 
**priority** | **Number** | Priority of IP restriction rule. | [optional] 
**subnetMask** | **String** | Subnet mask for the range of IP addresses the restriction is valid for. | [optional] 
**subnetTrafficTag** | **Number** | (internal) Subnet traffic tag | [optional] 
**tag** | **String** | Defines what this IP filter will be used for. This is to support IP filtering on proxies. | [optional] 
**vnetSubnetResourceId** | **String** | Virtual network resource id | [optional] 
**vnetTrafficTag** | **Number** | (internal) Vnet traffic tag | [optional] 



## Enum: TagEnum


* `Default` (value: `"Default"`)

* `XffProxy` (value: `"XffProxy"`)




