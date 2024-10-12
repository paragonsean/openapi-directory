

# ListPermissionsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catalogId** | **String** | The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.  |  [optional] |
|**principal** | [**GrantPermissionsRequestPrincipal**](GrantPermissionsRequestPrincipal.md) |  |  [optional] |
|**resourceType** | [**ResourceTypeEnum**](#ResourceTypeEnum) | Specifies a resource type to filter the permissions returned. |  [optional] |
|**resource** | [**AddLFTagsToResourceRequestResource**](AddLFTagsToResourceRequestResource.md) |  |  [optional] |
|**nextToken** | **String** | A continuation token, if this is not the first call to retrieve this list. |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to return. |  [optional] |
|**includeRelated** | **String** | Indicates that related permissions should be included in the results. |  [optional] |



## Enum: ResourceTypeEnum

| Name | Value |
|---- | -----|
| CATALOG | &quot;CATALOG&quot; |
| DATABASE | &quot;DATABASE&quot; |
| TABLE | &quot;TABLE&quot; |
| DATA_LOCATION | &quot;DATA_LOCATION&quot; |
| LF_TAG | &quot;LF_TAG&quot; |
| LF_TAG_POLICY | &quot;LF_TAG_POLICY&quot; |
| LF_TAG_POLICY_DATABASE | &quot;LF_TAG_POLICY_DATABASE&quot; |
| LF_TAG_POLICY_TABLE | &quot;LF_TAG_POLICY_TABLE&quot; |



