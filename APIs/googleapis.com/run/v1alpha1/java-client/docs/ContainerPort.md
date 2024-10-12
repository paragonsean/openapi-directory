

# ContainerPort

ContainerPort represents a network port in a single container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerPort** | **Integer** | (Optional) Port number the container listens on. This must be a valid port number, 0 &lt; x &lt; 65536. |  [optional] |
|**name** | **String** | (Optional) If specified, used to specify which protocol to use. Allowed values are \&quot;http1\&quot; and \&quot;h2c\&quot;. |  [optional] |
|**protocol** | **String** | (Optional) Protocol for port. Must be \&quot;TCP\&quot;. Defaults to \&quot;TCP\&quot;. |  [optional] |



