# GkeHubApi.MonitoringConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **String** | Optional. Cluster name used to report metrics. For Anthos on VMWare/Baremetal/MultiCloud clusters, it would be in format {cluster_type}/{cluster_name}, e.g., \&quot;awsClusters/cluster_1\&quot;. | [optional] 
**clusterHash** | **String** | Optional. For GKE and Multicloud clusters, this is the UUID of the cluster resource. For VMWare and Baremetal clusters, this is the kube-system UID. | [optional] 
**kubernetesMetricsPrefix** | **String** | Optional. Kubernetes system metrics, if available, are written to this prefix. This defaults to kubernetes.io for GKE, and kubernetes.io/anthos for Anthos eventually. Noted: Anthos MultiCloud will have kubernetes.io prefix today but will migration to be under kubernetes.io/anthos. | [optional] 
**location** | **String** | Optional. Location used to report Metrics | [optional] 
**projectId** | **String** | Optional. Project used to report Metrics | [optional] 


