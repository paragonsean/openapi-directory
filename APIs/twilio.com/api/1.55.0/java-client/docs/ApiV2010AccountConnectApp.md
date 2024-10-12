

# ApiV2010AccountConnectApp


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource. |  [optional] |
|**authorizeRedirectUrl** | **URI** | The URL we redirect the user to after we authenticate the user and obtain authorization to access the Connect App. |  [optional] |
|**companyName** | **String** | The company name set for the Connect App. |  [optional] |
|**deauthorizeCallbackMethod** | [**DeauthorizeCallbackMethodEnum**](#DeauthorizeCallbackMethodEnum) | The HTTP method we use to call &#x60;deauthorize_callback_url&#x60;. |  [optional] |
|**deauthorizeCallbackUrl** | **URI** | The URL we call using the &#x60;deauthorize_callback_method&#x60; to de-authorize the Connect App. |  [optional] |
|**description** | **String** | The description of the Connect App. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the resource. |  [optional] |
|**homepageUrl** | **URI** | The public URL where users can obtain more information about this Connect App. |  [optional] |
|**permissions** | **List&lt;ConnectAppEnumPermission&gt;** | The set of permissions that your ConnectApp requests. |  [optional] |
|**sid** | **String** | The unique string that that we created to identify the ConnectApp resource. |  [optional] |
|**uri** | **String** | The URI of the resource, relative to &#x60;https://api.twilio.com&#x60;. |  [optional] |



## Enum: DeauthorizeCallbackMethodEnum

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PATCH | &quot;PATCH&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |



