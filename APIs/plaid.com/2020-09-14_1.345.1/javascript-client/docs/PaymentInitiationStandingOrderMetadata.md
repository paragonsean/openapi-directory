# ThePlaidApi.PaymentInitiationStandingOrderMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supportsStandingOrderEndDate** | **Boolean** | Indicates whether the institution supports closed-ended standing orders by providing an end date. | 
**supportsStandingOrderNegativeExecutionDays** | **Boolean** | This is only applicable to &#x60;MONTHLY&#x60; standing orders. Indicates whether the institution supports negative integers (-1 to -5) for setting up a &#x60;MONTHLY&#x60; standing order relative to the end of the month. | 
**validStandingOrderIntervals** | [**[PaymentScheduleInterval]**](PaymentScheduleInterval.md) | A list of the valid standing order intervals supported by the institution. | 


