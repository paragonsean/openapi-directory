

# GoogleCloudDiscoveryengineV1betaPageInfo

Detailed page information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pageCategory** | **String** | The most specific category associated with a category page. To represent full path of category, use &#39;&gt;&#39; sign to separate different hierarchies. If &#39;&gt;&#39; is part of the category name, please replace it with other character(s). Category pages include special pages such as sales or promotions. For instance, a special sale page may have the category hierarchy: &#x60;\&quot;pageCategory\&quot; : \&quot;Sales &gt; 2017 Black Friday Deals\&quot;&#x60;. Required for &#x60;view-category-page&#x60; events. Other event types should not set this field. Otherwise, an &#x60;INVALID_ARGUMENT&#x60; error is returned. |  [optional] |
|**pageviewId** | **String** | A unique ID of a web page view. This should be kept the same for all user events triggered from the same pageview. For example, an item detail page view could trigger multiple events as the user is browsing the page. The &#x60;pageview_id&#x60; property should be kept the same for all these events so that they can be grouped together properly. When using the client side event reporting with JavaScript pixel and Google Tag Manager, this value is filled in automatically. |  [optional] |
|**referrerUri** | **String** | The referrer URL of the current page. When using the client side event reporting with JavaScript pixel and Google Tag Manager, this value is filled in automatically. However, some browser privacy restrictions may cause this field to be empty. |  [optional] |
|**uri** | **String** | Complete URL (window.location.href) of the user&#39;s current page. When using the client side event reporting with JavaScript pixel and Google Tag Manager, this value is filled in automatically. Maximum length 5,000 characters. |  [optional] |



