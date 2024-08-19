# RocketServices.SingleSignOnRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookieType** | **String** | If you specify a cookie type then a content filter cookie will be returned along with the token(s). This is only intended for web based clients which need to pass the cookies to a server to render a page based on the user&#39;s content filters e.g subscription code.  If type &#x60;Session&#x60; the cookie will be session based. If type &#x60;Persistent&#x60; the cookie will have a medium term lifespan. If undefined no cookies will be set.  | [optional] 
**linkAccounts** | **Boolean** | When a user attempts to sign in using single-sign-on, we may find an account created previously through the manual sign up flow with the same email. If this is the case then an option to link the two accounts can be made available.  If this flag is set to true then accounts will be linked automatically.  If this flag is not set or set to false and an existing account is found  then an http 401 with subcode &#x60;6001&#x60; will be returned. Client apps can then present the option to link the accounts. If the user decides to accept, then the same call can be repeated with this flag set to true.  | [optional] 
**provider** | **String** | The third party single-sign-on provider. | 
**scopes** | **[String]** | The scope(s) of the tokens required. For each scope listed an Account and Profile token of that scope will be returned.  | [optional] 
**token** | **String** | A token from the third party single-sign-on provider e.g. an identity token from Facebook. | 



## Enum: CookieTypeEnum


* `Session` (value: `"Session"`)

* `Persistent` (value: `"Persistent"`)





## Enum: ProviderEnum


* `Facebook` (value: `"Facebook"`)





## Enum: [ScopesEnum]


* `Catalog` (value: `"Catalog"`)

* `Commerce` (value: `"Commerce"`)

* `Settings` (value: `"Settings"`)

* `Playback` (value: `"Playback"`)




