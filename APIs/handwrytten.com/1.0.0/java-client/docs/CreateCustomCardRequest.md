

# CreateCustomCardRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardId** | **Integer** | the card id of the card template you&#39;re starting with.  You can find this by logging into Handwrytten, clicking \&quot;customize\&quot; next to any customizable card, and pulling the card ID from the end of the URL |  [optional] |
|**coverId** | **Integer** | the id of the image you want to use for the \&quot;cover\&quot;.  The cover is the large image on the front of the flat card. |  [optional] |
|**coverSizePercent** | **Integer** | the size of the image to use as the cover. |  [optional] |
|**footerAlign** | **String** | set to \&quot;left\&quot;, \&quot;center\&quot;, or \&quot;right\&quot; to align the footer appropriately |  [optional] |
|**footerFontId** | **Integer** | font ID of the text in the footer, found by using ListFontForCustomizer |  [optional] |
|**footerFontSize** | **Integer** | Font size of the text in the footer |  [optional] |
|**footerText** | **String** | optional text for the footer of the customizable card |  [optional] |
|**headerAlign** | **String** | set to \&quot;left\&quot;, \&quot;center\&quot;, or \&quot;right\&quot; to align the header appropriately |  [optional] |
|**headerAutoSize** | **Boolean** | if set to true, the header will be maximized to fill the header area |  [optional] |
|**headerFontId** | **Integer** | font ID of the text in the header, found by using ListFontForCustomizer |  [optional] |
|**headerFontSize** | **Integer** | font size of the text in the header of the card |  [optional] |
|**headerText** | **String** | text in the header, if type is set to \&quot;text\&quot; |  [optional] |
|**logoId** | **Integer** | Optional.  If setting \&quot;type\&quot; to \&quot;logo\&quot;, set the id of the logo here. |  [optional] |
|**logoSizePercent** | **Integer** | set to the desired scaling of the logo on the header |  [optional] |
|**name** | **String** | the name of the new card |  [optional] |
|**type** | **String** | Defines the top of the back of the card. Set to either \&quot;logo\&quot; or \&quot;text\&quot;. |  [optional] |
|**uid** | **String** | authorized UID of the session. |  [optional] |



