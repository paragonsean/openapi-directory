

# AdvancedSecurityOptionsInput

Options for enabling and configuring fine-grained access control. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html\">Fine-grained access control in Amazon OpenSearch Service</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**internalUserDatabaseEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**masterUserOptions** | [**CreateDomainRequestAdvancedSecurityOptionsMasterUserOptions**](CreateDomainRequestAdvancedSecurityOptionsMasterUserOptions.md) |  |  [optional] |
|**saMLOptions** | [**CreateDomainRequestAdvancedSecurityOptionsSAMLOptions**](CreateDomainRequestAdvancedSecurityOptionsSAMLOptions.md) |  |  [optional] |
|**anonymousAuthEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |



