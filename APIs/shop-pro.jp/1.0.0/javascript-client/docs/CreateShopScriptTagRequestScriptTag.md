# Api.CreateShopScriptTagRequestScriptTag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayScope** | **String** | スクリプトを出力するページ - &#x60;shop&#x60;: ショップページ - &#x60;thanks_page&#x60;: 注文完了ページ  | [optional] 
**integrity** | **String** | スクリプトのハッシュ値をBase64エンコードした値を設定します。この値はスクリプトタグのIntegrity属性値として利用されます。 詳しくは [サブリソース完全性 - Web セキュリティ | MDN](https://developer.mozilla.org/ja/docs/Web/Security/Subresource_Integrity) (外部サイト) をご覧ください。 ※この値が正しく設定されない場合はブラウザがスクリプトの読み込みをブロックします。この場合、一般的なWebブラウザ(e.g. Google Chrome, Firefox)の開発者ツールのコンソールでエラーを確認できます。  | [optional] 
**src** | **String** | スクリプトURL | [optional] 



## Enum: DisplayScopeEnum


* `shop` (value: `"shop"`)

* `thanks_page` (value: `"thanks_page"`)




