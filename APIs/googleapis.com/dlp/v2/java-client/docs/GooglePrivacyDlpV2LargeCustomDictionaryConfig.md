

# GooglePrivacyDlpV2LargeCustomDictionaryConfig

Configuration for a custom dictionary created from a data source of any size up to the maximum size defined in the [limits](https://cloud.google.com/sensitive-data-protection/limits) page. The artifacts of dictionary creation are stored in the specified Cloud Storage location. Consider using `CustomInfoType.Dictionary` for smaller dictionaries that satisfy the size requirements.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigQueryField** | [**GooglePrivacyDlpV2BigQueryField**](GooglePrivacyDlpV2BigQueryField.md) |  |  [optional] |
|**cloudStorageFileSet** | [**GooglePrivacyDlpV2CloudStorageFileSet**](GooglePrivacyDlpV2CloudStorageFileSet.md) |  |  [optional] |
|**outputPath** | [**GooglePrivacyDlpV2CloudStoragePath**](GooglePrivacyDlpV2CloudStoragePath.md) |  |  [optional] |



