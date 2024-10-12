# ArtifactRegistryApi.MavenArtifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactId** | **String** | Artifact ID for the artifact. | [optional] 
**createTime** | **String** | Output only. Time the artifact was created. | [optional] [readonly] 
**groupId** | **String** | Group ID for the artifact. Example: com.google.guava | [optional] 
**name** | **String** | Required. registry_location, project_id, repository_name and maven_artifact forms a unique artifact For example, \&quot;projects/test-project/locations/us-west4/repositories/test-repo/mavenArtifacts/ com.google.guava:guava:31.0-jre\&quot;, where \&quot;us-west4\&quot; is the registry_location, \&quot;test-project\&quot; is the project_id, \&quot;test-repo\&quot; is the repository_name and \&quot;com.google.guava:guava:31.0-jre\&quot; is the maven artifact. | [optional] 
**pomUri** | **String** | Required. URL to access the pom file of the artifact. Example: us-west4-maven.pkg.dev/test-project/test-repo/com/google/guava/guava/31.0/guava-31.0.pom | [optional] 
**updateTime** | **String** | Output only. Time the artifact was updated. | [optional] [readonly] 
**version** | **String** | Version of this artifact. | [optional] 


