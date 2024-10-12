

# PayeeDetailResponseV4


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptTermsAndConditionsTimestamp** | **OffsetDateTime** | The timestamp when the payee last accepted T&amp;Cs |  [optional] [readonly] |
|**address** | [**PayeeAddressV4**](PayeeAddressV4.md) |  |  [optional] |
|**cellphoneNumber** | **String** |  |  [optional] |
|**challenge** | [**ChallengeV4**](ChallengeV4.md) |  |  [optional] |
|**company** | [**CompanyV4**](CompanyV4.md) |  |  [optional] |
|**country** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] |
|**disabled** | **Boolean** |  |  [optional] |
|**disabledComment** | **String** |  |  [optional] |
|**disabledUpdatedTimestamp** | **OffsetDateTime** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**enhancedKycCompleted** | **Boolean** |  |  [optional] |
|**gracePeriodEndDate** | **LocalDate** |  |  [optional] [readonly] |
|**individual** | [**IndividualV4**](IndividualV4.md) |  |  [optional] |
|**kycCompletedTimestamp** | **String** |  |  [optional] |
|**language** | **String** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  |  [optional] |
|**marketingOptInDecision** | **Boolean** |  |  [optional] |
|**marketingOptInTimestamp** | **String** |  |  [optional] |
|**onboardedStatus** | **String** | Payee onboarded status. One of the following values: CREATED, INVITED, REGISTERED, ONBOARDED |  [optional] |
|**pausePayment** | **Boolean** |  |  [optional] |
|**pausePaymentTimestamp** | **String** |  |  [optional] |
|**payeeId** | **UUID** |  |  [optional] [readonly] |
|**payeeType** | **String** | Type of Payee. One of the following values: Individual, Company |  [optional] |
|**payorRefs** | [**List&lt;PayeePayorRefV4&gt;**](PayeePayorRefV4.md) |  |  [optional] [readonly] |
|**watchlistOverrideComment** | **String** |  |  [optional] |
|**watchlistOverrideExpiresAtTimestamp** | **OffsetDateTime** |  |  [optional] |
|**watchlistStatus** | **String** | Current watchlist status. One of the following values: NONE, PENDING, REVIEW, PASSED, FAILED |  [optional] |
|**watchlistStatusUpdatedTimestamp** | **String** |  |  [optional] [readonly] |



