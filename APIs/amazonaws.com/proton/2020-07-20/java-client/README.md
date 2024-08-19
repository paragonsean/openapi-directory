# openapi-java-client

AWS Proton
- API version: 2020-07-20
  - Build date: 2024-10-12T12:26:35.899404-04:00[America/New_York]
  - Generator version: 7.9.0

<p>This is the Proton Service API Reference. It provides descriptions, syntax and usage examples for each of the <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Operations.html\">actions</a> and <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Types.html\">data types</a> for the Proton service.</p> <p>The documentation for each action shows the Query API request parameters and the XML response.</p> <p>Alternatively, you can use the Amazon Web Services CLI to access an API. For more information, see the <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html\">Amazon Web Services Command Line Interface User Guide</a>.</p> <p>The Proton service is a two-pronged automation framework. Administrators create service templates to provide standardized infrastructure and deployment tooling for serverless and container based applications. Developers, in turn, select from the available service templates to automate their application or service deployments.</p> <p>Because administrators define the infrastructure and tooling that Proton deploys and manages, they need permissions to use all of the listed API operations.</p> <p>When developers select a specific infrastructure and tooling set, Proton deploys their applications. To monitor their applications that are running on Proton, developers need permissions to the service <i>create</i>, <i>list</i>, <i>update</i> and <i>delete</i> API operations and the service instance <i>list</i> and <i>update</i> API operations.</p> <p>To learn more about Proton, see the <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html\">Proton User Guide</a>.</p> <p> <b>Ensuring Idempotency</b> </p> <p>When you make a mutating API request, the request typically returns a result before the asynchronous workflows of the operation are complete. Operations might also time out or encounter other server issues before they're complete, even if the request already returned a result. This might make it difficult to determine whether the request succeeded. Moreover, you might need to retry the request multiple times to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation occurs multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request action completes no more than one time. With an idempotent request, if the original request action completes successfully, any subsequent retries complete successfully without performing any further actions. However, the result might contain updated information, such as the current creation status.</p> <p>The following lists of APIs are grouped according to methods that ensure idempotency.</p> <p> <b>Idempotent create APIs with a client token</b> </p> <p>The API actions in this list support idempotency with the use of a <i>client token</i>. The corresponding Amazon Web Services CLI commands also support idempotency using a client token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request. We recommend that you <i>don't</i> reuse the same client token for other API requests. If you don’t provide a client token for these APIs, a default client token is automatically provided by SDKs.</p> <p>Given a request action that has succeeded:</p> <p>If you retry the request using the same client token and the same parameters, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If you retry the request using the same client token, but one or more of the parameters are different, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Client tokens expire eight hours after a request is made. If you retry the request with the expired token, a new resource is created.</p> <p>If the original resource is deleted and you retry the request, a new resource is created.</p> <p>Idempotent create APIs with a client token:</p> <ul> <li> <p>CreateEnvironmentTemplateVersion</p> </li> <li> <p>CreateServiceTemplateVersion</p> </li> <li> <p>CreateEnvironmentAccountConnection</p> </li> </ul> <p> <b>Idempotent create APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, and the original resource <i>hasn't</i> been modified, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If the original resource has been modified, the retry throws a <code>ConflictException</code>.</p> <p>If you retry with different input parameters, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Idempotent create APIs:</p> <ul> <li> <p>CreateEnvironmentTemplate</p> </li> <li> <p>CreateServiceTemplate</p> </li> <li> <p>CreateEnvironment</p> </li> <li> <p>CreateService</p> </li> </ul> <p> <b>Idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>When you retry the request with an API from this group and the resource was deleted, its metadata is returned in the response.</p> <p>If you retry and the resource doesn't exist, the response is empty.</p> <p>In both cases, the retry succeeds.</p> <p>Idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironmentTemplate</p> </li> <li> <p>DeleteEnvironmentTemplateVersion</p> </li> <li> <p>DeleteServiceTemplate</p> </li> <li> <p>DeleteServiceTemplateVersion</p> </li> <li> <p>DeleteEnvironmentAccountConnection</p> </li> </ul> <p> <b>Asynchronous idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, if the original request delete operation status is <code>DELETE_IN_PROGRESS</code>, the retry returns the resource detail data in the response without performing any further actions.</p> <p>If the original request delete operation is complete, a retry returns an empty response.</p> <p>Asynchronous idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironment</p> </li> <li> <p>DeleteService</p> </li> </ul>

  For more information, please visit [https://github.com/mermade/aws2openapi](https://github.com/mermade/aws2openapi)

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>2020-07-20</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:2020-07-20"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-2020-07-20.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://proton.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AwsProton20200720.AcceptEnvironmentAccountConnection"; // String | 
    AcceptEnvironmentAccountConnectionInput acceptEnvironmentAccountConnectionInput = new AcceptEnvironmentAccountConnectionInput(); // AcceptEnvironmentAccountConnectionInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AcceptEnvironmentAccountConnectionOutput result = apiInstance.acceptEnvironmentAccountConnection(xAmzTarget, acceptEnvironmentAccountConnectionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#acceptEnvironmentAccountConnection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://proton.us-east-1.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**acceptEnvironmentAccountConnection**](docs/DefaultApi.md#acceptEnvironmentAccountConnection) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.AcceptEnvironmentAccountConnection | 
*DefaultApi* | [**cancelComponentDeployment**](docs/DefaultApi.md#cancelComponentDeployment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CancelComponentDeployment | 
*DefaultApi* | [**cancelEnvironmentDeployment**](docs/DefaultApi.md#cancelEnvironmentDeployment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CancelEnvironmentDeployment | 
*DefaultApi* | [**cancelServiceInstanceDeployment**](docs/DefaultApi.md#cancelServiceInstanceDeployment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CancelServiceInstanceDeployment | 
*DefaultApi* | [**cancelServicePipelineDeployment**](docs/DefaultApi.md#cancelServicePipelineDeployment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CancelServicePipelineDeployment | 
*DefaultApi* | [**createComponent**](docs/DefaultApi.md#createComponent) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateComponent | 
*DefaultApi* | [**createEnvironment**](docs/DefaultApi.md#createEnvironment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateEnvironment | 
*DefaultApi* | [**createEnvironmentAccountConnection**](docs/DefaultApi.md#createEnvironmentAccountConnection) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateEnvironmentAccountConnection | 
*DefaultApi* | [**createEnvironmentTemplate**](docs/DefaultApi.md#createEnvironmentTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateEnvironmentTemplate | 
*DefaultApi* | [**createEnvironmentTemplateVersion**](docs/DefaultApi.md#createEnvironmentTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateEnvironmentTemplateVersion | 
*DefaultApi* | [**createRepository**](docs/DefaultApi.md#createRepository) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateRepository | 
*DefaultApi* | [**createService**](docs/DefaultApi.md#createService) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateService | 
*DefaultApi* | [**createServiceInstance**](docs/DefaultApi.md#createServiceInstance) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateServiceInstance | 
*DefaultApi* | [**createServiceSyncConfig**](docs/DefaultApi.md#createServiceSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateServiceSyncConfig | 
*DefaultApi* | [**createServiceTemplate**](docs/DefaultApi.md#createServiceTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateServiceTemplate | 
*DefaultApi* | [**createServiceTemplateVersion**](docs/DefaultApi.md#createServiceTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateServiceTemplateVersion | 
*DefaultApi* | [**createTemplateSyncConfig**](docs/DefaultApi.md#createTemplateSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateTemplateSyncConfig | 
*DefaultApi* | [**deleteComponent**](docs/DefaultApi.md#deleteComponent) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteComponent | 
*DefaultApi* | [**deleteDeployment**](docs/DefaultApi.md#deleteDeployment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteDeployment | 
*DefaultApi* | [**deleteEnvironment**](docs/DefaultApi.md#deleteEnvironment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteEnvironment | 
*DefaultApi* | [**deleteEnvironmentAccountConnection**](docs/DefaultApi.md#deleteEnvironmentAccountConnection) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteEnvironmentAccountConnection | 
*DefaultApi* | [**deleteEnvironmentTemplate**](docs/DefaultApi.md#deleteEnvironmentTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteEnvironmentTemplate | 
*DefaultApi* | [**deleteEnvironmentTemplateVersion**](docs/DefaultApi.md#deleteEnvironmentTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteEnvironmentTemplateVersion | 
*DefaultApi* | [**deleteRepository**](docs/DefaultApi.md#deleteRepository) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteRepository | 
*DefaultApi* | [**deleteService**](docs/DefaultApi.md#deleteService) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteService | 
*DefaultApi* | [**deleteServiceSyncConfig**](docs/DefaultApi.md#deleteServiceSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteServiceSyncConfig | 
*DefaultApi* | [**deleteServiceTemplate**](docs/DefaultApi.md#deleteServiceTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteServiceTemplate | 
*DefaultApi* | [**deleteServiceTemplateVersion**](docs/DefaultApi.md#deleteServiceTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteServiceTemplateVersion | 
*DefaultApi* | [**deleteTemplateSyncConfig**](docs/DefaultApi.md#deleteTemplateSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteTemplateSyncConfig | 
*DefaultApi* | [**getAccountSettings**](docs/DefaultApi.md#getAccountSettings) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetAccountSettings | 
*DefaultApi* | [**getComponent**](docs/DefaultApi.md#getComponent) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetComponent | 
*DefaultApi* | [**getDeployment**](docs/DefaultApi.md#getDeployment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetDeployment | 
*DefaultApi* | [**getEnvironment**](docs/DefaultApi.md#getEnvironment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetEnvironment | 
*DefaultApi* | [**getEnvironmentAccountConnection**](docs/DefaultApi.md#getEnvironmentAccountConnection) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetEnvironmentAccountConnection | 
*DefaultApi* | [**getEnvironmentTemplate**](docs/DefaultApi.md#getEnvironmentTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetEnvironmentTemplate | 
*DefaultApi* | [**getEnvironmentTemplateVersion**](docs/DefaultApi.md#getEnvironmentTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetEnvironmentTemplateVersion | 
*DefaultApi* | [**getRepository**](docs/DefaultApi.md#getRepository) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetRepository | 
*DefaultApi* | [**getRepositorySyncStatus**](docs/DefaultApi.md#getRepositorySyncStatus) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetRepositorySyncStatus | 
*DefaultApi* | [**getResourcesSummary**](docs/DefaultApi.md#getResourcesSummary) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetResourcesSummary | 
*DefaultApi* | [**getService**](docs/DefaultApi.md#getService) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetService | 
*DefaultApi* | [**getServiceInstance**](docs/DefaultApi.md#getServiceInstance) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetServiceInstance | 
*DefaultApi* | [**getServiceInstanceSyncStatus**](docs/DefaultApi.md#getServiceInstanceSyncStatus) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetServiceInstanceSyncStatus | 
*DefaultApi* | [**getServiceSyncBlockerSummary**](docs/DefaultApi.md#getServiceSyncBlockerSummary) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetServiceSyncBlockerSummary | 
*DefaultApi* | [**getServiceSyncConfig**](docs/DefaultApi.md#getServiceSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetServiceSyncConfig | 
*DefaultApi* | [**getServiceTemplate**](docs/DefaultApi.md#getServiceTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetServiceTemplate | 
*DefaultApi* | [**getServiceTemplateVersion**](docs/DefaultApi.md#getServiceTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetServiceTemplateVersion | 
*DefaultApi* | [**getTemplateSyncConfig**](docs/DefaultApi.md#getTemplateSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetTemplateSyncConfig | 
*DefaultApi* | [**getTemplateSyncStatus**](docs/DefaultApi.md#getTemplateSyncStatus) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetTemplateSyncStatus | 
*DefaultApi* | [**listComponentOutputs**](docs/DefaultApi.md#listComponentOutputs) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListComponentOutputs | 
*DefaultApi* | [**listComponentProvisionedResources**](docs/DefaultApi.md#listComponentProvisionedResources) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListComponentProvisionedResources | 
*DefaultApi* | [**listComponents**](docs/DefaultApi.md#listComponents) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListComponents | 
*DefaultApi* | [**listDeployments**](docs/DefaultApi.md#listDeployments) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListDeployments | 
*DefaultApi* | [**listEnvironmentAccountConnections**](docs/DefaultApi.md#listEnvironmentAccountConnections) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListEnvironmentAccountConnections | 
*DefaultApi* | [**listEnvironmentOutputs**](docs/DefaultApi.md#listEnvironmentOutputs) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListEnvironmentOutputs | 
*DefaultApi* | [**listEnvironmentProvisionedResources**](docs/DefaultApi.md#listEnvironmentProvisionedResources) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListEnvironmentProvisionedResources | 
*DefaultApi* | [**listEnvironmentTemplateVersions**](docs/DefaultApi.md#listEnvironmentTemplateVersions) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListEnvironmentTemplateVersions | 
*DefaultApi* | [**listEnvironmentTemplates**](docs/DefaultApi.md#listEnvironmentTemplates) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListEnvironmentTemplates | 
*DefaultApi* | [**listEnvironments**](docs/DefaultApi.md#listEnvironments) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListEnvironments | 
*DefaultApi* | [**listRepositories**](docs/DefaultApi.md#listRepositories) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListRepositories | 
*DefaultApi* | [**listRepositorySyncDefinitions**](docs/DefaultApi.md#listRepositorySyncDefinitions) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListRepositorySyncDefinitions | 
*DefaultApi* | [**listServiceInstanceOutputs**](docs/DefaultApi.md#listServiceInstanceOutputs) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServiceInstanceOutputs | 
*DefaultApi* | [**listServiceInstanceProvisionedResources**](docs/DefaultApi.md#listServiceInstanceProvisionedResources) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServiceInstanceProvisionedResources | 
*DefaultApi* | [**listServiceInstances**](docs/DefaultApi.md#listServiceInstances) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServiceInstances | 
*DefaultApi* | [**listServicePipelineOutputs**](docs/DefaultApi.md#listServicePipelineOutputs) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServicePipelineOutputs | 
*DefaultApi* | [**listServicePipelineProvisionedResources**](docs/DefaultApi.md#listServicePipelineProvisionedResources) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServicePipelineProvisionedResources | 
*DefaultApi* | [**listServiceTemplateVersions**](docs/DefaultApi.md#listServiceTemplateVersions) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServiceTemplateVersions | 
*DefaultApi* | [**listServiceTemplates**](docs/DefaultApi.md#listServiceTemplates) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServiceTemplates | 
*DefaultApi* | [**listServices**](docs/DefaultApi.md#listServices) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServices | 
*DefaultApi* | [**listTagsForResource**](docs/DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListTagsForResource | 
*DefaultApi* | [**notifyResourceDeploymentStatusChange**](docs/DefaultApi.md#notifyResourceDeploymentStatusChange) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.NotifyResourceDeploymentStatusChange | 
*DefaultApi* | [**rejectEnvironmentAccountConnection**](docs/DefaultApi.md#rejectEnvironmentAccountConnection) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.RejectEnvironmentAccountConnection | 
*DefaultApi* | [**tagResource**](docs/DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.TagResource | 
*DefaultApi* | [**untagResource**](docs/DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UntagResource | 
*DefaultApi* | [**updateAccountSettings**](docs/DefaultApi.md#updateAccountSettings) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateAccountSettings | 
*DefaultApi* | [**updateComponent**](docs/DefaultApi.md#updateComponent) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateComponent | 
*DefaultApi* | [**updateEnvironment**](docs/DefaultApi.md#updateEnvironment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateEnvironment | 
*DefaultApi* | [**updateEnvironmentAccountConnection**](docs/DefaultApi.md#updateEnvironmentAccountConnection) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateEnvironmentAccountConnection | 
*DefaultApi* | [**updateEnvironmentTemplate**](docs/DefaultApi.md#updateEnvironmentTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateEnvironmentTemplate | 
*DefaultApi* | [**updateEnvironmentTemplateVersion**](docs/DefaultApi.md#updateEnvironmentTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateEnvironmentTemplateVersion | 
*DefaultApi* | [**updateService**](docs/DefaultApi.md#updateService) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateService | 
*DefaultApi* | [**updateServiceInstance**](docs/DefaultApi.md#updateServiceInstance) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateServiceInstance | 
*DefaultApi* | [**updateServicePipeline**](docs/DefaultApi.md#updateServicePipeline) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateServicePipeline | 
*DefaultApi* | [**updateServiceSyncBlocker**](docs/DefaultApi.md#updateServiceSyncBlocker) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateServiceSyncBlocker | 
*DefaultApi* | [**updateServiceSyncConfig**](docs/DefaultApi.md#updateServiceSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateServiceSyncConfig | 
*DefaultApi* | [**updateServiceTemplate**](docs/DefaultApi.md#updateServiceTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateServiceTemplate | 
*DefaultApi* | [**updateServiceTemplateVersion**](docs/DefaultApi.md#updateServiceTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateServiceTemplateVersion | 
*DefaultApi* | [**updateTemplateSyncConfig**](docs/DefaultApi.md#updateTemplateSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateTemplateSyncConfig | 


## Documentation for Models

 - [AcceptEnvironmentAccountConnectionInput](docs/AcceptEnvironmentAccountConnectionInput.md)
 - [AcceptEnvironmentAccountConnectionOutput](docs/AcceptEnvironmentAccountConnectionOutput.md)
 - [AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection](docs/AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.md)
 - [AccountSettings](docs/AccountSettings.md)
 - [AccountSettingsPipelineProvisioningRepository](docs/AccountSettingsPipelineProvisioningRepository.md)
 - [BlockerStatus](docs/BlockerStatus.md)
 - [BlockerType](docs/BlockerType.md)
 - [CancelComponentDeploymentInput](docs/CancelComponentDeploymentInput.md)
 - [CancelComponentDeploymentOutput](docs/CancelComponentDeploymentOutput.md)
 - [CancelComponentDeploymentOutputComponent](docs/CancelComponentDeploymentOutputComponent.md)
 - [CancelEnvironmentDeploymentInput](docs/CancelEnvironmentDeploymentInput.md)
 - [CancelEnvironmentDeploymentOutput](docs/CancelEnvironmentDeploymentOutput.md)
 - [CancelEnvironmentDeploymentOutputEnvironment](docs/CancelEnvironmentDeploymentOutputEnvironment.md)
 - [CancelServiceInstanceDeploymentInput](docs/CancelServiceInstanceDeploymentInput.md)
 - [CancelServiceInstanceDeploymentOutput](docs/CancelServiceInstanceDeploymentOutput.md)
 - [CancelServiceInstanceDeploymentOutputServiceInstance](docs/CancelServiceInstanceDeploymentOutputServiceInstance.md)
 - [CancelServicePipelineDeploymentInput](docs/CancelServicePipelineDeploymentInput.md)
 - [CancelServicePipelineDeploymentOutput](docs/CancelServicePipelineDeploymentOutput.md)
 - [CancelServicePipelineDeploymentOutputPipeline](docs/CancelServicePipelineDeploymentOutputPipeline.md)
 - [CompatibleEnvironmentTemplate](docs/CompatibleEnvironmentTemplate.md)
 - [CompatibleEnvironmentTemplateInput](docs/CompatibleEnvironmentTemplateInput.md)
 - [Component](docs/Component.md)
 - [ComponentDeploymentUpdateType](docs/ComponentDeploymentUpdateType.md)
 - [ComponentState](docs/ComponentState.md)
 - [ComponentSummary](docs/ComponentSummary.md)
 - [CountsSummary](docs/CountsSummary.md)
 - [CountsSummaryComponents](docs/CountsSummaryComponents.md)
 - [CountsSummaryEnvironmentTemplates](docs/CountsSummaryEnvironmentTemplates.md)
 - [CountsSummaryEnvironments](docs/CountsSummaryEnvironments.md)
 - [CountsSummaryPipelines](docs/CountsSummaryPipelines.md)
 - [CountsSummaryServiceInstances](docs/CountsSummaryServiceInstances.md)
 - [CountsSummaryServiceTemplates](docs/CountsSummaryServiceTemplates.md)
 - [CountsSummaryServices](docs/CountsSummaryServices.md)
 - [CreateComponentInput](docs/CreateComponentInput.md)
 - [CreateComponentOutput](docs/CreateComponentOutput.md)
 - [CreateComponentOutputComponent](docs/CreateComponentOutputComponent.md)
 - [CreateEnvironmentAccountConnectionInput](docs/CreateEnvironmentAccountConnectionInput.md)
 - [CreateEnvironmentAccountConnectionOutput](docs/CreateEnvironmentAccountConnectionOutput.md)
 - [CreateEnvironmentAccountConnectionOutputEnvironmentAccountConnection](docs/CreateEnvironmentAccountConnectionOutputEnvironmentAccountConnection.md)
 - [CreateEnvironmentInput](docs/CreateEnvironmentInput.md)
 - [CreateEnvironmentInputProvisioningRepository](docs/CreateEnvironmentInputProvisioningRepository.md)
 - [CreateEnvironmentOutput](docs/CreateEnvironmentOutput.md)
 - [CreateEnvironmentOutputEnvironment](docs/CreateEnvironmentOutputEnvironment.md)
 - [CreateEnvironmentTemplateInput](docs/CreateEnvironmentTemplateInput.md)
 - [CreateEnvironmentTemplateOutput](docs/CreateEnvironmentTemplateOutput.md)
 - [CreateEnvironmentTemplateOutputEnvironmentTemplate](docs/CreateEnvironmentTemplateOutputEnvironmentTemplate.md)
 - [CreateEnvironmentTemplateVersionInput](docs/CreateEnvironmentTemplateVersionInput.md)
 - [CreateEnvironmentTemplateVersionInputSource](docs/CreateEnvironmentTemplateVersionInputSource.md)
 - [CreateEnvironmentTemplateVersionOutput](docs/CreateEnvironmentTemplateVersionOutput.md)
 - [CreateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion](docs/CreateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion.md)
 - [CreateRepositoryInput](docs/CreateRepositoryInput.md)
 - [CreateRepositoryOutput](docs/CreateRepositoryOutput.md)
 - [CreateRepositoryOutputRepository](docs/CreateRepositoryOutputRepository.md)
 - [CreateServiceInput](docs/CreateServiceInput.md)
 - [CreateServiceInstanceInput](docs/CreateServiceInstanceInput.md)
 - [CreateServiceInstanceOutput](docs/CreateServiceInstanceOutput.md)
 - [CreateServiceInstanceOutputServiceInstance](docs/CreateServiceInstanceOutputServiceInstance.md)
 - [CreateServiceOutput](docs/CreateServiceOutput.md)
 - [CreateServiceOutputService](docs/CreateServiceOutputService.md)
 - [CreateServiceSyncConfigInput](docs/CreateServiceSyncConfigInput.md)
 - [CreateServiceSyncConfigOutput](docs/CreateServiceSyncConfigOutput.md)
 - [CreateServiceSyncConfigOutputServiceSyncConfig](docs/CreateServiceSyncConfigOutputServiceSyncConfig.md)
 - [CreateServiceTemplateInput](docs/CreateServiceTemplateInput.md)
 - [CreateServiceTemplateOutput](docs/CreateServiceTemplateOutput.md)
 - [CreateServiceTemplateOutputServiceTemplate](docs/CreateServiceTemplateOutputServiceTemplate.md)
 - [CreateServiceTemplateVersionInput](docs/CreateServiceTemplateVersionInput.md)
 - [CreateServiceTemplateVersionInputSource](docs/CreateServiceTemplateVersionInputSource.md)
 - [CreateServiceTemplateVersionOutput](docs/CreateServiceTemplateVersionOutput.md)
 - [CreateServiceTemplateVersionOutputServiceTemplateVersion](docs/CreateServiceTemplateVersionOutputServiceTemplateVersion.md)
 - [CreateTemplateSyncConfigInput](docs/CreateTemplateSyncConfigInput.md)
 - [CreateTemplateSyncConfigOutput](docs/CreateTemplateSyncConfigOutput.md)
 - [CreateTemplateSyncConfigOutputTemplateSyncConfig](docs/CreateTemplateSyncConfigOutputTemplateSyncConfig.md)
 - [DeleteComponentInput](docs/DeleteComponentInput.md)
 - [DeleteComponentOutput](docs/DeleteComponentOutput.md)
 - [DeleteComponentOutputComponent](docs/DeleteComponentOutputComponent.md)
 - [DeleteDeploymentInput](docs/DeleteDeploymentInput.md)
 - [DeleteDeploymentOutput](docs/DeleteDeploymentOutput.md)
 - [DeleteDeploymentOutputDeployment](docs/DeleteDeploymentOutputDeployment.md)
 - [DeleteEnvironmentAccountConnectionInput](docs/DeleteEnvironmentAccountConnectionInput.md)
 - [DeleteEnvironmentAccountConnectionOutput](docs/DeleteEnvironmentAccountConnectionOutput.md)
 - [DeleteEnvironmentAccountConnectionOutputEnvironmentAccountConnection](docs/DeleteEnvironmentAccountConnectionOutputEnvironmentAccountConnection.md)
 - [DeleteEnvironmentInput](docs/DeleteEnvironmentInput.md)
 - [DeleteEnvironmentOutput](docs/DeleteEnvironmentOutput.md)
 - [DeleteEnvironmentOutputEnvironment](docs/DeleteEnvironmentOutputEnvironment.md)
 - [DeleteEnvironmentTemplateInput](docs/DeleteEnvironmentTemplateInput.md)
 - [DeleteEnvironmentTemplateOutput](docs/DeleteEnvironmentTemplateOutput.md)
 - [DeleteEnvironmentTemplateOutputEnvironmentTemplate](docs/DeleteEnvironmentTemplateOutputEnvironmentTemplate.md)
 - [DeleteEnvironmentTemplateVersionInput](docs/DeleteEnvironmentTemplateVersionInput.md)
 - [DeleteEnvironmentTemplateVersionOutput](docs/DeleteEnvironmentTemplateVersionOutput.md)
 - [DeleteEnvironmentTemplateVersionOutputEnvironmentTemplateVersion](docs/DeleteEnvironmentTemplateVersionOutputEnvironmentTemplateVersion.md)
 - [DeleteRepositoryInput](docs/DeleteRepositoryInput.md)
 - [DeleteRepositoryOutput](docs/DeleteRepositoryOutput.md)
 - [DeleteRepositoryOutputRepository](docs/DeleteRepositoryOutputRepository.md)
 - [DeleteServiceInput](docs/DeleteServiceInput.md)
 - [DeleteServiceOutput](docs/DeleteServiceOutput.md)
 - [DeleteServiceOutputService](docs/DeleteServiceOutputService.md)
 - [DeleteServiceSyncConfigInput](docs/DeleteServiceSyncConfigInput.md)
 - [DeleteServiceSyncConfigOutput](docs/DeleteServiceSyncConfigOutput.md)
 - [DeleteServiceSyncConfigOutputServiceSyncConfig](docs/DeleteServiceSyncConfigOutputServiceSyncConfig.md)
 - [DeleteServiceTemplateInput](docs/DeleteServiceTemplateInput.md)
 - [DeleteServiceTemplateOutput](docs/DeleteServiceTemplateOutput.md)
 - [DeleteServiceTemplateOutputServiceTemplate](docs/DeleteServiceTemplateOutputServiceTemplate.md)
 - [DeleteServiceTemplateVersionInput](docs/DeleteServiceTemplateVersionInput.md)
 - [DeleteServiceTemplateVersionOutput](docs/DeleteServiceTemplateVersionOutput.md)
 - [DeleteServiceTemplateVersionOutputServiceTemplateVersion](docs/DeleteServiceTemplateVersionOutputServiceTemplateVersion.md)
 - [DeleteTemplateSyncConfigInput](docs/DeleteTemplateSyncConfigInput.md)
 - [DeleteTemplateSyncConfigOutput](docs/DeleteTemplateSyncConfigOutput.md)
 - [Deployment](docs/Deployment.md)
 - [DeploymentInitialState](docs/DeploymentInitialState.md)
 - [DeploymentState](docs/DeploymentState.md)
 - [DeploymentStateComponent](docs/DeploymentStateComponent.md)
 - [DeploymentStateEnvironment](docs/DeploymentStateEnvironment.md)
 - [DeploymentStateServiceInstance](docs/DeploymentStateServiceInstance.md)
 - [DeploymentStateServicePipeline](docs/DeploymentStateServicePipeline.md)
 - [DeploymentStatus](docs/DeploymentStatus.md)
 - [DeploymentSummary](docs/DeploymentSummary.md)
 - [DeploymentTargetResourceType](docs/DeploymentTargetResourceType.md)
 - [DeploymentTargetState](docs/DeploymentTargetState.md)
 - [DeploymentUpdateType](docs/DeploymentUpdateType.md)
 - [Environment](docs/Environment.md)
 - [EnvironmentAccountConnection](docs/EnvironmentAccountConnection.md)
 - [EnvironmentAccountConnectionRequesterAccountType](docs/EnvironmentAccountConnectionRequesterAccountType.md)
 - [EnvironmentAccountConnectionStatus](docs/EnvironmentAccountConnectionStatus.md)
 - [EnvironmentAccountConnectionSummary](docs/EnvironmentAccountConnectionSummary.md)
 - [EnvironmentProvisioningRepository](docs/EnvironmentProvisioningRepository.md)
 - [EnvironmentState](docs/EnvironmentState.md)
 - [EnvironmentSummary](docs/EnvironmentSummary.md)
 - [EnvironmentTemplate](docs/EnvironmentTemplate.md)
 - [EnvironmentTemplateFilter](docs/EnvironmentTemplateFilter.md)
 - [EnvironmentTemplateSummary](docs/EnvironmentTemplateSummary.md)
 - [EnvironmentTemplateVersion](docs/EnvironmentTemplateVersion.md)
 - [EnvironmentTemplateVersionSummary](docs/EnvironmentTemplateVersionSummary.md)
 - [GetAccountSettingsOutput](docs/GetAccountSettingsOutput.md)
 - [GetAccountSettingsOutputAccountSettings](docs/GetAccountSettingsOutputAccountSettings.md)
 - [GetComponentInput](docs/GetComponentInput.md)
 - [GetComponentOutput](docs/GetComponentOutput.md)
 - [GetComponentOutputComponent](docs/GetComponentOutputComponent.md)
 - [GetDeploymentInput](docs/GetDeploymentInput.md)
 - [GetDeploymentOutput](docs/GetDeploymentOutput.md)
 - [GetDeploymentOutputDeployment](docs/GetDeploymentOutputDeployment.md)
 - [GetEnvironmentAccountConnectionInput](docs/GetEnvironmentAccountConnectionInput.md)
 - [GetEnvironmentAccountConnectionOutput](docs/GetEnvironmentAccountConnectionOutput.md)
 - [GetEnvironmentAccountConnectionOutputEnvironmentAccountConnection](docs/GetEnvironmentAccountConnectionOutputEnvironmentAccountConnection.md)
 - [GetEnvironmentInput](docs/GetEnvironmentInput.md)
 - [GetEnvironmentOutput](docs/GetEnvironmentOutput.md)
 - [GetEnvironmentOutputEnvironment](docs/GetEnvironmentOutputEnvironment.md)
 - [GetEnvironmentTemplateInput](docs/GetEnvironmentTemplateInput.md)
 - [GetEnvironmentTemplateOutput](docs/GetEnvironmentTemplateOutput.md)
 - [GetEnvironmentTemplateOutputEnvironmentTemplate](docs/GetEnvironmentTemplateOutputEnvironmentTemplate.md)
 - [GetEnvironmentTemplateVersionInput](docs/GetEnvironmentTemplateVersionInput.md)
 - [GetEnvironmentTemplateVersionOutput](docs/GetEnvironmentTemplateVersionOutput.md)
 - [GetEnvironmentTemplateVersionOutputEnvironmentTemplateVersion](docs/GetEnvironmentTemplateVersionOutputEnvironmentTemplateVersion.md)
 - [GetRepositoryInput](docs/GetRepositoryInput.md)
 - [GetRepositoryOutput](docs/GetRepositoryOutput.md)
 - [GetRepositorySyncStatusInput](docs/GetRepositorySyncStatusInput.md)
 - [GetRepositorySyncStatusOutput](docs/GetRepositorySyncStatusOutput.md)
 - [GetRepositorySyncStatusOutputLatestSync](docs/GetRepositorySyncStatusOutputLatestSync.md)
 - [GetResourcesSummaryOutput](docs/GetResourcesSummaryOutput.md)
 - [GetResourcesSummaryOutputCounts](docs/GetResourcesSummaryOutputCounts.md)
 - [GetServiceInput](docs/GetServiceInput.md)
 - [GetServiceInstanceInput](docs/GetServiceInstanceInput.md)
 - [GetServiceInstanceOutput](docs/GetServiceInstanceOutput.md)
 - [GetServiceInstanceOutputServiceInstance](docs/GetServiceInstanceOutputServiceInstance.md)
 - [GetServiceInstanceSyncStatusInput](docs/GetServiceInstanceSyncStatusInput.md)
 - [GetServiceInstanceSyncStatusOutput](docs/GetServiceInstanceSyncStatusOutput.md)
 - [GetServiceInstanceSyncStatusOutputDesiredState](docs/GetServiceInstanceSyncStatusOutputDesiredState.md)
 - [GetServiceInstanceSyncStatusOutputLatestSuccessfulSync](docs/GetServiceInstanceSyncStatusOutputLatestSuccessfulSync.md)
 - [GetServiceInstanceSyncStatusOutputLatestSync](docs/GetServiceInstanceSyncStatusOutputLatestSync.md)
 - [GetServiceOutput](docs/GetServiceOutput.md)
 - [GetServiceOutputService](docs/GetServiceOutputService.md)
 - [GetServiceSyncBlockerSummaryInput](docs/GetServiceSyncBlockerSummaryInput.md)
 - [GetServiceSyncBlockerSummaryOutput](docs/GetServiceSyncBlockerSummaryOutput.md)
 - [GetServiceSyncBlockerSummaryOutputServiceSyncBlockerSummary](docs/GetServiceSyncBlockerSummaryOutputServiceSyncBlockerSummary.md)
 - [GetServiceSyncConfigInput](docs/GetServiceSyncConfigInput.md)
 - [GetServiceSyncConfigOutput](docs/GetServiceSyncConfigOutput.md)
 - [GetServiceSyncConfigOutputServiceSyncConfig](docs/GetServiceSyncConfigOutputServiceSyncConfig.md)
 - [GetServiceTemplateInput](docs/GetServiceTemplateInput.md)
 - [GetServiceTemplateOutput](docs/GetServiceTemplateOutput.md)
 - [GetServiceTemplateOutputServiceTemplate](docs/GetServiceTemplateOutputServiceTemplate.md)
 - [GetServiceTemplateVersionInput](docs/GetServiceTemplateVersionInput.md)
 - [GetServiceTemplateVersionOutput](docs/GetServiceTemplateVersionOutput.md)
 - [GetServiceTemplateVersionOutputServiceTemplateVersion](docs/GetServiceTemplateVersionOutputServiceTemplateVersion.md)
 - [GetTemplateSyncConfigInput](docs/GetTemplateSyncConfigInput.md)
 - [GetTemplateSyncConfigOutput](docs/GetTemplateSyncConfigOutput.md)
 - [GetTemplateSyncStatusInput](docs/GetTemplateSyncStatusInput.md)
 - [GetTemplateSyncStatusOutput](docs/GetTemplateSyncStatusOutput.md)
 - [GetTemplateSyncStatusOutputDesiredState](docs/GetTemplateSyncStatusOutputDesiredState.md)
 - [GetTemplateSyncStatusOutputLatestSuccessfulSync](docs/GetTemplateSyncStatusOutputLatestSuccessfulSync.md)
 - [GetTemplateSyncStatusOutputLatestSync](docs/GetTemplateSyncStatusOutputLatestSync.md)
 - [ListComponentOutputsInput](docs/ListComponentOutputsInput.md)
 - [ListComponentOutputsOutput](docs/ListComponentOutputsOutput.md)
 - [ListComponentProvisionedResourcesInput](docs/ListComponentProvisionedResourcesInput.md)
 - [ListComponentProvisionedResourcesOutput](docs/ListComponentProvisionedResourcesOutput.md)
 - [ListComponentsInput](docs/ListComponentsInput.md)
 - [ListComponentsOutput](docs/ListComponentsOutput.md)
 - [ListDeploymentsInput](docs/ListDeploymentsInput.md)
 - [ListDeploymentsOutput](docs/ListDeploymentsOutput.md)
 - [ListEnvironmentAccountConnectionsInput](docs/ListEnvironmentAccountConnectionsInput.md)
 - [ListEnvironmentAccountConnectionsOutput](docs/ListEnvironmentAccountConnectionsOutput.md)
 - [ListEnvironmentOutputsInput](docs/ListEnvironmentOutputsInput.md)
 - [ListEnvironmentOutputsOutput](docs/ListEnvironmentOutputsOutput.md)
 - [ListEnvironmentProvisionedResourcesInput](docs/ListEnvironmentProvisionedResourcesInput.md)
 - [ListEnvironmentProvisionedResourcesOutput](docs/ListEnvironmentProvisionedResourcesOutput.md)
 - [ListEnvironmentTemplateVersionsInput](docs/ListEnvironmentTemplateVersionsInput.md)
 - [ListEnvironmentTemplateVersionsOutput](docs/ListEnvironmentTemplateVersionsOutput.md)
 - [ListEnvironmentTemplatesInput](docs/ListEnvironmentTemplatesInput.md)
 - [ListEnvironmentTemplatesOutput](docs/ListEnvironmentTemplatesOutput.md)
 - [ListEnvironmentsInput](docs/ListEnvironmentsInput.md)
 - [ListEnvironmentsOutput](docs/ListEnvironmentsOutput.md)
 - [ListRepositoriesInput](docs/ListRepositoriesInput.md)
 - [ListRepositoriesOutput](docs/ListRepositoriesOutput.md)
 - [ListRepositorySyncDefinitionsInput](docs/ListRepositorySyncDefinitionsInput.md)
 - [ListRepositorySyncDefinitionsOutput](docs/ListRepositorySyncDefinitionsOutput.md)
 - [ListServiceInstanceOutputsInput](docs/ListServiceInstanceOutputsInput.md)
 - [ListServiceInstanceOutputsOutput](docs/ListServiceInstanceOutputsOutput.md)
 - [ListServiceInstanceProvisionedResourcesInput](docs/ListServiceInstanceProvisionedResourcesInput.md)
 - [ListServiceInstanceProvisionedResourcesOutput](docs/ListServiceInstanceProvisionedResourcesOutput.md)
 - [ListServiceInstancesFilter](docs/ListServiceInstancesFilter.md)
 - [ListServiceInstancesFilterBy](docs/ListServiceInstancesFilterBy.md)
 - [ListServiceInstancesInput](docs/ListServiceInstancesInput.md)
 - [ListServiceInstancesOutput](docs/ListServiceInstancesOutput.md)
 - [ListServiceInstancesSortBy](docs/ListServiceInstancesSortBy.md)
 - [ListServicePipelineOutputsInput](docs/ListServicePipelineOutputsInput.md)
 - [ListServicePipelineOutputsOutput](docs/ListServicePipelineOutputsOutput.md)
 - [ListServicePipelineProvisionedResourcesInput](docs/ListServicePipelineProvisionedResourcesInput.md)
 - [ListServicePipelineProvisionedResourcesOutput](docs/ListServicePipelineProvisionedResourcesOutput.md)
 - [ListServiceTemplateVersionsInput](docs/ListServiceTemplateVersionsInput.md)
 - [ListServiceTemplateVersionsOutput](docs/ListServiceTemplateVersionsOutput.md)
 - [ListServiceTemplatesInput](docs/ListServiceTemplatesInput.md)
 - [ListServiceTemplatesOutput](docs/ListServiceTemplatesOutput.md)
 - [ListServicesInput](docs/ListServicesInput.md)
 - [ListServicesOutput](docs/ListServicesOutput.md)
 - [ListTagsForResourceInput](docs/ListTagsForResourceInput.md)
 - [ListTagsForResourceOutput](docs/ListTagsForResourceOutput.md)
 - [NotifyResourceDeploymentStatusChangeInput](docs/NotifyResourceDeploymentStatusChangeInput.md)
 - [Output](docs/Output.md)
 - [ProvisionedResource](docs/ProvisionedResource.md)
 - [ProvisionedResourceEngine](docs/ProvisionedResourceEngine.md)
 - [Provisioning](docs/Provisioning.md)
 - [RejectEnvironmentAccountConnectionInput](docs/RejectEnvironmentAccountConnectionInput.md)
 - [RejectEnvironmentAccountConnectionOutput](docs/RejectEnvironmentAccountConnectionOutput.md)
 - [RejectEnvironmentAccountConnectionOutputEnvironmentAccountConnection](docs/RejectEnvironmentAccountConnectionOutputEnvironmentAccountConnection.md)
 - [Repository](docs/Repository.md)
 - [RepositoryBranch](docs/RepositoryBranch.md)
 - [RepositoryBranchInput](docs/RepositoryBranchInput.md)
 - [RepositoryProvider](docs/RepositoryProvider.md)
 - [RepositorySummary](docs/RepositorySummary.md)
 - [RepositorySyncAttempt](docs/RepositorySyncAttempt.md)
 - [RepositorySyncDefinition](docs/RepositorySyncDefinition.md)
 - [RepositorySyncEvent](docs/RepositorySyncEvent.md)
 - [RepositorySyncStatus](docs/RepositorySyncStatus.md)
 - [ResourceCountsSummary](docs/ResourceCountsSummary.md)
 - [ResourceDeploymentStatus](docs/ResourceDeploymentStatus.md)
 - [ResourceSyncAttempt](docs/ResourceSyncAttempt.md)
 - [ResourceSyncAttemptInitialRevision](docs/ResourceSyncAttemptInitialRevision.md)
 - [ResourceSyncAttemptTargetRevision](docs/ResourceSyncAttemptTargetRevision.md)
 - [ResourceSyncEvent](docs/ResourceSyncEvent.md)
 - [ResourceSyncStatus](docs/ResourceSyncStatus.md)
 - [Revision](docs/Revision.md)
 - [S3ObjectSource](docs/S3ObjectSource.md)
 - [Service](docs/Service.md)
 - [ServiceInstance](docs/ServiceInstance.md)
 - [ServiceInstanceState](docs/ServiceInstanceState.md)
 - [ServiceInstanceSummary](docs/ServiceInstanceSummary.md)
 - [ServicePipeline](docs/ServicePipeline.md)
 - [ServicePipelineState](docs/ServicePipelineState.md)
 - [ServiceStatus](docs/ServiceStatus.md)
 - [ServiceSummary](docs/ServiceSummary.md)
 - [ServiceSyncBlockerSummary](docs/ServiceSyncBlockerSummary.md)
 - [ServiceSyncConfig](docs/ServiceSyncConfig.md)
 - [ServiceTemplate](docs/ServiceTemplate.md)
 - [ServiceTemplateSummary](docs/ServiceTemplateSummary.md)
 - [ServiceTemplateSupportedComponentSourceType](docs/ServiceTemplateSupportedComponentSourceType.md)
 - [ServiceTemplateVersion](docs/ServiceTemplateVersion.md)
 - [ServiceTemplateVersionSummary](docs/ServiceTemplateVersionSummary.md)
 - [SortOrder](docs/SortOrder.md)
 - [SyncBlocker](docs/SyncBlocker.md)
 - [SyncBlockerContext](docs/SyncBlockerContext.md)
 - [SyncType](docs/SyncType.md)
 - [Tag](docs/Tag.md)
 - [TagResourceInput](docs/TagResourceInput.md)
 - [TemplateSyncConfig](docs/TemplateSyncConfig.md)
 - [TemplateType](docs/TemplateType.md)
 - [TemplateVersionSourceInput](docs/TemplateVersionSourceInput.md)
 - [TemplateVersionSourceInputS3](docs/TemplateVersionSourceInputS3.md)
 - [TemplateVersionStatus](docs/TemplateVersionStatus.md)
 - [UntagResourceInput](docs/UntagResourceInput.md)
 - [UpdateAccountSettingsInput](docs/UpdateAccountSettingsInput.md)
 - [UpdateAccountSettingsInputPipelineProvisioningRepository](docs/UpdateAccountSettingsInputPipelineProvisioningRepository.md)
 - [UpdateAccountSettingsOutput](docs/UpdateAccountSettingsOutput.md)
 - [UpdateAccountSettingsOutputAccountSettings](docs/UpdateAccountSettingsOutputAccountSettings.md)
 - [UpdateComponentInput](docs/UpdateComponentInput.md)
 - [UpdateComponentOutput](docs/UpdateComponentOutput.md)
 - [UpdateComponentOutputComponent](docs/UpdateComponentOutputComponent.md)
 - [UpdateEnvironmentAccountConnectionInput](docs/UpdateEnvironmentAccountConnectionInput.md)
 - [UpdateEnvironmentAccountConnectionOutput](docs/UpdateEnvironmentAccountConnectionOutput.md)
 - [UpdateEnvironmentInput](docs/UpdateEnvironmentInput.md)
 - [UpdateEnvironmentInputProvisioningRepository](docs/UpdateEnvironmentInputProvisioningRepository.md)
 - [UpdateEnvironmentOutput](docs/UpdateEnvironmentOutput.md)
 - [UpdateEnvironmentTemplateInput](docs/UpdateEnvironmentTemplateInput.md)
 - [UpdateEnvironmentTemplateOutput](docs/UpdateEnvironmentTemplateOutput.md)
 - [UpdateEnvironmentTemplateVersionInput](docs/UpdateEnvironmentTemplateVersionInput.md)
 - [UpdateEnvironmentTemplateVersionOutput](docs/UpdateEnvironmentTemplateVersionOutput.md)
 - [UpdateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion](docs/UpdateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion.md)
 - [UpdateServiceInput](docs/UpdateServiceInput.md)
 - [UpdateServiceInstanceInput](docs/UpdateServiceInstanceInput.md)
 - [UpdateServiceInstanceOutput](docs/UpdateServiceInstanceOutput.md)
 - [UpdateServiceOutput](docs/UpdateServiceOutput.md)
 - [UpdateServicePipelineInput](docs/UpdateServicePipelineInput.md)
 - [UpdateServicePipelineOutput](docs/UpdateServicePipelineOutput.md)
 - [UpdateServicePipelineOutputPipeline](docs/UpdateServicePipelineOutputPipeline.md)
 - [UpdateServiceSyncBlockerInput](docs/UpdateServiceSyncBlockerInput.md)
 - [UpdateServiceSyncBlockerOutput](docs/UpdateServiceSyncBlockerOutput.md)
 - [UpdateServiceSyncBlockerOutputServiceSyncBlocker](docs/UpdateServiceSyncBlockerOutputServiceSyncBlocker.md)
 - [UpdateServiceSyncConfigInput](docs/UpdateServiceSyncConfigInput.md)
 - [UpdateServiceSyncConfigOutput](docs/UpdateServiceSyncConfigOutput.md)
 - [UpdateServiceTemplateInput](docs/UpdateServiceTemplateInput.md)
 - [UpdateServiceTemplateOutput](docs/UpdateServiceTemplateOutput.md)
 - [UpdateServiceTemplateVersionInput](docs/UpdateServiceTemplateVersionInput.md)
 - [UpdateServiceTemplateVersionOutput](docs/UpdateServiceTemplateVersionOutput.md)
 - [UpdateServiceTemplateVersionOutputServiceTemplateVersion](docs/UpdateServiceTemplateVersionOutputServiceTemplateVersion.md)
 - [UpdateTemplateSyncConfigInput](docs/UpdateTemplateSyncConfigInput.md)
 - [UpdateTemplateSyncConfigOutput](docs/UpdateTemplateSyncConfigOutput.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="hmac"></a>
### hmac

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

mike.ralphson@gmail.com

