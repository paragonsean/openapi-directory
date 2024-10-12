

# Resource

Resource definition

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pathTemplate** | **String** | Template to uniquely represent a Google Cloud resource in a format IAM expects This is a template that can have references to other values provided in the config variable template. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Different types of resource supported. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| GCP_PROJECT | &quot;GCP_PROJECT&quot; |
| GCP_RESOURCE | &quot;GCP_RESOURCE&quot; |
| GCP_SECRETMANAGER_SECRET | &quot;GCP_SECRETMANAGER_SECRET&quot; |
| GCP_SECRETMANAGER_SECRET_VERSION | &quot;GCP_SECRETMANAGER_SECRET_VERSION&quot; |



