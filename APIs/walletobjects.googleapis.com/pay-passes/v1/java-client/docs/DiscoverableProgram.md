

# DiscoverableProgram

Information about how a class may be discovered and instantiated from within the Android Pay app. This is done by searching for a loyalty or gift card program and scanning or manually entering.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**merchantSigninInfo** | [**DiscoverableProgramMerchantSigninInfo**](DiscoverableProgramMerchantSigninInfo.md) |  |  [optional] |
|**merchantSignupInfo** | [**DiscoverableProgramMerchantSignupInfo**](DiscoverableProgramMerchantSignupInfo.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Visibility state of the discoverable program. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| TRUSTED_TESTERS | &quot;TRUSTED_TESTERS&quot; |
| TRUSTED_TESTERS2 | &quot;trustedTesters&quot; |
| LIVE | &quot;LIVE&quot; |
| LIVE2 | &quot;live&quot; |
| DISABLED | &quot;DISABLED&quot; |
| DISABLED2 | &quot;disabled&quot; |



