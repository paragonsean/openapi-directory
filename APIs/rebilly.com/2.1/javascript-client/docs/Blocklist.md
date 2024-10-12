# RebillyRestApi.Blocklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[SelfLink]**](SelfLink.md) | The links related to resource. | [optional] [readonly] 
**createdTime** | **Date** | The blocklist created time. | [optional] [readonly] 
**expirationTime** | **Date** | The blocklist expiration time. | [optional] 
**id** | **String** | The blocklist identifier string. | [optional] [readonly] 
**type** | **String** | The blocklist type. | 
**updatedTime** | **Date** | The blocklist updated time. | [optional] [readonly] 
**value** | **String** | The blocklist value. | 



## Enum: TypeEnum


* `payment-card` (value: `"payment-card"`)

* `bank-account` (value: `"bank-account"`)

* `customer-id` (value: `"customer-id"`)

* `email` (value: `"email"`)

* `email-domain` (value: `"email-domain"`)

* `ip-address` (value: `"ip-address"`)

* `country` (value: `"country"`)

* `fingerprint` (value: `"fingerprint"`)

* `bin` (value: `"bin"`)

* `address` (value: `"address"`)




