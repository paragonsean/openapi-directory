

# DatabaseBackup

A database backup object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **String** | A time value given in a combined date and time format that represents when the database backup was created. |  [optional] |
|**id** | **Integer** | The ID of the database backup object. |  [optional] |
|**label** | **String** | The database backup&#39;s label, for display purposes only.  Must include only ASCII letters or numbers.  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of database backup, determined by how the backup was created. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SNAPSHOT | &quot;snapshot&quot; |
| AUTO | &quot;auto&quot; |



