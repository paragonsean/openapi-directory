# OsConfigApi.OSPolicyResourcePackageResourceDeb

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pullDeps** | **Boolean** | Whether dependencies should also be installed. - install when false: &#x60;dpkg -i package&#x60; - install when true: &#x60;apt-get update &amp;&amp; apt-get -y install package.deb&#x60; | [optional] 
**source** | [**OSPolicyResourceFile**](OSPolicyResourceFile.md) |  | [optional] 


