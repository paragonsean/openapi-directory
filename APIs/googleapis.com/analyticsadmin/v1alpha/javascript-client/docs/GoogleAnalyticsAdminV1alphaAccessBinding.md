# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaAccessBinding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Output only. Resource name of this binding. Format: accounts/{account}/accessBindings/{access_binding} or properties/{property}/accessBindings/{access_binding} Example: \&quot;accounts/100/accessBindings/200\&quot; | [optional] [readonly] 
**roles** | **[String]** | A list of roles for to grant to the parent resource. Valid values: predefinedRoles/viewer predefinedRoles/analyst predefinedRoles/editor predefinedRoles/admin predefinedRoles/no-cost-data predefinedRoles/no-revenue-data For users, if an empty list of roles is set, this AccessBinding will be deleted. | [optional] 
**user** | **String** | If set, the email address of the user to set roles for. Format: \&quot;someuser@gmail.com\&quot; | [optional] 


