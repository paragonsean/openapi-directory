

# ApiV2010AccountShortCode


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this ShortCode resource. |  [optional] |
|**apiVersion** | **String** | The API version used to start a new TwiML session when an SMS message is sent to this short code. |  [optional] |
|**dateCreated** | **String** | The date and time in GMT that this resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **String** | The date and time in GMT that this resource was last updated, specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**friendlyName** | **String** | A string that you assigned to describe this resource. By default, the &#x60;FriendlyName&#x60; is the short code. |  [optional] |
|**shortCode** | **String** | The short code. e.g., 894546. |  [optional] |
|**sid** | **String** | The unique string that that we created to identify this ShortCode resource. |  [optional] |
|**smsFallbackMethod** | [**SmsFallbackMethodEnum**](#SmsFallbackMethodEnum) | The HTTP method we use to call the &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. |  [optional] |
|**smsFallbackUrl** | **URI** | The URL that we call if an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;. |  [optional] |
|**smsMethod** | [**SmsMethodEnum**](#SmsMethodEnum) | The HTTP method we use to call the &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. |  [optional] |
|**smsUrl** | **URI** | The URL we call when receiving an incoming SMS message to this short code. |  [optional] |
|**uri** | **String** | The URI of this resource, relative to &#x60;https://api.twilio.com&#x60;. |  [optional] |



## Enum: SmsFallbackMethodEnum

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PATCH | &quot;PATCH&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |



## Enum: SmsMethodEnum

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PATCH | &quot;PATCH&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |



