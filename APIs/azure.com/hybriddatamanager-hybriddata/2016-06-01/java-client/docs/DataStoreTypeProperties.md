

# DataStoreTypeProperties

Data Store Type properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**repositoryType** | **String** | Arm type for the manager resource to which the data source type is associated. This is optional. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the data store type. |  |
|**supportedDataServicesAsSink** | **List&lt;String&gt;** | Supported data services where it can be used as a sink. |  [optional] |
|**supportedDataServicesAsSource** | **List&lt;String&gt;** | Supported data services where it can be used as a source. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |
| SUPPORTED | &quot;Supported&quot; |



