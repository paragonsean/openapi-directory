

# OpenXJsonSerDe

The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**convertDotsInJsonKeysToUnderscores** | [**Boolean**](Boolean.md) |  |  [optional] |
|**caseInsensitive** | [**Boolean**](Boolean.md) |  |  [optional] |
|**columnToJsonKeyMappings** | [**Map**](Map.md) |  |  [optional] |



