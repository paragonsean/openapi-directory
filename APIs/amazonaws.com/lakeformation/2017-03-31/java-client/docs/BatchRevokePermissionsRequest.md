

# BatchRevokePermissionsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catalogId** | **String** | The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.  |  [optional] |
|**entries** | [**List&lt;BatchPermissionsRequestEntry&gt;**](BatchPermissionsRequestEntry.md) | A list of up to 20 entries for resource permissions to be revoked by batch operation to the principal. |  |



