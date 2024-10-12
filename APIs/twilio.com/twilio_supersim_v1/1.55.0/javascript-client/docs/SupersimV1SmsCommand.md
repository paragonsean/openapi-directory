# TwilioSupersim.SupersimV1SmsCommand

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SMS Command resource. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**direction** | [**SmsCommandEnumDirection**](SmsCommandEnumDirection.md) |  | [optional] 
**payload** | **String** | The message body of the SMS Command sent to or from the SIM. For text mode messages, this can be up to 160 characters. | [optional] 
**sid** | **String** | The unique string that we created to identify the SMS Command resource. | [optional] 
**simSid** | **String** | The SID of the [SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) that this SMS Command was sent to or from. | [optional] 
**status** | [**SmsCommandEnumStatus**](SmsCommandEnumStatus.md) |  | [optional] 
**url** | **String** | The absolute URL of the SMS Command resource. | [optional] 


