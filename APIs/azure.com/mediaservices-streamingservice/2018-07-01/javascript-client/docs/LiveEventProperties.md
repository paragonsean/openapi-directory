# AzureMediaServices.LiveEventProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | The exact time the Live Event was created. | [optional] [readonly] 
**crossSiteAccessPolicies** | [**CrossSiteAccessPolicies**](CrossSiteAccessPolicies.md) |  | [optional] 
**description** | **String** | The Live Event description. | [optional] 
**encoding** | [**LiveEventEncoding**](LiveEventEncoding.md) |  | [optional] 
**input** | [**LiveEventInput**](LiveEventInput.md) |  | 
**lastModified** | **Date** | The exact time the Live Event was last modified. | [optional] [readonly] 
**preview** | [**LiveEventPreview**](LiveEventPreview.md) |  | [optional] 
**provisioningState** | **String** | The provisioning state of the Live Event. | [optional] [readonly] 
**resourceState** | **String** | The resource state of the Live Event. | [optional] [readonly] 
**streamOptions** | **[String]** | The options to use for the LiveEvent.  This value is specified at creation time and cannot be updated. | [optional] 
**vanityUrl** | **Boolean** | Specifies whether to use a vanity url with the Live Event.  This value is specified at creation time and cannot be updated. | [optional] 



## Enum: ResourceStateEnum


* `Stopped` (value: `"Stopped"`)

* `Starting` (value: `"Starting"`)

* `Running` (value: `"Running"`)

* `Stopping` (value: `"Stopping"`)

* `Deleting` (value: `"Deleting"`)





## Enum: [StreamOptionsEnum]


* `Default` (value: `"Default"`)

* `LowLatency` (value: `"LowLatency"`)




