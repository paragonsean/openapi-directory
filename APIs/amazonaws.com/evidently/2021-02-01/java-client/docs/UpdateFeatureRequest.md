

# UpdateFeatureRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addOrUpdateVariations** | [**List&lt;VariationConfig&gt;**](VariationConfig.md) | To update variation configurations for this feature, or add new ones, specify this structure. In this array, include any variations that you want to add or update. If the array includes a variation name that already exists for this feature, it is updated. If it includes a new variation name, it is added as a new variation. |  [optional] |
|**defaultVariation** | **String** | The name of the variation to use as the default variation. The default variation is served to users who are not allocated to any ongoing launches or experiments of this feature. |  [optional] |
|**description** | **String** | An optional description of the feature. |  [optional] |
|**entityOverrides** | **Map&lt;String, String&gt;** | &lt;p&gt;Specified users that should always be served a specific variation of a feature. Each user is specified by a key-value pair . For each key, specify a user by entering their user ID, account ID, or some other identifier. For the value, specify the name of the variation that they are to be served.&lt;/p&gt; &lt;p&gt;This parameter is limited to 2500 overrides or a total of 40KB. The 40KB limit includes an overhead of 6 bytes per override.&lt;/p&gt; |  [optional] |
|**evaluationStrategy** | [**EvaluationStrategyEnum**](#EvaluationStrategyEnum) | Specify &lt;code&gt;ALL_RULES&lt;/code&gt; to activate the traffic allocation specified by any ongoing launches or experiments. Specify &lt;code&gt;DEFAULT_VARIATION&lt;/code&gt; to serve the default variation to all users instead. |  [optional] |
|**removeVariations** | **List&lt;String&gt;** | &lt;p&gt;Removes a variation from the feature. If the variation you specify doesn&#39;t exist, then this makes no change and does not report an error.&lt;/p&gt; &lt;p&gt;This operation fails if you try to remove a variation that is part of an ongoing launch or experiment.&lt;/p&gt; |  [optional] |



## Enum: EvaluationStrategyEnum

| Name | Value |
|---- | -----|
| ALL_RULES | &quot;ALL_RULES&quot; |
| DEFAULT_VARIATION | &quot;DEFAULT_VARIATION&quot; |



