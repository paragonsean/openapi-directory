# MotaWordApi.ProjectUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callbackUrl** | **String** | Optional. If you provide a callback URL, we will send POST callbacks when the status of the current project is changed. Possible status changes are, &#39;translated&#39;, &#39;proofread&#39;, &#39;completed&#39;. | [optional] 
**couponCode** | **String** | Coupon code to redeem | [optional] 
**custom** | **[String]** | Optional. This is a consistent custom data parameter that will be given to you in the response across every request of this project model. Values should be provided like this, custom[my_key] &#x3D; my_value. If you previously provided one, it will be replaced. | [optional] 
**sourceLanguage** | **String** |  | [optional] 
**targetLanguages** | **[String]** |  | [optional] 


