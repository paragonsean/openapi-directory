# LogicManagementClient.X12EnvelopeSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controlStandardsId** | **Number** | The controls standards id. | 
**controlVersionNumber** | **String** | The control version number. | 
**enableDefaultGroupHeaders** | **Boolean** | The value indicating whether to enable default group headers. | 
**functionalGroupId** | **String** | The functional group id. | [optional] 
**groupControlNumberLowerBound** | **Number** | The group control number lower bound. | 
**groupControlNumberUpperBound** | **Number** | The group control number upper bound. | 
**groupHeaderAgencyCode** | **String** | The group header agency code. | 
**groupHeaderDateFormat** | [**X12DateFormat**](X12DateFormat.md) |  | 
**groupHeaderTimeFormat** | [**X12TimeFormat**](X12TimeFormat.md) |  | 
**groupHeaderVersion** | **String** | The group header version. | 
**interchangeControlNumberLowerBound** | **Number** | The interchange  control number lower bound. | 
**interchangeControlNumberUpperBound** | **Number** | The interchange  control number upper bound. | 
**overwriteExistingTransactionSetControlNumber** | **Boolean** | The value indicating whether to overwrite existing transaction set control number. | 
**receiverApplicationId** | **String** | The receiver application id. | 
**rolloverGroupControlNumber** | **Boolean** | The value indicating whether to rollover group control number. | 
**rolloverInterchangeControlNumber** | **Boolean** | The value indicating whether to rollover interchange control number. | 
**rolloverTransactionSetControlNumber** | **Boolean** | The value indicating whether to rollover transaction set control number. | 
**senderApplicationId** | **String** | The sender application id. | 
**transactionSetControlNumberLowerBound** | **Number** | The transaction set control number lower bound. | 
**transactionSetControlNumberPrefix** | **String** | The transaction set control number prefix. | [optional] 
**transactionSetControlNumberSuffix** | **String** | The transaction set control number suffix. | [optional] 
**transactionSetControlNumberUpperBound** | **Number** | The transaction set control number upper bound. | 
**usageIndicator** | [**UsageIndicator**](UsageIndicator.md) |  | 
**useControlStandardsIdAsRepetitionCharacter** | **Boolean** | The value indicating whether to use control standards id as repetition character. | 


