

# AccessToken


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acr** | **String** |  |  [optional] |
|**address** | [**AddressClaimSet**](AddressClaimSet.md) |  |  [optional] |
|**allowedOrigins** | **List&lt;String&gt;** |  |  [optional] |
|**atHash** | **String** |  |  [optional] |
|**authTime** | **Long** |  |  [optional] |
|**authorization** | [**AccessTokenAuthorization**](AccessTokenAuthorization.md) |  |  [optional] |
|**azp** | **String** |  |  [optional] |
|**birthdate** | **String** |  |  [optional] |
|**cHash** | **String** |  |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) |  |  [optional] |
|**claimsLocales** | **String** |  |  [optional] |
|**cnf** | [**AccessTokenCertConf**](AccessTokenCertConf.md) |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**emailVerified** | **Boolean** |  |  [optional] |
|**exp** | **Long** |  |  [optional] |
|**familyName** | **String** |  |  [optional] |
|**gender** | **String** |  |  [optional] |
|**givenName** | **String** |  |  [optional] |
|**iat** | **Long** |  |  [optional] |
|**iss** | **String** |  |  [optional] |
|**jti** | **String** |  |  [optional] |
|**locale** | **String** |  |  [optional] |
|**middleName** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**nbf** | **Long** |  |  [optional] |
|**nickname** | **String** |  |  [optional] |
|**nonce** | **String** |  |  [optional] |
|**otherClaims** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**phoneNumberVerified** | **Boolean** |  |  [optional] |
|**picture** | **String** |  |  [optional] |
|**preferredUsername** | **String** |  |  [optional] |
|**profile** | **String** |  |  [optional] |
|**realmAccess** | [**AccessTokenAccess**](AccessTokenAccess.md) |  |  [optional] |
|**sHash** | **String** |  |  [optional] |
|**scope** | **String** |  |  [optional] |
|**sessionState** | **String** |  |  [optional] |
|**sub** | **String** |  |  [optional] |
|**trustedCerts** | **List&lt;String&gt;** |  |  [optional] |
|**typ** | **String** |  |  [optional] |
|**updatedAt** | **Long** |  |  [optional] |
|**website** | **String** |  |  [optional] |
|**zoneinfo** | **String** |  |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| INTERNAL | &quot;INTERNAL&quot; |
| ACCESS | &quot;ACCESS&quot; |
| ID | &quot;ID&quot; |
| ADMIN | &quot;ADMIN&quot; |
| USERINFO | &quot;USERINFO&quot; |



