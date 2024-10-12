

# HdfsData

An HdfsData resource specifies a path within an HDFS entity (e.g. a cluster). All cluster-specific settings, such as namenodes and ports, are configured on the transfer agents servicing requests, so HdfsData only contains the root path to the data in our transfer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**path** | **String** | Root path to transfer files. |  [optional] |



