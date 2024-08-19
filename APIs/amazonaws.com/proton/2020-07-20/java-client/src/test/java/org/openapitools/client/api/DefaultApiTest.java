/*
 * AWS Proton
 * <p>This is the Proton Service API Reference. It provides descriptions, syntax and usage examples for each of the <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Operations.html\">actions</a> and <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Types.html\">data types</a> for the Proton service.</p> <p>The documentation for each action shows the Query API request parameters and the XML response.</p> <p>Alternatively, you can use the Amazon Web Services CLI to access an API. For more information, see the <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html\">Amazon Web Services Command Line Interface User Guide</a>.</p> <p>The Proton service is a two-pronged automation framework. Administrators create service templates to provide standardized infrastructure and deployment tooling for serverless and container based applications. Developers, in turn, select from the available service templates to automate their application or service deployments.</p> <p>Because administrators define the infrastructure and tooling that Proton deploys and manages, they need permissions to use all of the listed API operations.</p> <p>When developers select a specific infrastructure and tooling set, Proton deploys their applications. To monitor their applications that are running on Proton, developers need permissions to the service <i>create</i>, <i>list</i>, <i>update</i> and <i>delete</i> API operations and the service instance <i>list</i> and <i>update</i> API operations.</p> <p>To learn more about Proton, see the <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html\">Proton User Guide</a>.</p> <p> <b>Ensuring Idempotency</b> </p> <p>When you make a mutating API request, the request typically returns a result before the asynchronous workflows of the operation are complete. Operations might also time out or encounter other server issues before they're complete, even if the request already returned a result. This might make it difficult to determine whether the request succeeded. Moreover, you might need to retry the request multiple times to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation occurs multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request action completes no more than one time. With an idempotent request, if the original request action completes successfully, any subsequent retries complete successfully without performing any further actions. However, the result might contain updated information, such as the current creation status.</p> <p>The following lists of APIs are grouped according to methods that ensure idempotency.</p> <p> <b>Idempotent create APIs with a client token</b> </p> <p>The API actions in this list support idempotency with the use of a <i>client token</i>. The corresponding Amazon Web Services CLI commands also support idempotency using a client token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request. We recommend that you <i>don't</i> reuse the same client token for other API requests. If you don’t provide a client token for these APIs, a default client token is automatically provided by SDKs.</p> <p>Given a request action that has succeeded:</p> <p>If you retry the request using the same client token and the same parameters, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If you retry the request using the same client token, but one or more of the parameters are different, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Client tokens expire eight hours after a request is made. If you retry the request with the expired token, a new resource is created.</p> <p>If the original resource is deleted and you retry the request, a new resource is created.</p> <p>Idempotent create APIs with a client token:</p> <ul> <li> <p>CreateEnvironmentTemplateVersion</p> </li> <li> <p>CreateServiceTemplateVersion</p> </li> <li> <p>CreateEnvironmentAccountConnection</p> </li> </ul> <p> <b>Idempotent create APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, and the original resource <i>hasn't</i> been modified, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If the original resource has been modified, the retry throws a <code>ConflictException</code>.</p> <p>If you retry with different input parameters, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Idempotent create APIs:</p> <ul> <li> <p>CreateEnvironmentTemplate</p> </li> <li> <p>CreateServiceTemplate</p> </li> <li> <p>CreateEnvironment</p> </li> <li> <p>CreateService</p> </li> </ul> <p> <b>Idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>When you retry the request with an API from this group and the resource was deleted, its metadata is returned in the response.</p> <p>If you retry and the resource doesn't exist, the response is empty.</p> <p>In both cases, the retry succeeds.</p> <p>Idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironmentTemplate</p> </li> <li> <p>DeleteEnvironmentTemplateVersion</p> </li> <li> <p>DeleteServiceTemplate</p> </li> <li> <p>DeleteServiceTemplateVersion</p> </li> <li> <p>DeleteEnvironmentAccountConnection</p> </li> </ul> <p> <b>Asynchronous idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, if the original request delete operation status is <code>DELETE_IN_PROGRESS</code>, the retry returns the resource detail data in the response without performing any further actions.</p> <p>If the original request delete operation is complete, a retry returns an empty response.</p> <p>Asynchronous idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironment</p> </li> <li> <p>DeleteService</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2020-07-20
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.AcceptEnvironmentAccountConnectionInput;
import org.openapitools.client.model.AcceptEnvironmentAccountConnectionOutput;
import org.openapitools.client.model.CancelComponentDeploymentInput;
import org.openapitools.client.model.CancelComponentDeploymentOutput;
import org.openapitools.client.model.CancelEnvironmentDeploymentInput;
import org.openapitools.client.model.CancelEnvironmentDeploymentOutput;
import org.openapitools.client.model.CancelServiceInstanceDeploymentInput;
import org.openapitools.client.model.CancelServiceInstanceDeploymentOutput;
import org.openapitools.client.model.CancelServicePipelineDeploymentInput;
import org.openapitools.client.model.CancelServicePipelineDeploymentOutput;
import org.openapitools.client.model.CreateComponentInput;
import org.openapitools.client.model.CreateComponentOutput;
import org.openapitools.client.model.CreateEnvironmentAccountConnectionInput;
import org.openapitools.client.model.CreateEnvironmentAccountConnectionOutput;
import org.openapitools.client.model.CreateEnvironmentInput;
import org.openapitools.client.model.CreateEnvironmentOutput;
import org.openapitools.client.model.CreateEnvironmentTemplateInput;
import org.openapitools.client.model.CreateEnvironmentTemplateOutput;
import org.openapitools.client.model.CreateEnvironmentTemplateVersionInput;
import org.openapitools.client.model.CreateEnvironmentTemplateVersionOutput;
import org.openapitools.client.model.CreateRepositoryInput;
import org.openapitools.client.model.CreateRepositoryOutput;
import org.openapitools.client.model.CreateServiceInput;
import org.openapitools.client.model.CreateServiceInstanceInput;
import org.openapitools.client.model.CreateServiceInstanceOutput;
import org.openapitools.client.model.CreateServiceOutput;
import org.openapitools.client.model.CreateServiceSyncConfigInput;
import org.openapitools.client.model.CreateServiceSyncConfigOutput;
import org.openapitools.client.model.CreateServiceTemplateInput;
import org.openapitools.client.model.CreateServiceTemplateOutput;
import org.openapitools.client.model.CreateServiceTemplateVersionInput;
import org.openapitools.client.model.CreateServiceTemplateVersionOutput;
import org.openapitools.client.model.CreateTemplateSyncConfigInput;
import org.openapitools.client.model.CreateTemplateSyncConfigOutput;
import org.openapitools.client.model.DeleteComponentInput;
import org.openapitools.client.model.DeleteComponentOutput;
import org.openapitools.client.model.DeleteDeploymentInput;
import org.openapitools.client.model.DeleteDeploymentOutput;
import org.openapitools.client.model.DeleteEnvironmentAccountConnectionInput;
import org.openapitools.client.model.DeleteEnvironmentAccountConnectionOutput;
import org.openapitools.client.model.DeleteEnvironmentInput;
import org.openapitools.client.model.DeleteEnvironmentOutput;
import org.openapitools.client.model.DeleteEnvironmentTemplateInput;
import org.openapitools.client.model.DeleteEnvironmentTemplateOutput;
import org.openapitools.client.model.DeleteEnvironmentTemplateVersionInput;
import org.openapitools.client.model.DeleteEnvironmentTemplateVersionOutput;
import org.openapitools.client.model.DeleteRepositoryInput;
import org.openapitools.client.model.DeleteRepositoryOutput;
import org.openapitools.client.model.DeleteServiceInput;
import org.openapitools.client.model.DeleteServiceOutput;
import org.openapitools.client.model.DeleteServiceSyncConfigInput;
import org.openapitools.client.model.DeleteServiceSyncConfigOutput;
import org.openapitools.client.model.DeleteServiceTemplateInput;
import org.openapitools.client.model.DeleteServiceTemplateOutput;
import org.openapitools.client.model.DeleteServiceTemplateVersionInput;
import org.openapitools.client.model.DeleteServiceTemplateVersionOutput;
import org.openapitools.client.model.DeleteTemplateSyncConfigInput;
import org.openapitools.client.model.DeleteTemplateSyncConfigOutput;
import org.openapitools.client.model.GetAccountSettingsOutput;
import org.openapitools.client.model.GetComponentInput;
import org.openapitools.client.model.GetComponentOutput;
import org.openapitools.client.model.GetDeploymentInput;
import org.openapitools.client.model.GetDeploymentOutput;
import org.openapitools.client.model.GetEnvironmentAccountConnectionInput;
import org.openapitools.client.model.GetEnvironmentAccountConnectionOutput;
import org.openapitools.client.model.GetEnvironmentInput;
import org.openapitools.client.model.GetEnvironmentOutput;
import org.openapitools.client.model.GetEnvironmentTemplateInput;
import org.openapitools.client.model.GetEnvironmentTemplateOutput;
import org.openapitools.client.model.GetEnvironmentTemplateVersionInput;
import org.openapitools.client.model.GetEnvironmentTemplateVersionOutput;
import org.openapitools.client.model.GetRepositoryInput;
import org.openapitools.client.model.GetRepositoryOutput;
import org.openapitools.client.model.GetRepositorySyncStatusInput;
import org.openapitools.client.model.GetRepositorySyncStatusOutput;
import org.openapitools.client.model.GetResourcesSummaryOutput;
import org.openapitools.client.model.GetServiceInput;
import org.openapitools.client.model.GetServiceInstanceInput;
import org.openapitools.client.model.GetServiceInstanceOutput;
import org.openapitools.client.model.GetServiceInstanceSyncStatusInput;
import org.openapitools.client.model.GetServiceInstanceSyncStatusOutput;
import org.openapitools.client.model.GetServiceOutput;
import org.openapitools.client.model.GetServiceSyncBlockerSummaryInput;
import org.openapitools.client.model.GetServiceSyncBlockerSummaryOutput;
import org.openapitools.client.model.GetServiceSyncConfigInput;
import org.openapitools.client.model.GetServiceSyncConfigOutput;
import org.openapitools.client.model.GetServiceTemplateInput;
import org.openapitools.client.model.GetServiceTemplateOutput;
import org.openapitools.client.model.GetServiceTemplateVersionInput;
import org.openapitools.client.model.GetServiceTemplateVersionOutput;
import org.openapitools.client.model.GetTemplateSyncConfigInput;
import org.openapitools.client.model.GetTemplateSyncConfigOutput;
import org.openapitools.client.model.GetTemplateSyncStatusInput;
import org.openapitools.client.model.GetTemplateSyncStatusOutput;
import org.openapitools.client.model.ListComponentOutputsInput;
import org.openapitools.client.model.ListComponentOutputsOutput;
import org.openapitools.client.model.ListComponentProvisionedResourcesInput;
import org.openapitools.client.model.ListComponentProvisionedResourcesOutput;
import org.openapitools.client.model.ListComponentsInput;
import org.openapitools.client.model.ListComponentsOutput;
import org.openapitools.client.model.ListDeploymentsInput;
import org.openapitools.client.model.ListDeploymentsOutput;
import org.openapitools.client.model.ListEnvironmentAccountConnectionsInput;
import org.openapitools.client.model.ListEnvironmentAccountConnectionsOutput;
import org.openapitools.client.model.ListEnvironmentOutputsInput;
import org.openapitools.client.model.ListEnvironmentOutputsOutput;
import org.openapitools.client.model.ListEnvironmentProvisionedResourcesInput;
import org.openapitools.client.model.ListEnvironmentProvisionedResourcesOutput;
import org.openapitools.client.model.ListEnvironmentTemplateVersionsInput;
import org.openapitools.client.model.ListEnvironmentTemplateVersionsOutput;
import org.openapitools.client.model.ListEnvironmentTemplatesInput;
import org.openapitools.client.model.ListEnvironmentTemplatesOutput;
import org.openapitools.client.model.ListEnvironmentsInput;
import org.openapitools.client.model.ListEnvironmentsOutput;
import org.openapitools.client.model.ListRepositoriesInput;
import org.openapitools.client.model.ListRepositoriesOutput;
import org.openapitools.client.model.ListRepositorySyncDefinitionsInput;
import org.openapitools.client.model.ListRepositorySyncDefinitionsOutput;
import org.openapitools.client.model.ListServiceInstanceOutputsInput;
import org.openapitools.client.model.ListServiceInstanceOutputsOutput;
import org.openapitools.client.model.ListServiceInstanceProvisionedResourcesInput;
import org.openapitools.client.model.ListServiceInstanceProvisionedResourcesOutput;
import org.openapitools.client.model.ListServiceInstancesInput;
import org.openapitools.client.model.ListServiceInstancesOutput;
import org.openapitools.client.model.ListServicePipelineOutputsInput;
import org.openapitools.client.model.ListServicePipelineOutputsOutput;
import org.openapitools.client.model.ListServicePipelineProvisionedResourcesInput;
import org.openapitools.client.model.ListServicePipelineProvisionedResourcesOutput;
import org.openapitools.client.model.ListServiceTemplateVersionsInput;
import org.openapitools.client.model.ListServiceTemplateVersionsOutput;
import org.openapitools.client.model.ListServiceTemplatesInput;
import org.openapitools.client.model.ListServiceTemplatesOutput;
import org.openapitools.client.model.ListServicesInput;
import org.openapitools.client.model.ListServicesOutput;
import org.openapitools.client.model.ListTagsForResourceInput;
import org.openapitools.client.model.ListTagsForResourceOutput;
import org.openapitools.client.model.NotifyResourceDeploymentStatusChangeInput;
import org.openapitools.client.model.RejectEnvironmentAccountConnectionInput;
import org.openapitools.client.model.RejectEnvironmentAccountConnectionOutput;
import org.openapitools.client.model.TagResourceInput;
import org.openapitools.client.model.UntagResourceInput;
import org.openapitools.client.model.UpdateAccountSettingsInput;
import org.openapitools.client.model.UpdateAccountSettingsOutput;
import org.openapitools.client.model.UpdateComponentInput;
import org.openapitools.client.model.UpdateComponentOutput;
import org.openapitools.client.model.UpdateEnvironmentAccountConnectionInput;
import org.openapitools.client.model.UpdateEnvironmentAccountConnectionOutput;
import org.openapitools.client.model.UpdateEnvironmentInput;
import org.openapitools.client.model.UpdateEnvironmentOutput;
import org.openapitools.client.model.UpdateEnvironmentTemplateInput;
import org.openapitools.client.model.UpdateEnvironmentTemplateOutput;
import org.openapitools.client.model.UpdateEnvironmentTemplateVersionInput;
import org.openapitools.client.model.UpdateEnvironmentTemplateVersionOutput;
import org.openapitools.client.model.UpdateServiceInput;
import org.openapitools.client.model.UpdateServiceInstanceInput;
import org.openapitools.client.model.UpdateServiceInstanceOutput;
import org.openapitools.client.model.UpdateServiceOutput;
import org.openapitools.client.model.UpdateServicePipelineInput;
import org.openapitools.client.model.UpdateServicePipelineOutput;
import org.openapitools.client.model.UpdateServiceSyncBlockerInput;
import org.openapitools.client.model.UpdateServiceSyncBlockerOutput;
import org.openapitools.client.model.UpdateServiceSyncConfigInput;
import org.openapitools.client.model.UpdateServiceSyncConfigOutput;
import org.openapitools.client.model.UpdateServiceTemplateInput;
import org.openapitools.client.model.UpdateServiceTemplateOutput;
import org.openapitools.client.model.UpdateServiceTemplateVersionInput;
import org.openapitools.client.model.UpdateServiceTemplateVersionOutput;
import org.openapitools.client.model.UpdateTemplateSyncConfigInput;
import org.openapitools.client.model.UpdateTemplateSyncConfigOutput;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * &lt;p&gt;In a management account, an environment account connection request is accepted. When the environment account connection request is accepted, Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\&quot;&gt;Environment account connections&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void acceptEnvironmentAccountConnectionTest() throws ApiException {
        String xAmzTarget = null;
        AcceptEnvironmentAccountConnectionInput acceptEnvironmentAccountConnectionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        AcceptEnvironmentAccountConnectionOutput response = api.acceptEnvironmentAccountConnection(xAmzTarget, acceptEnvironmentAccountConnectionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Attempts to cancel a component deployment (for a component that is in the &lt;code&gt;IN_PROGRESS&lt;/code&gt; deployment status).&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cancelComponentDeploymentTest() throws ApiException {
        String xAmzTarget = null;
        CancelComponentDeploymentInput cancelComponentDeploymentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CancelComponentDeploymentOutput response = api.cancelComponentDeployment(xAmzTarget, cancelComponentDeploymentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Attempts to cancel an environment deployment on an &lt;a&gt;UpdateEnvironment&lt;/a&gt; action, if the deployment is &lt;code&gt;IN_PROGRESS&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-update.html\&quot;&gt;Update an environment&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following list includes potential cancellation scenarios.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the cancellation attempt succeeds, the resulting deployment state is &lt;code&gt;CANCELLED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the cancellation attempt fails, the resulting deployment state is &lt;code&gt;FAILED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the current &lt;a&gt;UpdateEnvironment&lt;/a&gt; action succeeds before the cancellation attempt starts, the resulting deployment state is &lt;code&gt;SUCCEEDED&lt;/code&gt; and the cancellation attempt has no effect.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cancelEnvironmentDeploymentTest() throws ApiException {
        String xAmzTarget = null;
        CancelEnvironmentDeploymentInput cancelEnvironmentDeploymentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CancelEnvironmentDeploymentOutput response = api.cancelEnvironmentDeployment(xAmzTarget, cancelEnvironmentDeploymentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Attempts to cancel a service instance deployment on an &lt;a&gt;UpdateServiceInstance&lt;/a&gt; action, if the deployment is &lt;code&gt;IN_PROGRESS&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-instance-update.html\&quot;&gt;Update a service instance&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following list includes potential cancellation scenarios.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the cancellation attempt succeeds, the resulting deployment state is &lt;code&gt;CANCELLED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the cancellation attempt fails, the resulting deployment state is &lt;code&gt;FAILED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the current &lt;a&gt;UpdateServiceInstance&lt;/a&gt; action succeeds before the cancellation attempt starts, the resulting deployment state is &lt;code&gt;SUCCEEDED&lt;/code&gt; and the cancellation attempt has no effect.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cancelServiceInstanceDeploymentTest() throws ApiException {
        String xAmzTarget = null;
        CancelServiceInstanceDeploymentInput cancelServiceInstanceDeploymentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CancelServiceInstanceDeploymentOutput response = api.cancelServiceInstanceDeployment(xAmzTarget, cancelServiceInstanceDeploymentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Attempts to cancel a service pipeline deployment on an &lt;a&gt;UpdateServicePipeline&lt;/a&gt; action, if the deployment is &lt;code&gt;IN_PROGRESS&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-pipeline-update.html\&quot;&gt;Update a service pipeline&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following list includes potential cancellation scenarios.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the cancellation attempt succeeds, the resulting deployment state is &lt;code&gt;CANCELLED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the cancellation attempt fails, the resulting deployment state is &lt;code&gt;FAILED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the current &lt;a&gt;UpdateServicePipeline&lt;/a&gt; action succeeds before the cancellation attempt starts, the resulting deployment state is &lt;code&gt;SUCCEEDED&lt;/code&gt; and the cancellation attempt has no effect.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cancelServicePipelineDeploymentTest() throws ApiException {
        String xAmzTarget = null;
        CancelServicePipelineDeploymentInput cancelServicePipelineDeploymentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CancelServicePipelineDeploymentOutput response = api.cancelServicePipelineDeployment(xAmzTarget, cancelServicePipelineDeploymentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Create an Proton component. A component is an infrastructure extension for a service instance.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createComponentTest() throws ApiException {
        String xAmzTarget = null;
        CreateComponentInput createComponentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateComponentOutput response = api.createComponent(xAmzTarget, createComponentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Deploy a new environment. An Proton environment is created from an environment template that defines infrastructure and resources that can be shared across services.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;You can provision environments using the following methods:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Amazon Web Services-managed provisioning: Proton makes direct calls to provision your resources.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Self-managed provisioning: Proton makes pull requests on your repository to provide compiled infrastructure as code (IaC) files that your IaC engine uses to provision resources.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html\&quot;&gt;Environments&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html\&quot;&gt;Provisioning methods&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createEnvironmentTest() throws ApiException {
        String xAmzTarget = null;
        CreateEnvironmentInput createEnvironmentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateEnvironmentOutput response = api.createEnvironment(xAmzTarget, createEnvironmentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Create an environment account connection in an environment account so that environment infrastructure resources can be provisioned in the environment account from a management account.&lt;/p&gt; &lt;p&gt;An environment account connection is a secure bi-directional connection between a &lt;i&gt;management account&lt;/i&gt; and an &lt;i&gt;environment account&lt;/i&gt; that maintains authorization and permissions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\&quot;&gt;Environment account connections&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createEnvironmentAccountConnectionTest() throws ApiException {
        String xAmzTarget = null;
        CreateEnvironmentAccountConnectionInput createEnvironmentAccountConnectionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateEnvironmentAccountConnectionOutput response = api.createEnvironmentAccountConnection(xAmzTarget, createEnvironmentAccountConnectionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Create an environment template for Proton. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html\&quot;&gt;Environment Templates&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can create an environment template in one of the two following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Register and publish a &lt;i&gt;standard&lt;/i&gt; environment template that instructs Proton to deploy and manage environment infrastructure.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Register and publish a &lt;i&gt;customer managed&lt;/i&gt; environment template that connects Proton to your existing provisioned infrastructure that you manage. Proton &lt;i&gt;doesn&#39;t&lt;/i&gt; manage your existing provisioned infrastructure. To create an environment template for customer provisioned and managed infrastructure, include the &lt;code&gt;provisioning&lt;/code&gt; parameter and set the value to &lt;code&gt;CUSTOMER_MANAGED&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/template-create.html\&quot;&gt;Register and publish an environment template&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createEnvironmentTemplateTest() throws ApiException {
        String xAmzTarget = null;
        CreateEnvironmentTemplateInput createEnvironmentTemplateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateEnvironmentTemplateOutput response = api.createEnvironmentTemplate(xAmzTarget, createEnvironmentTemplateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Create a new major or minor version of an environment template. A major version of an environment template is a version that &lt;i&gt;isn&#39;t&lt;/i&gt; backwards compatible. A minor version of an environment template is a version that&#39;s backwards compatible within its major version.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createEnvironmentTemplateVersionTest() throws ApiException {
        String xAmzTarget = null;
        CreateEnvironmentTemplateVersionInput createEnvironmentTemplateVersionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateEnvironmentTemplateVersionOutput response = api.createEnvironmentTemplateVersion(xAmzTarget, createEnvironmentTemplateVersionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Create and register a link to a repository. Proton uses the link to repeatedly access the repository, to either push to it (self-managed provisioning) or pull from it (template sync). You can share a linked repository across multiple resources (like environments using self-managed provisioning, or synced templates). When you create a repository link, Proton creates a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/using-service-linked-roles.html\&quot;&gt;service-linked role&lt;/a&gt; for you.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self\&quot;&gt;Self-managed provisioning&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html#ag-template-bundles\&quot;&gt;Template bundles&lt;/a&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html\&quot;&gt;Template sync configurations&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createRepositoryTest() throws ApiException {
        String xAmzTarget = null;
        CreateRepositoryInput createRepositoryInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateRepositoryOutput response = api.createRepository(xAmzTarget, createRepositoryInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Create an Proton service. An Proton service is an instantiation of a service template and often includes several service instances and pipeline. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-services.html\&quot;&gt;Services&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createServiceTest() throws ApiException {
        String xAmzTarget = null;
        CreateServiceInput createServiceInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateServiceOutput response = api.createService(xAmzTarget, createServiceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Create a service instance.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createServiceInstanceTest() throws ApiException {
        String xAmzTarget = null;
        CreateServiceInstanceInput createServiceInstanceInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateServiceInstanceOutput response = api.createServiceInstance(xAmzTarget, createServiceInstanceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Create the Proton Ops configuration file.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createServiceSyncConfigTest() throws ApiException {
        String xAmzTarget = null;
        CreateServiceSyncConfigInput createServiceSyncConfigInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateServiceSyncConfigOutput response = api.createServiceSyncConfig(xAmzTarget, createServiceSyncConfigInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Create a service template. The administrator creates a service template to define standardized infrastructure and an optional CI/CD service pipeline. Developers, in turn, select the service template from Proton. If the selected service template includes a service pipeline definition, they provide a link to their source code repository. Proton then deploys and manages the infrastructure defined by the selected service template. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html\&quot;&gt;Proton templates&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createServiceTemplateTest() throws ApiException {
        String xAmzTarget = null;
        CreateServiceTemplateInput createServiceTemplateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateServiceTemplateOutput response = api.createServiceTemplate(xAmzTarget, createServiceTemplateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Create a new major or minor version of a service template. A major version of a service template is a version that &lt;i&gt;isn&#39;t&lt;/i&gt; backward compatible. A minor version of a service template is a version that&#39;s backward compatible within its major version.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createServiceTemplateVersionTest() throws ApiException {
        String xAmzTarget = null;
        CreateServiceTemplateVersionInput createServiceTemplateVersionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateServiceTemplateVersionOutput response = api.createServiceTemplateVersion(xAmzTarget, createServiceTemplateVersionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Set up a template to create new template versions automatically by tracking a linked repository. A linked repository is a repository that has been registered with Proton. For more information, see &lt;a&gt;CreateRepository&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;When a commit is pushed to your linked repository, Proton checks for changes to your repository template bundles. If it detects a template bundle change, a new major or minor version of its template is created, if the version doesn’t already exist. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html\&quot;&gt;Template sync configurations&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createTemplateSyncConfigTest() throws ApiException {
        String xAmzTarget = null;
        CreateTemplateSyncConfigInput createTemplateSyncConfigInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateTemplateSyncConfigOutput response = api.createTemplateSyncConfig(xAmzTarget, createTemplateSyncConfigInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Delete an Proton component resource.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteComponentTest() throws ApiException {
        String xAmzTarget = null;
        DeleteComponentInput deleteComponentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteComponentOutput response = api.deleteComponent(xAmzTarget, deleteComponentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Delete the deployment.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteDeploymentTest() throws ApiException {
        String xAmzTarget = null;
        DeleteDeploymentInput deleteDeploymentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteDeploymentOutput response = api.deleteDeployment(xAmzTarget, deleteDeploymentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Delete an environment.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteEnvironmentTest() throws ApiException {
        String xAmzTarget = null;
        DeleteEnvironmentInput deleteEnvironmentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteEnvironmentOutput response = api.deleteEnvironment(xAmzTarget, deleteEnvironmentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;In an environment account, delete an environment account connection.&lt;/p&gt; &lt;p&gt;After you delete an environment account connection that’s in use by an Proton environment, Proton &lt;i&gt;can’t&lt;/i&gt; manage the environment infrastructure resources until a new environment account connection is accepted for the environment account and associated environment. You&#39;re responsible for cleaning up provisioned resources that remain without an environment connection.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\&quot;&gt;Environment account connections&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteEnvironmentAccountConnectionTest() throws ApiException {
        String xAmzTarget = null;
        DeleteEnvironmentAccountConnectionInput deleteEnvironmentAccountConnectionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteEnvironmentAccountConnectionOutput response = api.deleteEnvironmentAccountConnection(xAmzTarget, deleteEnvironmentAccountConnectionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * If no other major or minor versions of an environment template exist, delete the environment template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteEnvironmentTemplateTest() throws ApiException {
        String xAmzTarget = null;
        DeleteEnvironmentTemplateInput deleteEnvironmentTemplateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteEnvironmentTemplateOutput response = api.deleteEnvironmentTemplate(xAmzTarget, deleteEnvironmentTemplateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;If no other minor versions of an environment template exist, delete a major version of the environment template if it&#39;s not the &lt;code&gt;Recommended&lt;/code&gt; version. Delete the &lt;code&gt;Recommended&lt;/code&gt; version of the environment template if no other major versions or minor versions of the environment template exist. A major version of an environment template is a version that&#39;s not backward compatible.&lt;/p&gt; &lt;p&gt;Delete a minor version of an environment template if it &lt;i&gt;isn&#39;t&lt;/i&gt; the &lt;code&gt;Recommended&lt;/code&gt; version. Delete a &lt;code&gt;Recommended&lt;/code&gt; minor version of the environment template if no other minor versions of the environment template exist. A minor version of an environment template is a version that&#39;s backward compatible.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteEnvironmentTemplateVersionTest() throws ApiException {
        String xAmzTarget = null;
        DeleteEnvironmentTemplateVersionInput deleteEnvironmentTemplateVersionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteEnvironmentTemplateVersionOutput response = api.deleteEnvironmentTemplateVersion(xAmzTarget, deleteEnvironmentTemplateVersionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * De-register and unlink your repository.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteRepositoryTest() throws ApiException {
        String xAmzTarget = null;
        DeleteRepositoryInput deleteRepositoryInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteRepositoryOutput response = api.deleteRepository(xAmzTarget, deleteRepositoryInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Delete a service, with its instances and pipeline.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t delete a service if it has any service instances that have components attached to them.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteServiceTest() throws ApiException {
        String xAmzTarget = null;
        DeleteServiceInput deleteServiceInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteServiceOutput response = api.deleteService(xAmzTarget, deleteServiceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Delete the Proton Ops file.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteServiceSyncConfigTest() throws ApiException {
        String xAmzTarget = null;
        DeleteServiceSyncConfigInput deleteServiceSyncConfigInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteServiceSyncConfigOutput response = api.deleteServiceSyncConfig(xAmzTarget, deleteServiceSyncConfigInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * If no other major or minor versions of the service template exist, delete the service template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteServiceTemplateTest() throws ApiException {
        String xAmzTarget = null;
        DeleteServiceTemplateInput deleteServiceTemplateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteServiceTemplateOutput response = api.deleteServiceTemplate(xAmzTarget, deleteServiceTemplateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;If no other minor versions of a service template exist, delete a major version of the service template if it&#39;s not the &lt;code&gt;Recommended&lt;/code&gt; version. Delete the &lt;code&gt;Recommended&lt;/code&gt; version of the service template if no other major versions or minor versions of the service template exist. A major version of a service template is a version that &lt;i&gt;isn&#39;t&lt;/i&gt; backwards compatible.&lt;/p&gt; &lt;p&gt;Delete a minor version of a service template if it&#39;s not the &lt;code&gt;Recommended&lt;/code&gt; version. Delete a &lt;code&gt;Recommended&lt;/code&gt; minor version of the service template if no other minor versions of the service template exist. A minor version of a service template is a version that&#39;s backwards compatible.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteServiceTemplateVersionTest() throws ApiException {
        String xAmzTarget = null;
        DeleteServiceTemplateVersionInput deleteServiceTemplateVersionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteServiceTemplateVersionOutput response = api.deleteServiceTemplateVersion(xAmzTarget, deleteServiceTemplateVersionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Delete a template sync configuration.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteTemplateSyncConfigTest() throws ApiException {
        String xAmzTarget = null;
        DeleteTemplateSyncConfigInput deleteTemplateSyncConfigInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteTemplateSyncConfigOutput response = api.deleteTemplateSyncConfig(xAmzTarget, deleteTemplateSyncConfigInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get detail data for Proton account-wide settings.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAccountSettingsTest() throws ApiException {
        String xAmzTarget = null;
        Object body = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetAccountSettingsOutput response = api.getAccountSettings(xAmzTarget, body, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Get detailed data for a component.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getComponentTest() throws ApiException {
        String xAmzTarget = null;
        GetComponentInput getComponentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetComponentOutput response = api.getComponent(xAmzTarget, getComponentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get detailed data for a deployment.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDeploymentTest() throws ApiException {
        String xAmzTarget = null;
        GetDeploymentInput getDeploymentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetDeploymentOutput response = api.getDeployment(xAmzTarget, getDeploymentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get detailed data for an environment.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEnvironmentTest() throws ApiException {
        String xAmzTarget = null;
        GetEnvironmentInput getEnvironmentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetEnvironmentOutput response = api.getEnvironment(xAmzTarget, getEnvironmentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;In an environment account, get the detailed data for an environment account connection.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\&quot;&gt;Environment account connections&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEnvironmentAccountConnectionTest() throws ApiException {
        String xAmzTarget = null;
        GetEnvironmentAccountConnectionInput getEnvironmentAccountConnectionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetEnvironmentAccountConnectionOutput response = api.getEnvironmentAccountConnection(xAmzTarget, getEnvironmentAccountConnectionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get detailed data for an environment template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEnvironmentTemplateTest() throws ApiException {
        String xAmzTarget = null;
        GetEnvironmentTemplateInput getEnvironmentTemplateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetEnvironmentTemplateOutput response = api.getEnvironmentTemplate(xAmzTarget, getEnvironmentTemplateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get detailed data for a major or minor version of an environment template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEnvironmentTemplateVersionTest() throws ApiException {
        String xAmzTarget = null;
        GetEnvironmentTemplateVersionInput getEnvironmentTemplateVersionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetEnvironmentTemplateVersionOutput response = api.getEnvironmentTemplateVersion(xAmzTarget, getEnvironmentTemplateVersionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get detail data for a linked repository.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getRepositoryTest() throws ApiException {
        String xAmzTarget = null;
        GetRepositoryInput getRepositoryInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetRepositoryOutput response = api.getRepository(xAmzTarget, getRepositoryInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Get the sync status of a repository used for Proton template sync. For more information about template sync, see .&lt;/p&gt; &lt;note&gt; &lt;p&gt;A repository sync status isn&#39;t tied to the Proton Repository resource (or any other Proton resource). Therefore, tags on an Proton Repository resource have no effect on this action. Specifically, you can&#39;t use these tags to control access to this action using Attribute-based access control (ABAC).&lt;/p&gt; &lt;p&gt;For more information about ABAC, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags\&quot;&gt;ABAC&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getRepositorySyncStatusTest() throws ApiException {
        String xAmzTarget = null;
        GetRepositorySyncStatusInput getRepositorySyncStatusInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetRepositorySyncStatusOutput response = api.getRepositorySyncStatus(xAmzTarget, getRepositorySyncStatusInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Get counts of Proton resources.&lt;/p&gt; &lt;p&gt;For infrastructure-provisioning resources (environments, services, service instances, pipelines), the action returns staleness counts. A resource is stale when it&#39;s behind the recommended version of the Proton template that it uses and it needs an update to become current.&lt;/p&gt; &lt;p&gt;The action returns staleness counts (counts of resources that are up-to-date, behind a template major version, or behind a template minor version), the total number of resources, and the number of resources that are in a failed state, grouped by resource type. Components, environments, and service templates return less information - see the &lt;code&gt;components&lt;/code&gt;, &lt;code&gt;environments&lt;/code&gt;, and &lt;code&gt;serviceTemplates&lt;/code&gt; field descriptions.&lt;/p&gt; &lt;p&gt;For context, the action also returns the total number of each type of Proton template in the Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/monitoring-dashboard.html\&quot;&gt;Proton dashboard&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getResourcesSummaryTest() throws ApiException {
        String xAmzTarget = null;
        Object body = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetResourcesSummaryOutput response = api.getResourcesSummary(xAmzTarget, body, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get detailed data for a service.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getServiceTest() throws ApiException {
        String xAmzTarget = null;
        GetServiceInput getServiceInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetServiceOutput response = api.getService(xAmzTarget, getServiceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get detailed data for a service instance. A service instance is an instantiation of service template and it runs in a specific environment.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getServiceInstanceTest() throws ApiException {
        String xAmzTarget = null;
        GetServiceInstanceInput getServiceInstanceInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetServiceInstanceOutput response = api.getServiceInstance(xAmzTarget, getServiceInstanceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get the status of the synced service instance.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getServiceInstanceSyncStatusTest() throws ApiException {
        String xAmzTarget = null;
        GetServiceInstanceSyncStatusInput getServiceInstanceSyncStatusInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetServiceInstanceSyncStatusOutput response = api.getServiceInstanceSyncStatus(xAmzTarget, getServiceInstanceSyncStatusInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get detailed data for the service sync blocker summary.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getServiceSyncBlockerSummaryTest() throws ApiException {
        String xAmzTarget = null;
        GetServiceSyncBlockerSummaryInput getServiceSyncBlockerSummaryInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetServiceSyncBlockerSummaryOutput response = api.getServiceSyncBlockerSummary(xAmzTarget, getServiceSyncBlockerSummaryInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get detailed information for the service sync configuration.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getServiceSyncConfigTest() throws ApiException {
        String xAmzTarget = null;
        GetServiceSyncConfigInput getServiceSyncConfigInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetServiceSyncConfigOutput response = api.getServiceSyncConfig(xAmzTarget, getServiceSyncConfigInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get detailed data for a service template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getServiceTemplateTest() throws ApiException {
        String xAmzTarget = null;
        GetServiceTemplateInput getServiceTemplateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetServiceTemplateOutput response = api.getServiceTemplate(xAmzTarget, getServiceTemplateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get detailed data for a major or minor version of a service template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getServiceTemplateVersionTest() throws ApiException {
        String xAmzTarget = null;
        GetServiceTemplateVersionInput getServiceTemplateVersionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetServiceTemplateVersionOutput response = api.getServiceTemplateVersion(xAmzTarget, getServiceTemplateVersionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get detail data for a template sync configuration.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTemplateSyncConfigTest() throws ApiException {
        String xAmzTarget = null;
        GetTemplateSyncConfigInput getTemplateSyncConfigInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetTemplateSyncConfigOutput response = api.getTemplateSyncConfig(xAmzTarget, getTemplateSyncConfigInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Get the status of a template sync.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTemplateSyncStatusTest() throws ApiException {
        String xAmzTarget = null;
        GetTemplateSyncStatusInput getTemplateSyncStatusInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetTemplateSyncStatusOutput response = api.getTemplateSyncStatus(xAmzTarget, getTemplateSyncStatusInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Get a list of component Infrastructure as Code (IaC) outputs.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listComponentOutputsTest() throws ApiException {
        String xAmzTarget = null;
        ListComponentOutputsInput listComponentOutputsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String nextToken = null;
        ListComponentOutputsOutput response = api.listComponentOutputs(xAmzTarget, listComponentOutputsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;List provisioned resources for a component with details.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listComponentProvisionedResourcesTest() throws ApiException {
        String xAmzTarget = null;
        ListComponentProvisionedResourcesInput listComponentProvisionedResourcesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String nextToken = null;
        ListComponentProvisionedResourcesOutput response = api.listComponentProvisionedResources(xAmzTarget, listComponentProvisionedResourcesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;List components with summary data. You can filter the result list by environment, service, or a single service instance.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listComponentsTest() throws ApiException {
        String xAmzTarget = null;
        ListComponentsInput listComponentsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListComponentsOutput response = api.listComponents(xAmzTarget, listComponentsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * List deployments. You can filter the result list by environment, service, or a single service instance.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listDeploymentsTest() throws ApiException {
        String xAmzTarget = null;
        ListDeploymentsInput listDeploymentsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListDeploymentsOutput response = api.listDeployments(xAmzTarget, listDeploymentsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;View a list of environment account connections.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\&quot;&gt;Environment account connections&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listEnvironmentAccountConnectionsTest() throws ApiException {
        String xAmzTarget = null;
        ListEnvironmentAccountConnectionsInput listEnvironmentAccountConnectionsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListEnvironmentAccountConnectionsOutput response = api.listEnvironmentAccountConnections(xAmzTarget, listEnvironmentAccountConnectionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * List the infrastructure as code outputs for your environment.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listEnvironmentOutputsTest() throws ApiException {
        String xAmzTarget = null;
        ListEnvironmentOutputsInput listEnvironmentOutputsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String nextToken = null;
        ListEnvironmentOutputsOutput response = api.listEnvironmentOutputs(xAmzTarget, listEnvironmentOutputsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken);
        // TODO: test validations
    }

    /**
     * List the provisioned resources for your environment.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listEnvironmentProvisionedResourcesTest() throws ApiException {
        String xAmzTarget = null;
        ListEnvironmentProvisionedResourcesInput listEnvironmentProvisionedResourcesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String nextToken = null;
        ListEnvironmentProvisionedResourcesOutput response = api.listEnvironmentProvisionedResources(xAmzTarget, listEnvironmentProvisionedResourcesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken);
        // TODO: test validations
    }

    /**
     * List major or minor versions of an environment template with detail data.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listEnvironmentTemplateVersionsTest() throws ApiException {
        String xAmzTarget = null;
        ListEnvironmentTemplateVersionsInput listEnvironmentTemplateVersionsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListEnvironmentTemplateVersionsOutput response = api.listEnvironmentTemplateVersions(xAmzTarget, listEnvironmentTemplateVersionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * List environment templates.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listEnvironmentTemplatesTest() throws ApiException {
        String xAmzTarget = null;
        ListEnvironmentTemplatesInput listEnvironmentTemplatesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListEnvironmentTemplatesOutput response = api.listEnvironmentTemplates(xAmzTarget, listEnvironmentTemplatesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * List environments with detail data summaries.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listEnvironmentsTest() throws ApiException {
        String xAmzTarget = null;
        ListEnvironmentsInput listEnvironmentsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListEnvironmentsOutput response = api.listEnvironments(xAmzTarget, listEnvironmentsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * List linked repositories with detail data.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listRepositoriesTest() throws ApiException {
        String xAmzTarget = null;
        ListRepositoriesInput listRepositoriesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListRepositoriesOutput response = api.listRepositories(xAmzTarget, listRepositoriesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * List repository sync definitions with detail data.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listRepositorySyncDefinitionsTest() throws ApiException {
        String xAmzTarget = null;
        ListRepositorySyncDefinitionsInput listRepositorySyncDefinitionsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String nextToken = null;
        ListRepositorySyncDefinitionsOutput response = api.listRepositorySyncDefinitions(xAmzTarget, listRepositorySyncDefinitionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken);
        // TODO: test validations
    }

    /**
     * Get a list service of instance Infrastructure as Code (IaC) outputs.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listServiceInstanceOutputsTest() throws ApiException {
        String xAmzTarget = null;
        ListServiceInstanceOutputsInput listServiceInstanceOutputsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String nextToken = null;
        ListServiceInstanceOutputsOutput response = api.listServiceInstanceOutputs(xAmzTarget, listServiceInstanceOutputsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken);
        // TODO: test validations
    }

    /**
     * List provisioned resources for a service instance with details.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listServiceInstanceProvisionedResourcesTest() throws ApiException {
        String xAmzTarget = null;
        ListServiceInstanceProvisionedResourcesInput listServiceInstanceProvisionedResourcesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String nextToken = null;
        ListServiceInstanceProvisionedResourcesOutput response = api.listServiceInstanceProvisionedResources(xAmzTarget, listServiceInstanceProvisionedResourcesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken);
        // TODO: test validations
    }

    /**
     * List service instances with summary data. This action lists service instances of all services in the Amazon Web Services account.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listServiceInstancesTest() throws ApiException {
        String xAmzTarget = null;
        ListServiceInstancesInput listServiceInstancesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListServiceInstancesOutput response = api.listServiceInstances(xAmzTarget, listServiceInstancesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Get a list of service pipeline Infrastructure as Code (IaC) outputs.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listServicePipelineOutputsTest() throws ApiException {
        String xAmzTarget = null;
        ListServicePipelineOutputsInput listServicePipelineOutputsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String nextToken = null;
        ListServicePipelineOutputsOutput response = api.listServicePipelineOutputs(xAmzTarget, listServicePipelineOutputsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken);
        // TODO: test validations
    }

    /**
     * List provisioned resources for a service and pipeline with details.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listServicePipelineProvisionedResourcesTest() throws ApiException {
        String xAmzTarget = null;
        ListServicePipelineProvisionedResourcesInput listServicePipelineProvisionedResourcesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String nextToken = null;
        ListServicePipelineProvisionedResourcesOutput response = api.listServicePipelineProvisionedResources(xAmzTarget, listServicePipelineProvisionedResourcesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken);
        // TODO: test validations
    }

    /**
     * List major or minor versions of a service template with detail data.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listServiceTemplateVersionsTest() throws ApiException {
        String xAmzTarget = null;
        ListServiceTemplateVersionsInput listServiceTemplateVersionsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListServiceTemplateVersionsOutput response = api.listServiceTemplateVersions(xAmzTarget, listServiceTemplateVersionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * List service templates with detail data.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listServiceTemplatesTest() throws ApiException {
        String xAmzTarget = null;
        ListServiceTemplatesInput listServiceTemplatesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListServiceTemplatesOutput response = api.listServiceTemplates(xAmzTarget, listServiceTemplatesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * List services with summaries of detail data.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listServicesTest() throws ApiException {
        String xAmzTarget = null;
        ListServicesInput listServicesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListServicesOutput response = api.listServices(xAmzTarget, listServicesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * List tags for a resource. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/resources.html\&quot;&gt;Proton resources and tagging&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listTagsForResourceTest() throws ApiException {
        String xAmzTarget = null;
        ListTagsForResourceInput listTagsForResourceInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListTagsForResourceOutput response = api.listTagsForResource(xAmzTarget, listTagsForResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Notify Proton of status changes to a provisioned resource when you use self-managed provisioning.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self\&quot;&gt;Self-managed provisioning&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void notifyResourceDeploymentStatusChangeTest() throws ApiException {
        String xAmzTarget = null;
        NotifyResourceDeploymentStatusChangeInput notifyResourceDeploymentStatusChangeInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.notifyResourceDeploymentStatusChange(xAmzTarget, notifyResourceDeploymentStatusChangeInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;In a management account, reject an environment account connection from another environment account.&lt;/p&gt; &lt;p&gt;After you reject an environment account connection request, you &lt;i&gt;can&#39;t&lt;/i&gt; accept or use the rejected environment account connection.&lt;/p&gt; &lt;p&gt;You &lt;i&gt;can’t&lt;/i&gt; reject an environment account connection that&#39;s connected to an environment.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\&quot;&gt;Environment account connections&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void rejectEnvironmentAccountConnectionTest() throws ApiException {
        String xAmzTarget = null;
        RejectEnvironmentAccountConnectionInput rejectEnvironmentAccountConnectionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        RejectEnvironmentAccountConnectionOutput response = api.rejectEnvironmentAccountConnection(xAmzTarget, rejectEnvironmentAccountConnectionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Tag a resource. A tag is a key-value pair of metadata that you associate with an Proton resource.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/resources.html\&quot;&gt;Proton resources and tagging&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void tagResourceTest() throws ApiException {
        String xAmzTarget = null;
        TagResourceInput tagResourceInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.tagResource(xAmzTarget, tagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Remove a customer tag from a resource. A tag is a key-value pair of metadata associated with an Proton resource.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/resources.html\&quot;&gt;Proton resources and tagging&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void untagResourceTest() throws ApiException {
        String xAmzTarget = null;
        UntagResourceInput untagResourceInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.untagResource(xAmzTarget, untagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Update Proton settings that are used for multiple services in the Amazon Web Services account.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateAccountSettingsTest() throws ApiException {
        String xAmzTarget = null;
        UpdateAccountSettingsInput updateAccountSettingsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateAccountSettingsOutput response = api.updateAccountSettings(xAmzTarget, updateAccountSettingsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Update a component.&lt;/p&gt; &lt;p&gt;There are a few modes for updating a component. The &lt;code&gt;deploymentType&lt;/code&gt; field defines the mode.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t update a component while its deployment status, or the deployment status of a service instance attached to it, is &lt;code&gt;IN_PROGRESS&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateComponentTest() throws ApiException {
        String xAmzTarget = null;
        UpdateComponentInput updateComponentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateComponentOutput response = api.updateComponent(xAmzTarget, updateComponentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Update an environment.&lt;/p&gt; &lt;p&gt;If the environment is associated with an environment account connection, &lt;i&gt;don&#39;t&lt;/i&gt; update or include the &lt;code&gt;protonServiceRoleArn&lt;/code&gt; and &lt;code&gt;provisioningRepository&lt;/code&gt; parameter to update or connect to an environment account connection.&lt;/p&gt; &lt;p&gt;You can only update to a new environment account connection if that connection was created in the same environment account that the current environment account connection was created in. The account connection must also be associated with the current environment.&lt;/p&gt; &lt;p&gt;If the environment &lt;i&gt;isn&#39;t&lt;/i&gt; associated with an environment account connection, &lt;i&gt;don&#39;t&lt;/i&gt; update or include the &lt;code&gt;environmentAccountConnectionId&lt;/code&gt; parameter. You &lt;i&gt;can&#39;t&lt;/i&gt; update or connect the environment to an environment account connection if it &lt;i&gt;isn&#39;t&lt;/i&gt; already associated with an environment connection.&lt;/p&gt; &lt;p&gt;You can update either the &lt;code&gt;environmentAccountConnectionId&lt;/code&gt; or &lt;code&gt;protonServiceRoleArn&lt;/code&gt; parameter and value. You can’t update both.&lt;/p&gt; &lt;p&gt;If the environment was configured for Amazon Web Services-managed provisioning, omit the &lt;code&gt;provisioningRepository&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;If the environment was configured for self-managed provisioning, specify the &lt;code&gt;provisioningRepository&lt;/code&gt; parameter and omit the &lt;code&gt;protonServiceRoleArn&lt;/code&gt; and &lt;code&gt;environmentAccountConnectionId&lt;/code&gt; parameters.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html\&quot;&gt;Environments&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html\&quot;&gt;Provisioning methods&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;There are four modes for updating an environment. The &lt;code&gt;deploymentType&lt;/code&gt; field defines the mode.&lt;/p&gt; &lt;dl&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;NONE&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, a deployment &lt;i&gt;doesn&#39;t&lt;/i&gt; occur. Only the requested metadata parameters are updated.&lt;/p&gt; &lt;/dd&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;CURRENT_VERSION&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, the environment is deployed and updated with the new spec that you provide. Only requested parameters are updated. &lt;i&gt;Don’t&lt;/i&gt; include minor or major version parameters when you use this &lt;code&gt;deployment-type&lt;/code&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;MINOR_VERSION&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, the environment is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.&lt;/p&gt; &lt;/dd&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;MAJOR_VERSION&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, the environment is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can also specify a different major version that&#39;s higher than the major version in use and a minor version.&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateEnvironmentTest() throws ApiException {
        String xAmzTarget = null;
        UpdateEnvironmentInput updateEnvironmentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateEnvironmentOutput response = api.updateEnvironment(xAmzTarget, updateEnvironmentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;In an environment account, update an environment account connection to use a new IAM role.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\&quot;&gt;Environment account connections&lt;/a&gt; in the &lt;i&gt;Proton User guide&lt;/i&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateEnvironmentAccountConnectionTest() throws ApiException {
        String xAmzTarget = null;
        UpdateEnvironmentAccountConnectionInput updateEnvironmentAccountConnectionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateEnvironmentAccountConnectionOutput response = api.updateEnvironmentAccountConnection(xAmzTarget, updateEnvironmentAccountConnectionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Update an environment template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateEnvironmentTemplateTest() throws ApiException {
        String xAmzTarget = null;
        UpdateEnvironmentTemplateInput updateEnvironmentTemplateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateEnvironmentTemplateOutput response = api.updateEnvironmentTemplate(xAmzTarget, updateEnvironmentTemplateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Update a major or minor version of an environment template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateEnvironmentTemplateVersionTest() throws ApiException {
        String xAmzTarget = null;
        UpdateEnvironmentTemplateVersionInput updateEnvironmentTemplateVersionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateEnvironmentTemplateVersionOutput response = api.updateEnvironmentTemplateVersion(xAmzTarget, updateEnvironmentTemplateVersionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Edit a service description or use a spec to add and delete service instances.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Existing service instances and the service pipeline &lt;i&gt;can&#39;t&lt;/i&gt; be edited using this API. They can only be deleted.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Use the &lt;code&gt;description&lt;/code&gt; parameter to modify the description.&lt;/p&gt; &lt;p&gt;Edit the &lt;code&gt;spec&lt;/code&gt; parameter to add or delete instances.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t delete a service instance (remove it from the spec) if it has an attached component.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateServiceTest() throws ApiException {
        String xAmzTarget = null;
        UpdateServiceInput updateServiceInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateServiceOutput response = api.updateService(xAmzTarget, updateServiceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Update a service instance.&lt;/p&gt; &lt;p&gt;There are a few modes for updating a service instance. The &lt;code&gt;deploymentType&lt;/code&gt; field defines the mode.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t update a service instance while its deployment status, or the deployment status of a component attached to it, is &lt;code&gt;IN_PROGRESS&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateServiceInstanceTest() throws ApiException {
        String xAmzTarget = null;
        UpdateServiceInstanceInput updateServiceInstanceInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateServiceInstanceOutput response = api.updateServiceInstance(xAmzTarget, updateServiceInstanceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Update the service pipeline.&lt;/p&gt; &lt;p&gt;There are four modes for updating a service pipeline. The &lt;code&gt;deploymentType&lt;/code&gt; field defines the mode.&lt;/p&gt; &lt;dl&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;NONE&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, a deployment &lt;i&gt;doesn&#39;t&lt;/i&gt; occur. Only the requested metadata parameters are updated.&lt;/p&gt; &lt;/dd&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;CURRENT_VERSION&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. &lt;i&gt;Don’t&lt;/i&gt; include major or minor version parameters when you use this &lt;code&gt;deployment-type&lt;/code&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;MINOR_VERSION&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.&lt;/p&gt; &lt;/dd&gt; &lt;dt/&gt; &lt;dd&gt; &lt;p&gt; &lt;code&gt;MAJOR_VERSION&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template by default. You can specify a different major version that&#39;s higher than the major version in use and a minor version.&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateServicePipelineTest() throws ApiException {
        String xAmzTarget = null;
        UpdateServicePipelineInput updateServicePipelineInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateServicePipelineOutput response = api.updateServicePipeline(xAmzTarget, updateServicePipelineInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Update the service sync blocker by resolving it.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateServiceSyncBlockerTest() throws ApiException {
        String xAmzTarget = null;
        UpdateServiceSyncBlockerInput updateServiceSyncBlockerInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateServiceSyncBlockerOutput response = api.updateServiceSyncBlocker(xAmzTarget, updateServiceSyncBlockerInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Update the Proton Ops config file.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateServiceSyncConfigTest() throws ApiException {
        String xAmzTarget = null;
        UpdateServiceSyncConfigInput updateServiceSyncConfigInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateServiceSyncConfigOutput response = api.updateServiceSyncConfig(xAmzTarget, updateServiceSyncConfigInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Update a service template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateServiceTemplateTest() throws ApiException {
        String xAmzTarget = null;
        UpdateServiceTemplateInput updateServiceTemplateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateServiceTemplateOutput response = api.updateServiceTemplate(xAmzTarget, updateServiceTemplateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Update a major or minor version of a service template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateServiceTemplateVersionTest() throws ApiException {
        String xAmzTarget = null;
        UpdateServiceTemplateVersionInput updateServiceTemplateVersionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateServiceTemplateVersionOutput response = api.updateServiceTemplateVersion(xAmzTarget, updateServiceTemplateVersionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Update template sync configuration parameters, except for the &lt;code&gt;templateName&lt;/code&gt; and &lt;code&gt;templateType&lt;/code&gt;. Repository details (branch, name, and provider) should be of a linked repository. A linked repository is a repository that has been registered with Proton. For more information, see &lt;a&gt;CreateRepository&lt;/a&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateTemplateSyncConfigTest() throws ApiException {
        String xAmzTarget = null;
        UpdateTemplateSyncConfigInput updateTemplateSyncConfigInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateTemplateSyncConfigOutput response = api.updateTemplateSyncConfig(xAmzTarget, updateTemplateSyncConfigInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

}
