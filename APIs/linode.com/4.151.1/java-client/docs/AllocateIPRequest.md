

# AllocateIPRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**linodeId** | **Integer** | The ID of a Linode you you have access to that this address will be allocated to.  |  |
|**_public** | **Boolean** | Whether to create a public or private IPv4 address.  |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of address you are requesting. Only IPv4 addresses may be allocated through this endpoint.  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IPV4 | &quot;ipv4&quot; |



