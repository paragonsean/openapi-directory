

# LoggingServer

Logging server to receive vCenter or ESXi logs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Creation time of this resource. |  [optional] [readonly] |
|**hostname** | **String** | Required. Fully-qualified domain name (FQDN) or IP Address of the logging server. |  [optional] |
|**name** | **String** | Output only. The resource name of this logging server. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud/loggingServers/my-logging-server&#x60; |  [optional] [readonly] |
|**port** | **Integer** | Required. Port number at which the logging server receives logs. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Required. Protocol used by vCenter to send logs to a logging server. |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | Required. The type of component that produces logs that will be forwarded to this logging server. |  [optional] |
|**uid** | **String** | Output only. System-generated unique identifier for the resource. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Last update time of this resource. |  [optional] [readonly] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| PROTOCOL_UNSPECIFIED | &quot;PROTOCOL_UNSPECIFIED&quot; |
| UDP | &quot;UDP&quot; |
| TCP | &quot;TCP&quot; |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| SOURCE_TYPE_UNSPECIFIED | &quot;SOURCE_TYPE_UNSPECIFIED&quot; |
| ESXI | &quot;ESXI&quot; |
| VCSA | &quot;VCSA&quot; |



