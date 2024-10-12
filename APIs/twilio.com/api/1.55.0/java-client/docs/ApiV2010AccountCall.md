

# ApiV2010AccountCall


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Call resource. |  [optional] |
|**answeredBy** | **String** | Either &#x60;human&#x60; or &#x60;machine&#x60; if this call was initiated with answering machine detection. Empty otherwise. |  [optional] |
|**apiVersion** | **String** | The API version used to create the call. |  [optional] |
|**callerName** | **String** | The caller&#39;s name if this call was an incoming call to a phone number with caller ID Lookup enabled. Otherwise, empty. |  [optional] |
|**dateCreated** | **String** | The date and time in GMT that this resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **String** | The date and time in GMT that this resource was last updated, specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**direction** | **String** | A string describing the direction of the call. Can be: &#x60;inbound&#x60; for inbound calls, &#x60;outbound-api&#x60; for calls initiated via the REST API or &#x60;outbound-dial&#x60; for calls initiated by a &#x60;&lt;Dial&gt;&#x60; verb. Using [Elastic SIP Trunking](https://www.twilio.com/docs/sip-trunking), the values can be [&#x60;trunking-terminating&#x60;](https://www.twilio.com/docs/sip-trunking#termination) for outgoing calls from your communications infrastructure to the PSTN or [&#x60;trunking-originating&#x60;](https://www.twilio.com/docs/sip-trunking#origination) for incoming calls to your communications infrastructure from the PSTN. |  [optional] |
|**duration** | **String** | The length of the call in seconds. This value is empty for busy, failed, unanswered, or ongoing calls. |  [optional] |
|**endTime** | **String** | The time the call ended, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format. Empty if the call did not complete successfully. |  [optional] |
|**forwardedFrom** | **String** | The forwarding phone number if this call was an incoming call forwarded from another number (depends on carrier supporting forwarding). Otherwise, empty. |  [optional] |
|**from** | **String** | The phone number, SIP address, Client identifier or SIM SID that made this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). SIP addresses are formatted as &#x60;name@company.com&#x60;. Client identifiers are formatted &#x60;client:name&#x60;. SIM SIDs are formatted as &#x60;sim:sid&#x60;. |  [optional] |
|**fromFormatted** | **String** | The calling phone number, SIP address, or Client identifier formatted for display. Non-North American phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +442071838750). |  [optional] |
|**groupSid** | **String** | The Group SID associated with this call. If no Group is associated with the call, the field is empty. |  [optional] |
|**parentCallSid** | **String** | The SID that identifies the call that created this leg. |  [optional] |
|**phoneNumberSid** | **String** | If the call was inbound, this is the SID of the IncomingPhoneNumber resource that received the call. If the call was outbound, it is the SID of the OutgoingCallerId resource from which the call was placed. |  [optional] |
|**price** | **String** | The charge for this call, in the currency associated with the account. Populated after the call is completed. May not be immediately available. |  [optional] |
|**priceUnit** | **String** | The currency in which &#x60;Price&#x60; is measured, in [ISO 4127](https://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g., &#x60;USD&#x60;, &#x60;EUR&#x60;, &#x60;JPY&#x60;). Always capitalized for calls. |  [optional] |
|**queueTime** | **String** | The wait time in milliseconds before the call is placed. |  [optional] |
|**sid** | **String** | The unique string that we created to identify this Call resource. |  [optional] |
|**startTime** | **String** | The start time of the call, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format. Empty if the call has not yet been dialed. |  [optional] |
|**status** | **CallEnumStatus** |  |  [optional] |
|**subresourceUris** | **Object** | A list of subresources available to this call, identified by their URIs relative to &#x60;https://api.twilio.com&#x60;. |  [optional] |
|**to** | **String** | The phone number, SIP address, Client identifier or SIM SID that received this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). SIP addresses are formatted as &#x60;name@company.com&#x60;. Client identifiers are formatted &#x60;client:name&#x60;. SIM SIDs are formatted as &#x60;sim:sid&#x60;. |  [optional] |
|**toFormatted** | **String** | The phone number, SIP address or Client identifier that received this call. Formatted for display. Non-North American phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +442071838750). |  [optional] |
|**trunkSid** | **String** | The unique identifier of the trunk resource that was used for this call. The field is empty if the call was not made using a SIP trunk or if the call is not terminated. |  [optional] |
|**uri** | **String** | The URI of this resource, relative to &#x60;https://api.twilio.com&#x60;. |  [optional] |



