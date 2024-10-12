# OsConfigApi.OSPolicyResourcePackageResourceRPM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pullDeps** | **Boolean** | Whether dependencies should also be installed. - install when false: &#x60;rpm --upgrade --replacepkgs package.rpm&#x60; - install when true: &#x60;yum -y install package.rpm&#x60; or &#x60;zypper -y install package.rpm&#x60; | [optional] 
**source** | [**OSPolicyResourceFile**](OSPolicyResourceFile.md) |  | [optional] 


