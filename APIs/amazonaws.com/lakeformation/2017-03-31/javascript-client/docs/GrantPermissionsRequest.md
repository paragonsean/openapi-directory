# AwsLakeFormation.GrantPermissionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalogId** | **String** | The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.  | [optional] 
**principal** | [**GrantPermissionsRequestPrincipal**](GrantPermissionsRequestPrincipal.md) |  | 
**resource** | [**AddLFTagsToResourceRequestResource**](AddLFTagsToResourceRequestResource.md) |  | 
**permissions** | [**[Permission]**](Permission.md) | The permissions granted to the principal on the resource. Lake Formation defines privileges to grant and revoke access to metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3. Lake Formation requires that each principal be authorized to perform a specific task on Lake Formation resources.  | 
**permissionsWithGrantOption** | [**[Permission]**](Permission.md) | Indicates a list of the granted permissions that the principal may pass to other users. These permissions may only be a subset of the permissions granted in the &lt;code&gt;Privileges&lt;/code&gt;. | [optional] 


