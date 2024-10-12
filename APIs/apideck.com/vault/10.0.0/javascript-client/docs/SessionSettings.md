# VaultApi.SessionSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowActions** | **[String]** | Hide actions from your users in [Vault](/apis/vault/reference#section/Get-Started). Actions in &#x60;allow_actions&#x60; will be shown on a connection in Vault. Available actions are: &#x60;delete&#x60;, &#x60;disconnect&#x60;, &#x60;reauthorize&#x60; and &#x60;disable&#x60;. Empty array will hide all actions. By default all actions are visible. | [optional] 
**autoRedirect** | **Boolean** | Automatically redirect to redirect uri after the connection has been configured as callable. Defaults to &#x60;false&#x60;. | [optional] [default to false]
**hideGuides** | **Boolean** | Hide Apideck connection guides in [Vault](/apis/vault/reference#section/Get-Started). Defaults to &#x60;false&#x60;. | [optional] [default to false]
**hideResourceSettings** | **Boolean** | A boolean that controls the display of the configurable resources for an integration. When set to true, the resource configuration options will be hidden and not shown to the user. When set to false, the resource configuration options will be displayed to the user. | [optional] [default to false]
**isolationMode** | **Boolean** | Configure [Vault](/apis/vault/reference#section/Get-Started) to run in isolation mode, meaning it only shows the connection settings and hides the navigation items. | [optional] [default to false]
**sandboxMode** | **Boolean** | Configure [Vault](/apis/vault/reference#section/Get-Started) to show a banner informing the logged in user is in a test environment. | [optional] [default to false]
**sessionLength** | **String** | The duration of time the session is valid for (maximum 1 week). | [optional] [default to &#39;1h&#39;]
**showLogs** | **Boolean** | Configure [Vault](/apis/vault/reference#section/Get-Started) to show the logs page. Defaults to &#x60;true&#x60;. | [optional] [default to true]
**showSidebar** | **Boolean** | Configure [Vault](/apis/vault/reference#section/Get-Started) to show the sidebar. Defaults to &#x60;true&#x60;. | [optional] [default to true]
**showSuggestions** | **Boolean** | Configure [Vault](/apis/vault/reference#section/Get-Started) to show the suggestions page. Defaults to &#x60;false&#x60;. | [optional] [default to false]
**unifiedApis** | [**[UnifiedApiId]**](UnifiedApiId.md) | Provide the IDs of the Unified APIs you want to be visible. Leaving it empty or omitting this field will show all Unified APIs. | [optional] 



## Enum: [AllowActionsEnum]


* `delete` (value: `"delete"`)

* `disconnect` (value: `"disconnect"`)

* `reauthorize` (value: `"reauthorize"`)

* `disable` (value: `"disable"`)




