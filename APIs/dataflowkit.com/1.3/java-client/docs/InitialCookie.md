

# InitialCookie

InitialCookie structure keep cookies that optionally can be passed to the new fetcher crawl a website that requires a login. Generate Cookies array with EditThisCookie chrome extension.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domain** | **String** |  |  [optional] |
|**expirationDate** | **BigDecimal** |  |  [optional] |
|**hostOnly** | **Boolean** |  |  [optional] |
|**httpOnly** | **Boolean** |  |  [optional] |
|**id** | **BigDecimal** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**path** | **String** |  |  [optional] |
|**sameSite** | [**SameSiteEnum**](#SameSiteEnum) |  |  [optional] |
|**secure** | **Boolean** |  |  [optional] |
|**session** | **Boolean** |  |  [optional] |
|**storeID** | **String** |  |  [optional] |
|**value** | **String** |  |  [optional] |



## Enum: SameSiteEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;unspecified&quot; |
| STRICT | &quot;strict&quot; |
| LAX | &quot;lax&quot; |
| NO_RESTRICTION | &quot;no_restriction&quot; |



