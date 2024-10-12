# TwilioNumbers.NumbersV1PortingPortInFetch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The Account SID that the numbers will be added to after they are ported into Twilio. | [optional] 
**documents** | **[String]** | The list of documents SID referencing a utility bills | [optional] 
**losingCarrierInformation** | **Object** | The information for the losing carrier.  | [optional] 
**notificationEmails** | **[String]** | List of emails for getting notifications about the LOA signing process. Allowed Max 10 emails. | [optional] 
**phoneNumbers** | **[Object]** | The list of phone numbers to Port in. Phone numbers are in E.164 format (e.g. +16175551212). | [optional] 
**portInRequestSid** | **String** | The SID of the Port In request. This is a unique identifier of the port in request. | [optional] 
**targetPortInDate** | **Date** | Minimum number of days in the future (at least 2 days) needs to be established with the Ops team for validation. | [optional] 
**targetPortInTimeRangeEnd** | **String** | Maximum hour in the future needs to be established with the Ops team for validation. | [optional] 
**targetPortInTimeRangeStart** | **String** | Minimum hour in the future needs to be established with the Ops team for validation. | [optional] 
**url** | **String** | The URL of this Port In request | [optional] 


