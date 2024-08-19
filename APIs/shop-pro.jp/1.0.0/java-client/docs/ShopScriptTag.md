

# ShopScriptTag


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | アカウントID |  [optional] |
|**displayScope** | [**DisplayScopeEnum**](#DisplayScopeEnum) | スクリプトを出力するページ - &#x60;shop&#x60;: ショップページ - &#x60;thanks_page&#x60;: 注文完了ページ  |  [optional] |
|**id** | **Integer** | スクリプトタグID |  [optional] |
|**integrity** | **String** | スクリプトファイルのハッシュ値（script tagのintegrity属性） |  [optional] |
|**makeDate** | **Integer** | 作成日時 |  [optional] |
|**oauthApplicationId** | **Integer** | OAuthアプリケーションID |  [optional] |
|**src** | **String** | スクリプトURL |  [optional] |
|**updateDate** | **Integer** | 更新日時 |  [optional] |



## Enum: DisplayScopeEnum

| Name | Value |
|---- | -----|
| SHOP | &quot;shop&quot; |
| THANKS_PAGE | &quot;thanks_page&quot; |



