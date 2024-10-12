

# GooglePrivacyDlpV2InspectTemplate

The inspectTemplate contains a configuration (set of types of sensitive data to be detected) to be used anywhere you otherwise would normally specify InspectConfig. See https://cloud.google.com/sensitive-data-protection/docs/concepts-templates to learn more.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The creation timestamp of an inspectTemplate. |  [optional] [readonly] |
|**description** | **String** | Short description (max 256 chars). |  [optional] |
|**displayName** | **String** | Display name (max 256 chars). |  [optional] |
|**inspectConfig** | [**GooglePrivacyDlpV2InspectConfig**](GooglePrivacyDlpV2InspectConfig.md) |  |  [optional] |
|**name** | **String** | Output only. The template name. The template will have one of the following formats: &#x60;projects/PROJECT_ID/inspectTemplates/TEMPLATE_ID&#x60; OR &#x60;organizations/ORGANIZATION_ID/inspectTemplates/TEMPLATE_ID&#x60;; |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The last update timestamp of an inspectTemplate. |  [optional] [readonly] |



