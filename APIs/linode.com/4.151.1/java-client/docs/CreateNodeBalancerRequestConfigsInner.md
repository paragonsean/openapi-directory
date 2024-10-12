

# CreateNodeBalancerRequestConfigsInner

A request object representing a NodeBalancer Config, including Nodes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**AlgorithmEnum**](#AlgorithmEnum) | What algorithm this NodeBalancer should use for routing traffic to backends.  |  [optional] |
|**check** | [**CheckEnum**](#CheckEnum) | The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down. * If &#x60;none&#x60; no check is performed. * &#x60;connection&#x60; requires only a connection to the backend to succeed. * &#x60;http&#x60; and &#x60;http_body&#x60; rely on the backend serving HTTP, and that   the response returned matches what is expected.  |  [optional] |
|**checkAttempts** | **Integer** | How many times to attempt a check before considering a backend to be down.  |  [optional] |
|**checkBody** | **String** | This value must be present in the response body of the check in order for it to pass. If this value is not present in the response body of a check request, the backend is considered to be down.  |  [optional] |
|**checkInterval** | **Integer** | How often, in seconds, to check that backends are up and serving requests.  Must be greater than &#x60;check_timeout&#x60;.  |  [optional] |
|**checkPassive** | **Boolean** | If true, any response from this backend with a &#x60;5xx&#x60; status code will be enough for it to be considered unhealthy and taken out of rotation.  |  [optional] |
|**checkPath** | **String** | The URL path to check on each backend. If the backend does not respond to this request it is considered to be down.  |  [optional] |
|**checkTimeout** | **Integer** | How long, in seconds, to wait for a check attempt before considering it failed.  Must be less than &#x60;check_interval&#x60;.  |  [optional] |
|**cipherSuite** | [**CipherSuiteEnum**](#CipherSuiteEnum) | What ciphers to use for SSL connections served by this NodeBalancer.  * &#x60;legacy&#x60; is considered insecure and should only be used if necessary.  |  [optional] |
|**nodes** | [**List&lt;NodeBalancerNode&gt;**](NodeBalancerNode.md) | The NodeBalancer Node(s) that serve this Config.  |  [optional] |
|**port** | **Integer** | The port this Config is for. These values must be unique across configs on a single NodeBalancer (you can&#39;t have two configs for port 80, for example).  While some ports imply some protocols, no enforcement is done and you may configure your NodeBalancer however is useful to you. For example, while port 443 is generally used for HTTPS, you do not need SSL configured to have a NodeBalancer listening on port 443.  |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | The protocol this port is configured to serve.  * The &#x60;http&#x60; and &#x60;tcp&#x60; protocols do not support &#x60;ssl_cert&#x60; and &#x60;ssl_key&#x60;.  * The &#x60;https&#x60; protocol is mutually required with &#x60;ssl_cert&#x60; and &#x60;ssl_key&#x60;.  Review our guide on [Available Protocols](/docs/products/networking/nodebalancers/guides/protocols/) for information on protocol features.  |  [optional] |
|**proxyProtocol** | [**ProxyProtocolEnum**](#ProxyProtocolEnum) | ProxyProtocol is a TCP extension that sends initial TCP connection information such as source/destination IPs and ports to backend devices. This information would be lost otherwise. Backend devices must be configured to work with ProxyProtocol if enabled.  * If ommited, or set to &#x60;none&#x60;, the NodeBalancer doesn&#39;t send any auxilary data over TCP connections. This is the default. * If set to &#x60;v1&#x60;, the human-readable header format (Version 1) is used. Requires &#x60;tcp&#x60; protocol. * If set to &#x60;v2&#x60;, the binary header format (Version 2) is used. Requires &#x60;tcp&#x60; protocol.  |  [optional] |
|**sslCert** | **String** | The PEM-formatted public SSL certificate (or the combined PEM-formatted SSL certificate and Certificate Authority chain) that should be served on this NodeBalancerConfig&#39;s port.  Line breaks must be represented as \&quot;\\n\&quot; in the string for requests (but not when using the Linode CLI).  [Diffie-Hellman Parameters](/docs/products/networking/nodebalancers/guides/ssl-termination/#diffie-hellman-parameters) can be included in this value to enable forward secrecy.  The contents of this field will not be shown in any responses that display the NodeBalancerConfig. Instead, &#x60;&lt;REDACTED&gt;&#x60; will be printed where the field appears.  The read-only &#x60;ssl_commonname&#x60; and &#x60;ssl_fingerprint&#x60; fields in a NodeBalancerConfig response are automatically derived from your certificate. Please refer to these fields to verify that the appropriate certificate was assigned to your NodeBalancerConfig.  |  [optional] |
|**sslKey** | **String** | The PEM-formatted private key for the SSL certificate set in the &#x60;ssl_cert&#x60; field.  Line breaks must be represented as \&quot;\\n\&quot; in the string for requests (but not when using the Linode CLI).  The contents of this field will not be shown in any responses that display the NodeBalancerConfig. Instead, &#x60;&lt;REDACTED&gt;&#x60; will be printed where the field appears.  The read-only &#x60;ssl_commonname&#x60; and &#x60;ssl_fingerprint&#x60; fields in a NodeBalancerConfig response are automatically derived from your certificate. Please refer to these fields to verify that the appropriate certificate was assigned to your NodeBalancerConfig.  |  [optional] |
|**stickiness** | [**StickinessEnum**](#StickinessEnum) | Controls how session stickiness is handled on this port. * If set to &#x60;none&#x60; connections will always be assigned a backend based on the algorithm configured. * If set to &#x60;table&#x60; sessions from the same remote address will be routed to the same   backend.  * For HTTP or HTTPS clients, &#x60;http_cookie&#x60; allows sessions to be   routed to the same backend based on a cookie set by the NodeBalancer.  |  [optional] |



## Enum: AlgorithmEnum

| Name | Value |
|---- | -----|
| ROUNDROBIN | &quot;roundrobin&quot; |
| LEASTCONN | &quot;leastconn&quot; |
| SOURCE | &quot;source&quot; |



## Enum: CheckEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| CONNECTION | &quot;connection&quot; |
| HTTP | &quot;http&quot; |
| HTTP_BODY | &quot;http_body&quot; |



## Enum: CipherSuiteEnum

| Name | Value |
|---- | -----|
| RECOMMENDED | &quot;recommended&quot; |
| LEGACY | &quot;legacy&quot; |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;http&quot; |
| HTTPS | &quot;https&quot; |
| TCP | &quot;tcp&quot; |



## Enum: ProxyProtocolEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| V1 | &quot;v1&quot; |
| V2 | &quot;v2&quot; |



## Enum: StickinessEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| TABLE | &quot;table&quot; |
| HTTP_COOKIE | &quot;http_cookie&quot; |



