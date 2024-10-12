# CloudFunctionsApi.SecretVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **String** | Relative path of the file under the mount path where the secret value for this version will be fetched and made available. For example, setting the mount_path as &#39;/etc/secrets&#39; and path as &#x60;secret_foo&#x60; would mount the secret value file at &#x60;/etc/secrets/secret_foo&#x60;. | [optional] 
**version** | **String** | Version of the secret (version number or the string &#39;latest&#39;). It is preferable to use &#x60;latest&#x60; version with secret volumes as secret value changes are reflected immediately. | [optional] 


