# RudderApi.Datasource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the goal of the data source to create. | [optional] 
**enabled** | **Boolean** | Enable or disable data source. | [optional] 
**id** | **String** | Unique identifier of the data source to create. | [optional] 
**name** | **String** | The human readable name of the data source to create. | [optional] 
**runParameters** | [**DatasourceRunParameters**](DatasourceRunParameters.md) |  | [optional] 
**type** | [**DatasourceType**](DatasourceType.md) |  | [optional] 
**updateTimeout** | **Number** | Duration in seconds before aborting data source update. The main goal is to prevent never ending requests. If a periodicity if configured, you should set that timeout at a lower value. | [optional] 


