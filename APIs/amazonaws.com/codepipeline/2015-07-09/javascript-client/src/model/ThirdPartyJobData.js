/**
 * AWS CodePipeline
 * <fullname>CodePipeline</fullname> <p> <b>Overview</b> </p> <p>This is the CodePipeline API Reference. This guide provides descriptions of the actions and data types for CodePipeline. Some functionality for your pipeline can only be configured through the API. For more information, see the <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html\">CodePipeline User Guide</a>.</p> <p>You can use the CodePipeline API to work with pipelines, stages, actions, and transitions.</p> <p> <i>Pipelines</i> are models of automated release processes. Each pipeline is uniquely named, and consists of stages, actions, and transitions. </p> <p>You can work with pipelines by calling:</p> <ul> <li> <p> <a>CreatePipeline</a>, which creates a uniquely named pipeline.</p> </li> <li> <p> <a>DeletePipeline</a>, which deletes the specified pipeline.</p> </li> <li> <p> <a>GetPipeline</a>, which returns information about the pipeline structure and pipeline metadata, including the pipeline Amazon Resource Name (ARN).</p> </li> <li> <p> <a>GetPipelineExecution</a>, which returns information about a specific execution of a pipeline.</p> </li> <li> <p> <a>GetPipelineState</a>, which returns information about the current state of the stages and actions of a pipeline.</p> </li> <li> <p> <a>ListActionExecutions</a>, which returns action-level details for past executions. The details include full stage and action-level details, including individual action duration, status, any errors that occurred during the execution, and input and output artifact location details.</p> </li> <li> <p> <a>ListPipelines</a>, which gets a summary of all of the pipelines associated with your account.</p> </li> <li> <p> <a>ListPipelineExecutions</a>, which gets a summary of the most recent executions for a pipeline.</p> </li> <li> <p> <a>StartPipelineExecution</a>, which runs the most recent revision of an artifact through the pipeline.</p> </li> <li> <p> <a>StopPipelineExecution</a>, which stops the specified pipeline execution from continuing through the pipeline.</p> </li> <li> <p> <a>UpdatePipeline</a>, which updates a pipeline with edits or changes to the structure of the pipeline.</p> </li> </ul> <p>Pipelines include <i>stages</i>. Each stage contains one or more actions that must complete before the next stage begins. A stage results in success or failure. If a stage fails, the pipeline stops at that stage and remains stopped until either a new version of an artifact appears in the source location, or a user takes action to rerun the most recent artifact through the pipeline. You can call <a>GetPipelineState</a>, which displays the status of a pipeline, including the status of stages in the pipeline, or <a>GetPipeline</a>, which returns the entire structure of the pipeline, including the stages of that pipeline. For more information about the structure of stages and actions, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-structure.html\">CodePipeline Pipeline Structure Reference</a>.</p> <p>Pipeline stages include <i>actions</i> that are categorized into categories such as source or build actions performed in a stage of a pipeline. For example, you can use a source action to import artifacts into a pipeline from a source such as Amazon S3. Like stages, you do not work with actions directly in most cases, but you do define and interact with actions when working with pipeline operations such as <a>CreatePipeline</a> and <a>GetPipelineState</a>. Valid action categories are:</p> <ul> <li> <p>Source</p> </li> <li> <p>Build</p> </li> <li> <p>Test</p> </li> <li> <p>Deploy</p> </li> <li> <p>Approval</p> </li> <li> <p>Invoke</p> </li> </ul> <p>Pipelines also include <i>transitions</i>, which allow the transition of artifacts from one stage to the next in a pipeline after the actions in one stage complete.</p> <p>You can work with transitions by calling:</p> <ul> <li> <p> <a>DisableStageTransition</a>, which prevents artifacts from transitioning to the next stage in a pipeline.</p> </li> <li> <p> <a>EnableStageTransition</a>, which enables transition of artifacts between stages in a pipeline. </p> </li> </ul> <p> <b>Using the API to integrate with CodePipeline</b> </p> <p>For third-party integrators or developers who want to create their own integrations with CodePipeline, the expected sequence varies from the standard API user. To integrate with CodePipeline, developers need to work with the following items:</p> <p> <b>Jobs</b>, which are instances of an action. For example, a job for a source action might import a revision of an artifact from a source. </p> <p>You can work with jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetJobDetails</a>, which returns the details of a job.</p> </li> <li> <p> <a>PollForJobs</a>, which determines whether there are any jobs to act on.</p> </li> <li> <p> <a>PutJobFailureResult</a>, which provides details of a job failure. </p> </li> <li> <p> <a>PutJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul> <p> <b>Third party jobs</b>, which are instances of an action created by a partner action and integrated into CodePipeline. Partner actions are created by members of the Amazon Web Services Partner Network.</p> <p>You can work with third party jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeThirdPartyJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetThirdPartyJobDetails</a>, which requests the details of a job for a partner action.</p> </li> <li> <p> <a>PollForThirdPartyJobs</a>, which determines whether there are any jobs to act on. </p> </li> <li> <p> <a>PutThirdPartyJobFailureResult</a>, which provides details of a job failure.</p> </li> <li> <p> <a>PutThirdPartyJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2015-07-09
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import JobDataActionConfiguration from './JobDataActionConfiguration';
import PollForJobsInputActionTypeId from './PollForJobsInputActionTypeId';
import ThirdPartyJobDataArtifactCredentials from './ThirdPartyJobDataArtifactCredentials';
import ThirdPartyJobDataEncryptionKey from './ThirdPartyJobDataEncryptionKey';
import ThirdPartyJobDataPipelineContext from './ThirdPartyJobDataPipelineContext';

/**
 * The ThirdPartyJobData model module.
 * @module model/ThirdPartyJobData
 * @version 2015-07-09
 */
