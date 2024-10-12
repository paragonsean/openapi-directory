# CloudPubSubApi.PushConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **{String: String}** | Endpoint configuration attributes. Every endpoint has a set of API supported attributes that can be used to control different aspects of the message delivery. The currently supported attribute is &#x60;x-goog-version&#x60;, which you can use to change the format of the push message. This attribute indicates the version of the data expected by the endpoint. This controls the shape of the envelope (i.e. its fields and metadata). The endpoint version is based on the version of the Pub/Sub API. If not present during the &#x60;CreateSubscription&#x60; call, it will default to the version of the API used to make such call. If not present during a &#x60;ModifyPushConfig&#x60; call, its value will not be changed. &#x60;GetSubscription&#x60; calls will always return a valid version, even if the subscription was created without this attribute. The possible values for this attribute are: * &#x60;v1beta1&#x60;: uses the push format defined in the v1beta1 Pub/Sub API. * &#x60;v1&#x60; or &#x60;v1beta2&#x60;: uses the push format defined in the v1 Pub/Sub API. | [optional] 
**oidcToken** | [**OidcToken**](OidcToken.md) |  | [optional] 
**pushEndpoint** | **String** | A URL locating the endpoint to which messages should be pushed. For example, a Webhook endpoint might use \&quot;https://example.com/push\&quot;. | [optional] 


