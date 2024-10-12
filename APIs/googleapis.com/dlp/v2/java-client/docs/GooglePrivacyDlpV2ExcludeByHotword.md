

# GooglePrivacyDlpV2ExcludeByHotword

The rule to exclude findings based on a hotword. For record inspection of tables, column names are considered hotwords. An example of this is to exclude a finding if it belongs to a BigQuery column that matches a specific pattern.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hotwordRegex** | [**GooglePrivacyDlpV2Regex**](GooglePrivacyDlpV2Regex.md) |  |  [optional] |
|**proximity** | [**GooglePrivacyDlpV2Proximity**](GooglePrivacyDlpV2Proximity.md) |  |  [optional] |



