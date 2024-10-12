# RedisManagementClient.RedisRebootParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rebootType** | **String** | Which Redis node(s) to reboot. Depending on this value data loss is possible. | 
**shardId** | **Number** | If clustering is enabled, the ID of the shared be rebooted. | [optional] 



## Enum: RebootTypeEnum


* `PrimaryNode` (value: `"PrimaryNode"`)

* `SecondaryNode` (value: `"SecondaryNode"`)

* `AllNodes` (value: `"AllNodes"`)




