# CloudMonitoringApi.IstioCanonicalService

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonicalService** | **String** | The name of the canonical service underlying this service. Corresponds to the destination_canonical_service_name metric label in label in Istio metrics (https://cloud.google.com/monitoring/api/metrics_istio). | [optional] 
**canonicalServiceNamespace** | **String** | The namespace of the canonical service underlying this service. Corresponds to the destination_canonical_service_namespace metric label in Istio metrics (https://cloud.google.com/monitoring/api/metrics_istio). | [optional] 
**meshUid** | **String** | Identifier for the Istio mesh in which this canonical service is defined. Corresponds to the mesh_uid metric label in Istio metrics (https://cloud.google.com/monitoring/api/metrics_istio). | [optional] 


