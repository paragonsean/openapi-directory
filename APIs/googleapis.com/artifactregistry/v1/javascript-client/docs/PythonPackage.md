# ArtifactRegistryApi.PythonPackage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Time the package was created. | [optional] [readonly] 
**name** | **String** | Required. registry_location, project_id, repository_name and python_package forms a unique package name:&#x60;projects//locations//repository//pythonPackages/&#x60;. For example, \&quot;projects/test-project/locations/us-west4/repositories/test-repo/pythonPackages/ python_package:1.0.0\&quot;, where \&quot;us-west4\&quot; is the registry_location, \&quot;test-project\&quot; is the project_id, \&quot;test-repo\&quot; is the repository_name and python_package:1.0.0\&quot; is the python package. | [optional] 
**packageName** | **String** | Package for the artifact. | [optional] 
**updateTime** | **String** | Output only. Time the package was updated. | [optional] [readonly] 
**uri** | **String** | Required. URL to access the package. Example: us-west4-python.pkg.dev/test-project/test-repo/python_package/file-name-1.0.0.tar.gz | [optional] 
**version** | **String** | Version of this package. | [optional] 


