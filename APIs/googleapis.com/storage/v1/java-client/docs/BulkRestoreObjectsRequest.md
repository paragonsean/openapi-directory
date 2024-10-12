

# BulkRestoreObjectsRequest

A bulk restore objects request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowOverwrite** | **Boolean** | If false (default), the restore will not overwrite live objects with the same name at the destination. This means some deleted objects may be skipped. If true, live objects will be overwritten resulting in a noncurrent object (if versioning is enabled). If versioning is not enabled, overwriting the object will result in a soft-deleted object. In either case, if a noncurrent object already exists with the same name, a live version can be written without issue. |  [optional] |
|**copySourceAcl** | **Boolean** | If true, copies the source object&#39;s ACL; otherwise, uses the bucket&#39;s default object ACL. The default is false. |  [optional] |
|**matchGlobs** | **List&lt;String&gt;** | Restores only the objects matching any of the specified glob(s). If this parameter is not specified, all objects will be restored within the specified time range. |  [optional] |
|**softDeletedAfterTime** | **OffsetDateTime** | Restores only the objects that were soft-deleted after this time. |  [optional] |
|**softDeletedBeforeTime** | **OffsetDateTime** | Restores only the objects that were soft-deleted before this time. |  [optional] |



