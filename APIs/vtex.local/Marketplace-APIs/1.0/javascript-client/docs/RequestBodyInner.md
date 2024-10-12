# MarketplaceApi.RequestBodyInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **String** | The action being performed, which is always going to be &#x60;replace&#x60;. | [default to &#39;replace&#39;]
**path** | **String** | The path in which the value is being updated. It follows the standardized format &#x60;/{field}&#x60;, where &#x60;{field}&#x60; is the path&#39;s name. | [default to &#39;/field&#39;]
**value** | **Boolean** | The value that is being updated. Notice that the type will depend on the path that is being updated. | [default to false]


