

# GooglePrivacyDlpV2LDiversityEquivalenceClass

The set of columns' values that share the same ldiversity value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**equivalenceClassSize** | **String** | Size of the k-anonymity equivalence class. |  [optional] |
|**numDistinctSensitiveValues** | **String** | Number of distinct sensitive values in this equivalence class. |  [optional] |
|**quasiIdsValues** | [**List&lt;GooglePrivacyDlpV2Value&gt;**](GooglePrivacyDlpV2Value.md) | Quasi-identifier values defining the k-anonymity equivalence class. The order is always the same as the original request. |  [optional] |
|**topSensitiveValues** | [**List&lt;GooglePrivacyDlpV2ValueFrequency&gt;**](GooglePrivacyDlpV2ValueFrequency.md) | Estimated frequencies of top sensitive values. |  [optional] |



