# DefaultApi

All URIs are relative to *http://eks.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**associateEncryptionConfig**](DefaultApi.md#associateEncryptionConfig) | **POST** /clusters/{name}/encryption-config/associate |  |
| [**associateIdentityProviderConfig**](DefaultApi.md#associateIdentityProviderConfig) | **POST** /clusters/{name}/identity-provider-configs/associate |  |
| [**createAddon**](DefaultApi.md#createAddon) | **POST** /clusters/{name}/addons |  |
| [**createCluster**](DefaultApi.md#createCluster) | **POST** /clusters |  |
| [**createFargateProfile**](DefaultApi.md#createFargateProfile) | **POST** /clusters/{name}/fargate-profiles |  |
| [**createNodegroup**](DefaultApi.md#createNodegroup) | **POST** /clusters/{name}/node-groups |  |
| [**deleteAddon**](DefaultApi.md#deleteAddon) | **DELETE** /clusters/{name}/addons/{addonName} |  |
| [**deleteCluster**](DefaultApi.md#deleteCluster) | **DELETE** /clusters/{name} |  |
| [**deleteFargateProfile**](DefaultApi.md#deleteFargateProfile) | **DELETE** /clusters/{name}/fargate-profiles/{fargateProfileName} |  |
| [**deleteNodegroup**](DefaultApi.md#deleteNodegroup) | **DELETE** /clusters/{name}/node-groups/{nodegroupName} |  |
| [**deregisterCluster**](DefaultApi.md#deregisterCluster) | **DELETE** /cluster-registrations/{name} |  |
| [**describeAddon**](DefaultApi.md#describeAddon) | **GET** /clusters/{name}/addons/{addonName} |  |
| [**describeAddonConfiguration**](DefaultApi.md#describeAddonConfiguration) | **GET** /addons/configuration-schemas#addonName&amp;addonVersion |  |
| [**describeAddonVersions**](DefaultApi.md#describeAddonVersions) | **GET** /addons/supported-versions |  |
| [**describeCluster**](DefaultApi.md#describeCluster) | **GET** /clusters/{name} |  |
| [**describeFargateProfile**](DefaultApi.md#describeFargateProfile) | **GET** /clusters/{name}/fargate-profiles/{fargateProfileName} |  |
| [**describeIdentityProviderConfig**](DefaultApi.md#describeIdentityProviderConfig) | **POST** /clusters/{name}/identity-provider-configs/describe |  |
| [**describeNodegroup**](DefaultApi.md#describeNodegroup) | **GET** /clusters/{name}/node-groups/{nodegroupName} |  |
| [**describeUpdate**](DefaultApi.md#describeUpdate) | **GET** /clusters/{name}/updates/{updateId} |  |
| [**disassociateIdentityProviderConfig**](DefaultApi.md#disassociateIdentityProviderConfig) | **POST** /clusters/{name}/identity-provider-configs/disassociate |  |
| [**listAddons**](DefaultApi.md#listAddons) | **GET** /clusters/{name}/addons |  |
| [**listClusters**](DefaultApi.md#listClusters) | **GET** /clusters |  |
| [**listFargateProfiles**](DefaultApi.md#listFargateProfiles) | **GET** /clusters/{name}/fargate-profiles |  |
| [**listIdentityProviderConfigs**](DefaultApi.md#listIdentityProviderConfigs) | **GET** /clusters/{name}/identity-provider-configs |  |
| [**listNodegroups**](DefaultApi.md#listNodegroups) | **GET** /clusters/{name}/node-groups |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} |  |
| [**listUpdates**](DefaultApi.md#listUpdates) | **GET** /clusters/{name}/updates |  |
| [**registerCluster**](DefaultApi.md#registerCluster) | **POST** /cluster-registrations |  |
| [**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} |  |
| [**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys |  |
| [**updateAddon**](DefaultApi.md#updateAddon) | **POST** /clusters/{name}/addons/{addonName}/update |  |
| [**updateClusterConfig**](DefaultApi.md#updateClusterConfig) | **POST** /clusters/{name}/update-config |  |
| [**updateClusterVersion**](DefaultApi.md#updateClusterVersion) | **POST** /clusters/{name}/updates |  |
| [**updateNodegroupConfig**](DefaultApi.md#updateNodegroupConfig) | **POST** /clusters/{name}/node-groups/{nodegroupName}/update-config |  |
| [**updateNodegroupVersion**](DefaultApi.md#updateNodegroupVersion) | **POST** /clusters/{name}/node-groups/{nodegroupName}/update-version |  |


<a id="associateEncryptionConfig"></a>
# **associateEncryptionConfig**
> AssociateEncryptionConfigResponse associateEncryptionConfig(name, associateEncryptionConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Associate encryption configuration to an existing cluster.&lt;/p&gt; &lt;p&gt;You can use this API to enable encryption on existing clusters which do not have encryption already enabled. This allows you to implement a defense-in-depth security strategy without migrating applications to new Amazon EKS clusters.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the cluster that you are associating with encryption configuration.
    AssociateEncryptionConfigRequest associateEncryptionConfigRequest = new AssociateEncryptionConfigRequest(); // AssociateEncryptionConfigRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AssociateEncryptionConfigResponse result = apiInstance.associateEncryptionConfig(name, associateEncryptionConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associateEncryptionConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the cluster that you are associating with encryption configuration. | |
| **associateEncryptionConfigRequest** | [**AssociateEncryptionConfigRequest**](AssociateEncryptionConfigRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AssociateEncryptionConfigResponse**](AssociateEncryptionConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ResourceInUseException |  -  |
| **484** | ResourceNotFoundException |  -  |
| **485** | InvalidRequestException |  -  |

<a id="associateIdentityProviderConfig"></a>
# **associateIdentityProviderConfig**
> AssociateIdentityProviderConfigResponse associateIdentityProviderConfig(name, associateIdentityProviderConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Associate an identity provider configuration to a cluster.&lt;/p&gt; &lt;p&gt;If you want to authenticate identities using an identity provider, you can create an identity provider configuration and associate it to your cluster. After configuring authentication to your cluster you can create Kubernetes &lt;code&gt;roles&lt;/code&gt; and &lt;code&gt;clusterroles&lt;/code&gt; to assign permissions to the roles, and then bind the roles to the identities using Kubernetes &lt;code&gt;rolebindings&lt;/code&gt; and &lt;code&gt;clusterrolebindings&lt;/code&gt;. For more information see &lt;a href&#x3D;\&quot;https://kubernetes.io/docs/reference/access-authn-authz/rbac/\&quot;&gt;Using RBAC Authorization&lt;/a&gt; in the Kubernetes documentation.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the cluster to associate the configuration to.
    AssociateIdentityProviderConfigRequest associateIdentityProviderConfigRequest = new AssociateIdentityProviderConfigRequest(); // AssociateIdentityProviderConfigRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AssociateIdentityProviderConfigResponse result = apiInstance.associateIdentityProviderConfig(name, associateIdentityProviderConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associateIdentityProviderConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the cluster to associate the configuration to. | |
| **associateIdentityProviderConfigRequest** | [**AssociateIdentityProviderConfigRequest**](AssociateIdentityProviderConfigRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AssociateIdentityProviderConfigResponse**](AssociateIdentityProviderConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ResourceInUseException |  -  |
| **484** | ResourceNotFoundException |  -  |
| **485** | InvalidRequestException |  -  |

<a id="createAddon"></a>
# **createAddon**
> CreateAddonResponse createAddon(name, createAddonRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an Amazon EKS add-on.&lt;/p&gt; &lt;p&gt;Amazon EKS add-ons help to automate the provisioning and lifecycle management of common operational software for Amazon EKS clusters. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html\&quot;&gt;Amazon EKS add-ons&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the cluster to create the add-on for.
    CreateAddonRequest createAddonRequest = new CreateAddonRequest(); // CreateAddonRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateAddonResponse result = apiInstance.createAddon(name, createAddonRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAddon");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the cluster to create the add-on for. | |
| **createAddonRequest** | [**CreateAddonRequest**](CreateAddonRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateAddonResponse**](CreateAddonResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidRequestException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ResourceInUseException |  -  |
| **484** | ClientException |  -  |
| **485** | ServerException |  -  |

<a id="createCluster"></a>
# **createCluster**
> CreateClusterResponse createCluster(createClusterRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an Amazon EKS control plane. &lt;/p&gt; &lt;p&gt;The Amazon EKS control plane consists of control plane instances that run the Kubernetes software, such as &lt;code&gt;etcd&lt;/code&gt; and the API server. The control plane runs in an account managed by Amazon Web Services, and the Kubernetes API is exposed by the Amazon EKS API server endpoint. Each Amazon EKS cluster control plane is single tenant and unique. It runs on its own set of Amazon EC2 instances.&lt;/p&gt; &lt;p&gt;The cluster control plane is provisioned across multiple Availability Zones and fronted by an Elastic Load Balancing Network Load Balancer. Amazon EKS also provisions elastic network interfaces in your VPC subnets to provide connectivity from the control plane instances to the nodes (for example, to support &lt;code&gt;kubectl exec&lt;/code&gt;, &lt;code&gt;logs&lt;/code&gt;, and &lt;code&gt;proxy&lt;/code&gt; data flows).&lt;/p&gt; &lt;p&gt;Amazon EKS nodes run in your Amazon Web Services account and connect to your cluster&#39;s control plane over the Kubernetes API server endpoint and a certificate file that is created for your cluster.&lt;/p&gt; &lt;p&gt;In most cases, it takes several minutes to create a cluster. After you create an Amazon EKS cluster, you must configure your Kubernetes tooling to communicate with the API server and launch nodes into your cluster. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/managing-auth.html\&quot;&gt;Managing Cluster Authentication&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html\&quot;&gt;Launching Amazon EKS nodes&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateClusterRequest createClusterRequest = new CreateClusterRequest(); // CreateClusterRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateClusterResponse result = apiInstance.createCluster(createClusterRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createCluster");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createClusterRequest** | [**CreateClusterRequest**](CreateClusterRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateClusterResponse**](CreateClusterResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceInUseException |  -  |
| **481** | ResourceLimitExceededException |  -  |
| **482** | InvalidParameterException |  -  |
| **483** | ClientException |  -  |
| **484** | ServerException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | UnsupportedAvailabilityZoneException |  -  |

<a id="createFargateProfile"></a>
# **createFargateProfile**
> CreateFargateProfileResponse createFargateProfile(name, createFargateProfileRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an Fargate profile for your Amazon EKS cluster. You must have at least one Fargate profile in a cluster to be able to run pods on Fargate.&lt;/p&gt; &lt;p&gt;The Fargate profile allows an administrator to declare which pods run on Fargate and specify which pods run on which Fargate profile. This declaration is done through the profile’s selectors. Each profile can have up to five selectors that contain a namespace and labels. A namespace is required for every selector. The label field consists of multiple optional key-value pairs. Pods that match the selectors are scheduled on Fargate. If a to-be-scheduled pod matches any of the selectors in the Fargate profile, then that pod is run on Fargate.&lt;/p&gt; &lt;p&gt;When you create a Fargate profile, you must specify a pod execution role to use with the pods that are scheduled with the profile. This role is added to the cluster&#39;s Kubernetes &lt;a href&#x3D;\&quot;https://kubernetes.io/docs/admin/authorization/rbac/\&quot;&gt;Role Based Access Control&lt;/a&gt; (RBAC) for authorization so that the &lt;code&gt;kubelet&lt;/code&gt; that is running on the Fargate infrastructure can register with your Amazon EKS cluster so that it can appear in your cluster as a node. The pod execution role also provides IAM permissions to the Fargate infrastructure to allow read access to Amazon ECR image repositories. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html\&quot;&gt;Pod Execution Role&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Fargate profiles are immutable. However, you can create a new updated profile to replace an existing profile and then delete the original after the updated profile has finished creating.&lt;/p&gt; &lt;p&gt;If any Fargate profiles in a cluster are in the &lt;code&gt;DELETING&lt;/code&gt; status, you must wait for that Fargate profile to finish deleting before you can create any other profiles in that cluster.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html\&quot;&gt;Fargate Profile&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the Amazon EKS cluster to apply the Fargate profile to.
    CreateFargateProfileRequest createFargateProfileRequest = new CreateFargateProfileRequest(); // CreateFargateProfileRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateFargateProfileResponse result = apiInstance.createFargateProfile(name, createFargateProfileRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createFargateProfile");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the Amazon EKS cluster to apply the Fargate profile to. | |
| **createFargateProfileRequest** | [**CreateFargateProfileRequest**](CreateFargateProfileRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateFargateProfileResponse**](CreateFargateProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidRequestException |  -  |
| **482** | ClientException |  -  |
| **483** | ServerException |  -  |
| **484** | ResourceLimitExceededException |  -  |
| **485** | UnsupportedAvailabilityZoneException |  -  |

<a id="createNodegroup"></a>
# **createNodegroup**
> CreateNodegroupResponse createNodegroup(name, createNodegroupRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a managed node group for an Amazon EKS cluster. You can only create a node group for your cluster that is equal to the current Kubernetes version for the cluster. All node groups are created with the latest AMI release version for the respective minor Kubernetes version of the cluster, unless you deploy a custom AMI using a launch template. For more information about using launch templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html\&quot;&gt;Launch template support&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;An Amazon EKS managed node group is an Amazon EC2 Auto Scaling group and associated Amazon EC2 instances that are managed by Amazon Web Services for an Amazon EKS cluster. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html\&quot;&gt;Managed node groups&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Windows AMI types are only supported for commercial Regions that support Windows Amazon EKS.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the cluster to create the node group in.
    CreateNodegroupRequest createNodegroupRequest = new CreateNodegroupRequest(); // CreateNodegroupRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateNodegroupResponse result = apiInstance.createNodegroup(name, createNodegroupRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createNodegroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the cluster to create the node group in. | |
| **createNodegroupRequest** | [**CreateNodegroupRequest**](CreateNodegroupRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateNodegroupResponse**](CreateNodegroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceInUseException |  -  |
| **481** | ResourceLimitExceededException |  -  |
| **482** | InvalidRequestException |  -  |
| **483** | InvalidParameterException |  -  |
| **484** | ClientException |  -  |
| **485** | ServerException |  -  |
| **486** | ServiceUnavailableException |  -  |

<a id="deleteAddon"></a>
# **deleteAddon**
> DeleteAddonResponse deleteAddon(name, addonName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, preserve)



&lt;p&gt;Delete an Amazon EKS add-on.&lt;/p&gt; &lt;p&gt;When you remove the add-on, it will also be deleted from the cluster. You can always manually start an add-on on the cluster using the Kubernetes API.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the cluster to delete the add-on from.
    String addonName = "addonName_example"; // String | The name of the add-on. The name must match one of the names returned by <a href=\"https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\"> <code>ListAddons</code> </a>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Boolean preserve = true; // Boolean | Specifying this option preserves the add-on software on your cluster but Amazon EKS stops managing any settings for the add-on. If an IAM account is associated with the add-on, it isn't removed.
    try {
      DeleteAddonResponse result = apiInstance.deleteAddon(name, addonName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, preserve);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteAddon");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the cluster to delete the add-on from. | |
| **addonName** | **String**| The name of the add-on. The name must match one of the names returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\&quot;&gt; &lt;code&gt;ListAddons&lt;/code&gt; &lt;/a&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **preserve** | **Boolean**| Specifying this option preserves the add-on software on your cluster but Amazon EKS stops managing any settings for the add-on. If an IAM account is associated with the add-on, it isn&#39;t removed. | [optional] |

### Return type

[**DeleteAddonResponse**](DeleteAddonResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidRequestException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ClientException |  -  |
| **484** | ServerException |  -  |

<a id="deleteCluster"></a>
# **deleteCluster**
> DeleteClusterResponse deleteCluster(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the Amazon EKS cluster control plane.&lt;/p&gt; &lt;p&gt;If you have active services in your cluster that are associated with a load balancer, you must delete those services before deleting the cluster so that the load balancers are deleted properly. Otherwise, you can have orphaned resources in your VPC that prevent you from being able to delete the VPC. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/delete-cluster.html\&quot;&gt;Deleting a Cluster&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you have managed node groups or Fargate profiles attached to the cluster, you must delete them first. For more information, see &lt;a&gt;DeleteNodegroup&lt;/a&gt; and &lt;a&gt;DeleteFargateProfile&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the cluster to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteClusterResponse result = apiInstance.deleteCluster(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteCluster");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the cluster to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteClusterResponse**](DeleteClusterResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceInUseException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | ClientException |  -  |
| **483** | ServerException |  -  |
| **484** | ServiceUnavailableException |  -  |

<a id="deleteFargateProfile"></a>
# **deleteFargateProfile**
> DeleteFargateProfileResponse deleteFargateProfile(name, fargateProfileName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes an Fargate profile.&lt;/p&gt; &lt;p&gt;When you delete a Fargate profile, any pods running on Fargate that were created with the profile are deleted. If those pods match another Fargate profile, then they are scheduled on Fargate with that profile. If they no longer match any Fargate profiles, then they are not scheduled on Fargate and they may remain in a pending state.&lt;/p&gt; &lt;p&gt;Only one Fargate profile in a cluster can be in the &lt;code&gt;DELETING&lt;/code&gt; status at a time. You must wait for a Fargate profile to finish deleting before you can delete any other profiles in that cluster.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the Amazon EKS cluster associated with the Fargate profile to delete.
    String fargateProfileName = "fargateProfileName_example"; // String | The name of the Fargate profile to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteFargateProfileResponse result = apiInstance.deleteFargateProfile(name, fargateProfileName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteFargateProfile");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the Amazon EKS cluster associated with the Fargate profile to delete. | |
| **fargateProfileName** | **String**| The name of the Fargate profile to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteFargateProfileResponse**](DeleteFargateProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="deleteNodegroup"></a>
# **deleteNodegroup**
> DeleteNodegroupResponse deleteNodegroup(name, nodegroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes an Amazon EKS node group for a cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the Amazon EKS cluster that is associated with your node group.
    String nodegroupName = "nodegroupName_example"; // String | The name of the node group to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteNodegroupResponse result = apiInstance.deleteNodegroup(name, nodegroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteNodegroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the Amazon EKS cluster that is associated with your node group. | |
| **nodegroupName** | **String**| The name of the node group to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteNodegroupResponse**](DeleteNodegroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceInUseException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InvalidParameterException |  -  |
| **483** | ClientException |  -  |
| **484** | ServerException |  -  |
| **485** | ServiceUnavailableException |  -  |

<a id="deregisterCluster"></a>
# **deregisterCluster**
> DeregisterClusterResponse deregisterCluster(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deregisters a connected cluster to remove it from the Amazon EKS control plane.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the connected cluster to deregister.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeregisterClusterResponse result = apiInstance.deregisterCluster(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deregisterCluster");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the connected cluster to deregister. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeregisterClusterResponse**](DeregisterClusterResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceInUseException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | ClientException |  -  |
| **483** | ServerException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | AccessDeniedException |  -  |

<a id="describeAddon"></a>
# **describeAddon**
> DescribeAddonResponse describeAddon(name, addonName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Describes an Amazon EKS add-on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the cluster.
    String addonName = "addonName_example"; // String | The name of the add-on. The name must match one of the names returned by <a href=\"https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\"> <code>ListAddons</code> </a>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeAddonResponse result = apiInstance.describeAddon(name, addonName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeAddon");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the cluster. | |
| **addonName** | **String**| The name of the add-on. The name must match one of the names returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\&quot;&gt; &lt;code&gt;ListAddons&lt;/code&gt; &lt;/a&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeAddonResponse**](DescribeAddonResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidRequestException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ClientException |  -  |
| **484** | ServerException |  -  |

<a id="describeAddonConfiguration"></a>
# **describeAddonConfiguration**
> DescribeAddonConfigurationResponse describeAddonConfiguration(addonName, addonVersion, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns configuration options.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String addonName = "addonName_example"; // String | The name of the add-on. The name must match one of the names that <a href=\"https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html\"> <code>DescribeAddonVersions</code> </a> returns.
    String addonVersion = "addonVersion_example"; // String | The version of the add-on. The version must match one of the versions returned by <a href=\"https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html\"> <code>DescribeAddonVersions</code> </a>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeAddonConfigurationResponse result = apiInstance.describeAddonConfiguration(addonName, addonVersion, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeAddonConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **addonName** | **String**| The name of the add-on. The name must match one of the names that &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html\&quot;&gt; &lt;code&gt;DescribeAddonVersions&lt;/code&gt; &lt;/a&gt; returns. | |
| **addonVersion** | **String**| The version of the add-on. The version must match one of the versions returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html\&quot;&gt; &lt;code&gt;DescribeAddonVersions&lt;/code&gt; &lt;/a&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeAddonConfigurationResponse**](DescribeAddonConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServerException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InvalidParameterException |  -  |

<a id="describeAddonVersions"></a>
# **describeAddonVersions**
> DescribeAddonVersionsResponse describeAddonVersions(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, kubernetesVersion, maxResults, nextToken, addonName, types, publishers, owners)



Describes the versions for an add-on. Information such as the Kubernetes versions that you can use the add-on with, the &lt;code&gt;owner&lt;/code&gt;, &lt;code&gt;publisher&lt;/code&gt;, and the &lt;code&gt;type&lt;/code&gt; of the add-on are returned. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String kubernetesVersion = "kubernetesVersion_example"; // String | The Kubernetes versions that you can use the add-on with.
    Integer maxResults = 56; // Integer | The maximum number of results to return.
    String nextToken = "nextToken_example"; // String | <p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeAddonVersionsRequest</code> where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
    String addonName = "addonName_example"; // String | The name of the add-on. The name must match one of the names returned by <a href=\"https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\"> <code>ListAddons</code> </a>.
    List<String> types = Arrays.asList(); // List<String> | The type of the add-on. For valid <code>types</code>, don't specify a value for this property.
    List<String> publishers = Arrays.asList(); // List<String> | The publisher of the add-on. For valid <code>publishers</code>, don't specify a value for this property.
    List<String> owners = Arrays.asList(); // List<String> | The owner of the add-on. For valid <code>owners</code>, don't specify a value for this property.
    try {
      DescribeAddonVersionsResponse result = apiInstance.describeAddonVersions(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, kubernetesVersion, maxResults, nextToken, addonName, types, publishers, owners);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeAddonVersions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **kubernetesVersion** | **String**| The Kubernetes versions that you can use the add-on with. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return. | [optional] |
| **nextToken** | **String**| &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;DescribeAddonVersionsRequest&lt;/code&gt; where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt; | [optional] |
| **addonName** | **String**| The name of the add-on. The name must match one of the names returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\&quot;&gt; &lt;code&gt;ListAddons&lt;/code&gt; &lt;/a&gt;. | [optional] |
| **types** | [**List&lt;String&gt;**](String.md)| The type of the add-on. For valid &lt;code&gt;types&lt;/code&gt;, don&#39;t specify a value for this property. | [optional] |
| **publishers** | [**List&lt;String&gt;**](String.md)| The publisher of the add-on. For valid &lt;code&gt;publishers&lt;/code&gt;, don&#39;t specify a value for this property. | [optional] |
| **owners** | [**List&lt;String&gt;**](String.md)| The owner of the add-on. For valid &lt;code&gt;owners&lt;/code&gt;, don&#39;t specify a value for this property. | [optional] |

### Return type

[**DescribeAddonVersionsResponse**](DescribeAddonVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServerException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | InvalidParameterException |  -  |

<a id="describeCluster"></a>
# **describeCluster**
> DescribeClusterResponse describeCluster(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns descriptive information about an Amazon EKS cluster.&lt;/p&gt; &lt;p&gt;The API server endpoint and certificate authority data returned by this operation are required for &lt;code&gt;kubelet&lt;/code&gt; and &lt;code&gt;kubectl&lt;/code&gt; to communicate with your Kubernetes API server. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html\&quot;&gt;Create a kubeconfig for Amazon EKS&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The API server endpoint and certificate authority data aren&#39;t available until the cluster reaches the &lt;code&gt;ACTIVE&lt;/code&gt; state.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the cluster to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeClusterResponse result = apiInstance.describeCluster(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeCluster");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the cluster to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeClusterResponse**](DescribeClusterResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="describeFargateProfile"></a>
# **describeFargateProfile**
> DescribeFargateProfileResponse describeFargateProfile(name, fargateProfileName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns descriptive information about an Fargate profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the Amazon EKS cluster associated with the Fargate profile.
    String fargateProfileName = "fargateProfileName_example"; // String | The name of the Fargate profile to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeFargateProfileResponse result = apiInstance.describeFargateProfile(name, fargateProfileName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeFargateProfile");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the Amazon EKS cluster associated with the Fargate profile. | |
| **fargateProfileName** | **String**| The name of the Fargate profile to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeFargateProfileResponse**](DescribeFargateProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="describeIdentityProviderConfig"></a>
# **describeIdentityProviderConfig**
> DescribeIdentityProviderConfigResponse describeIdentityProviderConfig(name, describeIdentityProviderConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns descriptive information about an identity provider configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The cluster name that the identity provider configuration is associated to.
    DescribeIdentityProviderConfigRequest describeIdentityProviderConfigRequest = new DescribeIdentityProviderConfigRequest(); // DescribeIdentityProviderConfigRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeIdentityProviderConfigResponse result = apiInstance.describeIdentityProviderConfig(name, describeIdentityProviderConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeIdentityProviderConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The cluster name that the identity provider configuration is associated to. | |
| **describeIdentityProviderConfigRequest** | [**DescribeIdentityProviderConfigRequest**](DescribeIdentityProviderConfigRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeIdentityProviderConfigResponse**](DescribeIdentityProviderConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | ClientException |  -  |
| **483** | ServerException |  -  |
| **484** | ServiceUnavailableException |  -  |

<a id="describeNodegroup"></a>
# **describeNodegroup**
> DescribeNodegroupResponse describeNodegroup(name, nodegroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns descriptive information about an Amazon EKS node group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the Amazon EKS cluster associated with the node group.
    String nodegroupName = "nodegroupName_example"; // String | The name of the node group to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeNodegroupResponse result = apiInstance.describeNodegroup(name, nodegroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeNodegroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the Amazon EKS cluster associated with the node group. | |
| **nodegroupName** | **String**| The name of the node group to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeNodegroupResponse**](DescribeNodegroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | ClientException |  -  |
| **483** | ServerException |  -  |
| **484** | ServiceUnavailableException |  -  |

<a id="describeUpdate"></a>
# **describeUpdate**
> DescribeUpdateResponse describeUpdate(name, updateId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nodegroupName, addonName)



&lt;p&gt;Returns descriptive information about an update against your Amazon EKS cluster or associated managed node group or Amazon EKS add-on.&lt;/p&gt; &lt;p&gt;When the status of the update is &lt;code&gt;Succeeded&lt;/code&gt;, the update is complete. If an update fails, the status is &lt;code&gt;Failed&lt;/code&gt;, and an error detail explains the reason for the failure.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the Amazon EKS cluster associated with the update.
    String updateId = "updateId_example"; // String | The ID of the update to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nodegroupName = "nodegroupName_example"; // String | The name of the Amazon EKS node group associated with the update. This parameter is required if the update is a node group update.
    String addonName = "addonName_example"; // String | The name of the add-on. The name must match one of the names returned by <a href=\"https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\"> <code>ListAddons</code> </a>. This parameter is required if the update is an add-on update.
    try {
      DescribeUpdateResponse result = apiInstance.describeUpdate(name, updateId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nodegroupName, addonName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the Amazon EKS cluster associated with the update. | |
| **updateId** | **String**| The ID of the update to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nodegroupName** | **String**| The name of the Amazon EKS node group associated with the update. This parameter is required if the update is a node group update. | [optional] |
| **addonName** | **String**| The name of the add-on. The name must match one of the names returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\&quot;&gt; &lt;code&gt;ListAddons&lt;/code&gt; &lt;/a&gt;. This parameter is required if the update is an add-on update. | [optional] |

### Return type

[**DescribeUpdateResponse**](DescribeUpdateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="disassociateIdentityProviderConfig"></a>
# **disassociateIdentityProviderConfig**
> DisassociateIdentityProviderConfigResponse disassociateIdentityProviderConfig(name, disassociateIdentityProviderConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Disassociates an identity provider configuration from a cluster. If you disassociate an identity provider from your cluster, users included in the provider can no longer access the cluster. However, you can still access the cluster with Amazon Web Services IAM users.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the cluster to disassociate an identity provider from.
    DisassociateIdentityProviderConfigRequest disassociateIdentityProviderConfigRequest = new DisassociateIdentityProviderConfigRequest(); // DisassociateIdentityProviderConfigRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DisassociateIdentityProviderConfigResponse result = apiInstance.disassociateIdentityProviderConfig(name, disassociateIdentityProviderConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disassociateIdentityProviderConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the cluster to disassociate an identity provider from. | |
| **disassociateIdentityProviderConfigRequest** | [**DisassociateIdentityProviderConfigRequest**](DisassociateIdentityProviderConfigRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DisassociateIdentityProviderConfigResponse**](DisassociateIdentityProviderConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ResourceInUseException |  -  |
| **484** | ResourceNotFoundException |  -  |
| **485** | InvalidRequestException |  -  |

<a id="listAddons"></a>
# **listAddons**
> ListAddonsResponse listAddons(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Lists the available add-ons.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the cluster.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of add-on results returned by <code>ListAddonsRequest</code> in paginated output. When you use this parameter, <code>ListAddonsRequest</code> returns only <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListAddonsRequest</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListAddonsRequest</code> returns up to 100 results and a <code>nextToken</code> value, if applicable.
    String nextToken = "nextToken_example"; // String | <p>The <code>nextToken</code> value returned from a previous paginated <code>ListAddonsRequest</code> where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
    try {
      ListAddonsResponse result = apiInstance.listAddons(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAddons");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the cluster. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of add-on results returned by &lt;code&gt;ListAddonsRequest&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListAddonsRequest&lt;/code&gt; returns only &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListAddonsRequest&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListAddonsRequest&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value, if applicable. | [optional] |
| **nextToken** | **String**| &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListAddonsRequest&lt;/code&gt; where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt; | [optional] |

### Return type

[**ListAddonsResponse**](ListAddonsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidRequestException |  -  |
| **482** | ClientException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ServerException |  -  |

<a id="listClusters"></a>
# **listClusters**
> ListClustersResponse listClusters(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, include)



Lists the Amazon EKS clusters in your Amazon Web Services account in the specified Region.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of cluster results returned by <code>ListClusters</code> in paginated output. When you use this parameter, <code>ListClusters</code> returns only <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListClusters</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListClusters</code> returns up to 100 results and a <code>nextToken</code> value if applicable.
    String nextToken = "nextToken_example"; // String | <p>The <code>nextToken</code> value returned from a previous paginated <code>ListClusters</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
    List<String> include = Arrays.asList(); // List<String> | Indicates whether external clusters are included in the returned list. Use '<code>all</code>' to return connected clusters, or blank to return only Amazon EKS clusters. '<code>all</code>' must be in lowercase otherwise an error occurs.
    try {
      ListClustersResponse result = apiInstance.listClusters(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listClusters");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of cluster results returned by &lt;code&gt;ListClusters&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListClusters&lt;/code&gt; returns only &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListClusters&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListClusters&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **nextToken** | **String**| &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListClusters&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt; | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Indicates whether external clusters are included in the returned list. Use &#39;&lt;code&gt;all&lt;/code&gt;&#39; to return connected clusters, or blank to return only Amazon EKS clusters. &#39;&lt;code&gt;all&lt;/code&gt;&#39; must be in lowercase otherwise an error occurs. | [optional] |

### Return type

[**ListClustersResponse**](ListClustersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="listFargateProfiles"></a>
# **listFargateProfiles**
> ListFargateProfilesResponse listFargateProfiles(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Lists the Fargate profiles associated with the specified cluster in your Amazon Web Services account in the specified Region.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the Amazon EKS cluster that you would like to list Fargate profiles in.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of Fargate profile results returned by <code>ListFargateProfiles</code> in paginated output. When you use this parameter, <code>ListFargateProfiles</code> returns only <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListFargateProfiles</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListFargateProfiles</code> returns up to 100 results and a <code>nextToken</code> value if applicable.
    String nextToken = "nextToken_example"; // String | The <code>nextToken</code> value returned from a previous paginated <code>ListFargateProfiles</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.
    try {
      ListFargateProfilesResponse result = apiInstance.listFargateProfiles(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listFargateProfiles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the Amazon EKS cluster that you would like to list Fargate profiles in. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of Fargate profile results returned by &lt;code&gt;ListFargateProfiles&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListFargateProfiles&lt;/code&gt; returns only &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListFargateProfiles&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListFargateProfiles&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListFargateProfiles&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |

### Return type

[**ListFargateProfilesResponse**](ListFargateProfilesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | ClientException |  -  |
| **483** | ServerException |  -  |

<a id="listIdentityProviderConfigs"></a>
# **listIdentityProviderConfigs**
> ListIdentityProviderConfigsResponse listIdentityProviderConfigs(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



A list of identity provider configurations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The cluster name that you want to list identity provider configurations for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of identity provider configurations returned by <code>ListIdentityProviderConfigs</code> in paginated output. When you use this parameter, <code>ListIdentityProviderConfigs</code> returns only <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListIdentityProviderConfigs</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListIdentityProviderConfigs</code> returns up to 100 results and a <code>nextToken</code> value, if applicable.
    String nextToken = "nextToken_example"; // String | The <code>nextToken</code> value returned from a previous paginated <code>IdentityProviderConfigsRequest</code> where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.
    try {
      ListIdentityProviderConfigsResponse result = apiInstance.listIdentityProviderConfigs(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listIdentityProviderConfigs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The cluster name that you want to list identity provider configurations for. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of identity provider configurations returned by &lt;code&gt;ListIdentityProviderConfigs&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListIdentityProviderConfigs&lt;/code&gt; returns only &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListIdentityProviderConfigs&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListIdentityProviderConfigs&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value, if applicable. | [optional] |
| **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;IdentityProviderConfigsRequest&lt;/code&gt; where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |

### Return type

[**ListIdentityProviderConfigsResponse**](ListIdentityProviderConfigsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ServiceUnavailableException |  -  |
| **484** | ResourceNotFoundException |  -  |

<a id="listNodegroups"></a>
# **listNodegroups**
> ListNodegroupsResponse listNodegroups(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Lists the Amazon EKS managed node groups associated with the specified cluster in your Amazon Web Services account in the specified Region. Self-managed node groups are not listed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the Amazon EKS cluster that you would like to list node groups in.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of node group results returned by <code>ListNodegroups</code> in paginated output. When you use this parameter, <code>ListNodegroups</code> returns only <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListNodegroups</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListNodegroups</code> returns up to 100 results and a <code>nextToken</code> value if applicable.
    String nextToken = "nextToken_example"; // String | The <code>nextToken</code> value returned from a previous paginated <code>ListNodegroups</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.
    try {
      ListNodegroupsResponse result = apiInstance.listNodegroups(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listNodegroups");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the Amazon EKS cluster that you would like to list node groups in. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of node group results returned by &lt;code&gt;ListNodegroups&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListNodegroups&lt;/code&gt; returns only &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListNodegroups&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListNodegroups&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListNodegroups&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |

### Return type

[**ListNodegroupsResponse**](ListNodegroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ServiceUnavailableException |  -  |
| **484** | ResourceNotFoundException |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceResponse listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



List the tags for an Amazon EKS resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the supported resources are Amazon EKS clusters and managed node groups.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceResponse result = apiInstance.listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForResource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceArn** | **String**| The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the supported resources are Amazon EKS clusters and managed node groups. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | NotFoundException |  -  |

<a id="listUpdates"></a>
# **listUpdates**
> ListUpdatesResponse listUpdates(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nodegroupName, addonName, nextToken, maxResults)



Lists the updates associated with an Amazon EKS cluster or managed node group in your Amazon Web Services account, in the specified Region.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the Amazon EKS cluster to list updates for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nodegroupName = "nodegroupName_example"; // String | The name of the Amazon EKS managed node group to list updates for.
    String addonName = "addonName_example"; // String | The names of the installed add-ons that have available updates.
    String nextToken = "nextToken_example"; // String | The <code>nextToken</code> value returned from a previous paginated <code>ListUpdates</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.
    Integer maxResults = 56; // Integer | The maximum number of update results returned by <code>ListUpdates</code> in paginated output. When you use this parameter, <code>ListUpdates</code> returns only <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListUpdates</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListUpdates</code> returns up to 100 results and a <code>nextToken</code> value if applicable.
    try {
      ListUpdatesResponse result = apiInstance.listUpdates(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nodegroupName, addonName, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listUpdates");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the Amazon EKS cluster to list updates for. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nodegroupName** | **String**| The name of the Amazon EKS managed node group to list updates for. | [optional] |
| **addonName** | **String**| The names of the installed add-ons that have available updates. | [optional] |
| **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListUpdates&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |
| **maxResults** | **Integer**| The maximum number of update results returned by &lt;code&gt;ListUpdates&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListUpdates&lt;/code&gt; returns only &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListUpdates&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListUpdates&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |

### Return type

[**ListUpdatesResponse**](ListUpdatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="registerCluster"></a>
# **registerCluster**
> RegisterClusterResponse registerCluster(registerClusterRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Connects a Kubernetes cluster to the Amazon EKS control plane. &lt;/p&gt; &lt;p&gt;Any Kubernetes cluster can be connected to the Amazon EKS control plane to view current information about the cluster and its nodes. &lt;/p&gt; &lt;p&gt;Cluster connection requires two steps. First, send a &lt;code&gt; &lt;a&gt;RegisterClusterRequest&lt;/a&gt; &lt;/code&gt; to add it to the Amazon EKS control plane.&lt;/p&gt; &lt;p&gt;Second, a &lt;a href&#x3D;\&quot;https://amazon-eks.s3.us-west-2.amazonaws.com/eks-connector/manifests/eks-connector/latest/eks-connector.yaml\&quot;&gt;Manifest&lt;/a&gt; containing the &lt;code&gt;activationID&lt;/code&gt; and &lt;code&gt;activationCode&lt;/code&gt; must be applied to the Kubernetes cluster through it&#39;s native provider to provide visibility.&lt;/p&gt; &lt;p&gt;After the Manifest is updated and applied, then the connected cluster is visible to the Amazon EKS control plane. If the Manifest is not applied within three days, then the connected cluster will no longer be visible and must be deregistered. See &lt;a&gt;DeregisterCluster&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    RegisterClusterRequest registerClusterRequest = new RegisterClusterRequest(); // RegisterClusterRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      RegisterClusterResponse result = apiInstance.registerCluster(registerClusterRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#registerCluster");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **registerClusterRequest** | [**RegisterClusterRequest**](RegisterClusterRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**RegisterClusterResponse**](RegisterClusterResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceLimitExceededException |  -  |
| **481** | InvalidParameterException |  -  |
| **482** | ClientException |  -  |
| **483** | ServerException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ResourceInUseException |  -  |
| **487** | ResourcePropagationDelayException |  -  |

<a id="tagResource"></a>
# **tagResource**
> Object tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Associates the specified tags to a resource with the specified &lt;code&gt;resourceArn&lt;/code&gt;. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are deleted as well. Tags that you create for Amazon EKS resources do not propagate to any other resources associated with the cluster. For example, if you tag a cluster with this operation, that tag does not automatically propagate to the subnets and nodes associated with the cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource to which to add tags. Currently, the supported resources are Amazon EKS clusters and managed node groups.
    TagResourceRequest tagResourceRequest = new TagResourceRequest(); // TagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagResource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource to which to add tags. Currently, the supported resources are Amazon EKS clusters and managed node groups. | |
| **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | NotFoundException |  -  |

<a id="untagResource"></a>
# **untagResource**
> Object untagResource(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes specified tags from a resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource from which to delete tags. Currently, the supported resources are Amazon EKS clusters and managed node groups.
    List<String> tagKeys = Arrays.asList(); // List<String> | The keys of the tags to be removed.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.untagResource(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagResource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource from which to delete tags. Currently, the supported resources are Amazon EKS clusters and managed node groups. | |
| **tagKeys** | [**List&lt;String&gt;**](String.md)| The keys of the tags to be removed. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | NotFoundException |  -  |

<a id="updateAddon"></a>
# **updateAddon**
> UpdateAddonResponse updateAddon(name, addonName, updateAddonRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates an Amazon EKS add-on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the cluster.
    String addonName = "addonName_example"; // String | The name of the add-on. The name must match one of the names returned by <a href=\"https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\"> <code>ListAddons</code> </a>.
    UpdateAddonRequest updateAddonRequest = new UpdateAddonRequest(); // UpdateAddonRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateAddonResponse result = apiInstance.updateAddon(name, addonName, updateAddonRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateAddon");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the cluster. | |
| **addonName** | **String**| The name of the add-on. The name must match one of the names returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\&quot;&gt; &lt;code&gt;ListAddons&lt;/code&gt; &lt;/a&gt;. | |
| **updateAddonRequest** | [**UpdateAddonRequest**](UpdateAddonRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateAddonResponse**](UpdateAddonResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidRequestException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ResourceInUseException |  -  |
| **484** | ClientException |  -  |
| **485** | ServerException |  -  |

<a id="updateClusterConfig"></a>
# **updateClusterConfig**
> UpdateClusterConfigResponse updateClusterConfig(name, updateClusterConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates an Amazon EKS cluster configuration. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with the &lt;a&gt;DescribeUpdate&lt;/a&gt; API operation.&lt;/p&gt; &lt;p&gt;You can use this API operation to enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs aren&#39;t exported to CloudWatch Logs. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html\&quot;&gt;Amazon EKS Cluster Control Plane Logs&lt;/a&gt; in the &lt;i&gt; &lt;i&gt;Amazon EKS User Guide&lt;/i&gt; &lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudwatch/pricing/\&quot;&gt;CloudWatch Pricing&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You can also use this API operation to enable or disable public and private access to your cluster&#39;s Kubernetes API server endpoint. By default, public access is enabled, and private access is disabled. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html\&quot;&gt;Amazon EKS cluster endpoint access control&lt;/a&gt; in the &lt;i&gt; &lt;i&gt;Amazon EKS User Guide&lt;/i&gt; &lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt;You can&#39;t update the subnets or security group IDs for an existing cluster.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to &lt;code&gt;UPDATING&lt;/code&gt; (this status transition is eventually consistent). When the update is complete (either &lt;code&gt;Failed&lt;/code&gt; or &lt;code&gt;Successful&lt;/code&gt;), the cluster status moves to &lt;code&gt;Active&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the Amazon EKS cluster to update.
    UpdateClusterConfigRequest updateClusterConfigRequest = new UpdateClusterConfigRequest(); // UpdateClusterConfigRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateClusterConfigResponse result = apiInstance.updateClusterConfig(name, updateClusterConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateClusterConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the Amazon EKS cluster to update. | |
| **updateClusterConfigRequest** | [**UpdateClusterConfigRequest**](UpdateClusterConfigRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateClusterConfigResponse**](UpdateClusterConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ResourceInUseException |  -  |
| **484** | ResourceNotFoundException |  -  |
| **485** | InvalidRequestException |  -  |

<a id="updateClusterVersion"></a>
# **updateClusterVersion**
> UpdateClusterVersionResponse updateClusterVersion(name, updateClusterVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates an Amazon EKS cluster to the specified Kubernetes version. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with the &lt;a&gt;DescribeUpdate&lt;/a&gt; API operation.&lt;/p&gt; &lt;p&gt;Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to &lt;code&gt;UPDATING&lt;/code&gt; (this status transition is eventually consistent). When the update is complete (either &lt;code&gt;Failed&lt;/code&gt; or &lt;code&gt;Successful&lt;/code&gt;), the cluster status moves to &lt;code&gt;Active&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If your cluster has managed node groups attached to it, all of your node groups’ Kubernetes versions must match the cluster’s Kubernetes version in order to update the cluster to a new Kubernetes version.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the Amazon EKS cluster to update.
    UpdateClusterVersionRequest updateClusterVersionRequest = new UpdateClusterVersionRequest(); // UpdateClusterVersionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateClusterVersionResponse result = apiInstance.updateClusterVersion(name, updateClusterVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateClusterVersion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the Amazon EKS cluster to update. | |
| **updateClusterVersionRequest** | [**UpdateClusterVersionRequest**](UpdateClusterVersionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateClusterVersionResponse**](UpdateClusterVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ResourceInUseException |  -  |
| **484** | ResourceNotFoundException |  -  |
| **485** | InvalidRequestException |  -  |

<a id="updateNodegroupConfig"></a>
# **updateNodegroupConfig**
> UpdateNodegroupConfigResponse updateNodegroupConfig(name, nodegroupName, updateNodegroupConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates an Amazon EKS managed node group configuration. Your node group continues to function during the update. The response output includes an update ID that you can use to track the status of your node group update with the &lt;a&gt;DescribeUpdate&lt;/a&gt; API operation. Currently you can update the Kubernetes labels for a node group or the scaling configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the Amazon EKS cluster that the managed node group resides in.
    String nodegroupName = "nodegroupName_example"; // String | The name of the managed node group to update.
    UpdateNodegroupConfigRequest updateNodegroupConfigRequest = new UpdateNodegroupConfigRequest(); // UpdateNodegroupConfigRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateNodegroupConfigResponse result = apiInstance.updateNodegroupConfig(name, nodegroupName, updateNodegroupConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateNodegroupConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the Amazon EKS cluster that the managed node group resides in. | |
| **nodegroupName** | **String**| The name of the managed node group to update. | |
| **updateNodegroupConfigRequest** | [**UpdateNodegroupConfigRequest**](UpdateNodegroupConfigRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateNodegroupConfigResponse**](UpdateNodegroupConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ResourceInUseException |  -  |
| **484** | ResourceNotFoundException |  -  |
| **485** | InvalidRequestException |  -  |

<a id="updateNodegroupVersion"></a>
# **updateNodegroupVersion**
> UpdateNodegroupVersionResponse updateNodegroupVersion(name, nodegroupName, updateNodegroupVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates the Kubernetes version or AMI version of an Amazon EKS managed node group.&lt;/p&gt; &lt;p&gt;You can update a node group using a launch template only if the node group was originally deployed with a launch template. If you need to update a custom AMI in a node group that was deployed with a launch template, then update your custom AMI, specify the new ID in a new version of the launch template, and then update the node group to the new version of the launch template.&lt;/p&gt; &lt;p&gt;If you update without a launch template, then you can update to the latest available AMI version of a node group&#39;s current Kubernetes version by not specifying a Kubernetes version in the request. You can update to the latest AMI version of your cluster&#39;s current Kubernetes version by specifying your cluster&#39;s Kubernetes version in the request. For information about Linux versions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html\&quot;&gt;Amazon EKS optimized Amazon Linux AMI versions&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;. For information about Windows versions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html\&quot;&gt;Amazon EKS optimized Windows AMI versions&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;You cannot roll back a node group to an earlier Kubernetes version or AMI version.&lt;/p&gt; &lt;p&gt;When a node in a managed node group is terminated due to a scaling action or update, the pods in that node are drained first. Amazon EKS attempts to drain the nodes gracefully and will fail if it is unable to do so. You can &lt;code&gt;force&lt;/code&gt; the update if Amazon EKS is unable to drain the nodes as a result of a pod disruption budget issue.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://eks.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the Amazon EKS cluster that is associated with the managed node group to update.
    String nodegroupName = "nodegroupName_example"; // String | The name of the managed node group to update.
    UpdateNodegroupVersionRequest updateNodegroupVersionRequest = new UpdateNodegroupVersionRequest(); // UpdateNodegroupVersionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateNodegroupVersionResponse result = apiInstance.updateNodegroupVersion(name, nodegroupName, updateNodegroupVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateNodegroupVersion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the Amazon EKS cluster that is associated with the managed node group to update. | |
| **nodegroupName** | **String**| The name of the managed node group to update. | |
| **updateNodegroupVersionRequest** | [**UpdateNodegroupVersionRequest**](UpdateNodegroupVersionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateNodegroupVersionResponse**](UpdateNodegroupVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | ClientException |  -  |
| **482** | ServerException |  -  |
| **483** | ResourceInUseException |  -  |
| **484** | ResourceNotFoundException |  -  |
| **485** | InvalidRequestException |  -  |

