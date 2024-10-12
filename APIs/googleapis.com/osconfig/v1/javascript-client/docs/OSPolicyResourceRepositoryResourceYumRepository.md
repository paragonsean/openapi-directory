# OsConfigApi.OSPolicyResourceRepositoryResourceYumRepository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseUrl** | **String** | Required. The location of the repository directory. | [optional] 
**displayName** | **String** | The display name of the repository. | [optional] 
**gpgKeys** | **[String]** | URIs of GPG keys. | [optional] 
**id** | **String** | Required. A one word, unique name for this repository. This is the &#x60;repo id&#x60; in the yum config file and also the &#x60;display_name&#x60; if &#x60;display_name&#x60; is omitted. This id is also used as the unique identifier when checking for resource conflicts. | [optional] 


