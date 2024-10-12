

# VmwareManualLbConfig

Represents configuration parameters for an already existing manual load balancer. Given the nature of manual load balancers it is expected that said load balancer will be fully managed by users. IMPORTANT: Please note that the Anthos On-Prem API will not generate or update ManualLB configurations it can only bind a pre-existing configuration to a new VMware user cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**controlPlaneNodePort** | **Integer** | NodePort for control plane service. The Kubernetes API server in the admin cluster is implemented as a Service of type NodePort (ex. 30968). |  [optional] |
|**ingressHttpNodePort** | **Integer** | NodePort for ingress service&#39;s http. The ingress service in the admin cluster is implemented as a Service of type NodePort (ex. 32527). |  [optional] |
|**ingressHttpsNodePort** | **Integer** | NodePort for ingress service&#39;s https. The ingress service in the admin cluster is implemented as a Service of type NodePort (ex. 30139). |  [optional] |
|**konnectivityServerNodePort** | **Integer** | NodePort for konnectivity server service running as a sidecar in each kube-apiserver pod (ex. 30564). |  [optional] |



