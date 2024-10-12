# NetworkManagementClient.VpnClientParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticationMethod** | **String** | VPN client Authentication Method. Possible values are: &#39;EAPTLS&#39; and &#39;EAPMSCHAPv2&#39;. | [optional] 
**clientRootCertificates** | **[String]** | A list of client root certificates public certificate data encoded as Base-64 strings. Optional parameter for external radius based authentication with EAPTLS. | [optional] 
**processorArchitecture** | **String** | VPN client Processor Architecture. Possible values are: &#39;AMD64&#39; and &#39;X86&#39;. | [optional] 
**radiusServerAuthCertificate** | **String** | The public certificate data for the radius server authentication certificate as a Base-64 encoded string. Required only if external radius authentication has been configured with EAPTLS authentication. | [optional] 



## Enum: AuthenticationMethodEnum


* `EAPTLS` (value: `"EAPTLS"`)

* `EAPMSCHAPv2` (value: `"EAPMSCHAPv2"`)





## Enum: ProcessorArchitectureEnum


* `Amd64` (value: `"Amd64"`)

* `X86` (value: `"X86"`)




