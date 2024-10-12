

# GetInlineScriptTags200ResponseInlineScriptTagsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | アカウントID |  [optional] |
|**displayScope** | [**DisplayScopeEnum**](#DisplayScopeEnum) | インラインスクリプトを出力するページ。  - &#x60;all&#x60;: カートの途中のページと注文完了ページの両方 - &#x60;thanks_page&#x60;: 注文完了ページ - &#x60;cart&#x60;: カートの途中のページ  |  [optional] |
|**id** | **Integer** | インラインスクリプトタグID |  [optional] |
|**makeDate** | **Integer** | 作成日時 |  [optional] |
|**oauthApplicationId** | **Integer** | アプリID |  [optional] |
|**script** | **String** | インラインスクリプト |  [optional] |
|**triggerEvent** | [**TriggerEventEnum**](#TriggerEventEnum) | インラインスクリプトを実行するタイミング。  - &#x60;object_builded&#x60;: JSオブジェクトの作成が完了した時  |  [optional] |
|**updateDate** | **Integer** | 更新日時 |  [optional] |



## Enum: DisplayScopeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| THANKS_PAGE | &quot;thanks_page&quot; |
| CART | &quot;cart&quot; |



## Enum: TriggerEventEnum

| Name | Value |
|---- | -----|
| OBJECT_BUILDED | &quot;object_builded&quot; |



