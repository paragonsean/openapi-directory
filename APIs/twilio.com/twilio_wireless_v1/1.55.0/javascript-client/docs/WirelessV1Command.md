# TwilioWireless.WirelessV1Command

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Command resource. | [optional] 
**command** | **String** | The message being sent to or from the SIM. For text mode messages, this can be up to 160 characters. For binary mode messages, this is a series of up to 140 bytes of data encoded using base64. | [optional] 
**commandMode** | [**CommandEnumCommandMode**](CommandEnumCommandMode.md) |  | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. | [optional] 
**deliveryReceiptRequested** | **Boolean** | Whether to request a delivery receipt. | [optional] 
**direction** | [**CommandEnumDirection**](CommandEnumDirection.md) |  | [optional] 
**sid** | **String** | The unique string that we created to identify the Command resource. | [optional] 
**simSid** | **String** | The SID of the [Sim resource](https://www.twilio.com/docs/iot/wireless/api/sim-resource) that the Command was sent to or from. | [optional] 
**status** | [**CommandEnumStatus**](CommandEnumStatus.md) |  | [optional] 
**transport** | [**CommandEnumTransport**](CommandEnumTransport.md) |  | [optional] 
**url** | **String** | The absolute URL of the resource. | [optional] 


