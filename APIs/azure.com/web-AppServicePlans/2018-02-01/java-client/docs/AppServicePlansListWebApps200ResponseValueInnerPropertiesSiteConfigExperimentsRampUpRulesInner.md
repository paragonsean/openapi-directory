

# AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner

Routing rules for ramp up testing. This rule allows to redirect static traffic % to a slot or to gradually change routing % based on performance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionHostName** | **String** | Hostname of a slot to which the traffic will be redirected if decided to. E.g. myapp-stage.azurewebsites.net. |  [optional] |
|**changeDecisionCallbackUrl** | **String** | Custom decision algorithm can be provided in TiPCallback site extension which URL can be specified. See TiPCallback site extension for the scaffold and contracts. https://www.siteextensions.net/packages/TiPCallback/ |  [optional] |
|**changeIntervalInMinutes** | **Integer** | Specifies interval in minutes to reevaluate ReroutePercentage. |  [optional] |
|**changeStep** | **Double** | In auto ramp up scenario this is the step to add/remove from &lt;code&gt;ReroutePercentage&lt;/code&gt; until it reaches  &lt;code&gt;MinReroutePercentage&lt;/code&gt; or &lt;code&gt;MaxReroutePercentage&lt;/code&gt;. Site metrics are checked every N minutes specified in &lt;code&gt;ChangeIntervalInMinutes&lt;/code&gt;. Custom decision algorithm can be provided in TiPCallback site extension which URL can be specified in &lt;code&gt;ChangeDecisionCallbackUrl&lt;/code&gt;. |  [optional] |
|**maxReroutePercentage** | **Double** | Specifies upper boundary below which ReroutePercentage will stay. |  [optional] |
|**minReroutePercentage** | **Double** | Specifies lower boundary above which ReroutePercentage will stay. |  [optional] |
|**name** | **String** | Name of the routing rule. The recommended name would be to point to the slot which will receive the traffic in the experiment. |  [optional] |
|**reroutePercentage** | **Double** | Percentage of the traffic which will be redirected to &lt;code&gt;ActionHostName&lt;/code&gt;. |  [optional] |



