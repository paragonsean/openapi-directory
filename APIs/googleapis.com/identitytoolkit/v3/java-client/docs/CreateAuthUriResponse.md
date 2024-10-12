

# CreateAuthUriResponse

Response of creating the IDP authentication URL.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allProviders** | **List&lt;String&gt;** | all providers the user has once used to do federated login |  [optional] |
|**authUri** | **String** | The URI used by the IDP to authenticate the user. |  [optional] |
|**captchaRequired** | **Boolean** | True if captcha is required. |  [optional] |
|**forExistingProvider** | **Boolean** | True if the authUri is for user&#39;s existing provider. |  [optional] |
|**kind** | **String** | The fixed string identitytoolkit#CreateAuthUriResponse\&quot;. |  [optional] |
|**providerId** | **String** | The provider ID of the auth URI. |  [optional] |
|**registered** | **Boolean** | Whether the user is registered if the identifier is an email. |  [optional] |
|**sessionId** | **String** | Session ID which should be passed in the following verifyAssertion request. |  [optional] |
|**signinMethods** | **List&lt;String&gt;** | All sign-in methods this user has used. |  [optional] |



