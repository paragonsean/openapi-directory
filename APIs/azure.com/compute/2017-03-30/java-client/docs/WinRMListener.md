

# WinRMListener

Describes Protocol and thumbprint of Windows Remote Management listener

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateUrl** | **String** | This is the URL of a certificate that has been uploaded to Key Vault as a secret. For adding a secret to the Key Vault, see [Add a key or secret to the key vault](https://docs.microsoft.com/azure/key-vault/key-vault-get-started/#add). In this case, your certificate needs to be It is the Base64 encoding of the following JSON Object which is encoded in UTF-8: &lt;br&gt;&lt;br&gt; {&lt;br&gt;  \&quot;data\&quot;:\&quot;&lt;Base64-encoded-certificate&gt;\&quot;,&lt;br&gt;  \&quot;dataType\&quot;:\&quot;pfx\&quot;,&lt;br&gt;  \&quot;password\&quot;:\&quot;&lt;pfx-file-password&gt;\&quot;&lt;br&gt;} |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Specifies the protocol of listener. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;**http** &lt;br&gt;&lt;br&gt; **https** |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



