

# EventLog

Log of user operations via CLI or Web UI.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dagId** | **String** | The DAG ID |  [optional] [readonly] |
|**event** | **String** | A key describing the type of event. |  [optional] [readonly] |
|**eventLogId** | **Integer** | The event log ID |  [optional] [readonly] |
|**executionDate** | **OffsetDateTime** | When the event was dispatched for an object having execution_date, the value of this field.  |  [optional] [readonly] |
|**extra** | **String** | Other information that was not included in the other fields, e.g. the complete CLI command.  |  [optional] [readonly] |
|**owner** | **String** | Name of the user who triggered these events a. |  [optional] [readonly] |
|**taskId** | **String** | The DAG ID |  [optional] [readonly] |
|**when** | **OffsetDateTime** | The time when these events happened. |  [optional] [readonly] |



