

# ManagementPolicyFilter

Filters limit rule actions to a subset of blobs within the storage account. If multiple filters are defined, a logical AND is performed on all filters. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blobTypes** | **List&lt;String&gt;** | An array of predefined enum values. Only blockBlob is supported. |  |
|**prefixMatch** | **List&lt;String&gt;** | An array of strings for prefixes to be match. |  [optional] |



