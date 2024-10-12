

# GkeCluster

Information specifying a GKE Cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cluster** | **String** | Information specifying a GKE Cluster. Format is &#x60;projects/{project_id}/locations/{location_id}/clusters/{cluster_id}&#x60;. |  [optional] |
|**internalIp** | **Boolean** | Optional. If true, &#x60;cluster&#x60; is accessed using the private IP address of the control plane endpoint. Otherwise, the default IP address of the control plane endpoint is used. The default IP address is the private IP address for clusters with private control-plane endpoints and the public IP address otherwise. Only specify this option when &#x60;cluster&#x60; is a [private GKE cluster](https://cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept). |  [optional] |



