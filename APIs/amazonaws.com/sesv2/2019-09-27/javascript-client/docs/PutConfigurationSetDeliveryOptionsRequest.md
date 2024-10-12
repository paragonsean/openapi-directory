# AmazonSimpleEmailService.PutConfigurationSetDeliveryOptionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tlsPolicy** | **String** | Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is &lt;code&gt;Require&lt;/code&gt;, messages are only delivered if a TLS connection can be established. If the value is &lt;code&gt;Optional&lt;/code&gt;, messages can be delivered in plain text if a TLS connection can&#39;t be established. | [optional] 
**sendingPoolName** | **String** | The name of the dedicated IP pool to associate with the configuration set. | [optional] 



## Enum: TlsPolicyEnum


* `REQUIRE` (value: `"REQUIRE"`)

* `OPTIONAL` (value: `"OPTIONAL"`)




