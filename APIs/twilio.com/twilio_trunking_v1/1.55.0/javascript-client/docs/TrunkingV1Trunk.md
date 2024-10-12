# TwilioTrunking.TrunkingV1Trunk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Trunk resource. | [optional] 
**authType** | **String** | The types of authentication mapped to the domain. Can be: &#x60;IP_ACL&#x60; and &#x60;CREDENTIAL_LIST&#x60;. If both are mapped, the values are returned in a comma delimited list. If empty, the domain will not receive any traffic. | [optional] 
**authTypeSet** | **[String]** | Reserved. | [optional] 
**cnamLookupEnabled** | **Boolean** | Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**disasterRecoveryMethod** | **String** | The HTTP method we use to call the &#x60;disaster_recovery_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**disasterRecoveryUrl** | **String** | The URL we call using the &#x60;disaster_recovery_method&#x60; if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from this URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information. | [optional] 
**domainName** | **String** | The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and &#x60;-&#x60; and must end with &#x60;pstn.twilio.com&#x60;. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**links** | **Object** | The URLs of related resources. | [optional] 
**recording** | **Object** | The recording settings for the trunk. Can be: &#x60;do-not-record&#x60;, &#x60;record-from-ringing&#x60;, &#x60;record-from-answer&#x60;. If set to &#x60;record-from-ringing&#x60; or &#x60;record-from-answer&#x60;, all calls going through the trunk will be recorded. The only way to change recording parameters is on a sub-resource of a Trunk after it has been created. e.g.&#x60;/Trunks/[Trunk_SID]/Recording -XPOST -d&#39;Mode&#x3D;record-from-answer&#39;&#x60;. See [Recording](https://www.twilio.com/docs/sip-trunking#recording) for more information. | [optional] 
**secure** | **Boolean** | Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information. | [optional] 
**sid** | **String** | The unique string that we created to identify the Trunk resource. | [optional] 
**transferCallerId** | [**TrunkEnumTransferCallerId**](TrunkEnumTransferCallerId.md) |  | [optional] 
**transferMode** | [**TrunkEnumTransferSetting**](TrunkEnumTransferSetting.md) |  | [optional] 
**url** | **String** | The absolute URL of the resource. | [optional] 



## Enum: DisasterRecoveryMethodEnum


* `HEAD` (value: `"HEAD"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PATCH` (value: `"PATCH"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)




