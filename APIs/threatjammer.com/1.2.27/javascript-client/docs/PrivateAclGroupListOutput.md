# ThreatJammerComUserApi.PrivateAclGroupListOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **String** |  | 
**createdAt** | **Number** |  | 
**description** | **String** |  | 
**listType** | **String** |  | 
**name** | **String** |  | 
**origins** | [**AclGroupOriginCollectionOutput**](AclGroupOriginCollectionOutput.md) |  | [optional] 
**resourceType** | **String** |  | 
**self** | **String** |  | 
**tags** | **[String]** |  | 
**ttl** | **Number** |  | [optional] 
**updatedAt** | **Number** |  | 



## Enum: ListTypeEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `ALLOW` (value: `"ALLOW"`)

* `DENY` (value: `"DENY"`)





## Enum: ResourceTypeEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `CIDR` (value: `"CIDR"`)

* `COUNTRY` (value: `"COUNTRY"`)

* `CONTINENT` (value: `"CONTINENT"`)

* `AS` (value: `"AS"`)

* `DATACENTER` (value: `"DATACENTER"`)

* `USERAGENT` (value: `"USERAGENT"`)




