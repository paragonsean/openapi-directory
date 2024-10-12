# LinodeApi.DatabaseType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_class** | **String** | The compute class category. | [optional] 
**deprecated** | **Boolean** | Whether this Database plan type has been deprecated and is no longer available. | [optional] 
**disk** | **Number** | The amount of disk space set aside for Databases of this plan type. The value is represented in megabytes. | [optional] 
**engines** | [**DatabaseTypeEngines**](DatabaseTypeEngines.md) |  | [optional] 
**id** | **String** | The ID representing the Managed Database node plan type. | [optional] [readonly] 
**label** | **String** | A human-readable string that describes each plan type. For display purposes only. | [optional] [readonly] 
**memory** | **Number** | The amount of RAM allocated to Database created of this plan type. The value is represented in megabytes. | [optional] 
**vcpus** | **Number** | The integer of number CPUs allocated to databases of this plan type. | [optional] 


