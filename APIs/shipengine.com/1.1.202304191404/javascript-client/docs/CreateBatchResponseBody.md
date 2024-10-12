# ShipEngineApi.CreateBatchResponseBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batchErrorsUrl** | [**OptionalLink**](OptionalLink.md) | Link to batch errors endpoint | [readonly] 
**batchId** | **String** | A string that uniquely identifies the batch | [readonly] 
**batchLabelsUrl** | [**OptionalLink**](OptionalLink.md) | Link to batch labels query | 
**batchNotes** | **String** | Custom notes you can add for each created batch | [readonly] [default to &#39;&#39;]
**batchNumber** | **String** | The batch number. | [readonly] 
**batchShipmentsUrl** | [**OptionalLink**](OptionalLink.md) | The batch shipments endpoint | 
**completed** | **Number** | The number of labels generated in the batch | [readonly] 
**count** | **Number** | The total of errors, warnings, and completed properties | [readonly] 
**createdAt** | **Date** | The date and time the batch was created in ShipEngine | [readonly] 
**errors** | **Number** | The number of errors that occurred while generating the batch | [readonly] 
**externalBatchId** | **String** | A string that uniquely identifies the external batch | [readonly] 
**formDownload** | [**OptionalLink**](OptionalLink.md) | The form download for any customs that are needed | [readonly] 
**forms** | **Number** | The number of forms for customs that are available for download | [readonly] 
**labelDownload** | [**LabelDownload**](LabelDownload.md) | The label download for the batch | [readonly] 
**labelFormat** | [**LabelFormat**](LabelFormat.md) |  | [readonly] 
**labelLayout** | [**LabelLayout**](LabelLayout.md) | label layout | [readonly] 
**processedAt** | **Date** | The date and time the batch was processed in ShipEngine | [readonly] 
**status** | [**BatchStatus**](BatchStatus.md) |  | [readonly] 
**warnings** | **Number** | The number of warnings that occurred while generating the batch | [readonly] 


