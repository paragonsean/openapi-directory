

# DatabaseType

Managed Database plan type object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**propertyClass** | **String** | The compute class category. |  [optional] |
|**deprecated** | **Boolean** | Whether this Database plan type has been deprecated and is no longer available. |  [optional] |
|**disk** | **Integer** | The amount of disk space set aside for Databases of this plan type. The value is represented in megabytes. |  [optional] |
|**engines** | [**DatabaseTypeEngines**](DatabaseTypeEngines.md) |  |  [optional] |
|**id** | **String** | The ID representing the Managed Database node plan type. |  [optional] [readonly] |
|**label** | **String** | A human-readable string that describes each plan type. For display purposes only. |  [optional] [readonly] |
|**memory** | **Integer** | The amount of RAM allocated to Database created of this plan type. The value is represented in megabytes. |  [optional] |
|**vcpus** | **Integer** | The integer of number CPUs allocated to databases of this plan type. |  [optional] |



