# ThreatJammerComUserApi.PublicAclGroupListOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Number** |  | 
**description** | **String** |  | 
**listType** | **String** |  | 
**name** | **String** |  | 
**origins** | [**AclGroupOriginCollectionOutput**](AclGroupOriginCollectionOutput.md) |  | [optional] 
**resourceType** | **String** |  | 
**self** | **String** |  | 
**status** | **String** |  | [optional] 
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





## Enum: StatusEnum


* `INACTIVE` (value: `"INACTIVE"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `EXPIRED` (value: `"EXPIRED"`)




