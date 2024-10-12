

# ConnectorMappingErrorManagement

The error management.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorLimit** | **Integer** | The error limit allowed while importing data. |  [optional] |
|**errorManagementType** | [**ErrorManagementTypeEnum**](#ErrorManagementTypeEnum) | The type of error management to use for the mapping. |  |



## Enum: ErrorManagementTypeEnum

| Name | Value |
|---- | -----|
| REJECT_AND_CONTINUE | &quot;RejectAndContinue&quot; |
| STOP_IMPORT | &quot;StopImport&quot; |
| REJECT_UNTIL_LIMIT | &quot;RejectUntilLimit&quot; |



