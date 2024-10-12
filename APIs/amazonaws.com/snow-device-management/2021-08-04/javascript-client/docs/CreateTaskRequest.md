# AwsSnowDeviceManagement.CreateTaskRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | A token ensuring that the action is called only once with the specified details. | [optional] 
**command** | [**CreateTaskRequestCommand**](CreateTaskRequestCommand.md) |  | 
**description** | **String** | A description of the task and its targets. | [optional] 
**tags** | **{String: String}** | Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.  | [optional] 
**targets** | **[String]** | A list of managed device IDs. | 


