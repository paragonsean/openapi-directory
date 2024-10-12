

# CreateObjectStorageObjectURLRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentType** | **String** | The expected &#x60;Content-type&#x60; header of the request this signed URL will be valid for.  If provided, the &#x60;Content-type&#x60; header _must_ be sent with the request when this URL is used, and _must_ be the same as it was when the signed URL was created. Required for all methods *except* \&quot;GET\&quot; or \&quot;DELETE\&quot;.  |  [optional] |
|**expiresIn** | **Integer** | How long this signed URL will be valid for, in seconds.  If omitted, the URL will be valid for 3600 seconds (1 hour).  |  [optional] |
|**method** | **String** | The HTTP method allowed to be used with the pre-signed URL. |  |
|**name** | **String** | The name of the object that will be accessed with the pre-signed URL. This object need not exist, and no error will be returned if it doesn&#39;t. This behavior is useful for generating pre-signed URLs to upload new objects to by setting the &#x60;method&#x60; to \&quot;PUT\&quot;.  |  |



