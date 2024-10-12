

# AdClient

Representation of an ad client. An ad client represents a user's subscription with a specific AdSense product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Output only. Resource name of the ad client. Format: accounts/{account}/adclients/{adclient} |  [optional] [readonly] |
|**productCode** | **String** | Output only. Reporting product code of the ad client. For example, \&quot;AFC\&quot; for AdSense for Content. Corresponds to the &#x60;PRODUCT_CODE&#x60; dimension, and present only if the ad client supports reporting. |  [optional] [readonly] |
|**reportingDimensionId** | **String** | Output only. Unique ID of the ad client as used in the &#x60;AD_CLIENT_ID&#x60; reporting dimension. Present only if the ad client supports reporting. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the ad client. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| READY | &quot;READY&quot; |
| GETTING_READY | &quot;GETTING_READY&quot; |
| REQUIRES_REVIEW | &quot;REQUIRES_REVIEW&quot; |



