

# AccountResponse

Successful response for `/api/vlm/account`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountName** | **String** | Account name |  [optional] |
|**address** | **String** | Address of contact |  [optional] |
|**appKey** | [**AccountResponseAppKey**](AccountResponseAppKey.md) |  |  [optional] |
|**appKeys** | [**List&lt;AppKeyItems&gt;**](AppKeyItems.md) | Array of application keys |  [optional] |
|**city** | **String** | City of contact |  [optional] |
|**cnpj** | **String** | CNPJ (Tax ID) of account |  [optional] |
|**companyName** | **String** | Company name |  [optional] |
|**complement** | **String** | Additional address of contact |  [optional] |
|**contact** | [**AccountResponseContact**](AccountResponseContact.md) |  |  [optional] |
|**country** | **String** | Country of contact |  [optional] |
|**creationDate** | **OffsetDateTime** | The date when the account was created |  [optional] |
|**defaultUrl** | **String** |  |  [optional] |
|**district** | **String** | Neighborhood of contact |  [optional] |
|**hasLogo** | **Boolean** | If logo has been setup |  [optional] |
|**haveParentAccount** | **Boolean** | If it has a parent account |  [optional] |
|**hosts** | **List&lt;String&gt;** | Hosts of all stores |  [optional] |
|**id** | **String** | ID of the account |  [optional] |
|**inactivationDate** | **OffsetDateTime** | The date when the account was deactivated |  [optional] |
|**isActive** | **Boolean** | If account is active or not |  [optional] |
|**isOperating** | **Boolean** | If it is in production |  [optional] |
|**licenses** | [**List&lt;LicenseItems&gt;**](LicenseItems.md) | Licenses of the account |  [optional] |
|**logo** | **String** | Filename of account logo |  [optional] |
|**lv** | **String** |  |  [optional] |
|**name** | **String** | Trading name |  [optional] |
|**number** | **String** | Number of the address of contact |  [optional] |
|**operationDate** | **OffsetDateTime** | The date when the account went into production |  [optional] |
|**parentAccountId** | **String** | The ID of the parent account |  [optional] |
|**parentAccountName** | **String** | The name of the parent account |  [optional] |
|**postalCode** | **String** | Zip Code of contact |  [optional] |
|**sites** | [**List&lt;SiteItems&gt;**](SiteItems.md) | Array of objects representing a store |  [optional] |
|**sponsor** | [**AccountResponseSponsor**](AccountResponseSponsor.md) |  |  [optional] |
|**state** | **String** | State/Province of contact |  [optional] |
|**telephone** | **String** | Telephone of contact |  [optional] |
|**tradingName** | **String** | Trading name |  [optional] |



