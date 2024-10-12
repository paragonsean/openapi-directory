# BrowshotApi.Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser** | [**Browser**](Browser.md) |  | [optional] 
**country** | **String** | instance&#39;s country of origin | [optional] 
**height** | **Number** | screen height in pixels | [optional] 
**id** | **Number** | instance ID (required to requests screenshots) | [optional] 
**load** | **Number** | instance load:  &lt; 1: new screenshot requests will be processed immediately,  1-2: new screenshot requests will be processed in about two minutes,  2-3: new screenshot requests will be processed in about four minutes,  3-4: new screenshot requests will be processed in about six minutes,  etc.  | [optional] 
**screenshotCost** | **Number** | number of credits for each screenshot | [optional] 
**type** | **String** | public, shared or private | [optional] 
**width** | **Number** | screen width in pixels | [optional] 



## Enum: TypeEnum


* `public` (value: `"public"`)

* `shared` (value: `"shared"`)

* `private` (value: `"private"`)




