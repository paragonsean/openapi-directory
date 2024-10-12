

# CreateProjectMetadata

A status object which is used as the `metadata` field for the Operation returned by CreateProject. It provides insight for when significant phases of Project creation have completed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Creation time of the project creation workflow. |  [optional] |
|**gettable** | **Boolean** | True if the project can be retrieved using &#x60;GetProject&#x60;. No other operations on the project are guaranteed to work until the project creation is complete. |  [optional] |
|**ready** | **Boolean** | True if the project creation process is complete. |  [optional] |



