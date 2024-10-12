# LogicAppsManagementClient.HostingEnvironmentServiceDescriptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostId** | **String** | Host Id | [optional] 
**hostingEnvironmentId** | **String** | Hosting environment Id | [optional] 
**serviceUrl** | **String** | service url to use | [optional] 
**useInternalRouting** | **Boolean** | When the backend url is in same ASE, for performance reason this flag can be set to true              If WebApp.DisableHostNames is also set it improves the security by making the back end accessible only               via API calls              Note: calls will fail if this option is used but back end is not on the same ASE | [optional] 


