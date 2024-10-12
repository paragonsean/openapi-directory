# TravelImpactModelApi.ModelVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dated** | **String** | Dated versions: Model datasets are recreated with refreshed input data but no change to the algorithms regularly. | [optional] 
**major** | **Number** | Major versions: Major changes to methodology (e.g. adding new data sources to the model that lead to major output changes). Such changes will be infrequent and announced well in advance. Might involve API version changes, which will respect guidelines in https://cloud.google.com/endpoints/docs/openapi/versioning-an-api#backwards-incompatible | [optional] 
**minor** | **Number** | Minor versions: Changes to the model that, while being consistent across schema versions, change the model parameters or implementation. | [optional] 
**patch** | **Number** | Patch versions: Implementation changes meant to address bugs or inaccuracies in the model implementation. | [optional] 


