

# VmwareEngineNetwork

VMware Engine network resource that provides connectivity for VMware Engine private clouds.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Creation time of this resource. |  [optional] [readonly] |
|**description** | **String** | User-provided description for this VMware Engine network. |  [optional] |
|**etag** | **String** | Checksum that may be sent on update and delete requests to ensure that the user-provided value is up to date before the server processes a request. The server computes checksums based on the value of other fields in the request. |  [optional] |
|**name** | **String** | Output only. The resource name of the VMware Engine network. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/global/vmwareEngineNetworks/my-network&#x60; |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the VMware Engine network. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. VMware Engine network type. |  [optional] |
|**uid** | **String** | Output only. System-generated unique identifier for the resource. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Last update time of this resource. |  [optional] [readonly] |
|**vpcNetworks** | [**List&lt;VpcNetwork&gt;**](VpcNetwork.md) | Output only. VMware Engine service VPC networks that provide connectivity from a private cloud to customer projects, the internet, and other Google Cloud services. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| UPDATING | &quot;UPDATING&quot; |
| DELETING | &quot;DELETING&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| LEGACY | &quot;LEGACY&quot; |
| STANDARD | &quot;STANDARD&quot; |



