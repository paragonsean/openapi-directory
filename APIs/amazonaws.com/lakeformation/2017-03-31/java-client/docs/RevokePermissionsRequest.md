

# RevokePermissionsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catalogId** | **String** | The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.  |  [optional] |
|**principal** | [**GrantPermissionsRequestPrincipal**](GrantPermissionsRequestPrincipal.md) |  |  |
|**resource** | [**AddLFTagsToResourceRequestResource**](AddLFTagsToResourceRequestResource.md) |  |  |
|**permissions** | **List&lt;Permission&gt;** | The permissions revoked to the principal on the resource. For information about permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html\&quot;&gt;Security and Access Control to Metadata and Data&lt;/a&gt;. |  |
|**permissionsWithGrantOption** | **List&lt;Permission&gt;** | Indicates a list of permissions for which to revoke the grant option allowing the principal to pass permissions to other principals. |  [optional] |



