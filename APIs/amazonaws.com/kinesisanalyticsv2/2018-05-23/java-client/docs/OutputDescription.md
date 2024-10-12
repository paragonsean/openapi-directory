

# OutputDescription

For a SQL-based Kinesis Data Analytics application, describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**outputId** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**kinesisStreamsOutputDescription** | [**OutputDescriptionKinesisStreamsOutputDescription**](OutputDescriptionKinesisStreamsOutputDescription.md) |  |  [optional] |
|**kinesisFirehoseOutputDescription** | [**OutputDescriptionKinesisFirehoseOutputDescription**](OutputDescriptionKinesisFirehoseOutputDescription.md) |  |  [optional] |
|**lambdaOutputDescription** | [**OutputDescriptionLambdaOutputDescription**](OutputDescriptionLambdaOutputDescription.md) |  |  [optional] |
|**destinationSchema** | [**OutputDescriptionDestinationSchema**](OutputDescriptionDestinationSchema.md) |  |  [optional] |



