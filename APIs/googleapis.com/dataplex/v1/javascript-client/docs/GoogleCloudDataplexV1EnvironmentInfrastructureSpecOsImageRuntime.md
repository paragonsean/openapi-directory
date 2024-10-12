# CloudDataplexApi.GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntime

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imageVersion** | **String** | Required. Dataplex Image version. | [optional] 
**javaLibraries** | **[String]** | Optional. List of Java jars to be included in the runtime environment. Valid input includes Cloud Storage URIs to Jar binaries. For example, gs://bucket-name/my/path/to/file.jar | [optional] 
**properties** | **{String: String}** | Optional. Spark properties to provide configuration for use in sessions created for this environment. The properties to set on daemon config files. Property keys are specified in prefix:property format. The prefix must be \&quot;spark\&quot;. | [optional] 
**pythonPackages** | **[String]** | Optional. A list of python packages to be installed. Valid formats include Cloud Storage URI to a PIP installable library. For example, gs://bucket-name/my/path/to/lib.tar.gz | [optional] 


