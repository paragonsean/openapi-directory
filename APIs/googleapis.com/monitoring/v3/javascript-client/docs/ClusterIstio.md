# CloudMonitoringApi.ClusterIstio

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterName** | **String** | The name of the Kubernetes cluster in which this Istio service is defined. Corresponds to the cluster_name resource label in k8s_cluster resources. | [optional] 
**location** | **String** | The location of the Kubernetes cluster in which this Istio service is defined. Corresponds to the location resource label in k8s_cluster resources. | [optional] 
**serviceName** | **String** | The name of the Istio service underlying this service. Corresponds to the destination_service_name metric label in Istio metrics. | [optional] 
**serviceNamespace** | **String** | The namespace of the Istio service underlying this service. Corresponds to the destination_service_namespace metric label in Istio metrics. | [optional] 


