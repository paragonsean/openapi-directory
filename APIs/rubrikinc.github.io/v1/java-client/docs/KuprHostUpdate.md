

# KuprHostUpdate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentCertificate** | **String** | The agent certificate of the registered host. X.509 certificates in Base64 encoded DER format. Each certificate must start with -----BEGIN CERTIFICATE----- and end with -----END CERTIFICATE-----.  |  [optional] |
|**agentId** | **String** | The agent ID of the registered host. |  [optional] |
|**hostname** | **String** |  |  [optional] |
|**ipv4Addresses** | **List&lt;String&gt;** | An array containing the IPv4 address to Kupr host.  |  [optional] |
|**operatingSystemInfo** | [**OperatingSystemInfoEnum**](#OperatingSystemInfoEnum) | Operating system information of a specified kupr host. |  [optional] |
|**operatingSystemType** | [**OperatingSystemTypeEnum**](#OperatingSystemTypeEnum) | Operating system of a specified kupr host. |  [optional] |
|**operatingSystemVersion** | **String** | Operating system version of a specified kupr host. |  [optional] |



## Enum: OperatingSystemInfoEnum

| Name | Value |
|---- | -----|
| LINUX | &quot;Linux&quot; |
| RHEL | &quot;Rhel&quot; |
| UBUNTU | &quot;Ubuntu&quot; |
| SUSE | &quot;Suse&quot; |
| CENTOS | &quot;Centos&quot; |



## Enum: OperatingSystemTypeEnum

| Name | Value |
|---- | -----|
| LINUX | &quot;Linux&quot; |



