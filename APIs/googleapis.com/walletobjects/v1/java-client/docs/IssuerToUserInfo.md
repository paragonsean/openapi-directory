

# IssuerToUserInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) |  |  [optional] |
|**signUpInfo** | [**SignUpInfo**](SignUpInfo.md) |  |  [optional] |
|**url** | **String** | Currently not used, consider deprecating. |  [optional] |
|**value** | **String** | JSON web token for action S2AP. |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ACTION_UNSPECIFIED | &quot;ACTION_UNSPECIFIED&quot; |
| S2_AP | &quot;S2AP&quot; |
| S2AP | &quot;s2ap&quot; |
| SIGN_UP | &quot;SIGN_UP&quot; |
| SIGN_UP2 | &quot;signUp&quot; |



