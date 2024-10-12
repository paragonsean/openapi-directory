# TwilioNumbers.NumbersV1PortingPortability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The target account sid to which the number will be ported | [optional] 
**country** | **String** | Country the phone number belongs to. | [optional] 
**messagingCarrier** | **String** | Current messaging carrier of the phone number | [optional] 
**notPortableReason** | **String** | Reason why the phone number cannot be ported into Twilio, &#x60;null&#x60; otherwise. | [optional] 
**notPortableReasonCode** | **Number** | The Portability Reason Code for the phone number if it cannot be ported into Twilio, &#x60;null&#x60; otherwise. One of &#x60;22131&#x60;, &#x60;22132&#x60;, &#x60;22130&#x60;, &#x60;22133&#x60;, &#x60;22102&#x60; or &#x60;22135&#x60;. | [optional] 
**numberType** | [**PortingPortabilityEnumNumberType**](PortingPortabilityEnumNumberType.md) |  | [optional] 
**phoneNumber** | **String** | The phone number which portability is to be checked. Phone numbers are in E.164 format (e.g. +16175551212). | [optional] 
**pinAndAccountNumberRequired** | **Boolean** | Boolean flag specifying if PIN and account number is required for the phone number. | [optional] 
**portable** | **Boolean** | Boolean flag specifying if phone number is portable or not. | [optional] 
**url** | **String** | This is the url of the request that you&#39;re trying to reach out to locate the resource. | [optional] 
**voiceCarrier** | **String** | Current voice carrier of the phone number | [optional] 


