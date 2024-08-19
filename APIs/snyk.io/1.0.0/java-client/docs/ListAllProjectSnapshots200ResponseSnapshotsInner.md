

# ListAllProjectSnapshots200ResponseSnapshotsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **String** | The date that the snapshot was taken |  |
|**id** | **String** | The snapshot identifier |  |
|**imageBaseImage** | **String** |  |  [optional] |
|**imageId** | **String** |  |  [optional] |
|**imagePlatform** | **String** |  |  [optional] |
|**imageTag** | **String** |  |  [optional] |
|**issueCounts** | [**ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCounts**](ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCounts.md) |  |  |
|**method** | [**MethodEnum**](#MethodEnum) | The method by which this snapshot was created. |  [optional] |
|**totalDependencies** | **BigDecimal** | Number of dependencies of the project |  |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| API | &quot;api&quot; |
| CLI | &quot;cli&quot; |
| RECURRING | &quot;recurring&quot; |
| WEB | &quot;web&quot; |
| WEB_TEST | &quot;web-test&quot; |
| WIZARD | &quot;wizard&quot; |



