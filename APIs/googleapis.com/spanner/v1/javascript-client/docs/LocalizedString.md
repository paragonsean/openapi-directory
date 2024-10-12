# CloudSpannerApi.LocalizedString

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **{String: String}** | A map of arguments used when creating the localized message. Keys represent parameter names which may be used by the localized version when substituting dynamic values. | [optional] 
**message** | **String** | The canonical English version of this message. If no token is provided or the front-end has no message associated with the token, this text will be displayed as-is. | [optional] 
**token** | **String** | The token identifying the message, e.g. &#39;METRIC_READ_CPU&#39;. This should be unique within the service. | [optional] 


