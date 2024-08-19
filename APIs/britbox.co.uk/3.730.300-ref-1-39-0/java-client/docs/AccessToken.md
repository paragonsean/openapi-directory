

# AccessToken


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountCreated** | **Boolean** | When a &#x60;UserAccount&#x60; token is issued during a single-sign-on flow a user may have been automatically registered if they didn&#39;t have an account already. If this occurs then &#x60;accountCreated&#x60; will be &#x60;true&#x60;.  |  [optional] |
|**expirationDate** | **OffsetDateTime** | The timestamp this token expires. |  |
|**refreshable** | **Boolean** | True if this token can be refreshed, false if not. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the token. |  |
|**value** | **String** | The token value used for authenticated requests. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| USER_ACCOUNT | &quot;UserAccount&quot; |
| USER_PROFILE | &quot;UserProfile&quot; |



