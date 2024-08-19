

# FileshareParam


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fsIOPS** | **Double** | The number of input/output transactions per second. Available values are 0.25, 2 or 4. |  |
|**fsName** | **String** | The name of the new file share that you want to create. The name can contain uppercase letters, lowercase letters, numbers, underscores (_), and hyphens (-). |  |
|**fsSize** | **Integer** | The size of the file share in gigabyte. Run &#x60;cf ic volume fs-flavor-list&#x60; or call the GET /volumes/fs/flavors/json API endpoint to retrieve a list of available file share sizes.  |  |



