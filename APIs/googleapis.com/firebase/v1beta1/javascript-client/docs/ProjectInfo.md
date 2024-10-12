# FirebaseManagementApi.ProjectInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The user-assigned display name of the GCP &#x60;Project&#x60;, for example: &#x60;My App&#x60; | [optional] 
**locationId** | **String** | The ID of the Project&#39;s default GCP resource location. The location is one of the available [GCP resource locations](https://firebase.google.com/docs/projects/locations). Not all Projects will have this field populated. If it is not populated, it means that the Project does not yet have a default GCP resource location. To set a Project&#39;s default GCP resource location, call [&#x60;FinalizeDefaultLocation&#x60;](../projects.defaultLocation/finalize) after you add Firebase resources to the Project. | [optional] 
**project** | **String** | The resource name of the GCP &#x60;Project&#x60; to which Firebase resources can be added, in the format: projects/PROJECT_IDENTIFIER Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. | [optional] 


