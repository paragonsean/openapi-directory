

# DiagnoseClusterRequest

A request to collect cluster diagnostic information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diagnosisInterval** | [**Interval**](Interval.md) |  |  [optional] |
|**job** | **String** | Optional. DEPRECATED Specifies the job on which diagnosis is to be performed. Format: projects/{project}/regions/{region}/jobs/{job} |  [optional] |
|**jobs** | **List&lt;String&gt;** | Optional. Specifies a list of jobs on which diagnosis is to be performed. Format: projects/{project}/regions/{region}/jobs/{job} |  [optional] |
|**tarballAccess** | [**TarballAccessEnum**](#TarballAccessEnum) | Optional. (Optional) The access type to the diagnostic tarball. If not specified, falls back to default access of the bucket |  [optional] |
|**tarballGcsDir** | **String** | Optional. (Optional) The output Cloud Storage directory for the diagnostic tarball. If not specified, a task-specific directory in the cluster&#39;s staging bucket will be used. |  [optional] |
|**yarnApplicationId** | **String** | Optional. DEPRECATED Specifies the yarn application on which diagnosis is to be performed. |  [optional] |
|**yarnApplicationIds** | **List&lt;String&gt;** | Optional. Specifies a list of yarn applications on which diagnosis is to be performed. |  [optional] |



## Enum: TarballAccessEnum

| Name | Value |
|---- | -----|
| TARBALL_ACCESS_UNSPECIFIED | &quot;TARBALL_ACCESS_UNSPECIFIED&quot; |
| GOOGLE_CLOUD_SUPPORT | &quot;GOOGLE_CLOUD_SUPPORT&quot; |
| GOOGLE_DATAPROC_DIAGNOSE | &quot;GOOGLE_DATAPROC_DIAGNOSE&quot; |



