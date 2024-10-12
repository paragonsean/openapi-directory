# ServiceControlApi.ConsumerInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerNumber** | **String** | The consumer identity number, can be Google cloud project number, folder number or organization number e.g. 1234567890. A value of 0 indicates no consumer number is found. | [optional] 
**projectNumber** | **String** | The Google cloud project number, e.g. 1234567890. A value of 0 indicates no project number is found. NOTE: This field is deprecated after Chemist support flexible consumer id. New code should not depend on this field anymore. | [optional] 
**type** | **String** | The type of the consumer which should have been defined in [Google Resource Manager](https://cloud.google.com/resource-manager/). | [optional] 



## Enum: TypeEnum


* `CONSUMER_TYPE_UNSPECIFIED` (value: `"CONSUMER_TYPE_UNSPECIFIED"`)

* `PROJECT` (value: `"PROJECT"`)

* `FOLDER` (value: `"FOLDER"`)

* `ORGANIZATION` (value: `"ORGANIZATION"`)

* `SERVICE_SPECIFIC` (value: `"SERVICE_SPECIFIC"`)




