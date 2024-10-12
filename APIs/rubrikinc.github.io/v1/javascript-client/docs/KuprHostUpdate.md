# RubrikRestApi.KuprHostUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentCertificate** | **String** | The agent certificate of the registered host. X.509 certificates in Base64 encoded DER format. Each certificate must start with -----BEGIN CERTIFICATE----- and end with -----END CERTIFICATE-----.  | [optional] 
**agentId** | **String** | The agent ID of the registered host. | [optional] 
**hostname** | **String** |  | [optional] 
**ipv4Addresses** | **[String]** | An array containing the IPv4 address to Kupr host.  | [optional] 
**operatingSystemInfo** | **String** | Operating system information of a specified kupr host. | [optional] 
**operatingSystemType** | **String** | Operating system of a specified kupr host. | [optional] 
**operatingSystemVersion** | **String** | Operating system version of a specified kupr host. | [optional] 



## Enum: OperatingSystemInfoEnum


* `Linux` (value: `"Linux"`)

* `Rhel` (value: `"Rhel"`)

* `Ubuntu` (value: `"Ubuntu"`)

* `Suse` (value: `"Suse"`)

* `Centos` (value: `"Centos"`)





## Enum: OperatingSystemTypeEnum


* `Linux` (value: `"Linux"`)




