# Asana.PortfolioResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **String** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resourceType** | **String** | The base type of this resource. | [optional] [readonly] 
**name** | **String** | The name of the portfolio. | [optional] 
**color** | **String** | Color of the portfolio. | [optional] 
**createdAt** | **Date** | The time at which this resource was created. | [optional] [readonly] 
**createdBy** | [**UserCompact**](UserCompact.md) |  | [optional] 
**currentStatusUpdate** | [**StatusUpdateCompact**](StatusUpdateCompact.md) | The latest &#x60;status_update&#x60; posted to this portfolio. | [optional] 
**customFieldSettings** | [**[CustomFieldSettingResponse]**](CustomFieldSettingResponse.md) | Array of custom field settings applied to the portfolio. | [optional] 
**customFields** | [**[CustomFieldCompact]**](CustomFieldCompact.md) | Array of Custom Fields. | [optional] 
**dueOn** | **Date** | The localized day on which this portfolio is due. This takes a date with format YYYY-MM-DD. | [optional] 
**members** | [**[UserCompact]**](UserCompact.md) |  | [optional] [readonly] 
**owner** | [**UserCompact**](UserCompact.md) |  | [optional] 
**permalinkUrl** | **String** | A url that points directly to the object within Asana. | [optional] [readonly] 
**_public** | **Boolean** | True if the portfolio is public to its workspace members. | [optional] 
**startOn** | **Date** | The day on which work for this portfolio begins, or null if the portfolio has no start date. This takes a date with &#x60;YYYY-MM-DD&#x60; format. *Note: &#x60;due_on&#x60; must be present in the request when setting or unsetting the &#x60;start_on&#x60; parameter. Additionally, &#x60;start_on&#x60; and &#x60;due_on&#x60; cannot be the same date.* | [optional] 
**workspace** | [**PortfolioResponseAllOfWorkspace**](PortfolioResponseAllOfWorkspace.md) |  | [optional] 



## Enum: ColorEnum


* `dark-pink` (value: `"dark-pink"`)

* `dark-green` (value: `"dark-green"`)

* `dark-blue` (value: `"dark-blue"`)

* `dark-red` (value: `"dark-red"`)

* `dark-teal` (value: `"dark-teal"`)

* `dark-brown` (value: `"dark-brown"`)

* `dark-orange` (value: `"dark-orange"`)

* `dark-purple` (value: `"dark-purple"`)

* `dark-warm-gray` (value: `"dark-warm-gray"`)

* `light-pink` (value: `"light-pink"`)

* `light-green` (value: `"light-green"`)

* `light-blue` (value: `"light-blue"`)

* `light-red` (value: `"light-red"`)

* `light-teal` (value: `"light-teal"`)

* `light-brown` (value: `"light-brown"`)

* `light-orange` (value: `"light-orange"`)

* `light-purple` (value: `"light-purple"`)

* `light-warm-gray` (value: `"light-warm-gray"`)




