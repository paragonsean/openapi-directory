

# CredasApiModelsRegistrationsRegistrationSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comments** | [**List&lt;CredasApiModelsRegistrationsRegistrationComment&gt;**](CredasApiModelsRegistrationsRegistrationComment.md) |  |  [optional] |
|**createdByAgencyUserEmail** | **String** |  |  [optional] |
|**diTFDate** | **OffsetDateTime** |  |  [optional] |
|**diTFStatus** | [**DiTFStatusEnum**](#DiTFStatusEnum) | No &#x3D; 0, Yes &#x3D; 1, Pending &#x3D; 2 |  [optional] |
|**isExpired** | **Boolean** |  |  [optional] |
|**verifiedInAppDate** | **OffsetDateTime** |  |  [optional] |
|**bankAccountChecks** | [**List&lt;CredasApiModelsBankAccountsAccountVerificationResponse&gt;**](CredasApiModelsBankAccountsAccountVerificationResponse.md) |  |  [optional] |
|**createdByAgencyUserId** | **UUID** |  |  [optional] |
|**creditStatusCheck** | [**CredasApiModelsStatusChecksStatusCheck**](CredasApiModelsStatusChecksStatusCheck.md) |  |  [optional] |
|**customTermsAccepted** | **Boolean** |  |  [optional] |
|**customTermsAcceptedDateTime** | **OffsetDateTime** |  |  [optional] |
|**customTermsAcceptedVersion** | **Integer** |  |  [optional] |
|**dataCheckResult** | [**DataCheckResultEnum**](#DataCheckResultEnum) | Unknown &#x3D; 0, Pass &#x3D; 1, Refer &#x3D; 2, Fail &#x3D; 3 |  |
|**dataCheckSources** | [**List&lt;CredasApiModelsRegistrationsDataCheckSourceSummary&gt;**](CredasApiModelsRegistrationsDataCheckSourceSummary.md) |  |  [optional] |
|**dataChecksPerformed** | **Boolean** |  |  |
|**dateCompleted** | **OffsetDateTime** |  |  [optional] |
|**dateCreated** | **OffsetDateTime** |  |  |
|**email** | **String** |  |  [optional] |
|**forename** | **String** |  |  |
|**hasLivenessPerformed** | **Boolean** |  |  [optional] |
|**hasSelfie** | **Boolean** |  |  [optional] |
|**id** | **UUID** |  |  |
|**idDocuments** | [**List&lt;CredasApiModelsRegistrationsIdDocumentSummary&gt;**](CredasApiModelsRegistrationsIdDocumentSummary.md) |  |  [optional] |
|**idVerification** | [**CredasApiModelsRegistrationsIdVerification**](CredasApiModelsRegistrationsIdVerification.md) |  |  [optional] |
|**isAgentLed** | **Boolean** |  |  [optional] |
|**livenessMethod** | [**LivenessMethodEnum**](#LivenessMethodEnum) | NotApplicable &#x3D; 0, UniqueActionProcess &#x3D; 1, Passive &#x3D; 2 |  [optional] |
|**livenessStatus** | [**LivenessStatusEnum**](#LivenessStatusEnum) | NotSubmitted &#x3D; 0, Verified &#x3D; 1, Unverified &#x3D; 2, Unknown &#x3D; 3, RetakeRequested &#x3D; 4 |  |
|**livenessVerified** | **Boolean** |  |  |
|**middleName** | **String** |  |  [optional] |
|**personalDetails** | [**CredasApiModelsRegistrationsPersonalDetails**](CredasApiModelsRegistrationsPersonalDetails.md) |  |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**proofOfOwnershipCheck** | [**CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse**](CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse.md) |  |  [optional] |
|**referenceId** | **String** |  |  [optional] |
|**regCode** | **String** |  |  |
|**regTypeId** | **UUID** |  |  |
|**rightToRentCheck** | [**CredasApiModelsRegistrationsSettlementStatus**](CredasApiModelsRegistrationsSettlementStatus.md) |  |  [optional] |
|**rightToWorkCheck** | [**CredasApiModelsRegistrationsSettlementStatus**](CredasApiModelsRegistrationsSettlementStatus.md) |  |  [optional] |
|**rightToWorkDocumentsProvided** | [**RightToWorkDocumentsProvidedEnum**](#RightToWorkDocumentsProvidedEnum) | This property is no longer supported. Right to work is now available as an individual check.&lt;br /&gt;  values&#x3D;&gt; Pending &#x3D; 0, Pass &#x3D; 1, Fail &#x3D; 2 |  |
|**safeHarbourVerifiedDate** | **OffsetDateTime** |  |  [optional] |
|**safeHarbourVerifiedStatus** | [**SafeHarbourVerifiedStatusEnum**](#SafeHarbourVerifiedStatusEnum) | No &#x3D; 0, Yes &#x3D; 1, UnderReview &#x3D; 2 |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Unknown &#x3D; 0, Submitted &#x3D; 1, Approved &#x3D; 2, Rejected &#x3D; 3, Exported &#x3D; 4, Invited &#x3D; 6 |  |
|**surname** | **String** |  |  |



## Enum: DiTFStatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



## Enum: DataCheckResultEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |



## Enum: LivenessMethodEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



## Enum: LivenessStatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |



## Enum: RightToWorkDocumentsProvidedEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



## Enum: SafeHarbourVerifiedStatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_6 | 6 |



