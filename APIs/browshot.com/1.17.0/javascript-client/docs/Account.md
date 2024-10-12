# BrowshotApi.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **Number** | number of credits left on your account | 
**browsers** | [**[Browser]**](Browser.md) | list of custom browsers as returned by /api/v1/browser/list | [optional] 
**freeScreenshotsLeft** | **Number** | number of free screenshots available for the current month | 
**hostingBrowshot** | **Number** | 1 is your account is authorized to request hosting on Browshot, 0 otherwise (default) | 
**instances** | [**[Instance]**](Instance.md) | list of private instances as returned by /api/v1/instance/list | [optional] 
**privateInstances** | **Number** | 1 is your account is authorized to create and use private instances, 0 otherwise (default) | 
**screenshots** | [**[Screenshot]**](Screenshot.md) | list of 10 latest screenshots requests as returned by /api/v1/screenshot/list | [optional] 


