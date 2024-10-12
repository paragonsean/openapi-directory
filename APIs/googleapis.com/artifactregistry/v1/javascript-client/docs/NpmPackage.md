# ArtifactRegistryApi.NpmPackage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Time the package was created. | [optional] [readonly] 
**name** | **String** | Required. registry_location, project_id, repository_name and npm_package forms a unique package For example, \&quot;projects/test-project/locations/us-west4/repositories/test-repo/npmPackages/ npm_test:1.0.0\&quot;, where \&quot;us-west4\&quot; is the registry_location, \&quot;test-project\&quot; is the project_id, \&quot;test-repo\&quot; is the repository_name and npm_test:1.0.0\&quot; is the npm package. | [optional] 
**packageName** | **String** | Package for the artifact. | [optional] 
**tags** | **[String]** | Tags attached to this package. | [optional] 
**updateTime** | **String** | Output only. Time the package was updated. | [optional] [readonly] 
**version** | **String** | Version of this package. | [optional] 


