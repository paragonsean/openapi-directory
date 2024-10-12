# ArtifactRegistryApi.Repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cleanupPolicies** | [**{String: CleanupPolicy}**](CleanupPolicy.md) | Optional. Cleanup policies for this repository. Cleanup policies indicate when certain package versions can be automatically deleted. Map keys are policy IDs supplied by users during policy creation. They must unique within a repository and be under 128 characters in length. | [optional] 
**cleanupPolicyDryRun** | **Boolean** | Optional. If true, the cleanup pipeline is prevented from deleting versions in this repository. | [optional] 
**createTime** | **String** | Output only. The time when the repository was created. | [optional] [readonly] 
**description** | **String** | The user-provided description of the repository. | [optional] 
**disallowUnspecifiedMode** | **Boolean** | Optional. If this is true, aunspecified repo type will be treated as error. Is used for new repo types that don&#39;t have any specific fields. Right now is used by AOSS team when creating repos for customers. | [optional] 
**dockerConfig** | [**DockerRepositoryConfig**](DockerRepositoryConfig.md) |  | [optional] 
**format** | **String** | Optional. The format of packages that are stored in the repository. | [optional] 
**kmsKeyName** | **String** | The Cloud KMS resource name of the customer managed encryption key that&#39;s used to encrypt the contents of the Repository. Has the form: &#x60;projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key&#x60;. This value may not be changed after the Repository has been created. | [optional] 
**labels** | **{String: String}** | Labels with user-defined metadata. This field may contain up to 64 entries. Label keys and values may be no longer than 63 characters. Label keys must begin with a lowercase letter and may only contain lowercase letters, numeric characters, underscores, and dashes. | [optional] 
**mavenConfig** | [**MavenRepositoryConfig**](MavenRepositoryConfig.md) |  | [optional] 
**mode** | **String** | Optional. The mode of the repository. | [optional] 
**name** | **String** | The name of the repository, for example: &#x60;projects/p1/locations/us-central1/repositories/repo1&#x60;. | [optional] 
**remoteRepositoryConfig** | [**RemoteRepositoryConfig**](RemoteRepositoryConfig.md) |  | [optional] 
**satisfiesPzs** | **Boolean** | Output only. If set, the repository satisfies physical zone separation. | [optional] [readonly] 
**sizeBytes** | **String** | Output only. The size, in bytes, of all artifact storage in this repository. Repositories that are generally available or in public preview use this to calculate storage costs. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the repository was last updated. | [optional] [readonly] 
**virtualRepositoryConfig** | [**VirtualRepositoryConfig**](VirtualRepositoryConfig.md) |  | [optional] 



## Enum: FormatEnum


* `FORMAT_UNSPECIFIED` (value: `"FORMAT_UNSPECIFIED"`)

* `DOCKER` (value: `"DOCKER"`)

* `MAVEN` (value: `"MAVEN"`)

* `NPM` (value: `"NPM"`)

* `APT` (value: `"APT"`)

* `YUM` (value: `"YUM"`)

* `GOOGET` (value: `"GOOGET"`)

* `PYTHON` (value: `"PYTHON"`)

* `KFP` (value: `"KFP"`)

* `GO` (value: `"GO"`)





## Enum: ModeEnum


* `MODE_UNSPECIFIED` (value: `"MODE_UNSPECIFIED"`)

* `STANDARD_REPOSITORY` (value: `"STANDARD_REPOSITORY"`)

* `VIRTUAL_REPOSITORY` (value: `"VIRTUAL_REPOSITORY"`)

* `REMOTE_REPOSITORY` (value: `"REMOTE_REPOSITORY"`)




