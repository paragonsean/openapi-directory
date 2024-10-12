# AnthosOnPremApi.VmwareManualLbConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controlPlaneNodePort** | **Number** | NodePort for control plane service. The Kubernetes API server in the admin cluster is implemented as a Service of type NodePort (ex. 30968). | [optional] 
**ingressHttpNodePort** | **Number** | NodePort for ingress service&#39;s http. The ingress service in the admin cluster is implemented as a Service of type NodePort (ex. 32527). | [optional] 
**ingressHttpsNodePort** | **Number** | NodePort for ingress service&#39;s https. The ingress service in the admin cluster is implemented as a Service of type NodePort (ex. 30139). | [optional] 
**konnectivityServerNodePort** | **Number** | NodePort for konnectivity server service running as a sidecar in each kube-apiserver pod (ex. 30564). | [optional] 


