

# ExternalAction

Action that is implemented and performed outside of the third-party application. It should redirect the merchant to the provided URL of an external system where they can perform the action. For example to request a review in the Merchant Center.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | The type of external action. |  [optional] |
|**uri** | **String** | URL to external system, for example Merchant Center, where the merchant can perform the action. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EXTERNAL_ACTION_TYPE_UNSPECIFIED | &quot;EXTERNAL_ACTION_TYPE_UNSPECIFIED&quot; |
| REVIEW_PRODUCT_ISSUE_IN_MERCHANT_CENTER | &quot;REVIEW_PRODUCT_ISSUE_IN_MERCHANT_CENTER&quot; |
| REVIEW_ACCOUNT_ISSUE_IN_MERCHANT_CENTER | &quot;REVIEW_ACCOUNT_ISSUE_IN_MERCHANT_CENTER&quot; |
| LEGAL_APPEAL_IN_HELP_CENTER | &quot;LEGAL_APPEAL_IN_HELP_CENTER&quot; |
| VERIFY_IDENTITY_IN_MERCHANT_CENTER | &quot;VERIFY_IDENTITY_IN_MERCHANT_CENTER&quot; |



