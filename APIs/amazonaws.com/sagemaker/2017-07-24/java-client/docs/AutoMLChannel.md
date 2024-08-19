

# AutoMLChannel

<p>A channel is a named input source that training algorithms can consume. The validation dataset size is limited to less than 2 GB. The training dataset size must be less than 100 GB. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html\"> Channel</a>.</p> <note> <p>A validation dataset must contain the same headers as the training dataset.</p> </note> <p/>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSource** | [**AutoMLChannelDataSource**](AutoMLChannelDataSource.md) |  |  |
|**compressionType** | [**CompressionType**](CompressionType.md) |  |  [optional] |
|**targetAttributeName** | [**String**](String.md) |  |  |
|**contentType** | [**String**](String.md) |  |  [optional] |
|**channelType** | [**AutoMLChannelType**](AutoMLChannelType.md) |  |  [optional] |
|**sampleWeightAttributeName** | [**String**](String.md) |  |  [optional] |



