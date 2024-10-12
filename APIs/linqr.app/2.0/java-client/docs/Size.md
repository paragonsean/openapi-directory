

# Size


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorCorrection** | **ECLevel** | Error correction level for generated QR Code. Correction mechanism allows to restore some encoded data if it is partially unreadable (e.g. physically damaged). Literals correspond to amount of data (QR Code area) which can be restored: * &#x60;L&#x60;: approx. 7% * &#x60;M&#x60;: approx. 15% * &#x60;Q&#x60;: approx. 25% * &#x60;H&#x60;: approx. 30%  Higher correction level causes in bigger (more data modules) resulting QR Code. **Note:** If image is embedded in the QR Code, &#x60;H&#x60; correction level is chosen automatically and overrides user input.  For more information please refer to: &lt;a href&#x3D;\&quot;https://www.qrcode.com/en/about/error_correction.html\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; target&#x3D;\&quot;_blank\&quot; &gt;QRCode.com&lt;/a&gt; |  [optional] |
|**quietZone** | **Integer** | Default size of margin with background color around the generated QR Code. This length is expressed as number of modules of the Code. Recommended value is 4, but most readers allow you to read the code with smaller or zero margin.  For more information please refer to: &lt;a href&#x3D;\&quot;https://www.qrcode.com/en/howto/code.html\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; target&#x3D;\&quot;_blank\&quot; &gt;QRCode.com&lt;/a&gt;. |  [optional] |
|**width** | **Integer** | Width (and height, as the QR Codes are squares) in pixels of the generated image. If the requested value is &#x60;float&#x60; it will be casted to nearest &#x60;int&#x60;. |  [optional] |



