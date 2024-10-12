# AdSenseManagementApi.AdClient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Output only. Resource name of the ad client. Format: accounts/{account}/adclients/{adclient} | [optional] [readonly] 
**productCode** | **String** | Output only. Reporting product code of the ad client. For example, \&quot;AFC\&quot; for AdSense for Content. Corresponds to the &#x60;PRODUCT_CODE&#x60; dimension, and present only if the ad client supports reporting. | [optional] [readonly] 
**reportingDimensionId** | **String** | Output only. Unique ID of the ad client as used in the &#x60;AD_CLIENT_ID&#x60; reporting dimension. Present only if the ad client supports reporting. | [optional] [readonly] 
**state** | **String** | Output only. State of the ad client. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `READY` (value: `"READY"`)

* `GETTING_READY` (value: `"GETTING_READY"`)

* `REQUIRES_REVIEW` (value: `"REQUIRES_REVIEW"`)




