

# MessagingV1ServiceUsAppToPerson


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the Campaign belongs to. |  [optional] |
|**ageGated** | **Boolean** | A boolean that specifies whether campaign is age gated or not. |  [optional] |
|**brandRegistrationSid** | **String** | The unique string to identify the A2P brand. |  [optional] |
|**campaignId** | **String** | The Campaign Registry (TCR) Campaign ID. |  [optional] |
|**campaignStatus** | **String** | Campaign status. Examples: IN_PROGRESS, VERIFIED, FAILED. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**description** | **String** | A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters. |  [optional] |
|**directLending** | **Boolean** | A boolean that specifies whether campaign allows direct lending or not. |  [optional] |
|**errors** | **List&lt;Object&gt;** | Details indicating why a campaign registration failed. These errors can indicate one or more fields that were incorrect or did not meet review requirements. |  [optional] |
|**hasEmbeddedLinks** | **Boolean** | Indicate that this SMS campaign will send messages that contain links. |  [optional] |
|**hasEmbeddedPhone** | **Boolean** | Indicates that this SMS campaign will send messages that contain phone numbers. |  [optional] |
|**helpKeywords** | **List&lt;String&gt;** | End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum. |  [optional] |
|**helpMessage** | **String** | When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). 20 character minimum. 320 character maximum. |  [optional] |
|**isExternallyRegistered** | **Boolean** | Indicates whether the campaign was registered externally or not. |  [optional] |
|**messageFlow** | **String** | Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum. |  [optional] |
|**messageSamples** | **List&lt;String&gt;** | An array of sample message strings, min two and max five. Min length for each sample: 20 chars. Max length for each sample: 1024 chars. |  [optional] |
|**messagingServiceSid** | **String** | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) that the resource is associated with. |  [optional] |
|**mock** | **Boolean** | A boolean that specifies whether campaign is a mock or not. Mock campaigns will be automatically created if using a mock brand. Mock campaigns should only be used for testing purposes. |  [optional] |
|**optInKeywords** | **List&lt;String&gt;** | If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum. |  [optional] |
|**optInMessage** | **String** | If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum. |  [optional] |
|**optOutKeywords** | **List&lt;String&gt;** | End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum. |  [optional] |
|**optOutMessage** | **String** | Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). 20 character minimum. 320 character maximum. |  [optional] |
|**rateLimits** | **Object** | Rate limit and/or classification set by each carrier, Ex. AT&amp;T or T-Mobile. |  [optional] |
|**sid** | **String** | The unique string that identifies a US A2P Compliance resource &#x60;QE2c6890da8086d771620e9b13fadeba0b&#x60;. |  [optional] |
|**subscriberOptIn** | **Boolean** | A boolean that specifies whether campaign has Subscriber Optin or not. |  [optional] |
|**url** | **URI** | The absolute URL of the US App to Person resource. |  [optional] |
|**usAppToPersonUsecase** | **String** | A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING, SOLE_PROPRIETOR...]. SOLE_PROPRIETOR campaign use cases can only be created by SOLE_PROPRIETOR Brands, and there can only be one SOLE_PROPRIETOR campaign created per SOLE_PROPRIETOR Brand. |  [optional] |



