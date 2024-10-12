

# ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifact

A Maven artifact to upload to Artifact Registry upon successful completion of all build steps.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifactId** | **String** | Maven &#x60;artifactId&#x60; value used when uploading the artifact to Artifact Registry. |  [optional] |
|**groupId** | **String** | Maven &#x60;groupId&#x60; value used when uploading the artifact to Artifact Registry. |  [optional] |
|**path** | **String** | Path to an artifact in the build&#39;s workspace to be uploaded to Artifact Registry. This can be either an absolute path, e.g. /workspace/my-app/target/my-app-1.0.SNAPSHOT.jar or a relative path from /workspace, e.g. my-app/target/my-app-1.0.SNAPSHOT.jar. |  [optional] |
|**repository** | **String** | Artifact Registry repository, in the form \&quot;https://$REGION-maven.pkg.dev/$PROJECT/$REPOSITORY\&quot; Artifact in the workspace specified by path will be uploaded to Artifact Registry with this location as a prefix. |  [optional] |
|**version** | **String** | Maven &#x60;version&#x60; value used when uploading the artifact to Artifact Registry. |  [optional] |



