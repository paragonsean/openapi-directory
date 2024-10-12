

# AccessDeniedPageSettings

Custom content configuration for access denied page. IAP allows customers to define a custom URI to use as the error page when access is denied to users. If IAP prevents access to this page, the default IAP error page will be displayed instead.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessDeniedPageUri** | **String** | The URI to be redirected to when access is denied. |  [optional] |
|**generateTroubleshootingUri** | **Boolean** | Whether to generate a troubleshooting URL on access denied events to this application. |  [optional] |
|**remediationTokenGenerationEnabled** | **Boolean** | Whether to generate remediation token on access denied events to this application. |  [optional] |



