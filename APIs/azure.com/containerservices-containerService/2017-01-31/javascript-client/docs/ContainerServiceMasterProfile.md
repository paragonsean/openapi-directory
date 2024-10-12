# ContainerServiceClient.ContainerServiceMasterProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **Number** | Number of masters (VMs) in the container service cluster. Allowed values are 1, 3, and 5. The default value is 1. | [optional] [default to CountEnum.1]
**dnsPrefix** | **String** | DNS prefix to be used to create the FQDN for master. | 
**fqdn** | **String** | FQDN for the master. | [optional] [readonly] 



## Enum: CountEnum


* `1` (value: `1`)

* `3` (value: `3`)

* `5` (value: `5`)




