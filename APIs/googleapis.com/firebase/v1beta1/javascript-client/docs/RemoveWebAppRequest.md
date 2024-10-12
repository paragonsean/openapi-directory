# FirebaseManagementApi.RemoveWebAppRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowMissing** | **Boolean** | If set to true, and the App is not found, the request will succeed but no action will be taken on the server. | [optional] 
**etag** | **String** | Checksum provided in the WebApp resource. If provided, this checksum ensures that the client has an up-to-date value before proceeding. | [optional] 
**immediate** | **Boolean** | Determines whether to _immediately_ delete the WebApp. If set to true, the App is immediately deleted from the Project and cannot be restored to the Project. If not set, defaults to false, which means the App will be set to expire in 30 days. Within the 30 days, the App may be restored to the Project using UndeleteWebApp | [optional] 
**validateOnly** | **Boolean** | If set to true, the request is only validated. The App will _not_ be removed. | [optional] 


