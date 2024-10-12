

# PackResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boxes** | [**List&lt;Box&gt;**](Box.md) | List of boxes, packed, with their contained items. |  [optional] |
|**built** | **String** | build timestamp of engine. |  [optional] |
|**leftovers** | [**List&lt;Item&gt;**](Item.md) | items left over that could not be packed into any available boxes. |  [optional] |
|**lenBoxes** | **Integer** | cardinality of all packed boxes |  [optional] |
|**lenItems** | **Integer** | cardinality of all items |  [optional] |
|**lenLeftovers** | **Integer** | cardinality of items unabled to be packed |  [optional] |
|**packTime** | **BigDecimal** | seconds spent in packing |  [optional] |
|**renderTime** | **BigDecimal** | seconds spent in rendering and placement instruction creation of packing solution |  [optional] |
|**scripts** | **String** | additional javascripts for any image loading. |  [optional] |
|**styles** | **String** | additional styles for pack images |  [optional] |
|**svgs** | **String** | all box SVG images |  [optional] |
|**title** | **String** | title of packing result, when applicable. |  [optional] |
|**totalCost** | **Integer** | total estimated cost of all packed boxes, when applicable, in cents. |  [optional] |
|**totalTime** | **BigDecimal** | seconds spent generating response, total. |  [optional] |
|**version** | **String** | version of engine |  [optional] |



