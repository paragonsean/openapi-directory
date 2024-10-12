

# NewDisk

A Persistent Disk resource that will be created and attached to each Replica in the Pool. Each Replica will have a unique persistent disk that is created and attached to that Replica in READ_WRITE mode.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachment** | [**DiskAttachment**](DiskAttachment.md) |  |  [optional] |
|**autoDelete** | **Boolean** | If true, then this disk will be deleted when the instance is deleted. The default value is true. |  [optional] |
|**boot** | **Boolean** | If true, indicates that this is the root persistent disk. |  [optional] |
|**initializeParams** | [**NewDiskInitializeParams**](NewDiskInitializeParams.md) |  |  [optional] |



