

# GooglePrivacyDlpV2InspectContentRequest

Request to search for potentially sensitive info in a ContentItem.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inspectConfig** | [**GooglePrivacyDlpV2InspectConfig**](GooglePrivacyDlpV2InspectConfig.md) |  |  [optional] |
|**inspectTemplateName** | **String** | Template to use. Any configuration directly specified in inspect_config will override those set in the template. Singular fields that are set in this request will replace their corresponding fields in the template. Repeated fields are appended. Singular sub-messages and groups are recursively merged. |  [optional] |
|**item** | [**GooglePrivacyDlpV2ContentItem**](GooglePrivacyDlpV2ContentItem.md) |  |  [optional] |
|**locationId** | **String** | Deprecated. This field has no effect. |  [optional] |



