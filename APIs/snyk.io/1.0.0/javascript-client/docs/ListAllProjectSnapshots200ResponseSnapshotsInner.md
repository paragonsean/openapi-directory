# SnykApi.ListAllProjectSnapshots200ResponseSnapshotsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **String** | The date that the snapshot was taken | 
**id** | **String** | The snapshot identifier | 
**imageBaseImage** | **String** |  | [optional] 
**imageId** | **String** |  | [optional] 
**imagePlatform** | **String** |  | [optional] 
**imageTag** | **String** |  | [optional] 
**issueCounts** | [**ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCounts**](ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCounts.md) |  | 
**method** | **String** | The method by which this snapshot was created. | [optional] 
**totalDependencies** | **Number** | Number of dependencies of the project | 



## Enum: MethodEnum


* `api` (value: `"api"`)

* `cli` (value: `"cli"`)

* `recurring` (value: `"recurring"`)

* `web` (value: `"web"`)

* `web-test` (value: `"web-test"`)

* `wizard` (value: `"wizard"`)




