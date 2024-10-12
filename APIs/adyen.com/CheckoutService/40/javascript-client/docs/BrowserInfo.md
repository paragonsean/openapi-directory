# AdyenCheckoutApi.BrowserInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptHeader** | **String** | The accept header value of the shopper&#39;s browser. | 
**colorDepth** | **Number** | The color depth of the shopper&#39;s browser in bits per pixel. This should be obtained by using the browser&#39;s &#x60;screen.colorDepth&#x60; property. Accepted values: 1, 4, 8, 15, 16, 24, 30, 32 or 48 bit color depth. | 
**javaEnabled** | **Boolean** | Boolean value indicating if the shopper&#39;s browser is able to execute Java. | 
**javaScriptEnabled** | **Boolean** | Boolean value indicating if the shopper&#39;s browser is able to execute JavaScript. A default &#39;true&#39; value is assumed if the field is not present. | [optional] [default to true]
**language** | **String** | The &#x60;navigator.language&#x60; value of the shopper&#39;s browser (as defined in IETF BCP 47). | 
**screenHeight** | **Number** | The total height of the shopper&#39;s device screen in pixels. | 
**screenWidth** | **Number** | The total width of the shopper&#39;s device screen in pixels. | 
**timeZoneOffset** | **Number** | Time difference between UTC time and the shopper&#39;s browser local time, in minutes. | 
**userAgent** | **String** | The user agent value of the shopper&#39;s browser. | 


