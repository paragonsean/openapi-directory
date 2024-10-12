

# InputUpdate

For a SQL-based Kinesis Data Analytics application, describes updates to a specific input configuration (identified by the <code>InputId</code> of an application). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inputId** | [**String**](String.md) |  |  |
|**namePrefixUpdate** | [**String**](String.md) |  |  [optional] |
|**inputProcessingConfigurationUpdate** | [**InputUpdateInputProcessingConfigurationUpdate**](InputUpdateInputProcessingConfigurationUpdate.md) |  |  [optional] |
|**kinesisStreamsInputUpdate** | [**InputUpdateKinesisStreamsInputUpdate**](InputUpdateKinesisStreamsInputUpdate.md) |  |  [optional] |
|**kinesisFirehoseInputUpdate** | [**InputUpdateKinesisFirehoseInputUpdate**](InputUpdateKinesisFirehoseInputUpdate.md) |  |  [optional] |
|**inputSchemaUpdate** | [**InputUpdateInputSchemaUpdate**](InputUpdateInputSchemaUpdate.md) |  |  [optional] |
|**inputParallelismUpdate** | [**InputUpdateInputParallelismUpdate**](InputUpdateInputParallelismUpdate.md) |  |  [optional] |



