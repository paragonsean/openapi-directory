# IncreaseApi.InboundWireReversal1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The amount that was reversed. | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the reversal was created. | 
**description** | **String** | The description on the reversal message from Fedwire. | 
**financialInstitutionToFinancialInstitutionInformation** | **String** | Additional financial institution information included in the wire reversal. | 
**inputCycleDate** | **Date** | The Fedwire cycle date for the wire reversal. | 
**inputMessageAccountabilityData** | **String** | The Fedwire transaction identifier. | 
**inputSequenceNumber** | **String** | The Fedwire sequence number. | 
**inputSource** | **String** | The Fedwire input source identifier. | 
**previousMessageInputCycleDate** | **Date** | The Fedwire cycle date for the wire transfer that was reversed. | 
**previousMessageInputMessageAccountabilityData** | **String** | The Fedwire transaction identifier for the wire transfer that was reversed. | 
**previousMessageInputSequenceNumber** | **String** | The Fedwire sequence number for the wire transfer that was reversed. | 
**previousMessageInputSource** | **String** | The Fedwire input source identifier for the wire transfer that was reversed. | 
**receiverFinancialInstitutionInformation** | **String** | Information included in the wire reversal for the receiving financial institution. | 
**transactionId** | **String** | The ID for the Transaction associated with the transfer reversal. | 


