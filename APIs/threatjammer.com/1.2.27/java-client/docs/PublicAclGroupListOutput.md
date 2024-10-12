

# PublicAclGroupListOutput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **Integer** |  |  |
|**description** | **String** |  |  |
|**listType** | [**ListTypeEnum**](#ListTypeEnum) |  |  |
|**name** | **String** |  |  |
|**origins** | [**AclGroupOriginCollectionOutput**](AclGroupOriginCollectionOutput.md) |  |  [optional] |
|**resourceType** | [**ResourceTypeEnum**](#ResourceTypeEnum) |  |  |
|**self** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  |
|**ttl** | **Integer** |  |  [optional] |
|**updatedAt** | **Integer** |  |  |



## Enum: ListTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| ALLOW | &quot;ALLOW&quot; |
| DENY | &quot;DENY&quot; |



## Enum: ResourceTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| CIDR | &quot;CIDR&quot; |
| COUNTRY | &quot;COUNTRY&quot; |
| CONTINENT | &quot;CONTINENT&quot; |
| AS | &quot;AS&quot; |
| DATACENTER | &quot;DATACENTER&quot; |
| USERAGENT | &quot;USERAGENT&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INACTIVE | &quot;INACTIVE&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| EXPIRED | &quot;EXPIRED&quot; |



