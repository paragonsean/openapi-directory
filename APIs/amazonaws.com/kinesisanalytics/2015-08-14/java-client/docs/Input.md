

# Input

When you configure the application input, you specify the streaming source, the in-application stream name that is created, and the mapping between the two. For more information, see <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html\">Configuring Application Input</a>. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**namePrefix** | [**String**](String.md) |  |  |
|**inputProcessingConfiguration** | [**InputInputProcessingConfiguration**](InputInputProcessingConfiguration.md) |  |  [optional] |
|**kinesisStreamsInput** | [**InputKinesisStreamsInput**](InputKinesisStreamsInput.md) |  |  [optional] |
|**kinesisFirehoseInput** | [**InputKinesisFirehoseInput**](InputKinesisFirehoseInput.md) |  |  [optional] |
|**inputParallelism** | [**InputInputParallelism**](InputInputParallelism.md) |  |  [optional] |
|**inputSchema** | [**InputInputSchema**](InputInputSchema.md) |  |  |



