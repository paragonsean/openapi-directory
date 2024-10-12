# CloudDataprocApi.DiagnoseClusterRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diagnosisInterval** | [**Interval**](Interval.md) |  | [optional] 
**job** | **String** | Optional. DEPRECATED Specifies the job on which diagnosis is to be performed. Format: projects/{project}/regions/{region}/jobs/{job} | [optional] 
**jobs** | **[String]** | Optional. Specifies a list of jobs on which diagnosis is to be performed. Format: projects/{project}/regions/{region}/jobs/{job} | [optional] 
**tarballAccess** | **String** | Optional. (Optional) The access type to the diagnostic tarball. If not specified, falls back to default access of the bucket | [optional] 
**tarballGcsDir** | **String** | Optional. (Optional) The output Cloud Storage directory for the diagnostic tarball. If not specified, a task-specific directory in the cluster&#39;s staging bucket will be used. | [optional] 
**yarnApplicationId** | **String** | Optional. DEPRECATED Specifies the yarn application on which diagnosis is to be performed. | [optional] 
**yarnApplicationIds** | **[String]** | Optional. Specifies a list of yarn applications on which diagnosis is to be performed. | [optional] 



## Enum: TarballAccessEnum


* `TARBALL_ACCESS_UNSPECIFIED` (value: `"TARBALL_ACCESS_UNSPECIFIED"`)

* `GOOGLE_CLOUD_SUPPORT` (value: `"GOOGLE_CLOUD_SUPPORT"`)

* `GOOGLE_DATAPROC_DIAGNOSE` (value: `"GOOGLE_DATAPROC_DIAGNOSE"`)




