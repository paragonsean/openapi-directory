

# Account


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**balance** | **Integer** | number of credits left on your account |  |
|**browsers** | [**List&lt;Browser&gt;**](Browser.md) | list of custom browsers as returned by /api/v1/browser/list |  [optional] |
|**freeScreenshotsLeft** | **Integer** | number of free screenshots available for the current month |  |
|**hostingBrowshot** | **Integer** | 1 is your account is authorized to request hosting on Browshot, 0 otherwise (default) |  |
|**instances** | [**List&lt;Instance&gt;**](Instance.md) | list of private instances as returned by /api/v1/instance/list |  [optional] |
|**privateInstances** | **Integer** | 1 is your account is authorized to create and use private instances, 0 otherwise (default) |  |
|**screenshots** | [**List&lt;Screenshot&gt;**](Screenshot.md) | list of 10 latest screenshots requests as returned by /api/v1/screenshot/list |  [optional] |



