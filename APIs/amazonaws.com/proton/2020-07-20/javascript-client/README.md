# aws_proton

AwsProton - JavaScript client for aws_proton
<p>This is the Proton Service API Reference. It provides descriptions, syntax and usage examples for each of the <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Operations.html\">actions</a> and <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Types.html\">data types</a> for the Proton service.</p> <p>The documentation for each action shows the Query API request parameters and the XML response.</p> <p>Alternatively, you can use the Amazon Web Services CLI to access an API. For more information, see the <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html\">Amazon Web Services Command Line Interface User Guide</a>.</p> <p>The Proton service is a two-pronged automation framework. Administrators create service templates to provide standardized infrastructure and deployment tooling for serverless and container based applications. Developers, in turn, select from the available service templates to automate their application or service deployments.</p> <p>Because administrators define the infrastructure and tooling that Proton deploys and manages, they need permissions to use all of the listed API operations.</p> <p>When developers select a specific infrastructure and tooling set, Proton deploys their applications. To monitor their applications that are running on Proton, developers need permissions to the service <i>create</i>, <i>list</i>, <i>update</i> and <i>delete</i> API operations and the service instance <i>list</i> and <i>update</i> API operations.</p> <p>To learn more about Proton, see the <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html\">Proton User Guide</a>.</p> <p> <b>Ensuring Idempotency</b> </p> <p>When you make a mutating API request, the request typically returns a result before the asynchronous workflows of the operation are complete. Operations might also time out or encounter other server issues before they're complete, even if the request already returned a result. This might make it difficult to determine whether the request succeeded. Moreover, you might need to retry the request multiple times to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation occurs multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request action completes no more than one time. With an idempotent request, if the original request action completes successfully, any subsequent retries complete successfully without performing any further actions. However, the result might contain updated information, such as the current creation status.</p> <p>The following lists of APIs are grouped according to methods that ensure idempotency.</p> <p> <b>Idempotent create APIs with a client token</b> </p> <p>The API actions in this list support idempotency with the use of a <i>client token</i>. The corresponding Amazon Web Services CLI commands also support idempotency using a client token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request. We recommend that you <i>don't</i> reuse the same client token for other API requests. If you don’t provide a client token for these APIs, a default client token is automatically provided by SDKs.</p> <p>Given a request action that has succeeded:</p> <p>If you retry the request using the same client token and the same parameters, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If you retry the request using the same client token, but one or more of the parameters are different, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Client tokens expire eight hours after a request is made. If you retry the request with the expired token, a new resource is created.</p> <p>If the original resource is deleted and you retry the request, a new resource is created.</p> <p>Idempotent create APIs with a client token:</p> <ul> <li> <p>CreateEnvironmentTemplateVersion</p> </li> <li> <p>CreateServiceTemplateVersion</p> </li> <li> <p>CreateEnvironmentAccountConnection</p> </li> </ul> <p> <b>Idempotent create APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, and the original resource <i>hasn't</i> been modified, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If the original resource has been modified, the retry throws a <code>ConflictException</code>.</p> <p>If you retry with different input parameters, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Idempotent create APIs:</p> <ul> <li> <p>CreateEnvironmentTemplate</p> </li> <li> <p>CreateServiceTemplate</p> </li> <li> <p>CreateEnvironment</p> </li> <li> <p>CreateService</p> </li> </ul> <p> <b>Idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>When you retry the request with an API from this group and the resource was deleted, its metadata is returned in the response.</p> <p>If you retry and the resource doesn't exist, the response is empty.</p> <p>In both cases, the retry succeeds.</p> <p>Idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironmentTemplate</p> </li> <li> <p>DeleteEnvironmentTemplateVersion</p> </li> <li> <p>DeleteServiceTemplate</p> </li> <li> <p>DeleteServiceTemplateVersion</p> </li> <li> <p>DeleteEnvironmentAccountConnection</p> </li> </ul> <p> <b>Asynchronous idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, if the original request delete operation status is <code>DELETE_IN_PROGRESS</code>, the retry returns the resource detail data in the response without performing any further actions.</p> <p>If the original request delete operation is complete, a retry returns an empty response.</p> <p>Asynchronous idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironment</p> </li> <li> <p>DeleteService</p> </li> </ul>
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2020-07-20
- Package version: 2020-07-20
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://github.com/mermade/aws2openapi](https://github.com/mermade/aws2openapi)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install aws_proton --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your aws_proton from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var AwsProton = require('aws_proton');

var defaultClient = AwsProton.ApiClient.instance;
// Configure API key authorization: hmac
var hmac = defaultClient.authentications['hmac'];
hmac.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix['Authorization'] = "Token"

var api = new AwsProton.DefaultApi()
var xAmzTarget = "xAmzTarget_example"; // {String} 
var acceptEnvironmentAccountConnectionInput = new AwsProton.AcceptEnvironmentAccountConnectionInput(); // {AcceptEnvironmentAccountConnectionInput} 
var opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // {String} 
  'xAmzDate': "xAmzDate_example", // {String} 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // {String} 
  'xAmzCredential': "xAmzCredential_example", // {String} 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // {String} 
  'xAmzSignature': "xAmzSignature_example", // {String} 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // {String} 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.acceptEnvironmentAccountConnection(xAmzTarget, acceptEnvironmentAccountConnectionInput, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *http://proton.us-east-1.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AwsProton.DefaultApi* | [**acceptEnvironmentAccountConnection**](docs/DefaultApi.md#acceptEnvironmentAccountConnection) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.AcceptEnvironmentAccountConnection | 
