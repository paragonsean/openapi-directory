

# PermissionList

A list of permissions associated with a file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | The ETag of the list. |  [optional] |
|**items** | [**List&lt;Permission&gt;**](Permission.md) | The list of permissions. |  [optional] |
|**kind** | **String** | This is always &#x60;drive#permissionList&#x60;. |  [optional] |
|**nextPageToken** | **String** | The page token for the next page of permissions. This field will be absent if the end of the permissions list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. |  [optional] |
|**selfLink** | **String** | A link back to this list. |  [optional] |



