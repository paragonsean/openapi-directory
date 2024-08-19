

# ServerTlsPolicy

ServerTlsPolicy is a resource that specifies how a server should authenticate incoming requests. This resource itself does not affect configuration unless it is attached to a target HTTPS proxy or endpoint config selector resource. ServerTlsPolicy in the form accepted by external HTTPS load balancers can be attached only to TargetHttpsProxy with an `EXTERNAL` or `EXTERNAL_MANAGED` load balancing scheme. Traffic Director compatible ServerTlsPolicies can be attached to EndpointPolicy and TargetHttpsProxy with Traffic Director `INTERNAL_SELF_MANAGED` load balancing scheme.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowOpen** | **Boolean** | This field applies only for Traffic Director policies. It is must be set to false for external HTTPS load balancer policies. Determines if server allows plaintext connections. If set to true, server allows plain text connections. By default, it is set to false. This setting is not exclusive of other encryption modes. For example, if &#x60;allow_open&#x60; and &#x60;mtls_policy&#x60; are set, server allows both plain text and mTLS connections. See documentation of other encryption modes to confirm compatibility. Consider using it if you wish to upgrade in place your deployment to TLS while having mixed TLS and non-TLS traffic reaching port :80. |  [optional] |
|**createTime** | **String** | Output only. The timestamp when the resource was created. |  [optional] [readonly] |
|**description** | **String** | Free-text description of the resource. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Set of label tags associated with the resource. |  [optional] |
|**mtlsPolicy** | [**MTLSPolicy**](MTLSPolicy.md) |  |  [optional] |
|**name** | **String** | Required. Name of the ServerTlsPolicy resource. It matches the pattern &#x60;projects/_*_/locations/{location}/serverTlsPolicies/{server_tls_policy}&#x60; |  [optional] |
|**serverCertificate** | [**GoogleCloudNetworksecurityV1CertificateProvider**](GoogleCloudNetworksecurityV1CertificateProvider.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The timestamp when the resource was updated. |  [optional] [readonly] |



