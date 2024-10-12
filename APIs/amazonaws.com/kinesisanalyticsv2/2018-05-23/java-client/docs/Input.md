

# Input

When you configure the application input for a SQL-based Kinesis Data Analytics application, you specify the streaming source, the in-application stream name that is created, and the mapping between the two. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**namePrefix** | [**String**](String.md) |  |  |
|**inputProcessingConfiguration** | [**InputInputProcessingConfiguration**](InputInputProcessingConfiguration.md) |  |  [optional] |
|**kinesisStreamsInput** | [**InputKinesisStreamsInput**](InputKinesisStreamsInput.md) |  |  [optional] |
|**kinesisFirehoseInput** | [**InputKinesisFirehoseInput**](InputKinesisFirehoseInput.md) |  |  [optional] |
|**inputParallelism** | [**InputInputParallelism**](InputInputParallelism.md) |  |  [optional] |
|**inputSchema** | [**InputInputSchema**](InputInputSchema.md) |  |  |



