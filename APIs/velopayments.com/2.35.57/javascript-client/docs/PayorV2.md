# VeloPaymentsApis.PayorV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**PayorAddressV2**](PayorAddressV2.md) |  | [optional] 
**allowsLanguageChoice** | **Boolean** | Whether or not the payor allows language choice in the UI. | [optional] 
**collectiveAlias** | **String** | How the payor has chosen to refer to payees. | [optional] 
**dbaName** | **String** | The payor’s &#39;Doing Business As&#39; name. | [optional] 
**includesReports** | **Boolean** |  | [optional] 
**kycState** | **String** | The kyc state of the payor. One of the following values: FAILED_KYC, PASSED_KYC, REQUIRES_KYC | [optional] [readonly] 
**language** | **String** | The payor’s language preference. Must be one of [EN, FR] | [optional] 
**managingPayees** | **Boolean** |  | [optional] 
**manualLockout** | **Boolean** | Whether or not the payor has been manually locked by the backoffice. | [optional] 
**maxMasterPayorAdmins** | **Number** |  | [optional] 
**openBankingEnabled** | **Boolean** | Is Open Banking supported for this payor | [optional] 
**payeeGracePeriodDays** | **Number** | The grace period for paying payees in days. | [optional] [readonly] 
**payeeGracePeriodProcessingEnabled** | **Boolean** | Whether grace period processing is enabled. | [optional] [readonly] 
**paymentRails** | **String** | The id of the payment rails | [optional] 
**payorId** | **String** |  | [readonly] 
**payorName** | **String** | The name of the payor. | 
**payorXid** | **String** | A unique identifier that an external system uses to reference the payor in their system | [optional] 
**primaryContactEmail** | **String** | Primary contact email for the payor. | [optional] 
**primaryContactName** | **String** | Name of primary contact for the payor. | [optional] 
**primaryContactPhone** | **String** | Primary contact phone number for the payor. | [optional] 
**provider** | **String** | The source of the payorXid, default is null which means Velo | [optional] 
**reminderEmailsOptOut** | **Boolean** | Whether or not the payor has opted-out of reminder emails being sent. | [optional] [readonly] 
**remoteSystemIds** | **[String]** | The payor’s supported remote systems by id | [optional] 
**supportContact** | **String** | The payor’s support contact email address. | [optional] 
**transmissionTypes** | [**TransmissionTypes2**](TransmissionTypes2.md) |  | [optional] 
**usdTxnValueReportingThreshold** | **Number** | USD in minor units | [optional] 
**wuCustomerId** | **String** |  | [optional] 


