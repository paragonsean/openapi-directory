

# Compatibility

Product compatibility

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Full error message if any compatibility issues are found |  [optional] |
|**isCompatible** | **Boolean** | Tells if product is compatible with current device |  [optional] |
|**issues** | [**List&lt;IssuesEnum&gt;**](#List&lt;IssuesEnum&gt;) | List of all issues found |  [optional] |
|**message** | **String** | Short error message if any compatibility issues are found |  [optional] |



## Enum: List&lt;IssuesEnum&gt;

| Name | Value |
|---- | -----|
| HIGHER_DEVICE_VERSION_REQUIRED | &quot;HigherDeviceVersionRequired&quot; |
| LOWER_DEVICE_VERSION_REQUIRED | &quot;LowerDeviceVersionRequired&quot; |
| CAPACITY_BILLING_MODEL_REQUIRED | &quot;CapacityBillingModelRequired&quot; |
| PAY_AS_YOU_GO_BILLING_MODEL_REQUIRED | &quot;PayAsYouGoBillingModelRequired&quot; |
| DEVELOPMENT_BILLING_MODEL_REQUIRED | &quot;DevelopmentBillingModelRequired&quot; |
| AZURE_AD_IDENTITY_SYSTEM_REQUIRED | &quot;AzureADIdentitySystemRequired&quot; |
| ADFS_IDENTITY_SYSTEM_REQUIRED | &quot;ADFSIdentitySystemRequired&quot; |
| CONNECTION_TO_INTERNET_REQUIRED | &quot;ConnectionToInternetRequired&quot; |
| CONNECTION_TO_AZURE_REQUIRED | &quot;ConnectionToAzureRequired&quot; |
| DISCONNECTED_ENVIRONMENT_REQUIRED | &quot;DisconnectedEnvironmentRequired&quot; |



