

# GooglePrivacyDlpV2QuasiIdentifierField

A quasi-identifier column has a custom_tag, used to know which column in the data corresponds to which column in the statistical model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customTag** | **String** | A column can be tagged with a custom tag. In this case, the user must indicate an auxiliary table that contains statistical information on the possible values of this column (below). |  [optional] |
|**field** | [**GooglePrivacyDlpV2FieldId**](GooglePrivacyDlpV2FieldId.md) |  |  [optional] |



