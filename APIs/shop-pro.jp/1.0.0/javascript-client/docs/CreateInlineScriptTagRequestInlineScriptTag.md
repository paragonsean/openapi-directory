# Api.CreateInlineScriptTagRequestInlineScriptTag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayScope** | **String** | インラインスクリプトを出力するページ。  - &#x60;all&#x60;: カートの途中のページと注文完了ページの両方 - &#x60;thanks_page&#x60;: 注文完了ページ - &#x60;cart&#x60;: カートの途中のページ  | [optional] 
**script** | **String** | インラインスクリプト | [optional] 
**triggerEvent** | **String** | インラインスクリプトを実行するタイミング。  - &#x60;object_builded&#x60;: JSオブジェクトの作成が完了した時  | [optional] 



## Enum: DisplayScopeEnum


* `all` (value: `"all"`)

* `thanks_page` (value: `"thanks_page"`)

* `cart` (value: `"cart"`)





## Enum: TriggerEventEnum


* `object_builded` (value: `"object_builded"`)




