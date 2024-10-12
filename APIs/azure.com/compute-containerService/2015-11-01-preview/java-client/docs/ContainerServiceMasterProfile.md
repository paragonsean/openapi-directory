

# ContainerServiceMasterProfile

Profile for container service master

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | [**CountEnum**](#CountEnum) | Number of masters (VMs) in the container cluster |  [optional] |
|**dnsPrefix** | **String** | DNS prefix to be used to create FQDN for master |  |
|**fqdn** | **String** | FQDN for the master |  [optional] [readonly] |



## Enum: CountEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_3 | 3 |
| NUMBER_5 | 5 |



