

# ProvisioningIssue

Information about issues with provisioning a Managed Certificate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **String** | Output only. Human readable explanation about the issue. Provided to help address the configuration issues. Not guaranteed to be stable. For programmatic access use Reason enum. |  [optional] [readonly] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Output only. Reason for provisioning failures. |  [optional] [readonly] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| REASON_UNSPECIFIED | &quot;REASON_UNSPECIFIED&quot; |
| AUTHORIZATION_ISSUE | &quot;AUTHORIZATION_ISSUE&quot; |
| RATE_LIMITED | &quot;RATE_LIMITED&quot; |



