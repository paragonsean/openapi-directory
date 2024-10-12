

# AutoData

`data` property allows you to specify the data stored in the QR Code.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hidden** | **Boolean** | Hidden network. Set to &#x60;true&#x60; if the SSID broadcasting is disabled (network is hidden). |  [optional] |
|**password** | **String** | Network password. The value is not required for the public network. |  [optional] |
|**security** | **WiFiSecurity** | Network authentication type. Value &#x60;nopass&#x60; is used to set explicitly no access password (public network) and is an equivalent for left the password unset. In that case, the value may be also omitted. |  [optional] |
|**ssid** | **String** | Network SSID (name). |  |
|**bcc** | [**Bcc**](Bcc.md) |  |  [optional] |
|**body** | **String** | The message body. |  [optional] |
|**cc** | [**Cc**](Cc.md) |  |  [optional] |
|**subject** | **String** | The message subject. |  [optional] |
|**to** | [**To1**](To1.md) |  |  |
|**address** | **String** | Wallet address. |  |
|**amount** | **BigDecimal** | Decimal value of payment amount. |  [optional] |
|**currency** | **Cryptocurrency** | Payment currency. |  |
|**label** | **String** | Label for the wallet address (e.g. name of receiver). |  [optional] |
|**message** | **String** | Message template. |  [optional] |
|**phone** | **String** | Telephone number. |  |
|**format** | **GeolocationUriFormat** | URI format.  - &#x60;rfc5870&#x60; data encoded according to &lt;a href&#x3D;\&quot;https://datatracker.ietf.org/doc/html/rfc5870\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; target&#x3D;\&quot;_blank\&quot; &gt;RFC5870 standard&lt;/a&gt;  - &#x60;google&#x60; data encoded according to &lt;a href&#x3D;\&quot;https://developers.google.com/maps/documentation/urls/android-intents\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; target&#x3D;\&quot;_blank\&quot; &gt;Google Maps standard&lt;/a&gt; |  [optional] |
|**latitude** | **BigDecimal** | Location latitude. |  |
|**longitude** | **BigDecimal** | Location longitude. |  |



