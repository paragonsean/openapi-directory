

# ContaineranalysisGoogleDevtoolsCloudbuildV1Results

Artifacts created by the build pipeline.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifactManifest** | **String** | Path to the artifact manifest for non-container artifacts uploaded to Cloud Storage. Only populated when artifacts are uploaded to Cloud Storage. |  [optional] |
|**artifactTiming** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan**](ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan.md) |  |  [optional] |
|**buildStepImages** | **List&lt;String&gt;** | List of build step digests, in the order corresponding to build step indices. |  [optional] |
|**buildStepOutputs** | **List&lt;byte[]&gt;** | List of build step outputs, produced by builder images, in the order corresponding to build step indices. [Cloud Builders](https://cloud.google.com/cloud-build/docs/cloud-builders) can produce this output by writing to &#x60;$BUILDER_OUTPUT/output&#x60;. Only the first 50KB of data is stored. |  [optional] |
|**images** | [**List&lt;ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImage&gt;**](ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImage.md) | Container images that were built as a part of the build. |  [optional] |
|**mavenArtifacts** | [**List&lt;ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifact&gt;**](ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifact.md) | Maven artifacts uploaded to Artifact Registry at the end of the build. |  [optional] |
|**npmPackages** | [**List&lt;ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackage&gt;**](ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackage.md) | Npm packages uploaded to Artifact Registry at the end of the build. |  [optional] |
|**numArtifacts** | **String** | Number of non-container artifacts uploaded to Cloud Storage. Only populated when artifacts are uploaded to Cloud Storage. |  [optional] |
|**pythonPackages** | [**List&lt;ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackage&gt;**](ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackage.md) | Python artifacts uploaded to Artifact Registry at the end of the build. |  [optional] |



