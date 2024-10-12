# TrafficDirectorApi.Node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientFeatures** | **[String]** | Client feature support list. These are well known features described in the Envoy API repository for a given major version of an API. Client features use reverse DNS naming scheme, for example &#x60;&#x60;com.acme.feature&#x60;&#x60;. See :ref:&#x60;the list of features &#x60; that xDS client may support. | [optional] 
**cluster** | **String** | Defines the local service cluster name where Envoy is running. Though optional, it should be set if any of the following features are used: :ref:&#x60;statsd &#x60;, :ref:&#x60;health check cluster verification &#x60;, :ref:&#x60;runtime override directory &#x60;, :ref:&#x60;user agent addition &#x60;, :ref:&#x60;HTTP global rate limiting &#x60;, :ref:&#x60;CDS &#x60;, and :ref:&#x60;HTTP tracing &#x60;, either in this message or via :option:&#x60;--service-cluster&#x60;. | [optional] 
**dynamicParameters** | [**{String: ContextParams}**](ContextParams.md) | Map from xDS resource type URL to dynamic context parameters. These may vary at runtime (unlike other fields in this message). For example, the xDS client may have a shard identifier that changes during the lifetime of the xDS client. In Envoy, this would be achieved by updating the dynamic context on the Server::Instance&#39;s LocalInfo context provider. The shard ID dynamic parameter then appears in this field during future discovery requests. | [optional] 
**extensions** | [**[Extension]**](Extension.md) | List of extensions and their versions supported by the node. | [optional] 
**id** | **String** | An opaque node identifier for the Envoy node. This also provides the local service node name. It should be set if any of the following features are used: :ref:&#x60;statsd &#x60;, :ref:&#x60;CDS &#x60;, and :ref:&#x60;HTTP tracing &#x60;, either in this message or via :option:&#x60;--service-node&#x60;. | [optional] 
**listeningAddresses** | [**[Address]**](Address.md) | Known listening ports on the node as a generic hint to the management server for filtering :ref:&#x60;listeners &#x60; to be returned. For example, if there is a listener bound to port 80, the list can optionally contain the SocketAddress &#x60;&#x60;(0.0.0.0,80)&#x60;&#x60;. The field is optional and just a hint. | [optional] 
**locality** | [**Locality**](Locality.md) |  | [optional] 
**metadata** | **{String: Object}** | Opaque metadata extending the node identifier. Envoy will pass this directly to the management server. | [optional] 
**userAgentBuildVersion** | [**BuildVersion**](BuildVersion.md) |  | [optional] 
**userAgentName** | **String** | Free-form string that identifies the entity requesting config. E.g. \&quot;envoy\&quot; or \&quot;grpc\&quot; | [optional] 
**userAgentVersion** | **String** | Free-form string that identifies the version of the entity requesting config. E.g. \&quot;1.12.2\&quot; or \&quot;abcd1234\&quot;, or \&quot;SpecialEnvoyBuild\&quot; | [optional] 


