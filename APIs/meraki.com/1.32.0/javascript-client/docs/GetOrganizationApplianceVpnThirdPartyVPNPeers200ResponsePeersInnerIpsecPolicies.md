# MerakiDashboardApi.GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**childAuthAlgo** | **[String]** | This is the authentication algorithms to be used in Phase 2. The value should be an array with one of the following algorithms: &#39;sha256&#39;, &#39;sha1&#39;, &#39;md5&#39; | [optional] 
**childCipherAlgo** | **[String]** | This is the cipher algorithms to be used in Phase 2. The value should be an array with one or more of the following algorithms: &#39;aes256&#39;, &#39;aes192&#39;, &#39;aes128&#39;, &#39;tripledes&#39;, &#39;des&#39;, &#39;null&#39; | [optional] 
**childLifetime** | **Number** | The lifetime of the Phase 2 SA in seconds. | [optional] 
**childPfsGroup** | **[String]** | This is the Diffie-Hellman group to be used for Perfect Forward Secrecy in Phase 2. The value should be an array with one of the following values: &#39;disabled&#39;,&#39;group14&#39;, &#39;group5&#39;, &#39;group2&#39;, &#39;group1&#39; | [optional] 
**ikeAuthAlgo** | **[String]** | This is the authentication algorithm to be used in Phase 1. The value should be an array with one of the following algorithms: &#39;sha256&#39;, &#39;sha1&#39;, &#39;md5&#39; | [optional] 
**ikeCipherAlgo** | **[String]** | This is the cipher algorithm to be used in Phase 1. The value should be an array with one of the following algorithms: &#39;aes256&#39;, &#39;aes192&#39;, &#39;aes128&#39;, &#39;tripledes&#39;, &#39;des&#39; | [optional] 
**ikeDiffieHellmanGroup** | **[String]** | This is the Diffie-Hellman group to be used in Phase 1. The value should be an array with one of the following algorithms: &#39;group14&#39;, &#39;group5&#39;, &#39;group2&#39;, &#39;group1&#39; | [optional] 
**ikeLifetime** | **Number** | The lifetime of the Phase 1 SA in seconds. | [optional] 
**ikePrfAlgo** | **[String]** | [optional] This is the pseudo-random function to be used in IKE_SA. The value should be an array with one of the following algorithms: &#39;prfsha256&#39;, &#39;prfsha1&#39;, &#39;prfmd5&#39;, &#39;default&#39;. The &#39;default&#39; option can be used to default to the Authentication algorithm. | [optional] 



## Enum: [ChildAuthAlgoEnum]


* `md5` (value: `"md5"`)

* `sha1` (value: `"sha1"`)

* `sha256` (value: `"sha256"`)





## Enum: [ChildCipherAlgoEnum]


* `aes128` (value: `"aes128"`)

* `aes192` (value: `"aes192"`)

* `aes256` (value: `"aes256"`)

* `des` (value: `"des"`)

* `null` (value: `"null"`)

* `tripledes` (value: `"tripledes"`)





## Enum: [IkeAuthAlgoEnum]


* `md5` (value: `"md5"`)

* `sha1` (value: `"sha1"`)

* `sha256` (value: `"sha256"`)





## Enum: [IkeCipherAlgoEnum]


* `aes128` (value: `"aes128"`)

* `aes192` (value: `"aes192"`)

* `aes256` (value: `"aes256"`)

* `des` (value: `"des"`)

* `tripledes` (value: `"tripledes"`)





## Enum: [IkePrfAlgoEnum]


* `default` (value: `"default"`)

* `prfmd5` (value: `"prfmd5"`)

* `prfsha1` (value: `"prfsha1"`)

* `prfsha256` (value: `"prfsha256"`)




