

# AdmissionWhitelistPattern

An admission allowlist pattern exempts images from checks by admission rules.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**namePattern** | **String** | An image name pattern to allowlist, in the form &#x60;registry/path/to/image&#x60;. This supports a trailing &#x60;*&#x60; as a wildcard, but this is allowed only in text after the &#x60;registry/&#x60; part. &#x60;*&#x60; wildcard does not match &#x60;/&#x60;, i.e., &#x60;gcr.io/nginx*&#x60; matches &#x60;gcr.io/nginx@latest&#x60;, but it does not match &#x60;gcr.io/nginx/image&#x60;. This also supports a trailing &#x60;**&#x60; wildcard which matches subdirectories, i.e., &#x60;gcr.io/nginx**&#x60; matches &#x60;gcr.io/nginx/image&#x60;. |  [optional] |



