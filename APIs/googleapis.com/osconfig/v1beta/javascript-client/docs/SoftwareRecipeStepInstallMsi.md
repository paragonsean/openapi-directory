# OsConfigApi.SoftwareRecipeStepInstallMsi

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedExitCodes** | **[Number]** | Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0] | [optional] 
**artifactId** | **String** | Required. The id of the relevant artifact in the recipe. | [optional] 
**flags** | **[String]** | The flags to use when installing the MSI defaults to [\&quot;/i\&quot;] (i.e. the install flag). | [optional] 


