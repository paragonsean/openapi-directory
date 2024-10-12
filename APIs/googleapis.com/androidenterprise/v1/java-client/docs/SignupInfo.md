

# SignupInfo

A resource returned by the GenerateSignupUrl API, which contains the Signup URL and Completion Token.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completionToken** | **String** | An opaque token that will be required, along with the Enterprise Token, for obtaining the enterprise resource from CompleteSignup. |  [optional] |
|**kind** | **String** | Deprecated. |  [optional] |
|**url** | **String** | A URL under which the Admin can sign up for an enterprise. The page pointed to cannot be rendered in an iframe. |  [optional] |



