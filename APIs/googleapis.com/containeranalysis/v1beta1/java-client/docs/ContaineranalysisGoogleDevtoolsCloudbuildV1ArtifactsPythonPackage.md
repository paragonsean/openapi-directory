

# ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackage

Python package to upload to Artifact Registry upon successful completion of all build steps. A package can encapsulate multiple objects to be uploaded to a single repository.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**paths** | **List&lt;String&gt;** | Path globs used to match files in the build&#39;s workspace. For Python/ Twine, this is usually &#x60;dist/_*&#x60;, and sometimes additionally an &#x60;.asc&#x60; file. |  [optional] |
|**repository** | **String** | Artifact Registry repository, in the form \&quot;https://$REGION-python.pkg.dev/$PROJECT/$REPOSITORY\&quot; Files in the workspace matching any path pattern will be uploaded to Artifact Registry with this location as a prefix. |  [optional] |



