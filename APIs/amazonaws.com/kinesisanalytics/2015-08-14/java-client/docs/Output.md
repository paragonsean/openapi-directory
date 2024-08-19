

# Output

<p> Describes application output configuration in which you identify an in-application stream and a destination where you want the in-application stream data to be written. The destination can be an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream. </p> <p/> <p>For limits on how many destinations an application can write and other limitations, see <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html\">Limits</a>. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  |
|**kinesisStreamsOutput** | [**OutputKinesisStreamsOutput**](OutputKinesisStreamsOutput.md) |  |  [optional] |
|**kinesisFirehoseOutput** | [**OutputKinesisFirehoseOutput**](OutputKinesisFirehoseOutput.md) |  |  [optional] |
|**lambdaOutput** | [**OutputLambdaOutput**](OutputLambdaOutput.md) |  |  [optional] |
|**destinationSchema** | [**OutputDestinationSchema**](OutputDestinationSchema.md) |  |  |