class ThirdPartyJobData {
    /**
     * Constructs a new <code>ThirdPartyJobData</code>.
     * Represents information about the job data for a partner action.
     * @alias module:model/ThirdPartyJobData
     */
    constructor() { 
        
        ThirdPartyJobData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ThirdPartyJobData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ThirdPartyJobData} obj Optional instance to populate.
     * @return {module:model/ThirdPartyJobData} The populated <code>ThirdPartyJobData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ThirdPartyJobData();

            if (data.hasOwnProperty('actionTypeId')) {
                obj['actionTypeId'] = PollForJobsInputActionTypeId.constructFromObject(data['actionTypeId']);
            }
            if (data.hasOwnProperty('actionConfiguration')) {
                obj['actionConfiguration'] = JobDataActionConfiguration.constructFromObject(data['actionConfiguration']);
            }
            if (data.hasOwnProperty('pipelineContext')) {
                obj['pipelineContext'] = ThirdPartyJobDataPipelineContext.constructFromObject(data['pipelineContext']);
            }
            if (data.hasOwnProperty('inputArtifacts')) {
                obj['inputArtifacts'] = ApiClient.convertToType(data['inputArtifacts'], Array);
            }
            if (data.hasOwnProperty('outputArtifacts')) {
                obj['outputArtifacts'] = ApiClient.convertToType(data['outputArtifacts'], Array);
            }
            if (data.hasOwnProperty('artifactCredentials')) {
                obj['artifactCredentials'] = ThirdPartyJobDataArtifactCredentials.constructFromObject(data['artifactCredentials']);
            }
            if (data.hasOwnProperty('continuationToken')) {
                obj['continuationToken'] = ApiClient.convertToType(data['continuationToken'], 'String');
            }
            if (data.hasOwnProperty('encryptionKey')) {
                obj['encryptionKey'] = ThirdPartyJobDataEncryptionKey.constructFromObject(data['encryptionKey']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ThirdPartyJobData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ThirdPartyJobData</code>.
     */
    static validateJSON(data) {
        // validate the optional field `actionTypeId`
        if (data['actionTypeId']) { // data not null
          PollForJobsInputActionTypeId.validateJSON(data['actionTypeId']);
        }
        // validate the optional field `actionConfiguration`
        if (data['actionConfiguration']) { // data not null
          JobDataActionConfiguration.validateJSON(data['actionConfiguration']);
        }
        // validate the optional field `pipelineContext`
        if (data['pipelineContext']) { // data not null
          ThirdPartyJobDataPipelineContext.validateJSON(data['pipelineContext']);
        }
        // validate the optional field `inputArtifacts`
        if (data['inputArtifacts']) { // data not null
          Array.validateJSON(data['inputArtifacts']);
        }
        // validate the optional field `outputArtifacts`
        if (data['outputArtifacts']) { // data not null
          Array.validateJSON(data['outputArtifacts']);
        }
        // validate the optional field `artifactCredentials`
        if (data['artifactCredentials']) { // data not null
          ThirdPartyJobDataArtifactCredentials.validateJSON(data['artifactCredentials']);
        }
        // validate the optional field `continuationToken`
        if (data['continuationToken']) { // data not null
          String.validateJSON(data['continuationToken']);
        }
        // validate the optional field `encryptionKey`
        if (data['encryptionKey']) { // data not null
          ThirdPartyJobDataEncryptionKey.validateJSON(data['encryptionKey']);
        }

        return true;
    }


}



/**
 * @member {module:model/PollForJobsInputActionTypeId} actionTypeId
 */
ThirdPartyJobData.prototype['actionTypeId'] = undefined;

/**
 * @member {module:model/JobDataActionConfiguration} actionConfiguration
 */
ThirdPartyJobData.prototype['actionConfiguration'] = undefined;

/**
 * @member {module:model/ThirdPartyJobDataPipelineContext} pipelineContext
 */
ThirdPartyJobData.prototype['pipelineContext'] = undefined;

/**
 * @member {Array} inputArtifacts
 */
ThirdPartyJobData.prototype['inputArtifacts'] = undefined;

/**
 * @member {Array} outputArtifacts
 */
ThirdPartyJobData.prototype['outputArtifacts'] = undefined;

/**
 * @member {module:model/ThirdPartyJobDataArtifactCredentials} artifactCredentials
 */
ThirdPartyJobData.prototype['artifactCredentials'] = undefined;

/**
 * @member {String} continuationToken
 */
ThirdPartyJobData.prototype['continuationToken'] = undefined;

/**
 * @member {module:model/ThirdPartyJobDataEncryptionKey} encryptionKey
 */
ThirdPartyJobData.prototype['encryptionKey'] = undefined;






export default ThirdPartyJobData;

