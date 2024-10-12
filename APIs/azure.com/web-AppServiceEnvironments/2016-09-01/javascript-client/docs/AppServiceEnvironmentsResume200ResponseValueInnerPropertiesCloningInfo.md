# AppServiceEnvironmentsApiClient.AppServiceEnvironmentsResume200ResponseValueInnerPropertiesCloningInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appSettingsOverrides** | **{String: String}** | Application setting overrides for cloned app. If specified, these settings override the settings cloned  from source app. Otherwise, application settings from source app are retained. | [optional] 
**cloneCustomHostNames** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to clone custom hostnames from source app; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**cloneSourceControl** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to clone source control from source app; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**configureLoadBalancing** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to configure load balancing for source and destination app. | [optional] 
**correlationId** | **String** | Correlation ID of cloning operation. This ID ties multiple cloning operations together to use the same snapshot. | [optional] 
**hostingEnvironment** | **String** | App Service Environment. | [optional] 
**ignoreQuotas** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if quotas should be ignored; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**overwrite** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to overwrite destination app; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**sourceWebAppId** | **String** | ARM resource ID of the source app. App resource ID is of the form  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName} for production slots and  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slotName} for other slots. | 
**trafficManagerProfileId** | **String** | ARM resource ID of the Traffic Manager profile to use, if it exists. Traffic Manager resource ID is of the form  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{profileName}. | [optional] 
**trafficManagerProfileName** | **String** | Name of Traffic Manager profile to create. This is only needed if Traffic Manager profile does not already exist. | [optional] 


