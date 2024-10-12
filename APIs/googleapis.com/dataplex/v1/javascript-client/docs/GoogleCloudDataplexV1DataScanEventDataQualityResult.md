# CloudDataplexApi.GoogleCloudDataplexV1DataScanEventDataQualityResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columnScore** | **{String: Number}** | The score of each column scanned in the data scan job. The key of the map is the name of the column. The value is the data quality score for the column.The score ranges between 0, 100 (up to two decimal points). | [optional] 
**dimensionPassed** | **{String: Boolean}** | The result of each dimension for data quality result. The key of the map is the name of the dimension. The value is the bool value depicting whether the dimension result was pass or not. | [optional] 
**dimensionScore** | **{String: Number}** | The score of each dimension for data quality result. The key of the map is the name of the dimension. The value is the data quality score for the dimension.The score ranges between 0, 100 (up to two decimal points). | [optional] 
**passed** | **Boolean** | Whether the data quality result was pass or not. | [optional] 
**rowCount** | **String** | The count of rows processed in the data scan job. | [optional] 
**score** | **Number** | The table-level data quality score for the data scan job.The data quality score ranges between 0, 100 (up to two decimal points). | [optional] 


