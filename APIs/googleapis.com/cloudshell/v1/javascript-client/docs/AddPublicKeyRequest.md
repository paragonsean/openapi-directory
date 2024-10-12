# CloudShellApi.AddPublicKeyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | Key that should be added to the environment. Supported formats are &#x60;ssh-dss&#x60; (see RFC4253), &#x60;ssh-rsa&#x60; (see RFC4253), &#x60;ecdsa-sha2-nistp256&#x60; (see RFC5656), &#x60;ecdsa-sha2-nistp384&#x60; (see RFC5656) and &#x60;ecdsa-sha2-nistp521&#x60; (see RFC5656). It should be structured as &lt;format&gt; &lt;content&gt;, where &lt;content&gt; part is encoded with Base64. | [optional] 


