

# TapeArchive

Represents a virtual tape that is archived in the virtual tape shelf (VTS).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tapeARN** | [**String**](String.md) |  |  [optional] |
|**tapeBarcode** | [**String**](String.md) |  |  [optional] |
|**tapeCreatedDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**tapeSizeInBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**completionTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**retrievedTo** | [**String**](String.md) |  |  [optional] |
|**tapeStatus** | [**String**](String.md) |  |  [optional] |
|**tapeUsedInBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**kmSKey** | **String** | The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value can only be set when &lt;code&gt;KMSEncrypted&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. Optional. |  [optional] |
|**poolId** | [**String**](String.md) |  |  [optional] |
|**worm** | [**Boolean**](Boolean.md) |  |  [optional] |
|**retentionStartDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**poolEntryDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



