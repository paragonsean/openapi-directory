# LinQr.AutoQRCodeMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AutoData**](AutoData.md) |  | 
**image** | [**EmbeddedImageMultipart**](EmbeddedImageMultipart.md) | &#x60;image&#x60; property allows you to set parameters of a custom image (e.g. your company logo, icon etc.) placed in the center of the generated QR Code. | [optional] 
**output** | [**OutputFile**](OutputFile.md) | &#x60;output&#x60; property allows you to specify the name and extension (type) of the file returned by the API | [optional] 
**size** | [**SizeMultipart**](SizeMultipart.md) | &#x60;size&#x60; property allows you to set the values that define the sizes of the generated QR Code. | [optional] 
**style** | [**Style**](Style.md) | &#x60;style&#x60; property allows you to select the appearance parameters of the modules and eyes of the generated QR Code.  All color specifications can be defined via: * CSS3 name: &#x60;Black&#x60;, &#x60;azure&#x60;, ... * hex value: &#x60;0x000&#x60;, &#x60;#FFFFFF&#x60;, &#x60;7fffd4&#x60;, ... * RGB/RGBA strings: &#x60;rgb(255, 255, 255)&#x60;, &#x60;rgba(255, 255, 255, 0.5)&#x60;, ... * HSL strings: &#x60;hsl(270, 60%, 70%)&#x60;, &#x60;hsl(270, 60%, 70%, .5)&#x60;, ...  Color values can be obtained from any online color picker like &lt;a href&#x3D;\&quot;https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; target&#x3D;\&quot;_blank\&quot; &gt;developer.mozilla.org&lt;/a&gt;. | [optional] 


