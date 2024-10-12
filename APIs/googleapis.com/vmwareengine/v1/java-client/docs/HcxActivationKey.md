

# HcxActivationKey

HCX activation key. A default key is created during private cloud provisioning, but this behavior is subject to change and you should always verify active keys. Use VmwareEngine.ListHcxActivationKeys to retrieve existing keys and VmwareEngine.CreateHcxActivationKey to create new ones.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationKey** | **String** | Output only. HCX activation key. |  [optional] [readonly] |
|**createTime** | **String** | Output only. Creation time of HCX activation key. |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name of this HcxActivationKey. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1/privateClouds/my-cloud/hcxActivationKeys/my-key&#x60; |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of HCX activation key. |  [optional] [readonly] |
|**uid** | **String** | Output only. System-generated unique identifier for the resource. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| AVAILABLE | &quot;AVAILABLE&quot; |
| CONSUMED | &quot;CONSUMED&quot; |
| CREATING | &quot;CREATING&quot; |



