# DefaultApi

All URIs are relative to *https://route53.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activateKeySigningKey**](DefaultApi.md#activateKeySigningKey) | **POST** /2013-04-01/keysigningkey/{HostedZoneId}/{Name}/activate |  |
| [**associateVPCWithHostedZone**](DefaultApi.md#associateVPCWithHostedZone) | **POST** /2013-04-01/hostedzone/{Id}/associatevpc |  |
| [**changeCidrCollection**](DefaultApi.md#changeCidrCollection) | **POST** /2013-04-01/cidrcollection/{CidrCollectionId} |  |
| [**changeResourceRecordSets**](DefaultApi.md#changeResourceRecordSets) | **POST** /2013-04-01/hostedzone/{Id}/rrset/ |  |
| [**changeTagsForResource**](DefaultApi.md#changeTagsForResource) | **POST** /2013-04-01/tags/{ResourceType}/{ResourceId} |  |
| [**createCidrCollection**](DefaultApi.md#createCidrCollection) | **POST** /2013-04-01/cidrcollection |  |
| [**createHealthCheck**](DefaultApi.md#createHealthCheck) | **POST** /2013-04-01/healthcheck |  |
| [**createHostedZone**](DefaultApi.md#createHostedZone) | **POST** /2013-04-01/hostedzone |  |
| [**createKeySigningKey**](DefaultApi.md#createKeySigningKey) | **POST** /2013-04-01/keysigningkey |  |
| [**createQueryLoggingConfig**](DefaultApi.md#createQueryLoggingConfig) | **POST** /2013-04-01/queryloggingconfig |  |
| [**createReusableDelegationSet**](DefaultApi.md#createReusableDelegationSet) | **POST** /2013-04-01/delegationset |  |
| [**createTrafficPolicy**](DefaultApi.md#createTrafficPolicy) | **POST** /2013-04-01/trafficpolicy |  |
| [**createTrafficPolicyInstance**](DefaultApi.md#createTrafficPolicyInstance) | **POST** /2013-04-01/trafficpolicyinstance |  |
| [**createTrafficPolicyVersion**](DefaultApi.md#createTrafficPolicyVersion) | **POST** /2013-04-01/trafficpolicy/{Id} |  |
| [**createVPCAssociationAuthorization**](DefaultApi.md#createVPCAssociationAuthorization) | **POST** /2013-04-01/hostedzone/{Id}/authorizevpcassociation |  |
| [**deactivateKeySigningKey**](DefaultApi.md#deactivateKeySigningKey) | **POST** /2013-04-01/keysigningkey/{HostedZoneId}/{Name}/deactivate |  |
| [**deleteCidrCollection**](DefaultApi.md#deleteCidrCollection) | **DELETE** /2013-04-01/cidrcollection/{CidrCollectionId} |  |
| [**deleteHealthCheck**](DefaultApi.md#deleteHealthCheck) | **DELETE** /2013-04-01/healthcheck/{HealthCheckId} |  |
| [**deleteHostedZone**](DefaultApi.md#deleteHostedZone) | **DELETE** /2013-04-01/hostedzone/{Id} |  |
| [**deleteKeySigningKey**](DefaultApi.md#deleteKeySigningKey) | **DELETE** /2013-04-01/keysigningkey/{HostedZoneId}/{Name} |  |
| [**deleteQueryLoggingConfig**](DefaultApi.md#deleteQueryLoggingConfig) | **DELETE** /2013-04-01/queryloggingconfig/{Id} |  |
| [**deleteReusableDelegationSet**](DefaultApi.md#deleteReusableDelegationSet) | **DELETE** /2013-04-01/delegationset/{Id} |  |
| [**deleteTrafficPolicy**](DefaultApi.md#deleteTrafficPolicy) | **DELETE** /2013-04-01/trafficpolicy/{Id}/{Version} |  |
| [**deleteTrafficPolicyInstance**](DefaultApi.md#deleteTrafficPolicyInstance) | **DELETE** /2013-04-01/trafficpolicyinstance/{Id} |  |
| [**deleteVPCAssociationAuthorization**](DefaultApi.md#deleteVPCAssociationAuthorization) | **POST** /2013-04-01/hostedzone/{Id}/deauthorizevpcassociation |  |
| [**disableHostedZoneDNSSEC**](DefaultApi.md#disableHostedZoneDNSSEC) | **POST** /2013-04-01/hostedzone/{Id}/disable-dnssec |  |
| [**disassociateVPCFromHostedZone**](DefaultApi.md#disassociateVPCFromHostedZone) | **POST** /2013-04-01/hostedzone/{Id}/disassociatevpc |  |
| [**enableHostedZoneDNSSEC**](DefaultApi.md#enableHostedZoneDNSSEC) | **POST** /2013-04-01/hostedzone/{Id}/enable-dnssec |  |
| [**getAccountLimit**](DefaultApi.md#getAccountLimit) | **GET** /2013-04-01/accountlimit/{Type} |  |
| [**getChange**](DefaultApi.md#getChange) | **GET** /2013-04-01/change/{Id} |  |
| [**getCheckerIpRanges**](DefaultApi.md#getCheckerIpRanges) | **GET** /2013-04-01/checkeripranges |  |
| [**getDNSSEC**](DefaultApi.md#getDNSSEC) | **GET** /2013-04-01/hostedzone/{Id}/dnssec |  |
| [**getGeoLocation**](DefaultApi.md#getGeoLocation) | **GET** /2013-04-01/geolocation |  |
| [**getHealthCheck**](DefaultApi.md#getHealthCheck) | **GET** /2013-04-01/healthcheck/{HealthCheckId} |  |
| [**getHealthCheckCount**](DefaultApi.md#getHealthCheckCount) | **GET** /2013-04-01/healthcheckcount |  |
| [**getHealthCheckLastFailureReason**](DefaultApi.md#getHealthCheckLastFailureReason) | **GET** /2013-04-01/healthcheck/{HealthCheckId}/lastfailurereason |  |
| [**getHealthCheckStatus**](DefaultApi.md#getHealthCheckStatus) | **GET** /2013-04-01/healthcheck/{HealthCheckId}/status |  |
| [**getHostedZone**](DefaultApi.md#getHostedZone) | **GET** /2013-04-01/hostedzone/{Id} |  |
| [**getHostedZoneCount**](DefaultApi.md#getHostedZoneCount) | **GET** /2013-04-01/hostedzonecount |  |
| [**getHostedZoneLimit**](DefaultApi.md#getHostedZoneLimit) | **GET** /2013-04-01/hostedzonelimit/{Id}/{Type} |  |
| [**getQueryLoggingConfig**](DefaultApi.md#getQueryLoggingConfig) | **GET** /2013-04-01/queryloggingconfig/{Id} |  |
| [**getReusableDelegationSet**](DefaultApi.md#getReusableDelegationSet) | **GET** /2013-04-01/delegationset/{Id} |  |
| [**getReusableDelegationSetLimit**](DefaultApi.md#getReusableDelegationSetLimit) | **GET** /2013-04-01/reusabledelegationsetlimit/{Id}/{Type} |  |
| [**getTrafficPolicy**](DefaultApi.md#getTrafficPolicy) | **GET** /2013-04-01/trafficpolicy/{Id}/{Version} |  |
| [**getTrafficPolicyInstance**](DefaultApi.md#getTrafficPolicyInstance) | **GET** /2013-04-01/trafficpolicyinstance/{Id} |  |
| [**getTrafficPolicyInstanceCount**](DefaultApi.md#getTrafficPolicyInstanceCount) | **GET** /2013-04-01/trafficpolicyinstancecount |  |
| [**listCidrBlocks**](DefaultApi.md#listCidrBlocks) | **GET** /2013-04-01/cidrcollection/{CidrCollectionId}/cidrblocks |  |
| [**listCidrCollections**](DefaultApi.md#listCidrCollections) | **GET** /2013-04-01/cidrcollection |  |
| [**listCidrLocations**](DefaultApi.md#listCidrLocations) | **GET** /2013-04-01/cidrcollection/{CidrCollectionId} |  |
| [**listGeoLocations**](DefaultApi.md#listGeoLocations) | **GET** /2013-04-01/geolocations |  |
| [**listHealthChecks**](DefaultApi.md#listHealthChecks) | **GET** /2013-04-01/healthcheck |  |
| [**listHostedZones**](DefaultApi.md#listHostedZones) | **GET** /2013-04-01/hostedzone |  |
| [**listHostedZonesByName**](DefaultApi.md#listHostedZonesByName) | **GET** /2013-04-01/hostedzonesbyname |  |
| [**listHostedZonesByVPC**](DefaultApi.md#listHostedZonesByVPC) | **GET** /2013-04-01/hostedzonesbyvpc#vpcid&amp;vpcregion |  |
| [**listQueryLoggingConfigs**](DefaultApi.md#listQueryLoggingConfigs) | **GET** /2013-04-01/queryloggingconfig |  |
| [**listResourceRecordSets**](DefaultApi.md#listResourceRecordSets) | **GET** /2013-04-01/hostedzone/{Id}/rrset |  |
| [**listReusableDelegationSets**](DefaultApi.md#listReusableDelegationSets) | **GET** /2013-04-01/delegationset |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /2013-04-01/tags/{ResourceType}/{ResourceId} |  |
| [**listTagsForResources**](DefaultApi.md#listTagsForResources) | **POST** /2013-04-01/tags/{ResourceType} |  |
| [**listTrafficPolicies**](DefaultApi.md#listTrafficPolicies) | **GET** /2013-04-01/trafficpolicies |  |
| [**listTrafficPolicyInstances**](DefaultApi.md#listTrafficPolicyInstances) | **GET** /2013-04-01/trafficpolicyinstances |  |
| [**listTrafficPolicyInstancesByHostedZone**](DefaultApi.md#listTrafficPolicyInstancesByHostedZone) | **GET** /2013-04-01/trafficpolicyinstances/hostedzone#id |  |
| [**listTrafficPolicyInstancesByPolicy**](DefaultApi.md#listTrafficPolicyInstancesByPolicy) | **GET** /2013-04-01/trafficpolicyinstances/trafficpolicy#id&amp;version |  |
| [**listTrafficPolicyVersions**](DefaultApi.md#listTrafficPolicyVersions) | **GET** /2013-04-01/trafficpolicies/{Id}/versions |  |
| [**listVPCAssociationAuthorizations**](DefaultApi.md#listVPCAssociationAuthorizations) | **GET** /2013-04-01/hostedzone/{Id}/authorizevpcassociation |  |
| [**testDNSAnswer**](DefaultApi.md#testDNSAnswer) | **GET** /2013-04-01/testdnsanswer#hostedzoneid&amp;recordname&amp;recordtype |  |
| [**updateHealthCheck**](DefaultApi.md#updateHealthCheck) | **POST** /2013-04-01/healthcheck/{HealthCheckId} |  |
| [**updateHostedZoneComment**](DefaultApi.md#updateHostedZoneComment) | **POST** /2013-04-01/hostedzone/{Id} |  |
| [**updateTrafficPolicyComment**](DefaultApi.md#updateTrafficPolicyComment) | **POST** /2013-04-01/trafficpolicy/{Id}/{Version} |  |
| [**updateTrafficPolicyInstance**](DefaultApi.md#updateTrafficPolicyInstance) | **POST** /2013-04-01/trafficpolicyinstance/{Id} |  |


<a id="activateKeySigningKey"></a>
# **activateKeySigningKey**
> ActivateKeySigningKeyResponse activateKeySigningKey(hostedZoneId, name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Activates a key-signing key (KSK) so that it can be used for signing by DNSSEC. This operation changes the KSK status to &lt;code&gt;ACTIVE&lt;/code&gt;.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostedZoneId = "hostedZoneId_example"; // String | A unique string used to identify a hosted zone.
    String name = "name_example"; // String | A string used to identify a key-signing key (KSK). <code>Name</code> can include numbers, letters, and underscores (_). <code>Name</code> must be unique for each key-signing key in the same hosted zone.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ActivateKeySigningKeyResponse result = apiInstance.activateKeySigningKey(hostedZoneId, name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#activateKeySigningKey");
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
| **hostedZoneId** | **String**| A unique string used to identify a hosted zone. | |
| **name** | **String**| A string used to identify a key-signing key (KSK). &lt;code&gt;Name&lt;/code&gt; can include numbers, letters, and underscores (_). &lt;code&gt;Name&lt;/code&gt; must be unique for each key-signing key in the same hosted zone. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ActivateKeySigningKeyResponse**](ActivateKeySigningKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ConcurrentModification |  -  |
| **481** | NoSuchKeySigningKey |  -  |
| **482** | InvalidKeySigningKeyStatus |  -  |
| **483** | InvalidSigningStatus |  -  |
| **484** | InvalidKMSArn |  -  |
| **485** | InvalidInput |  -  |

<a id="associateVPCWithHostedZone"></a>
# **associateVPCWithHostedZone**
> AssociateVPCWithHostedZoneResponse associateVPCWithHostedZone(id, associateVPCWithHostedZoneRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Associates an Amazon VPC with a private hosted zone. &lt;/p&gt; &lt;important&gt; &lt;p&gt;To perform the association, the VPC and the private hosted zone must already exist. You can&#39;t convert a public hosted zone into a private hosted zone.&lt;/p&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;If you want to associate a VPC that was created by using one Amazon Web Services account with a private hosted zone that was created by using a different account, the Amazon Web Services account that created the private hosted zone must first submit a &lt;code&gt;CreateVPCAssociationAuthorization&lt;/code&gt; request. Then the account that created the VPC must submit an &lt;code&gt;AssociateVPCWithHostedZone&lt;/code&gt; request.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;When granting access, the hosted zone and the Amazon VPC must belong to the same partition. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.&lt;/p&gt; &lt;p&gt;The following are the supported partitions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws&lt;/code&gt; - Amazon Web Services Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-cn&lt;/code&gt; - China Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-us-gov&lt;/code&gt; - Amazon Web Services GovCloud (US) Region&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Access Management&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | <p>The ID of the private hosted zone that you want to associate an Amazon VPC with.</p> <p>Note that you can't associate a VPC with a hosted zone that doesn't have an existing VPC association.</p>
    AssociateVPCWithHostedZoneRequest associateVPCWithHostedZoneRequest = new AssociateVPCWithHostedZoneRequest(); // AssociateVPCWithHostedZoneRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AssociateVPCWithHostedZoneResponse result = apiInstance.associateVPCWithHostedZone(id, associateVPCWithHostedZoneRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associateVPCWithHostedZone");
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
| **id** | **String**| &lt;p&gt;The ID of the private hosted zone that you want to associate an Amazon VPC with.&lt;/p&gt; &lt;p&gt;Note that you can&#39;t associate a VPC with a hosted zone that doesn&#39;t have an existing VPC association.&lt;/p&gt; | |
| **associateVPCWithHostedZoneRequest** | [**AssociateVPCWithHostedZoneRequest**](AssociateVPCWithHostedZoneRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AssociateVPCWithHostedZoneResponse**](AssociateVPCWithHostedZoneResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | NotAuthorizedException |  -  |
| **482** | InvalidVPCId |  -  |
| **483** | InvalidInput |  -  |
| **484** | PublicZoneVPCAssociation |  -  |
| **485** | ConflictingDomainExists |  -  |
| **486** | LimitsExceeded |  -  |
| **487** | PriorRequestNotComplete |  -  |

<a id="changeCidrCollection"></a>
# **changeCidrCollection**
> ChangeCidrCollectionResponse changeCidrCollection(cidrCollectionId, changeCidrCollectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates, changes, or deletes CIDR blocks within a collection. Contains authoritative IP information mapping blocks to one or multiple locations.&lt;/p&gt; &lt;p&gt;A change request can update multiple locations in a collection at a time, which is helpful if you want to move one or more CIDR blocks from one location to another in one transaction, without downtime. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Limits&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The max number of CIDR blocks included in the request is 1000. As a result, big updates require multiple API calls.&lt;/p&gt; &lt;p&gt; &lt;b&gt; PUT and DELETE_IF_EXISTS&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Use &lt;code&gt;ChangeCidrCollection&lt;/code&gt; to perform the following actions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PUT&lt;/code&gt;: Create a CIDR block within the specified collection.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt; DELETE_IF_EXISTS&lt;/code&gt;: Delete an existing CIDR block from the collection.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cidrCollectionId = "cidrCollectionId_example"; // String | The UUID of the CIDR collection to update.
    ChangeCidrCollectionRequest changeCidrCollectionRequest = new ChangeCidrCollectionRequest(); // ChangeCidrCollectionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ChangeCidrCollectionResponse result = apiInstance.changeCidrCollection(cidrCollectionId, changeCidrCollectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#changeCidrCollection");
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
| **cidrCollectionId** | **String**| The UUID of the CIDR collection to update. | |
| **changeCidrCollectionRequest** | [**ChangeCidrCollectionRequest**](ChangeCidrCollectionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ChangeCidrCollectionResponse**](ChangeCidrCollectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchCidrCollectionException |  -  |
| **481** | CidrCollectionVersionMismatchException |  -  |
| **482** | InvalidInput |  -  |
| **483** | CidrBlockInUseException |  -  |
| **484** | LimitsExceeded |  -  |
| **485** | ConcurrentModification |  -  |

<a id="changeResourceRecordSets"></a>
# **changeResourceRecordSets**
> ChangeResourceRecordSetsResponse changeResourceRecordSets(id, changeResourceRecordSetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates, changes, or deletes a resource record set, which contains authoritative DNS information for a specified domain name or subdomain name. For example, you can use &lt;code&gt;ChangeResourceRecordSets&lt;/code&gt; to create a resource record set that routes traffic for test.example.com to a web server that has an IP address of 192.0.2.44.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Deleting Resource Record Sets&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To delete a resource record set, you must specify all the same values that you specified when you created it.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Change Batches and Transactional Changes&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The request body must include a document with a &lt;code&gt;ChangeResourceRecordSetsRequest&lt;/code&gt; element. The request body contains a list of change items, known as a change batch. Change batches are considered transactional changes. Route 53 validates the changes in the request and then either makes all or none of the changes in the change batch request. This ensures that DNS routing isn&#39;t adversely affected by partial changes to the resource record sets in a hosted zone. &lt;/p&gt; &lt;p&gt;For example, suppose a change batch request contains two changes: it deletes the &lt;code&gt;CNAME&lt;/code&gt; resource record set for www.example.com and creates an alias resource record set for www.example.com. If validation for both records succeeds, Route 53 deletes the first resource record set and creates the second resource record set in a single operation. If validation for either the &lt;code&gt;DELETE&lt;/code&gt; or the &lt;code&gt;CREATE&lt;/code&gt; action fails, then the request is canceled, and the original &lt;code&gt;CNAME&lt;/code&gt; record continues to exist.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you try to delete the same resource record set more than once in a single change batch, Route 53 returns an &lt;code&gt;InvalidChangeBatch&lt;/code&gt; error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Traffic Flow&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To create resource record sets for complex routing configurations, use either the traffic flow visual editor in the Route 53 console or the API actions for traffic policies and traffic policy instances. Save the configuration as a traffic policy, then associate the traffic policy with one or more domain names (such as example.com) or subdomain names (such as www.example.com), in the same hosted zone or in multiple hosted zones. You can roll back the updates if the new configuration isn&#39;t performing as expected. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-flow.html\&quot;&gt;Using Traffic Flow to Route DNS Traffic&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Create, Delete, and Upsert&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Use &lt;code&gt;ChangeResourceRecordsSetsRequest&lt;/code&gt; to perform the following actions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CREATE&lt;/code&gt;: Creates a resource record set that has the specified values.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DELETE&lt;/code&gt;: Deletes an existing resource record set that has the specified values.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UPSERT&lt;/code&gt;: If a resource set exists Route 53 updates it with the values in the request. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Syntaxes for Creating, Updating, and Deleting Resource Record Sets&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The syntax for a request depends on the type of resource record set that you want to create, delete, or update, such as weighted, alias, or failover. The XML elements in your request must appear in the order listed in the syntax. &lt;/p&gt; &lt;p&gt;For an example for each type of resource record set, see \&quot;Examples.\&quot;&lt;/p&gt; &lt;p&gt;Don&#39;t refer to the syntax in the \&quot;Parameter Syntax\&quot; section, which includes all of the elements for every kind of resource record set that you can create, delete, or update by using &lt;code&gt;ChangeResourceRecordSets&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Change Propagation to Route 53 DNS Servers&lt;/b&gt; &lt;/p&gt; &lt;p&gt;When you submit a &lt;code&gt;ChangeResourceRecordSets&lt;/code&gt; request, Route 53 propagates your changes to all of the Route 53 authoritative DNS servers managing the hosted zone. While your changes are propagating, &lt;code&gt;GetChange&lt;/code&gt; returns a status of &lt;code&gt;PENDING&lt;/code&gt;. When propagation is complete, &lt;code&gt;GetChange&lt;/code&gt; returns a status of &lt;code&gt;INSYNC&lt;/code&gt;. Changes generally propagate to all Route 53 name servers managing the hosted zone within 60 seconds. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html\&quot;&gt;GetChange&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Limits on ChangeResourceRecordSets Requests&lt;/b&gt; &lt;/p&gt; &lt;p&gt;For information about the limits on a &lt;code&gt;ChangeResourceRecordSets&lt;/code&gt; request, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html\&quot;&gt;Limits&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the hosted zone that contains the resource record sets that you want to change.
    ChangeResourceRecordSetsRequest changeResourceRecordSetsRequest = new ChangeResourceRecordSetsRequest(); // ChangeResourceRecordSetsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ChangeResourceRecordSetsResponse result = apiInstance.changeResourceRecordSets(id, changeResourceRecordSetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#changeResourceRecordSets");
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
| **id** | **String**| The ID of the hosted zone that contains the resource record sets that you want to change. | |
| **changeResourceRecordSetsRequest** | [**ChangeResourceRecordSetsRequest**](ChangeResourceRecordSetsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ChangeResourceRecordSetsResponse**](ChangeResourceRecordSetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | NoSuchHealthCheck |  -  |
| **482** | InvalidChangeBatch |  -  |
| **483** | InvalidInput |  -  |
| **484** | PriorRequestNotComplete |  -  |

<a id="changeTagsForResource"></a>
# **changeTagsForResource**
> Object changeTagsForResource(resourceType, resourceId, changeTagsForResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Adds, edits, or deletes tags for a health check or a hosted zone.&lt;/p&gt; &lt;p&gt;For information about using tags for cost allocation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management User Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceType = "healthcheck"; // String | <p>The type of the resource.</p> <ul> <li> <p>The resource type for health checks is <code>healthcheck</code>.</p> </li> <li> <p>The resource type for hosted zones is <code>hostedzone</code>.</p> </li> </ul>
    String resourceId = "resourceId_example"; // String | The ID of the resource for which you want to add, change, or delete tags.
    ChangeTagsForResourceRequest changeTagsForResourceRequest = new ChangeTagsForResourceRequest(); // ChangeTagsForResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.changeTagsForResource(resourceType, resourceId, changeTagsForResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#changeTagsForResource");
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
| **resourceType** | **String**| &lt;p&gt;The type of the resource.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The resource type for health checks is &lt;code&gt;healthcheck&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The resource type for hosted zones is &lt;code&gt;hostedzone&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [enum: healthcheck, hostedzone] |
| **resourceId** | **String**| The ID of the resource for which you want to add, change, or delete tags. | |
| **changeTagsForResourceRequest** | [**ChangeTagsForResourceRequest**](ChangeTagsForResourceRequest.md)|  | |
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

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | NoSuchHealthCheck |  -  |
| **482** | NoSuchHostedZone |  -  |
| **483** | PriorRequestNotComplete |  -  |
| **484** | ThrottlingException |  -  |

<a id="createCidrCollection"></a>
# **createCidrCollection**
> CreateCidrCollectionResponse createCidrCollection(createCidrCollectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a CIDR collection in the current Amazon Web Services account.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateCidrCollectionRequest createCidrCollectionRequest = new CreateCidrCollectionRequest(); // CreateCidrCollectionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateCidrCollectionResponse result = apiInstance.createCidrCollection(createCidrCollectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createCidrCollection");
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
| **createCidrCollectionRequest** | [**CreateCidrCollectionRequest**](CreateCidrCollectionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateCidrCollectionResponse**](CreateCidrCollectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | LimitsExceeded |  -  |
| **481** | InvalidInput |  -  |
| **482** | CidrCollectionAlreadyExistsException |  -  |
| **483** | ConcurrentModification |  -  |

<a id="createHealthCheck"></a>
# **createHealthCheck**
> CreateHealthCheckResponse createHealthCheck(createHealthCheckRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new health check.&lt;/p&gt; &lt;p&gt;For information about adding health checks to resource record sets, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecordSet.html#Route53-Type-ResourceRecordSet-HealthCheckId\&quot;&gt;HealthCheckId&lt;/a&gt; in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html\&quot;&gt;ChangeResourceRecordSets&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; &lt;b&gt;ELB Load Balancers&lt;/b&gt; &lt;/p&gt; &lt;p&gt;If you&#39;re registering EC2 instances with an Elastic Load Balancing (ELB) load balancer, do not create Amazon Route 53 health checks for the EC2 instances. When you register an EC2 instance with a load balancer, you configure settings for an ELB health check, which performs a similar function to a Route 53 health check.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Private Hosted Zones&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can associate health checks with failover resource record sets in a private hosted zone. Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Route 53 health checkers are outside the VPC. To check the health of an endpoint within a VPC by IP address, you must assign a public IP address to the instance in the VPC.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can configure a health checker to check the health of an external resource that the instance relies on, such as a database server.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can create a CloudWatch metric, associate an alarm with the metric, and then create a health check that is based on the state of the alarm. For example, you might create a CloudWatch metric that checks the status of the Amazon EC2 &lt;code&gt;StatusCheckFailed&lt;/code&gt; metric, add an alarm to the metric, and then create a health check that is based on the state of the alarm. For information about creating CloudWatch metrics and alarms by using the CloudWatch console, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.html\&quot;&gt;Amazon CloudWatch User Guide&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateHealthCheckRequest createHealthCheckRequest = new CreateHealthCheckRequest(); // CreateHealthCheckRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateHealthCheckResponse result = apiInstance.createHealthCheck(createHealthCheckRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createHealthCheck");
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
| **createHealthCheckRequest** | [**CreateHealthCheckRequest**](CreateHealthCheckRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateHealthCheckResponse**](CreateHealthCheckResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | TooManyHealthChecks |  -  |
| **481** | HealthCheckAlreadyExists |  -  |
| **482** | InvalidInput |  -  |

<a id="createHostedZone"></a>
# **createHostedZone**
> CreateHostedZoneResponse createHostedZone(createHostedZoneRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new public or private hosted zone. You create records in a public hosted zone to define how you want to route traffic on the internet for a domain, such as example.com, and its subdomains (apex.example.com, acme.example.com). You create records in a private hosted zone to define how you want to route traffic for a domain and its subdomains within one or more Amazon Virtual Private Clouds (Amazon VPCs). &lt;/p&gt; &lt;important&gt; &lt;p&gt;You can&#39;t convert a public hosted zone to a private hosted zone or vice versa. Instead, you must create a new hosted zone with the same name and create new resource record sets.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about charges for hosted zones, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/route53/pricing/\&quot;&gt;Amazon Route 53 Pricing&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can&#39;t create a hosted zone for a top-level domain (TLD) such as .com.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For public hosted zones, Route 53 automatically creates a default SOA record and four NS records for the zone. For more information about SOA and NS records, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/SOA-NSrecords.html\&quot;&gt;NS and SOA Records that Route 53 Creates for a Hosted Zone&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you want to use the same name servers for multiple public hosted zones, you can optionally associate a reusable delegation set with the hosted zone. See the &lt;code&gt;DelegationSetId&lt;/code&gt; element.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If your domain is registered with a registrar other than Route 53, you must update the name servers with your registrar to make Route 53 the DNS service for the domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html\&quot;&gt;Migrating DNS Service for an Existing Domain to Amazon Route 53&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When you submit a &lt;code&gt;CreateHostedZone&lt;/code&gt; request, the initial status of the hosted zone is &lt;code&gt;PENDING&lt;/code&gt;. For public hosted zones, this means that the NS and SOA records are not yet available on all Route 53 DNS servers. When the NS and SOA records are available, the status of the zone changes to &lt;code&gt;INSYNC&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;CreateHostedZone&lt;/code&gt; request requires the caller to have an &lt;code&gt;ec2:DescribeVpcs&lt;/code&gt; permission.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When creating private hosted zones, the Amazon VPC must belong to the same partition where the hosted zone is created. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.&lt;/p&gt; &lt;p&gt;The following are the supported partitions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws&lt;/code&gt; - Amazon Web Services Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-cn&lt;/code&gt; - China Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-us-gov&lt;/code&gt; - Amazon Web Services GovCloud (US) Region&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Access Management&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateHostedZoneRequest createHostedZoneRequest = new CreateHostedZoneRequest(); // CreateHostedZoneRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateHostedZoneResponse result = apiInstance.createHostedZone(createHostedZoneRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createHostedZone");
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
| **createHostedZoneRequest** | [**CreateHostedZoneRequest**](CreateHostedZoneRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateHostedZoneResponse**](CreateHostedZoneResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | InvalidDomainName |  -  |
| **481** | HostedZoneAlreadyExists |  -  |
| **482** | TooManyHostedZones |  -  |
| **483** | InvalidVPCId |  -  |
| **484** | InvalidInput |  -  |
| **485** | DelegationSetNotAvailable |  -  |
| **486** | ConflictingDomainExists |  -  |
| **487** | NoSuchDelegationSet |  -  |
| **488** | DelegationSetNotReusable |  -  |

<a id="createKeySigningKey"></a>
# **createKeySigningKey**
> CreateKeySigningKeyResponse createKeySigningKey(createKeySigningKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a new key-signing key (KSK) associated with a hosted zone. You can only have two KSKs per hosted zone.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateKeySigningKeyRequest createKeySigningKeyRequest = new CreateKeySigningKeyRequest(); // CreateKeySigningKeyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateKeySigningKeyResponse result = apiInstance.createKeySigningKey(createKeySigningKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createKeySigningKey");
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
| **createKeySigningKeyRequest** | [**CreateKeySigningKeyRequest**](CreateKeySigningKeyRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateKeySigningKeyResponse**](CreateKeySigningKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | InvalidArgument |  -  |
| **482** | InvalidInput |  -  |
| **483** | InvalidKMSArn |  -  |
| **484** | InvalidKeySigningKeyStatus |  -  |
| **485** | InvalidSigningStatus |  -  |
| **486** | InvalidKeySigningKeyName |  -  |
| **487** | KeySigningKeyAlreadyExists |  -  |
| **488** | TooManyKeySigningKeys |  -  |
| **489** | ConcurrentModification |  -  |

<a id="createQueryLoggingConfig"></a>
# **createQueryLoggingConfig**
> CreateQueryLoggingConfigResponse createQueryLoggingConfig(createQueryLoggingConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a configuration for DNS query logging. After you create a query logging configuration, Amazon Route 53 begins to publish log data to an Amazon CloudWatch Logs log group.&lt;/p&gt; &lt;p&gt;DNS query logs contain information about the queries that Route 53 receives for a specified public hosted zone, such as the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Route 53 edge location that responded to the DNS query&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Domain or subdomain that was requested&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;DNS record type, such as A or AAAA&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;DNS response code, such as &lt;code&gt;NoError&lt;/code&gt; or &lt;code&gt;ServFail&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;dl&gt; &lt;dt&gt;Log Group and Resource Policy&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Before you create a query logging configuration, perform the following operations.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you create a query logging configuration using the Route 53 console, Route 53 performs these operations automatically.&lt;/p&gt; &lt;/note&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create a CloudWatch Logs log group, and make note of the ARN, which you specify when you create a query logging configuration. Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must create the log group in the us-east-1 region.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You must use the same Amazon Web Services account to create the log group and the hosted zone that you want to configure query logging for.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When you create log groups for query logging, we recommend that you use a consistent prefix, for example:&lt;/p&gt; &lt;p&gt; &lt;code&gt;/aws/route53/&lt;i&gt;hosted zone name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;In the next step, you&#39;ll create a resource policy, which controls access to one or more log groups and the associated Amazon Web Services resources, such as Route 53 hosted zones. There&#39;s a limit on the number of resource policies that you can create, so we recommend that you use a consistent prefix so you can use the same resource policy for all the log groups that you create for query logging.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create a CloudWatch Logs resource policy, and give it the permissions that Route 53 needs to create log streams and to send query logs to log streams. For the value of &lt;code&gt;Resource&lt;/code&gt;, specify the ARN for the log group that you created in the previous step. To use the same resource policy for all the CloudWatch Logs log groups that you created for query logging configurations, replace the hosted zone name with &lt;code&gt;*&lt;/code&gt;, for example:&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:aws:logs:us-east-1:123412341234:log-group:/aws/route53/_*&lt;/code&gt; &lt;/p&gt; &lt;p&gt;To avoid the confused deputy problem, a security issue where an entity without a permission for an action can coerce a more-privileged entity to perform it, you can optionally limit the permissions that a service has to a resource in a resource-based policy by supplying the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;aws:SourceArn&lt;/code&gt;, supply the hosted zone ARN used in creating the query logging configuration. For example, &lt;code&gt;aws:SourceArn: arn:aws:route53:::hostedzone/hosted zone ID&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;aws:SourceAccount&lt;/code&gt;, supply the account ID for the account that creates the query logging configuration. For example, &lt;code&gt;aws:SourceAccount:111111111111&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html\&quot;&gt;The confused deputy problem&lt;/a&gt; in the &lt;i&gt;Amazon Web Services IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t use the CloudWatch console to create or edit a resource policy. You must use the CloudWatch API, one of the Amazon Web Services SDKs, or the CLI.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;/ol&gt; &lt;/dd&gt; &lt;dt&gt;Log Streams and Edge Locations&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;When Route 53 finishes creating the configuration for DNS query logging, it does the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Creates a log stream for an edge location the first time that the edge location responds to DNS queries for the specified hosted zone. That log stream is used to log all queries that Route 53 responds to for that edge location.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Begins to send query logs to the applicable log stream.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The name of each log stream is in the following format:&lt;/p&gt; &lt;p&gt; &lt;code&gt; &lt;i&gt;hosted zone ID&lt;/i&gt;/&lt;i&gt;edge location code&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;The edge location code is a three-letter code and an arbitrarily assigned number, for example, DFW3. The three-letter code typically corresponds with the International Air Transport Association airport code for an airport near the edge location. (These abbreviations might change in the future.) For a list of edge locations, see \&quot;The Route 53 Global Network\&quot; on the &lt;a href&#x3D;\&quot;http://aws.amazon.com/route53/details/\&quot;&gt;Route 53 Product Details&lt;/a&gt; page.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;Queries That Are Logged&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Query logs contain only the queries that DNS resolvers forward to Route 53. If a DNS resolver has already cached the response to a query (such as the IP address for a load balancer for example.com), the resolver will continue to return the cached response. It doesn&#39;t forward another query to Route 53 until the TTL for the corresponding resource record set expires. Depending on how many DNS queries are submitted for a resource record set, and depending on the TTL for that resource record set, query logs might contain information about only one query out of every several thousand queries that are submitted to DNS. For more information about how DNS works, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html\&quot;&gt;Routing Internet Traffic to Your Website or Web Application&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;Log File Format&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;For a list of the values in each query log and the format of each value, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html\&quot;&gt;Logging DNS Queries&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;Pricing&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;For information about charges for query logs, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudwatch/pricing/\&quot;&gt;Amazon CloudWatch Pricing&lt;/a&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;How to Stop Logging&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;If you want Route 53 to stop sending query logs to CloudWatch Logs, delete the query logging configuration. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteQueryLoggingConfig.html\&quot;&gt;DeleteQueryLoggingConfig&lt;/a&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateQueryLoggingConfigRequest createQueryLoggingConfigRequest = new CreateQueryLoggingConfigRequest(); // CreateQueryLoggingConfigRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateQueryLoggingConfigResponse result = apiInstance.createQueryLoggingConfig(createQueryLoggingConfigRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createQueryLoggingConfig");
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
| **createQueryLoggingConfigRequest** | [**CreateQueryLoggingConfigRequest**](CreateQueryLoggingConfigRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateQueryLoggingConfigResponse**](CreateQueryLoggingConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | ConcurrentModification |  -  |
| **481** | NoSuchHostedZone |  -  |
| **482** | NoSuchCloudWatchLogsLogGroup |  -  |
| **483** | InvalidInput |  -  |
| **484** | QueryLoggingConfigAlreadyExists |  -  |
| **485** | InsufficientCloudWatchLogsResourcePolicy |  -  |

<a id="createReusableDelegationSet"></a>
# **createReusableDelegationSet**
> CreateReusableDelegationSetResponse createReusableDelegationSet(createReusableDelegationSetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a delegation set (a group of four name servers) that can be reused by multiple hosted zones that were created by the same Amazon Web Services account. &lt;/p&gt; &lt;p&gt;You can also create a reusable delegation set that uses the four name servers that are associated with an existing hosted zone. Specify the hosted zone ID in the &lt;code&gt;CreateReusableDelegationSet&lt;/code&gt; request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t associate a reusable delegation set with a private hosted zone.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For information about using a reusable delegation set to configure white label name servers, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/white-label-name-servers.html\&quot;&gt;Configuring White Label Name Servers&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The process for migrating existing hosted zones to use a reusable delegation set is comparable to the process for configuring white label name servers. You need to perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create a reusable delegation set.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Recreate hosted zones, and reduce the TTL to 60 seconds or less.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Recreate resource record sets in the new hosted zones.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Change the registrar&#39;s name servers to use the name servers for the new hosted zones.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Monitor traffic for the website or application.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Change TTLs back to their original values.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;If you want to migrate existing hosted zones to use a reusable delegation set, the existing hosted zones can&#39;t use any of the name servers that are assigned to the reusable delegation set. If one or more hosted zones do use one or more name servers that are assigned to the reusable delegation set, you can do one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For small numbers of hosted zones—up to a few hundred—it&#39;s relatively easy to create reusable delegation sets until you get one that has four name servers that don&#39;t overlap with any of the name servers in your hosted zones.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For larger numbers of hosted zones, the easiest solution is to use more than one reusable delegation set.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For larger numbers of hosted zones, you can also migrate hosted zones that have overlapping name servers to hosted zones that don&#39;t have overlapping name servers, then migrate the hosted zones again to use the reusable delegation set.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateReusableDelegationSetRequest createReusableDelegationSetRequest = new CreateReusableDelegationSetRequest(); // CreateReusableDelegationSetRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateReusableDelegationSetResponse result = apiInstance.createReusableDelegationSet(createReusableDelegationSetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createReusableDelegationSet");
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
| **createReusableDelegationSetRequest** | [**CreateReusableDelegationSetRequest**](CreateReusableDelegationSetRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateReusableDelegationSetResponse**](CreateReusableDelegationSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | DelegationSetAlreadyCreated |  -  |
| **481** | LimitsExceeded |  -  |
| **482** | HostedZoneNotFound |  -  |
| **483** | InvalidArgument |  -  |
| **484** | InvalidInput |  -  |
| **485** | DelegationSetNotAvailable |  -  |
| **486** | DelegationSetAlreadyReusable |  -  |

<a id="createTrafficPolicy"></a>
# **createTrafficPolicy**
> CreateTrafficPolicyResponse createTrafficPolicy(createTrafficPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a traffic policy, which you use to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com).

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateTrafficPolicyRequest createTrafficPolicyRequest = new CreateTrafficPolicyRequest(); // CreateTrafficPolicyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateTrafficPolicyResponse result = apiInstance.createTrafficPolicy(createTrafficPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createTrafficPolicy");
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
| **createTrafficPolicyRequest** | [**CreateTrafficPolicyRequest**](CreateTrafficPolicyRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateTrafficPolicyResponse**](CreateTrafficPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | TooManyTrafficPolicies |  -  |
| **482** | TrafficPolicyAlreadyExists |  -  |
| **483** | InvalidTrafficPolicyDocument |  -  |

<a id="createTrafficPolicyInstance"></a>
# **createTrafficPolicyInstance**
> CreateTrafficPolicyInstanceResponse createTrafficPolicyInstance(createTrafficPolicyInstanceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates resource record sets in a specified hosted zone based on the settings in a specified traffic policy version. In addition, &lt;code&gt;CreateTrafficPolicyInstance&lt;/code&gt; associates the resource record sets with a specified domain name (such as example.com) or subdomain name (such as www.example.com). Amazon Route 53 responds to DNS queries for the domain or subdomain name by using the resource record sets that &lt;code&gt;CreateTrafficPolicyInstance&lt;/code&gt; created.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateTrafficPolicyInstanceRequest createTrafficPolicyInstanceRequest = new CreateTrafficPolicyInstanceRequest(); // CreateTrafficPolicyInstanceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateTrafficPolicyInstanceResponse result = apiInstance.createTrafficPolicyInstance(createTrafficPolicyInstanceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createTrafficPolicyInstance");
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
| **createTrafficPolicyInstanceRequest** | [**CreateTrafficPolicyInstanceRequest**](CreateTrafficPolicyInstanceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateTrafficPolicyInstanceResponse**](CreateTrafficPolicyInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | InvalidInput |  -  |
| **482** | TooManyTrafficPolicyInstances |  -  |
| **483** | NoSuchTrafficPolicy |  -  |
| **484** | TrafficPolicyInstanceAlreadyExists |  -  |

<a id="createTrafficPolicyVersion"></a>
# **createTrafficPolicyVersion**
> CreateTrafficPolicyVersionResponse createTrafficPolicyVersion(id, createTrafficPolicyVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a new version of an existing traffic policy. When you create a new version of a traffic policy, you specify the ID of the traffic policy that you want to update and a JSON-formatted document that describes the new version. You use traffic policies to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com). You can create a maximum of 1000 versions of a traffic policy. If you reach the limit and need to create another version, you&#39;ll need to start a new traffic policy.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the traffic policy for which you want to create a new version.
    CreateTrafficPolicyVersionRequest createTrafficPolicyVersionRequest = new CreateTrafficPolicyVersionRequest(); // CreateTrafficPolicyVersionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateTrafficPolicyVersionResponse result = apiInstance.createTrafficPolicyVersion(id, createTrafficPolicyVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createTrafficPolicyVersion");
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
| **id** | **String**| The ID of the traffic policy for which you want to create a new version. | |
| **createTrafficPolicyVersionRequest** | [**CreateTrafficPolicyVersionRequest**](CreateTrafficPolicyVersionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateTrafficPolicyVersionResponse**](CreateTrafficPolicyVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | NoSuchTrafficPolicy |  -  |
| **481** | InvalidInput |  -  |
| **482** | TooManyTrafficPolicyVersionsForCurrentPolicy |  -  |
| **483** | ConcurrentModification |  -  |
| **484** | InvalidTrafficPolicyDocument |  -  |

<a id="createVPCAssociationAuthorization"></a>
# **createVPCAssociationAuthorization**
> CreateVPCAssociationAuthorizationResponse createVPCAssociationAuthorization(id, createVPCAssociationAuthorizationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Authorizes the Amazon Web Services account that created a specified VPC to submit an &lt;code&gt;AssociateVPCWithHostedZone&lt;/code&gt; request to associate the VPC with a specified hosted zone that was created by a different account. To submit a &lt;code&gt;CreateVPCAssociationAuthorization&lt;/code&gt; request, you must use the account that created the hosted zone. After you authorize the association, use the account that created the VPC to submit an &lt;code&gt;AssociateVPCWithHostedZone&lt;/code&gt; request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you want to associate multiple VPCs that you created by using one account with a hosted zone that you created by using a different account, you must submit one authorization request for each VPC.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the private hosted zone that you want to authorize associating a VPC with.
    CreateVPCAssociationAuthorizationRequest createVPCAssociationAuthorizationRequest = new CreateVPCAssociationAuthorizationRequest(); // CreateVPCAssociationAuthorizationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateVPCAssociationAuthorizationResponse result = apiInstance.createVPCAssociationAuthorization(id, createVPCAssociationAuthorizationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createVPCAssociationAuthorization");
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
| **id** | **String**| The ID of the private hosted zone that you want to authorize associating a VPC with. | |
| **createVPCAssociationAuthorizationRequest** | [**CreateVPCAssociationAuthorizationRequest**](CreateVPCAssociationAuthorizationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateVPCAssociationAuthorizationResponse**](CreateVPCAssociationAuthorizationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ConcurrentModification |  -  |
| **481** | TooManyVPCAssociationAuthorizations |  -  |
| **482** | NoSuchHostedZone |  -  |
| **483** | InvalidVPCId |  -  |
| **484** | InvalidInput |  -  |

<a id="deactivateKeySigningKey"></a>
# **deactivateKeySigningKey**
> DeactivateKeySigningKeyResponse deactivateKeySigningKey(hostedZoneId, name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deactivates a key-signing key (KSK) so that it will not be used for signing by DNSSEC. This operation changes the KSK status to &lt;code&gt;INACTIVE&lt;/code&gt;.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostedZoneId = "hostedZoneId_example"; // String | A unique string used to identify a hosted zone.
    String name = "name_example"; // String | A string used to identify a key-signing key (KSK).
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeactivateKeySigningKeyResponse result = apiInstance.deactivateKeySigningKey(hostedZoneId, name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deactivateKeySigningKey");
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
| **hostedZoneId** | **String**| A unique string used to identify a hosted zone. | |
| **name** | **String**| A string used to identify a key-signing key (KSK). | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeactivateKeySigningKeyResponse**](DeactivateKeySigningKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ConcurrentModification |  -  |
| **481** | NoSuchKeySigningKey |  -  |
| **482** | InvalidKeySigningKeyStatus |  -  |
| **483** | InvalidSigningStatus |  -  |
| **484** | KeySigningKeyInUse |  -  |
| **485** | KeySigningKeyInParentDSRecord |  -  |
| **486** | InvalidInput |  -  |

<a id="deleteCidrCollection"></a>
# **deleteCidrCollection**
> Object deleteCidrCollection(cidrCollectionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes a CIDR collection in the current Amazon Web Services account. The collection must be empty before it can be deleted.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cidrCollectionId = "cidrCollectionId_example"; // String | The UUID of the collection to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteCidrCollection(cidrCollectionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteCidrCollection");
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
| **cidrCollectionId** | **String**| The UUID of the collection to delete. | |
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
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchCidrCollectionException |  -  |
| **481** | CidrCollectionInUseException |  -  |
| **482** | InvalidInput |  -  |
| **483** | ConcurrentModification |  -  |

<a id="deleteHealthCheck"></a>
# **deleteHealthCheck**
> Object deleteHealthCheck(healthCheckId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a health check.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Amazon Route 53 does not prevent you from deleting a health check even if the health check is associated with one or more resource record sets. If you delete a health check and you don&#39;t update the associated resource record sets, the future status of the health check can&#39;t be predicted and may change. This will affect the routing of DNS queries for your DNS failover configuration. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-deleting.html#health-checks-deleting.html\&quot;&gt;Replacing and Deleting Health Checks&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If you&#39;re using Cloud Map and you configured Cloud Map to create a Route 53 health check when you register an instance, you can&#39;t use the Route 53 &lt;code&gt;DeleteHealthCheck&lt;/code&gt; command to delete the health check. The health check is deleted automatically when you deregister the instance; there can be a delay of several hours before the health check is deleted from Route 53. &lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String healthCheckId = "healthCheckId_example"; // String | The ID of the health check that you want to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteHealthCheck(healthCheckId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteHealthCheck");
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
| **healthCheckId** | **String**| The ID of the health check that you want to delete. | |
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
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHealthCheck |  -  |
| **481** | HealthCheckInUse |  -  |
| **482** | InvalidInput |  -  |

<a id="deleteHostedZone"></a>
# **deleteHostedZone**
> DeleteHostedZoneResponse deleteHostedZone(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a hosted zone.&lt;/p&gt; &lt;p&gt;If the hosted zone was created by another service, such as Cloud Map, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DeleteHostedZone.html#delete-public-hosted-zone-created-by-another-service\&quot;&gt;Deleting Public Hosted Zones That Were Created by Another Service&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt; for information about how to delete it. (The process is the same for public and private hosted zones that were created by another service.)&lt;/p&gt; &lt;p&gt;If you want to keep your domain registration but you want to stop routing internet traffic to your website or web application, we recommend that you delete resource record sets in the hosted zone instead of deleting the hosted zone.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you delete a hosted zone, you can&#39;t undelete it. You must create a new hosted zone and update the name servers for your domain registration, which can require up to 48 hours to take effect. (If you delegated responsibility for a subdomain to a hosted zone and you delete the child hosted zone, you must update the name servers in the parent hosted zone.) In addition, if you delete a hosted zone, someone could hijack the domain and route traffic to their own resources using your domain name.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If you want to avoid the monthly charge for the hosted zone, you can transfer DNS service for the domain to a free DNS service. When you transfer DNS service, you have to update the name servers for the domain registration. If the domain is registered with Route 53, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainNameservers.html\&quot;&gt;UpdateDomainNameservers&lt;/a&gt; for information about how to replace Route 53 name servers with name servers for the new DNS service. If the domain is registered with another registrar, use the method provided by the registrar to update name servers for the domain registration. For more information, perform an internet search on \&quot;free DNS service.\&quot;&lt;/p&gt; &lt;p&gt;You can delete a hosted zone only if it contains only the default SOA record and NS resource record sets. If the hosted zone contains other resource record sets, you must delete them before you can delete the hosted zone. If you try to delete a hosted zone that contains other resource record sets, the request fails, and Route 53 returns a &lt;code&gt;HostedZoneNotEmpty&lt;/code&gt; error. For information about deleting records from your hosted zone, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html\&quot;&gt;ChangeResourceRecordSets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To verify that the hosted zone has been deleted, do one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;GetHostedZone&lt;/code&gt; action to request information about the hosted zone.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;ListHostedZones&lt;/code&gt; action to get a list of the hosted zones associated with the current Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the hosted zone you want to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteHostedZoneResponse result = apiInstance.deleteHostedZone(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteHostedZone");
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
| **id** | **String**| The ID of the hosted zone you want to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteHostedZoneResponse**](DeleteHostedZoneResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | HostedZoneNotEmpty |  -  |
| **482** | PriorRequestNotComplete |  -  |
| **483** | InvalidInput |  -  |
| **484** | InvalidDomainName |  -  |

<a id="deleteKeySigningKey"></a>
# **deleteKeySigningKey**
> DeleteKeySigningKeyResponse deleteKeySigningKey(hostedZoneId, name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a key-signing key (KSK). Before you can delete a KSK, you must deactivate it. The KSK must be deactivated before you can delete it regardless of whether the hosted zone is enabled for DNSSEC signing.&lt;/p&gt; &lt;p&gt;You can use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeactivateKeySigningKey.html\&quot;&gt;DeactivateKeySigningKey&lt;/a&gt; to deactivate the key before you delete it.&lt;/p&gt; &lt;p&gt;Use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetDNSSEC.html\&quot;&gt;GetDNSSEC&lt;/a&gt; to verify that the KSK is in an &lt;code&gt;INACTIVE&lt;/code&gt; status.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostedZoneId = "hostedZoneId_example"; // String | A unique string used to identify a hosted zone.
    String name = "name_example"; // String | A string used to identify a key-signing key (KSK).
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteKeySigningKeyResponse result = apiInstance.deleteKeySigningKey(hostedZoneId, name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteKeySigningKey");
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
| **hostedZoneId** | **String**| A unique string used to identify a hosted zone. | |
| **name** | **String**| A string used to identify a key-signing key (KSK). | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteKeySigningKeyResponse**](DeleteKeySigningKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ConcurrentModification |  -  |
| **481** | NoSuchKeySigningKey |  -  |
| **482** | InvalidKeySigningKeyStatus |  -  |
| **483** | InvalidSigningStatus |  -  |
| **484** | InvalidKMSArn |  -  |
| **485** | InvalidInput |  -  |

<a id="deleteQueryLoggingConfig"></a>
# **deleteQueryLoggingConfig**
> Object deleteQueryLoggingConfig(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a configuration for DNS query logging. If you delete a configuration, Amazon Route 53 stops sending query logs to CloudWatch Logs. Route 53 doesn&#39;t delete any logs that are already in CloudWatch Logs.&lt;/p&gt; &lt;p&gt;For more information about DNS query logs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateQueryLoggingConfig.html\&quot;&gt;CreateQueryLoggingConfig&lt;/a&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the configuration that you want to delete. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteQueryLoggingConfig(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteQueryLoggingConfig");
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
| **id** | **String**| The ID of the configuration that you want to delete.  | |
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
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ConcurrentModification |  -  |
| **481** | NoSuchQueryLoggingConfig |  -  |
| **482** | InvalidInput |  -  |

<a id="deleteReusableDelegationSet"></a>
# **deleteReusableDelegationSet**
> Object deleteReusableDelegationSet(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a reusable delegation set.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You can delete a reusable delegation set only if it isn&#39;t associated with any hosted zones.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;To verify that the reusable delegation set is not associated with any hosted zones, submit a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetReusableDelegationSet.html\&quot;&gt;GetReusableDelegationSet&lt;/a&gt; request and specify the ID of the reusable delegation set that you want to delete.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the reusable delegation set that you want to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteReusableDelegationSet(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteReusableDelegationSet");
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
| **id** | **String**| The ID of the reusable delegation set that you want to delete. | |
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
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchDelegationSet |  -  |
| **481** | DelegationSetInUse |  -  |
| **482** | DelegationSetNotReusable |  -  |
| **483** | InvalidInput |  -  |

<a id="deleteTrafficPolicy"></a>
# **deleteTrafficPolicy**
> Object deleteTrafficPolicy(id, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a traffic policy.&lt;/p&gt; &lt;p&gt;When you delete a traffic policy, Route 53 sets a flag on the policy to indicate that it has been deleted. However, Route 53 never fully deletes the traffic policy. Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Deleted traffic policies aren&#39;t listed if you run &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicies.html\&quot;&gt;ListTrafficPolicies&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; There&#39;s no way to get a list of deleted policies.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you retain the ID of the policy, you can get information about the policy, including the traffic policy document, by running &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetTrafficPolicy.html\&quot;&gt;GetTrafficPolicy&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the traffic policy that you want to delete.
    Integer version = 56; // Integer | The version number of the traffic policy that you want to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteTrafficPolicy(id, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteTrafficPolicy");
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
| **id** | **String**| The ID of the traffic policy that you want to delete. | |
| **version** | **Integer**| The version number of the traffic policy that you want to delete. | |
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
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchTrafficPolicy |  -  |
| **481** | InvalidInput |  -  |
| **482** | TrafficPolicyInUse |  -  |
| **483** | ConcurrentModification |  -  |

<a id="deleteTrafficPolicyInstance"></a>
# **deleteTrafficPolicyInstance**
> Object deleteTrafficPolicyInstance(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a traffic policy instance and all of the resource record sets that Amazon Route 53 created when you created the instance.&lt;/p&gt; &lt;note&gt; &lt;p&gt;In the Route 53 console, traffic policy instances are known as policy records.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | <p>The ID of the traffic policy instance that you want to delete. </p> <important> <p>When you delete a traffic policy instance, Amazon Route 53 also deletes all of the resource record sets that were created when you created the traffic policy instance.</p> </important>
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteTrafficPolicyInstance(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteTrafficPolicyInstance");
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
| **id** | **String**| &lt;p&gt;The ID of the traffic policy instance that you want to delete. &lt;/p&gt; &lt;important&gt; &lt;p&gt;When you delete a traffic policy instance, Amazon Route 53 also deletes all of the resource record sets that were created when you created the traffic policy instance.&lt;/p&gt; &lt;/important&gt; | |
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
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchTrafficPolicyInstance |  -  |
| **481** | InvalidInput |  -  |
| **482** | PriorRequestNotComplete |  -  |

<a id="deleteVPCAssociationAuthorization"></a>
# **deleteVPCAssociationAuthorization**
> Object deleteVPCAssociationAuthorization(id, createVPCAssociationAuthorizationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Removes authorization to submit an &lt;code&gt;AssociateVPCWithHostedZone&lt;/code&gt; request to associate a specified VPC with a hosted zone that was created by a different account. You must use the account that created the hosted zone to submit a &lt;code&gt;DeleteVPCAssociationAuthorization&lt;/code&gt; request.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Sending this request only prevents the Amazon Web Services account that created the VPC from associating the VPC with the Amazon Route 53 hosted zone in the future. If the VPC is already associated with the hosted zone, &lt;code&gt;DeleteVPCAssociationAuthorization&lt;/code&gt; won&#39;t disassociate the VPC from the hosted zone. If you want to delete an existing association, use &lt;code&gt;DisassociateVPCFromHostedZone&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | When removing authorization to associate a VPC that was created by one Amazon Web Services account with a hosted zone that was created with a different Amazon Web Services account, the ID of the hosted zone.
    CreateVPCAssociationAuthorizationRequest createVPCAssociationAuthorizationRequest = new CreateVPCAssociationAuthorizationRequest(); // CreateVPCAssociationAuthorizationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteVPCAssociationAuthorization(id, createVPCAssociationAuthorizationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVPCAssociationAuthorization");
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
| **id** | **String**| When removing authorization to associate a VPC that was created by one Amazon Web Services account with a hosted zone that was created with a different Amazon Web Services account, the ID of the hosted zone. | |
| **createVPCAssociationAuthorizationRequest** | [**CreateVPCAssociationAuthorizationRequest**](CreateVPCAssociationAuthorizationRequest.md)|  | |
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

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ConcurrentModification |  -  |
| **481** | VPCAssociationAuthorizationNotFound |  -  |
| **482** | NoSuchHostedZone |  -  |
| **483** | InvalidVPCId |  -  |
| **484** | InvalidInput |  -  |

<a id="disableHostedZoneDNSSEC"></a>
# **disableHostedZoneDNSSEC**
> DisableHostedZoneDNSSECResponse disableHostedZoneDNSSEC(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Disables DNSSEC signing in a specific hosted zone. This action does not deactivate any key-signing keys (KSKs) that are active in the hosted zone.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | A unique string used to identify a hosted zone.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DisableHostedZoneDNSSECResponse result = apiInstance.disableHostedZoneDNSSEC(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disableHostedZoneDNSSEC");
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
| **id** | **String**| A unique string used to identify a hosted zone. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DisableHostedZoneDNSSECResponse**](DisableHostedZoneDNSSECResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | InvalidArgument |  -  |
| **482** | ConcurrentModification |  -  |
| **483** | KeySigningKeyInParentDSRecord |  -  |
| **484** | DNSSECNotFound |  -  |
| **485** | InvalidKeySigningKeyStatus |  -  |
| **486** | InvalidKMSArn |  -  |
| **487** | InvalidInput |  -  |

<a id="disassociateVPCFromHostedZone"></a>
# **disassociateVPCFromHostedZone**
> DisassociateVPCFromHostedZoneResponse disassociateVPCFromHostedZone(id, disassociateVPCFromHostedZoneRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Disassociates an Amazon Virtual Private Cloud (Amazon VPC) from an Amazon Route 53 private hosted zone. Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can&#39;t disassociate the last Amazon VPC from a private hosted zone.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can&#39;t convert a private hosted zone into a public hosted zone.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can submit a &lt;code&gt;DisassociateVPCFromHostedZone&lt;/code&gt; request using either the account that created the hosted zone or the account that created the Amazon VPC.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Some services, such as Cloud Map and Amazon Elastic File System (Amazon EFS) automatically create hosted zones and associate VPCs with the hosted zones. A service can create a hosted zone using your account or using its own account. You can disassociate a VPC from a hosted zone only if the service created the hosted zone using your account.&lt;/p&gt; &lt;p&gt;When you run &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZonesByVPC.html\&quot;&gt;DisassociateVPCFromHostedZone&lt;/a&gt;, if the hosted zone has a value for &lt;code&gt;OwningAccount&lt;/code&gt;, you can use &lt;code&gt;DisassociateVPCFromHostedZone&lt;/code&gt;. If the hosted zone has a value for &lt;code&gt;OwningService&lt;/code&gt;, you can&#39;t use &lt;code&gt;DisassociateVPCFromHostedZone&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;When revoking access, the hosted zone and the Amazon VPC must belong to the same partition. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.&lt;/p&gt; &lt;p&gt;The following are the supported partitions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws&lt;/code&gt; - Amazon Web Services Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-cn&lt;/code&gt; - China Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-us-gov&lt;/code&gt; - Amazon Web Services GovCloud (US) Region&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Access Management&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the private hosted zone that you want to disassociate a VPC from.
    DisassociateVPCFromHostedZoneRequest disassociateVPCFromHostedZoneRequest = new DisassociateVPCFromHostedZoneRequest(); // DisassociateVPCFromHostedZoneRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DisassociateVPCFromHostedZoneResponse result = apiInstance.disassociateVPCFromHostedZone(id, disassociateVPCFromHostedZoneRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disassociateVPCFromHostedZone");
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
| **id** | **String**| The ID of the private hosted zone that you want to disassociate a VPC from. | |
| **disassociateVPCFromHostedZoneRequest** | [**DisassociateVPCFromHostedZoneRequest**](DisassociateVPCFromHostedZoneRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DisassociateVPCFromHostedZoneResponse**](DisassociateVPCFromHostedZoneResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | InvalidVPCId |  -  |
| **482** | VPCAssociationNotFound |  -  |
| **483** | LastVPCAssociation |  -  |
| **484** | InvalidInput |  -  |

<a id="enableHostedZoneDNSSEC"></a>
# **enableHostedZoneDNSSEC**
> EnableHostedZoneDNSSECResponse enableHostedZoneDNSSEC(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Enables DNSSEC signing in a specific hosted zone.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | A unique string used to identify a hosted zone.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      EnableHostedZoneDNSSECResponse result = apiInstance.enableHostedZoneDNSSEC(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#enableHostedZoneDNSSEC");
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
| **id** | **String**| A unique string used to identify a hosted zone. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**EnableHostedZoneDNSSECResponse**](EnableHostedZoneDNSSECResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | InvalidArgument |  -  |
| **482** | ConcurrentModification |  -  |
| **483** | KeySigningKeyWithActiveStatusNotFound |  -  |
| **484** | InvalidKMSArn |  -  |
| **485** | HostedZonePartiallyDelegated |  -  |
| **486** | DNSSECNotFound |  -  |
| **487** | InvalidKeySigningKeyStatus |  -  |
| **488** | InvalidInput |  -  |

<a id="getAccountLimit"></a>
# **getAccountLimit**
> GetAccountLimitResponse getAccountLimit(type, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets the specified limit for the current account, for example, the maximum number of health checks that you can create using the account.&lt;/p&gt; &lt;p&gt;For the default limit, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html\&quot;&gt;Limits&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;. To request a higher limit, &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create?issueType&#x3D;service-limit-increase&amp;amp;limitType&#x3D;service-code-route53\&quot;&gt;open a case&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can also view account limits in Amazon Web Services Trusted Advisor. Sign in to the Amazon Web Services Management Console and open the Trusted Advisor console at &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/trustedadvisor\&quot;&gt;https://console.aws.amazon.com/trustedadvisor/&lt;/a&gt;. Then choose &lt;b&gt;Service limits&lt;/b&gt; in the navigation pane.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String type = "MAX_HEALTH_CHECKS_BY_OWNER"; // String | <p>The limit that you want to get. Valid values include the following:</p> <ul> <li> <p> <b>MAX_HEALTH_CHECKS_BY_OWNER</b>: The maximum number of health checks that you can create using the current account.</p> </li> <li> <p> <b>MAX_HOSTED_ZONES_BY_OWNER</b>: The maximum number of hosted zones that you can create using the current account.</p> </li> <li> <p> <b>MAX_REUSABLE_DELEGATION_SETS_BY_OWNER</b>: The maximum number of reusable delegation sets that you can create using the current account.</p> </li> <li> <p> <b>MAX_TRAFFIC_POLICIES_BY_OWNER</b>: The maximum number of traffic policies that you can create using the current account.</p> </li> <li> <p> <b>MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER</b>: The maximum number of traffic policy instances that you can create using the current account. (Traffic policy instances are referred to as traffic flow policy records in the Amazon Route 53 console.)</p> </li> </ul>
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetAccountLimitResponse result = apiInstance.getAccountLimit(type, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAccountLimit");
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
| **type** | **String**| &lt;p&gt;The limit that you want to get. Valid values include the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;MAX_HEALTH_CHECKS_BY_OWNER&lt;/b&gt;: The maximum number of health checks that you can create using the current account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;MAX_HOSTED_ZONES_BY_OWNER&lt;/b&gt;: The maximum number of hosted zones that you can create using the current account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;MAX_REUSABLE_DELEGATION_SETS_BY_OWNER&lt;/b&gt;: The maximum number of reusable delegation sets that you can create using the current account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;MAX_TRAFFIC_POLICIES_BY_OWNER&lt;/b&gt;: The maximum number of traffic policies that you can create using the current account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER&lt;/b&gt;: The maximum number of traffic policy instances that you can create using the current account. (Traffic policy instances are referred to as traffic flow policy records in the Amazon Route 53 console.)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [enum: MAX_HEALTH_CHECKS_BY_OWNER, MAX_HOSTED_ZONES_BY_OWNER, MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER, MAX_REUSABLE_DELEGATION_SETS_BY_OWNER, MAX_TRAFFIC_POLICIES_BY_OWNER] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetAccountLimitResponse**](GetAccountLimitResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |

<a id="getChange"></a>
# **getChange**
> GetChangeResponse getChange(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the current status of a change batch request. The status is one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PENDING&lt;/code&gt; indicates that the changes in this request have not propagated to all Amazon Route 53 DNS servers managing the hosted zone. This is the initial status of all change batch requests.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;INSYNC&lt;/code&gt; indicates that the changes have propagated to all Route 53 DNS servers managing the hosted zone. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the change batch request. The value that you specify here is the value that <code>ChangeResourceRecordSets</code> returned in the <code>Id</code> element when you submitted the request.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetChangeResponse result = apiInstance.getChange(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getChange");
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
| **id** | **String**| The ID of the change batch request. The value that you specify here is the value that &lt;code&gt;ChangeResourceRecordSets&lt;/code&gt; returned in the &lt;code&gt;Id&lt;/code&gt; element when you submitted the request. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetChangeResponse**](GetChangeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchChange |  -  |
| **481** | InvalidInput |  -  |

<a id="getCheckerIpRanges"></a>
# **getCheckerIpRanges**
> GetCheckerIpRangesResponse getCheckerIpRanges(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Route 53 does not perform authorization for this API because it retrieves information that is already available to the public.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;code&gt;GetCheckerIpRanges&lt;/code&gt; still works, but we recommend that you download ip-ranges.json, which includes IP address ranges for all Amazon Web Services services. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-ip-addresses.html\&quot;&gt;IP Address Ranges of Amazon Route 53 Servers&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
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
    try {
      GetCheckerIpRangesResponse result = apiInstance.getCheckerIpRanges(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCheckerIpRanges");
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

### Return type

[**GetCheckerIpRangesResponse**](GetCheckerIpRangesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getDNSSEC"></a>
# **getDNSSEC**
> GetDNSSECResponse getDNSSEC(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns information about DNSSEC for a specific hosted zone, including the key-signing keys (KSKs) in the hosted zone.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | A unique string used to identify a hosted zone.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetDNSSECResponse result = apiInstance.getDNSSEC(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDNSSEC");
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
| **id** | **String**| A unique string used to identify a hosted zone. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetDNSSECResponse**](GetDNSSECResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | InvalidArgument |  -  |
| **482** | InvalidInput |  -  |

<a id="getGeoLocation"></a>
# **getGeoLocation**
> GetGeoLocationResponse getGeoLocation(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, continentcode, countrycode, subdivisioncode)



&lt;p&gt;Gets information about whether a specified geographic location is supported for Amazon Route 53 geolocation resource record sets.&lt;/p&gt; &lt;p&gt;Route 53 does not perform authorization for this API because it retrieves information that is already available to the public.&lt;/p&gt; &lt;p&gt;Use the following syntax to determine whether a continent is supported for geolocation:&lt;/p&gt; &lt;p&gt; &lt;code&gt;GET /2013-04-01/geolocation?continentcode&#x3D;&lt;i&gt;two-letter abbreviation for a continent&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;Use the following syntax to determine whether a country is supported for geolocation:&lt;/p&gt; &lt;p&gt; &lt;code&gt;GET /2013-04-01/geolocation?countrycode&#x3D;&lt;i&gt;two-character country code&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;Use the following syntax to determine whether a subdivision of a country is supported for geolocation:&lt;/p&gt; &lt;p&gt; &lt;code&gt;GET /2013-04-01/geolocation?countrycode&#x3D;&lt;i&gt;two-character country code&lt;/i&gt;&amp;amp;subdivisioncode&#x3D;&lt;i&gt;subdivision code&lt;/i&gt; &lt;/code&gt; &lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
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
    String continentcode = "continentcode_example"; // String | <p>For geolocation resource record sets, a two-letter abbreviation that identifies a continent. Amazon Route 53 supports the following continent codes:</p> <ul> <li> <p> <b>AF</b>: Africa</p> </li> <li> <p> <b>AN</b>: Antarctica</p> </li> <li> <p> <b>AS</b>: Asia</p> </li> <li> <p> <b>EU</b>: Europe</p> </li> <li> <p> <b>OC</b>: Oceania</p> </li> <li> <p> <b>NA</b>: North America</p> </li> <li> <p> <b>SA</b>: South America</p> </li> </ul>
    String countrycode = "countrycode_example"; // String | Amazon Route 53 uses the two-letter country codes that are specified in <a href=\"https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\">ISO standard 3166-1 alpha-2</a>.
    String subdivisioncode = "subdivisioncode_example"; // String | The code for the subdivision, such as a particular state within the United States. For a list of US state abbreviations, see <a href=\"https://pe.usps.com/text/pub28/28apb.htm\">Appendix B: Two–Letter State and Possession Abbreviations</a> on the United States Postal Service website. For a list of all supported subdivision codes, use the <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListGeoLocations.html\">ListGeoLocations</a> API.
    try {
      GetGeoLocationResponse result = apiInstance.getGeoLocation(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, continentcode, countrycode, subdivisioncode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getGeoLocation");
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
| **continentcode** | **String**| &lt;p&gt;For geolocation resource record sets, a two-letter abbreviation that identifies a continent. Amazon Route 53 supports the following continent codes:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;AF&lt;/b&gt;: Africa&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;AN&lt;/b&gt;: Antarctica&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;AS&lt;/b&gt;: Asia&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;EU&lt;/b&gt;: Europe&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;OC&lt;/b&gt;: Oceania&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;NA&lt;/b&gt;: North America&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;SA&lt;/b&gt;: South America&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |
| **countrycode** | **String**| Amazon Route 53 uses the two-letter country codes that are specified in &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\&quot;&gt;ISO standard 3166-1 alpha-2&lt;/a&gt;. | [optional] |
| **subdivisioncode** | **String**| The code for the subdivision, such as a particular state within the United States. For a list of US state abbreviations, see &lt;a href&#x3D;\&quot;https://pe.usps.com/text/pub28/28apb.htm\&quot;&gt;Appendix B: Two–Letter State and Possession Abbreviations&lt;/a&gt; on the United States Postal Service website. For a list of all supported subdivision codes, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListGeoLocations.html\&quot;&gt;ListGeoLocations&lt;/a&gt; API. | [optional] |

### Return type

[**GetGeoLocationResponse**](GetGeoLocationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchGeoLocation |  -  |
| **481** | InvalidInput |  -  |

<a id="getHealthCheck"></a>
# **getHealthCheck**
> GetHealthCheckResponse getHealthCheck(healthCheckId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets information about a specified health check.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String healthCheckId = "healthCheckId_example"; // String | The identifier that Amazon Route 53 assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetHealthCheckResponse result = apiInstance.getHealthCheck(healthCheckId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getHealthCheck");
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
| **healthCheckId** | **String**| The identifier that Amazon Route 53 assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetHealthCheckResponse**](GetHealthCheckResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHealthCheck |  -  |
| **481** | InvalidInput |  -  |
| **482** | IncompatibleVersion |  -  |

<a id="getHealthCheckCount"></a>
# **getHealthCheckCount**
> GetHealthCheckCountResponse getHealthCheckCount(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves the number of health checks that are associated with the current Amazon Web Services account.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
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
    try {
      GetHealthCheckCountResponse result = apiInstance.getHealthCheckCount(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getHealthCheckCount");
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

### Return type

[**GetHealthCheckCountResponse**](GetHealthCheckCountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getHealthCheckLastFailureReason"></a>
# **getHealthCheckLastFailureReason**
> GetHealthCheckLastFailureReasonResponse getHealthCheckLastFailureReason(healthCheckId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets the reason that a specified health check failed most recently.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String healthCheckId = "healthCheckId_example"; // String | <p>The ID for the health check for which you want the last failure reason. When you created the health check, <code>CreateHealthCheck</code> returned the ID in the response, in the <code>HealthCheckId</code> element.</p> <note> <p>If you want to get the last failure reason for a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can't use <code>GetHealthCheckLastFailureReason</code> for a calculated health check.</p> </note>
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetHealthCheckLastFailureReasonResponse result = apiInstance.getHealthCheckLastFailureReason(healthCheckId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getHealthCheckLastFailureReason");
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
| **healthCheckId** | **String**| &lt;p&gt;The ID for the health check for which you want the last failure reason. When you created the health check, &lt;code&gt;CreateHealthCheck&lt;/code&gt; returned the ID in the response, in the &lt;code&gt;HealthCheckId&lt;/code&gt; element.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you want to get the last failure reason for a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can&#39;t use &lt;code&gt;GetHealthCheckLastFailureReason&lt;/code&gt; for a calculated health check.&lt;/p&gt; &lt;/note&gt; | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetHealthCheckLastFailureReasonResponse**](GetHealthCheckLastFailureReasonResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHealthCheck |  -  |
| **481** | InvalidInput |  -  |

<a id="getHealthCheckStatus"></a>
# **getHealthCheckStatus**
> GetHealthCheckStatusResponse getHealthCheckStatus(healthCheckId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets status of a specified health check. &lt;/p&gt; &lt;important&gt; &lt;p&gt;This API is intended for use during development to diagnose behavior. It doesn’t support production use-cases with high query rates that require immediate and actionable responses.&lt;/p&gt; &lt;/important&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String healthCheckId = "healthCheckId_example"; // String | <p>The ID for the health check that you want the current status for. When you created the health check, <code>CreateHealthCheck</code> returned the ID in the response, in the <code>HealthCheckId</code> element.</p> <note> <p>If you want to check the status of a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can't use <code>GetHealthCheckStatus</code> to get the status of a calculated health check.</p> </note>
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetHealthCheckStatusResponse result = apiInstance.getHealthCheckStatus(healthCheckId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getHealthCheckStatus");
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
| **healthCheckId** | **String**| &lt;p&gt;The ID for the health check that you want the current status for. When you created the health check, &lt;code&gt;CreateHealthCheck&lt;/code&gt; returned the ID in the response, in the &lt;code&gt;HealthCheckId&lt;/code&gt; element.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you want to check the status of a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can&#39;t use &lt;code&gt;GetHealthCheckStatus&lt;/code&gt; to get the status of a calculated health check.&lt;/p&gt; &lt;/note&gt; | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetHealthCheckStatusResponse**](GetHealthCheckStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHealthCheck |  -  |
| **481** | InvalidInput |  -  |

<a id="getHostedZone"></a>
# **getHostedZone**
> GetHostedZoneResponse getHostedZone(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets information about a specified hosted zone including the four name servers assigned to the hosted zone.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the hosted zone that you want to get information about.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetHostedZoneResponse result = apiInstance.getHostedZone(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getHostedZone");
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
| **id** | **String**| The ID of the hosted zone that you want to get information about. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetHostedZoneResponse**](GetHostedZoneResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | InvalidInput |  -  |

<a id="getHostedZoneCount"></a>
# **getHostedZoneCount**
> GetHostedZoneCountResponse getHostedZoneCount(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves the number of hosted zones that are associated with the current Amazon Web Services account.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
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
    try {
      GetHostedZoneCountResponse result = apiInstance.getHostedZoneCount(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getHostedZoneCount");
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

### Return type

[**GetHostedZoneCountResponse**](GetHostedZoneCountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |

<a id="getHostedZoneLimit"></a>
# **getHostedZoneLimit**
> GetHostedZoneLimitResponse getHostedZoneLimit(type, id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets the specified limit for a specified hosted zone, for example, the maximum number of records that you can create in the hosted zone. &lt;/p&gt; &lt;p&gt;For the default limit, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html\&quot;&gt;Limits&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;. To request a higher limit, &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create?issueType&#x3D;service-limit-increase&amp;amp;limitType&#x3D;service-code-route53\&quot;&gt;open a case&lt;/a&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String type = "MAX_RRSETS_BY_ZONE"; // String | <p>The limit that you want to get. Valid values include the following:</p> <ul> <li> <p> <b>MAX_RRSETS_BY_ZONE</b>: The maximum number of records that you can create in the specified hosted zone.</p> </li> <li> <p> <b>MAX_VPCS_ASSOCIATED_BY_ZONE</b>: The maximum number of Amazon VPCs that you can associate with the specified private hosted zone.</p> </li> </ul>
    String id = "id_example"; // String | The ID of the hosted zone that you want to get a limit for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetHostedZoneLimitResponse result = apiInstance.getHostedZoneLimit(type, id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getHostedZoneLimit");
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
| **type** | **String**| &lt;p&gt;The limit that you want to get. Valid values include the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;MAX_RRSETS_BY_ZONE&lt;/b&gt;: The maximum number of records that you can create in the specified hosted zone.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;MAX_VPCS_ASSOCIATED_BY_ZONE&lt;/b&gt;: The maximum number of Amazon VPCs that you can associate with the specified private hosted zone.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [enum: MAX_RRSETS_BY_ZONE, MAX_VPCS_ASSOCIATED_BY_ZONE] |
| **id** | **String**| The ID of the hosted zone that you want to get a limit for. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetHostedZoneLimitResponse**](GetHostedZoneLimitResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | InvalidInput |  -  |
| **482** | HostedZoneNotPrivate |  -  |

<a id="getQueryLoggingConfig"></a>
# **getQueryLoggingConfig**
> GetQueryLoggingConfigResponse getQueryLoggingConfig(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets information about a specified configuration for DNS query logging.&lt;/p&gt; &lt;p&gt;For more information about DNS query logs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateQueryLoggingConfig.html\&quot;&gt;CreateQueryLoggingConfig&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html\&quot;&gt;Logging DNS Queries&lt;/a&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the configuration for DNS query logging that you want to get information about.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetQueryLoggingConfigResponse result = apiInstance.getQueryLoggingConfig(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getQueryLoggingConfig");
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
| **id** | **String**| The ID of the configuration for DNS query logging that you want to get information about. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetQueryLoggingConfigResponse**](GetQueryLoggingConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchQueryLoggingConfig |  -  |
| **481** | InvalidInput |  -  |

<a id="getReusableDelegationSet"></a>
# **getReusableDelegationSet**
> GetReusableDelegationSetResponse getReusableDelegationSet(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves information about a specified reusable delegation set, including the four name servers that are assigned to the delegation set.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the reusable delegation set that you want to get a list of name servers for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetReusableDelegationSetResponse result = apiInstance.getReusableDelegationSet(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReusableDelegationSet");
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
| **id** | **String**| The ID of the reusable delegation set that you want to get a list of name servers for. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetReusableDelegationSetResponse**](GetReusableDelegationSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchDelegationSet |  -  |
| **481** | DelegationSetNotReusable |  -  |
| **482** | InvalidInput |  -  |

<a id="getReusableDelegationSetLimit"></a>
# **getReusableDelegationSetLimit**
> GetReusableDelegationSetLimitResponse getReusableDelegationSetLimit(type, id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets the maximum number of hosted zones that you can associate with the specified reusable delegation set.&lt;/p&gt; &lt;p&gt;For the default limit, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html\&quot;&gt;Limits&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;. To request a higher limit, &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create?issueType&#x3D;service-limit-increase&amp;amp;limitType&#x3D;service-code-route53\&quot;&gt;open a case&lt;/a&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String type = "MAX_ZONES_BY_REUSABLE_DELEGATION_SET"; // String | Specify <code>MAX_ZONES_BY_REUSABLE_DELEGATION_SET</code> to get the maximum number of hosted zones that you can associate with the specified reusable delegation set.
    String id = "id_example"; // String | The ID of the delegation set that you want to get the limit for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetReusableDelegationSetLimitResponse result = apiInstance.getReusableDelegationSetLimit(type, id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReusableDelegationSetLimit");
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
| **type** | **String**| Specify &lt;code&gt;MAX_ZONES_BY_REUSABLE_DELEGATION_SET&lt;/code&gt; to get the maximum number of hosted zones that you can associate with the specified reusable delegation set. | [enum: MAX_ZONES_BY_REUSABLE_DELEGATION_SET] |
| **id** | **String**| The ID of the delegation set that you want to get the limit for. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetReusableDelegationSetLimitResponse**](GetReusableDelegationSetLimitResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | NoSuchDelegationSet |  -  |

<a id="getTrafficPolicy"></a>
# **getTrafficPolicy**
> GetTrafficPolicyResponse getTrafficPolicy(id, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets information about a specific traffic policy version.&lt;/p&gt; &lt;p&gt;For information about how of deleting a traffic policy affects the response from &lt;code&gt;GetTrafficPolicy&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicy.html\&quot;&gt;DeleteTrafficPolicy&lt;/a&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the traffic policy that you want to get information about.
    Integer version = 56; // Integer | The version number of the traffic policy that you want to get information about.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetTrafficPolicyResponse result = apiInstance.getTrafficPolicy(id, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getTrafficPolicy");
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
| **id** | **String**| The ID of the traffic policy that you want to get information about. | |
| **version** | **Integer**| The version number of the traffic policy that you want to get information about. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetTrafficPolicyResponse**](GetTrafficPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchTrafficPolicy |  -  |
| **481** | InvalidInput |  -  |

<a id="getTrafficPolicyInstance"></a>
# **getTrafficPolicyInstance**
> GetTrafficPolicyInstanceResponse getTrafficPolicyInstance(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets information about a specified traffic policy instance.&lt;/p&gt; &lt;note&gt; &lt;p&gt;After you submit a &lt;code&gt;CreateTrafficPolicyInstance&lt;/code&gt; or an &lt;code&gt;UpdateTrafficPolicyInstance&lt;/code&gt; request, there&#39;s a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the &lt;code&gt;State&lt;/code&gt; response element.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;In the Route 53 console, traffic policy instances are known as policy records.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the traffic policy instance that you want to get information about.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetTrafficPolicyInstanceResponse result = apiInstance.getTrafficPolicyInstance(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getTrafficPolicyInstance");
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
| **id** | **String**| The ID of the traffic policy instance that you want to get information about. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetTrafficPolicyInstanceResponse**](GetTrafficPolicyInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchTrafficPolicyInstance |  -  |
| **481** | InvalidInput |  -  |

<a id="getTrafficPolicyInstanceCount"></a>
# **getTrafficPolicyInstanceCount**
> GetTrafficPolicyInstanceCountResponse getTrafficPolicyInstanceCount(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets the number of traffic policy instances that are associated with the current Amazon Web Services account.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
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
    try {
      GetTrafficPolicyInstanceCountResponse result = apiInstance.getTrafficPolicyInstanceCount(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getTrafficPolicyInstanceCount");
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

### Return type

[**GetTrafficPolicyInstanceCountResponse**](GetTrafficPolicyInstanceCountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listCidrBlocks"></a>
# **listCidrBlocks**
> ListCidrBlocksResponse listCidrBlocks(cidrCollectionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, location, nexttoken, maxresults, maxResults, nextToken)



Returns a paginated list of location objects and their CIDR blocks.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cidrCollectionId = "cidrCollectionId_example"; // String | The UUID of the CIDR collection.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String location = "location_example"; // String | The name of the CIDR collection location.
    String nexttoken = "nexttoken_example"; // String | An opaque pagination token to indicate where the service is to begin enumerating results.
    String maxresults = "maxresults_example"; // String | Maximum number of results you want returned.
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListCidrBlocksResponse result = apiInstance.listCidrBlocks(cidrCollectionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, location, nexttoken, maxresults, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listCidrBlocks");
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
| **cidrCollectionId** | **String**| The UUID of the CIDR collection. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **location** | **String**| The name of the CIDR collection location. | [optional] |
| **nexttoken** | **String**| An opaque pagination token to indicate where the service is to begin enumerating results. | [optional] |
| **maxresults** | **String**| Maximum number of results you want returned. | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListCidrBlocksResponse**](ListCidrBlocksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchCidrCollectionException |  -  |
| **481** | NoSuchCidrLocationException |  -  |
| **482** | InvalidInput |  -  |

<a id="listCidrCollections"></a>
# **listCidrCollections**
> ListCidrCollectionsResponse listCidrCollections(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nexttoken, maxresults, maxResults, nextToken)



Returns a paginated list of CIDR collections in the Amazon Web Services account (metadata only).

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
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
    String nexttoken = "nexttoken_example"; // String | <p>An opaque pagination token to indicate where the service is to begin enumerating results.</p> <p>If no value is provided, the listing of results starts from the beginning.</p>
    String maxresults = "maxresults_example"; // String | The maximum number of CIDR collections to return in the response.
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListCidrCollectionsResponse result = apiInstance.listCidrCollections(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nexttoken, maxresults, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listCidrCollections");
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
| **nexttoken** | **String**| &lt;p&gt;An opaque pagination token to indicate where the service is to begin enumerating results.&lt;/p&gt; &lt;p&gt;If no value is provided, the listing of results starts from the beginning.&lt;/p&gt; | [optional] |
| **maxresults** | **String**| The maximum number of CIDR collections to return in the response. | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListCidrCollectionsResponse**](ListCidrCollectionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |

<a id="listCidrLocations"></a>
# **listCidrLocations**
> ListCidrLocationsResponse listCidrLocations(cidrCollectionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nexttoken, maxresults, maxResults, nextToken)



Returns a paginated list of CIDR locations for the given collection (metadata only, does not include CIDR blocks).

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cidrCollectionId = "cidrCollectionId_example"; // String | The CIDR collection ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nexttoken = "nexttoken_example"; // String | <p>An opaque pagination token to indicate where the service is to begin enumerating results.</p> <p>If no value is provided, the listing of results starts from the beginning.</p>
    String maxresults = "maxresults_example"; // String | The maximum number of CIDR collection locations to return in the response.
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListCidrLocationsResponse result = apiInstance.listCidrLocations(cidrCollectionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nexttoken, maxresults, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listCidrLocations");
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
| **cidrCollectionId** | **String**| The CIDR collection ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nexttoken** | **String**| &lt;p&gt;An opaque pagination token to indicate where the service is to begin enumerating results.&lt;/p&gt; &lt;p&gt;If no value is provided, the listing of results starts from the beginning.&lt;/p&gt; | [optional] |
| **maxresults** | **String**| The maximum number of CIDR collection locations to return in the response. | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListCidrLocationsResponse**](ListCidrLocationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchCidrCollectionException |  -  |
| **481** | InvalidInput |  -  |

<a id="listGeoLocations"></a>
# **listGeoLocations**
> ListGeoLocationsResponse listGeoLocations(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, startcontinentcode, startcountrycode, startsubdivisioncode, maxitems)



&lt;p&gt;Retrieves a list of supported geographic locations.&lt;/p&gt; &lt;p&gt;Countries are listed first, and continents are listed last. If Amazon Route 53 supports subdivisions for a country (for example, states or provinces), the subdivisions for that country are listed in alphabetical order immediately after the corresponding country.&lt;/p&gt; &lt;p&gt;Route 53 does not perform authorization for this API because it retrieves information that is already available to the public.&lt;/p&gt; &lt;p&gt;For a list of supported geolocation codes, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_GeoLocation.html\&quot;&gt;GeoLocation&lt;/a&gt; data type.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
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
    String startcontinentcode = "startcontinentcode_example"; // String | <p>The code for the continent with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if <code>IsTruncated</code> is true, and if <code>NextContinentCode</code> from the previous response has a value, enter that value in <code>startcontinentcode</code> to return the next page of results.</p> <p>Include <code>startcontinentcode</code> only if you want to list continents. Don't include <code>startcontinentcode</code> when you're listing countries or countries with their subdivisions.</p>
    String startcountrycode = "startcountrycode_example"; // String | The code for the country with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if <code>IsTruncated</code> is <code>true</code>, and if <code>NextCountryCode</code> from the previous response has a value, enter that value in <code>startcountrycode</code> to return the next page of results.
    String startsubdivisioncode = "startsubdivisioncode_example"; // String | <p>The code for the state of the United States with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if <code>IsTruncated</code> is <code>true</code>, and if <code>NextSubdivisionCode</code> from the previous response has a value, enter that value in <code>startsubdivisioncode</code> to return the next page of results.</p> <p>To list subdivisions (U.S. states), you must include both <code>startcountrycode</code> and <code>startsubdivisioncode</code>.</p>
    String maxitems = "maxitems_example"; // String | (Optional) The maximum number of geolocations to be included in the response body for this request. If more than <code>maxitems</code> geolocations remain to be listed, then the value of the <code>IsTruncated</code> element in the response is <code>true</code>.
    try {
      ListGeoLocationsResponse result = apiInstance.listGeoLocations(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, startcontinentcode, startcountrycode, startsubdivisioncode, maxitems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listGeoLocations");
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
| **startcontinentcode** | **String**| &lt;p&gt;The code for the continent with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if &lt;code&gt;IsTruncated&lt;/code&gt; is true, and if &lt;code&gt;NextContinentCode&lt;/code&gt; from the previous response has a value, enter that value in &lt;code&gt;startcontinentcode&lt;/code&gt; to return the next page of results.&lt;/p&gt; &lt;p&gt;Include &lt;code&gt;startcontinentcode&lt;/code&gt; only if you want to list continents. Don&#39;t include &lt;code&gt;startcontinentcode&lt;/code&gt; when you&#39;re listing countries or countries with their subdivisions.&lt;/p&gt; | [optional] |
| **startcountrycode** | **String**| The code for the country with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if &lt;code&gt;IsTruncated&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;, and if &lt;code&gt;NextCountryCode&lt;/code&gt; from the previous response has a value, enter that value in &lt;code&gt;startcountrycode&lt;/code&gt; to return the next page of results. | [optional] |
| **startsubdivisioncode** | **String**| &lt;p&gt;The code for the state of the United States with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if &lt;code&gt;IsTruncated&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;, and if &lt;code&gt;NextSubdivisionCode&lt;/code&gt; from the previous response has a value, enter that value in &lt;code&gt;startsubdivisioncode&lt;/code&gt; to return the next page of results.&lt;/p&gt; &lt;p&gt;To list subdivisions (U.S. states), you must include both &lt;code&gt;startcountrycode&lt;/code&gt; and &lt;code&gt;startsubdivisioncode&lt;/code&gt;.&lt;/p&gt; | [optional] |
| **maxitems** | **String**| (Optional) The maximum number of geolocations to be included in the response body for this request. If more than &lt;code&gt;maxitems&lt;/code&gt; geolocations remain to be listed, then the value of the &lt;code&gt;IsTruncated&lt;/code&gt; element in the response is &lt;code&gt;true&lt;/code&gt;. | [optional] |

### Return type

[**ListGeoLocationsResponse**](ListGeoLocationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |

<a id="listHealthChecks"></a>
# **listHealthChecks**
> ListHealthChecksResponse listHealthChecks(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxitems, maxItems, marker2)



Retrieve a list of the health checks that are associated with the current Amazon Web Services account. 

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
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
    String marker = "marker_example"; // String | <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more health checks. To get another group, submit another <code>ListHealthChecks</code> request. </p> <p>For the value of <code>marker</code>, specify the value of <code>NextMarker</code> from the previous response, which is the ID of the first health check that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more health checks to get.</p>
    String maxitems = "maxitems_example"; // String | The maximum number of health checks that you want <code>ListHealthChecks</code> to return in response to the current request. Amazon Route 53 returns a maximum of 100 items. If you set <code>MaxItems</code> to a value greater than 100, Route 53 returns only the first 100 health checks. 
    String maxItems = "maxItems_example"; // String | Pagination limit
    String marker2 = "marker_example"; // String | Pagination token
    try {
      ListHealthChecksResponse result = apiInstance.listHealthChecks(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxitems, maxItems, marker2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listHealthChecks");
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
| **marker** | **String**| &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more health checks. To get another group, submit another &lt;code&gt;ListHealthChecks&lt;/code&gt; request. &lt;/p&gt; &lt;p&gt;For the value of &lt;code&gt;marker&lt;/code&gt;, specify the value of &lt;code&gt;NextMarker&lt;/code&gt; from the previous response, which is the ID of the first health check that Amazon Route 53 will return if you submit another request.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more health checks to get.&lt;/p&gt; | [optional] |
| **maxitems** | **String**| The maximum number of health checks that you want &lt;code&gt;ListHealthChecks&lt;/code&gt; to return in response to the current request. Amazon Route 53 returns a maximum of 100 items. If you set &lt;code&gt;MaxItems&lt;/code&gt; to a value greater than 100, Route 53 returns only the first 100 health checks.  | [optional] |
| **maxItems** | **String**| Pagination limit | [optional] |
| **marker2** | **String**| Pagination token | [optional] |

### Return type

[**ListHealthChecksResponse**](ListHealthChecksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | IncompatibleVersion |  -  |

<a id="listHostedZones"></a>
# **listHostedZones**
> ListHostedZonesResponse listHostedZones(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxitems, delegationsetid, maxItems, marker2)



&lt;p&gt;Retrieves a list of the public and private hosted zones that are associated with the current Amazon Web Services account. The response includes a &lt;code&gt;HostedZones&lt;/code&gt; child element for each hosted zone.&lt;/p&gt; &lt;p&gt;Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of hosted zones, you can use the &lt;code&gt;maxitems&lt;/code&gt; parameter to list them in groups of up to 100.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
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
    String marker = "marker_example"; // String | <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more hosted zones. To get more hosted zones, submit another <code>ListHostedZones</code> request. </p> <p>For the value of <code>marker</code>, specify the value of <code>NextMarker</code> from the previous response, which is the ID of the first hosted zone that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more hosted zones to get.</p>
    String maxitems = "maxitems_example"; // String | (Optional) The maximum number of hosted zones that you want Amazon Route 53 to return. If you have more than <code>maxitems</code> hosted zones, the value of <code>IsTruncated</code> in the response is <code>true</code>, and the value of <code>NextMarker</code> is the hosted zone ID of the first hosted zone that Route 53 will return if you submit another request.
    String delegationsetid = "delegationsetid_example"; // String | If you're using reusable delegation sets and you want to list all of the hosted zones that are associated with a reusable delegation set, specify the ID of that reusable delegation set. 
    String maxItems = "maxItems_example"; // String | Pagination limit
    String marker2 = "marker_example"; // String | Pagination token
    try {
      ListHostedZonesResponse result = apiInstance.listHostedZones(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxitems, delegationsetid, maxItems, marker2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listHostedZones");
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
| **marker** | **String**| &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more hosted zones. To get more hosted zones, submit another &lt;code&gt;ListHostedZones&lt;/code&gt; request. &lt;/p&gt; &lt;p&gt;For the value of &lt;code&gt;marker&lt;/code&gt;, specify the value of &lt;code&gt;NextMarker&lt;/code&gt; from the previous response, which is the ID of the first hosted zone that Amazon Route 53 will return if you submit another request.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more hosted zones to get.&lt;/p&gt; | [optional] |
| **maxitems** | **String**| (Optional) The maximum number of hosted zones that you want Amazon Route 53 to return. If you have more than &lt;code&gt;maxitems&lt;/code&gt; hosted zones, the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the response is &lt;code&gt;true&lt;/code&gt;, and the value of &lt;code&gt;NextMarker&lt;/code&gt; is the hosted zone ID of the first hosted zone that Route 53 will return if you submit another request. | [optional] |
| **delegationsetid** | **String**| If you&#39;re using reusable delegation sets and you want to list all of the hosted zones that are associated with a reusable delegation set, specify the ID of that reusable delegation set.  | [optional] |
| **maxItems** | **String**| Pagination limit | [optional] |
| **marker2** | **String**| Pagination token | [optional] |

### Return type

[**ListHostedZonesResponse**](ListHostedZonesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | NoSuchDelegationSet |  -  |
| **482** | DelegationSetNotReusable |  -  |

<a id="listHostedZonesByName"></a>
# **listHostedZonesByName**
> ListHostedZonesByNameResponse listHostedZonesByName(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, dnsname, hostedzoneid, maxitems)



&lt;p&gt;Retrieves a list of your hosted zones in lexicographic order. The response includes a &lt;code&gt;HostedZones&lt;/code&gt; child element for each hosted zone created by the current Amazon Web Services account. &lt;/p&gt; &lt;p&gt; &lt;code&gt;ListHostedZonesByName&lt;/code&gt; sorts hosted zones by name with the labels reversed. For example:&lt;/p&gt; &lt;p&gt; &lt;code&gt;com.example.www.&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Note the trailing dot, which can change the sort order in some circumstances.&lt;/p&gt; &lt;p&gt;If the domain name includes escape characters or Punycode, &lt;code&gt;ListHostedZonesByName&lt;/code&gt; alphabetizes the domain name using the escaped or Punycoded value, which is the format that Amazon Route 53 saves in its database. For example, to create a hosted zone for exämple.com, you specify ex\\344mple.com for the domain name. &lt;code&gt;ListHostedZonesByName&lt;/code&gt; alphabetizes it as:&lt;/p&gt; &lt;p&gt; &lt;code&gt;com.ex\\344mple.&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The labels are reversed and alphabetized using the escaped value. For more information about valid domain name formats, including internationalized domain names, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html\&quot;&gt;DNS Domain Name Format&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Route 53 returns up to 100 items in each response. If you have a lot of hosted zones, use the &lt;code&gt;MaxItems&lt;/code&gt; parameter to list them in groups of up to 100. The response includes values that help navigate from one group of &lt;code&gt;MaxItems&lt;/code&gt; hosted zones to the next:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;DNSName&lt;/code&gt; and &lt;code&gt;HostedZoneId&lt;/code&gt; elements in the response contain the values, if any, specified for the &lt;code&gt;dnsname&lt;/code&gt; and &lt;code&gt;hostedzoneid&lt;/code&gt; parameters in the request that produced the current response.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;MaxItems&lt;/code&gt; element in the response contains the value, if any, that you specified for the &lt;code&gt;maxitems&lt;/code&gt; parameter in the request that produced the current response.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the response is true, there are more hosted zones associated with the current Amazon Web Services account. &lt;/p&gt; &lt;p&gt;If &lt;code&gt;IsTruncated&lt;/code&gt; is false, this response includes the last hosted zone that is associated with the current account. The &lt;code&gt;NextDNSName&lt;/code&gt; element and &lt;code&gt;NextHostedZoneId&lt;/code&gt; elements are omitted from the response.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;NextDNSName&lt;/code&gt; and &lt;code&gt;NextHostedZoneId&lt;/code&gt; elements in the response contain the domain name and the hosted zone ID of the next hosted zone that is associated with the current Amazon Web Services account. If you want to list more hosted zones, make another call to &lt;code&gt;ListHostedZonesByName&lt;/code&gt;, and specify the value of &lt;code&gt;NextDNSName&lt;/code&gt; and &lt;code&gt;NextHostedZoneId&lt;/code&gt; in the &lt;code&gt;dnsname&lt;/code&gt; and &lt;code&gt;hostedzoneid&lt;/code&gt; parameters, respectively.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
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
    String dnsname = "dnsname_example"; // String | (Optional) For your first request to <code>ListHostedZonesByName</code>, include the <code>dnsname</code> parameter only if you want to specify the name of the first hosted zone in the response. If you don't include the <code>dnsname</code> parameter, Amazon Route 53 returns all of the hosted zones that were created by the current Amazon Web Services account, in ASCII order. For subsequent requests, include both <code>dnsname</code> and <code>hostedzoneid</code> parameters. For <code>dnsname</code>, specify the value of <code>NextDNSName</code> from the previous response.
    String hostedzoneid = "hostedzoneid_example"; // String | <p>(Optional) For your first request to <code>ListHostedZonesByName</code>, do not include the <code>hostedzoneid</code> parameter.</p> <p>If you have more hosted zones than the value of <code>maxitems</code>, <code>ListHostedZonesByName</code> returns only the first <code>maxitems</code> hosted zones. To get the next group of <code>maxitems</code> hosted zones, submit another request to <code>ListHostedZonesByName</code> and include both <code>dnsname</code> and <code>hostedzoneid</code> parameters. For the value of <code>hostedzoneid</code>, specify the value of the <code>NextHostedZoneId</code> element from the previous response.</p>
    String maxitems = "maxitems_example"; // String | The maximum number of hosted zones to be included in the response body for this request. If you have more than <code>maxitems</code> hosted zones, then the value of the <code>IsTruncated</code> element in the response is true, and the values of <code>NextDNSName</code> and <code>NextHostedZoneId</code> specify the first hosted zone in the next group of <code>maxitems</code> hosted zones. 
    try {
      ListHostedZonesByNameResponse result = apiInstance.listHostedZonesByName(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, dnsname, hostedzoneid, maxitems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listHostedZonesByName");
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
| **dnsname** | **String**| (Optional) For your first request to &lt;code&gt;ListHostedZonesByName&lt;/code&gt;, include the &lt;code&gt;dnsname&lt;/code&gt; parameter only if you want to specify the name of the first hosted zone in the response. If you don&#39;t include the &lt;code&gt;dnsname&lt;/code&gt; parameter, Amazon Route 53 returns all of the hosted zones that were created by the current Amazon Web Services account, in ASCII order. For subsequent requests, include both &lt;code&gt;dnsname&lt;/code&gt; and &lt;code&gt;hostedzoneid&lt;/code&gt; parameters. For &lt;code&gt;dnsname&lt;/code&gt;, specify the value of &lt;code&gt;NextDNSName&lt;/code&gt; from the previous response. | [optional] |
| **hostedzoneid** | **String**| &lt;p&gt;(Optional) For your first request to &lt;code&gt;ListHostedZonesByName&lt;/code&gt;, do not include the &lt;code&gt;hostedzoneid&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;If you have more hosted zones than the value of &lt;code&gt;maxitems&lt;/code&gt;, &lt;code&gt;ListHostedZonesByName&lt;/code&gt; returns only the first &lt;code&gt;maxitems&lt;/code&gt; hosted zones. To get the next group of &lt;code&gt;maxitems&lt;/code&gt; hosted zones, submit another request to &lt;code&gt;ListHostedZonesByName&lt;/code&gt; and include both &lt;code&gt;dnsname&lt;/code&gt; and &lt;code&gt;hostedzoneid&lt;/code&gt; parameters. For the value of &lt;code&gt;hostedzoneid&lt;/code&gt;, specify the value of the &lt;code&gt;NextHostedZoneId&lt;/code&gt; element from the previous response.&lt;/p&gt; | [optional] |
| **maxitems** | **String**| The maximum number of hosted zones to be included in the response body for this request. If you have more than &lt;code&gt;maxitems&lt;/code&gt; hosted zones, then the value of the &lt;code&gt;IsTruncated&lt;/code&gt; element in the response is true, and the values of &lt;code&gt;NextDNSName&lt;/code&gt; and &lt;code&gt;NextHostedZoneId&lt;/code&gt; specify the first hosted zone in the next group of &lt;code&gt;maxitems&lt;/code&gt; hosted zones.  | [optional] |

### Return type

[**ListHostedZonesByNameResponse**](ListHostedZonesByNameResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | InvalidDomainName |  -  |

<a id="listHostedZonesByVPC"></a>
# **listHostedZonesByVPC**
> ListHostedZonesByVPCResponse listHostedZonesByVPC(vpcid, vpcregion, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxitems, nexttoken)



&lt;p&gt;Lists all the private hosted zones that a specified VPC is associated with, regardless of which Amazon Web Services account or Amazon Web Services service owns the hosted zones. The &lt;code&gt;HostedZoneOwner&lt;/code&gt; structure in the response contains one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;An &lt;code&gt;OwningAccount&lt;/code&gt; element, which contains the account number of either the current Amazon Web Services account or another Amazon Web Services account. Some services, such as Cloud Map, create hosted zones using the current account. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An &lt;code&gt;OwningService&lt;/code&gt; element, which identifies the Amazon Web Services service that created and owns the hosted zone. For example, if a hosted zone was created by Amazon Elastic File System (Amazon EFS), the value of &lt;code&gt;Owner&lt;/code&gt; is &lt;code&gt;efs.amazonaws.com&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;When listing private hosted zones, the hosted zone and the Amazon VPC must belong to the same partition where the hosted zones were created. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.&lt;/p&gt; &lt;p&gt;The following are the supported partitions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws&lt;/code&gt; - Amazon Web Services Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-cn&lt;/code&gt; - China Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-us-gov&lt;/code&gt; - Amazon Web Services GovCloud (US) Region&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Access Management&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String vpcid = "vpcid_example"; // String | The ID of the Amazon VPC that you want to list hosted zones for.
    String vpcregion = "us-east-1"; // String | For the Amazon VPC that you specified for <code>VPCId</code>, the Amazon Web Services Region that you created the VPC in. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxitems = "maxitems_example"; // String | (Optional) The maximum number of hosted zones that you want Amazon Route 53 to return. If the specified VPC is associated with more than <code>MaxItems</code> hosted zones, the response includes a <code>NextToken</code> element. <code>NextToken</code> contains an encrypted token that identifies the first hosted zone that Route 53 will return if you submit another request.
    String nexttoken = "nexttoken_example"; // String | <p>If the previous response included a <code>NextToken</code> element, the specified VPC is associated with more hosted zones. To get more hosted zones, submit another <code>ListHostedZonesByVPC</code> request. </p> <p>For the value of <code>NextToken</code>, specify the value of <code>NextToken</code> from the previous response.</p> <p>If the previous response didn't include a <code>NextToken</code> element, there are no more hosted zones to get.</p>
    try {
      ListHostedZonesByVPCResponse result = apiInstance.listHostedZonesByVPC(vpcid, vpcregion, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxitems, nexttoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listHostedZonesByVPC");
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
| **vpcid** | **String**| The ID of the Amazon VPC that you want to list hosted zones for. | |
| **vpcregion** | **String**| For the Amazon VPC that you specified for &lt;code&gt;VPCId&lt;/code&gt;, the Amazon Web Services Region that you created the VPC in.  | [enum: us-east-1, us-east-2, us-west-1, us-west-2, eu-west-1, eu-west-2, eu-west-3, eu-central-1, eu-central-2, ap-east-1, me-south-1, us-gov-west-1, us-gov-east-1, us-iso-east-1, us-iso-west-1, us-isob-east-1, me-central-1, ap-southeast-1, ap-southeast-2, ap-southeast-3, ap-south-1, ap-south-2, ap-northeast-1, ap-northeast-2, ap-northeast-3, eu-north-1, sa-east-1, ca-central-1, cn-north-1, af-south-1, eu-south-1, eu-south-2, ap-southeast-4, il-central-1] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxitems** | **String**| (Optional) The maximum number of hosted zones that you want Amazon Route 53 to return. If the specified VPC is associated with more than &lt;code&gt;MaxItems&lt;/code&gt; hosted zones, the response includes a &lt;code&gt;NextToken&lt;/code&gt; element. &lt;code&gt;NextToken&lt;/code&gt; contains an encrypted token that identifies the first hosted zone that Route 53 will return if you submit another request. | [optional] |
| **nexttoken** | **String**| &lt;p&gt;If the previous response included a &lt;code&gt;NextToken&lt;/code&gt; element, the specified VPC is associated with more hosted zones. To get more hosted zones, submit another &lt;code&gt;ListHostedZonesByVPC&lt;/code&gt; request. &lt;/p&gt; &lt;p&gt;For the value of &lt;code&gt;NextToken&lt;/code&gt;, specify the value of &lt;code&gt;NextToken&lt;/code&gt; from the previous response.&lt;/p&gt; &lt;p&gt;If the previous response didn&#39;t include a &lt;code&gt;NextToken&lt;/code&gt; element, there are no more hosted zones to get.&lt;/p&gt; | [optional] |

### Return type

[**ListHostedZonesByVPCResponse**](ListHostedZonesByVPCResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | InvalidPaginationToken |  -  |

<a id="listQueryLoggingConfigs"></a>
# **listQueryLoggingConfigs**
> ListQueryLoggingConfigsResponse listQueryLoggingConfigs(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, hostedzoneid, nexttoken, maxresults, maxResults, nextToken)



&lt;p&gt;Lists the configurations for DNS query logging that are associated with the current Amazon Web Services account or the configuration that is associated with a specified hosted zone.&lt;/p&gt; &lt;p&gt;For more information about DNS query logs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateQueryLoggingConfig.html\&quot;&gt;CreateQueryLoggingConfig&lt;/a&gt;. Additional information, including the format of DNS query logs, appears in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html\&quot;&gt;Logging DNS Queries&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
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
    String hostedzoneid = "hostedzoneid_example"; // String | <p>(Optional) If you want to list the query logging configuration that is associated with a hosted zone, specify the ID in <code>HostedZoneId</code>. </p> <p>If you don't specify a hosted zone ID, <code>ListQueryLoggingConfigs</code> returns all of the configurations that are associated with the current Amazon Web Services account.</p>
    String nexttoken = "nexttoken_example"; // String | <p>(Optional) If the current Amazon Web Services account has more than <code>MaxResults</code> query logging configurations, use <code>NextToken</code> to get the second and subsequent pages of results.</p> <p>For the first <code>ListQueryLoggingConfigs</code> request, omit this value.</p> <p>For the second and subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request.</p>
    String maxresults = "maxresults_example"; // String | <p>(Optional) The maximum number of query logging configurations that you want Amazon Route 53 to return in response to the current request. If the current Amazon Web Services account has more than <code>MaxResults</code> configurations, use the value of <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListQueryLoggingConfigs.html#API_ListQueryLoggingConfigs_RequestSyntax\">NextToken</a> in the response to get the next page of results.</p> <p>If you don't specify a value for <code>MaxResults</code>, Route 53 returns up to 100 configurations.</p>
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListQueryLoggingConfigsResponse result = apiInstance.listQueryLoggingConfigs(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, hostedzoneid, nexttoken, maxresults, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listQueryLoggingConfigs");
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
| **hostedzoneid** | **String**| &lt;p&gt;(Optional) If you want to list the query logging configuration that is associated with a hosted zone, specify the ID in &lt;code&gt;HostedZoneId&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;If you don&#39;t specify a hosted zone ID, &lt;code&gt;ListQueryLoggingConfigs&lt;/code&gt; returns all of the configurations that are associated with the current Amazon Web Services account.&lt;/p&gt; | [optional] |
| **nexttoken** | **String**| &lt;p&gt;(Optional) If the current Amazon Web Services account has more than &lt;code&gt;MaxResults&lt;/code&gt; query logging configurations, use &lt;code&gt;NextToken&lt;/code&gt; to get the second and subsequent pages of results.&lt;/p&gt; &lt;p&gt;For the first &lt;code&gt;ListQueryLoggingConfigs&lt;/code&gt; request, omit this value.&lt;/p&gt; &lt;p&gt;For the second and subsequent requests, get the value of &lt;code&gt;NextToken&lt;/code&gt; from the previous response and specify that value for &lt;code&gt;NextToken&lt;/code&gt; in the request.&lt;/p&gt; | [optional] |
| **maxresults** | **String**| &lt;p&gt;(Optional) The maximum number of query logging configurations that you want Amazon Route 53 to return in response to the current request. If the current Amazon Web Services account has more than &lt;code&gt;MaxResults&lt;/code&gt; configurations, use the value of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListQueryLoggingConfigs.html#API_ListQueryLoggingConfigs_RequestSyntax\&quot;&gt;NextToken&lt;/a&gt; in the response to get the next page of results.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for &lt;code&gt;MaxResults&lt;/code&gt;, Route 53 returns up to 100 configurations.&lt;/p&gt; | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListQueryLoggingConfigsResponse**](ListQueryLoggingConfigsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | InvalidPaginationToken |  -  |
| **482** | NoSuchHostedZone |  -  |

<a id="listResourceRecordSets"></a>
# **listResourceRecordSets**
> ListResourceRecordSetsResponse listResourceRecordSets(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, name, type, identifier, maxitems, maxItems, startRecordName, startRecordType, startRecordIdentifier)



&lt;p&gt;Lists the resource record sets in a specified hosted zone.&lt;/p&gt; &lt;p&gt; &lt;code&gt;ListResourceRecordSets&lt;/code&gt; returns up to 300 resource record sets at a time in ASCII order, beginning at a position specified by the &lt;code&gt;name&lt;/code&gt; and &lt;code&gt;type&lt;/code&gt; elements.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Sort order&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt;ListResourceRecordSets&lt;/code&gt; sorts results first by DNS name with the labels reversed, for example:&lt;/p&gt; &lt;p&gt; &lt;code&gt;com.example.www.&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Note the trailing dot, which can change the sort order when the record name contains characters that appear before &lt;code&gt;.&lt;/code&gt; (decimal 46) in the ASCII table. These characters include the following: &lt;code&gt;! \&quot; # $ % &amp;amp; &#39; ( ) * + , -&lt;/code&gt; &lt;/p&gt; &lt;p&gt;When multiple records have the same DNS name, &lt;code&gt;ListResourceRecordSets&lt;/code&gt; sorts results by the record type.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Specifying where to start listing records&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use the name and type elements to specify the resource record set that the list begins with:&lt;/p&gt; &lt;dl&gt; &lt;dt&gt;If you do not specify Name or Type&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;The results begin with the first resource record set that the hosted zone contains.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;If you specify Name but not Type&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;The results begin with the first resource record set in the list whose name is greater than or equal to &lt;code&gt;Name&lt;/code&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;If you specify Type but not Name&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Amazon Route 53 returns the &lt;code&gt;InvalidInput&lt;/code&gt; error.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;If you specify both Name and Type&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;The results begin with the first resource record set in the list whose name is greater than or equal to &lt;code&gt;Name&lt;/code&gt;, and whose type is greater than or equal to &lt;code&gt;Type&lt;/code&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt; &lt;p&gt; &lt;b&gt;Resource record sets that are PENDING&lt;/b&gt; &lt;/p&gt; &lt;p&gt;This action returns the most current version of the records. This includes records that are &lt;code&gt;PENDING&lt;/code&gt;, and that are not yet available on all Route 53 DNS servers.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Changing resource record sets&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To ensure that you get an accurate listing of the resource record sets for a hosted zone at a point in time, do not submit a &lt;code&gt;ChangeResourceRecordSets&lt;/code&gt; request while you&#39;re paging through the results of a &lt;code&gt;ListResourceRecordSets&lt;/code&gt; request. If you do, some pages may display results without the latest changes while other pages display results with the latest changes.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Displaying the next page of results&lt;/b&gt; &lt;/p&gt; &lt;p&gt;If a &lt;code&gt;ListResourceRecordSets&lt;/code&gt; command returns more than one page of results, the value of &lt;code&gt;IsTruncated&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. To display the next page of results, get the values of &lt;code&gt;NextRecordName&lt;/code&gt;, &lt;code&gt;NextRecordType&lt;/code&gt;, and &lt;code&gt;NextRecordIdentifier&lt;/code&gt; (if any) from the response. Then submit another &lt;code&gt;ListResourceRecordSets&lt;/code&gt; request, and specify those values for &lt;code&gt;StartRecordName&lt;/code&gt;, &lt;code&gt;StartRecordType&lt;/code&gt;, and &lt;code&gt;StartRecordIdentifier&lt;/code&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the hosted zone that contains the resource record sets that you want to list.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String name = "name_example"; // String | The first name in the lexicographic ordering of resource record sets that you want to list. If the specified record name doesn't exist, the results begin with the first resource record set that has a name greater than the value of <code>name</code>.
    String type = "SOA"; // String | <p>The type of resource record set to begin the record listing from.</p> <p>Valid values for basic resource record sets: <code>A</code> | <code>AAAA</code> | <code>CAA</code> | <code>CNAME</code> | <code>MX</code> | <code>NAPTR</code> | <code>NS</code> | <code>PTR</code> | <code>SOA</code> | <code>SPF</code> | <code>SRV</code> | <code>TXT</code> </p> <p>Values for weighted, latency, geolocation, and failover resource record sets: <code>A</code> | <code>AAAA</code> | <code>CAA</code> | <code>CNAME</code> | <code>MX</code> | <code>NAPTR</code> | <code>PTR</code> | <code>SPF</code> | <code>SRV</code> | <code>TXT</code> </p> <p>Values for alias resource record sets: </p> <ul> <li> <p> <b>API Gateway custom regional API or edge-optimized API</b>: A</p> </li> <li> <p> <b>CloudFront distribution</b>: A or AAAA</p> </li> <li> <p> <b>Elastic Beanstalk environment that has a regionalized subdomain</b>: A</p> </li> <li> <p> <b>Elastic Load Balancing load balancer</b>: A | AAAA</p> </li> <li> <p> <b>S3 bucket</b>: A</p> </li> <li> <p> <b>VPC interface VPC endpoint</b>: A</p> </li> <li> <p> <b>Another resource record set in this hosted zone:</b> The type of the resource record set that the alias references.</p> </li> </ul> <p>Constraint: Specifying <code>type</code> without specifying <code>name</code> returns an <code>InvalidInput</code> error.</p>
    String identifier = "identifier_example"; // String |  <i>Resource record sets that have a routing policy other than simple:</i> If results were truncated for a given DNS name and type, specify the value of <code>NextRecordIdentifier</code> from the previous response to get the next resource record set that has the current DNS name and type.
    String maxitems = "maxitems_example"; // String | (Optional) The maximum number of resource records sets to include in the response body for this request. If the response includes more than <code>maxitems</code> resource record sets, the value of the <code>IsTruncated</code> element in the response is <code>true</code>, and the values of the <code>NextRecordName</code> and <code>NextRecordType</code> elements in the response identify the first resource record set in the next group of <code>maxitems</code> resource record sets.
    String maxItems = "maxItems_example"; // String | Pagination limit
    String startRecordName = "startRecordName_example"; // String | Pagination token
    String startRecordType = "startRecordType_example"; // String | Pagination token
    String startRecordIdentifier = "startRecordIdentifier_example"; // String | Pagination token
    try {
      ListResourceRecordSetsResponse result = apiInstance.listResourceRecordSets(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, name, type, identifier, maxitems, maxItems, startRecordName, startRecordType, startRecordIdentifier);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listResourceRecordSets");
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
| **id** | **String**| The ID of the hosted zone that contains the resource record sets that you want to list. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **name** | **String**| The first name in the lexicographic ordering of resource record sets that you want to list. If the specified record name doesn&#39;t exist, the results begin with the first resource record set that has a name greater than the value of &lt;code&gt;name&lt;/code&gt;. | [optional] |
| **type** | **String**| &lt;p&gt;The type of resource record set to begin the record listing from.&lt;/p&gt; &lt;p&gt;Valid values for basic resource record sets: &lt;code&gt;A&lt;/code&gt; | &lt;code&gt;AAAA&lt;/code&gt; | &lt;code&gt;CAA&lt;/code&gt; | &lt;code&gt;CNAME&lt;/code&gt; | &lt;code&gt;MX&lt;/code&gt; | &lt;code&gt;NAPTR&lt;/code&gt; | &lt;code&gt;NS&lt;/code&gt; | &lt;code&gt;PTR&lt;/code&gt; | &lt;code&gt;SOA&lt;/code&gt; | &lt;code&gt;SPF&lt;/code&gt; | &lt;code&gt;SRV&lt;/code&gt; | &lt;code&gt;TXT&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Values for weighted, latency, geolocation, and failover resource record sets: &lt;code&gt;A&lt;/code&gt; | &lt;code&gt;AAAA&lt;/code&gt; | &lt;code&gt;CAA&lt;/code&gt; | &lt;code&gt;CNAME&lt;/code&gt; | &lt;code&gt;MX&lt;/code&gt; | &lt;code&gt;NAPTR&lt;/code&gt; | &lt;code&gt;PTR&lt;/code&gt; | &lt;code&gt;SPF&lt;/code&gt; | &lt;code&gt;SRV&lt;/code&gt; | &lt;code&gt;TXT&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Values for alias resource record sets: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;API Gateway custom regional API or edge-optimized API&lt;/b&gt;: A&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;CloudFront distribution&lt;/b&gt;: A or AAAA&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Elastic Beanstalk environment that has a regionalized subdomain&lt;/b&gt;: A&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Elastic Load Balancing load balancer&lt;/b&gt;: A | AAAA&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;S3 bucket&lt;/b&gt;: A&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;VPC interface VPC endpoint&lt;/b&gt;: A&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Another resource record set in this hosted zone:&lt;/b&gt; The type of the resource record set that the alias references.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Constraint: Specifying &lt;code&gt;type&lt;/code&gt; without specifying &lt;code&gt;name&lt;/code&gt; returns an &lt;code&gt;InvalidInput&lt;/code&gt; error.&lt;/p&gt; | [optional] [enum: SOA, A, TXT, NS, CNAME, MX, NAPTR, PTR, SRV, SPF, AAAA, CAA, DS] |
| **identifier** | **String**|  &lt;i&gt;Resource record sets that have a routing policy other than simple:&lt;/i&gt; If results were truncated for a given DNS name and type, specify the value of &lt;code&gt;NextRecordIdentifier&lt;/code&gt; from the previous response to get the next resource record set that has the current DNS name and type. | [optional] |
| **maxitems** | **String**| (Optional) The maximum number of resource records sets to include in the response body for this request. If the response includes more than &lt;code&gt;maxitems&lt;/code&gt; resource record sets, the value of the &lt;code&gt;IsTruncated&lt;/code&gt; element in the response is &lt;code&gt;true&lt;/code&gt;, and the values of the &lt;code&gt;NextRecordName&lt;/code&gt; and &lt;code&gt;NextRecordType&lt;/code&gt; elements in the response identify the first resource record set in the next group of &lt;code&gt;maxitems&lt;/code&gt; resource record sets. | [optional] |
| **maxItems** | **String**| Pagination limit | [optional] |
| **startRecordName** | **String**| Pagination token | [optional] |
| **startRecordType** | **String**| Pagination token | [optional] |
| **startRecordIdentifier** | **String**| Pagination token | [optional] |

### Return type

[**ListResourceRecordSetsResponse**](ListResourceRecordSetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | InvalidInput |  -  |

<a id="listReusableDelegationSets"></a>
# **listReusableDelegationSets**
> ListReusableDelegationSetsResponse listReusableDelegationSets(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxitems)



Retrieves a list of the reusable delegation sets that are associated with the current Amazon Web Services account.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
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
    String marker = "marker_example"; // String | <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more reusable delegation sets. To get another group, submit another <code>ListReusableDelegationSets</code> request. </p> <p>For the value of <code>marker</code>, specify the value of <code>NextMarker</code> from the previous response, which is the ID of the first reusable delegation set that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more reusable delegation sets to get.</p>
    String maxitems = "maxitems_example"; // String | The number of reusable delegation sets that you want Amazon Route 53 to return in the response to this request. If you specify a value greater than 100, Route 53 returns only the first 100 reusable delegation sets.
    try {
      ListReusableDelegationSetsResponse result = apiInstance.listReusableDelegationSets(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, marker, maxitems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listReusableDelegationSets");
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
| **marker** | **String**| &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more reusable delegation sets. To get another group, submit another &lt;code&gt;ListReusableDelegationSets&lt;/code&gt; request. &lt;/p&gt; &lt;p&gt;For the value of &lt;code&gt;marker&lt;/code&gt;, specify the value of &lt;code&gt;NextMarker&lt;/code&gt; from the previous response, which is the ID of the first reusable delegation set that Amazon Route 53 will return if you submit another request.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more reusable delegation sets to get.&lt;/p&gt; | [optional] |
| **maxitems** | **String**| The number of reusable delegation sets that you want Amazon Route 53 to return in the response to this request. If you specify a value greater than 100, Route 53 returns only the first 100 reusable delegation sets. | [optional] |

### Return type

[**ListReusableDelegationSetsResponse**](ListReusableDelegationSetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceResponse listTagsForResource(resourceType, resourceId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Lists tags for one health check or hosted zone. &lt;/p&gt; &lt;p&gt;For information about using tags for cost allocation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management User Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceType = "healthcheck"; // String | <p>The type of the resource.</p> <ul> <li> <p>The resource type for health checks is <code>healthcheck</code>.</p> </li> <li> <p>The resource type for hosted zones is <code>hostedzone</code>.</p> </li> </ul>
    String resourceId = "resourceId_example"; // String | The ID of the resource for which you want to retrieve tags.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceResponse result = apiInstance.listTagsForResource(resourceType, resourceId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **resourceType** | **String**| &lt;p&gt;The type of the resource.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The resource type for health checks is &lt;code&gt;healthcheck&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The resource type for hosted zones is &lt;code&gt;hostedzone&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [enum: healthcheck, hostedzone] |
| **resourceId** | **String**| The ID of the resource for which you want to retrieve tags. | |
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
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | NoSuchHealthCheck |  -  |
| **482** | NoSuchHostedZone |  -  |
| **483** | PriorRequestNotComplete |  -  |
| **484** | ThrottlingException |  -  |

<a id="listTagsForResources"></a>
# **listTagsForResources**
> ListTagsForResourcesResponse listTagsForResources(resourceType, listTagsForResourcesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Lists tags for up to 10 health checks or hosted zones.&lt;/p&gt; &lt;p&gt;For information about using tags for cost allocation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management User Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceType = "healthcheck"; // String | <p>The type of the resources.</p> <ul> <li> <p>The resource type for health checks is <code>healthcheck</code>.</p> </li> <li> <p>The resource type for hosted zones is <code>hostedzone</code>.</p> </li> </ul>
    ListTagsForResourcesRequest listTagsForResourcesRequest = new ListTagsForResourcesRequest(); // ListTagsForResourcesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourcesResponse result = apiInstance.listTagsForResources(resourceType, listTagsForResourcesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForResources");
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
| **resourceType** | **String**| &lt;p&gt;The type of the resources.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The resource type for health checks is &lt;code&gt;healthcheck&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The resource type for hosted zones is &lt;code&gt;hostedzone&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [enum: healthcheck, hostedzone] |
| **listTagsForResourcesRequest** | [**ListTagsForResourcesRequest**](ListTagsForResourcesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListTagsForResourcesResponse**](ListTagsForResourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | NoSuchHealthCheck |  -  |
| **482** | NoSuchHostedZone |  -  |
| **483** | PriorRequestNotComplete |  -  |
| **484** | ThrottlingException |  -  |

<a id="listTrafficPolicies"></a>
# **listTrafficPolicies**
> ListTrafficPoliciesResponse listTrafficPolicies(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, trafficpolicyid, maxitems)



&lt;p&gt;Gets information about the latest version for every traffic policy that is associated with the current Amazon Web Services account. Policies are listed in the order that they were created in. &lt;/p&gt; &lt;p&gt;For information about how of deleting a traffic policy affects the response from &lt;code&gt;ListTrafficPolicies&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicy.html\&quot;&gt;DeleteTrafficPolicy&lt;/a&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
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
    String trafficpolicyid = "trafficpolicyid_example"; // String | <p>(Conditional) For your first request to <code>ListTrafficPolicies</code>, don't include the <code>TrafficPolicyIdMarker</code> parameter.</p> <p>If you have more traffic policies than the value of <code>MaxItems</code>, <code>ListTrafficPolicies</code> returns only the first <code>MaxItems</code> traffic policies. To get the next group of policies, submit another request to <code>ListTrafficPolicies</code>. For the value of <code>TrafficPolicyIdMarker</code>, specify the value of <code>TrafficPolicyIdMarker</code> that was returned in the previous response.</p>
    String maxitems = "maxitems_example"; // String | (Optional) The maximum number of traffic policies that you want Amazon Route 53 to return in response to this request. If you have more than <code>MaxItems</code> traffic policies, the value of <code>IsTruncated</code> in the response is <code>true</code>, and the value of <code>TrafficPolicyIdMarker</code> is the ID of the first traffic policy that Route 53 will return if you submit another request.
    try {
      ListTrafficPoliciesResponse result = apiInstance.listTrafficPolicies(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, trafficpolicyid, maxitems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTrafficPolicies");
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
| **trafficpolicyid** | **String**| &lt;p&gt;(Conditional) For your first request to &lt;code&gt;ListTrafficPolicies&lt;/code&gt;, don&#39;t include the &lt;code&gt;TrafficPolicyIdMarker&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;If you have more traffic policies than the value of &lt;code&gt;MaxItems&lt;/code&gt;, &lt;code&gt;ListTrafficPolicies&lt;/code&gt; returns only the first &lt;code&gt;MaxItems&lt;/code&gt; traffic policies. To get the next group of policies, submit another request to &lt;code&gt;ListTrafficPolicies&lt;/code&gt;. For the value of &lt;code&gt;TrafficPolicyIdMarker&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyIdMarker&lt;/code&gt; that was returned in the previous response.&lt;/p&gt; | [optional] |
| **maxitems** | **String**| (Optional) The maximum number of traffic policies that you want Amazon Route 53 to return in response to this request. If you have more than &lt;code&gt;MaxItems&lt;/code&gt; traffic policies, the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the response is &lt;code&gt;true&lt;/code&gt;, and the value of &lt;code&gt;TrafficPolicyIdMarker&lt;/code&gt; is the ID of the first traffic policy that Route 53 will return if you submit another request. | [optional] |

### Return type

[**ListTrafficPoliciesResponse**](ListTrafficPoliciesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |

<a id="listTrafficPolicyInstances"></a>
# **listTrafficPolicyInstances**
> ListTrafficPolicyInstancesResponse listTrafficPolicyInstances(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, hostedzoneid, trafficpolicyinstancename, trafficpolicyinstancetype, maxitems)



&lt;p&gt;Gets information about the traffic policy instances that you created by using the current Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;After you submit an &lt;code&gt;UpdateTrafficPolicyInstance&lt;/code&gt; request, there&#39;s a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the &lt;code&gt;State&lt;/code&gt; response element.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the &lt;code&gt;MaxItems&lt;/code&gt; parameter to list them in groups of up to 100.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
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
    String hostedzoneid = "hostedzoneid_example"; // String | <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstances</code> request. For the value of <code>HostedZoneId</code>, specify the value of <code>HostedZoneIdMarker</code> from the previous response, which is the hosted zone ID of the first traffic policy instance in the next group of traffic policy instances.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
    String trafficpolicyinstancename = "trafficpolicyinstancename_example"; // String | <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstances</code> request. For the value of <code>trafficpolicyinstancename</code>, specify the value of <code>TrafficPolicyInstanceNameMarker</code> from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
    String trafficpolicyinstancetype = "SOA"; // String | <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstances</code> request. For the value of <code>trafficpolicyinstancetype</code>, specify the value of <code>TrafficPolicyInstanceTypeMarker</code> from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
    String maxitems = "maxitems_example"; // String | The maximum number of traffic policy instances that you want Amazon Route 53 to return in response to a <code>ListTrafficPolicyInstances</code> request. If you have more than <code>MaxItems</code> traffic policy instances, the value of the <code>IsTruncated</code> element in the response is <code>true</code>, and the values of <code>HostedZoneIdMarker</code>, <code>TrafficPolicyInstanceNameMarker</code>, and <code>TrafficPolicyInstanceTypeMarker</code> represent the first traffic policy instance in the next group of <code>MaxItems</code> traffic policy instances.
    try {
      ListTrafficPolicyInstancesResponse result = apiInstance.listTrafficPolicyInstances(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, hostedzoneid, trafficpolicyinstancename, trafficpolicyinstancetype, maxitems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTrafficPolicyInstances");
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
| **hostedzoneid** | **String**| &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstances&lt;/code&gt; request. For the value of &lt;code&gt;HostedZoneId&lt;/code&gt;, specify the value of &lt;code&gt;HostedZoneIdMarker&lt;/code&gt; from the previous response, which is the hosted zone ID of the first traffic policy instance in the next group of traffic policy instances.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt; | [optional] |
| **trafficpolicyinstancename** | **String**| &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstances&lt;/code&gt; request. For the value of &lt;code&gt;trafficpolicyinstancename&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyInstanceNameMarker&lt;/code&gt; from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt; | [optional] |
| **trafficpolicyinstancetype** | **String**| &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstances&lt;/code&gt; request. For the value of &lt;code&gt;trafficpolicyinstancetype&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyInstanceTypeMarker&lt;/code&gt; from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt; | [optional] [enum: SOA, A, TXT, NS, CNAME, MX, NAPTR, PTR, SRV, SPF, AAAA, CAA, DS] |
| **maxitems** | **String**| The maximum number of traffic policy instances that you want Amazon Route 53 to return in response to a &lt;code&gt;ListTrafficPolicyInstances&lt;/code&gt; request. If you have more than &lt;code&gt;MaxItems&lt;/code&gt; traffic policy instances, the value of the &lt;code&gt;IsTruncated&lt;/code&gt; element in the response is &lt;code&gt;true&lt;/code&gt;, and the values of &lt;code&gt;HostedZoneIdMarker&lt;/code&gt;, &lt;code&gt;TrafficPolicyInstanceNameMarker&lt;/code&gt;, and &lt;code&gt;TrafficPolicyInstanceTypeMarker&lt;/code&gt; represent the first traffic policy instance in the next group of &lt;code&gt;MaxItems&lt;/code&gt; traffic policy instances. | [optional] |

### Return type

[**ListTrafficPolicyInstancesResponse**](ListTrafficPolicyInstancesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | NoSuchTrafficPolicyInstance |  -  |

<a id="listTrafficPolicyInstancesByHostedZone"></a>
# **listTrafficPolicyInstancesByHostedZone**
> ListTrafficPolicyInstancesByHostedZoneResponse listTrafficPolicyInstancesByHostedZone(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, trafficpolicyinstancename, trafficpolicyinstancetype, maxitems)



&lt;p&gt;Gets information about the traffic policy instances that you created in a specified hosted zone.&lt;/p&gt; &lt;note&gt; &lt;p&gt;After you submit a &lt;code&gt;CreateTrafficPolicyInstance&lt;/code&gt; or an &lt;code&gt;UpdateTrafficPolicyInstance&lt;/code&gt; request, there&#39;s a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the &lt;code&gt;State&lt;/code&gt; response element.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the &lt;code&gt;MaxItems&lt;/code&gt; parameter to list them in groups of up to 100.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the hosted zone that you want to list traffic policy instances for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String trafficpolicyinstancename = "trafficpolicyinstancename_example"; // String | <p>If the value of <code>IsTruncated</code> in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstances</code> request. For the value of <code>trafficpolicyinstancename</code>, specify the value of <code>TrafficPolicyInstanceNameMarker</code> from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
    String trafficpolicyinstancetype = "SOA"; // String | <p>If the value of <code>IsTruncated</code> in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstances</code> request. For the value of <code>trafficpolicyinstancetype</code>, specify the value of <code>TrafficPolicyInstanceTypeMarker</code> from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
    String maxitems = "maxitems_example"; // String | The maximum number of traffic policy instances to be included in the response body for this request. If you have more than <code>MaxItems</code> traffic policy instances, the value of the <code>IsTruncated</code> element in the response is <code>true</code>, and the values of <code>HostedZoneIdMarker</code>, <code>TrafficPolicyInstanceNameMarker</code>, and <code>TrafficPolicyInstanceTypeMarker</code> represent the first traffic policy instance that Amazon Route 53 will return if you submit another request.
    try {
      ListTrafficPolicyInstancesByHostedZoneResponse result = apiInstance.listTrafficPolicyInstancesByHostedZone(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, trafficpolicyinstancename, trafficpolicyinstancetype, maxitems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTrafficPolicyInstancesByHostedZone");
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
| **id** | **String**| The ID of the hosted zone that you want to list traffic policy instances for. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **trafficpolicyinstancename** | **String**| &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstances&lt;/code&gt; request. For the value of &lt;code&gt;trafficpolicyinstancename&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyInstanceNameMarker&lt;/code&gt; from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt; | [optional] |
| **trafficpolicyinstancetype** | **String**| &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstances&lt;/code&gt; request. For the value of &lt;code&gt;trafficpolicyinstancetype&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyInstanceTypeMarker&lt;/code&gt; from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt; | [optional] [enum: SOA, A, TXT, NS, CNAME, MX, NAPTR, PTR, SRV, SPF, AAAA, CAA, DS] |
| **maxitems** | **String**| The maximum number of traffic policy instances to be included in the response body for this request. If you have more than &lt;code&gt;MaxItems&lt;/code&gt; traffic policy instances, the value of the &lt;code&gt;IsTruncated&lt;/code&gt; element in the response is &lt;code&gt;true&lt;/code&gt;, and the values of &lt;code&gt;HostedZoneIdMarker&lt;/code&gt;, &lt;code&gt;TrafficPolicyInstanceNameMarker&lt;/code&gt;, and &lt;code&gt;TrafficPolicyInstanceTypeMarker&lt;/code&gt; represent the first traffic policy instance that Amazon Route 53 will return if you submit another request. | [optional] |

### Return type

[**ListTrafficPolicyInstancesByHostedZoneResponse**](ListTrafficPolicyInstancesByHostedZoneResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | NoSuchTrafficPolicyInstance |  -  |
| **482** | NoSuchHostedZone |  -  |

<a id="listTrafficPolicyInstancesByPolicy"></a>
# **listTrafficPolicyInstancesByPolicy**
> ListTrafficPolicyInstancesByPolicyResponse listTrafficPolicyInstancesByPolicy(id, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, hostedzoneid, trafficpolicyinstancename, trafficpolicyinstancetype, maxitems)



&lt;p&gt;Gets information about the traffic policy instances that you created by using a specify traffic policy version.&lt;/p&gt; &lt;note&gt; &lt;p&gt;After you submit a &lt;code&gt;CreateTrafficPolicyInstance&lt;/code&gt; or an &lt;code&gt;UpdateTrafficPolicyInstance&lt;/code&gt; request, there&#39;s a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the &lt;code&gt;State&lt;/code&gt; response element.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the &lt;code&gt;MaxItems&lt;/code&gt; parameter to list them in groups of up to 100.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the traffic policy for which you want to list traffic policy instances.
    Integer version = 56; // Integer | The version of the traffic policy for which you want to list traffic policy instances. The version must be associated with the traffic policy that is specified by <code>TrafficPolicyId</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String hostedzoneid = "hostedzoneid_example"; // String | <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstancesByPolicy</code> request. </p> <p>For the value of <code>hostedzoneid</code>, specify the value of <code>HostedZoneIdMarker</code> from the previous response, which is the hosted zone ID of the first traffic policy instance that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
    String trafficpolicyinstancename = "trafficpolicyinstancename_example"; // String | <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstancesByPolicy</code> request.</p> <p>For the value of <code>trafficpolicyinstancename</code>, specify the value of <code>TrafficPolicyInstanceNameMarker</code> from the previous response, which is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
    String trafficpolicyinstancetype = "SOA"; // String | <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstancesByPolicy</code> request.</p> <p>For the value of <code>trafficpolicyinstancetype</code>, specify the value of <code>TrafficPolicyInstanceTypeMarker</code> from the previous response, which is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
    String maxitems = "maxitems_example"; // String | The maximum number of traffic policy instances to be included in the response body for this request. If you have more than <code>MaxItems</code> traffic policy instances, the value of the <code>IsTruncated</code> element in the response is <code>true</code>, and the values of <code>HostedZoneIdMarker</code>, <code>TrafficPolicyInstanceNameMarker</code>, and <code>TrafficPolicyInstanceTypeMarker</code> represent the first traffic policy instance that Amazon Route 53 will return if you submit another request.
    try {
      ListTrafficPolicyInstancesByPolicyResponse result = apiInstance.listTrafficPolicyInstancesByPolicy(id, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, hostedzoneid, trafficpolicyinstancename, trafficpolicyinstancetype, maxitems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTrafficPolicyInstancesByPolicy");
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
| **id** | **String**| The ID of the traffic policy for which you want to list traffic policy instances. | |
| **version** | **Integer**| The version of the traffic policy for which you want to list traffic policy instances. The version must be associated with the traffic policy that is specified by &lt;code&gt;TrafficPolicyId&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **hostedzoneid** | **String**| &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstancesByPolicy&lt;/code&gt; request. &lt;/p&gt; &lt;p&gt;For the value of &lt;code&gt;hostedzoneid&lt;/code&gt;, specify the value of &lt;code&gt;HostedZoneIdMarker&lt;/code&gt; from the previous response, which is the hosted zone ID of the first traffic policy instance that Amazon Route 53 will return if you submit another request.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt; | [optional] |
| **trafficpolicyinstancename** | **String**| &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstancesByPolicy&lt;/code&gt; request.&lt;/p&gt; &lt;p&gt;For the value of &lt;code&gt;trafficpolicyinstancename&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyInstanceNameMarker&lt;/code&gt; from the previous response, which is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another request.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt; | [optional] |
| **trafficpolicyinstancetype** | **String**| &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstancesByPolicy&lt;/code&gt; request.&lt;/p&gt; &lt;p&gt;For the value of &lt;code&gt;trafficpolicyinstancetype&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyInstanceTypeMarker&lt;/code&gt; from the previous response, which is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another request.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt; | [optional] [enum: SOA, A, TXT, NS, CNAME, MX, NAPTR, PTR, SRV, SPF, AAAA, CAA, DS] |
| **maxitems** | **String**| The maximum number of traffic policy instances to be included in the response body for this request. If you have more than &lt;code&gt;MaxItems&lt;/code&gt; traffic policy instances, the value of the &lt;code&gt;IsTruncated&lt;/code&gt; element in the response is &lt;code&gt;true&lt;/code&gt;, and the values of &lt;code&gt;HostedZoneIdMarker&lt;/code&gt;, &lt;code&gt;TrafficPolicyInstanceNameMarker&lt;/code&gt;, and &lt;code&gt;TrafficPolicyInstanceTypeMarker&lt;/code&gt; represent the first traffic policy instance that Amazon Route 53 will return if you submit another request. | [optional] |

### Return type

[**ListTrafficPolicyInstancesByPolicyResponse**](ListTrafficPolicyInstancesByPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | NoSuchTrafficPolicyInstance |  -  |
| **482** | NoSuchTrafficPolicy |  -  |

<a id="listTrafficPolicyVersions"></a>
# **listTrafficPolicyVersions**
> ListTrafficPolicyVersionsResponse listTrafficPolicyVersions(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, trafficpolicyversion, maxitems)



&lt;p&gt;Gets information about all of the versions for a specified traffic policy.&lt;/p&gt; &lt;p&gt;Traffic policy versions are listed in numerical order by &lt;code&gt;VersionNumber&lt;/code&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Specify the value of <code>Id</code> of the traffic policy for which you want to list all versions.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String trafficpolicyversion = "trafficpolicyversion_example"; // String | <p>For your first request to <code>ListTrafficPolicyVersions</code>, don't include the <code>TrafficPolicyVersionMarker</code> parameter.</p> <p>If you have more traffic policy versions than the value of <code>MaxItems</code>, <code>ListTrafficPolicyVersions</code> returns only the first group of <code>MaxItems</code> versions. To get more traffic policy versions, submit another <code>ListTrafficPolicyVersions</code> request. For the value of <code>TrafficPolicyVersionMarker</code>, specify the value of <code>TrafficPolicyVersionMarker</code> in the previous response.</p>
    String maxitems = "maxitems_example"; // String | The maximum number of traffic policy versions that you want Amazon Route 53 to include in the response body for this request. If the specified traffic policy has more than <code>MaxItems</code> versions, the value of <code>IsTruncated</code> in the response is <code>true</code>, and the value of the <code>TrafficPolicyVersionMarker</code> element is the ID of the first version that Route 53 will return if you submit another request.
    try {
      ListTrafficPolicyVersionsResponse result = apiInstance.listTrafficPolicyVersions(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, trafficpolicyversion, maxitems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTrafficPolicyVersions");
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
| **id** | **String**| Specify the value of &lt;code&gt;Id&lt;/code&gt; of the traffic policy for which you want to list all versions. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **trafficpolicyversion** | **String**| &lt;p&gt;For your first request to &lt;code&gt;ListTrafficPolicyVersions&lt;/code&gt;, don&#39;t include the &lt;code&gt;TrafficPolicyVersionMarker&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;If you have more traffic policy versions than the value of &lt;code&gt;MaxItems&lt;/code&gt;, &lt;code&gt;ListTrafficPolicyVersions&lt;/code&gt; returns only the first group of &lt;code&gt;MaxItems&lt;/code&gt; versions. To get more traffic policy versions, submit another &lt;code&gt;ListTrafficPolicyVersions&lt;/code&gt; request. For the value of &lt;code&gt;TrafficPolicyVersionMarker&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyVersionMarker&lt;/code&gt; in the previous response.&lt;/p&gt; | [optional] |
| **maxitems** | **String**| The maximum number of traffic policy versions that you want Amazon Route 53 to include in the response body for this request. If the specified traffic policy has more than &lt;code&gt;MaxItems&lt;/code&gt; versions, the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the response is &lt;code&gt;true&lt;/code&gt;, and the value of the &lt;code&gt;TrafficPolicyVersionMarker&lt;/code&gt; element is the ID of the first version that Route 53 will return if you submit another request. | [optional] |

### Return type

[**ListTrafficPolicyVersionsResponse**](ListTrafficPolicyVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | NoSuchTrafficPolicy |  -  |

<a id="listVPCAssociationAuthorizations"></a>
# **listVPCAssociationAuthorizations**
> ListVPCAssociationAuthorizationsResponse listVPCAssociationAuthorizations(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nexttoken, maxresults)



&lt;p&gt;Gets a list of the VPCs that were created by other accounts and that can be associated with a specified hosted zone because you&#39;ve submitted one or more &lt;code&gt;CreateVPCAssociationAuthorization&lt;/code&gt; requests. &lt;/p&gt; &lt;p&gt;The response includes a &lt;code&gt;VPCs&lt;/code&gt; element with a &lt;code&gt;VPC&lt;/code&gt; child element for each VPC that can be associated with the hosted zone.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the hosted zone for which you want a list of VPCs that can be associated with the hosted zone.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nexttoken = "nexttoken_example"; // String |  <i>Optional</i>: If a response includes a <code>NextToken</code> element, there are more VPCs that can be associated with the specified hosted zone. To get the next page of results, submit another request, and include the value of <code>NextToken</code> from the response in the <code>nexttoken</code> parameter in another <code>ListVPCAssociationAuthorizations</code> request.
    String maxresults = "maxresults_example"; // String |  <i>Optional</i>: An integer that specifies the maximum number of VPCs that you want Amazon Route 53 to return. If you don't specify a value for <code>MaxResults</code>, Route 53 returns up to 50 VPCs per page.
    try {
      ListVPCAssociationAuthorizationsResponse result = apiInstance.listVPCAssociationAuthorizations(id, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nexttoken, maxresults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listVPCAssociationAuthorizations");
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
| **id** | **String**| The ID of the hosted zone for which you want a list of VPCs that can be associated with the hosted zone. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nexttoken** | **String**|  &lt;i&gt;Optional&lt;/i&gt;: If a response includes a &lt;code&gt;NextToken&lt;/code&gt; element, there are more VPCs that can be associated with the specified hosted zone. To get the next page of results, submit another request, and include the value of &lt;code&gt;NextToken&lt;/code&gt; from the response in the &lt;code&gt;nexttoken&lt;/code&gt; parameter in another &lt;code&gt;ListVPCAssociationAuthorizations&lt;/code&gt; request. | [optional] |
| **maxresults** | **String**|  &lt;i&gt;Optional&lt;/i&gt;: An integer that specifies the maximum number of VPCs that you want Amazon Route 53 to return. If you don&#39;t specify a value for &lt;code&gt;MaxResults&lt;/code&gt;, Route 53 returns up to 50 VPCs per page. | [optional] |

### Return type

[**ListVPCAssociationAuthorizationsResponse**](ListVPCAssociationAuthorizationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | InvalidInput |  -  |
| **482** | InvalidPaginationToken |  -  |

<a id="testDNSAnswer"></a>
# **testDNSAnswer**
> TestDNSAnswerResponse testDNSAnswer(hostedzoneid, recordname, recordtype, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, resolverip, edns0clientsubnetip, edns0clientsubnetmask)



&lt;p&gt;Gets the value that Amazon Route 53 returns in response to a DNS request for a specified record name and type. You can optionally specify the IP address of a DNS resolver, an EDNS0 client subnet IP address, and a subnet mask. &lt;/p&gt; &lt;p&gt;This call only supports querying public hosted zones.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;TestDnsAnswer &lt;/code&gt; returns information similar to what you would expect from the answer section of the &lt;code&gt;dig&lt;/code&gt; command. Therefore, if you query for the name servers of a subdomain that point to the parent name servers, those will not be returned.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostedzoneid = "hostedzoneid_example"; // String | The ID of the hosted zone that you want Amazon Route 53 to simulate a query for.
    String recordname = "recordname_example"; // String | The name of the resource record set that you want Amazon Route 53 to simulate a query for.
    String recordtype = "SOA"; // String | The type of the resource record set.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String resolverip = "resolverip_example"; // String | If you want to simulate a request from a specific DNS resolver, specify the IP address for that resolver. If you omit this value, <code>TestDnsAnswer</code> uses the IP address of a DNS resolver in the Amazon Web Services US East (N. Virginia) Region (<code>us-east-1</code>).
    String edns0clientsubnetip = "edns0clientsubnetip_example"; // String | If the resolver that you specified for resolverip supports EDNS0, specify the IPv4 or IPv6 address of a client in the applicable location, for example, <code>192.0.2.44</code> or <code>2001:db8:85a3::8a2e:370:7334</code>.
    String edns0clientsubnetmask = "edns0clientsubnetmask_example"; // String | <p>If you specify an IP address for <code>edns0clientsubnetip</code>, you can optionally specify the number of bits of the IP address that you want the checking tool to include in the DNS query. For example, if you specify <code>192.0.2.44</code> for <code>edns0clientsubnetip</code> and <code>24</code> for <code>edns0clientsubnetmask</code>, the checking tool will simulate a request from 192.0.2.0/24. The default value is 24 bits for IPv4 addresses and 64 bits for IPv6 addresses.</p> <p>The range of valid values depends on whether <code>edns0clientsubnetip</code> is an IPv4 or an IPv6 address:</p> <ul> <li> <p> <b>IPv4</b>: Specify a value between 0 and 32</p> </li> <li> <p> <b>IPv6</b>: Specify a value between 0 and 128</p> </li> </ul>
    try {
      TestDNSAnswerResponse result = apiInstance.testDNSAnswer(hostedzoneid, recordname, recordtype, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, resolverip, edns0clientsubnetip, edns0clientsubnetmask);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#testDNSAnswer");
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
| **hostedzoneid** | **String**| The ID of the hosted zone that you want Amazon Route 53 to simulate a query for. | |
| **recordname** | **String**| The name of the resource record set that you want Amazon Route 53 to simulate a query for. | |
| **recordtype** | **String**| The type of the resource record set. | [enum: SOA, A, TXT, NS, CNAME, MX, NAPTR, PTR, SRV, SPF, AAAA, CAA, DS] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **resolverip** | **String**| If you want to simulate a request from a specific DNS resolver, specify the IP address for that resolver. If you omit this value, &lt;code&gt;TestDnsAnswer&lt;/code&gt; uses the IP address of a DNS resolver in the Amazon Web Services US East (N. Virginia) Region (&lt;code&gt;us-east-1&lt;/code&gt;). | [optional] |
| **edns0clientsubnetip** | **String**| If the resolver that you specified for resolverip supports EDNS0, specify the IPv4 or IPv6 address of a client in the applicable location, for example, &lt;code&gt;192.0.2.44&lt;/code&gt; or &lt;code&gt;2001:db8:85a3::8a2e:370:7334&lt;/code&gt;. | [optional] |
| **edns0clientsubnetmask** | **String**| &lt;p&gt;If you specify an IP address for &lt;code&gt;edns0clientsubnetip&lt;/code&gt;, you can optionally specify the number of bits of the IP address that you want the checking tool to include in the DNS query. For example, if you specify &lt;code&gt;192.0.2.44&lt;/code&gt; for &lt;code&gt;edns0clientsubnetip&lt;/code&gt; and &lt;code&gt;24&lt;/code&gt; for &lt;code&gt;edns0clientsubnetmask&lt;/code&gt;, the checking tool will simulate a request from 192.0.2.0/24. The default value is 24 bits for IPv4 addresses and 64 bits for IPv6 addresses.&lt;/p&gt; &lt;p&gt;The range of valid values depends on whether &lt;code&gt;edns0clientsubnetip&lt;/code&gt; is an IPv4 or an IPv6 address:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;IPv4&lt;/b&gt;: Specify a value between 0 and 32&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;IPv6&lt;/b&gt;: Specify a value between 0 and 128&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |

### Return type

[**TestDNSAnswerResponse**](TestDNSAnswerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | InvalidInput |  -  |

<a id="updateHealthCheck"></a>
# **updateHealthCheck**
> UpdateHealthCheckResponse updateHealthCheck(healthCheckId, updateHealthCheckRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates an existing health check. Note that some values can&#39;t be updated. &lt;/p&gt; &lt;p&gt;For more information about updating health checks, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-deleting.html\&quot;&gt;Creating, Updating, and Deleting Health Checks&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String healthCheckId = "healthCheckId_example"; // String | The ID for the health check for which you want detailed information. When you created the health check, <code>CreateHealthCheck</code> returned the ID in the response, in the <code>HealthCheckId</code> element.
    UpdateHealthCheckRequest updateHealthCheckRequest = new UpdateHealthCheckRequest(); // UpdateHealthCheckRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateHealthCheckResponse result = apiInstance.updateHealthCheck(healthCheckId, updateHealthCheckRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateHealthCheck");
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
| **healthCheckId** | **String**| The ID for the health check for which you want detailed information. When you created the health check, &lt;code&gt;CreateHealthCheck&lt;/code&gt; returned the ID in the response, in the &lt;code&gt;HealthCheckId&lt;/code&gt; element. | |
| **updateHealthCheckRequest** | [**UpdateHealthCheckRequest**](UpdateHealthCheckRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateHealthCheckResponse**](UpdateHealthCheckResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHealthCheck |  -  |
| **481** | InvalidInput |  -  |
| **482** | HealthCheckVersionMismatch |  -  |

<a id="updateHostedZoneComment"></a>
# **updateHostedZoneComment**
> UpdateHostedZoneCommentResponse updateHostedZoneComment(id, updateHostedZoneCommentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates the comment for a specified hosted zone.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID for the hosted zone that you want to update the comment for.
    UpdateHostedZoneCommentRequest updateHostedZoneCommentRequest = new UpdateHostedZoneCommentRequest(); // UpdateHostedZoneCommentRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateHostedZoneCommentResponse result = apiInstance.updateHostedZoneComment(id, updateHostedZoneCommentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateHostedZoneComment");
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
| **id** | **String**| The ID for the hosted zone that you want to update the comment for. | |
| **updateHostedZoneCommentRequest** | [**UpdateHostedZoneCommentRequest**](UpdateHostedZoneCommentRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateHostedZoneCommentResponse**](UpdateHostedZoneCommentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NoSuchHostedZone |  -  |
| **481** | InvalidInput |  -  |
| **482** | PriorRequestNotComplete |  -  |

<a id="updateTrafficPolicyComment"></a>
# **updateTrafficPolicyComment**
> UpdateTrafficPolicyCommentResponse updateTrafficPolicyComment(id, version, updateTrafficPolicyCommentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates the comment for a specified traffic policy version.

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The value of <code>Id</code> for the traffic policy that you want to update the comment for.
    Integer version = 56; // Integer | The value of <code>Version</code> for the traffic policy that you want to update the comment for.
    UpdateTrafficPolicyCommentRequest updateTrafficPolicyCommentRequest = new UpdateTrafficPolicyCommentRequest(); // UpdateTrafficPolicyCommentRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateTrafficPolicyCommentResponse result = apiInstance.updateTrafficPolicyComment(id, version, updateTrafficPolicyCommentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateTrafficPolicyComment");
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
| **id** | **String**| The value of &lt;code&gt;Id&lt;/code&gt; for the traffic policy that you want to update the comment for. | |
| **version** | **Integer**| The value of &lt;code&gt;Version&lt;/code&gt; for the traffic policy that you want to update the comment for. | |
| **updateTrafficPolicyCommentRequest** | [**UpdateTrafficPolicyCommentRequest**](UpdateTrafficPolicyCommentRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateTrafficPolicyCommentResponse**](UpdateTrafficPolicyCommentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | NoSuchTrafficPolicy |  -  |
| **482** | ConcurrentModification |  -  |

<a id="updateTrafficPolicyInstance"></a>
# **updateTrafficPolicyInstance**
> UpdateTrafficPolicyInstanceResponse updateTrafficPolicyInstance(id, updateTrafficPolicyInstanceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates the resource record sets in a specified hosted zone that were created based on the settings in a specified traffic policy version.&lt;/p&gt; &lt;p&gt;When you update a traffic policy instance, Amazon Route 53 continues to respond to DNS queries for the root resource record set name (such as example.com) while it replaces one group of resource record sets with another. Route 53 performs the following operations:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Route 53 creates a new group of resource record sets based on the specified traffic policy. This is true regardless of how significant the differences are between the existing resource record sets and the new resource record sets. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When all of the new resource record sets have been created, Route 53 starts to respond to DNS queries for the root resource record set name (such as example.com) by using the new resource record sets.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Route 53 deletes the old group of resource record sets that are associated with the root resource record set name.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

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
    defaultClient.setBasePath("https://route53.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The ID of the traffic policy instance that you want to update.
    UpdateTrafficPolicyInstanceRequest updateTrafficPolicyInstanceRequest = new UpdateTrafficPolicyInstanceRequest(); // UpdateTrafficPolicyInstanceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateTrafficPolicyInstanceResponse result = apiInstance.updateTrafficPolicyInstance(id, updateTrafficPolicyInstanceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateTrafficPolicyInstance");
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
| **id** | **String**| The ID of the traffic policy instance that you want to update. | |
| **updateTrafficPolicyInstanceRequest** | [**UpdateTrafficPolicyInstanceRequest**](UpdateTrafficPolicyInstanceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateTrafficPolicyInstanceResponse**](UpdateTrafficPolicyInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidInput |  -  |
| **481** | NoSuchTrafficPolicy |  -  |
| **482** | NoSuchTrafficPolicyInstance |  -  |
| **483** | PriorRequestNotComplete |  -  |
| **484** | ConflictingTypes |  -  |

