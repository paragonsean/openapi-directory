# CosmosDb.ContainerPartitionKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **String** | Indicates the kind of algorithm used for partitioning | [optional] [default to &#39;Hash&#39;]
**paths** | **[String]** | List of paths using which data within the container can be partitioned | [optional] 
**version** | **Number** | Indicates the version of the partition key definition | [optional] 



## Enum: KindEnum


* `Hash` (value: `"Hash"`)

* `Range` (value: `"Range"`)




