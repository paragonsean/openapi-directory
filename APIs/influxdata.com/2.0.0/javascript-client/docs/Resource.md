# InfluxOssApiService.Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | If ID is set that is a permission for a specific resource. if it is not set it is a permission for all resources of that resource type. | [optional] 
**name** | **String** | Optional name of the resource if the resource has a name field. | [optional] 
**org** | **String** | Optional name of the organization of the organization with orgID. | [optional] 
**orgID** | **String** | If orgID is set that is a permission for all resources owned my that org. if it is not set it is a permission for all resources of that resource type. | [optional] 
**type** | **String** |  | 



## Enum: TypeEnum


* `authorizations` (value: `"authorizations"`)

* `buckets` (value: `"buckets"`)

* `dashboards` (value: `"dashboards"`)

* `orgs` (value: `"orgs"`)

* `sources` (value: `"sources"`)

* `tasks` (value: `"tasks"`)

* `telegrafs` (value: `"telegrafs"`)

* `users` (value: `"users"`)

* `variables` (value: `"variables"`)

* `scrapers` (value: `"scrapers"`)

* `secrets` (value: `"secrets"`)

* `labels` (value: `"labels"`)

* `views` (value: `"views"`)

* `documents` (value: `"documents"`)

* `notificationRules` (value: `"notificationRules"`)

* `notificationEndpoints` (value: `"notificationEndpoints"`)

* `checks` (value: `"checks"`)

* `dbrp` (value: `"dbrp"`)

* `notebooks` (value: `"notebooks"`)




