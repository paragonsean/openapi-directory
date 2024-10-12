# WebSiteManagementClient.RampUpRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionHostName** | **String** | Hostname of a slot to which the traffic will be redirected if decided to. E.g. mysite-stage.azurewebsites.net | [optional] 
**changeDecisionCallbackUrl** | **String** | Custom decision algorithm can be provided in TiPCallback site extension which Url can be specified. See TiPCallback site extension for the scaffold and contracts.              https://www.siteextensions.net/packages/TiPCallback/ | [optional] 
**changeIntervalInMinutes** | **Number** | [Optional] Specifies interval in minutes to reevaluate ReroutePercentage | [optional] 
**changeStep** | **Number** | [Optional] In auto ramp up scenario this is the step to add/remove from {Microsoft.Web.Hosting.Administration.RampUpRule.ReroutePercentage} until it reaches               {Microsoft.Web.Hosting.Administration.RampUpRule.MinReroutePercentage} or {Microsoft.Web.Hosting.Administration.RampUpRule.MaxReroutePercentage}. Site metrics are checked every N minutes specified in {Microsoft.Web.Hosting.Administration.RampUpRule.ChangeIntervalInMinutes}.              Custom decision algorithm can be provided in TiPCallback site extension which Url can be specified in {Microsoft.Web.Hosting.Administration.RampUpRule.ChangeDecisionCallbackUrl} | [optional] 
**maxReroutePercentage** | **Number** | [Optional] Specifies upper boundary below which ReroutePercentage will stay. | [optional] 
**minReroutePercentage** | **Number** | [Optional] Specifies lower boundary above which ReroutePercentage will stay. | [optional] 
**name** | **String** | Name of the routing rule. The recommended name would be to point to the slot which will receive the traffic in the experiment. | [optional] 
**reroutePercentage** | **Number** | Percentage of the traffic which will be redirected to {Microsoft.Web.Hosting.Administration.RampUpRule.ActionHostName} | [optional] 


