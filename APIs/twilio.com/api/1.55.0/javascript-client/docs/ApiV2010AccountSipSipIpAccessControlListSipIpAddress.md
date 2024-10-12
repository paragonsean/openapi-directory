# TwilioApi.ApiV2010AccountSipSipIpAccessControlListSipIpAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The unique id of the Account that is responsible for this resource. | [optional] 
**cidrPrefixLength** | **Number** | An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used. | [optional] 
**dateCreated** | **String** | The date that this resource was created, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format. | [optional] 
**dateUpdated** | **String** | The date that this resource was last updated, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format. | [optional] 
**friendlyName** | **String** | A human readable descriptive text for this resource, up to 255 characters long. | [optional] 
**ipAccessControlListSid** | **String** | The unique id of the IpAccessControlList resource that includes this resource. | [optional] 
**ipAddress** | **String** | An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today. | [optional] 
**sid** | **String** | A 34 character string that uniquely identifies this resource. | [optional] 
**uri** | **String** | The URI for this resource, relative to &#x60;https://api.twilio.com&#x60; | [optional] 


