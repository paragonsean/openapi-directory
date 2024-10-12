# ServiceConsumerManagementApi.BackendRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | The address of the API backend. The scheme is used to determine the backend protocol and security. The following schemes are accepted: SCHEME PROTOCOL SECURITY http:// HTTP None https:// HTTP TLS grpc:// gRPC None grpcs:// gRPC TLS It is recommended to explicitly include a scheme. Leaving out the scheme may cause constrasting behaviors across platforms. If the port is unspecified, the default is: - 80 for schemes without TLS - 443 for schemes with TLS For HTTP backends, use protocol to specify the protocol version. | [optional] 
**deadline** | **Number** | The number of seconds to wait for a response from a request. The default varies based on the request protocol and deployment environment. | [optional] 
**disableAuth** | **Boolean** | When disable_auth is true, a JWT ID token won&#39;t be generated and the original \&quot;Authorization\&quot; HTTP header will be preserved. If the header is used to carry the original token and is expected by the backend, this field must be set to true to preserve the header. | [optional] 
**jwtAudience** | **String** | The JWT audience is used when generating a JWT ID token for the backend. This ID token will be added in the HTTP \&quot;authorization\&quot; header, and sent to the backend. | [optional] 
**minDeadline** | **Number** | Deprecated, do not use. | [optional] 
**operationDeadline** | **Number** | The number of seconds to wait for the completion of a long running operation. The default is no deadline. | [optional] 
**overridesByRequestProtocol** | [**{String: BackendRule}**](BackendRule.md) | The map between request protocol and the backend address. | [optional] 
**pathTranslation** | **String** |  | [optional] 
**protocol** | **String** | The protocol used for sending a request to the backend. The supported values are \&quot;http/1.1\&quot; and \&quot;h2\&quot;. The default value is inferred from the scheme in the address field: SCHEME PROTOCOL http:// http/1.1 https:// http/1.1 grpc:// h2 grpcs:// h2 For secure HTTP backends (https://) that support HTTP/2, set this field to \&quot;h2\&quot; for improved performance. Configuring this field to non-default values is only supported for secure HTTP backends. This field will be ignored for all other backends. See https://www.iana.org/assignments/tls-extensiontype-values/tls-extensiontype-values.xhtml#alpn-protocol-ids for more details on the supported values. | [optional] 
**selector** | **String** | Selects the methods to which this rule applies. Refer to selector for syntax details. | [optional] 



## Enum: PathTranslationEnum


* `PATH_TRANSLATION_UNSPECIFIED` (value: `"PATH_TRANSLATION_UNSPECIFIED"`)

* `CONSTANT_ADDRESS` (value: `"CONSTANT_ADDRESS"`)

* `APPEND_PATH_TO_ADDRESS` (value: `"APPEND_PATH_TO_ADDRESS"`)




