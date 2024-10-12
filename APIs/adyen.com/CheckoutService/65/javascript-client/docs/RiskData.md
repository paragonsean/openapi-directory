# AdyenCheckoutApi.RiskData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientData** | **String** | Contains client-side data, like the device fingerprint, cookies, and specific browser settings. | [optional] 
**customFields** | **{String: String}** | Any custom fields used as part of the input to configured risk rules. | [optional] 
**fraudOffset** | **Number** | An integer value that is added to the normal fraud score. The value can be either positive or negative. | [optional] 
**profileReference** | **String** | The risk profile to assign to this payment. When left empty, the merchant-level account&#39;s default risk profile will be applied. | [optional] 


