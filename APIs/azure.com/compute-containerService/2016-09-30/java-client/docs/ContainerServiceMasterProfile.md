

# ContainerServiceMasterProfile

Profile for the container service master.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | [**CountEnum**](#CountEnum) | Number of masters (VMs) in the container service cluster. Allowed values are 1, 3, and 5. The default value is 1. |  [optional] |
|**dnsPrefix** | **String** | DNS prefix to be used to create the FQDN for master. |  |
|**fqdn** | **String** | FQDN for the master. |  [optional] [readonly] |



## Enum: CountEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_3 | 3 |
| NUMBER_5 | 5 |



