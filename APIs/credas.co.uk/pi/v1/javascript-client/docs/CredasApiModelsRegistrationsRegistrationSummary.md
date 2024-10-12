# CredasApi.CredasApiModelsRegistrationsRegistrationSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**[CredasApiModelsRegistrationsRegistrationComment]**](CredasApiModelsRegistrationsRegistrationComment.md) |  | [optional] 
**createdByAgencyUserEmail** | **String** |  | [optional] 
**dITFDate** | **Date** |  | [optional] 
**dITFStatus** | **Number** | No &#x3D; 0, Yes &#x3D; 1, Pending &#x3D; 2 | [optional] 
**isExpired** | **Boolean** |  | [optional] 
**verifiedInAppDate** | **Date** |  | [optional] 
**bankAccountChecks** | [**[CredasApiModelsBankAccountsAccountVerificationResponse]**](CredasApiModelsBankAccountsAccountVerificationResponse.md) |  | [optional] 
**createdByAgencyUserId** | **String** |  | [optional] 
**creditStatusCheck** | [**CredasApiModelsStatusChecksStatusCheck**](CredasApiModelsStatusChecksStatusCheck.md) |  | [optional] 
**customTermsAccepted** | **Boolean** |  | [optional] 
**customTermsAcceptedDateTime** | **Date** |  | [optional] 
**customTermsAcceptedVersion** | **Number** |  | [optional] 
**dataCheckResult** | **Number** | Unknown &#x3D; 0, Pass &#x3D; 1, Refer &#x3D; 2, Fail &#x3D; 3 | 
**dataCheckSources** | [**[CredasApiModelsRegistrationsDataCheckSourceSummary]**](CredasApiModelsRegistrationsDataCheckSourceSummary.md) |  | [optional] 
**dataChecksPerformed** | **Boolean** |  | 
**dateCompleted** | **Date** |  | [optional] 
**dateCreated** | **Date** |  | 
**email** | **String** |  | [optional] 
**forename** | **String** |  | 
**hasLivenessPerformed** | **Boolean** |  | [optional] 
**hasSelfie** | **Boolean** |  | [optional] 
**id** | **String** |  | 
**idDocuments** | [**[CredasApiModelsRegistrationsIdDocumentSummary]**](CredasApiModelsRegistrationsIdDocumentSummary.md) |  | [optional] 
**idVerification** | [**CredasApiModelsRegistrationsIdVerification**](CredasApiModelsRegistrationsIdVerification.md) |  | [optional] 
**isAgentLed** | **Boolean** |  | [optional] 
**livenessMethod** | **Number** | NotApplicable &#x3D; 0, UniqueActionProcess &#x3D; 1, Passive &#x3D; 2 | [optional] 
**livenessStatus** | **Number** | NotSubmitted &#x3D; 0, Verified &#x3D; 1, Unverified &#x3D; 2, Unknown &#x3D; 3, RetakeRequested &#x3D; 4 | 
**livenessVerified** | **Boolean** |  | 
**middleName** | **String** |  | [optional] 
**personalDetails** | [**CredasApiModelsRegistrationsPersonalDetails**](CredasApiModelsRegistrationsPersonalDetails.md) |  | [optional] 
**phoneNumber** | **String** |  | [optional] 
**proofOfOwnershipCheck** | [**CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse**](CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse.md) |  | [optional] 
**referenceId** | **String** |  | [optional] 
**regCode** | **String** |  | 
**regTypeId** | **String** |  | 
**rightToRentCheck** | [**CredasApiModelsRegistrationsSettlementStatus**](CredasApiModelsRegistrationsSettlementStatus.md) |  | [optional] 
**rightToWorkCheck** | [**CredasApiModelsRegistrationsSettlementStatus**](CredasApiModelsRegistrationsSettlementStatus.md) |  | [optional] 
**rightToWorkDocumentsProvided** | **Number** | This property is no longer supported. Right to work is now available as an individual check.&lt;br /&gt;  values&#x3D;&gt; Pending &#x3D; 0, Pass &#x3D; 1, Fail &#x3D; 2 | 
**safeHarbourVerifiedDate** | **Date** |  | [optional] 
**safeHarbourVerifiedStatus** | **Number** | No &#x3D; 0, Yes &#x3D; 1, UnderReview &#x3D; 2 | [optional] 
**status** | **Number** | Unknown &#x3D; 0, Submitted &#x3D; 1, Approved &#x3D; 2, Rejected &#x3D; 3, Exported &#x3D; 4, Invited &#x3D; 6 | 
**surname** | **String** |  | 



## Enum: DITFStatusEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)





## Enum: DataCheckResultEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)





## Enum: LivenessMethodEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)





## Enum: LivenessStatusEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)





## Enum: RightToWorkDocumentsProvidedEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)





## Enum: SafeHarbourVerifiedStatusEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)





## Enum: StatusEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `6` (value: `6`)




