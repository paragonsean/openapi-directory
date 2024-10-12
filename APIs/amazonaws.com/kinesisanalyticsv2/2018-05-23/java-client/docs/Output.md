

# Output

<p> Describes a SQL-based Kinesis Data Analytics application's output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream. </p> <p/>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  |
|**kinesisStreamsOutput** | [**OutputKinesisStreamsOutput**](OutputKinesisStreamsOutput.md) |  |  [optional] |
|**kinesisFirehoseOutput** | [**OutputKinesisFirehoseOutput**](OutputKinesisFirehoseOutput.md) |  |  [optional] |
|**lambdaOutput** | [**OutputLambdaOutput**](OutputLambdaOutput.md) |  |  [optional] |
|**destinationSchema** | [**OutputDestinationSchema**](OutputDestinationSchema.md) |  |  |



