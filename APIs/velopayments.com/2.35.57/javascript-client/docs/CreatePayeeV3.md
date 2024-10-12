# VeloPaymentsApis.CreatePayeeV3

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**CreatePayeeAddressV3**](CreatePayeeAddressV3.md) |  | 
**challenge** | [**ChallengeV3**](ChallengeV3.md) |  | [optional] 
**company** | [**CompanyV3**](CompanyV3.md) |  | [optional] 
**email** | **String** |  | 
**individual** | [**CreateIndividualV3**](CreateIndividualV3.md) |  | [optional] 
**language** | **String** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**payeeId** | **String** |  | [optional] [readonly] 
**paymentChannel** | [**CreatePaymentChannelV3**](CreatePaymentChannelV3.md) |  | [optional] 
**payorRefs** | [**[PayeePayorRefV3]**](PayeePayorRefV3.md) |  | [optional] [readonly] 
**remoteId** | **String** |  | 
**type** | **String** | Type of Payee. One of the following values: Individual, Company | 


