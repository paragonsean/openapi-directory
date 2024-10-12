# AccountApi.PaymentsProgramOnboardingSteps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the step in the steps array. Over time, these names are subject to change as processes change. The output sample contains example step names. Review an actual call response for updated step names.  | [optional] 
**status** | **String** | This enumeration value indicates the status of the associated step. &lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; Only one step can be &lt;code&gt;IN_PROGRESS&lt;/code&gt; at a time.&lt;/span&gt;&lt;/p&gt; For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/account/types/api:PaymentsProgramOnboardingStepStatus&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**webUrl** | **String** | This URL provides access to the &lt;code&gt;IN_PROGRESS&lt;/code&gt; step. | [optional] 


