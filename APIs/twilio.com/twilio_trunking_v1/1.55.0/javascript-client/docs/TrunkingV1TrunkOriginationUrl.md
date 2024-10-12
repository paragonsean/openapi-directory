# TwilioTrunking.TrunkingV1TrunkOriginationUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OriginationUrl resource. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**enabled** | **Boolean** | Whether the URL is enabled. The default is &#x60;true&#x60;. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**priority** | **Number** | The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI. | [optional] 
**sid** | **String** | The unique string that we created to identify the OriginationUrl resource. | [optional] 
**sipUrl** | **String** | The SIP address you want Twilio to route your Origination calls to. This must be a &#x60;sip:&#x60; schema. | [optional] 
**trunkSid** | **String** | The SID of the Trunk that owns the Origination URL. | [optional] 
**url** | **String** | The absolute URL of the resource. | [optional] 
**weight** | **Number** | The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority. | [optional] 


