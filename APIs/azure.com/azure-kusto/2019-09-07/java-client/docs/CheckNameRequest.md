

# CheckNameRequest

The result returned from a database check name availability request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Resource name. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of resource, for instance Microsoft.Kusto/clusters/databases. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DATABASES | &quot;Microsoft.Kusto/clusters/databases&quot; |
| ATTACHED_DATABASE_CONFIGURATIONS | &quot;Microsoft.Kusto/clusters/attachedDatabaseConfigurations&quot; |



