/**
 * AWS Proton
 * <p>This is the Proton Service API Reference. It provides descriptions, syntax and usage examples for each of the <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Operations.html\">actions</a> and <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Types.html\">data types</a> for the Proton service.</p> <p>The documentation for each action shows the Query API request parameters and the XML response.</p> <p>Alternatively, you can use the Amazon Web Services CLI to access an API. For more information, see the <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html\">Amazon Web Services Command Line Interface User Guide</a>.</p> <p>The Proton service is a two-pronged automation framework. Administrators create service templates to provide standardized infrastructure and deployment tooling for serverless and container based applications. Developers, in turn, select from the available service templates to automate their application or service deployments.</p> <p>Because administrators define the infrastructure and tooling that Proton deploys and manages, they need permissions to use all of the listed API operations.</p> <p>When developers select a specific infrastructure and tooling set, Proton deploys their applications. To monitor their applications that are running on Proton, developers need permissions to the service <i>create</i>, <i>list</i>, <i>update</i> and <i>delete</i> API operations and the service instance <i>list</i> and <i>update</i> API operations.</p> <p>To learn more about Proton, see the <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html\">Proton User Guide</a>.</p> <p> <b>Ensuring Idempotency</b> </p> <p>When you make a mutating API request, the request typically returns a result before the asynchronous workflows of the operation are complete. Operations might also time out or encounter other server issues before they're complete, even if the request already returned a result. This might make it difficult to determine whether the request succeeded. Moreover, you might need to retry the request multiple times to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation occurs multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request action completes no more than one time. With an idempotent request, if the original request action completes successfully, any subsequent retries complete successfully without performing any further actions. However, the result might contain updated information, such as the current creation status.</p> <p>The following lists of APIs are grouped according to methods that ensure idempotency.</p> <p> <b>Idempotent create APIs with a client token</b> </p> <p>The API actions in this list support idempotency with the use of a <i>client token</i>. The corresponding Amazon Web Services CLI commands also support idempotency using a client token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request. We recommend that you <i>don't</i> reuse the same client token for other API requests. If you don’t provide a client token for these APIs, a default client token is automatically provided by SDKs.</p> <p>Given a request action that has succeeded:</p> <p>If you retry the request using the same client token and the same parameters, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If you retry the request using the same client token, but one or more of the parameters are different, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Client tokens expire eight hours after a request is made. If you retry the request with the expired token, a new resource is created.</p> <p>If the original resource is deleted and you retry the request, a new resource is created.</p> <p>Idempotent create APIs with a client token:</p> <ul> <li> <p>CreateEnvironmentTemplateVersion</p> </li> <li> <p>CreateServiceTemplateVersion</p> </li> <li> <p>CreateEnvironmentAccountConnection</p> </li> </ul> <p> <b>Idempotent create APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, and the original resource <i>hasn't</i> been modified, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If the original resource has been modified, the retry throws a <code>ConflictException</code>.</p> <p>If you retry with different input parameters, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Idempotent create APIs:</p> <ul> <li> <p>CreateEnvironmentTemplate</p> </li> <li> <p>CreateServiceTemplate</p> </li> <li> <p>CreateEnvironment</p> </li> <li> <p>CreateService</p> </li> </ul> <p> <b>Idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>When you retry the request with an API from this group and the resource was deleted, its metadata is returned in the response.</p> <p>If you retry and the resource doesn't exist, the response is empty.</p> <p>In both cases, the retry succeeds.</p> <p>Idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironmentTemplate</p> </li> <li> <p>DeleteEnvironmentTemplateVersion</p> </li> <li> <p>DeleteServiceTemplate</p> </li> <li> <p>DeleteServiceTemplateVersion</p> </li> <li> <p>DeleteEnvironmentAccountConnection</p> </li> </ul> <p> <b>Asynchronous idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, if the original request delete operation status is <code>DELETE_IN_PROGRESS</code>, the retry returns the resource detail data in the response without performing any further actions.</p> <p>If the original request delete operation is complete, a retry returns an empty response.</p> <p>Asynchronous idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironment</p> </li> <li> <p>DeleteService</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2020-07-20
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.AwsProton);
  }
}(this, function(expect, AwsProton) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AwsProton.DefaultApi();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('DefaultApi', function() {
    describe('acceptEnvironmentAccountConnection', function() {
      it('should call acceptEnvironmentAccountConnection successfully', function(done) {
        //uncomment below and update the code to test acceptEnvironmentAccountConnection
        //instance.acceptEnvironmentAccountConnection(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('cancelComponentDeployment', function() {
      it('should call cancelComponentDeployment successfully', function(done) {
        //uncomment below and update the code to test cancelComponentDeployment
        //instance.cancelComponentDeployment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('cancelEnvironmentDeployment', function() {
      it('should call cancelEnvironmentDeployment successfully', function(done) {
        //uncomment below and update the code to test cancelEnvironmentDeployment
        //instance.cancelEnvironmentDeployment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('cancelServiceInstanceDeployment', function() {
      it('should call cancelServiceInstanceDeployment successfully', function(done) {
        //uncomment below and update the code to test cancelServiceInstanceDeployment
        //instance.cancelServiceInstanceDeployment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('cancelServicePipelineDeployment', function() {
      it('should call cancelServicePipelineDeployment successfully', function(done) {
        //uncomment below and update the code to test cancelServicePipelineDeployment
        //instance.cancelServicePipelineDeployment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createComponent', function() {
      it('should call createComponent successfully', function(done) {
        //uncomment below and update the code to test createComponent
        //instance.createComponent(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createEnvironment', function() {
      it('should call createEnvironment successfully', function(done) {
        //uncomment below and update the code to test createEnvironment
        //instance.createEnvironment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createEnvironmentAccountConnection', function() {
      it('should call createEnvironmentAccountConnection successfully', function(done) {
        //uncomment below and update the code to test createEnvironmentAccountConnection
        //instance.createEnvironmentAccountConnection(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createEnvironmentTemplate', function() {
      it('should call createEnvironmentTemplate successfully', function(done) {
        //uncomment below and update the code to test createEnvironmentTemplate
        //instance.createEnvironmentTemplate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createEnvironmentTemplateVersion', function() {
      it('should call createEnvironmentTemplateVersion successfully', function(done) {
        //uncomment below and update the code to test createEnvironmentTemplateVersion
        //instance.createEnvironmentTemplateVersion(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createRepository', function() {
      it('should call createRepository successfully', function(done) {
        //uncomment below and update the code to test createRepository
        //instance.createRepository(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createService', function() {
      it('should call createService successfully', function(done) {
        //uncomment below and update the code to test createService
        //instance.createService(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createServiceInstance', function() {
      it('should call createServiceInstance successfully', function(done) {
        //uncomment below and update the code to test createServiceInstance
        //instance.createServiceInstance(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createServiceSyncConfig', function() {
      it('should call createServiceSyncConfig successfully', function(done) {
        //uncomment below and update the code to test createServiceSyncConfig
        //instance.createServiceSyncConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createServiceTemplate', function() {
      it('should call createServiceTemplate successfully', function(done) {
        //uncomment below and update the code to test createServiceTemplate
        //instance.createServiceTemplate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createServiceTemplateVersion', function() {
      it('should call createServiceTemplateVersion successfully', function(done) {
        //uncomment below and update the code to test createServiceTemplateVersion
        //instance.createServiceTemplateVersion(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createTemplateSyncConfig', function() {
      it('should call createTemplateSyncConfig successfully', function(done) {
        //uncomment below and update the code to test createTemplateSyncConfig
        //instance.createTemplateSyncConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteComponent', function() {
      it('should call deleteComponent successfully', function(done) {
        //uncomment below and update the code to test deleteComponent
        //instance.deleteComponent(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteDeployment', function() {
      it('should call deleteDeployment successfully', function(done) {
        //uncomment below and update the code to test deleteDeployment
        //instance.deleteDeployment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteEnvironment', function() {
      it('should call deleteEnvironment successfully', function(done) {
        //uncomment below and update the code to test deleteEnvironment
        //instance.deleteEnvironment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteEnvironmentAccountConnection', function() {
      it('should call deleteEnvironmentAccountConnection successfully', function(done) {
        //uncomment below and update the code to test deleteEnvironmentAccountConnection
        //instance.deleteEnvironmentAccountConnection(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteEnvironmentTemplate', function() {
      it('should call deleteEnvironmentTemplate successfully', function(done) {
        //uncomment below and update the code to test deleteEnvironmentTemplate
        //instance.deleteEnvironmentTemplate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteEnvironmentTemplateVersion', function() {
      it('should call deleteEnvironmentTemplateVersion successfully', function(done) {
        //uncomment below and update the code to test deleteEnvironmentTemplateVersion
        //instance.deleteEnvironmentTemplateVersion(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteRepository', function() {
      it('should call deleteRepository successfully', function(done) {
        //uncomment below and update the code to test deleteRepository
        //instance.deleteRepository(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteService', function() {
      it('should call deleteService successfully', function(done) {
        //uncomment below and update the code to test deleteService
        //instance.deleteService(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteServiceSyncConfig', function() {
      it('should call deleteServiceSyncConfig successfully', function(done) {
        //uncomment below and update the code to test deleteServiceSyncConfig
        //instance.deleteServiceSyncConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteServiceTemplate', function() {
      it('should call deleteServiceTemplate successfully', function(done) {
        //uncomment below and update the code to test deleteServiceTemplate
        //instance.deleteServiceTemplate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteServiceTemplateVersion', function() {
      it('should call deleteServiceTemplateVersion successfully', function(done) {
        //uncomment below and update the code to test deleteServiceTemplateVersion
        //instance.deleteServiceTemplateVersion(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteTemplateSyncConfig', function() {
      it('should call deleteTemplateSyncConfig successfully', function(done) {
        //uncomment below and update the code to test deleteTemplateSyncConfig
        //instance.deleteTemplateSyncConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getAccountSettings', function() {
      it('should call getAccountSettings successfully', function(done) {
        //uncomment below and update the code to test getAccountSettings
        //instance.getAccountSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getComponent', function() {
      it('should call getComponent successfully', function(done) {
        //uncomment below and update the code to test getComponent
        //instance.getComponent(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDeployment', function() {
      it('should call getDeployment successfully', function(done) {
        //uncomment below and update the code to test getDeployment
        //instance.getDeployment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getEnvironment', function() {
      it('should call getEnvironment successfully', function(done) {
        //uncomment below and update the code to test getEnvironment
        //instance.getEnvironment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getEnvironmentAccountConnection', function() {
      it('should call getEnvironmentAccountConnection successfully', function(done) {
        //uncomment below and update the code to test getEnvironmentAccountConnection
        //instance.getEnvironmentAccountConnection(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getEnvironmentTemplate', function() {
      it('should call getEnvironmentTemplate successfully', function(done) {
        //uncomment below and update the code to test getEnvironmentTemplate
        //instance.getEnvironmentTemplate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getEnvironmentTemplateVersion', function() {
      it('should call getEnvironmentTemplateVersion successfully', function(done) {
        //uncomment below and update the code to test getEnvironmentTemplateVersion
        //instance.getEnvironmentTemplateVersion(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getRepository', function() {
      it('should call getRepository successfully', function(done) {
        //uncomment below and update the code to test getRepository
        //instance.getRepository(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getRepositorySyncStatus', function() {
      it('should call getRepositorySyncStatus successfully', function(done) {
        //uncomment below and update the code to test getRepositorySyncStatus
        //instance.getRepositorySyncStatus(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getResourcesSummary', function() {
      it('should call getResourcesSummary successfully', function(done) {
        //uncomment below and update the code to test getResourcesSummary
        //instance.getResourcesSummary(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getService', function() {
      it('should call getService successfully', function(done) {
        //uncomment below and update the code to test getService
        //instance.getService(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getServiceInstance', function() {
      it('should call getServiceInstance successfully', function(done) {
        //uncomment below and update the code to test getServiceInstance
        //instance.getServiceInstance(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getServiceInstanceSyncStatus', function() {
      it('should call getServiceInstanceSyncStatus successfully', function(done) {
        //uncomment below and update the code to test getServiceInstanceSyncStatus
        //instance.getServiceInstanceSyncStatus(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getServiceSyncBlockerSummary', function() {
      it('should call getServiceSyncBlockerSummary successfully', function(done) {
        //uncomment below and update the code to test getServiceSyncBlockerSummary
        //instance.getServiceSyncBlockerSummary(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getServiceSyncConfig', function() {
      it('should call getServiceSyncConfig successfully', function(done) {
        //uncomment below and update the code to test getServiceSyncConfig
        //instance.getServiceSyncConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getServiceTemplate', function() {
      it('should call getServiceTemplate successfully', function(done) {
        //uncomment below and update the code to test getServiceTemplate
        //instance.getServiceTemplate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getServiceTemplateVersion', function() {
      it('should call getServiceTemplateVersion successfully', function(done) {
        //uncomment below and update the code to test getServiceTemplateVersion
        //instance.getServiceTemplateVersion(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getTemplateSyncConfig', function() {
      it('should call getTemplateSyncConfig successfully', function(done) {
        //uncomment below and update the code to test getTemplateSyncConfig
        //instance.getTemplateSyncConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getTemplateSyncStatus', function() {
      it('should call getTemplateSyncStatus successfully', function(done) {
        //uncomment below and update the code to test getTemplateSyncStatus
        //instance.getTemplateSyncStatus(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listComponentOutputs', function() {
      it('should call listComponentOutputs successfully', function(done) {
        //uncomment below and update the code to test listComponentOutputs
        //instance.listComponentOutputs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listComponentProvisionedResources', function() {
      it('should call listComponentProvisionedResources successfully', function(done) {
        //uncomment below and update the code to test listComponentProvisionedResources
        //instance.listComponentProvisionedResources(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listComponents', function() {
      it('should call listComponents successfully', function(done) {
        //uncomment below and update the code to test listComponents
        //instance.listComponents(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listDeployments', function() {
      it('should call listDeployments successfully', function(done) {
        //uncomment below and update the code to test listDeployments
        //instance.listDeployments(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listEnvironmentAccountConnections', function() {
      it('should call listEnvironmentAccountConnections successfully', function(done) {
        //uncomment below and update the code to test listEnvironmentAccountConnections
        //instance.listEnvironmentAccountConnections(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listEnvironmentOutputs', function() {
      it('should call listEnvironmentOutputs successfully', function(done) {
        //uncomment below and update the code to test listEnvironmentOutputs
        //instance.listEnvironmentOutputs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listEnvironmentProvisionedResources', function() {
      it('should call listEnvironmentProvisionedResources successfully', function(done) {
        //uncomment below and update the code to test listEnvironmentProvisionedResources
        //instance.listEnvironmentProvisionedResources(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listEnvironmentTemplateVersions', function() {
      it('should call listEnvironmentTemplateVersions successfully', function(done) {
        //uncomment below and update the code to test listEnvironmentTemplateVersions
        //instance.listEnvironmentTemplateVersions(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listEnvironmentTemplates', function() {
      it('should call listEnvironmentTemplates successfully', function(done) {
        //uncomment below and update the code to test listEnvironmentTemplates
        //instance.listEnvironmentTemplates(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listEnvironments', function() {
      it('should call listEnvironments successfully', function(done) {
        //uncomment below and update the code to test listEnvironments
        //instance.listEnvironments(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listRepositories', function() {
      it('should call listRepositories successfully', function(done) {
        //uncomment below and update the code to test listRepositories
        //instance.listRepositories(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listRepositorySyncDefinitions', function() {
      it('should call listRepositorySyncDefinitions successfully', function(done) {
        //uncomment below and update the code to test listRepositorySyncDefinitions
        //instance.listRepositorySyncDefinitions(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listServiceInstanceOutputs', function() {
      it('should call listServiceInstanceOutputs successfully', function(done) {
        //uncomment below and update the code to test listServiceInstanceOutputs
        //instance.listServiceInstanceOutputs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listServiceInstanceProvisionedResources', function() {
      it('should call listServiceInstanceProvisionedResources successfully', function(done) {
        //uncomment below and update the code to test listServiceInstanceProvisionedResources
        //instance.listServiceInstanceProvisionedResources(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listServiceInstances', function() {
      it('should call listServiceInstances successfully', function(done) {
        //uncomment below and update the code to test listServiceInstances
        //instance.listServiceInstances(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listServicePipelineOutputs', function() {
      it('should call listServicePipelineOutputs successfully', function(done) {
        //uncomment below and update the code to test listServicePipelineOutputs
        //instance.listServicePipelineOutputs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listServicePipelineProvisionedResources', function() {
      it('should call listServicePipelineProvisionedResources successfully', function(done) {
        //uncomment below and update the code to test listServicePipelineProvisionedResources
        //instance.listServicePipelineProvisionedResources(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listServiceTemplateVersions', function() {
      it('should call listServiceTemplateVersions successfully', function(done) {
        //uncomment below and update the code to test listServiceTemplateVersions
        //instance.listServiceTemplateVersions(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listServiceTemplates', function() {
      it('should call listServiceTemplates successfully', function(done) {
        //uncomment below and update the code to test listServiceTemplates
        //instance.listServiceTemplates(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listServices', function() {
      it('should call listServices successfully', function(done) {
        //uncomment below and update the code to test listServices
        //instance.listServices(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listTagsForResource', function() {
      it('should call listTagsForResource successfully', function(done) {
        //uncomment below and update the code to test listTagsForResource
        //instance.listTagsForResource(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('notifyResourceDeploymentStatusChange', function() {
      it('should call notifyResourceDeploymentStatusChange successfully', function(done) {
        //uncomment below and update the code to test notifyResourceDeploymentStatusChange
        //instance.notifyResourceDeploymentStatusChange(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('rejectEnvironmentAccountConnection', function() {
      it('should call rejectEnvironmentAccountConnection successfully', function(done) {
        //uncomment below and update the code to test rejectEnvironmentAccountConnection
        //instance.rejectEnvironmentAccountConnection(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('tagResource', function() {
      it('should call tagResource successfully', function(done) {
        //uncomment below and update the code to test tagResource
        //instance.tagResource(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('untagResource', function() {
      it('should call untagResource successfully', function(done) {
        //uncomment below and update the code to test untagResource
        //instance.untagResource(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateAccountSettings', function() {
      it('should call updateAccountSettings successfully', function(done) {
        //uncomment below and update the code to test updateAccountSettings
        //instance.updateAccountSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateComponent', function() {
      it('should call updateComponent successfully', function(done) {
        //uncomment below and update the code to test updateComponent
        //instance.updateComponent(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateEnvironment', function() {
      it('should call updateEnvironment successfully', function(done) {
        //uncomment below and update the code to test updateEnvironment
        //instance.updateEnvironment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateEnvironmentAccountConnection', function() {
      it('should call updateEnvironmentAccountConnection successfully', function(done) {
        //uncomment below and update the code to test updateEnvironmentAccountConnection
        //instance.updateEnvironmentAccountConnection(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateEnvironmentTemplate', function() {
      it('should call updateEnvironmentTemplate successfully', function(done) {
        //uncomment below and update the code to test updateEnvironmentTemplate
        //instance.updateEnvironmentTemplate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateEnvironmentTemplateVersion', function() {
      it('should call updateEnvironmentTemplateVersion successfully', function(done) {
        //uncomment below and update the code to test updateEnvironmentTemplateVersion
        //instance.updateEnvironmentTemplateVersion(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateService', function() {
      it('should call updateService successfully', function(done) {
        //uncomment below and update the code to test updateService
        //instance.updateService(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateServiceInstance', function() {
      it('should call updateServiceInstance successfully', function(done) {
        //uncomment below and update the code to test updateServiceInstance
        //instance.updateServiceInstance(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateServicePipeline', function() {
      it('should call updateServicePipeline successfully', function(done) {
        //uncomment below and update the code to test updateServicePipeline
        //instance.updateServicePipeline(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateServiceSyncBlocker', function() {
      it('should call updateServiceSyncBlocker successfully', function(done) {
        //uncomment below and update the code to test updateServiceSyncBlocker
        //instance.updateServiceSyncBlocker(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateServiceSyncConfig', function() {
      it('should call updateServiceSyncConfig successfully', function(done) {
        //uncomment below and update the code to test updateServiceSyncConfig
        //instance.updateServiceSyncConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateServiceTemplate', function() {
      it('should call updateServiceTemplate successfully', function(done) {
        //uncomment below and update the code to test updateServiceTemplate
        //instance.updateServiceTemplate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateServiceTemplateVersion', function() {
      it('should call updateServiceTemplateVersion successfully', function(done) {
        //uncomment below and update the code to test updateServiceTemplateVersion
        //instance.updateServiceTemplateVersion(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateTemplateSyncConfig', function() {
      it('should call updateTemplateSyncConfig successfully', function(done) {
        //uncomment below and update the code to test updateTemplateSyncConfig
        //instance.updateTemplateSyncConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
