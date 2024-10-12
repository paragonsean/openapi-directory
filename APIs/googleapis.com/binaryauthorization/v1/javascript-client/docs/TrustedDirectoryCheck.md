# BinaryAuthorizationApi.TrustedDirectoryCheck

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trustedDirPatterns** | **[String]** | Required. List of trusted directory patterns. A pattern is in the form \&quot;registry/path/to/directory\&quot;. The registry domain part is defined as two or more dot-separated words, e.g., &#x60;us.pkg.dev&#x60;, or &#x60;gcr.io&#x60;. Additionally, &#x60;*&#x60; can be used in three ways as wildcards: 1. leading &#x60;*&#x60; to match varying prefixes in registry subdomain (useful for location prefixes); 2. trailing &#x60;*&#x60; after registry/ to match varying endings; 3. trailing &#x60;**&#x60; after registry/ to match \&quot;/\&quot; as well. For example: -- &#x60;gcr.io/my-project/my-repo&#x60; is valid to match a single directory -- &#x60;*-docker.pkg.dev/my-project/my-repo&#x60; or &#x60;*.gcr.io/my-project&#x60; are valid to match varying prefixes -- &#x60;gcr.io/my-project/_*&#x60; will match all direct directories in &#x60;my-project&#x60; -- &#x60;gcr.io/my-project/_**&#x60; would match all directories in &#x60;my-project&#x60; -- &#x60;gcr.i*&#x60; is not allowed since the registry is not completely specified -- &#x60;sub*domain.gcr.io/nginx&#x60; is not valid because only leading &#x60;*&#x60; or trailing &#x60;*&#x60; are allowed. -- &#x60;*pkg.dev/my-project/my-repo&#x60; is not valid because leading &#x60;*&#x60; can only match subdomain -- &#x60;**-docker.pkg.dev&#x60; is not valid because one leading &#x60;*&#x60; is allowed, and that it cannot match &#x60;/&#x60; | [optional] 


