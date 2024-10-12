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
import ActionExecutionDetailInput from './ActionExecutionDetailInput';
import ActionExecutionDetailOutput from './ActionExecutionDetailOutput';
import ActionExecutionStatus from './ActionExecutionStatus';

/**
 * The ActionExecutionDetail model module.
 * @module model/ActionExecutionDetail
 * @version 2015-07-09
 */
class ActionExecutionDetail {
    /**
     * Constructs a new <code>ActionExecutionDetail</code>.
     * Returns information about an execution of an action, including the action execution ID, and the name, version, and timing of the action. 
     * @alias module:model/ActionExecutionDetail
     */
    constructor() { 
        
        ActionExecutionDetail.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ActionExecutionDetail</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ActionExecutionDetail} obj Optional instance to populate.
     * @return {module:model/ActionExecutionDetail} The populated <code>ActionExecutionDetail</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ActionExecutionDetail();

            if (data.hasOwnProperty('pipelineExecutionId')) {
                obj['pipelineExecutionId'] = ApiClient.convertToType(data['pipelineExecutionId'], 'String');
            }
            if (data.hasOwnProperty('actionExecutionId')) {
                obj['actionExecutionId'] = ApiClient.convertToType(data['actionExecutionId'], 'String');
            }
            if (data.hasOwnProperty('pipelineVersion')) {
                obj['pipelineVersion'] = ApiClient.convertToType(data['pipelineVersion'], 'Number');
            }
            if (data.hasOwnProperty('stageName')) {
                obj['stageName'] = ApiClient.convertToType(data['stageName'], 'String');
            }
            if (data.hasOwnProperty('actionName')) {
                obj['actionName'] = ApiClient.convertToType(data['actionName'], 'String');
            }
            if (data.hasOwnProperty('startTime')) {
                obj['startTime'] = ApiClient.convertToType(data['startTime'], 'Date');
            }
            if (data.hasOwnProperty('lastUpdateTime')) {
                obj['lastUpdateTime'] = ApiClient.convertToType(data['lastUpdateTime'], 'Date');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], ActionExecutionStatus);
            }
            if (data.hasOwnProperty('input')) {
                obj['input'] = ActionExecutionDetailInput.constructFromObject(data['input']);
            }
            if (data.hasOwnProperty('output')) {
                obj['output'] = ActionExecutionDetailOutput.constructFromObject(data['output']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ActionExecutionDetail</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ActionExecutionDetail</code>.
     */
    static validateJSON(data) {
        // validate the optional field `pipelineExecutionId`
        if (data['pipelineExecutionId']) { // data not null
          String.validateJSON(data['pipelineExecutionId']);
        }
        // validate the optional field `actionExecutionId`
        if (data['actionExecutionId']) { // data not null
          String.validateJSON(data['actionExecutionId']);
        }
        // validate the optional field `pipelineVersion`
        if (data['pipelineVersion']) { // data not null
          Number.validateJSON(data['pipelineVersion']);
        }
        // validate the optional field `stageName`
        if (data['stageName']) { // data not null
          String.validateJSON(data['stageName']);
        }
        // validate the optional field `actionName`
        if (data['actionName']) { // data not null
          String.validateJSON(data['actionName']);
        }
        // validate the optional field `startTime`
        if (data['startTime']) { // data not null
          Date.validateJSON(data['startTime']);
        }
        // validate the optional field `lastUpdateTime`
        if (data['lastUpdateTime']) { // data not null
          Date.validateJSON(data['lastUpdateTime']);
        }
        // validate the optional field `status`
        if (data['status']) { // data not null
          ActionExecutionStatus.validateJSON(data['status']);
        }
        // validate the optional field `input`
        if (data['input']) { // data not null
          ActionExecutionDetailInput.validateJSON(data['input']);
        }
        // validate the optional field `output`
        if (data['output']) { // data not null
          ActionExecutionDetailOutput.validateJSON(data['output']);
        }

        return true;
    }


}



/**
 * @member {String} pipelineExecutionId
 */
ActionExecutionDetail.prototype['pipelineExecutionId'] = undefined;

/**
 * @member {String} actionExecutionId
 */
ActionExecutionDetail.prototype['actionExecutionId'] = undefined;

/**
 * @member {Number} pipelineVersion
 */
ActionExecutionDetail.prototype['pipelineVersion'] = undefined;

/**
 * @member {String} stageName
 */
ActionExecutionDetail.prototype['stageName'] = undefined;

/**
 * @member {String} actionName
 */
ActionExecutionDetail.prototype['actionName'] = undefined;

/**
 * @member {Date} startTime
 */
ActionExecutionDetail.prototype['startTime'] = undefined;

/**
 * @member {Date} lastUpdateTime
 */
ActionExecutionDetail.prototype['lastUpdateTime'] = undefined;

/**
 * @member {module:model/ActionExecutionStatus} status
 */
ActionExecutionDetail.prototype['status'] = undefined;

/**
 * @member {module:model/ActionExecutionDetailInput} input
 */
ActionExecutionDetail.prototype['input'] = undefined;

/**
 * @member {module:model/ActionExecutionDetailOutput} output
 */
ActionExecutionDetail.prototype['output'] = undefined;






export default ActionExecutionDetail;

