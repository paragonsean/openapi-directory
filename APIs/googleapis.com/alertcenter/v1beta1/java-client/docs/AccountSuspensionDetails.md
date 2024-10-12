

# AccountSuspensionDetails

Details about why an account is receiving an account suspension warning.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**abuseReason** | [**AbuseReasonEnum**](#AbuseReasonEnum) | The reason why this account is receiving an account suspension warning. |  [optional] |
|**productName** | **String** | The name of the product being abused. This is restricted to only the following values: \&quot;Gmail\&quot; \&quot;Google Workspace\&quot; \&quot;Payments\&quot; \&quot;Voice\&quot; \&quot;YouTube\&quot; \&quot;Other\&quot; |  [optional] |



## Enum: AbuseReasonEnum

| Name | Value |
|---- | -----|
| ACCOUNT_SUSPENSION_ABUSE_REASON_UNSPECIFIED | &quot;ACCOUNT_SUSPENSION_ABUSE_REASON_UNSPECIFIED&quot; |
| TOS_VIOLATION | &quot;TOS_VIOLATION&quot; |
| SPAM | &quot;SPAM&quot; |
| PHISHING | &quot;PHISHING&quot; |
| TRAFFIC_PUMPING | &quot;TRAFFIC_PUMPING&quot; |
| FRAUD | &quot;FRAUD&quot; |
| NUMBER_HARVESTING | &quot;NUMBER_HARVESTING&quot; |
| PAYMENTS_FRAUD | &quot;PAYMENTS_FRAUD&quot; |
| UNWANTED_CONTENT | &quot;UNWANTED_CONTENT&quot; |



