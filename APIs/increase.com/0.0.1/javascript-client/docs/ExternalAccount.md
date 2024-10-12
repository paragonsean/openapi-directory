# IncreaseApi.ExternalAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumber** | **String** | The destination account number. | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the External Account was created. | 
**description** | **String** | The External Account&#39;s description for display purposes. | 
**funding** | **String** | The type of the account to which the transfer will be sent. | 
**id** | **String** | The External Account&#39;s identifier. | 
**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN). | 
**status** | **String** | The External Account&#39;s status. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;external_account&#x60;. | 
**verificationStatus** | **String** | If you have verified ownership of the External Account. | 



## Enum: FundingEnum


* `checking` (value: `"checking"`)

* `savings` (value: `"savings"`)

* `other` (value: `"other"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `archived` (value: `"archived"`)





## Enum: TypeEnum


* `external_account` (value: `"external_account"`)





## Enum: VerificationStatusEnum


* `unverified` (value: `"unverified"`)

* `pending` (value: `"pending"`)

* `verified` (value: `"verified"`)




