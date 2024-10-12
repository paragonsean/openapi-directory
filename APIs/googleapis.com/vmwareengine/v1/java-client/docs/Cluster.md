

# Cluster

A cluster in a private cloud.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Creation time of this resource. |  [optional] [readonly] |
|**management** | **Boolean** | Output only. True if the cluster is a management cluster; false otherwise. There can only be one management cluster in a private cloud and it has to be the first one. |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name of this cluster. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster&#x60; |  [optional] [readonly] |
|**nodeTypeConfigs** | [**Map&lt;String, NodeTypeConfig&gt;**](NodeTypeConfig.md) | Required. The map of cluster node types in this cluster, where the key is canonical identifier of the node type (corresponds to the &#x60;NodeType&#x60;). |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the resource. |  [optional] [readonly] |
|**stretchedClusterConfig** | [**StretchedClusterConfig**](StretchedClusterConfig.md) |  |  [optional] |
|**uid** | **String** | Output only. System-generated unique identifier for the resource. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Last update time of this resource. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| CREATING | &quot;CREATING&quot; |
| UPDATING | &quot;UPDATING&quot; |
| DELETING | &quot;DELETING&quot; |
| REPAIRING | &quot;REPAIRING&quot; |



