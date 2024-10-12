# Taxamo.Refunds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | Amount, excluding tax, that was refunded. | [optional] 
**informative** | **Boolean** | Was this refund applied to an informative line? | [optional] 
**lineKey** | **String** | Line identifier. If neither line key or custom id is provided, the refund amount will be assigned to lines in order. | [optional] 
**refundNoteNumber** | **String** | Sequential refund note number. | [optional] 
**refundNoteUrl** | **String** | Refund note image url. | [optional] 
**refundReason** | **String** | Refund reason, displayed on the credit note. | [optional] 
**refundTimestamp** | **String** | Refund timestamp in UTC timezone. | [optional] 
**taxAmount** | **Number** | Calculated tax amount, that was refunded. | [optional] 
**taxRate** | **Number** | Tax rate for the line that was used for the refund calculation. | [optional] 
**totalAmount** | **Number** | Total amount, including tax, that was refunded. | [optional] 


