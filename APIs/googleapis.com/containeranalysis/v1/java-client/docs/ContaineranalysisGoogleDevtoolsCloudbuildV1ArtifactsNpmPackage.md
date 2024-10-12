

# ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackage

Npm package to upload to Artifact Registry upon successful completion of all build steps.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**packagePath** | **String** | Path to the package.json. e.g. workspace/path/to/package |  [optional] |
|**repository** | **String** | Artifact Registry repository, in the form \&quot;https://$REGION-npm.pkg.dev/$PROJECT/$REPOSITORY\&quot; Npm package in the workspace specified by path will be zipped and uploaded to Artifact Registry with this location as a prefix. |  [optional] |



