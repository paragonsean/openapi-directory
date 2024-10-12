# ConnectorsApi.Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pathTemplate** | **String** | Template to uniquely represent a Google Cloud resource in a format IAM expects This is a template that can have references to other values provided in the config variable template. | [optional] 
**type** | **String** | Different types of resource supported. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `GCP_PROJECT` (value: `"GCP_PROJECT"`)

* `GCP_RESOURCE` (value: `"GCP_RESOURCE"`)

* `GCP_SECRETMANAGER_SECRET` (value: `"GCP_SECRETMANAGER_SECRET"`)

* `GCP_SECRETMANAGER_SECRET_VERSION` (value: `"GCP_SECRETMANAGER_SECRET_VERSION"`)




