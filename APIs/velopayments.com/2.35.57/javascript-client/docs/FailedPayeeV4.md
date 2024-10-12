# VeloPaymentsApis.FailedPayeeV4

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**CreatePayeeAddressV4**](CreatePayeeAddressV4.md) |  | [optional] 
**challenge** | [**ChallengeV4**](ChallengeV4.md) |  | [optional] 
**company** | [**CompanyV4**](CompanyV4.md) |  | [optional] 
**email** | **String** |  | [optional] 
**individual** | [**CreateIndividualV4**](CreateIndividualV4.md) |  | [optional] 
**language** | **String** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**payeeId** | **String** |  | [optional] [readonly] 
**paymentChannel** | [**CreatePaymentChannelV4**](CreatePaymentChannelV4.md) |  | [optional] 
**payorRefs** | [**[PayeePayorRefV4]**](PayeePayorRefV4.md) |  | [optional] [readonly] 
**remoteId** | **String** |  | [optional] 
**type** | **String** | Type of Payee. One of the following values: Individual, Company | [optional] 


