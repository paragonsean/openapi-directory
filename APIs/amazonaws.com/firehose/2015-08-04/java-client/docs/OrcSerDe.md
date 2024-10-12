

# OrcSerDe

A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see <a href=\"https://orc.apache.org/docs/\">Apache ORC</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stripeSizeBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**blockSizeBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**rowIndexStride** | [**Integer**](Integer.md) |  |  [optional] |
|**enablePadding** | [**Boolean**](Boolean.md) |  |  [optional] |
|**paddingTolerance** | [**Double**](Double.md) |  |  [optional] |
|**compression** | [**OrcCompression**](OrcCompression.md) |  |  [optional] |
|**bloomFilterColumns** | [**List**](List.md) |  |  [optional] |
|**bloomFilterFalsePositiveProbability** | [**Double**](Double.md) |  |  [optional] |
|**dictionaryKeyThreshold** | [**Double**](Double.md) |  |  [optional] |
|**formatVersion** | [**OrcFormatVersion**](OrcFormatVersion.md) |  |  [optional] |



