# HetznerCloudApi.CreatePrimaryIPRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigneeId** | **Number** | ID of the resource the Primary IP should be assigned to. Omitted if it should not be assigned. | [optional] 
**assigneeType** | **String** | Resource type the Primary IP can be assigned to | 
**autoDelete** | **Boolean** | Delete the Primary IP when the Server it is assigned to is deleted. If omitted defaults to &#x60;false&#x60;. | [optional] 
**datacenter** | **String** | ID or name of Datacenter the Primary IP will be bound to. Needs to be omitted if &#x60;assignee_id&#x60; is passed. | [optional] 
**labels** | **Object** | User-defined labels (key-value pairs) | [optional] 
**name** | **String** |  | 
**type** | **String** | Primary IP type | 



## Enum: AssigneeTypeEnum


* `server` (value: `"server"`)





## Enum: TypeEnum


* `ipv4` (value: `"ipv4"`)

* `ipv6` (value: `"ipv6"`)




