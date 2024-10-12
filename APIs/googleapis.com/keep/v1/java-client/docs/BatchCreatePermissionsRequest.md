

# BatchCreatePermissionsRequest

The request to add one or more permissions on the note. Currently, only the `WRITER` role may be specified. If adding a permission fails, then the entire request fails and no changes are made.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requests** | [**List&lt;CreatePermissionRequest&gt;**](CreatePermissionRequest.md) | The request message specifying the resources to create. |  [optional] |



