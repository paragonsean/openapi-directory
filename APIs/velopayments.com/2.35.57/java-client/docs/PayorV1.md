

# PayorV1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**PayorAddress**](PayorAddress.md) |  |  [optional] |
|**allowsLanguageChoice** | **Boolean** | Whether or not the payor allows language choice in the UI. |  [optional] |
|**collectiveAlias** | **String** | How the payor has chosen to refer to payees. |  [optional] |
|**dbaName** | **String** | The payor’s &#39;Doing Business As&#39; name. |  [optional] |
|**fundingAccountAccountName** | **String** | The funding account name to be used for the payor. |  [optional] |
|**fundingAccountAccountNumber** | **String** | The funding account number to be used for the payor. |  [optional] |
|**fundingAccountRoutingNumber** | **String** | The funding account routing number to be used for the payor. |  [optional] |
|**includesReports** | **Boolean** |  |  [optional] |
|**kycState** | **String** | The kyc state of the payor. One of the following values: FAILED_KYC, PASSED_KYC, REQUIRES_KYC |  [optional] [readonly] |
|**language** | **String** | The payor’s language preference. Must be one of [EN, FR]. |  [optional] |
|**manualLockout** | **Boolean** | Whether or not the payor has been manually locked by the backoffice. |  [optional] |
|**maxMasterPayorAdmins** | **Integer** |  |  [optional] |
|**payeeGracePeriodDays** | **Integer** | The grace period for paying payees in days. |  [optional] [readonly] |
|**payeeGracePeriodProcessingEnabled** | **Boolean** | Whether grace period processing is enabled. |  [optional] [readonly] |
|**payorId** | **UUID** |  |  [optional] [readonly] |
|**payorName** | **String** | The name of the payor. |  |
|**primaryContactEmail** | **String** | Primary contact email for the payor. |  [optional] |
|**primaryContactName** | **String** | Name of primary contact for the payor. |  [optional] |
|**primaryContactPhone** | **String** | Primary contact phone number for the payor. |  [optional] |
|**reminderEmailsOptOut** | **Boolean** | Whether or not the payor has opted-out of reminder emails being sent. |  [optional] [readonly] |
|**supportContact** | **String** | The payor’s support contact email address. |  [optional] |
|**transmissionTypes** | [**TransmissionTypes**](TransmissionTypes.md) |  |  [optional] |



