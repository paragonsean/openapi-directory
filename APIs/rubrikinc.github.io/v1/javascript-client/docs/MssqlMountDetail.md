# RubrikRestApi.MssqlMountDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationDate** | **Date** | The date this mount was created. | 
**id** | **String** |  | 
**mountedDatabaseId** | **String** | ID for the mounted SQL Server database, once it is available. | [optional] 
**mountedDatabaseName** | **String** | Name for the mounted SQL Server database. | 
**ownerId** | **String** | ID of the user who created this mount. | [optional] 
**ownerName** | **String** | Name of the user who created this mount. | [optional] 
**sourceDatabaseId** | **String** |  | 
**sourceDatabaseName** | **String** |  | 
**sourceRecoveryPoint** | [**MssqlRecoveryPoint**](MssqlRecoveryPoint.md) |  | 
**status** | **String** | The status of this mount. The status is **_Available_** when the database is successfully mounted and ready to use. | 
**targetInstanceId** | **String** |  | 
**targetInstanceName** | **String** |  | 
**targetRootName** | **String** | Name of the top-level object on which the target instance resides. | 
**links** | [**MssqlMountLinks**](MssqlMountLinks.md) |  | 
**mountRequestId** | **String** | ID of the async request object for the mount task. | [optional] 
**unmountRequestId** | **String** | ID of the async request object for the delete task. | [optional] 



## Enum: StatusEnum


* `Available` (value: `"Available"`)

* `Unavailable` (value: `"Unavailable"`)

* `Mounting` (value: `"Mounting"`)

* `Unmounting` (value: `"Unmounting"`)




