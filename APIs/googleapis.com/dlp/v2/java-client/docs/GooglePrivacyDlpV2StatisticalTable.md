

# GooglePrivacyDlpV2StatisticalTable

An auxiliary table containing statistical information on the relative frequency of different quasi-identifiers values. It has one or several quasi-identifiers columns, and one column that indicates the relative frequency of each quasi-identifier tuple. If a tuple is present in the data but not in the auxiliary table, the corresponding relative frequency is assumed to be zero (and thus, the tuple is highly reidentifiable).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**quasiIds** | [**List&lt;GooglePrivacyDlpV2QuasiIdentifierField&gt;**](GooglePrivacyDlpV2QuasiIdentifierField.md) | Required. Quasi-identifier columns. |  [optional] |
|**relativeFrequency** | [**GooglePrivacyDlpV2FieldId**](GooglePrivacyDlpV2FieldId.md) |  |  [optional] |
|**table** | [**GooglePrivacyDlpV2BigQueryTable**](GooglePrivacyDlpV2BigQueryTable.md) |  |  [optional] |



