# RubrikRestApi.KuprHostRegister

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentCertificate** | **String** | The agent certificate of the registered host. X.509 certificates in Base64 encoded DER format. Each certificate must start with -----BEGIN CERTIFICATE----- and end with -----END CERTIFICATE-----.  | 
**agentId** | **String** | The agent ID of the registered host. | 
**hostname** | **String** |  | 
**ipv4Addresses** | **[String]** |  | [optional] 
**operatingSystemInfo** | **String** | Operating system information of a specified kupr host. | 
**operatingSystemType** | **String** | Operating system of a specified kupr host. | 
**operatingSystemVersion** | **String** | Operating system version of a specified kupr host. | [optional] 



## Enum: OperatingSystemInfoEnum


* `Linux` (value: `"Linux"`)

* `Rhel` (value: `"Rhel"`)

* `Ubuntu` (value: `"Ubuntu"`)

* `Suse` (value: `"Suse"`)

* `Centos` (value: `"Centos"`)





## Enum: OperatingSystemTypeEnum


* `Linux` (value: `"Linux"`)




