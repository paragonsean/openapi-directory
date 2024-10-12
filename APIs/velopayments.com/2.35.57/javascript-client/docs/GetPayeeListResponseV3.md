# VeloPaymentsApis.GetPayeeListResponseV3

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | [**GetPayeeListResponseCompanyV3**](GetPayeeListResponseCompanyV3.md) |  | [optional] 
**country** | **String** | Valid ISO 3166 2 character country code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. | [optional] 
**created** | **Date** |  | [optional] 
**disabled** | **Boolean** |  | [optional] 
**disabledComment** | **String** |  | [optional] 
**disabledUpdatedTimestamp** | **Date** |  | [optional] 
**displayName** | **String** |  | [optional] 
**email** | **String** |  | [optional] 
**individual** | [**GetPayeeListResponseIndividualV3**](GetPayeeListResponseIndividualV3.md) |  | [optional] 
**language** | **String** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**onboardedStatus** | **String** | Onboarded status. One of the following values: CREATED, INVITED, REGISTERED, ONBOARDED | [optional] 
**payeeId** | **String** |  | [optional] [readonly] 
**payeeType** | **String** | Type of Payee. One of the following values: Individual, Company | [optional] 
**payorRefs** | [**[PayeePayorRefV3]**](PayeePayorRefV3.md) |  | [optional] [readonly] 
**watchlistOverrideComment** | **String** |  | [optional] 
**watchlistStatus** | **String** | Current watchlist status. One of the following values: NONE, PENDING, REVIEW, PASSED, FAILED | [optional] 
**watchlistStatusUpdatedTimestamp** | **String** |  | [optional] [readonly] 


