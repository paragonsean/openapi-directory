# MonitorManagementClient.AutoscaleProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | [**ScaleCapacity**](ScaleCapacity.md) |  | 
**fixedDate** | [**TimeWindow**](TimeWindow.md) |  | [optional] 
**name** | **String** | the name of the profile. | 
**recurrence** | [**Recurrence**](Recurrence.md) |  | [optional] 
**rules** | [**[ScaleRule]**](ScaleRule.md) | the collection of rules that provide the triggers and parameters for the scaling action. A maximum of 10 rules can be specified. | 


