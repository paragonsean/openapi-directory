# WebSiteManagementClient.CloningInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appSettingsOverrides** | **{String: String}** | Application settings overrides for cloned web app. If specified these settings will override the settings cloned               from source web app. If not specified, application settings from source web app are retained. | [optional] 
**cloneCustomHostNames** | **Boolean** | If true, clone custom hostnames from source web app | [optional] 
**cloneSourceControl** | **Boolean** | Clone source control from source web app | [optional] 
**configureLoadBalancing** | **Boolean** | If specified configure load balancing for source and clone site | [optional] 
**correlationId** | **String** | Correlation Id of cloning operation. This id ties multiple cloning operations              together to use the same snapshot | [optional] 
**hostingEnvironment** | **String** | Hosting environment | [optional] 
**overwrite** | **Boolean** | Overwrite destination web app | [optional] 
**sourceWebAppId** | **String** | ARM resource id of the source web app. Web app resource id is of the form               /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName} for production slots and               /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slotName} for other slots | [optional] 
**trafficManagerProfileId** | **String** | ARM resource id of the traffic manager profile to use if it exists. Traffic manager resource id is of the form               /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{profileName} | [optional] 
**trafficManagerProfileName** | **String** | Name of traffic manager profile to create. This is only needed if traffic manager profile does not already exist | [optional] 


