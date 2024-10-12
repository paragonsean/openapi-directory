

# PackageData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**architecture** | **String** | The architecture of the package. |  [optional] |
|**binarySourceInfo** | [**List&lt;BinarySourceInfo&gt;**](BinarySourceInfo.md) | A bundle containing the binary and source information. |  [optional] |
|**binaryVersion** | [**PackageVersion**](PackageVersion.md) |  |  [optional] |
|**cpeUri** | **String** | The cpe_uri in [cpe format] (https://cpe.mitre.org/specification/) in which the vulnerability may manifest. Examples include distro or storage location for vulnerable jar. |  [optional] |
|**dependencyChain** | [**List&lt;LanguagePackageDependency&gt;**](LanguagePackageDependency.md) | The dependency chain between this package and the user&#39;s artifact. List in order from the customer&#39;s package under review first, to the current package last. Inclusive of the original package and the current package. |  [optional] |
|**fileLocation** | [**List&lt;FileLocation&gt;**](FileLocation.md) | The path to the jar file / go binary file. |  [optional] |
|**hashDigest** | **String** | HashDigest stores the SHA512 hash digest of the jar file if the package is of type Maven. This field will be unset for non Maven packages. |  [optional] |
|**licenses** | **List&lt;String&gt;** | The list of licenses found that are related to a given package. Note that licenses may also be stored on the BinarySourceInfo. If there is no BinarySourceInfo (because there&#39;s no concept of source vs binary), then it will be stored here, while if there are BinarySourceInfos, it will be stored there, as one source can have multiple binaries with different licenses. |  [optional] |
|**maintainer** | [**Maintainer**](Maintainer.md) |  |  [optional] |
|**os** | **String** | The OS affected by a vulnerability Used to generate the cpe_uri for OS packages |  [optional] |
|**osVersion** | **String** | The version of the OS Used to generate the cpe_uri for OS packages |  [optional] |
|**_package** | **String** | The package being analysed for vulnerabilities |  [optional] |
|**packageType** | [**PackageTypeEnum**](#PackageTypeEnum) | The type of package: os, maven, go, etc. |  [optional] |
|**patchedCve** | **List&lt;String&gt;** | CVEs that this package is no longer vulnerable to go/drydock-dd-custom-binary-scanning |  [optional] |
|**sourceVersion** | [**PackageVersion**](PackageVersion.md) |  |  [optional] |
|**unused** | **String** |  |  [optional] |
|**version** | **String** | The version of the package being analysed |  [optional] |



## Enum: PackageTypeEnum

| Name | Value |
|---- | -----|
| PACKAGE_TYPE_UNSPECIFIED | &quot;PACKAGE_TYPE_UNSPECIFIED&quot; |
| OS | &quot;OS&quot; |
| MAVEN | &quot;MAVEN&quot; |
| GO | &quot;GO&quot; |
| GO_STDLIB | &quot;GO_STDLIB&quot; |
| PYPI | &quot;PYPI&quot; |
| NPM | &quot;NPM&quot; |
| NUGET | &quot;NUGET&quot; |
| RUBYGEMS | &quot;RUBYGEMS&quot; |
| RUST | &quot;RUST&quot; |
| COMPOSER | &quot;COMPOSER&quot; |



