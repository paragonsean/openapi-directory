

# GetDataSourceOutput

Represents the output of a <code>GetDataSource</code> operation and describes a <code>DataSource</code>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceId** | [**String**](String.md) |  |  [optional] |
|**dataLocationS3** | [**String**](String.md) |  |  [optional] |
|**dataRearrangement** | [**String**](String.md) |  |  [optional] |
|**createdByIamUser** | [**String**](String.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastUpdatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**dataSizeInBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**numberOfFiles** | [**Integer**](Integer.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**status** | [**EntityStatus**](EntityStatus.md) |  |  [optional] |
|**logUri** | [**String**](String.md) |  |  [optional] |
|**message** | [**String**](String.md) |  |  [optional] |
|**redshiftMetadata** | [**RedshiftMetadata**](RedshiftMetadata.md) |  |  [optional] |
|**rdSMetadata** | [**RDSMetadata**](RDSMetadata.md) |  |  [optional] |
|**roleARN** | **String** | The Amazon Resource Name (ARN) of an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts\&quot;&gt;AWS IAM Role&lt;/a&gt;, such as the following: arn:aws:iam::account:role/rolename.  |  [optional] |
|**computeStatistics** | [**Boolean**](Boolean.md) |  |  [optional] |
|**computeTime** | [**Integer**](Integer.md) |  |  [optional] |
|**finishedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**startedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**dataSourceSchema** | [**String**](String.md) |  |  [optional] |



