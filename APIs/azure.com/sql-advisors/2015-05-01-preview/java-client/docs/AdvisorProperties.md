

# AdvisorProperties

Properties for a Database, Server or Elastic Pool Advisor.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advisorStatus** | [**AdvisorStatusEnum**](#AdvisorStatusEnum) | Gets the status of availability of this advisor to customers. Possible values are &#39;GA&#39;, &#39;PublicPreview&#39;, &#39;LimitedPublicPreview&#39; and &#39;PrivatePreview&#39;. |  [optional] [readonly] |
|**autoExecuteStatus** | [**AutoExecuteStatusEnum**](#AutoExecuteStatusEnum) | Gets the auto-execute status (whether to let the system execute the recommendations) of this advisor. Possible values are &#39;Enabled&#39; and &#39;Disabled&#39; |  |
|**autoExecuteStatusInheritedFrom** | [**AutoExecuteStatusInheritedFromEnum**](#AutoExecuteStatusInheritedFromEnum) | Gets the resource from which current value of auto-execute status is inherited. Auto-execute status can be set on (and inherited from) different levels in the resource hierarchy. Possible values are &#39;Subscription&#39;, &#39;Server&#39;, &#39;ElasticPool&#39;, &#39;Database&#39; and &#39;Default&#39; (when status is not explicitly set on any level). |  [optional] [readonly] |
|**lastChecked** | **OffsetDateTime** | Gets the time when the current resource was analyzed for recommendations by this advisor. |  [optional] [readonly] |
|**recommendationsStatus** | **String** | Gets that status of recommendations for this advisor and reason for not having any recommendations. Possible values include, but are not limited to, &#39;Ok&#39; (Recommendations available),LowActivity (not enough workload to analyze), &#39;DbSeemsTuned&#39; (Database is doing well), etc. |  [optional] [readonly] |
|**recommendedActions** | [**List&lt;RecommendedAction&gt;**](RecommendedAction.md) | Gets the recommended actions for this advisor. |  [optional] [readonly] |



## Enum: AdvisorStatusEnum

| Name | Value |
|---- | -----|
| GA | &quot;GA&quot; |
| PUBLIC_PREVIEW | &quot;PublicPreview&quot; |
| LIMITED_PUBLIC_PREVIEW | &quot;LimitedPublicPreview&quot; |
| PRIVATE_PREVIEW | &quot;PrivatePreview&quot; |



## Enum: AutoExecuteStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |
| DEFAULT | &quot;Default&quot; |



## Enum: AutoExecuteStatusInheritedFromEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| SUBSCRIPTION | &quot;Subscription&quot; |
| SERVER | &quot;Server&quot; |
| ELASTIC_POOL | &quot;ElasticPool&quot; |
| DATABASE | &quot;Database&quot; |



