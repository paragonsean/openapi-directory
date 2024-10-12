# RubrikRestApi.SamlSsoAuthnRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isForIdpTest** | **Boolean** | A Boolean that determines whether the authentication request is part of an identity provider test. A value of &#39;true&#39; indicates that the authentication request is part of an identity provider test. A value of &#39;false&#39; indicates that the authentication request is not part of an identity provider test. | [optional] [default to false]
**redirectPath** | **String** | The resource location that the Rubrik cluster redirects the browser to after a successful login. The value is the resource path portion of the URL of the resource. For example, for resource1 at http://example-host.com/resources/resource1, the value is \&quot;/resources/resource1\&quot;. | [optional] 


