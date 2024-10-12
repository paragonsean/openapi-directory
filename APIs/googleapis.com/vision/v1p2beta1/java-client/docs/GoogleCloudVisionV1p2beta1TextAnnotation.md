

# GoogleCloudVisionV1p2beta1TextAnnotation

TextAnnotation contains a structured representation of OCR extracted text. The hierarchy of an OCR extracted text structure is like this: TextAnnotation -> Page -> Block -> Paragraph -> Word -> Symbol Each structural component, starting from Page, may further have their own properties. Properties describe detected languages, breaks etc.. Please refer to the TextAnnotation.TextProperty message definition below for more detail.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pages** | [**List&lt;GoogleCloudVisionV1p2beta1Page&gt;**](GoogleCloudVisionV1p2beta1Page.md) | List of pages detected by OCR. |  [optional] |
|**text** | **String** | UTF-8 text detected on the pages. |  [optional] |



