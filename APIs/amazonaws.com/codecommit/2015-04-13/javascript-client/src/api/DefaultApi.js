/**
 * AWS CodeCommit
 * <fullname>AWS CodeCommit</fullname> <p>This is the <i>AWS CodeCommit API Reference</i>. This reference provides descriptions of the operations and data types for AWS CodeCommit API along with usage examples.</p> <p>You can use the AWS CodeCommit API to work with the following objects:</p> <p>Repositories, by calling the following:</p> <ul> <li> <p> <a>BatchGetRepositories</a>, which returns information about one or more repositories associated with your AWS account.</p> </li> <li> <p> <a>CreateRepository</a>, which creates an AWS CodeCommit repository.</p> </li> <li> <p> <a>DeleteRepository</a>, which deletes an AWS CodeCommit repository.</p> </li> <li> <p> <a>GetRepository</a>, which returns information about a specified repository.</p> </li> <li> <p> <a>ListRepositories</a>, which lists all AWS CodeCommit repositories associated with your AWS account.</p> </li> <li> <p> <a>UpdateRepositoryDescription</a>, which sets or updates the description of the repository.</p> </li> <li> <p> <a>UpdateRepositoryName</a>, which changes the name of the repository. If you change the name of a repository, no other users of that repository can access it until you send them the new HTTPS or SSH URL to use.</p> </li> </ul> <p>Branches, by calling the following:</p> <ul> <li> <p> <a>CreateBranch</a>, which creates a branch in a specified repository.</p> </li> <li> <p> <a>DeleteBranch</a>, which deletes the specified branch in a repository unless it is the default branch.</p> </li> <li> <p> <a>GetBranch</a>, which returns information about a specified branch.</p> </li> <li> <p> <a>ListBranches</a>, which lists all branches for a specified repository.</p> </li> <li> <p> <a>UpdateDefaultBranch</a>, which changes the default branch for a repository.</p> </li> </ul> <p>Files, by calling the following:</p> <ul> <li> <p> <a>DeleteFile</a>, which deletes the content of a specified file from a specified branch.</p> </li> <li> <p> <a>GetBlob</a>, which returns the base-64 encoded content of an individual Git blob object in a repository.</p> </li> <li> <p> <a>GetFile</a>, which returns the base-64 encoded content of a specified file.</p> </li> <li> <p> <a>GetFolder</a>, which returns the contents of a specified folder or directory.</p> </li> <li> <p> <a>PutFile</a>, which adds or modifies a single file in a specified repository and branch.</p> </li> </ul> <p>Commits, by calling the following:</p> <ul> <li> <p> <a>BatchGetCommits</a>, which returns information about one or more commits in a repository.</p> </li> <li> <p> <a>CreateCommit</a>, which creates a commit for changes to a repository.</p> </li> <li> <p> <a>GetCommit</a>, which returns information about a commit, including commit messages and author and committer information.</p> </li> <li> <p> <a>GetDifferences</a>, which returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID, or other fully qualified reference).</p> </li> </ul> <p>Merges, by calling the following:</p> <ul> <li> <p> <a>BatchDescribeMergeConflicts</a>, which returns information about conflicts in a merge between commits in a repository.</p> </li> <li> <p> <a>CreateUnreferencedMergeCommit</a>, which creates an unreferenced commit between two branches or commits for the purpose of comparing them and identifying any potential conflicts.</p> </li> <li> <p> <a>DescribeMergeConflicts</a>, which returns information about merge conflicts between the base, source, and destination versions of a file in a potential merge.</p> </li> <li> <p> <a>GetMergeCommit</a>, which returns information about the merge between a source and destination commit. </p> </li> <li> <p> <a>GetMergeConflicts</a>, which returns information about merge conflicts between the source and destination branch in a pull request.</p> </li> <li> <p> <a>GetMergeOptions</a>, which returns information about the available merge options between two branches or commit specifiers.</p> </li> <li> <p> <a>MergeBranchesByFastForward</a>, which merges two branches using the fast-forward merge option.</p> </li> <li> <p> <a>MergeBranchesBySquash</a>, which merges two branches using the squash merge option.</p> </li> <li> <p> <a>MergeBranchesByThreeWay</a>, which merges two branches using the three-way merge option.</p> </li> </ul> <p>Pull requests, by calling the following:</p> <ul> <li> <p> <a>CreatePullRequest</a>, which creates a pull request in a specified repository.</p> </li> <li> <p> <a>CreatePullRequestApprovalRule</a>, which creates an approval rule for a specified pull request.</p> </li> <li> <p> <a>DeletePullRequestApprovalRule</a>, which deletes an approval rule for a specified pull request.</p> </li> <li> <p> <a>DescribePullRequestEvents</a>, which returns information about one or more pull request events.</p> </li> <li> <p> <a>EvaluatePullRequestApprovalRules</a>, which evaluates whether a pull request has met all the conditions specified in its associated approval rules.</p> </li> <li> <p> <a>GetCommentsForPullRequest</a>, which returns information about comments on a specified pull request.</p> </li> <li> <p> <a>GetPullRequest</a>, which returns information about a specified pull request.</p> </li> <li> <p> <a>GetPullRequestApprovalStates</a>, which returns information about the approval states for a specified pull request.</p> </li> <li> <p> <a>GetPullRequestOverrideState</a>, which returns information about whether approval rules have been set aside (overriden) for a pull request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.</p> </li> <li> <p> <a>ListPullRequests</a>, which lists all pull requests for a repository.</p> </li> <li> <p> <a>MergePullRequestByFastForward</a>, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the fast-forward merge option.</p> </li> <li> <p> <a>MergePullRequestBySquash</a>, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the squash merge option.</p> </li> <li> <p> <a>MergePullRequestByThreeWay</a>. which merges the source destination branch of a pull request into the specified destination branch for that pull request using the three-way merge option.</p> </li> <li> <p> <a>OverridePullRequestApprovalRules</a>, which sets aside all approval rule requirements for a pull request.</p> </li> <li> <p> <a>PostCommentForPullRequest</a>, which posts a comment to a pull request at the specified line, file, or request.</p> </li> <li> <p> <a>UpdatePullRequestApprovalRuleContent</a>, which updates the structure of an approval rule for a pull request.</p> </li> <li> <p> <a>UpdatePullRequestApprovalState</a>, which updates the state of an approval on a pull request.</p> </li> <li> <p> <a>UpdatePullRequestDescription</a>, which updates the description of a pull request.</p> </li> <li> <p> <a>UpdatePullRequestStatus</a>, which updates the status of a pull request.</p> </li> <li> <p> <a>UpdatePullRequestTitle</a>, which updates the title of a pull request.</p> </li> </ul> <p>Approval rule templates, by calling the following:</p> <ul> <li> <p> <a>AssociateApprovalRuleTemplateWithRepository</a>, which associates a template with a specified repository. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repository.</p> </li> <li> <p> <a>BatchAssociateApprovalRuleTemplateWithRepositories</a>, which associates a template with one or more specified repositories. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repositories.</p> </li> <li> <p> <a>BatchDisassociateApprovalRuleTemplateFromRepositories</a>, which removes the association between a template and specified repositories so that approval rules based on the template are not automatically created when pull requests are created in those repositories.</p> </li> <li> <p> <a>CreateApprovalRuleTemplate</a>, which creates a template for approval rules that can then be associated with one or more repositories in your AWS account.</p> </li> <li> <p> <a>DeleteApprovalRuleTemplate</a>, which deletes the specified template. It does not remove approval rules on pull requests already created with the template.</p> </li> <li> <p> <a>DisassociateApprovalRuleTemplateFromRepository</a>, which removes the association between a template and a repository so that approval rules based on the template are not automatically created when pull requests are created in the specified repository.</p> </li> <li> <p> <a>GetApprovalRuleTemplate</a>, which returns information about an approval rule template.</p> </li> <li> <p> <a>ListApprovalRuleTemplates</a>, which lists all approval rule templates in the AWS Region in your AWS account.</p> </li> <li> <p> <a>ListAssociatedApprovalRuleTemplatesForRepository</a>, which lists all approval rule templates that are associated with a specified repository.</p> </li> <li> <p> <a>ListRepositoriesForApprovalRuleTemplate</a>, which lists all repositories associated with the specified approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateDescription</a>, which updates the description of an approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateName</a>, which updates the name of an approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateContent</a>, which updates the content of an approval rule template.</p> </li> </ul> <p>Comments in a repository, by calling the following:</p> <ul> <li> <p> <a>DeleteCommentContent</a>, which deletes the content of a comment on a commit in a repository.</p> </li> <li> <p> <a>GetComment</a>, which returns information about a comment on a commit.</p> </li> <li> <p> <a>GetCommentReactions</a>, which returns information about emoji reactions to comments.</p> </li> <li> <p> <a>GetCommentsForComparedCommit</a>, which returns information about comments on the comparison between two commit specifiers in a repository.</p> </li> <li> <p> <a>PostCommentForComparedCommit</a>, which creates a comment on the comparison between two commit specifiers in a repository.</p> </li> <li> <p> <a>PostCommentReply</a>, which creates a reply to a comment.</p> </li> <li> <p> <a>PutCommentReaction</a>, which creates or updates an emoji reaction to a comment.</p> </li> <li> <p> <a>UpdateComment</a>, which updates the content of a comment on a commit in a repository.</p> </li> </ul> <p>Tags used to tag resources in AWS CodeCommit (not Git tags), by calling the following:</p> <ul> <li> <p> <a>ListTagsForResource</a>, which gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS CodeCommit.</p> </li> <li> <p> <a>TagResource</a>, which adds or updates tags for a resource in AWS CodeCommit.</p> </li> <li> <p> <a>UntagResource</a>, which removes tags for a resource in AWS CodeCommit.</p> </li> </ul> <p>Triggers, by calling the following:</p> <ul> <li> <p> <a>GetRepositoryTriggers</a>, which returns information about triggers configured for a repository.</p> </li> <li> <p> <a>PutRepositoryTriggers</a>, which replaces all triggers for a repository and can be used to create or delete triggers.</p> </li> <li> <p> <a>TestRepositoryTriggers</a>, which tests the functionality of a repository trigger by sending data to the trigger target.</p> </li> </ul> <p>For information about how to use AWS CodeCommit, see the <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html\">AWS CodeCommit User Guide</a>.</p>
 *
 * The version of the OpenAPI document: 2015-04-13
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AssociateApprovalRuleTemplateWithRepositoryInput from '../model/AssociateApprovalRuleTemplateWithRepositoryInput';
import BatchAssociateApprovalRuleTemplateWithRepositoriesInput from '../model/BatchAssociateApprovalRuleTemplateWithRepositoriesInput';
import BatchAssociateApprovalRuleTemplateWithRepositoriesOutput from '../model/BatchAssociateApprovalRuleTemplateWithRepositoriesOutput';
import BatchDescribeMergeConflictsInput from '../model/BatchDescribeMergeConflictsInput';
import BatchDescribeMergeConflictsOutput from '../model/BatchDescribeMergeConflictsOutput';
import BatchDisassociateApprovalRuleTemplateFromRepositoriesInput from '../model/BatchDisassociateApprovalRuleTemplateFromRepositoriesInput';
import BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput from '../model/BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput';
import BatchGetCommitsInput from '../model/BatchGetCommitsInput';
import BatchGetCommitsOutput from '../model/BatchGetCommitsOutput';
import BatchGetRepositoriesInput from '../model/BatchGetRepositoriesInput';
import BatchGetRepositoriesOutput from '../model/BatchGetRepositoriesOutput';
import CreateApprovalRuleTemplateInput from '../model/CreateApprovalRuleTemplateInput';
import CreateApprovalRuleTemplateOutput from '../model/CreateApprovalRuleTemplateOutput';
import CreateBranchInput from '../model/CreateBranchInput';
import CreateCommitInput from '../model/CreateCommitInput';
import CreateCommitOutput from '../model/CreateCommitOutput';
import CreatePullRequestApprovalRuleInput from '../model/CreatePullRequestApprovalRuleInput';
import CreatePullRequestApprovalRuleOutput from '../model/CreatePullRequestApprovalRuleOutput';
import CreatePullRequestInput from '../model/CreatePullRequestInput';
import CreatePullRequestOutput from '../model/CreatePullRequestOutput';
import CreateRepositoryInput from '../model/CreateRepositoryInput';
import CreateRepositoryOutput from '../model/CreateRepositoryOutput';
import CreateUnreferencedMergeCommitInput from '../model/CreateUnreferencedMergeCommitInput';
import CreateUnreferencedMergeCommitOutput from '../model/CreateUnreferencedMergeCommitOutput';
import DeleteApprovalRuleTemplateInput from '../model/DeleteApprovalRuleTemplateInput';
import DeleteApprovalRuleTemplateOutput from '../model/DeleteApprovalRuleTemplateOutput';
import DeleteBranchInput from '../model/DeleteBranchInput';
import DeleteBranchOutput from '../model/DeleteBranchOutput';
import DeleteCommentContentInput from '../model/DeleteCommentContentInput';
import DeleteCommentContentOutput from '../model/DeleteCommentContentOutput';
import DeleteFileInput from '../model/DeleteFileInput';
import DeleteFileOutput from '../model/DeleteFileOutput';
import DeletePullRequestApprovalRuleInput from '../model/DeletePullRequestApprovalRuleInput';
import DeletePullRequestApprovalRuleOutput from '../model/DeletePullRequestApprovalRuleOutput';
import DeleteRepositoryInput from '../model/DeleteRepositoryInput';
import DeleteRepositoryOutput from '../model/DeleteRepositoryOutput';
import DescribeMergeConflictsInput from '../model/DescribeMergeConflictsInput';
import DescribeMergeConflictsOutput from '../model/DescribeMergeConflictsOutput';
import DescribePullRequestEventsInput from '../model/DescribePullRequestEventsInput';
import DescribePullRequestEventsOutput from '../model/DescribePullRequestEventsOutput';
import DisassociateApprovalRuleTemplateFromRepositoryInput from '../model/DisassociateApprovalRuleTemplateFromRepositoryInput';
import EvaluatePullRequestApprovalRulesInput from '../model/EvaluatePullRequestApprovalRulesInput';
import EvaluatePullRequestApprovalRulesOutput from '../model/EvaluatePullRequestApprovalRulesOutput';
import GetApprovalRuleTemplateInput from '../model/GetApprovalRuleTemplateInput';
import GetApprovalRuleTemplateOutput from '../model/GetApprovalRuleTemplateOutput';
import GetBlobInput from '../model/GetBlobInput';
import GetBlobOutput from '../model/GetBlobOutput';
import GetBranchInput from '../model/GetBranchInput';
import GetBranchOutput from '../model/GetBranchOutput';
import GetCommentInput from '../model/GetCommentInput';
import GetCommentOutput from '../model/GetCommentOutput';
import GetCommentReactionsInput from '../model/GetCommentReactionsInput';
import GetCommentReactionsOutput from '../model/GetCommentReactionsOutput';
import GetCommentsForComparedCommitInput from '../model/GetCommentsForComparedCommitInput';
import GetCommentsForComparedCommitOutput from '../model/GetCommentsForComparedCommitOutput';
import GetCommentsForPullRequestInput from '../model/GetCommentsForPullRequestInput';
import GetCommentsForPullRequestOutput from '../model/GetCommentsForPullRequestOutput';
import GetCommitInput from '../model/GetCommitInput';
import GetCommitOutput from '../model/GetCommitOutput';
import GetDifferencesInput from '../model/GetDifferencesInput';
import GetDifferencesOutput from '../model/GetDifferencesOutput';
import GetFileInput from '../model/GetFileInput';
import GetFileOutput from '../model/GetFileOutput';
import GetFolderInput from '../model/GetFolderInput';
import GetFolderOutput from '../model/GetFolderOutput';
import GetMergeCommitInput from '../model/GetMergeCommitInput';
import GetMergeCommitOutput from '../model/GetMergeCommitOutput';
import GetMergeConflictsInput from '../model/GetMergeConflictsInput';
import GetMergeConflictsOutput from '../model/GetMergeConflictsOutput';
import GetMergeOptionsInput from '../model/GetMergeOptionsInput';
import GetMergeOptionsOutput from '../model/GetMergeOptionsOutput';
import GetPullRequestApprovalStatesInput from '../model/GetPullRequestApprovalStatesInput';
import GetPullRequestApprovalStatesOutput from '../model/GetPullRequestApprovalStatesOutput';
import GetPullRequestInput from '../model/GetPullRequestInput';
import GetPullRequestOutput from '../model/GetPullRequestOutput';
import GetPullRequestOverrideStateInput from '../model/GetPullRequestOverrideStateInput';
import GetPullRequestOverrideStateOutput from '../model/GetPullRequestOverrideStateOutput';
import GetRepositoryInput from '../model/GetRepositoryInput';
import GetRepositoryOutput from '../model/GetRepositoryOutput';
import GetRepositoryTriggersInput from '../model/GetRepositoryTriggersInput';
import GetRepositoryTriggersOutput from '../model/GetRepositoryTriggersOutput';
import ListApprovalRuleTemplatesInput from '../model/ListApprovalRuleTemplatesInput';
import ListApprovalRuleTemplatesOutput from '../model/ListApprovalRuleTemplatesOutput';
import ListAssociatedApprovalRuleTemplatesForRepositoryInput from '../model/ListAssociatedApprovalRuleTemplatesForRepositoryInput';
import ListAssociatedApprovalRuleTemplatesForRepositoryOutput from '../model/ListAssociatedApprovalRuleTemplatesForRepositoryOutput';
import ListBranchesInput from '../model/ListBranchesInput';
import ListBranchesOutput from '../model/ListBranchesOutput';
import ListPullRequestsInput from '../model/ListPullRequestsInput';
import ListPullRequestsOutput from '../model/ListPullRequestsOutput';
import ListRepositoriesForApprovalRuleTemplateInput from '../model/ListRepositoriesForApprovalRuleTemplateInput';
import ListRepositoriesForApprovalRuleTemplateOutput from '../model/ListRepositoriesForApprovalRuleTemplateOutput';
import ListRepositoriesInput from '../model/ListRepositoriesInput';
import ListRepositoriesOutput from '../model/ListRepositoriesOutput';
import ListTagsForResourceInput from '../model/ListTagsForResourceInput';
import ListTagsForResourceOutput from '../model/ListTagsForResourceOutput';
import MergeBranchesByFastForwardInput from '../model/MergeBranchesByFastForwardInput';
import MergeBranchesByFastForwardOutput from '../model/MergeBranchesByFastForwardOutput';
import MergeBranchesBySquashInput from '../model/MergeBranchesBySquashInput';
import MergeBranchesBySquashOutput from '../model/MergeBranchesBySquashOutput';
import MergeBranchesByThreeWayInput from '../model/MergeBranchesByThreeWayInput';
import MergeBranchesByThreeWayOutput from '../model/MergeBranchesByThreeWayOutput';
import MergePullRequestByFastForwardInput from '../model/MergePullRequestByFastForwardInput';
import MergePullRequestByFastForwardOutput from '../model/MergePullRequestByFastForwardOutput';
import MergePullRequestBySquashInput from '../model/MergePullRequestBySquashInput';
import MergePullRequestBySquashOutput from '../model/MergePullRequestBySquashOutput';
import MergePullRequestByThreeWayInput from '../model/MergePullRequestByThreeWayInput';
import MergePullRequestByThreeWayOutput from '../model/MergePullRequestByThreeWayOutput';
import OverridePullRequestApprovalRulesInput from '../model/OverridePullRequestApprovalRulesInput';
import PostCommentForComparedCommitInput from '../model/PostCommentForComparedCommitInput';
import PostCommentForComparedCommitOutput from '../model/PostCommentForComparedCommitOutput';
import PostCommentForPullRequestInput from '../model/PostCommentForPullRequestInput';
import PostCommentForPullRequestOutput from '../model/PostCommentForPullRequestOutput';
import PostCommentReplyInput from '../model/PostCommentReplyInput';
import PostCommentReplyOutput from '../model/PostCommentReplyOutput';
import PutCommentReactionInput from '../model/PutCommentReactionInput';
import PutFileInput from '../model/PutFileInput';
import PutFileOutput from '../model/PutFileOutput';
import PutRepositoryTriggersInput from '../model/PutRepositoryTriggersInput';
import PutRepositoryTriggersOutput from '../model/PutRepositoryTriggersOutput';
import TagResourceInput from '../model/TagResourceInput';
import TestRepositoryTriggersInput from '../model/TestRepositoryTriggersInput';
import TestRepositoryTriggersOutput from '../model/TestRepositoryTriggersOutput';
import UntagResourceInput from '../model/UntagResourceInput';
import UpdateApprovalRuleTemplateContentInput from '../model/UpdateApprovalRuleTemplateContentInput';
import UpdateApprovalRuleTemplateContentOutput from '../model/UpdateApprovalRuleTemplateContentOutput';
import UpdateApprovalRuleTemplateDescriptionInput from '../model/UpdateApprovalRuleTemplateDescriptionInput';
import UpdateApprovalRuleTemplateDescriptionOutput from '../model/UpdateApprovalRuleTemplateDescriptionOutput';
import UpdateApprovalRuleTemplateNameInput from '../model/UpdateApprovalRuleTemplateNameInput';
import UpdateApprovalRuleTemplateNameOutput from '../model/UpdateApprovalRuleTemplateNameOutput';
import UpdateCommentInput from '../model/UpdateCommentInput';
import UpdateCommentOutput from '../model/UpdateCommentOutput';
import UpdateDefaultBranchInput from '../model/UpdateDefaultBranchInput';
import UpdatePullRequestApprovalRuleContentInput from '../model/UpdatePullRequestApprovalRuleContentInput';
import UpdatePullRequestApprovalRuleContentOutput from '../model/UpdatePullRequestApprovalRuleContentOutput';
import UpdatePullRequestApprovalStateInput from '../model/UpdatePullRequestApprovalStateInput';
import UpdatePullRequestDescriptionInput from '../model/UpdatePullRequestDescriptionInput';
import UpdatePullRequestDescriptionOutput from '../model/UpdatePullRequestDescriptionOutput';
import UpdatePullRequestStatusInput from '../model/UpdatePullRequestStatusInput';
import UpdatePullRequestStatusOutput from '../model/UpdatePullRequestStatusOutput';
import UpdatePullRequestTitleInput from '../model/UpdatePullRequestTitleInput';
import UpdatePullRequestTitleOutput from '../model/UpdatePullRequestTitleOutput';
import UpdateRepositoryDescriptionInput from '../model/UpdateRepositoryDescriptionInput';
import UpdateRepositoryNameInput from '../model/UpdateRepositoryNameInput';

/**
* Default service.
* @module api/DefaultApi
* @version 2015-04-13
*/
export default class DefaultApi {

