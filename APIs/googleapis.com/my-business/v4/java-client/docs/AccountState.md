

# AccountState

Indicates status of the account, such as whether the account has been verified by Google.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | If verified, future locations that are created are automatically connected to Google Maps, and have Google+ pages created, without requiring moderation. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACCOUNT_STATUS_UNSPECIFIED | &quot;ACCOUNT_STATUS_UNSPECIFIED&quot; |
| VERIFIED | &quot;VERIFIED&quot; |
| UNVERIFIED | &quot;UNVERIFIED&quot; |
| VERIFICATION_REQUESTED | &quot;VERIFICATION_REQUESTED&quot; |



