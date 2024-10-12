

# GooglePrivacyDlpV2DeltaPresenceEstimationConfig

δ-presence metric, used to estimate how likely it is for an attacker to figure out that one given individual appears in a de-identified dataset. Similarly to the k-map metric, we cannot compute δ-presence exactly without knowing the attack dataset, so we use a statistical model instead.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auxiliaryTables** | [**List&lt;GooglePrivacyDlpV2StatisticalTable&gt;**](GooglePrivacyDlpV2StatisticalTable.md) | Several auxiliary tables can be used in the analysis. Each custom_tag used to tag a quasi-identifiers field must appear in exactly one field of one auxiliary table. |  [optional] |
|**quasiIds** | [**List&lt;GooglePrivacyDlpV2QuasiId&gt;**](GooglePrivacyDlpV2QuasiId.md) | Required. Fields considered to be quasi-identifiers. No two fields can have the same tag. |  [optional] |
|**regionCode** | **String** | ISO 3166-1 alpha-2 region code to use in the statistical modeling. Set if no column is tagged with a region-specific InfoType (like US_ZIP_5) or a region code. |  [optional] |



