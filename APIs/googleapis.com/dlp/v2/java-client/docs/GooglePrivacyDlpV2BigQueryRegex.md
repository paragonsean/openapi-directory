

# GooglePrivacyDlpV2BigQueryRegex

A pattern to match against one or more tables, datasets, or projects that contain BigQuery tables. At least one pattern must be specified. Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datasetIdRegex** | **String** | If unset, this property matches all datasets. |  [optional] |
|**projectIdRegex** | **String** | For organizations, if unset, will match all projects. Has no effect for data profile configurations created within a project. |  [optional] |
|**tableIdRegex** | **String** | If unset, this property matches all tables. |  [optional] |



