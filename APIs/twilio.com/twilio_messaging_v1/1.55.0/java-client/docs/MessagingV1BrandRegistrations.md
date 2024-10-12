

# MessagingV1BrandRegistrations


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**a2pProfileBundleSid** | **String** | A2P Messaging Profile Bundle BundleSid. |  [optional] |
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Brand Registration resource. |  [optional] |
|**brandFeedback** | **List&lt;BrandRegistrationsEnumBrandFeedback&gt;** | Feedback on how to improve brand score |  [optional] |
|**brandScore** | **Integer** | The secondary vetting score if it was done. Otherwise, it will be the brand score if it&#39;s returned from TCR. It may be null if no score is available. |  [optional] |
|**brandType** | **String** | Type of brand. One of: \&quot;STANDARD\&quot;, \&quot;SOLE_PROPRIETOR\&quot;. SOLE_PROPRIETOR is for the low volume, SOLE_PROPRIETOR campaign use case. There can only be one SOLE_PROPRIETOR campaign created per SOLE_PROPRIETOR brand. STANDARD is for all other campaign use cases. Multiple campaign use cases can be created per STANDARD brand. |  [optional] |
|**customerProfileBundleSid** | **String** | A2P Messaging Profile Bundle BundleSid. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**failureReason** | **String** | A reason why brand registration has failed. Only applicable when status is FAILED. |  [optional] |
|**governmentEntity** | **Boolean** | Identified as a government entity |  [optional] |
|**identityStatus** | **BrandRegistrationsEnumIdentityStatus** |  |  [optional] |
|**links** | **Object** |  |  [optional] |
|**mock** | **Boolean** | A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided. |  [optional] |
|**russell3000** | **Boolean** | Publicly traded company identified in the Russell 3000 Index |  [optional] |
|**sid** | **String** | The unique string to identify Brand Registration. |  [optional] |
|**skipAutomaticSecVet** | **Boolean** | A flag to disable automatic secondary vetting for brands which it would otherwise be done. |  [optional] |
|**status** | **BrandRegistrationsEnumStatus** |  |  [optional] |
|**taxExemptStatus** | **String** | Nonprofit organization tax-exempt status per section 501 of the U.S. tax code. |  [optional] |
|**tcrId** | **String** | Campaign Registry (TCR) Brand ID. Assigned only after successful brand registration. |  [optional] |
|**url** | **URI** | The absolute URL of the Brand Registration resource. |  [optional] |



