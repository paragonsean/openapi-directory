# SqlManagementClient.AdvisorProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisorStatus** | **String** | Gets the status of availability of this advisor to customers. Possible values are &#39;GA&#39;, &#39;PublicPreview&#39;, &#39;LimitedPublicPreview&#39; and &#39;PrivatePreview&#39;. | [optional] [readonly] 
**autoExecuteValue** | **String** | Gets the auto-execute status (whether to let the system execute the recommendations) of this advisor. Possible values are &#39;Enabled&#39; and &#39;Disabled&#39; | 
**lastChecked** | **Date** | Gets the time when the current resource was analyzed for recommendations by this advisor. | [optional] [readonly] 
**recommendationsStatus** | **String** | Gets that status of recommendations for this advisor and reason for not having any recommendations. Possible values include, but are not limited to, &#39;Ok&#39; (Recommendations available), LowActivity (not enough workload to analyze), &#39;DbSeemsTuned&#39; (Database is doing well), etc. | [optional] [readonly] 



## Enum: AdvisorStatusEnum


* `GA` (value: `"GA"`)

* `PublicPreview` (value: `"PublicPreview"`)

* `LimitedPublicPreview` (value: `"LimitedPublicPreview"`)

* `PrivatePreview` (value: `"PrivatePreview"`)





## Enum: AutoExecuteValueEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)

* `Default` (value: `"Default"`)




