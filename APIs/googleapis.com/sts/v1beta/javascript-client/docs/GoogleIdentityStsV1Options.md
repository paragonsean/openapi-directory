# SecurityTokenServiceApi.GoogleIdentityStsV1Options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessBoundary** | [**GoogleIdentityStsV1AccessBoundary**](GoogleIdentityStsV1AccessBoundary.md) |  | [optional] 
**audiences** | **[String]** | The intended audience(s) of the credential. The audience value(s) should be the name(s) of services intended to receive the credential. Example: &#x60;[\&quot;https://pubsub.googleapis.com/\&quot;, \&quot;https://storage.googleapis.com/\&quot;]&#x60;. A maximum of 5 audiences can be included. For each provided audience, the maximum length is 262 characters. | [optional] 
**userProject** | **String** | A Google project used for quota and billing purposes when the credential is used to access Google APIs. The provided project overrides the project bound to the credential. The value must be a project number or a project ID. Example: &#x60;my-sample-project-191923&#x60;. The maximum length is 32 characters. | [optional] 