*AwsProton.DefaultApi* | [**cancelComponentDeployment**](docs/DefaultApi.md#cancelComponentDeployment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CancelComponentDeployment | 
*AwsProton.DefaultApi* | [**cancelEnvironmentDeployment**](docs/DefaultApi.md#cancelEnvironmentDeployment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CancelEnvironmentDeployment | 
*AwsProton.DefaultApi* | [**cancelServiceInstanceDeployment**](docs/DefaultApi.md#cancelServiceInstanceDeployment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CancelServiceInstanceDeployment | 
*AwsProton.DefaultApi* | [**cancelServicePipelineDeployment**](docs/DefaultApi.md#cancelServicePipelineDeployment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CancelServicePipelineDeployment | 
*AwsProton.DefaultApi* | [**createComponent**](docs/DefaultApi.md#createComponent) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateComponent | 
*AwsProton.DefaultApi* | [**createEnvironment**](docs/DefaultApi.md#createEnvironment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateEnvironment | 
*AwsProton.DefaultApi* | [**createEnvironmentAccountConnection**](docs/DefaultApi.md#createEnvironmentAccountConnection) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateEnvironmentAccountConnection | 
*AwsProton.DefaultApi* | [**createEnvironmentTemplate**](docs/DefaultApi.md#createEnvironmentTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateEnvironmentTemplate | 
*AwsProton.DefaultApi* | [**createEnvironmentTemplateVersion**](docs/DefaultApi.md#createEnvironmentTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateEnvironmentTemplateVersion | 
*AwsProton.DefaultApi* | [**createRepository**](docs/DefaultApi.md#createRepository) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateRepository | 
*AwsProton.DefaultApi* | [**createService**](docs/DefaultApi.md#createService) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateService | 
*AwsProton.DefaultApi* | [**createServiceInstance**](docs/DefaultApi.md#createServiceInstance) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateServiceInstance | 
*AwsProton.DefaultApi* | [**createServiceSyncConfig**](docs/DefaultApi.md#createServiceSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateServiceSyncConfig | 
*AwsProton.DefaultApi* | [**createServiceTemplate**](docs/DefaultApi.md#createServiceTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateServiceTemplate | 
*AwsProton.DefaultApi* | [**createServiceTemplateVersion**](docs/DefaultApi.md#createServiceTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateServiceTemplateVersion | 
*AwsProton.DefaultApi* | [**createTemplateSyncConfig**](docs/DefaultApi.md#createTemplateSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.CreateTemplateSyncConfig | 
*AwsProton.DefaultApi* | [**deleteComponent**](docs/DefaultApi.md#deleteComponent) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteComponent | 
*AwsProton.DefaultApi* | [**deleteDeployment**](docs/DefaultApi.md#deleteDeployment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteDeployment | 
*AwsProton.DefaultApi* | [**deleteEnvironment**](docs/DefaultApi.md#deleteEnvironment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteEnvironment | 
*AwsProton.DefaultApi* | [**deleteEnvironmentAccountConnection**](docs/DefaultApi.md#deleteEnvironmentAccountConnection) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteEnvironmentAccountConnection | 
*AwsProton.DefaultApi* | [**deleteEnvironmentTemplate**](docs/DefaultApi.md#deleteEnvironmentTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteEnvironmentTemplate | 
*AwsProton.DefaultApi* | [**deleteEnvironmentTemplateVersion**](docs/DefaultApi.md#deleteEnvironmentTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteEnvironmentTemplateVersion | 
*AwsProton.DefaultApi* | [**deleteRepository**](docs/DefaultApi.md#deleteRepository) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteRepository | 
*AwsProton.DefaultApi* | [**deleteService**](docs/DefaultApi.md#deleteService) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteService | 
*AwsProton.DefaultApi* | [**deleteServiceSyncConfig**](docs/DefaultApi.md#deleteServiceSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteServiceSyncConfig | 
*AwsProton.DefaultApi* | [**deleteServiceTemplate**](docs/DefaultApi.md#deleteServiceTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteServiceTemplate | 
*AwsProton.DefaultApi* | [**deleteServiceTemplateVersion**](docs/DefaultApi.md#deleteServiceTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteServiceTemplateVersion | 
*AwsProton.DefaultApi* | [**deleteTemplateSyncConfig**](docs/DefaultApi.md#deleteTemplateSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.DeleteTemplateSyncConfig | 
*AwsProton.DefaultApi* | [**getAccountSettings**](docs/DefaultApi.md#getAccountSettings) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetAccountSettings | 
*AwsProton.DefaultApi* | [**getComponent**](docs/DefaultApi.md#getComponent) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetComponent | 
*AwsProton.DefaultApi* | [**getDeployment**](docs/DefaultApi.md#getDeployment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetDeployment | 
*AwsProton.DefaultApi* | [**getEnvironment**](docs/DefaultApi.md#getEnvironment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetEnvironment | 
*AwsProton.DefaultApi* | [**getEnvironmentAccountConnection**](docs/DefaultApi.md#getEnvironmentAccountConnection) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetEnvironmentAccountConnection | 
*AwsProton.DefaultApi* | [**getEnvironmentTemplate**](docs/DefaultApi.md#getEnvironmentTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetEnvironmentTemplate | 
*AwsProton.DefaultApi* | [**getEnvironmentTemplateVersion**](docs/DefaultApi.md#getEnvironmentTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetEnvironmentTemplateVersion | 
*AwsProton.DefaultApi* | [**getRepository**](docs/DefaultApi.md#getRepository) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetRepository | 
*AwsProton.DefaultApi* | [**getRepositorySyncStatus**](docs/DefaultApi.md#getRepositorySyncStatus) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetRepositorySyncStatus | 
*AwsProton.DefaultApi* | [**getResourcesSummary**](docs/DefaultApi.md#getResourcesSummary) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetResourcesSummary | 
*AwsProton.DefaultApi* | [**getService**](docs/DefaultApi.md#getService) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetService | 
*AwsProton.DefaultApi* | [**getServiceInstance**](docs/DefaultApi.md#getServiceInstance) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetServiceInstance | 
*AwsProton.DefaultApi* | [**getServiceInstanceSyncStatus**](docs/DefaultApi.md#getServiceInstanceSyncStatus) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetServiceInstanceSyncStatus | 
*AwsProton.DefaultApi* | [**getServiceSyncBlockerSummary**](docs/DefaultApi.md#getServiceSyncBlockerSummary) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetServiceSyncBlockerSummary | 
*AwsProton.DefaultApi* | [**getServiceSyncConfig**](docs/DefaultApi.md#getServiceSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetServiceSyncConfig | 
*AwsProton.DefaultApi* | [**getServiceTemplate**](docs/DefaultApi.md#getServiceTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetServiceTemplate | 
*AwsProton.DefaultApi* | [**getServiceTemplateVersion**](docs/DefaultApi.md#getServiceTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetServiceTemplateVersion | 
*AwsProton.DefaultApi* | [**getTemplateSyncConfig**](docs/DefaultApi.md#getTemplateSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetTemplateSyncConfig | 
*AwsProton.DefaultApi* | [**getTemplateSyncStatus**](docs/DefaultApi.md#getTemplateSyncStatus) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.GetTemplateSyncStatus | 
*AwsProton.DefaultApi* | [**listComponentOutputs**](docs/DefaultApi.md#listComponentOutputs) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListComponentOutputs | 
*AwsProton.DefaultApi* | [**listComponentProvisionedResources**](docs/DefaultApi.md#listComponentProvisionedResources) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListComponentProvisionedResources | 
*AwsProton.DefaultApi* | [**listComponents**](docs/DefaultApi.md#listComponents) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListComponents | 
*AwsProton.DefaultApi* | [**listDeployments**](docs/DefaultApi.md#listDeployments) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListDeployments | 
*AwsProton.DefaultApi* | [**listEnvironmentAccountConnections**](docs/DefaultApi.md#listEnvironmentAccountConnections) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListEnvironmentAccountConnections | 
*AwsProton.DefaultApi* | [**listEnvironmentOutputs**](docs/DefaultApi.md#listEnvironmentOutputs) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListEnvironmentOutputs | 
*AwsProton.DefaultApi* | [**listEnvironmentProvisionedResources**](docs/DefaultApi.md#listEnvironmentProvisionedResources) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListEnvironmentProvisionedResources | 
*AwsProton.DefaultApi* | [**listEnvironmentTemplateVersions**](docs/DefaultApi.md#listEnvironmentTemplateVersions) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListEnvironmentTemplateVersions | 
*AwsProton.DefaultApi* | [**listEnvironmentTemplates**](docs/DefaultApi.md#listEnvironmentTemplates) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListEnvironmentTemplates | 
*AwsProton.DefaultApi* | [**listEnvironments**](docs/DefaultApi.md#listEnvironments) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListEnvironments | 
*AwsProton.DefaultApi* | [**listRepositories**](docs/DefaultApi.md#listRepositories) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListRepositories | 
*AwsProton.DefaultApi* | [**listRepositorySyncDefinitions**](docs/DefaultApi.md#listRepositorySyncDefinitions) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListRepositorySyncDefinitions | 
*AwsProton.DefaultApi* | [**listServiceInstanceOutputs**](docs/DefaultApi.md#listServiceInstanceOutputs) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServiceInstanceOutputs | 
*AwsProton.DefaultApi* | [**listServiceInstanceProvisionedResources**](docs/DefaultApi.md#listServiceInstanceProvisionedResources) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServiceInstanceProvisionedResources | 
*AwsProton.DefaultApi* | [**listServiceInstances**](docs/DefaultApi.md#listServiceInstances) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServiceInstances | 
*AwsProton.DefaultApi* | [**listServicePipelineOutputs**](docs/DefaultApi.md#listServicePipelineOutputs) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServicePipelineOutputs | 
*AwsProton.DefaultApi* | [**listServicePipelineProvisionedResources**](docs/DefaultApi.md#listServicePipelineProvisionedResources) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServicePipelineProvisionedResources | 
*AwsProton.DefaultApi* | [**listServiceTemplateVersions**](docs/DefaultApi.md#listServiceTemplateVersions) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServiceTemplateVersions | 
*AwsProton.DefaultApi* | [**listServiceTemplates**](docs/DefaultApi.md#listServiceTemplates) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServiceTemplates | 
*AwsProton.DefaultApi* | [**listServices**](docs/DefaultApi.md#listServices) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListServices | 
*AwsProton.DefaultApi* | [**listTagsForResource**](docs/DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.ListTagsForResource | 
*AwsProton.DefaultApi* | [**notifyResourceDeploymentStatusChange**](docs/DefaultApi.md#notifyResourceDeploymentStatusChange) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.NotifyResourceDeploymentStatusChange | 
*AwsProton.DefaultApi* | [**rejectEnvironmentAccountConnection**](docs/DefaultApi.md#rejectEnvironmentAccountConnection) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.RejectEnvironmentAccountConnection | 
*AwsProton.DefaultApi* | [**tagResource**](docs/DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.TagResource | 
*AwsProton.DefaultApi* | [**untagResource**](docs/DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UntagResource | 
*AwsProton.DefaultApi* | [**updateAccountSettings**](docs/DefaultApi.md#updateAccountSettings) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateAccountSettings | 
*AwsProton.DefaultApi* | [**updateComponent**](docs/DefaultApi.md#updateComponent) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateComponent | 
*AwsProton.DefaultApi* | [**updateEnvironment**](docs/DefaultApi.md#updateEnvironment) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateEnvironment | 
*AwsProton.DefaultApi* | [**updateEnvironmentAccountConnection**](docs/DefaultApi.md#updateEnvironmentAccountConnection) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateEnvironmentAccountConnection | 
*AwsProton.DefaultApi* | [**updateEnvironmentTemplate**](docs/DefaultApi.md#updateEnvironmentTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateEnvironmentTemplate | 
*AwsProton.DefaultApi* | [**updateEnvironmentTemplateVersion**](docs/DefaultApi.md#updateEnvironmentTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateEnvironmentTemplateVersion | 
*AwsProton.DefaultApi* | [**updateService**](docs/DefaultApi.md#updateService) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateService | 
*AwsProton.DefaultApi* | [**updateServiceInstance**](docs/DefaultApi.md#updateServiceInstance) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateServiceInstance | 
*AwsProton.DefaultApi* | [**updateServicePipeline**](docs/DefaultApi.md#updateServicePipeline) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateServicePipeline | 
*AwsProton.DefaultApi* | [**updateServiceSyncBlocker**](docs/DefaultApi.md#updateServiceSyncBlocker) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateServiceSyncBlocker | 
*AwsProton.DefaultApi* | [**updateServiceSyncConfig**](docs/DefaultApi.md#updateServiceSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateServiceSyncConfig | 
*AwsProton.DefaultApi* | [**updateServiceTemplate**](docs/DefaultApi.md#updateServiceTemplate) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateServiceTemplate | 
*AwsProton.DefaultApi* | [**updateServiceTemplateVersion**](docs/DefaultApi.md#updateServiceTemplateVersion) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateServiceTemplateVersion | 
*AwsProton.DefaultApi* | [**updateTemplateSyncConfig**](docs/DefaultApi.md#updateTemplateSyncConfig) | **POST** /#X-Amz-Target&#x3D;AwsProton20200720.UpdateTemplateSyncConfig | 


## Documentation for Models

 - [AwsProton.AcceptEnvironmentAccountConnectionInput](docs/AcceptEnvironmentAccountConnectionInput.md)
 - [AwsProton.AcceptEnvironmentAccountConnectionOutput](docs/AcceptEnvironmentAccountConnectionOutput.md)
 - [AwsProton.AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection](docs/AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.md)
 - [AwsProton.AccountSettings](docs/AccountSettings.md)
 - [AwsProton.AccountSettingsPipelineProvisioningRepository](docs/AccountSettingsPipelineProvisioningRepository.md)
 - [AwsProton.BlockerStatus](docs/BlockerStatus.md)
 - [AwsProton.BlockerType](docs/BlockerType.md)
 - [AwsProton.CancelComponentDeploymentInput](docs/CancelComponentDeploymentInput.md)
 - [AwsProton.CancelComponentDeploymentOutput](docs/CancelComponentDeploymentOutput.md)
 - [AwsProton.CancelComponentDeploymentOutputComponent](docs/CancelComponentDeploymentOutputComponent.md)
 - [AwsProton.CancelEnvironmentDeploymentInput](docs/CancelEnvironmentDeploymentInput.md)
 - [AwsProton.CancelEnvironmentDeploymentOutput](docs/CancelEnvironmentDeploymentOutput.md)
 - [AwsProton.CancelEnvironmentDeploymentOutputEnvironment](docs/CancelEnvironmentDeploymentOutputEnvironment.md)
 - [AwsProton.CancelServiceInstanceDeploymentInput](docs/CancelServiceInstanceDeploymentInput.md)
 - [AwsProton.CancelServiceInstanceDeploymentOutput](docs/CancelServiceInstanceDeploymentOutput.md)
 - [AwsProton.CancelServiceInstanceDeploymentOutputServiceInstance](docs/CancelServiceInstanceDeploymentOutputServiceInstance.md)
 - [AwsProton.CancelServicePipelineDeploymentInput](docs/CancelServicePipelineDeploymentInput.md)
 - [AwsProton.CancelServicePipelineDeploymentOutput](docs/CancelServicePipelineDeploymentOutput.md)
 - [AwsProton.CancelServicePipelineDeploymentOutputPipeline](docs/CancelServicePipelineDeploymentOutputPipeline.md)
 - [AwsProton.CompatibleEnvironmentTemplate](docs/CompatibleEnvironmentTemplate.md)
 - [AwsProton.CompatibleEnvironmentTemplateInput](docs/CompatibleEnvironmentTemplateInput.md)
 - [AwsProton.Component](docs/Component.md)
 - [AwsProton.ComponentDeploymentUpdateType](docs/ComponentDeploymentUpdateType.md)
 - [AwsProton.ComponentState](docs/ComponentState.md)
 - [AwsProton.ComponentSummary](docs/ComponentSummary.md)
 - [AwsProton.CountsSummary](docs/CountsSummary.md)
 - [AwsProton.CountsSummaryComponents](docs/CountsSummaryComponents.md)
 - [AwsProton.CountsSummaryEnvironmentTemplates](docs/CountsSummaryEnvironmentTemplates.md)
 - [AwsProton.CountsSummaryEnvironments](docs/CountsSummaryEnvironments.md)
 - [AwsProton.CountsSummaryPipelines](docs/CountsSummaryPipelines.md)
 - [AwsProton.CountsSummaryServiceInstances](docs/CountsSummaryServiceInstances.md)
 - [AwsProton.CountsSummaryServiceTemplates](docs/CountsSummaryServiceTemplates.md)
 - [AwsProton.CountsSummaryServices](docs/CountsSummaryServices.md)
 - [AwsProton.CreateComponentInput](docs/CreateComponentInput.md)
 - [AwsProton.CreateComponentOutput](docs/CreateComponentOutput.md)
 - [AwsProton.CreateComponentOutputComponent](docs/CreateComponentOutputComponent.md)
 - [AwsProton.CreateEnvironmentAccountConnectionInput](docs/CreateEnvironmentAccountConnectionInput.md)
 - [AwsProton.CreateEnvironmentAccountConnectionOutput](docs/CreateEnvironmentAccountConnectionOutput.md)
 - [AwsProton.CreateEnvironmentAccountConnectionOutputEnvironmentAccountConnection](docs/CreateEnvironmentAccountConnectionOutputEnvironmentAccountConnection.md)
 - [AwsProton.CreateEnvironmentInput](docs/CreateEnvironmentInput.md)
 - [AwsProton.CreateEnvironmentInputProvisioningRepository](docs/CreateEnvironmentInputProvisioningRepository.md)
 - [AwsProton.CreateEnvironmentOutput](docs/CreateEnvironmentOutput.md)
 - [AwsProton.CreateEnvironmentOutputEnvironment](docs/CreateEnvironmentOutputEnvironment.md)
 - [AwsProton.CreateEnvironmentTemplateInput](docs/CreateEnvironmentTemplateInput.md)
 - [AwsProton.CreateEnvironmentTemplateOutput](docs/CreateEnvironmentTemplateOutput.md)
 - [AwsProton.CreateEnvironmentTemplateOutputEnvironmentTemplate](docs/CreateEnvironmentTemplateOutputEnvironmentTemplate.md)
 - [AwsProton.CreateEnvironmentTemplateVersionInput](docs/CreateEnvironmentTemplateVersionInput.md)
 - [AwsProton.CreateEnvironmentTemplateVersionInputSource](docs/CreateEnvironmentTemplateVersionInputSource.md)
 - [AwsProton.CreateEnvironmentTemplateVersionOutput](docs/CreateEnvironmentTemplateVersionOutput.md)
 - [AwsProton.CreateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion](docs/CreateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion.md)
 - [AwsProton.CreateRepositoryInput](docs/CreateRepositoryInput.md)
 - [AwsProton.CreateRepositoryOutput](docs/CreateRepositoryOutput.md)
 - [AwsProton.CreateRepositoryOutputRepository](docs/CreateRepositoryOutputRepository.md)
 - [AwsProton.CreateServiceInput](docs/CreateServiceInput.md)
 - [AwsProton.CreateServiceInstanceInput](docs/CreateServiceInstanceInput.md)
 - [AwsProton.CreateServiceInstanceOutput](docs/CreateServiceInstanceOutput.md)
 - [AwsProton.CreateServiceInstanceOutputServiceInstance](docs/CreateServiceInstanceOutputServiceInstance.md)
 - [AwsProton.CreateServiceOutput](docs/CreateServiceOutput.md)
 - [AwsProton.CreateServiceOutputService](docs/CreateServiceOutputService.md)
 - [AwsProton.CreateServiceSyncConfigInput](docs/CreateServiceSyncConfigInput.md)
 - [AwsProton.CreateServiceSyncConfigOutput](docs/CreateServiceSyncConfigOutput.md)
 - [AwsProton.CreateServiceSyncConfigOutputServiceSyncConfig](docs/CreateServiceSyncConfigOutputServiceSyncConfig.md)
 - [AwsProton.CreateServiceTemplateInput](docs/CreateServiceTemplateInput.md)
 - [AwsProton.CreateServiceTemplateOutput](docs/CreateServiceTemplateOutput.md)
 - [AwsProton.CreateServiceTemplateOutputServiceTemplate](docs/CreateServiceTemplateOutputServiceTemplate.md)
 - [AwsProton.CreateServiceTemplateVersionInput](docs/CreateServiceTemplateVersionInput.md)
 - [AwsProton.CreateServiceTemplateVersionInputSource](docs/CreateServiceTemplateVersionInputSource.md)
 - [AwsProton.CreateServiceTemplateVersionOutput](docs/CreateServiceTemplateVersionOutput.md)
 - [AwsProton.CreateServiceTemplateVersionOutputServiceTemplateVersion](docs/CreateServiceTemplateVersionOutputServiceTemplateVersion.md)
 - [AwsProton.CreateTemplateSyncConfigInput](docs/CreateTemplateSyncConfigInput.md)
 - [AwsProton.CreateTemplateSyncConfigOutput](docs/CreateTemplateSyncConfigOutput.md)
 - [AwsProton.CreateTemplateSyncConfigOutputTemplateSyncConfig](docs/CreateTemplateSyncConfigOutputTemplateSyncConfig.md)
 - [AwsProton.DeleteComponentInput](docs/DeleteComponentInput.md)
 - [AwsProton.DeleteComponentOutput](docs/DeleteComponentOutput.md)
 - [AwsProton.DeleteComponentOutputComponent](docs/DeleteComponentOutputComponent.md)
 - [AwsProton.DeleteDeploymentInput](docs/DeleteDeploymentInput.md)
 - [AwsProton.DeleteDeploymentOutput](docs/DeleteDeploymentOutput.md)
 - [AwsProton.DeleteDeploymentOutputDeployment](docs/DeleteDeploymentOutputDeployment.md)
 - [AwsProton.DeleteEnvironmentAccountConnectionInput](docs/DeleteEnvironmentAccountConnectionInput.md)
 - [AwsProton.DeleteEnvironmentAccountConnectionOutput](docs/DeleteEnvironmentAccountConnectionOutput.md)
 - [AwsProton.DeleteEnvironmentAccountConnectionOutputEnvironmentAccountConnection](docs/DeleteEnvironmentAccountConnectionOutputEnvironmentAccountConnection.md)
 - [AwsProton.DeleteEnvironmentInput](docs/DeleteEnvironmentInput.md)
 - [AwsProton.DeleteEnvironmentOutput](docs/DeleteEnvironmentOutput.md)
 - [AwsProton.DeleteEnvironmentOutputEnvironment](docs/DeleteEnvironmentOutputEnvironment.md)
 - [AwsProton.DeleteEnvironmentTemplateInput](docs/DeleteEnvironmentTemplateInput.md)
 - [AwsProton.DeleteEnvironmentTemplateOutput](docs/DeleteEnvironmentTemplateOutput.md)
 - [AwsProton.DeleteEnvironmentTemplateOutputEnvironmentTemplate](docs/DeleteEnvironmentTemplateOutputEnvironmentTemplate.md)
 - [AwsProton.DeleteEnvironmentTemplateVersionInput](docs/DeleteEnvironmentTemplateVersionInput.md)
 - [AwsProton.DeleteEnvironmentTemplateVersionOutput](docs/DeleteEnvironmentTemplateVersionOutput.md)
 - [AwsProton.DeleteEnvironmentTemplateVersionOutputEnvironmentTemplateVersion](docs/DeleteEnvironmentTemplateVersionOutputEnvironmentTemplateVersion.md)
 - [AwsProton.DeleteRepositoryInput](docs/DeleteRepositoryInput.md)
 - [AwsProton.DeleteRepositoryOutput](docs/DeleteRepositoryOutput.md)
 - [AwsProton.DeleteRepositoryOutputRepository](docs/DeleteRepositoryOutputRepository.md)
 - [AwsProton.DeleteServiceInput](docs/DeleteServiceInput.md)
 - [AwsProton.DeleteServiceOutput](docs/DeleteServiceOutput.md)
 - [AwsProton.DeleteServiceOutputService](docs/DeleteServiceOutputService.md)
 - [AwsProton.DeleteServiceSyncConfigInput](docs/DeleteServiceSyncConfigInput.md)
 - [AwsProton.DeleteServiceSyncConfigOutput](docs/DeleteServiceSyncConfigOutput.md)
 - [AwsProton.DeleteServiceSyncConfigOutputServiceSyncConfig](docs/DeleteServiceSyncConfigOutputServiceSyncConfig.md)
 - [AwsProton.DeleteServiceTemplateInput](docs/DeleteServiceTemplateInput.md)
 - [AwsProton.DeleteServiceTemplateOutput](docs/DeleteServiceTemplateOutput.md)
 - [AwsProton.DeleteServiceTemplateOutputServiceTemplate](docs/DeleteServiceTemplateOutputServiceTemplate.md)
 - [AwsProton.DeleteServiceTemplateVersionInput](docs/DeleteServiceTemplateVersionInput.md)
 - [AwsProton.DeleteServiceTemplateVersionOutput](docs/DeleteServiceTemplateVersionOutput.md)
 - [AwsProton.DeleteServiceTemplateVersionOutputServiceTemplateVersion](docs/DeleteServiceTemplateVersionOutputServiceTemplateVersion.md)
 - [AwsProton.DeleteTemplateSyncConfigInput](docs/DeleteTemplateSyncConfigInput.md)
 - [AwsProton.DeleteTemplateSyncConfigOutput](docs/DeleteTemplateSyncConfigOutput.md)
 - [AwsProton.Deployment](docs/Deployment.md)
 - [AwsProton.DeploymentInitialState](docs/DeploymentInitialState.md)
 - [AwsProton.DeploymentState](docs/DeploymentState.md)
 - [AwsProton.DeploymentStateComponent](docs/DeploymentStateComponent.md)
 - [AwsProton.DeploymentStateEnvironment](docs/DeploymentStateEnvironment.md)
 - [AwsProton.DeploymentStateServiceInstance](docs/DeploymentStateServiceInstance.md)
 - [AwsProton.DeploymentStateServicePipeline](docs/DeploymentStateServicePipeline.md)
 - [AwsProton.DeploymentStatus](docs/DeploymentStatus.md)
 - [AwsProton.DeploymentSummary](docs/DeploymentSummary.md)
 - [AwsProton.DeploymentTargetResourceType](docs/DeploymentTargetResourceType.md)
 - [AwsProton.DeploymentTargetState](docs/DeploymentTargetState.md)
 - [AwsProton.DeploymentUpdateType](docs/DeploymentUpdateType.md)
 - [AwsProton.Environment](docs/Environment.md)
 - [AwsProton.EnvironmentAccountConnection](docs/EnvironmentAccountConnection.md)
 - [AwsProton.EnvironmentAccountConnectionRequesterAccountType](docs/EnvironmentAccountConnectionRequesterAccountType.md)
 - [AwsProton.EnvironmentAccountConnectionStatus](docs/EnvironmentAccountConnectionStatus.md)
 - [AwsProton.EnvironmentAccountConnectionSummary](docs/EnvironmentAccountConnectionSummary.md)
 - [AwsProton.EnvironmentProvisioningRepository](docs/EnvironmentProvisioningRepository.md)
 - [AwsProton.EnvironmentState](docs/EnvironmentState.md)
 - [AwsProton.EnvironmentSummary](docs/EnvironmentSummary.md)
 - [AwsProton.EnvironmentTemplate](docs/EnvironmentTemplate.md)
 - [AwsProton.EnvironmentTemplateFilter](docs/EnvironmentTemplateFilter.md)
 - [AwsProton.EnvironmentTemplateSummary](docs/EnvironmentTemplateSummary.md)
 - [AwsProton.EnvironmentTemplateVersion](docs/EnvironmentTemplateVersion.md)
 - [AwsProton.EnvironmentTemplateVersionSummary](docs/EnvironmentTemplateVersionSummary.md)
 - [AwsProton.GetAccountSettingsOutput](docs/GetAccountSettingsOutput.md)
 - [AwsProton.GetAccountSettingsOutputAccountSettings](docs/GetAccountSettingsOutputAccountSettings.md)
 - [AwsProton.GetComponentInput](docs/GetComponentInput.md)
 - [AwsProton.GetComponentOutput](docs/GetComponentOutput.md)
 - [AwsProton.GetComponentOutputComponent](docs/GetComponentOutputComponent.md)
 - [AwsProton.GetDeploymentInput](docs/GetDeploymentInput.md)
 - [AwsProton.GetDeploymentOutput](docs/GetDeploymentOutput.md)
 - [AwsProton.GetDeploymentOutputDeployment](docs/GetDeploymentOutputDeployment.md)
 - [AwsProton.GetEnvironmentAccountConnectionInput](docs/GetEnvironmentAccountConnectionInput.md)
 - [AwsProton.GetEnvironmentAccountConnectionOutput](docs/GetEnvironmentAccountConnectionOutput.md)
 - [AwsProton.GetEnvironmentAccountConnectionOutputEnvironmentAccountConnection](docs/GetEnvironmentAccountConnectionOutputEnvironmentAccountConnection.md)
 - [AwsProton.GetEnvironmentInput](docs/GetEnvironmentInput.md)
 - [AwsProton.GetEnvironmentOutput](docs/GetEnvironmentOutput.md)
 - [AwsProton.GetEnvironmentOutputEnvironment](docs/GetEnvironmentOutputEnvironment.md)
 - [AwsProton.GetEnvironmentTemplateInput](docs/GetEnvironmentTemplateInput.md)
 - [AwsProton.GetEnvironmentTemplateOutput](docs/GetEnvironmentTemplateOutput.md)
 - [AwsProton.GetEnvironmentTemplateOutputEnvironmentTemplate](docs/GetEnvironmentTemplateOutputEnvironmentTemplate.md)
 - [AwsProton.GetEnvironmentTemplateVersionInput](docs/GetEnvironmentTemplateVersionInput.md)
 - [AwsProton.GetEnvironmentTemplateVersionOutput](docs/GetEnvironmentTemplateVersionOutput.md)
 - [AwsProton.GetEnvironmentTemplateVersionOutputEnvironmentTemplateVersion](docs/GetEnvironmentTemplateVersionOutputEnvironmentTemplateVersion.md)
 - [AwsProton.GetRepositoryInput](docs/GetRepositoryInput.md)
 - [AwsProton.GetRepositoryOutput](docs/GetRepositoryOutput.md)
 - [AwsProton.GetRepositorySyncStatusInput](docs/GetRepositorySyncStatusInput.md)
 - [AwsProton.GetRepositorySyncStatusOutput](docs/GetRepositorySyncStatusOutput.md)
 - [AwsProton.GetRepositorySyncStatusOutputLatestSync](docs/GetRepositorySyncStatusOutputLatestSync.md)
 - [AwsProton.GetResourcesSummaryOutput](docs/GetResourcesSummaryOutput.md)
 - [AwsProton.GetResourcesSummaryOutputCounts](docs/GetResourcesSummaryOutputCounts.md)
 - [AwsProton.GetServiceInput](docs/GetServiceInput.md)
 - [AwsProton.GetServiceInstanceInput](docs/GetServiceInstanceInput.md)
 - [AwsProton.GetServiceInstanceOutput](docs/GetServiceInstanceOutput.md)
 - [AwsProton.GetServiceInstanceOutputServiceInstance](docs/GetServiceInstanceOutputServiceInstance.md)
 - [AwsProton.GetServiceInstanceSyncStatusInput](docs/GetServiceInstanceSyncStatusInput.md)
 - [AwsProton.GetServiceInstanceSyncStatusOutput](docs/GetServiceInstanceSyncStatusOutput.md)
 - [AwsProton.GetServiceInstanceSyncStatusOutputDesiredState](docs/GetServiceInstanceSyncStatusOutputDesiredState.md)
 - [AwsProton.GetServiceInstanceSyncStatusOutputLatestSuccessfulSync](docs/GetServiceInstanceSyncStatusOutputLatestSuccessfulSync.md)
 - [AwsProton.GetServiceInstanceSyncStatusOutputLatestSync](docs/GetServiceInstanceSyncStatusOutputLatestSync.md)
 - [AwsProton.GetServiceOutput](docs/GetServiceOutput.md)
 - [AwsProton.GetServiceOutputService](docs/GetServiceOutputService.md)
 - [AwsProton.GetServiceSyncBlockerSummaryInput](docs/GetServiceSyncBlockerSummaryInput.md)
 - [AwsProton.GetServiceSyncBlockerSummaryOutput](docs/GetServiceSyncBlockerSummaryOutput.md)
 - [AwsProton.GetServiceSyncBlockerSummaryOutputServiceSyncBlockerSummary](docs/GetServiceSyncBlockerSummaryOutputServiceSyncBlockerSummary.md)
 - [AwsProton.GetServiceSyncConfigInput](docs/GetServiceSyncConfigInput.md)
 - [AwsProton.GetServiceSyncConfigOutput](docs/GetServiceSyncConfigOutput.md)
 - [AwsProton.GetServiceSyncConfigOutputServiceSyncConfig](docs/GetServiceSyncConfigOutputServiceSyncConfig.md)
 - [AwsProton.GetServiceTemplateInput](docs/GetServiceTemplateInput.md)
 - [AwsProton.GetServiceTemplateOutput](docs/GetServiceTemplateOutput.md)
 - [AwsProton.GetServiceTemplateOutputServiceTemplate](docs/GetServiceTemplateOutputServiceTemplate.md)
 - [AwsProton.GetServiceTemplateVersionInput](docs/GetServiceTemplateVersionInput.md)
 - [AwsProton.GetServiceTemplateVersionOutput](docs/GetServiceTemplateVersionOutput.md)
 - [AwsProton.GetServiceTemplateVersionOutputServiceTemplateVersion](docs/GetServiceTemplateVersionOutputServiceTemplateVersion.md)
 - [AwsProton.GetTemplateSyncConfigInput](docs/GetTemplateSyncConfigInput.md)
 - [AwsProton.GetTemplateSyncConfigOutput](docs/GetTemplateSyncConfigOutput.md)
 - [AwsProton.GetTemplateSyncStatusInput](docs/GetTemplateSyncStatusInput.md)
 - [AwsProton.GetTemplateSyncStatusOutput](docs/GetTemplateSyncStatusOutput.md)
 - [AwsProton.GetTemplateSyncStatusOutputDesiredState](docs/GetTemplateSyncStatusOutputDesiredState.md)
 - [AwsProton.GetTemplateSyncStatusOutputLatestSuccessfulSync](docs/GetTemplateSyncStatusOutputLatestSuccessfulSync.md)
 - [AwsProton.GetTemplateSyncStatusOutputLatestSync](docs/GetTemplateSyncStatusOutputLatestSync.md)
 - [AwsProton.ListComponentOutputsInput](docs/ListComponentOutputsInput.md)
 - [AwsProton.ListComponentOutputsOutput](docs/ListComponentOutputsOutput.md)
 - [AwsProton.ListComponentProvisionedResourcesInput](docs/ListComponentProvisionedResourcesInput.md)
 - [AwsProton.ListComponentProvisionedResourcesOutput](docs/ListComponentProvisionedResourcesOutput.md)
 - [AwsProton.ListComponentsInput](docs/ListComponentsInput.md)
 - [AwsProton.ListComponentsOutput](docs/ListComponentsOutput.md)
 - [AwsProton.ListDeploymentsInput](docs/ListDeploymentsInput.md)
 - [AwsProton.ListDeploymentsOutput](docs/ListDeploymentsOutput.md)
 - [AwsProton.ListEnvironmentAccountConnectionsInput](docs/ListEnvironmentAccountConnectionsInput.md)
 - [AwsProton.ListEnvironmentAccountConnectionsOutput](docs/ListEnvironmentAccountConnectionsOutput.md)
 - [AwsProton.ListEnvironmentOutputsInput](docs/ListEnvironmentOutputsInput.md)
 - [AwsProton.ListEnvironmentOutputsOutput](docs/ListEnvironmentOutputsOutput.md)
 - [AwsProton.ListEnvironmentProvisionedResourcesInput](docs/ListEnvironmentProvisionedResourcesInput.md)
 - [AwsProton.ListEnvironmentProvisionedResourcesOutput](docs/ListEnvironmentProvisionedResourcesOutput.md)
 - [AwsProton.ListEnvironmentTemplateVersionsInput](docs/ListEnvironmentTemplateVersionsInput.md)
 - [AwsProton.ListEnvironmentTemplateVersionsOutput](docs/ListEnvironmentTemplateVersionsOutput.md)
 - [AwsProton.ListEnvironmentTemplatesInput](docs/ListEnvironmentTemplatesInput.md)
 - [AwsProton.ListEnvironmentTemplatesOutput](docs/ListEnvironmentTemplatesOutput.md)
 - [AwsProton.ListEnvironmentsInput](docs/ListEnvironmentsInput.md)
 - [AwsProton.ListEnvironmentsOutput](docs/ListEnvironmentsOutput.md)
 - [AwsProton.ListRepositoriesInput](docs/ListRepositoriesInput.md)
 - [AwsProton.ListRepositoriesOutput](docs/ListRepositoriesOutput.md)
 - [AwsProton.ListRepositorySyncDefinitionsInput](docs/ListRepositorySyncDefinitionsInput.md)
 - [AwsProton.ListRepositorySyncDefinitionsOutput](docs/ListRepositorySyncDefinitionsOutput.md)
 - [AwsProton.ListServiceInstanceOutputsInput](docs/ListServiceInstanceOutputsInput.md)
 - [AwsProton.ListServiceInstanceOutputsOutput](docs/ListServiceInstanceOutputsOutput.md)
 - [AwsProton.ListServiceInstanceProvisionedResourcesInput](docs/ListServiceInstanceProvisionedResourcesInput.md)
 - [AwsProton.ListServiceInstanceProvisionedResourcesOutput](docs/ListServiceInstanceProvisionedResourcesOutput.md)
 - [AwsProton.ListServiceInstancesFilter](docs/ListServiceInstancesFilter.md)
 - [AwsProton.ListServiceInstancesFilterBy](docs/ListServiceInstancesFilterBy.md)
 - [AwsProton.ListServiceInstancesInput](docs/ListServiceInstancesInput.md)
 - [AwsProton.ListServiceInstancesOutput](docs/ListServiceInstancesOutput.md)
 - [AwsProton.ListServiceInstancesSortBy](docs/ListServiceInstancesSortBy.md)
 - [AwsProton.ListServicePipelineOutputsInput](docs/ListServicePipelineOutputsInput.md)
 - [AwsProton.ListServicePipelineOutputsOutput](docs/ListServicePipelineOutputsOutput.md)
 - [AwsProton.ListServicePipelineProvisionedResourcesInput](docs/ListServicePipelineProvisionedResourcesInput.md)
 - [AwsProton.ListServicePipelineProvisionedResourcesOutput](docs/ListServicePipelineProvisionedResourcesOutput.md)
 - [AwsProton.ListServiceTemplateVersionsInput](docs/ListServiceTemplateVersionsInput.md)
 - [AwsProton.ListServiceTemplateVersionsOutput](docs/ListServiceTemplateVersionsOutput.md)
 - [AwsProton.ListServiceTemplatesInput](docs/ListServiceTemplatesInput.md)
 - [AwsProton.ListServiceTemplatesOutput](docs/ListServiceTemplatesOutput.md)
 - [AwsProton.ListServicesInput](docs/ListServicesInput.md)
 - [AwsProton.ListServicesOutput](docs/ListServicesOutput.md)
 - [AwsProton.ListTagsForResourceInput](docs/ListTagsForResourceInput.md)
 - [AwsProton.ListTagsForResourceOutput](docs/ListTagsForResourceOutput.md)
 - [AwsProton.NotifyResourceDeploymentStatusChangeInput](docs/NotifyResourceDeploymentStatusChangeInput.md)
 - [AwsProton.Output](docs/Output.md)
 - [AwsProton.ProvisionedResource](docs/ProvisionedResource.md)
 - [AwsProton.ProvisionedResourceEngine](docs/ProvisionedResourceEngine.md)
 - [AwsProton.Provisioning](docs/Provisioning.md)
 - [AwsProton.RejectEnvironmentAccountConnectionInput](docs/RejectEnvironmentAccountConnectionInput.md)
 - [AwsProton.RejectEnvironmentAccountConnectionOutput](docs/RejectEnvironmentAccountConnectionOutput.md)
 - [AwsProton.RejectEnvironmentAccountConnectionOutputEnvironmentAccountConnection](docs/RejectEnvironmentAccountConnectionOutputEnvironmentAccountConnection.md)
 - [AwsProton.Repository](docs/Repository.md)
 - [AwsProton.RepositoryBranch](docs/RepositoryBranch.md)
 - [AwsProton.RepositoryBranchInput](docs/RepositoryBranchInput.md)
 - [AwsProton.RepositoryProvider](docs/RepositoryProvider.md)
 - [AwsProton.RepositorySummary](docs/RepositorySummary.md)
 - [AwsProton.RepositorySyncAttempt](docs/RepositorySyncAttempt.md)
 - [AwsProton.RepositorySyncDefinition](docs/RepositorySyncDefinition.md)
 - [AwsProton.RepositorySyncEvent](docs/RepositorySyncEvent.md)
 - [AwsProton.RepositorySyncStatus](docs/RepositorySyncStatus.md)
 - [AwsProton.ResourceCountsSummary](docs/ResourceCountsSummary.md)
 - [AwsProton.ResourceDeploymentStatus](docs/ResourceDeploymentStatus.md)
 - [AwsProton.ResourceSyncAttempt](docs/ResourceSyncAttempt.md)
 - [AwsProton.ResourceSyncAttemptInitialRevision](docs/ResourceSyncAttemptInitialRevision.md)
 - [AwsProton.ResourceSyncAttemptTargetRevision](docs/ResourceSyncAttemptTargetRevision.md)
 - [AwsProton.ResourceSyncEvent](docs/ResourceSyncEvent.md)
 - [AwsProton.ResourceSyncStatus](docs/ResourceSyncStatus.md)
 - [AwsProton.Revision](docs/Revision.md)
 - [AwsProton.S3ObjectSource](docs/S3ObjectSource.md)
 - [AwsProton.Service](docs/Service.md)
 - [AwsProton.ServiceInstance](docs/ServiceInstance.md)
 - [AwsProton.ServiceInstanceState](docs/ServiceInstanceState.md)
 - [AwsProton.ServiceInstanceSummary](docs/ServiceInstanceSummary.md)
 - [AwsProton.ServicePipeline](docs/ServicePipeline.md)
 - [AwsProton.ServicePipelineState](docs/ServicePipelineState.md)
 - [AwsProton.ServiceStatus](docs/ServiceStatus.md)
 - [AwsProton.ServiceSummary](docs/ServiceSummary.md)
 - [AwsProton.ServiceSyncBlockerSummary](docs/ServiceSyncBlockerSummary.md)
 - [AwsProton.ServiceSyncConfig](docs/ServiceSyncConfig.md)
 - [AwsProton.ServiceTemplate](docs/ServiceTemplate.md)
 - [AwsProton.ServiceTemplateSummary](docs/ServiceTemplateSummary.md)
 - [AwsProton.ServiceTemplateSupportedComponentSourceType](docs/ServiceTemplateSupportedComponentSourceType.md)
 - [AwsProton.ServiceTemplateVersion](docs/ServiceTemplateVersion.md)
 - [AwsProton.ServiceTemplateVersionSummary](docs/ServiceTemplateVersionSummary.md)
 - [AwsProton.SortOrder](docs/SortOrder.md)
 - [AwsProton.SyncBlocker](docs/SyncBlocker.md)
 - [AwsProton.SyncBlockerContext](docs/SyncBlockerContext.md)
 - [AwsProton.SyncType](docs/SyncType.md)
 - [AwsProton.Tag](docs/Tag.md)
 - [AwsProton.TagResourceInput](docs/TagResourceInput.md)
 - [AwsProton.TemplateSyncConfig](docs/TemplateSyncConfig.md)
 - [AwsProton.TemplateType](docs/TemplateType.md)
 - [AwsProton.TemplateVersionSourceInput](docs/TemplateVersionSourceInput.md)
 - [AwsProton.TemplateVersionSourceInputS3](docs/TemplateVersionSourceInputS3.md)
 - [AwsProton.TemplateVersionStatus](docs/TemplateVersionStatus.md)
 - [AwsProton.UntagResourceInput](docs/UntagResourceInput.md)
 - [AwsProton.UpdateAccountSettingsInput](docs/UpdateAccountSettingsInput.md)
 - [AwsProton.UpdateAccountSettingsInputPipelineProvisioningRepository](docs/UpdateAccountSettingsInputPipelineProvisioningRepository.md)
 - [AwsProton.UpdateAccountSettingsOutput](docs/UpdateAccountSettingsOutput.md)
 - [AwsProton.UpdateAccountSettingsOutputAccountSettings](docs/UpdateAccountSettingsOutputAccountSettings.md)
 - [AwsProton.UpdateComponentInput](docs/UpdateComponentInput.md)
 - [AwsProton.UpdateComponentOutput](docs/UpdateComponentOutput.md)
 - [AwsProton.UpdateComponentOutputComponent](docs/UpdateComponentOutputComponent.md)
 - [AwsProton.UpdateEnvironmentAccountConnectionInput](docs/UpdateEnvironmentAccountConnectionInput.md)
 - [AwsProton.UpdateEnvironmentAccountConnectionOutput](docs/UpdateEnvironmentAccountConnectionOutput.md)
 - [AwsProton.UpdateEnvironmentInput](docs/UpdateEnvironmentInput.md)
 - [AwsProton.UpdateEnvironmentInputProvisioningRepository](docs/UpdateEnvironmentInputProvisioningRepository.md)
 - [AwsProton.UpdateEnvironmentOutput](docs/UpdateEnvironmentOutput.md)
 - [AwsProton.UpdateEnvironmentTemplateInput](docs/UpdateEnvironmentTemplateInput.md)
 - [AwsProton.UpdateEnvironmentTemplateOutput](docs/UpdateEnvironmentTemplateOutput.md)
 - [AwsProton.UpdateEnvironmentTemplateVersionInput](docs/UpdateEnvironmentTemplateVersionInput.md)
 - [AwsProton.UpdateEnvironmentTemplateVersionOutput](docs/UpdateEnvironmentTemplateVersionOutput.md)
 - [AwsProton.UpdateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion](docs/UpdateEnvironmentTemplateVersionOutputEnvironmentTemplateVersion.md)
 - [AwsProton.UpdateServiceInput](docs/UpdateServiceInput.md)
 - [AwsProton.UpdateServiceInstanceInput](docs/UpdateServiceInstanceInput.md)
 - [AwsProton.UpdateServiceInstanceOutput](docs/UpdateServiceInstanceOutput.md)
 - [AwsProton.UpdateServiceOutput](docs/UpdateServiceOutput.md)
 - [AwsProton.UpdateServicePipelineInput](docs/UpdateServicePipelineInput.md)
 - [AwsProton.UpdateServicePipelineOutput](docs/UpdateServicePipelineOutput.md)
 - [AwsProton.UpdateServicePipelineOutputPipeline](docs/UpdateServicePipelineOutputPipeline.md)
 - [AwsProton.UpdateServiceSyncBlockerInput](docs/UpdateServiceSyncBlockerInput.md)
 - [AwsProton.UpdateServiceSyncBlockerOutput](docs/UpdateServiceSyncBlockerOutput.md)
 - [AwsProton.UpdateServiceSyncBlockerOutputServiceSyncBlocker](docs/UpdateServiceSyncBlockerOutputServiceSyncBlocker.md)
 - [AwsProton.UpdateServiceSyncConfigInput](docs/UpdateServiceSyncConfigInput.md)
 - [AwsProton.UpdateServiceSyncConfigOutput](docs/UpdateServiceSyncConfigOutput.md)
 - [AwsProton.UpdateServiceTemplateInput](docs/UpdateServiceTemplateInput.md)
 - [AwsProton.UpdateServiceTemplateOutput](docs/UpdateServiceTemplateOutput.md)
 - [AwsProton.UpdateServiceTemplateVersionInput](docs/UpdateServiceTemplateVersionInput.md)
 - [AwsProton.UpdateServiceTemplateVersionOutput](docs/UpdateServiceTemplateVersionOutput.md)
 - [AwsProton.UpdateServiceTemplateVersionOutputServiceTemplateVersion](docs/UpdateServiceTemplateVersionOutputServiceTemplateVersion.md)
 - [AwsProton.UpdateTemplateSyncConfigInput](docs/UpdateTemplateSyncConfigInput.md)
 - [AwsProton.UpdateTemplateSyncConfigOutput](docs/UpdateTemplateSyncConfigOutput.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### hmac


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

