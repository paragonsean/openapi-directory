# AwsSsoOidc.CreateTokenRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | The unique identifier string for each client. This value should come from the persisted result of the &lt;a&gt;RegisterClient&lt;/a&gt; API. | 
**clientSecret** | **String** | A secret string generated for the client. This value should come from the persisted result of the &lt;a&gt;RegisterClient&lt;/a&gt; API. | 
**grantType** | **String** | &lt;p&gt;Supports grant types for the authorization code, refresh token, and device code request. For device code requests, specify the following value:&lt;/p&gt; &lt;p&gt; &lt;code&gt;urn:ietf:params:oauth:grant-type:&lt;i&gt;device_code&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;For information about how to obtain the device code, see the &lt;a&gt;StartDeviceAuthorization&lt;/a&gt; topic.&lt;/p&gt; | 
**deviceCode** | **String** | Used only when calling this API for the device code grant type. This short-term code is used to identify this authentication attempt. This should come from an in-memory reference to the result of the &lt;a&gt;StartDeviceAuthorization&lt;/a&gt; API. | [optional] 
**code** | **String** | The authorization code received from the authorization service. This parameter is required to perform an authorization grant request to get access to a token. | [optional] 
**refreshToken** | **String** | &lt;p&gt;Currently, &lt;code&gt;refreshToken&lt;/code&gt; is not yet implemented and is not supported. For more information about the features and limitations of the current IAM Identity Center OIDC implementation, see &lt;i&gt;Considerations for Using this Guide&lt;/i&gt; in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html\&quot;&gt;IAM Identity Center OIDC API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The token used to obtain an access token in the event that the access token is invalid or expired.&lt;/p&gt; | [optional] 
**scope** | **[String]** | The list of scopes that is defined by the client. Upon authorization, this list is used to restrict permissions when granting an access token. | [optional] 
**redirectUri** | **String** | The location of the application that will receive the authorization code. Users authorize the service to send the request to this location. | [optional] 


