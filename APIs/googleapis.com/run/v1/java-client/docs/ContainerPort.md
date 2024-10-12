

# ContainerPort

ContainerPort represents a network port in a single container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerPort** | **Integer** | Port number the container listens on. If present, this must be a valid port number, 0 &lt; x &lt; 65536. If not present, it will default to port 8080. For more information, see https://cloud.google.com/run/docs/container-contract#port |  [optional] |
|**name** | **String** | If specified, used to specify which protocol to use. Allowed values are \&quot;http1\&quot; and \&quot;h2c\&quot;. |  [optional] |
|**protocol** | **String** | Protocol for port. Must be \&quot;TCP\&quot;. Defaults to \&quot;TCP\&quot;. |  [optional] |



