# AwsSavingsPlans.CreateSavingsPlanRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**savingsPlanOfferingId** | **String** | The ID of the offering. | 
**commitment** | **String** | The hourly commitment, in USD. This is a value between 0.001 and 1 million. You cannot specify more than five digits after the decimal point. | 
**upfrontPaymentAmount** | **String** | The up-front payment amount. This is a whole number between 50 and 99 percent of the total value of the Savings Plan. This parameter is supported only if the payment option is &lt;code&gt;Partial Upfront&lt;/code&gt;. | [optional] 
**purchaseTime** | **Date** | The time at which to purchase the Savings Plan, in UTC format (YYYY-MM-DDTHH:MM:SSZ). | [optional] 
**clientToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. | [optional] 
**tags** | **{String: String}** | One or more tags. | [optional] 


