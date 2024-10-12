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

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.AwsCodePipeline);
  }
}(this, function(expect, AwsCodePipeline) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AwsCodePipeline.DefaultApi();
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
    describe('acknowledgeJob', function() {
      it('should call acknowledgeJob successfully', function(done) {
        //uncomment below and update the code to test acknowledgeJob
        //instance.acknowledgeJob(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('acknowledgeThirdPartyJob', function() {
      it('should call acknowledgeThirdPartyJob successfully', function(done) {
        //uncomment below and update the code to test acknowledgeThirdPartyJob
        //instance.acknowledgeThirdPartyJob(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createCustomActionType', function() {
      it('should call createCustomActionType successfully', function(done) {
        //uncomment below and update the code to test createCustomActionType
        //instance.createCustomActionType(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createPipeline', function() {
      it('should call createPipeline successfully', function(done) {
        //uncomment below and update the code to test createPipeline
        //instance.createPipeline(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteCustomActionType', function() {
      it('should call deleteCustomActionType successfully', function(done) {
        //uncomment below and update the code to test deleteCustomActionType
        //instance.deleteCustomActionType(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deletePipeline', function() {
      it('should call deletePipeline successfully', function(done) {
        //uncomment below and update the code to test deletePipeline
        //instance.deletePipeline(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteWebhook', function() {
      it('should call deleteWebhook successfully', function(done) {
        //uncomment below and update the code to test deleteWebhook
        //instance.deleteWebhook(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deregisterWebhookWithThirdParty', function() {
      it('should call deregisterWebhookWithThirdParty successfully', function(done) {
        //uncomment below and update the code to test deregisterWebhookWithThirdParty
        //instance.deregisterWebhookWithThirdParty(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('disableStageTransition', function() {
      it('should call disableStageTransition successfully', function(done) {
        //uncomment below and update the code to test disableStageTransition
        //instance.disableStageTransition(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('enableStageTransition', function() {
      it('should call enableStageTransition successfully', function(done) {
        //uncomment below and update the code to test enableStageTransition
        //instance.enableStageTransition(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getActionType', function() {
      it('should call getActionType successfully', function(done) {
        //uncomment below and update the code to test getActionType
        //instance.getActionType(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getJobDetails', function() {
      it('should call getJobDetails successfully', function(done) {
        //uncomment below and update the code to test getJobDetails
        //instance.getJobDetails(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getPipeline', function() {
      it('should call getPipeline successfully', function(done) {
        //uncomment below and update the code to test getPipeline
        //instance.getPipeline(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getPipelineExecution', function() {
      it('should call getPipelineExecution successfully', function(done) {
        //uncomment below and update the code to test getPipelineExecution
        //instance.getPipelineExecution(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getPipelineState', function() {
      it('should call getPipelineState successfully', function(done) {
        //uncomment below and update the code to test getPipelineState
        //instance.getPipelineState(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getThirdPartyJobDetails', function() {
      it('should call getThirdPartyJobDetails successfully', function(done) {
        //uncomment below and update the code to test getThirdPartyJobDetails
        //instance.getThirdPartyJobDetails(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listActionExecutions', function() {
      it('should call listActionExecutions successfully', function(done) {
        //uncomment below and update the code to test listActionExecutions
        //instance.listActionExecutions(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listActionTypes', function() {
      it('should call listActionTypes successfully', function(done) {
        //uncomment below and update the code to test listActionTypes
        //instance.listActionTypes(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listPipelineExecutions', function() {
      it('should call listPipelineExecutions successfully', function(done) {
        //uncomment below and update the code to test listPipelineExecutions
        //instance.listPipelineExecutions(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listPipelines', function() {
      it('should call listPipelines successfully', function(done) {
        //uncomment below and update the code to test listPipelines
        //instance.listPipelines(function(error) {
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
    describe('listWebhooks', function() {
      it('should call listWebhooks successfully', function(done) {
        //uncomment below and update the code to test listWebhooks
        //instance.listWebhooks(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('pollForJobs', function() {
      it('should call pollForJobs successfully', function(done) {
        //uncomment below and update the code to test pollForJobs
        //instance.pollForJobs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('pollForThirdPartyJobs', function() {
      it('should call pollForThirdPartyJobs successfully', function(done) {
        //uncomment below and update the code to test pollForThirdPartyJobs
        //instance.pollForThirdPartyJobs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('putActionRevision', function() {
      it('should call putActionRevision successfully', function(done) {
        //uncomment below and update the code to test putActionRevision
        //instance.putActionRevision(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('putApprovalResult', function() {
      it('should call putApprovalResult successfully', function(done) {
        //uncomment below and update the code to test putApprovalResult
        //instance.putApprovalResult(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('putJobFailureResult', function() {
      it('should call putJobFailureResult successfully', function(done) {
        //uncomment below and update the code to test putJobFailureResult
        //instance.putJobFailureResult(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('putJobSuccessResult', function() {
      it('should call putJobSuccessResult successfully', function(done) {
        //uncomment below and update the code to test putJobSuccessResult
        //instance.putJobSuccessResult(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('putThirdPartyJobFailureResult', function() {
      it('should call putThirdPartyJobFailureResult successfully', function(done) {
        //uncomment below and update the code to test putThirdPartyJobFailureResult
        //instance.putThirdPartyJobFailureResult(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('putThirdPartyJobSuccessResult', function() {
      it('should call putThirdPartyJobSuccessResult successfully', function(done) {
        //uncomment below and update the code to test putThirdPartyJobSuccessResult
        //instance.putThirdPartyJobSuccessResult(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('putWebhook', function() {
      it('should call putWebhook successfully', function(done) {
        //uncomment below and update the code to test putWebhook
        //instance.putWebhook(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('registerWebhookWithThirdParty', function() {
      it('should call registerWebhookWithThirdParty successfully', function(done) {
        //uncomment below and update the code to test registerWebhookWithThirdParty
        //instance.registerWebhookWithThirdParty(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('retryStageExecution', function() {
      it('should call retryStageExecution successfully', function(done) {
        //uncomment below and update the code to test retryStageExecution
        //instance.retryStageExecution(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('startPipelineExecution', function() {
      it('should call startPipelineExecution successfully', function(done) {
        //uncomment below and update the code to test startPipelineExecution
        //instance.startPipelineExecution(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('stopPipelineExecution', function() {
      it('should call stopPipelineExecution successfully', function(done) {
        //uncomment below and update the code to test stopPipelineExecution
        //instance.stopPipelineExecution(function(error) {
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
    describe('updateActionType', function() {
      it('should call updateActionType successfully', function(done) {
        //uncomment below and update the code to test updateActionType
        //instance.updateActionType(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updatePipeline', function() {
      it('should call updatePipeline successfully', function(done) {
        //uncomment below and update the code to test updatePipeline
        //instance.updatePipeline(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
