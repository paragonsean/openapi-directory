

# VpnClientParameters

Vpn Client Parameters for package generation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationMethod** | [**AuthenticationMethodEnum**](#AuthenticationMethodEnum) | VPN client Authentication Method. Possible values are: &#39;EAPTLS&#39; and &#39;EAPMSCHAPv2&#39;. |  [optional] |
|**clientRootCertificates** | **List&lt;String&gt;** | A list of client root certificates public certificate data encoded as Base-64 strings. Optional parameter for external radius based authentication with EAPTLS. |  [optional] |
|**processorArchitecture** | [**ProcessorArchitectureEnum**](#ProcessorArchitectureEnum) | VPN client Processor Architecture. Possible values are: &#39;AMD64&#39; and &#39;X86&#39;. |  [optional] |
|**radiusServerAuthCertificate** | **String** | The public certificate data for the radius server authentication certificate as a Base-64 encoded string. Required only if external radius authentication has been configured with EAPTLS authentication. |  [optional] |



## Enum: AuthenticationMethodEnum

| Name | Value |
|---- | -----|
| EAPTLS | &quot;EAPTLS&quot; |
| EAPMSCHAPV2 | &quot;EAPMSCHAPv2&quot; |



## Enum: ProcessorArchitectureEnum

| Name | Value |
|---- | -----|
| AMD64 | &quot;Amd64&quot; |
| X86 | &quot;X86&quot; |



