# LinQr.SizeMultipart

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quietZone** | **Number** | Default size of margin with background color around the generated QR Code. This length is expressed as number of modules of the Code. Recommended value is 4, but most readers allow you to read the code with smaller or zero margin.  For more information please refer to: &lt;a href&#x3D;\&quot;https://www.qrcode.com/en/howto/code.html\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; target&#x3D;\&quot;_blank\&quot; &gt;QRCode.com&lt;/a&gt;. | [optional] [default to 4]
**width** | **Number** | Width (and height, as the QR Codes are squares) in pixels of the generated image. If the requested value is &#x60;float&#x60; it will be casted to nearest &#x60;int&#x60;. | [optional] [default to 200]


