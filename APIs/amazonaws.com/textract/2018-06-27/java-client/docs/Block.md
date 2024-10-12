

# Block

<p>A <code>Block</code> represents items that are recognized in a document within a group of pixels close to each other. The information returned in a <code>Block</code> object depends on the type of operation. In text detection for documents (for example <a>DetectDocumentText</a>), you get information about the detected words and lines of text. In text analysis (for example <a>AnalyzeDocument</a>), you can also get information about the fields, tables, and selection elements that are detected in the document.</p> <p>An array of <code>Block</code> objects is returned by both synchronous and asynchronous operations. In synchronous operations, such as <a>DetectDocumentText</a>, the array of <code>Block</code> objects is the entire set of results. In asynchronous operations, such as <a>GetDocumentAnalysis</a>, the array is returned over one or more responses.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html\">How Amazon Textract Works</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockType** | [**BlockType**](BlockType.md) |  |  [optional] |
|**confidence** | [**Float**](Float.md) |  |  [optional] |
|**text** | [**String**](String.md) |  |  [optional] |
|**textType** | [**TextType**](TextType.md) |  |  [optional] |
|**rowIndex** | [**Integer**](Integer.md) |  |  [optional] |
|**columnIndex** | [**Integer**](Integer.md) |  |  [optional] |
|**rowSpan** | [**Integer**](Integer.md) |  |  [optional] |
|**columnSpan** | [**Integer**](Integer.md) |  |  [optional] |
|**geometry** | [**BlockGeometry**](BlockGeometry.md) |  |  [optional] |
|**id** | [**String**](String.md) |  |  [optional] |
|**relationships** | [**List**](List.md) |  |  [optional] |
|**entityTypes** | [**List**](List.md) |  |  [optional] |
|**selectionStatus** | [**SelectionStatus**](SelectionStatus.md) |  |  [optional] |
|**page** | [**Integer**](Integer.md) |  |  [optional] |
|**query** | [**BlockQuery**](BlockQuery.md) |  |  [optional] |



