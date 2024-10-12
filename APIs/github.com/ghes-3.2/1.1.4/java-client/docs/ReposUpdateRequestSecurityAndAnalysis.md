

# ReposUpdateRequestSecurityAndAnalysis

Specify which security and analysis features to enable or disable for the repository.  To use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see \"[Managing security managers in your organization](https://docs.github.com/enterprise-server@3.2/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).\"  For example, to enable GitHub Advanced Security, use this data in the body of the `PATCH` request: `{ \"security_and_analysis\": {\"advanced_security\": { \"status\": \"enabled\" } } }`.  You can check which security and analysis features are currently enabled by using a `GET /repos/{owner}/{repo}` request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advancedSecurity** | [**ReposUpdateRequestSecurityAndAnalysisAdvancedSecurity**](ReposUpdateRequestSecurityAndAnalysisAdvancedSecurity.md) |  |  [optional] |
|**secretScanning** | [**ReposUpdateRequestSecurityAndAnalysisSecretScanning**](ReposUpdateRequestSecurityAndAnalysisSecretScanning.md) |  |  [optional] |
|**secretScanningPushProtection** | [**ReposUpdateRequestSecurityAndAnalysisSecretScanningPushProtection**](ReposUpdateRequestSecurityAndAnalysisSecretScanningPushProtection.md) |  |  [optional] |



