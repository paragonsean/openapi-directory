

# VmwareAdminManualLbConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addonsNodePort** | **Integer** | NodePort for add-ons server in the admin cluster. |  [optional] |
|**controlPlaneNodePort** | **Integer** | NodePort for control plane service. The Kubernetes API server in the admin cluster is implemented as a Service of type NodePort (ex. 30968). |  [optional] |
|**ingressHttpNodePort** | **Integer** | NodePort for ingress service&#39;s http. The ingress service in the admin cluster is implemented as a Service of type NodePort (ex. 32527). |  [optional] |
|**ingressHttpsNodePort** | **Integer** | NodePort for ingress service&#39;s https. The ingress service in the admin cluster is implemented as a Service of type NodePort (ex. 30139). |  [optional] |
|**konnectivityServerNodePort** | **Integer** | NodePort for konnectivity server service running as a sidecar in each kube-apiserver pod (ex. 30564). |  [optional] |



