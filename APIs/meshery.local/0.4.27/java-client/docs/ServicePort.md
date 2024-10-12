

# ServicePort


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appProtocol** | **String** | The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and http://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol. Field can be enabled with ServiceAppProtocol feature gate. +optional |  [optional] |
|**name** | **String** | The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. When considering the endpoints for a Service, this must match the &#39;name&#39; field in the EndpointPort. Optional if only one ServicePort is defined on this service. +optional |  [optional] |
|**nodePort** | **Integer** | The port on each node on which this service is exposed when type&#x3D;NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. More info: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport +optional |  [optional] |
|**port** | **Integer** | The port that will be exposed by this service. |  [optional] |
|**protocol** | **String** |  |  [optional] |
|**targetPort** | [**IntOrString**](IntOrString.md) |  |  [optional] |



