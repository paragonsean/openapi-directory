# AwsLakeFormation.ListPermissionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalogId** | **String** | The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.  | [optional] 
**principal** | [**GrantPermissionsRequestPrincipal**](GrantPermissionsRequestPrincipal.md) |  | [optional] 
**resourceType** | **String** | Specifies a resource type to filter the permissions returned. | [optional] 
**resource** | [**AddLFTagsToResourceRequestResource**](AddLFTagsToResourceRequestResource.md) |  | [optional] 
**nextToken** | **String** | A continuation token, if this is not the first call to retrieve this list. | [optional] 
**maxResults** | **Number** | The maximum number of results to return. | [optional] 
**includeRelated** | **String** | Indicates that related permissions should be included in the results. | [optional] 



## Enum: ResourceTypeEnum


* `CATALOG` (value: `"CATALOG"`)

* `DATABASE` (value: `"DATABASE"`)

* `TABLE` (value: `"TABLE"`)

* `DATA_LOCATION` (value: `"DATA_LOCATION"`)

* `LF_TAG` (value: `"LF_TAG"`)

* `LF_TAG_POLICY` (value: `"LF_TAG_POLICY"`)

* `LF_TAG_POLICY_DATABASE` (value: `"LF_TAG_POLICY_DATABASE"`)

* `LF_TAG_POLICY_TABLE` (value: `"LF_TAG_POLICY_TABLE"`)




