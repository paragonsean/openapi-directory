

# AdvancedSecurityOptionsInput

Specifies the advanced security configuration: whether advanced security is enabled, whether the internal database option is enabled, master username and password (if internal database is enabled), and master user ARN (if IAM is enabled).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**internalUserDatabaseEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**masterUserOptions** | [**CreateElasticsearchDomainRequestAdvancedSecurityOptionsMasterUserOptions**](CreateElasticsearchDomainRequestAdvancedSecurityOptionsMasterUserOptions.md) |  |  [optional] |
|**saMLOptions** | [**CreateElasticsearchDomainRequestAdvancedSecurityOptionsSAMLOptions**](CreateElasticsearchDomainRequestAdvancedSecurityOptionsSAMLOptions.md) |  |  [optional] |
|**anonymousAuthEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |



