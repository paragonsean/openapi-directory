

# DataSource

<p> Represents the output of the <code>GetDataSource</code> operation. </p> <p> The content consists of the detailed metadata and data file information and the current status of the <code>DataSource</code>. </p>

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
|**message** | [**String**](String.md) |  |  [optional] |
|**redshiftMetadata** | [**RedshiftMetadata**](RedshiftMetadata.md) |  |  [optional] |
|**rdSMetadata** | [**RDSMetadata**](RDSMetadata.md) |  |  [optional] |
|**roleARN** | **String** | The Amazon Resource Name (ARN) of an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts\&quot;&gt;AWS IAM Role&lt;/a&gt;, such as the following: arn:aws:iam::account:role/rolename.  |  [optional] |
|**computeStatistics** | [**Boolean**](Boolean.md) |  |  [optional] |
|**computeTime** | **Integer** | Long integer type that is a 64-bit signed number. |  [optional] |
|**finishedAt** | **OffsetDateTime** | A timestamp represented in epoch time. |  [optional] |
|**startedAt** | **OffsetDateTime** | A timestamp represented in epoch time. |  [optional] |



