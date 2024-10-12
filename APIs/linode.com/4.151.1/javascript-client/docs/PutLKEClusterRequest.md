# LinodeApi.PutLKEClusterRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controlPlane** | [**PutLKEClusterRequestControlPlane**](PutLKEClusterRequestControlPlane.md) |  | [optional] 
**k8sVersion** | **String** | The desired Kubernetes version for this Kubernetes cluster in the format of &amp;lt;major&amp;gt;.&amp;lt;minor&amp;gt;. New and recycled Nodes in this cluster will be installed with the latest available patch for the Cluster&#39;s Kubernetes version.  When upgrading the Kubernetes version, only the next latest minor version following the current version can be deployed. For example, a cluster with Kubernetes version 1.19 can be upgraded to version 1.20, but not directly to 1.21.  The Kubernetes version of a cluster can not be downgraded.  | [optional] 
**label** | **String** | This Kubernetes cluster&#39;s unique label for display purposes only. Labels have the following constraints:    * UTF-8 characters will be returned by the API using escape     sequences of their Unicode code points. For example, the     Japanese character *か* is 3 bytes in UTF-8 (&#x60;0xE382AB&#x60;). Its     Unicode code point is 2 bytes (&#x60;0x30AB&#x60;). APIv4 supports this     character and the API will return it as the escape sequence     using six 1 byte characters which represent 2 bytes of Unicode     code point (&#x60;\&quot;\\u30ab\&quot;&#x60;).   * 4 byte UTF-8 characters are not supported.   * If the label is entirely composed of UTF-8 characters, the API     response will return the code points using up to 193 1 byte     characters.  | [optional] 
**tags** | **[String]** | An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only. To delete a tag, exclude it from your &#x60;tags&#x60; array.  | [optional] 


