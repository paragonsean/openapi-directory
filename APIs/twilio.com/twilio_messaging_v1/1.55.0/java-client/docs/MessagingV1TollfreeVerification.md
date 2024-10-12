

# MessagingV1TollfreeVerification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Tollfree Verification resource. |  [optional] |
|**additionalInformation** | **String** | Additional information to be provided for verification. |  [optional] |
|**businessCity** | **String** | The city of the business or organization using the Tollfree number. |  [optional] |
|**businessContactEmail** | **String** | The email address of the contact for the business or organization using the Tollfree number. |  [optional] |
|**businessContactFirstName** | **String** | The first name of the contact for the business or organization using the Tollfree number. |  [optional] |
|**businessContactLastName** | **String** | The last name of the contact for the business or organization using the Tollfree number. |  [optional] |
|**businessContactPhone** | **String** | The E.164 formatted phone number of the contact for the business or organization using the Tollfree number. |  [optional] |
|**businessCountry** | **String** | The country of the business or organization using the Tollfree number. |  [optional] |
|**businessName** | **String** | The name of the business or organization using the Tollfree number. |  [optional] |
|**businessPostalCode** | **String** | The postal code of the business or organization using the Tollfree number. |  [optional] |
|**businessStateProvinceRegion** | **String** | The state/province/region of the business or organization using the Tollfree number. |  [optional] |
|**businessStreetAddress** | **String** | The address of the business or organization using the Tollfree number. |  [optional] |
|**businessStreetAddress2** | **String** | The address of the business or organization using the Tollfree number. |  [optional] |
|**businessWebsite** | **String** | The website of the business or organization using the Tollfree number. |  [optional] |
|**customerProfileSid** | **String** | Customer&#39;s Profile Bundle BundleSid. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**editAllowed** | **Boolean** | If a rejected verification is allowed to be edited/resubmitted. Some rejection reasons allow editing and some do not. |  [optional] |
|**editExpiration** | **OffsetDateTime** | The date and time when the ability to edit a rejected verification expires. |  [optional] |
|**errorCode** | **Integer** | The error code given when a Tollfree Verification has been rejected. |  [optional] |
|**externalReferenceId** | **String** | An optional external reference ID supplied by customer and echoed back on status retrieval. |  [optional] |
|**messageVolume** | **String** | Estimate monthly volume of messages from the Tollfree Number. |  [optional] |
|**notificationEmail** | **String** | The email address to receive the notification about the verification result. . |  [optional] |
|**optInImageUrls** | **List&lt;String&gt;** | Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL. |  [optional] |
|**optInType** | **TollfreeVerificationEnumOptInType** |  |  [optional] |
|**productionMessageSample** | **String** | An example of message content, i.e. a sample message. |  [optional] |
|**regulatedItemSid** | **String** | The SID of the Regulated Item. |  [optional] |
|**rejectionReason** | **String** | The rejection reason given when a Tollfree Verification has been rejected. |  [optional] |
|**rejectionReasons** | **List&lt;Object&gt;** | A list of rejection reasons and codes describing why a Tollfree Verification has been rejected. |  [optional] |
|**resourceLinks** | **Object** | The URLs of the documents associated with the Tollfree Verification resource. |  [optional] |
|**sid** | **String** | The unique string to identify Tollfree Verification. |  [optional] |
|**status** | **TollfreeVerificationEnumStatus** |  |  [optional] |
|**tollfreePhoneNumberSid** | **String** | The SID of the Phone Number associated with the Tollfree Verification. |  [optional] |
|**trustProductSid** | **String** | Tollfree TrustProduct Bundle BundleSid. |  [optional] |
|**url** | **URI** | The absolute URL of the Tollfree Verification resource. |  [optional] |
|**useCaseCategories** | **List&lt;String&gt;** | The category of the use case for the Tollfree Number. List as many are applicable.. |  [optional] |
|**useCaseSummary** | **String** | Use this to further explain how messaging is used by the business or organization. |  [optional] |



