# ContainerAnalysisApi.ContaineranalysisGoogleDevtoolsCloudbuildV1Results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactManifest** | **String** | Path to the artifact manifest for non-container artifacts uploaded to Cloud Storage. Only populated when artifacts are uploaded to Cloud Storage. | [optional] 
**artifactTiming** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan**](ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan.md) |  | [optional] 
**buildStepImages** | **[String]** | List of build step digests, in the order corresponding to build step indices. | [optional] 
**buildStepOutputs** | **[Blob]** | List of build step outputs, produced by builder images, in the order corresponding to build step indices. [Cloud Builders](https://cloud.google.com/cloud-build/docs/cloud-builders) can produce this output by writing to &#x60;$BUILDER_OUTPUT/output&#x60;. Only the first 50KB of data is stored. | [optional] 
**images** | [**[ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImage]**](ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImage.md) | Container images that were built as a part of the build. | [optional] 
**mavenArtifacts** | [**[ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifact]**](ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifact.md) | Maven artifacts uploaded to Artifact Registry at the end of the build. | [optional] 
**npmPackages** | [**[ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackage]**](ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackage.md) | Npm packages uploaded to Artifact Registry at the end of the build. | [optional] 
**numArtifacts** | **String** | Number of non-container artifacts uploaded to Cloud Storage. Only populated when artifacts are uploaded to Cloud Storage. | [optional] 
**pythonPackages** | [**[ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackage]**](ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackage.md) | Python artifacts uploaded to Artifact Registry at the end of the build. | [optional] 


