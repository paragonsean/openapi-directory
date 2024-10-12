

# AutoMLJobChannel

A channel is a named input source that training algorithms can consume. This channel is used for AutoML jobs V2 (jobs created by calling <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html\">CreateAutoMLJobV2</a>).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelType** | [**AutoMLChannelType**](AutoMLChannelType.md) |  |  [optional] |
|**contentType** | [**String**](String.md) |  |  [optional] |
|**compressionType** | [**CompressionType**](CompressionType.md) |  |  [optional] |
|**dataSource** | [**AutoMLJobChannelDataSource**](AutoMLJobChannelDataSource.md) |  |  [optional] |



