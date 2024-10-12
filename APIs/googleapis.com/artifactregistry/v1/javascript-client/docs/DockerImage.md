# ArtifactRegistryApi.DockerImage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buildTime** | **String** | The time this image was built. This field is returned as the &#39;metadata.buildTime&#39; field in the Version resource. The build time is returned to the client as an RFC 3339 string, which can be easily used with the JavaScript Date constructor. | [optional] 
**imageSizeBytes** | **String** | Calculated size of the image. This field is returned as the &#39;metadata.imageSizeBytes&#39; field in the Version resource. | [optional] 
**mediaType** | **String** | Media type of this image, e.g. \&quot;application/vnd.docker.distribution.manifest.v2+json\&quot;. This field is returned as the &#39;metadata.mediaType&#39; field in the Version resource. | [optional] 
**name** | **String** | Required. registry_location, project_id, repository_name and image id forms a unique image name:&#x60;projects//locations//repository//dockerImages/&#x60;. For example, \&quot;projects/test-project/locations/us-west4/repositories/test-repo/dockerImages/ nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf\&quot;, where \&quot;us-west4\&quot; is the registry_location, \&quot;test-project\&quot; is the project_id, \&quot;test-repo\&quot; is the repository_name and \&quot;nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf\&quot; is the image&#39;s digest. | [optional] 
**tags** | **[String]** | Tags attached to this image. | [optional] 
**updateTime** | **String** | Output only. The time when the docker image was last updated. | [optional] [readonly] 
**uploadTime** | **String** | Time the image was uploaded. | [optional] 
**uri** | **String** | Required. URL to access the image. Example: us-west4-docker.pkg.dev/test-project/test-repo/nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf | [optional] 


