

# PutConfigurationSetDeliveryOptionsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tlsPolicy** | [**TlsPolicyEnum**](#TlsPolicyEnum) | Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is &lt;code&gt;Require&lt;/code&gt;, messages are only delivered if a TLS connection can be established. If the value is &lt;code&gt;Optional&lt;/code&gt;, messages can be delivered in plain text if a TLS connection can&#39;t be established. |  [optional] |
|**sendingPoolName** | **String** | The name of the dedicated IP pool that you want to associate with the configuration set. |  [optional] |



## Enum: TlsPolicyEnum

| Name | Value |
|---- | -----|
| REQUIRE | &quot;REQUIRE&quot; |
| OPTIONAL | &quot;OPTIONAL&quot; |



