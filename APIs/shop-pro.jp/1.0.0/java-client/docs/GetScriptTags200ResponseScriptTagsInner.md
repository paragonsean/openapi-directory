

# GetScriptTags200ResponseScriptTagsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayScope** | [**DisplayScopeEnum**](#DisplayScopeEnum) | スクリプトを出力するページ。  - &#x60;all&#x60;: ショップページと注文完了ページの両方 - &#x60;shop&#x60;: ショップページ - &#x60;thanks_page&#x60;: 注文完了ページ - &#x60;cart&#x60;: カートの途中のページ  |  [optional] |
|**id** | **Integer** | スクリプトタグID |  [optional] |
|**makeDate** | **Integer** | 作成日時 |  [optional] |
|**src** | **String** | スクリプトURL |  [optional] |
|**updateDate** | **Integer** | 更新日時 |  [optional] |



## Enum: DisplayScopeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| SHOP | &quot;shop&quot; |
| THANKS_PAGE | &quot;thanks_page&quot; |
| CART | &quot;cart&quot; |



