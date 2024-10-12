

# AnalysisResponse

This shows the expected contents of a response from the service

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**language** | **String** | This is the language used for recognizing handwriting from the ink strokes in the request. |  [optional] |
|**recognitionUnits** | [**List&lt;RecognitionUnitInner&gt;**](RecognitionUnitInner.md) | The list of recognition units based on the analysis of the ink strokes. |  |
|**unit** | [**UnitEnum**](#UnitEnum) | This is the physical unit of the ink strokes. It is up to the application developer to decide how to convert the device specific units to physical units before calling the service. The conversion factor can be different based on the type of the device used. |  [optional] |
|**unitMultiple** | **BigDecimal** |  This is a scaling factor to be applied to the point coordinates when interpreting them in the physical units specified. |  [optional] |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| MM | &quot;mm&quot; |
| CM | &quot;cm&quot; |
| IN | &quot;in&quot; |



