

# MeshIstio

Istio service scoped to an Istio mesh. Anthos clusters running ASM < 1.6.8 will have their services ingested as this type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**meshUid** | **String** | Identifier for the mesh in which this Istio service is defined. Corresponds to the mesh_uid metric label in Istio metrics. |  [optional] |
|**serviceName** | **String** | The name of the Istio service underlying this service. Corresponds to the destination_service_name metric label in Istio metrics. |  [optional] |
|**serviceNamespace** | **String** | The namespace of the Istio service underlying this service. Corresponds to the destination_service_namespace metric label in Istio metrics. |  [optional] |



