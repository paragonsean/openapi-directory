# ContainerAnalysisApi.ContaineranalysisGoogleDevtoolsCloudbuildV1Artifacts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | **[String]** | A list of images to be pushed upon the successful completion of all build steps. The images will be pushed using the builder service account&#39;s credentials. The digests of the pushed images will be stored in the Build resource&#39;s results field. If any of the images fail to be pushed, the build is marked FAILURE. | [optional] 
**mavenArtifacts** | [**[ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifact]**](ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifact.md) | A list of Maven artifacts to be uploaded to Artifact Registry upon successful completion of all build steps. Artifacts in the workspace matching specified paths globs will be uploaded to the specified Artifact Registry repository using the builder service account&#39;s credentials. If any artifacts fail to be pushed, the build is marked FAILURE. | [optional] 
**npmPackages** | [**[ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackage]**](ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackage.md) | A list of npm packages to be uploaded to Artifact Registry upon successful completion of all build steps. Npm packages in the specified paths will be uploaded to the specified Artifact Registry repository using the builder service account&#39;s credentials. If any packages fail to be pushed, the build is marked FAILURE. | [optional] 
**objects** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjects**](ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjects.md) |  | [optional] 
**pythonPackages** | [**[ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackage]**](ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackage.md) | A list of Python packages to be uploaded to Artifact Registry upon successful completion of all build steps. The build service account credentials will be used to perform the upload. If any objects fail to be pushed, the build is marked FAILURE. | [optional] 