    /**
    * Constructs a new DefaultApi. 
    * @alias module:api/DefaultApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the associateApprovalRuleTemplateWithRepository operation.
     * @callback module:api/DefaultApi~associateApprovalRuleTemplateWithRepositoryCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates an association between an approval rule template and a specified repository. Then, the next time a pull request is created in the repository where the destination reference (if specified) matches the destination reference (branch) for the pull request, an approval rule that matches the template conditions is automatically created for that pull request. If no destination references are specified in the template, an approval rule that matches the template contents is created for all pull requests in that repository.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/AssociateApprovalRuleTemplateWithRepositoryInput} associateApprovalRuleTemplateWithRepositoryInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~associateApprovalRuleTemplateWithRepositoryCallback} callback The callback function, accepting three arguments: error, data, response
     */
    associateApprovalRuleTemplateWithRepository(xAmzTarget, associateApprovalRuleTemplateWithRepositoryInput, opts, callback) {
      opts = opts || {};
      let postBody = associateApprovalRuleTemplateWithRepositoryInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling associateApprovalRuleTemplateWithRepository");
      }
      // verify the required parameter 'associateApprovalRuleTemplateWithRepositoryInput' is set
      if (associateApprovalRuleTemplateWithRepositoryInput === undefined || associateApprovalRuleTemplateWithRepositoryInput === null) {
        throw new Error("Missing the required parameter 'associateApprovalRuleTemplateWithRepositoryInput' when calling associateApprovalRuleTemplateWithRepository");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.AssociateApprovalRuleTemplateWithRepository', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the batchAssociateApprovalRuleTemplateWithRepositories operation.
     * @callback module:api/DefaultApi~batchAssociateApprovalRuleTemplateWithRepositoriesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BatchAssociateApprovalRuleTemplateWithRepositoriesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates an association between an approval rule template and one or more specified repositories. 
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/BatchAssociateApprovalRuleTemplateWithRepositoriesInput} batchAssociateApprovalRuleTemplateWithRepositoriesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~batchAssociateApprovalRuleTemplateWithRepositoriesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BatchAssociateApprovalRuleTemplateWithRepositoriesOutput}
     */
    batchAssociateApprovalRuleTemplateWithRepositories(xAmzTarget, batchAssociateApprovalRuleTemplateWithRepositoriesInput, opts, callback) {
      opts = opts || {};
      let postBody = batchAssociateApprovalRuleTemplateWithRepositoriesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling batchAssociateApprovalRuleTemplateWithRepositories");
      }
      // verify the required parameter 'batchAssociateApprovalRuleTemplateWithRepositoriesInput' is set
      if (batchAssociateApprovalRuleTemplateWithRepositoriesInput === undefined || batchAssociateApprovalRuleTemplateWithRepositoriesInput === null) {
        throw new Error("Missing the required parameter 'batchAssociateApprovalRuleTemplateWithRepositoriesInput' when calling batchAssociateApprovalRuleTemplateWithRepositories");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = BatchAssociateApprovalRuleTemplateWithRepositoriesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.BatchAssociateApprovalRuleTemplateWithRepositories', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the batchDescribeMergeConflicts operation.
     * @callback module:api/DefaultApi~batchDescribeMergeConflictsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BatchDescribeMergeConflictsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about one or more merge conflicts in the attempted merge of two commit specifiers using the squash or three-way merge strategy.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/BatchDescribeMergeConflictsInput} batchDescribeMergeConflictsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~batchDescribeMergeConflictsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BatchDescribeMergeConflictsOutput}
     */
    batchDescribeMergeConflicts(xAmzTarget, batchDescribeMergeConflictsInput, opts, callback) {
      opts = opts || {};
      let postBody = batchDescribeMergeConflictsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling batchDescribeMergeConflicts");
      }
      // verify the required parameter 'batchDescribeMergeConflictsInput' is set
      if (batchDescribeMergeConflictsInput === undefined || batchDescribeMergeConflictsInput === null) {
        throw new Error("Missing the required parameter 'batchDescribeMergeConflictsInput' when calling batchDescribeMergeConflicts");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = BatchDescribeMergeConflictsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.BatchDescribeMergeConflicts', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the batchDisassociateApprovalRuleTemplateFromRepositories operation.
     * @callback module:api/DefaultApi~batchDisassociateApprovalRuleTemplateFromRepositoriesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Removes the association between an approval rule template and one or more specified repositories. 
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/BatchDisassociateApprovalRuleTemplateFromRepositoriesInput} batchDisassociateApprovalRuleTemplateFromRepositoriesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~batchDisassociateApprovalRuleTemplateFromRepositoriesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput}
     */
    batchDisassociateApprovalRuleTemplateFromRepositories(xAmzTarget, batchDisassociateApprovalRuleTemplateFromRepositoriesInput, opts, callback) {
      opts = opts || {};
      let postBody = batchDisassociateApprovalRuleTemplateFromRepositoriesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling batchDisassociateApprovalRuleTemplateFromRepositories");
      }
      // verify the required parameter 'batchDisassociateApprovalRuleTemplateFromRepositoriesInput' is set
      if (batchDisassociateApprovalRuleTemplateFromRepositoriesInput === undefined || batchDisassociateApprovalRuleTemplateFromRepositoriesInput === null) {
        throw new Error("Missing the required parameter 'batchDisassociateApprovalRuleTemplateFromRepositoriesInput' when calling batchDisassociateApprovalRuleTemplateFromRepositories");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.BatchDisassociateApprovalRuleTemplateFromRepositories', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the batchGetCommits operation.
     * @callback module:api/DefaultApi~batchGetCommitsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BatchGetCommitsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about the contents of one or more commits in a repository.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/BatchGetCommitsInput} batchGetCommitsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~batchGetCommitsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BatchGetCommitsOutput}
     */
    batchGetCommits(xAmzTarget, batchGetCommitsInput, opts, callback) {
      opts = opts || {};
      let postBody = batchGetCommitsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling batchGetCommits");
      }
      // verify the required parameter 'batchGetCommitsInput' is set
      if (batchGetCommitsInput === undefined || batchGetCommitsInput === null) {
        throw new Error("Missing the required parameter 'batchGetCommitsInput' when calling batchGetCommits");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = BatchGetCommitsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.BatchGetCommits', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the batchGetRepositories operation.
     * @callback module:api/DefaultApi~batchGetRepositoriesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BatchGetRepositoriesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Returns information about one or more repositories.</p> <note> <p>The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/BatchGetRepositoriesInput} batchGetRepositoriesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~batchGetRepositoriesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BatchGetRepositoriesOutput}
     */
    batchGetRepositories(xAmzTarget, batchGetRepositoriesInput, opts, callback) {
      opts = opts || {};
      let postBody = batchGetRepositoriesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling batchGetRepositories");
      }
      // verify the required parameter 'batchGetRepositoriesInput' is set
      if (batchGetRepositoriesInput === undefined || batchGetRepositoriesInput === null) {
        throw new Error("Missing the required parameter 'batchGetRepositoriesInput' when calling batchGetRepositories");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = BatchGetRepositoriesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.BatchGetRepositories', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createApprovalRuleTemplate operation.
     * @callback module:api/DefaultApi~createApprovalRuleTemplateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateApprovalRuleTemplateOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a template for approval rules that can then be associated with one or more repositories in your AWS account. When you associate a template with a repository, AWS CodeCommit creates an approval rule that matches the conditions of the template for all pull requests that meet the conditions of the template. For more information, see <a>AssociateApprovalRuleTemplateWithRepository</a>.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateApprovalRuleTemplateInput} createApprovalRuleTemplateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createApprovalRuleTemplateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateApprovalRuleTemplateOutput}
     */
    createApprovalRuleTemplate(xAmzTarget, createApprovalRuleTemplateInput, opts, callback) {
      opts = opts || {};
      let postBody = createApprovalRuleTemplateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createApprovalRuleTemplate");
      }
      // verify the required parameter 'createApprovalRuleTemplateInput' is set
      if (createApprovalRuleTemplateInput === undefined || createApprovalRuleTemplateInput === null) {
        throw new Error("Missing the required parameter 'createApprovalRuleTemplateInput' when calling createApprovalRuleTemplate");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateApprovalRuleTemplateOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.CreateApprovalRuleTemplate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createBranch operation.
     * @callback module:api/DefaultApi~createBranchCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Creates a branch in a repository and points the branch to a commit.</p> <note> <p>Calling the create branch operation does not set a repository's default branch. To do this, call the update default branch operation.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateBranchInput} createBranchInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createBranchCallback} callback The callback function, accepting three arguments: error, data, response
     */
    createBranch(xAmzTarget, createBranchInput, opts, callback) {
      opts = opts || {};
      let postBody = createBranchInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createBranch");
      }
      // verify the required parameter 'createBranchInput' is set
      if (createBranchInput === undefined || createBranchInput === null) {
        throw new Error("Missing the required parameter 'createBranchInput' when calling createBranch");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.CreateBranch', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createCommit operation.
     * @callback module:api/DefaultApi~createCommitCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateCommitOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a commit for a repository on the tip of a specified branch.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateCommitInput} createCommitInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createCommitCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateCommitOutput}
     */
    createCommit(xAmzTarget, createCommitInput, opts, callback) {
      opts = opts || {};
      let postBody = createCommitInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createCommit");
      }
      // verify the required parameter 'createCommitInput' is set
      if (createCommitInput === undefined || createCommitInput === null) {
        throw new Error("Missing the required parameter 'createCommitInput' when calling createCommit");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateCommitOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.CreateCommit', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createPullRequest operation.
     * @callback module:api/DefaultApi~createPullRequestCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreatePullRequestOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a pull request in the specified repository.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreatePullRequestInput} createPullRequestInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createPullRequestCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreatePullRequestOutput}
     */
    createPullRequest(xAmzTarget, createPullRequestInput, opts, callback) {
      opts = opts || {};
      let postBody = createPullRequestInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createPullRequest");
      }
      // verify the required parameter 'createPullRequestInput' is set
      if (createPullRequestInput === undefined || createPullRequestInput === null) {
        throw new Error("Missing the required parameter 'createPullRequestInput' when calling createPullRequest");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreatePullRequestOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.CreatePullRequest', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createPullRequestApprovalRule operation.
     * @callback module:api/DefaultApi~createPullRequestApprovalRuleCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreatePullRequestApprovalRuleOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates an approval rule for a pull request.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreatePullRequestApprovalRuleInput} createPullRequestApprovalRuleInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createPullRequestApprovalRuleCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreatePullRequestApprovalRuleOutput}
     */
    createPullRequestApprovalRule(xAmzTarget, createPullRequestApprovalRuleInput, opts, callback) {
      opts = opts || {};
      let postBody = createPullRequestApprovalRuleInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createPullRequestApprovalRule");
      }
      // verify the required parameter 'createPullRequestApprovalRuleInput' is set
      if (createPullRequestApprovalRuleInput === undefined || createPullRequestApprovalRuleInput === null) {
        throw new Error("Missing the required parameter 'createPullRequestApprovalRuleInput' when calling createPullRequestApprovalRule");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreatePullRequestApprovalRuleOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.CreatePullRequestApprovalRule', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createRepository operation.
     * @callback module:api/DefaultApi~createRepositoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateRepositoryOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a new, empty repository.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateRepositoryInput} createRepositoryInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createRepositoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateRepositoryOutput}
     */
    createRepository(xAmzTarget, createRepositoryInput, opts, callback) {
      opts = opts || {};
      let postBody = createRepositoryInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createRepository");
      }
      // verify the required parameter 'createRepositoryInput' is set
      if (createRepositoryInput === undefined || createRepositoryInput === null) {
        throw new Error("Missing the required parameter 'createRepositoryInput' when calling createRepository");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateRepositoryOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.CreateRepository', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createUnreferencedMergeCommit operation.
     * @callback module:api/DefaultApi~createUnreferencedMergeCommitCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateUnreferencedMergeCommitOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Creates an unreferenced commit that represents the result of merging two branches using a specified merge strategy. This can help you determine the outcome of a potential merge. This API cannot be used with the fast-forward merge strategy because that strategy does not create a merge commit.</p> <note> <p>This unreferenced merge commit can only be accessed using the GetCommit API or through git commands such as git fetch. To retrieve this commit, you must specify its commit ID or otherwise reference it.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/CreateUnreferencedMergeCommitInput} createUnreferencedMergeCommitInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createUnreferencedMergeCommitCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateUnreferencedMergeCommitOutput}
     */
    createUnreferencedMergeCommit(xAmzTarget, createUnreferencedMergeCommitInput, opts, callback) {
      opts = opts || {};
      let postBody = createUnreferencedMergeCommitInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling createUnreferencedMergeCommit");
      }
      // verify the required parameter 'createUnreferencedMergeCommitInput' is set
      if (createUnreferencedMergeCommitInput === undefined || createUnreferencedMergeCommitInput === null) {
        throw new Error("Missing the required parameter 'createUnreferencedMergeCommitInput' when calling createUnreferencedMergeCommit");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateUnreferencedMergeCommitOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.CreateUnreferencedMergeCommit', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteApprovalRuleTemplate operation.
     * @callback module:api/DefaultApi~deleteApprovalRuleTemplateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteApprovalRuleTemplateOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes a specified approval rule template. Deleting a template does not remove approval rules on pull requests already created with the template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteApprovalRuleTemplateInput} deleteApprovalRuleTemplateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteApprovalRuleTemplateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteApprovalRuleTemplateOutput}
     */
    deleteApprovalRuleTemplate(xAmzTarget, deleteApprovalRuleTemplateInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteApprovalRuleTemplateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteApprovalRuleTemplate");
      }
      // verify the required parameter 'deleteApprovalRuleTemplateInput' is set
      if (deleteApprovalRuleTemplateInput === undefined || deleteApprovalRuleTemplateInput === null) {
        throw new Error("Missing the required parameter 'deleteApprovalRuleTemplateInput' when calling deleteApprovalRuleTemplate");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteApprovalRuleTemplateOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.DeleteApprovalRuleTemplate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteBranch operation.
     * @callback module:api/DefaultApi~deleteBranchCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteBranchOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes a branch from a repository, unless that branch is the default branch for the repository. 
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteBranchInput} deleteBranchInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteBranchCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteBranchOutput}
     */
    deleteBranch(xAmzTarget, deleteBranchInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteBranchInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteBranch");
      }
      // verify the required parameter 'deleteBranchInput' is set
      if (deleteBranchInput === undefined || deleteBranchInput === null) {
        throw new Error("Missing the required parameter 'deleteBranchInput' when calling deleteBranch");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteBranchOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.DeleteBranch', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteCommentContent operation.
     * @callback module:api/DefaultApi~deleteCommentContentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteCommentContentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes the content of a comment made on a change, file, or commit in a repository.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteCommentContentInput} deleteCommentContentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteCommentContentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteCommentContentOutput}
     */
    deleteCommentContent(xAmzTarget, deleteCommentContentInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteCommentContentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteCommentContent");
      }
      // verify the required parameter 'deleteCommentContentInput' is set
      if (deleteCommentContentInput === undefined || deleteCommentContentInput === null) {
        throw new Error("Missing the required parameter 'deleteCommentContentInput' when calling deleteCommentContent");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteCommentContentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.DeleteCommentContent', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteFile operation.
     * @callback module:api/DefaultApi~deleteFileCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteFileOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes a specified file from a specified branch. A commit is created on the branch that contains the revision. The file still exists in the commits earlier to the commit that contains the deletion.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteFileInput} deleteFileInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteFileCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteFileOutput}
     */
    deleteFile(xAmzTarget, deleteFileInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteFileInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteFile");
      }
      // verify the required parameter 'deleteFileInput' is set
      if (deleteFileInput === undefined || deleteFileInput === null) {
        throw new Error("Missing the required parameter 'deleteFileInput' when calling deleteFile");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteFileOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.DeleteFile', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deletePullRequestApprovalRule operation.
     * @callback module:api/DefaultApi~deletePullRequestApprovalRuleCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeletePullRequestApprovalRuleOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes an approval rule from a specified pull request. Approval rules can be deleted from a pull request only if the pull request is open, and if the approval rule was created specifically for a pull request and not generated from an approval rule template associated with the repository where the pull request was created. You cannot delete an approval rule from a merged or closed pull request.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeletePullRequestApprovalRuleInput} deletePullRequestApprovalRuleInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deletePullRequestApprovalRuleCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeletePullRequestApprovalRuleOutput}
     */
    deletePullRequestApprovalRule(xAmzTarget, deletePullRequestApprovalRuleInput, opts, callback) {
      opts = opts || {};
      let postBody = deletePullRequestApprovalRuleInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deletePullRequestApprovalRule");
      }
      // verify the required parameter 'deletePullRequestApprovalRuleInput' is set
      if (deletePullRequestApprovalRuleInput === undefined || deletePullRequestApprovalRuleInput === null) {
        throw new Error("Missing the required parameter 'deletePullRequestApprovalRuleInput' when calling deletePullRequestApprovalRule");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeletePullRequestApprovalRuleOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.DeletePullRequestApprovalRule', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteRepository operation.
     * @callback module:api/DefaultApi~deleteRepositoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteRepositoryOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Deletes a repository. If a specified repository was already deleted, a null repository ID is returned.</p> <important> <p>Deleting a repository also deletes all associated objects and metadata. After a repository is deleted, all future push calls to the deleted repository fail.</p> </important>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DeleteRepositoryInput} deleteRepositoryInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteRepositoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteRepositoryOutput}
     */
    deleteRepository(xAmzTarget, deleteRepositoryInput, opts, callback) {
      opts = opts || {};
      let postBody = deleteRepositoryInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling deleteRepository");
      }
      // verify the required parameter 'deleteRepositoryInput' is set
      if (deleteRepositoryInput === undefined || deleteRepositoryInput === null) {
        throw new Error("Missing the required parameter 'deleteRepositoryInput' when calling deleteRepository");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteRepositoryOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.DeleteRepository', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the describeMergeConflicts operation.
     * @callback module:api/DefaultApi~describeMergeConflictsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DescribeMergeConflictsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about one or more merge conflicts in the attempted merge of two commit specifiers using the squash or three-way merge strategy. If the merge option for the attempted merge is specified as FAST_FORWARD_MERGE, an exception is thrown.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DescribeMergeConflictsInput} describeMergeConflictsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxMergeHunks] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~describeMergeConflictsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DescribeMergeConflictsOutput}
     */
    describeMergeConflicts(xAmzTarget, describeMergeConflictsInput, opts, callback) {
      opts = opts || {};
      let postBody = describeMergeConflictsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling describeMergeConflicts");
      }
      // verify the required parameter 'describeMergeConflictsInput' is set
      if (describeMergeConflictsInput === undefined || describeMergeConflictsInput === null) {
        throw new Error("Missing the required parameter 'describeMergeConflictsInput' when calling describeMergeConflicts");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxMergeHunks': opts['maxMergeHunks'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DescribeMergeConflictsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.DescribeMergeConflicts', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the describePullRequestEvents operation.
     * @callback module:api/DefaultApi~describePullRequestEventsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DescribePullRequestEventsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about one or more pull request events.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DescribePullRequestEventsInput} describePullRequestEventsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~describePullRequestEventsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DescribePullRequestEventsOutput}
     */
    describePullRequestEvents(xAmzTarget, describePullRequestEventsInput, opts, callback) {
      opts = opts || {};
      let postBody = describePullRequestEventsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling describePullRequestEvents");
      }
      // verify the required parameter 'describePullRequestEventsInput' is set
      if (describePullRequestEventsInput === undefined || describePullRequestEventsInput === null) {
        throw new Error("Missing the required parameter 'describePullRequestEventsInput' when calling describePullRequestEvents");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DescribePullRequestEventsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.DescribePullRequestEvents', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the disassociateApprovalRuleTemplateFromRepository operation.
     * @callback module:api/DefaultApi~disassociateApprovalRuleTemplateFromRepositoryCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Removes the association between a template and a repository so that approval rules based on the template are not automatically created when pull requests are created in the specified repository. This does not delete any approval rules previously created for pull requests through the template association.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/DisassociateApprovalRuleTemplateFromRepositoryInput} disassociateApprovalRuleTemplateFromRepositoryInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~disassociateApprovalRuleTemplateFromRepositoryCallback} callback The callback function, accepting three arguments: error, data, response
     */
    disassociateApprovalRuleTemplateFromRepository(xAmzTarget, disassociateApprovalRuleTemplateFromRepositoryInput, opts, callback) {
      opts = opts || {};
      let postBody = disassociateApprovalRuleTemplateFromRepositoryInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling disassociateApprovalRuleTemplateFromRepository");
      }
      // verify the required parameter 'disassociateApprovalRuleTemplateFromRepositoryInput' is set
      if (disassociateApprovalRuleTemplateFromRepositoryInput === undefined || disassociateApprovalRuleTemplateFromRepositoryInput === null) {
        throw new Error("Missing the required parameter 'disassociateApprovalRuleTemplateFromRepositoryInput' when calling disassociateApprovalRuleTemplateFromRepository");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.DisassociateApprovalRuleTemplateFromRepository', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the evaluatePullRequestApprovalRules operation.
     * @callback module:api/DefaultApi~evaluatePullRequestApprovalRulesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EvaluatePullRequestApprovalRulesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Evaluates whether a pull request has met all the conditions specified in its associated approval rules.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/EvaluatePullRequestApprovalRulesInput} evaluatePullRequestApprovalRulesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~evaluatePullRequestApprovalRulesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EvaluatePullRequestApprovalRulesOutput}
     */
    evaluatePullRequestApprovalRules(xAmzTarget, evaluatePullRequestApprovalRulesInput, opts, callback) {
      opts = opts || {};
      let postBody = evaluatePullRequestApprovalRulesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling evaluatePullRequestApprovalRules");
      }
      // verify the required parameter 'evaluatePullRequestApprovalRulesInput' is set
      if (evaluatePullRequestApprovalRulesInput === undefined || evaluatePullRequestApprovalRulesInput === null) {
        throw new Error("Missing the required parameter 'evaluatePullRequestApprovalRulesInput' when calling evaluatePullRequestApprovalRules");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = EvaluatePullRequestApprovalRulesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.EvaluatePullRequestApprovalRules', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getApprovalRuleTemplate operation.
     * @callback module:api/DefaultApi~getApprovalRuleTemplateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetApprovalRuleTemplateOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about a specified approval rule template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetApprovalRuleTemplateInput} getApprovalRuleTemplateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getApprovalRuleTemplateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetApprovalRuleTemplateOutput}
     */
    getApprovalRuleTemplate(xAmzTarget, getApprovalRuleTemplateInput, opts, callback) {
      opts = opts || {};
      let postBody = getApprovalRuleTemplateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getApprovalRuleTemplate");
      }
      // verify the required parameter 'getApprovalRuleTemplateInput' is set
      if (getApprovalRuleTemplateInput === undefined || getApprovalRuleTemplateInput === null) {
        throw new Error("Missing the required parameter 'getApprovalRuleTemplateInput' when calling getApprovalRuleTemplate");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetApprovalRuleTemplateOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetApprovalRuleTemplate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getBlob operation.
     * @callback module:api/DefaultApi~getBlobCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetBlobOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns the base-64 encoded content of an individual blob in a repository.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetBlobInput} getBlobInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getBlobCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetBlobOutput}
     */
    getBlob(xAmzTarget, getBlobInput, opts, callback) {
      opts = opts || {};
      let postBody = getBlobInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getBlob");
      }
      // verify the required parameter 'getBlobInput' is set
      if (getBlobInput === undefined || getBlobInput === null) {
        throw new Error("Missing the required parameter 'getBlobInput' when calling getBlob");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetBlobOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetBlob', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getBranch operation.
     * @callback module:api/DefaultApi~getBranchCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetBranchOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about a repository branch, including its name and the last commit ID.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetBranchInput} getBranchInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getBranchCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetBranchOutput}
     */
    getBranch(xAmzTarget, getBranchInput, opts, callback) {
      opts = opts || {};
      let postBody = getBranchInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getBranch");
      }
      // verify the required parameter 'getBranchInput' is set
      if (getBranchInput === undefined || getBranchInput === null) {
        throw new Error("Missing the required parameter 'getBranchInput' when calling getBranch");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetBranchOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetBranch', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getComment operation.
     * @callback module:api/DefaultApi~getCommentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetCommentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Returns the content of a comment made on a change, file, or commit in a repository. </p> <note> <p>Reaction counts might include numbers from user identities who were deleted after the reaction was made. For a count of reactions from active identities, use GetCommentReactions.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetCommentInput} getCommentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getCommentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetCommentOutput}
     */
    getComment(xAmzTarget, getCommentInput, opts, callback) {
      opts = opts || {};
      let postBody = getCommentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getComment");
      }
      // verify the required parameter 'getCommentInput' is set
      if (getCommentInput === undefined || getCommentInput === null) {
        throw new Error("Missing the required parameter 'getCommentInput' when calling getComment");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetCommentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetComment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCommentReactions operation.
     * @callback module:api/DefaultApi~getCommentReactionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetCommentReactionsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about reactions to a specified comment ID. Reactions from users who have been deleted will not be included in the count.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetCommentReactionsInput} getCommentReactionsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~getCommentReactionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetCommentReactionsOutput}
     */
    getCommentReactions(xAmzTarget, getCommentReactionsInput, opts, callback) {
      opts = opts || {};
      let postBody = getCommentReactionsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getCommentReactions");
      }
      // verify the required parameter 'getCommentReactionsInput' is set
      if (getCommentReactionsInput === undefined || getCommentReactionsInput === null) {
        throw new Error("Missing the required parameter 'getCommentReactionsInput' when calling getCommentReactions");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetCommentReactionsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetCommentReactions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCommentsForComparedCommit operation.
     * @callback module:api/DefaultApi~getCommentsForComparedCommitCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetCommentsForComparedCommitOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Returns information about comments made on the comparison between two commits.</p> <note> <p>Reaction counts might include numbers from user identities who were deleted after the reaction was made. For a count of reactions from active identities, use GetCommentReactions.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetCommentsForComparedCommitInput} getCommentsForComparedCommitInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~getCommentsForComparedCommitCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetCommentsForComparedCommitOutput}
     */
    getCommentsForComparedCommit(xAmzTarget, getCommentsForComparedCommitInput, opts, callback) {
      opts = opts || {};
      let postBody = getCommentsForComparedCommitInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getCommentsForComparedCommit");
      }
      // verify the required parameter 'getCommentsForComparedCommitInput' is set
      if (getCommentsForComparedCommitInput === undefined || getCommentsForComparedCommitInput === null) {
        throw new Error("Missing the required parameter 'getCommentsForComparedCommitInput' when calling getCommentsForComparedCommit");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetCommentsForComparedCommitOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetCommentsForComparedCommit', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCommentsForPullRequest operation.
     * @callback module:api/DefaultApi~getCommentsForPullRequestCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetCommentsForPullRequestOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Returns comments made on a pull request.</p> <note> <p>Reaction counts might include numbers from user identities who were deleted after the reaction was made. For a count of reactions from active identities, use GetCommentReactions.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetCommentsForPullRequestInput} getCommentsForPullRequestInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~getCommentsForPullRequestCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetCommentsForPullRequestOutput}
     */
    getCommentsForPullRequest(xAmzTarget, getCommentsForPullRequestInput, opts, callback) {
      opts = opts || {};
      let postBody = getCommentsForPullRequestInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getCommentsForPullRequest");
      }
      // verify the required parameter 'getCommentsForPullRequestInput' is set
      if (getCommentsForPullRequestInput === undefined || getCommentsForPullRequestInput === null) {
        throw new Error("Missing the required parameter 'getCommentsForPullRequestInput' when calling getCommentsForPullRequest");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetCommentsForPullRequestOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetCommentsForPullRequest', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCommit operation.
     * @callback module:api/DefaultApi~getCommitCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetCommitOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about a commit, including commit message and committer information.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetCommitInput} getCommitInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getCommitCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetCommitOutput}
     */
    getCommit(xAmzTarget, getCommitInput, opts, callback) {
      opts = opts || {};
      let postBody = getCommitInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getCommit");
      }
      // verify the required parameter 'getCommitInput' is set
      if (getCommitInput === undefined || getCommitInput === null) {
        throw new Error("Missing the required parameter 'getCommitInput' when calling getCommit");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetCommitOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetCommit', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDifferences operation.
     * @callback module:api/DefaultApi~getDifferencesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDifferencesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID, or other fully qualified reference). Results can be limited to a specified path.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetDifferencesInput} getDifferencesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~getDifferencesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDifferencesOutput}
     */
    getDifferences(xAmzTarget, getDifferencesInput, opts, callback) {
      opts = opts || {};
      let postBody = getDifferencesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getDifferences");
      }
      // verify the required parameter 'getDifferencesInput' is set
      if (getDifferencesInput === undefined || getDifferencesInput === null) {
        throw new Error("Missing the required parameter 'getDifferencesInput' when calling getDifferences");
      }

      let pathParams = {
      };
      let queryParams = {
        'MaxResults': opts['maxResults'],
        'NextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetDifferencesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetDifferences', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getFile operation.
     * @callback module:api/DefaultApi~getFileCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetFileOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns the base-64 encoded contents of a specified file and its metadata.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetFileInput} getFileInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getFileCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetFileOutput}
     */
    getFile(xAmzTarget, getFileInput, opts, callback) {
      opts = opts || {};
      let postBody = getFileInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getFile");
      }
      // verify the required parameter 'getFileInput' is set
      if (getFileInput === undefined || getFileInput === null) {
        throw new Error("Missing the required parameter 'getFileInput' when calling getFile");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetFileOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetFile', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getFolder operation.
     * @callback module:api/DefaultApi~getFolderCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetFolderOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns the contents of a specified folder in a repository.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetFolderInput} getFolderInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getFolderCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetFolderOutput}
     */
    getFolder(xAmzTarget, getFolderInput, opts, callback) {
      opts = opts || {};
      let postBody = getFolderInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getFolder");
      }
      // verify the required parameter 'getFolderInput' is set
      if (getFolderInput === undefined || getFolderInput === null) {
        throw new Error("Missing the required parameter 'getFolderInput' when calling getFolder");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetFolderOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetFolder', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMergeCommit operation.
     * @callback module:api/DefaultApi~getMergeCommitCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetMergeCommitOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about a specified merge commit.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetMergeCommitInput} getMergeCommitInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getMergeCommitCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetMergeCommitOutput}
     */
    getMergeCommit(xAmzTarget, getMergeCommitInput, opts, callback) {
      opts = opts || {};
      let postBody = getMergeCommitInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getMergeCommit");
      }
      // verify the required parameter 'getMergeCommitInput' is set
      if (getMergeCommitInput === undefined || getMergeCommitInput === null) {
        throw new Error("Missing the required parameter 'getMergeCommitInput' when calling getMergeCommit");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetMergeCommitOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetMergeCommit', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMergeConflicts operation.
     * @callback module:api/DefaultApi~getMergeConflictsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetMergeConflictsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about merge conflicts between the before and after commit IDs for a pull request in a repository.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetMergeConflictsInput} getMergeConflictsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxConflictFiles] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~getMergeConflictsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetMergeConflictsOutput}
     */
    getMergeConflicts(xAmzTarget, getMergeConflictsInput, opts, callback) {
      opts = opts || {};
      let postBody = getMergeConflictsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getMergeConflicts");
      }
      // verify the required parameter 'getMergeConflictsInput' is set
      if (getMergeConflictsInput === undefined || getMergeConflictsInput === null) {
        throw new Error("Missing the required parameter 'getMergeConflictsInput' when calling getMergeConflicts");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxConflictFiles': opts['maxConflictFiles'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetMergeConflictsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetMergeConflicts', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMergeOptions operation.
     * @callback module:api/DefaultApi~getMergeOptionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetMergeOptionsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about the merge options available for merging two specified branches. For details about why a merge option is not available, use GetMergeConflicts or DescribeMergeConflicts.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetMergeOptionsInput} getMergeOptionsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getMergeOptionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetMergeOptionsOutput}
     */
    getMergeOptions(xAmzTarget, getMergeOptionsInput, opts, callback) {
      opts = opts || {};
      let postBody = getMergeOptionsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getMergeOptions");
      }
      // verify the required parameter 'getMergeOptionsInput' is set
      if (getMergeOptionsInput === undefined || getMergeOptionsInput === null) {
        throw new Error("Missing the required parameter 'getMergeOptionsInput' when calling getMergeOptions");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetMergeOptionsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetMergeOptions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPullRequest operation.
     * @callback module:api/DefaultApi~getPullRequestCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetPullRequestOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets information about a pull request in a specified repository.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetPullRequestInput} getPullRequestInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getPullRequestCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetPullRequestOutput}
     */
    getPullRequest(xAmzTarget, getPullRequestInput, opts, callback) {
      opts = opts || {};
      let postBody = getPullRequestInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getPullRequest");
      }
      // verify the required parameter 'getPullRequestInput' is set
      if (getPullRequestInput === undefined || getPullRequestInput === null) {
        throw new Error("Missing the required parameter 'getPullRequestInput' when calling getPullRequest");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetPullRequestOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetPullRequest', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPullRequestApprovalStates operation.
     * @callback module:api/DefaultApi~getPullRequestApprovalStatesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetPullRequestApprovalStatesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets information about the approval states for a specified pull request. Approval states only apply to pull requests that have one or more approval rules applied to them.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetPullRequestApprovalStatesInput} getPullRequestApprovalStatesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getPullRequestApprovalStatesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetPullRequestApprovalStatesOutput}
     */
    getPullRequestApprovalStates(xAmzTarget, getPullRequestApprovalStatesInput, opts, callback) {
      opts = opts || {};
      let postBody = getPullRequestApprovalStatesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getPullRequestApprovalStates");
      }
      // verify the required parameter 'getPullRequestApprovalStatesInput' is set
      if (getPullRequestApprovalStatesInput === undefined || getPullRequestApprovalStatesInput === null) {
        throw new Error("Missing the required parameter 'getPullRequestApprovalStatesInput' when calling getPullRequestApprovalStates");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetPullRequestApprovalStatesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetPullRequestApprovalStates', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPullRequestOverrideState operation.
     * @callback module:api/DefaultApi~getPullRequestOverrideStateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetPullRequestOverrideStateOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about whether approval rules have been set aside (overridden) for a pull request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetPullRequestOverrideStateInput} getPullRequestOverrideStateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getPullRequestOverrideStateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetPullRequestOverrideStateOutput}
     */
    getPullRequestOverrideState(xAmzTarget, getPullRequestOverrideStateInput, opts, callback) {
      opts = opts || {};
      let postBody = getPullRequestOverrideStateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getPullRequestOverrideState");
      }
      // verify the required parameter 'getPullRequestOverrideStateInput' is set
      if (getPullRequestOverrideStateInput === undefined || getPullRequestOverrideStateInput === null) {
        throw new Error("Missing the required parameter 'getPullRequestOverrideStateInput' when calling getPullRequestOverrideState");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetPullRequestOverrideStateOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetPullRequestOverrideState', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRepository operation.
     * @callback module:api/DefaultApi~getRepositoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetRepositoryOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Returns information about a repository.</p> <note> <p>The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetRepositoryInput} getRepositoryInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getRepositoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetRepositoryOutput}
     */
    getRepository(xAmzTarget, getRepositoryInput, opts, callback) {
      opts = opts || {};
      let postBody = getRepositoryInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getRepository");
      }
      // verify the required parameter 'getRepositoryInput' is set
      if (getRepositoryInput === undefined || getRepositoryInput === null) {
        throw new Error("Missing the required parameter 'getRepositoryInput' when calling getRepository");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetRepositoryOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetRepository', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRepositoryTriggers operation.
     * @callback module:api/DefaultApi~getRepositoryTriggersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetRepositoryTriggersOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets information about triggers configured for a repository.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/GetRepositoryTriggersInput} getRepositoryTriggersInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getRepositoryTriggersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetRepositoryTriggersOutput}
     */
    getRepositoryTriggers(xAmzTarget, getRepositoryTriggersInput, opts, callback) {
      opts = opts || {};
      let postBody = getRepositoryTriggersInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling getRepositoryTriggers");
      }
      // verify the required parameter 'getRepositoryTriggersInput' is set
      if (getRepositoryTriggersInput === undefined || getRepositoryTriggersInput === null) {
        throw new Error("Missing the required parameter 'getRepositoryTriggersInput' when calling getRepositoryTriggers");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetRepositoryTriggersOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.GetRepositoryTriggers', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listApprovalRuleTemplates operation.
     * @callback module:api/DefaultApi~listApprovalRuleTemplatesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListApprovalRuleTemplatesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists all approval rule templates in the specified AWS Region in your AWS account. If an AWS Region is not specified, the AWS Region where you are signed in is used.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListApprovalRuleTemplatesInput} listApprovalRuleTemplatesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listApprovalRuleTemplatesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListApprovalRuleTemplatesOutput}
     */
    listApprovalRuleTemplates(xAmzTarget, listApprovalRuleTemplatesInput, opts, callback) {
      opts = opts || {};
      let postBody = listApprovalRuleTemplatesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listApprovalRuleTemplates");
      }
      // verify the required parameter 'listApprovalRuleTemplatesInput' is set
      if (listApprovalRuleTemplatesInput === undefined || listApprovalRuleTemplatesInput === null) {
        throw new Error("Missing the required parameter 'listApprovalRuleTemplatesInput' when calling listApprovalRuleTemplates");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListApprovalRuleTemplatesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.ListApprovalRuleTemplates', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listAssociatedApprovalRuleTemplatesForRepository operation.
     * @callback module:api/DefaultApi~listAssociatedApprovalRuleTemplatesForRepositoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListAssociatedApprovalRuleTemplatesForRepositoryOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists all approval rule templates that are associated with a specified repository.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListAssociatedApprovalRuleTemplatesForRepositoryInput} listAssociatedApprovalRuleTemplatesForRepositoryInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listAssociatedApprovalRuleTemplatesForRepositoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListAssociatedApprovalRuleTemplatesForRepositoryOutput}
     */
    listAssociatedApprovalRuleTemplatesForRepository(xAmzTarget, listAssociatedApprovalRuleTemplatesForRepositoryInput, opts, callback) {
      opts = opts || {};
      let postBody = listAssociatedApprovalRuleTemplatesForRepositoryInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listAssociatedApprovalRuleTemplatesForRepository");
      }
      // verify the required parameter 'listAssociatedApprovalRuleTemplatesForRepositoryInput' is set
      if (listAssociatedApprovalRuleTemplatesForRepositoryInput === undefined || listAssociatedApprovalRuleTemplatesForRepositoryInput === null) {
        throw new Error("Missing the required parameter 'listAssociatedApprovalRuleTemplatesForRepositoryInput' when calling listAssociatedApprovalRuleTemplatesForRepository");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListAssociatedApprovalRuleTemplatesForRepositoryOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.ListAssociatedApprovalRuleTemplatesForRepository', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listBranches operation.
     * @callback module:api/DefaultApi~listBranchesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListBranchesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets information about one or more branches in a repository.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListBranchesInput} listBranchesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listBranchesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListBranchesOutput}
     */
    listBranches(xAmzTarget, listBranchesInput, opts, callback) {
      opts = opts || {};
      let postBody = listBranchesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listBranches");
      }
      // verify the required parameter 'listBranchesInput' is set
      if (listBranchesInput === undefined || listBranchesInput === null) {
        throw new Error("Missing the required parameter 'listBranchesInput' when calling listBranches");
      }

      let pathParams = {
      };
      let queryParams = {
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListBranchesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.ListBranches', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listPullRequests operation.
     * @callback module:api/DefaultApi~listPullRequestsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListPullRequestsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns a list of pull requests for a specified repository. The return list can be refined by pull request status or pull request author ARN.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListPullRequestsInput} listPullRequestsInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listPullRequestsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListPullRequestsOutput}
     */
    listPullRequests(xAmzTarget, listPullRequestsInput, opts, callback) {
      opts = opts || {};
      let postBody = listPullRequestsInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listPullRequests");
      }
      // verify the required parameter 'listPullRequestsInput' is set
      if (listPullRequestsInput === undefined || listPullRequestsInput === null) {
        throw new Error("Missing the required parameter 'listPullRequestsInput' when calling listPullRequests");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListPullRequestsOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.ListPullRequests', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listRepositories operation.
     * @callback module:api/DefaultApi~listRepositoriesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListRepositoriesOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets information about one or more repositories.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListRepositoriesInput} listRepositoriesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listRepositoriesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListRepositoriesOutput}
     */
    listRepositories(xAmzTarget, listRepositoriesInput, opts, callback) {
      opts = opts || {};
      let postBody = listRepositoriesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listRepositories");
      }
      // verify the required parameter 'listRepositoriesInput' is set
      if (listRepositoriesInput === undefined || listRepositoriesInput === null) {
        throw new Error("Missing the required parameter 'listRepositoriesInput' when calling listRepositories");
      }

      let pathParams = {
      };
      let queryParams = {
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListRepositoriesOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.ListRepositories', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listRepositoriesForApprovalRuleTemplate operation.
     * @callback module:api/DefaultApi~listRepositoriesForApprovalRuleTemplateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListRepositoriesForApprovalRuleTemplateOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists all repositories associated with the specified approval rule template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListRepositoriesForApprovalRuleTemplateInput} listRepositoriesForApprovalRuleTemplateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listRepositoriesForApprovalRuleTemplateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListRepositoriesForApprovalRuleTemplateOutput}
     */
    listRepositoriesForApprovalRuleTemplate(xAmzTarget, listRepositoriesForApprovalRuleTemplateInput, opts, callback) {
      opts = opts || {};
      let postBody = listRepositoriesForApprovalRuleTemplateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listRepositoriesForApprovalRuleTemplate");
      }
      // verify the required parameter 'listRepositoriesForApprovalRuleTemplateInput' is set
      if (listRepositoriesForApprovalRuleTemplateInput === undefined || listRepositoriesForApprovalRuleTemplateInput === null) {
        throw new Error("Missing the required parameter 'listRepositoriesForApprovalRuleTemplateInput' when calling listRepositoriesForApprovalRuleTemplate");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListRepositoriesForApprovalRuleTemplateOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.ListRepositoriesForApprovalRuleTemplate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listTagsForResource operation.
     * @callback module:api/DefaultApi~listTagsForResourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListTagsForResourceOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS CodeCommit. For a list of valid resources in AWS CodeCommit, see <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats\">CodeCommit Resources and Operations</a> in the<i> AWS CodeCommit User Guide</i>.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/ListTagsForResourceInput} listTagsForResourceInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~listTagsForResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListTagsForResourceOutput}
     */
    listTagsForResource(xAmzTarget, listTagsForResourceInput, opts, callback) {
      opts = opts || {};
      let postBody = listTagsForResourceInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling listTagsForResource");
      }
      // verify the required parameter 'listTagsForResourceInput' is set
      if (listTagsForResourceInput === undefined || listTagsForResourceInput === null) {
        throw new Error("Missing the required parameter 'listTagsForResourceInput' when calling listTagsForResource");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListTagsForResourceOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.ListTagsForResource', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the mergeBranchesByFastForward operation.
     * @callback module:api/DefaultApi~mergeBranchesByFastForwardCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MergeBranchesByFastForwardOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Merges two branches using the fast-forward merge strategy.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/MergeBranchesByFastForwardInput} mergeBranchesByFastForwardInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~mergeBranchesByFastForwardCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MergeBranchesByFastForwardOutput}
     */
    mergeBranchesByFastForward(xAmzTarget, mergeBranchesByFastForwardInput, opts, callback) {
      opts = opts || {};
      let postBody = mergeBranchesByFastForwardInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling mergeBranchesByFastForward");
      }
      // verify the required parameter 'mergeBranchesByFastForwardInput' is set
      if (mergeBranchesByFastForwardInput === undefined || mergeBranchesByFastForwardInput === null) {
        throw new Error("Missing the required parameter 'mergeBranchesByFastForwardInput' when calling mergeBranchesByFastForward");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = MergeBranchesByFastForwardOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.MergeBranchesByFastForward', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the mergeBranchesBySquash operation.
     * @callback module:api/DefaultApi~mergeBranchesBySquashCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MergeBranchesBySquashOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Merges two branches using the squash merge strategy.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/MergeBranchesBySquashInput} mergeBranchesBySquashInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~mergeBranchesBySquashCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MergeBranchesBySquashOutput}
     */
    mergeBranchesBySquash(xAmzTarget, mergeBranchesBySquashInput, opts, callback) {
      opts = opts || {};
      let postBody = mergeBranchesBySquashInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling mergeBranchesBySquash");
      }
      // verify the required parameter 'mergeBranchesBySquashInput' is set
      if (mergeBranchesBySquashInput === undefined || mergeBranchesBySquashInput === null) {
        throw new Error("Missing the required parameter 'mergeBranchesBySquashInput' when calling mergeBranchesBySquash");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = MergeBranchesBySquashOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.MergeBranchesBySquash', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the mergeBranchesByThreeWay operation.
     * @callback module:api/DefaultApi~mergeBranchesByThreeWayCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MergeBranchesByThreeWayOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Merges two specified branches using the three-way merge strategy.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/MergeBranchesByThreeWayInput} mergeBranchesByThreeWayInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~mergeBranchesByThreeWayCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MergeBranchesByThreeWayOutput}
     */
    mergeBranchesByThreeWay(xAmzTarget, mergeBranchesByThreeWayInput, opts, callback) {
      opts = opts || {};
      let postBody = mergeBranchesByThreeWayInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling mergeBranchesByThreeWay");
      }
      // verify the required parameter 'mergeBranchesByThreeWayInput' is set
      if (mergeBranchesByThreeWayInput === undefined || mergeBranchesByThreeWayInput === null) {
        throw new Error("Missing the required parameter 'mergeBranchesByThreeWayInput' when calling mergeBranchesByThreeWay");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = MergeBranchesByThreeWayOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.MergeBranchesByThreeWay', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the mergePullRequestByFastForward operation.
     * @callback module:api/DefaultApi~mergePullRequestByFastForwardCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MergePullRequestByFastForwardOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the fast-forward merge strategy. If the merge is successful, it closes the pull request.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/MergePullRequestByFastForwardInput} mergePullRequestByFastForwardInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~mergePullRequestByFastForwardCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MergePullRequestByFastForwardOutput}
     */
    mergePullRequestByFastForward(xAmzTarget, mergePullRequestByFastForwardInput, opts, callback) {
      opts = opts || {};
      let postBody = mergePullRequestByFastForwardInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling mergePullRequestByFastForward");
      }
      // verify the required parameter 'mergePullRequestByFastForwardInput' is set
      if (mergePullRequestByFastForwardInput === undefined || mergePullRequestByFastForwardInput === null) {
        throw new Error("Missing the required parameter 'mergePullRequestByFastForwardInput' when calling mergePullRequestByFastForward");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = MergePullRequestByFastForwardOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.MergePullRequestByFastForward', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the mergePullRequestBySquash operation.
     * @callback module:api/DefaultApi~mergePullRequestBySquashCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MergePullRequestBySquashOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the squash merge strategy. If the merge is successful, it closes the pull request.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/MergePullRequestBySquashInput} mergePullRequestBySquashInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~mergePullRequestBySquashCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MergePullRequestBySquashOutput}
     */
    mergePullRequestBySquash(xAmzTarget, mergePullRequestBySquashInput, opts, callback) {
      opts = opts || {};
      let postBody = mergePullRequestBySquashInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling mergePullRequestBySquash");
      }
      // verify the required parameter 'mergePullRequestBySquashInput' is set
      if (mergePullRequestBySquashInput === undefined || mergePullRequestBySquashInput === null) {
        throw new Error("Missing the required parameter 'mergePullRequestBySquashInput' when calling mergePullRequestBySquash");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = MergePullRequestBySquashOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.MergePullRequestBySquash', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the mergePullRequestByThreeWay operation.
     * @callback module:api/DefaultApi~mergePullRequestByThreeWayCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MergePullRequestByThreeWayOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the three-way merge strategy. If the merge is successful, it closes the pull request.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/MergePullRequestByThreeWayInput} mergePullRequestByThreeWayInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~mergePullRequestByThreeWayCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MergePullRequestByThreeWayOutput}
     */
    mergePullRequestByThreeWay(xAmzTarget, mergePullRequestByThreeWayInput, opts, callback) {
      opts = opts || {};
      let postBody = mergePullRequestByThreeWayInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling mergePullRequestByThreeWay");
      }
      // verify the required parameter 'mergePullRequestByThreeWayInput' is set
      if (mergePullRequestByThreeWayInput === undefined || mergePullRequestByThreeWayInput === null) {
        throw new Error("Missing the required parameter 'mergePullRequestByThreeWayInput' when calling mergePullRequestByThreeWay");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = MergePullRequestByThreeWayOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.MergePullRequestByThreeWay', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the overridePullRequestApprovalRules operation.
     * @callback module:api/DefaultApi~overridePullRequestApprovalRulesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Sets aside (overrides) all approval rule requirements for a specified pull request.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/OverridePullRequestApprovalRulesInput} overridePullRequestApprovalRulesInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~overridePullRequestApprovalRulesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    overridePullRequestApprovalRules(xAmzTarget, overridePullRequestApprovalRulesInput, opts, callback) {
      opts = opts || {};
      let postBody = overridePullRequestApprovalRulesInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling overridePullRequestApprovalRules");
      }
      // verify the required parameter 'overridePullRequestApprovalRulesInput' is set
      if (overridePullRequestApprovalRulesInput === undefined || overridePullRequestApprovalRulesInput === null) {
        throw new Error("Missing the required parameter 'overridePullRequestApprovalRulesInput' when calling overridePullRequestApprovalRules");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.OverridePullRequestApprovalRules', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postCommentForComparedCommit operation.
     * @callback module:api/DefaultApi~postCommentForComparedCommitCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PostCommentForComparedCommitOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Posts a comment on the comparison between two commits.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PostCommentForComparedCommitInput} postCommentForComparedCommitInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~postCommentForComparedCommitCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PostCommentForComparedCommitOutput}
     */
    postCommentForComparedCommit(xAmzTarget, postCommentForComparedCommitInput, opts, callback) {
      opts = opts || {};
      let postBody = postCommentForComparedCommitInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling postCommentForComparedCommit");
      }
      // verify the required parameter 'postCommentForComparedCommitInput' is set
      if (postCommentForComparedCommitInput === undefined || postCommentForComparedCommitInput === null) {
        throw new Error("Missing the required parameter 'postCommentForComparedCommitInput' when calling postCommentForComparedCommit");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = PostCommentForComparedCommitOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.PostCommentForComparedCommit', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postCommentForPullRequest operation.
     * @callback module:api/DefaultApi~postCommentForPullRequestCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PostCommentForPullRequestOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Posts a comment on a pull request.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PostCommentForPullRequestInput} postCommentForPullRequestInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~postCommentForPullRequestCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PostCommentForPullRequestOutput}
     */
    postCommentForPullRequest(xAmzTarget, postCommentForPullRequestInput, opts, callback) {
      opts = opts || {};
      let postBody = postCommentForPullRequestInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling postCommentForPullRequest");
      }
      // verify the required parameter 'postCommentForPullRequestInput' is set
      if (postCommentForPullRequestInput === undefined || postCommentForPullRequestInput === null) {
        throw new Error("Missing the required parameter 'postCommentForPullRequestInput' when calling postCommentForPullRequest");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = PostCommentForPullRequestOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.PostCommentForPullRequest', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postCommentReply operation.
     * @callback module:api/DefaultApi~postCommentReplyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PostCommentReplyOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Posts a comment in reply to an existing comment on a comparison between commits or a pull request.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PostCommentReplyInput} postCommentReplyInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~postCommentReplyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PostCommentReplyOutput}
     */
    postCommentReply(xAmzTarget, postCommentReplyInput, opts, callback) {
      opts = opts || {};
      let postBody = postCommentReplyInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling postCommentReply");
      }
      // verify the required parameter 'postCommentReplyInput' is set
      if (postCommentReplyInput === undefined || postCommentReplyInput === null) {
        throw new Error("Missing the required parameter 'postCommentReplyInput' when calling postCommentReply");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = PostCommentReplyOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.PostCommentReply', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putCommentReaction operation.
     * @callback module:api/DefaultApi~putCommentReactionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Adds or updates a reaction to a specified comment for the user whose identity is used to make the request. You can only add or update a reaction for yourself. You cannot add, modify, or delete a reaction for another user.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PutCommentReactionInput} putCommentReactionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~putCommentReactionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    putCommentReaction(xAmzTarget, putCommentReactionInput, opts, callback) {
      opts = opts || {};
      let postBody = putCommentReactionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling putCommentReaction");
      }
      // verify the required parameter 'putCommentReactionInput' is set
      if (putCommentReactionInput === undefined || putCommentReactionInput === null) {
        throw new Error("Missing the required parameter 'putCommentReactionInput' when calling putCommentReaction");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.PutCommentReaction', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putFile operation.
     * @callback module:api/DefaultApi~putFileCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PutFileOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Adds or updates a file in a branch in an AWS CodeCommit repository, and generates a commit for the addition in the specified branch.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PutFileInput} putFileInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~putFileCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PutFileOutput}
     */
    putFile(xAmzTarget, putFileInput, opts, callback) {
      opts = opts || {};
      let postBody = putFileInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling putFile");
      }
      // verify the required parameter 'putFileInput' is set
      if (putFileInput === undefined || putFileInput === null) {
        throw new Error("Missing the required parameter 'putFileInput' when calling putFile");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = PutFileOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.PutFile', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putRepositoryTriggers operation.
     * @callback module:api/DefaultApi~putRepositoryTriggersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PutRepositoryTriggersOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Replaces all triggers for a repository. Used to create or delete triggers.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/PutRepositoryTriggersInput} putRepositoryTriggersInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~putRepositoryTriggersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PutRepositoryTriggersOutput}
     */
    putRepositoryTriggers(xAmzTarget, putRepositoryTriggersInput, opts, callback) {
      opts = opts || {};
      let postBody = putRepositoryTriggersInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling putRepositoryTriggers");
      }
      // verify the required parameter 'putRepositoryTriggersInput' is set
      if (putRepositoryTriggersInput === undefined || putRepositoryTriggersInput === null) {
        throw new Error("Missing the required parameter 'putRepositoryTriggersInput' when calling putRepositoryTriggers");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = PutRepositoryTriggersOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.PutRepositoryTriggers', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the tagResource operation.
     * @callback module:api/DefaultApi~tagResourceCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Adds or updates tags for a resource in AWS CodeCommit. For a list of valid resources in AWS CodeCommit, see <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats\">CodeCommit Resources and Operations</a> in the <i>AWS CodeCommit User Guide</i>.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/TagResourceInput} tagResourceInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~tagResourceCallback} callback The callback function, accepting three arguments: error, data, response
     */
    tagResource(xAmzTarget, tagResourceInput, opts, callback) {
      opts = opts || {};
      let postBody = tagResourceInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling tagResource");
      }
      // verify the required parameter 'tagResourceInput' is set
      if (tagResourceInput === undefined || tagResourceInput === null) {
        throw new Error("Missing the required parameter 'tagResourceInput' when calling tagResource");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.TagResource', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testRepositoryTriggers operation.
     * @callback module:api/DefaultApi~testRepositoryTriggersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TestRepositoryTriggersOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Tests the functionality of repository triggers by sending information to the trigger target. If real data is available in the repository, the test sends data from the last commit. If no data is available, sample data is generated.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/TestRepositoryTriggersInput} testRepositoryTriggersInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~testRepositoryTriggersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TestRepositoryTriggersOutput}
     */
    testRepositoryTriggers(xAmzTarget, testRepositoryTriggersInput, opts, callback) {
      opts = opts || {};
      let postBody = testRepositoryTriggersInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling testRepositoryTriggers");
      }
      // verify the required parameter 'testRepositoryTriggersInput' is set
      if (testRepositoryTriggersInput === undefined || testRepositoryTriggersInput === null) {
        throw new Error("Missing the required parameter 'testRepositoryTriggersInput' when calling testRepositoryTriggers");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = TestRepositoryTriggersOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.TestRepositoryTriggers', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the untagResource operation.
     * @callback module:api/DefaultApi~untagResourceCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Removes tags for a resource in AWS CodeCommit. For a list of valid resources in AWS CodeCommit, see <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats\">CodeCommit Resources and Operations</a> in the <i>AWS CodeCommit User Guide</i>.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UntagResourceInput} untagResourceInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~untagResourceCallback} callback The callback function, accepting three arguments: error, data, response
     */
    untagResource(xAmzTarget, untagResourceInput, opts, callback) {
      opts = opts || {};
      let postBody = untagResourceInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling untagResource");
      }
      // verify the required parameter 'untagResourceInput' is set
      if (untagResourceInput === undefined || untagResourceInput === null) {
        throw new Error("Missing the required parameter 'untagResourceInput' when calling untagResource");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.UntagResource', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateApprovalRuleTemplateContent operation.
     * @callback module:api/DefaultApi~updateApprovalRuleTemplateContentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateApprovalRuleTemplateContentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates the content of an approval rule template. You can change the number of required approvals, the membership of the approval rule, and whether an approval pool is defined.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateApprovalRuleTemplateContentInput} updateApprovalRuleTemplateContentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateApprovalRuleTemplateContentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateApprovalRuleTemplateContentOutput}
     */
    updateApprovalRuleTemplateContent(xAmzTarget, updateApprovalRuleTemplateContentInput, opts, callback) {
      opts = opts || {};
      let postBody = updateApprovalRuleTemplateContentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateApprovalRuleTemplateContent");
      }
      // verify the required parameter 'updateApprovalRuleTemplateContentInput' is set
      if (updateApprovalRuleTemplateContentInput === undefined || updateApprovalRuleTemplateContentInput === null) {
        throw new Error("Missing the required parameter 'updateApprovalRuleTemplateContentInput' when calling updateApprovalRuleTemplateContent");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateApprovalRuleTemplateContentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.UpdateApprovalRuleTemplateContent', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateApprovalRuleTemplateDescription operation.
     * @callback module:api/DefaultApi~updateApprovalRuleTemplateDescriptionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateApprovalRuleTemplateDescriptionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates the description for a specified approval rule template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateApprovalRuleTemplateDescriptionInput} updateApprovalRuleTemplateDescriptionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateApprovalRuleTemplateDescriptionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateApprovalRuleTemplateDescriptionOutput}
     */
    updateApprovalRuleTemplateDescription(xAmzTarget, updateApprovalRuleTemplateDescriptionInput, opts, callback) {
      opts = opts || {};
      let postBody = updateApprovalRuleTemplateDescriptionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateApprovalRuleTemplateDescription");
      }
      // verify the required parameter 'updateApprovalRuleTemplateDescriptionInput' is set
      if (updateApprovalRuleTemplateDescriptionInput === undefined || updateApprovalRuleTemplateDescriptionInput === null) {
        throw new Error("Missing the required parameter 'updateApprovalRuleTemplateDescriptionInput' when calling updateApprovalRuleTemplateDescription");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateApprovalRuleTemplateDescriptionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.UpdateApprovalRuleTemplateDescription', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateApprovalRuleTemplateName operation.
     * @callback module:api/DefaultApi~updateApprovalRuleTemplateNameCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateApprovalRuleTemplateNameOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates the name of a specified approval rule template.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateApprovalRuleTemplateNameInput} updateApprovalRuleTemplateNameInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateApprovalRuleTemplateNameCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateApprovalRuleTemplateNameOutput}
     */
    updateApprovalRuleTemplateName(xAmzTarget, updateApprovalRuleTemplateNameInput, opts, callback) {
      opts = opts || {};
      let postBody = updateApprovalRuleTemplateNameInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateApprovalRuleTemplateName");
      }
      // verify the required parameter 'updateApprovalRuleTemplateNameInput' is set
      if (updateApprovalRuleTemplateNameInput === undefined || updateApprovalRuleTemplateNameInput === null) {
        throw new Error("Missing the required parameter 'updateApprovalRuleTemplateNameInput' when calling updateApprovalRuleTemplateName");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateApprovalRuleTemplateNameOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.UpdateApprovalRuleTemplateName', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateComment operation.
     * @callback module:api/DefaultApi~updateCommentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateCommentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Replaces the contents of a comment.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateCommentInput} updateCommentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateCommentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateCommentOutput}
     */
    updateComment(xAmzTarget, updateCommentInput, opts, callback) {
      opts = opts || {};
      let postBody = updateCommentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateComment");
      }
      // verify the required parameter 'updateCommentInput' is set
      if (updateCommentInput === undefined || updateCommentInput === null) {
        throw new Error("Missing the required parameter 'updateCommentInput' when calling updateComment");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateCommentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.UpdateComment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateDefaultBranch operation.
     * @callback module:api/DefaultApi~updateDefaultBranchCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Sets or changes the default branch name for the specified repository.</p> <note> <p>If you use this operation to change the default branch name to the current default branch name, a success message is returned even though the default branch did not change.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateDefaultBranchInput} updateDefaultBranchInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateDefaultBranchCallback} callback The callback function, accepting three arguments: error, data, response
     */
    updateDefaultBranch(xAmzTarget, updateDefaultBranchInput, opts, callback) {
      opts = opts || {};
      let postBody = updateDefaultBranchInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateDefaultBranch");
      }
      // verify the required parameter 'updateDefaultBranchInput' is set
      if (updateDefaultBranchInput === undefined || updateDefaultBranchInput === null) {
        throw new Error("Missing the required parameter 'updateDefaultBranchInput' when calling updateDefaultBranch");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.UpdateDefaultBranch', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updatePullRequestApprovalRuleContent operation.
     * @callback module:api/DefaultApi~updatePullRequestApprovalRuleContentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdatePullRequestApprovalRuleContentOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates the structure of an approval rule created specifically for a pull request. For example, you can change the number of required approvers and the approval pool for approvers. 
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdatePullRequestApprovalRuleContentInput} updatePullRequestApprovalRuleContentInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updatePullRequestApprovalRuleContentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdatePullRequestApprovalRuleContentOutput}
     */
    updatePullRequestApprovalRuleContent(xAmzTarget, updatePullRequestApprovalRuleContentInput, opts, callback) {
      opts = opts || {};
      let postBody = updatePullRequestApprovalRuleContentInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updatePullRequestApprovalRuleContent");
      }
      // verify the required parameter 'updatePullRequestApprovalRuleContentInput' is set
      if (updatePullRequestApprovalRuleContentInput === undefined || updatePullRequestApprovalRuleContentInput === null) {
        throw new Error("Missing the required parameter 'updatePullRequestApprovalRuleContentInput' when calling updatePullRequestApprovalRuleContent");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdatePullRequestApprovalRuleContentOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.UpdatePullRequestApprovalRuleContent', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updatePullRequestApprovalState operation.
     * @callback module:api/DefaultApi~updatePullRequestApprovalStateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates the state of a user's approval on a pull request. The user is derived from the signed-in account when the request is made.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdatePullRequestApprovalStateInput} updatePullRequestApprovalStateInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updatePullRequestApprovalStateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    updatePullRequestApprovalState(xAmzTarget, updatePullRequestApprovalStateInput, opts, callback) {
      opts = opts || {};
      let postBody = updatePullRequestApprovalStateInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updatePullRequestApprovalState");
      }
      // verify the required parameter 'updatePullRequestApprovalStateInput' is set
      if (updatePullRequestApprovalStateInput === undefined || updatePullRequestApprovalStateInput === null) {
        throw new Error("Missing the required parameter 'updatePullRequestApprovalStateInput' when calling updatePullRequestApprovalState");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.UpdatePullRequestApprovalState', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updatePullRequestDescription operation.
     * @callback module:api/DefaultApi~updatePullRequestDescriptionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdatePullRequestDescriptionOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Replaces the contents of the description of a pull request.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdatePullRequestDescriptionInput} updatePullRequestDescriptionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updatePullRequestDescriptionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdatePullRequestDescriptionOutput}
     */
    updatePullRequestDescription(xAmzTarget, updatePullRequestDescriptionInput, opts, callback) {
      opts = opts || {};
      let postBody = updatePullRequestDescriptionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updatePullRequestDescription");
      }
      // verify the required parameter 'updatePullRequestDescriptionInput' is set
      if (updatePullRequestDescriptionInput === undefined || updatePullRequestDescriptionInput === null) {
        throw new Error("Missing the required parameter 'updatePullRequestDescriptionInput' when calling updatePullRequestDescription");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdatePullRequestDescriptionOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.UpdatePullRequestDescription', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updatePullRequestStatus operation.
     * @callback module:api/DefaultApi~updatePullRequestStatusCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdatePullRequestStatusOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates the status of a pull request. 
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdatePullRequestStatusInput} updatePullRequestStatusInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updatePullRequestStatusCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdatePullRequestStatusOutput}
     */
    updatePullRequestStatus(xAmzTarget, updatePullRequestStatusInput, opts, callback) {
      opts = opts || {};
      let postBody = updatePullRequestStatusInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updatePullRequestStatus");
      }
      // verify the required parameter 'updatePullRequestStatusInput' is set
      if (updatePullRequestStatusInput === undefined || updatePullRequestStatusInput === null) {
        throw new Error("Missing the required parameter 'updatePullRequestStatusInput' when calling updatePullRequestStatus");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdatePullRequestStatusOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.UpdatePullRequestStatus', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updatePullRequestTitle operation.
     * @callback module:api/DefaultApi~updatePullRequestTitleCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdatePullRequestTitleOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Replaces the title of a pull request.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdatePullRequestTitleInput} updatePullRequestTitleInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updatePullRequestTitleCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdatePullRequestTitleOutput}
     */
    updatePullRequestTitle(xAmzTarget, updatePullRequestTitleInput, opts, callback) {
      opts = opts || {};
      let postBody = updatePullRequestTitleInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updatePullRequestTitle");
      }
      // verify the required parameter 'updatePullRequestTitleInput' is set
      if (updatePullRequestTitleInput === undefined || updatePullRequestTitleInput === null) {
        throw new Error("Missing the required parameter 'updatePullRequestTitleInput' when calling updatePullRequestTitle");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdatePullRequestTitleOutput;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.UpdatePullRequestTitle', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateRepositoryDescription operation.
     * @callback module:api/DefaultApi~updateRepositoryDescriptionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Sets or changes the comment or description for a repository.</p> <note> <p>The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.</p> </note>
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateRepositoryDescriptionInput} updateRepositoryDescriptionInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateRepositoryDescriptionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    updateRepositoryDescription(xAmzTarget, updateRepositoryDescriptionInput, opts, callback) {
      opts = opts || {};
      let postBody = updateRepositoryDescriptionInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateRepositoryDescription");
      }
      // verify the required parameter 'updateRepositoryDescriptionInput' is set
      if (updateRepositoryDescriptionInput === undefined || updateRepositoryDescriptionInput === null) {
        throw new Error("Missing the required parameter 'updateRepositoryDescriptionInput' when calling updateRepositoryDescription");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.UpdateRepositoryDescription', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateRepositoryName operation.
     * @callback module:api/DefaultApi~updateRepositoryNameCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Renames a repository. The repository name must be unique across the calling AWS account. Repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. The suffix .git is prohibited. For more information about the limits on repository names, see <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html\">Limits</a> in the AWS CodeCommit User Guide.
     * @param {module:model/String} xAmzTarget 
     * @param {module:model/UpdateRepositoryNameInput} updateRepositoryNameInput 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateRepositoryNameCallback} callback The callback function, accepting three arguments: error, data, response
     */
    updateRepositoryName(xAmzTarget, updateRepositoryNameInput, opts, callback) {
      opts = opts || {};
      let postBody = updateRepositoryNameInput;
      // verify the required parameter 'xAmzTarget' is set
      if (xAmzTarget === undefined || xAmzTarget === null) {
        throw new Error("Missing the required parameter 'xAmzTarget' when calling updateRepositoryName");
      }
      // verify the required parameter 'updateRepositoryNameInput' is set
      if (updateRepositoryNameInput === undefined || updateRepositoryNameInput === null) {
        throw new Error("Missing the required parameter 'updateRepositoryNameInput' when calling updateRepositoryName");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders'],
        'X-Amz-Target': xAmzTarget
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/#X-Amz-Target=CodeCommit_20150413.UpdateRepositoryName', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
