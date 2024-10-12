# GoogleWorkspaceResellerApi.ChangePlanRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dealCode** | **String** | Google-issued code (100 char max) for discounted pricing on subscription plans. Deal code must be included in &#x60;changePlan&#x60; request in order to receive discounted rate. This property is optional. If a deal code has already been added to a subscription, this property may be left empty and the existing discounted rate will still apply (if not empty, only provide the deal code that is already present on the subscription). If a deal code has never been added to a subscription and this property is left blank, regular pricing will apply. | [optional] 
**kind** | **String** | Identifies the resource as a subscription change plan request. Value: &#x60;subscriptions#changePlanRequest&#x60; | [optional] [default to &#39;subscriptions#changePlanRequest&#39;]
**planName** | **String** | The &#x60;planName&#x60; property is required. This is the name of the subscription&#39;s payment plan. For more information about the Google payment plans, see API concepts. Possible values are: - &#x60;ANNUAL_MONTHLY_PAY&#x60; - The annual commitment plan with monthly payments *Caution: *&#x60;ANNUAL_MONTHLY_PAY&#x60; is returned as &#x60;ANNUAL&#x60; in all API responses. - &#x60;ANNUAL_YEARLY_PAY&#x60; - The annual commitment plan with yearly payments - &#x60;FLEXIBLE&#x60; - The flexible plan - &#x60;TRIAL&#x60; - The 30-day free trial plan  | [optional] 
**purchaseOrderId** | **String** | This is an optional property. This purchase order (PO) information is for resellers to use for their company tracking usage. If a &#x60;purchaseOrderId&#x60; value is given it appears in the API responses and shows up in the invoice. The property accepts up to 80 plain text characters. | [optional] 
**seats** | [**Seats**](Seats.md) |  | [optional] 


