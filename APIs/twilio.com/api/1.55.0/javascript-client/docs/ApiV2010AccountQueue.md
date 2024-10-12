# TwilioApi.ApiV2010AccountQueue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Queue resource. | [optional] 
**averageWaitTime** | **Number** |  The average wait time in seconds of the members in this queue. This is calculated at the time of the request. | [optional] 
**currentSize** | **Number** | The number of calls currently in the queue. | [optional] 
**dateCreated** | **String** | The date and time in GMT that this resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **String** | The date and time in GMT that this resource was last updated, specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**friendlyName** | **String** | A string that you assigned to describe this resource. | [optional] 
**maxSize** | **Number** |  The maximum number of calls that can be in the queue. The default is 1000 and the maximum is 5000. | [optional] 
**sid** | **String** | The unique string that that we created to identify this Queue resource. | [optional] 
**uri** | **String** | The URI of this resource, relative to &#x60;https://api.twilio.com&#x60;. | [optional] 


