# MotaWordApi.NewProject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callbackUrl** | **String** | Optional. If you provide a callback URL, we will send POST callbacks when the status of the current project is changed. Possible status changes are, &#39;translated&#39;, &#39;proofread&#39;, &#39;completed&#39;. | [optional] 
**couponCode** | **String** | Coupon code to redeem | [optional] 
**custom** | **[String]** | Optional. This is a consistent custom data parameter that will be given to you in the response across every request of this project model. Values should be provided like this, custom[my_key] &#x3D; my_value. | [optional] 
**documents** | **File** | Optional. You can add as many files as you want in documents[] parameter. Or you add your documents later in separate calls. | [optional] 
**glossaries** | **File** | Optional. Only one glossary is supported at the moment. | [optional] 
**sourceLanguage** | **String** |  | [optional] 
**styleguides** | **File** | Optional. You can add as many files as you want in styleguides[] parameter. Or you add your style guides later in separate calls. | [optional] 
**targetLanguages** | **[String]** |  | [optional] 


