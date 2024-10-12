# FirebaseHostingApi.CloneVersionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | [**PathFilter**](PathFilter.md) |  | [optional] 
**finalize** | **Boolean** | If true, the call to &#x60;CloneVersion&#x60; immediately finalizes the version after cloning is complete. If false, the cloned version will have a status of &#x60;CREATED&#x60;. Use [&#x60;UpdateVersion&#x60;](patch) to set the status of the version to &#x60;FINALIZED&#x60;. | [optional] 
**include** | [**PathFilter**](PathFilter.md) |  | [optional] 
**sourceVersion** | **String** | Required. The unique identifier for the version to be cloned, in the format: sites/SITE_ID/versions/VERSION_ID | [optional] 


