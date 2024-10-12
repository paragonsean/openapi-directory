

# GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies

Custom IPSec policies for the VPN peer. If not included and a preset has not been chosen, the default preset for IPSec policies will be used.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**childAuthAlgo** | [**List&lt;ChildAuthAlgoEnum&gt;**](#List&lt;ChildAuthAlgoEnum&gt;) | This is the authentication algorithms to be used in Phase 2. The value should be an array with one of the following algorithms: &#39;sha256&#39;, &#39;sha1&#39;, &#39;md5&#39; |  [optional] |
|**childCipherAlgo** | [**List&lt;ChildCipherAlgoEnum&gt;**](#List&lt;ChildCipherAlgoEnum&gt;) | This is the cipher algorithms to be used in Phase 2. The value should be an array with one or more of the following algorithms: &#39;aes256&#39;, &#39;aes192&#39;, &#39;aes128&#39;, &#39;tripledes&#39;, &#39;des&#39;, &#39;null&#39; |  [optional] |
|**childLifetime** | **Integer** | The lifetime of the Phase 2 SA in seconds. |  [optional] |
|**childPfsGroup** | **List&lt;String&gt;** | This is the Diffie-Hellman group to be used for Perfect Forward Secrecy in Phase 2. The value should be an array with one of the following values: &#39;disabled&#39;,&#39;group14&#39;, &#39;group5&#39;, &#39;group2&#39;, &#39;group1&#39; |  [optional] |
|**ikeAuthAlgo** | [**List&lt;IkeAuthAlgoEnum&gt;**](#List&lt;IkeAuthAlgoEnum&gt;) | This is the authentication algorithm to be used in Phase 1. The value should be an array with one of the following algorithms: &#39;sha256&#39;, &#39;sha1&#39;, &#39;md5&#39; |  [optional] |
|**ikeCipherAlgo** | [**List&lt;IkeCipherAlgoEnum&gt;**](#List&lt;IkeCipherAlgoEnum&gt;) | This is the cipher algorithm to be used in Phase 1. The value should be an array with one of the following algorithms: &#39;aes256&#39;, &#39;aes192&#39;, &#39;aes128&#39;, &#39;tripledes&#39;, &#39;des&#39; |  [optional] |
|**ikeDiffieHellmanGroup** | **List&lt;String&gt;** | This is the Diffie-Hellman group to be used in Phase 1. The value should be an array with one of the following algorithms: &#39;group14&#39;, &#39;group5&#39;, &#39;group2&#39;, &#39;group1&#39; |  [optional] |
|**ikeLifetime** | **Integer** | The lifetime of the Phase 1 SA in seconds. |  [optional] |
|**ikePrfAlgo** | [**List&lt;IkePrfAlgoEnum&gt;**](#List&lt;IkePrfAlgoEnum&gt;) | [optional] This is the pseudo-random function to be used in IKE_SA. The value should be an array with one of the following algorithms: &#39;prfsha256&#39;, &#39;prfsha1&#39;, &#39;prfmd5&#39;, &#39;default&#39;. The &#39;default&#39; option can be used to default to the Authentication algorithm. |  [optional] |



## Enum: List&lt;ChildAuthAlgoEnum&gt;

| Name | Value |
|---- | -----|
| MD5 | &quot;md5&quot; |
| SHA1 | &quot;sha1&quot; |
| SHA256 | &quot;sha256&quot; |



## Enum: List&lt;ChildCipherAlgoEnum&gt;

| Name | Value |
|---- | -----|
| AES128 | &quot;aes128&quot; |
| AES192 | &quot;aes192&quot; |
| AES256 | &quot;aes256&quot; |
| DES | &quot;des&quot; |
| NULL | &quot;null&quot; |
| TRIPLEDES | &quot;tripledes&quot; |



## Enum: List&lt;IkeAuthAlgoEnum&gt;

| Name | Value |
|---- | -----|
| MD5 | &quot;md5&quot; |
| SHA1 | &quot;sha1&quot; |
| SHA256 | &quot;sha256&quot; |



## Enum: List&lt;IkeCipherAlgoEnum&gt;

| Name | Value |
|---- | -----|
| AES128 | &quot;aes128&quot; |
| AES192 | &quot;aes192&quot; |
| AES256 | &quot;aes256&quot; |
| DES | &quot;des&quot; |
| TRIPLEDES | &quot;tripledes&quot; |



## Enum: List&lt;IkePrfAlgoEnum&gt;

| Name | Value |
|---- | -----|
| DEFAULT | &quot;default&quot; |
| PRFMD5 | &quot;prfmd5&quot; |
| PRFSHA1 | &quot;prfsha1&quot; |
| PRFSHA256 | &quot;prfsha256&quot; |



