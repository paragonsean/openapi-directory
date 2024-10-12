/*
 * AWS CodeCommit
 * <fullname>AWS CodeCommit</fullname> <p>This is the <i>AWS CodeCommit API Reference</i>. This reference provides descriptions of the operations and data types for AWS CodeCommit API along with usage examples.</p> <p>You can use the AWS CodeCommit API to work with the following objects:</p> <p>Repositories, by calling the following:</p> <ul> <li> <p> <a>BatchGetRepositories</a>, which returns information about one or more repositories associated with your AWS account.</p> </li> <li> <p> <a>CreateRepository</a>, which creates an AWS CodeCommit repository.</p> </li> <li> <p> <a>DeleteRepository</a>, which deletes an AWS CodeCommit repository.</p> </li> <li> <p> <a>GetRepository</a>, which returns information about a specified repository.</p> </li> <li> <p> <a>ListRepositories</a>, which lists all AWS CodeCommit repositories associated with your AWS account.</p> </li> <li> <p> <a>UpdateRepositoryDescription</a>, which sets or updates the description of the repository.</p> </li> <li> <p> <a>UpdateRepositoryName</a>, which changes the name of the repository. If you change the name of a repository, no other users of that repository can access it until you send them the new HTTPS or SSH URL to use.</p> </li> </ul> <p>Branches, by calling the following:</p> <ul> <li> <p> <a>CreateBranch</a>, which creates a branch in a specified repository.</p> </li> <li> <p> <a>DeleteBranch</a>, which deletes the specified branch in a repository unless it is the default branch.</p> </li> <li> <p> <a>GetBranch</a>, which returns information about a specified branch.</p> </li> <li> <p> <a>ListBranches</a>, which lists all branches for a specified repository.</p> </li> <li> <p> <a>UpdateDefaultBranch</a>, which changes the default branch for a repository.</p> </li> </ul> <p>Files, by calling the following:</p> <ul> <li> <p> <a>DeleteFile</a>, which deletes the content of a specified file from a specified branch.</p> </li> <li> <p> <a>GetBlob</a>, which returns the base-64 encoded content of an individual Git blob object in a repository.</p> </li> <li> <p> <a>GetFile</a>, which returns the base-64 encoded content of a specified file.</p> </li> <li> <p> <a>GetFolder</a>, which returns the contents of a specified folder or directory.</p> </li> <li> <p> <a>PutFile</a>, which adds or modifies a single file in a specified repository and branch.</p> </li> </ul> <p>Commits, by calling the following:</p> <ul> <li> <p> <a>BatchGetCommits</a>, which returns information about one or more commits in a repository.</p> </li> <li> <p> <a>CreateCommit</a>, which creates a commit for changes to a repository.</p> </li> <li> <p> <a>GetCommit</a>, which returns information about a commit, including commit messages and author and committer information.</p> </li> <li> <p> <a>GetDifferences</a>, which returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID, or other fully qualified reference).</p> </li> </ul> <p>Merges, by calling the following:</p> <ul> <li> <p> <a>BatchDescribeMergeConflicts</a>, which returns information about conflicts in a merge between commits in a repository.</p> </li> <li> <p> <a>CreateUnreferencedMergeCommit</a>, which creates an unreferenced commit between two branches or commits for the purpose of comparing them and identifying any potential conflicts.</p> </li> <li> <p> <a>DescribeMergeConflicts</a>, which returns information about merge conflicts between the base, source, and destination versions of a file in a potential merge.</p> </li> <li> <p> <a>GetMergeCommit</a>, which returns information about the merge between a source and destination commit. </p> </li> <li> <p> <a>GetMergeConflicts</a>, which returns information about merge conflicts between the source and destination branch in a pull request.</p> </li> <li> <p> <a>GetMergeOptions</a>, which returns information about the available merge options between two branches or commit specifiers.</p> </li> <li> <p> <a>MergeBranchesByFastForward</a>, which merges two branches using the fast-forward merge option.</p> </li> <li> <p> <a>MergeBranchesBySquash</a>, which merges two branches using the squash merge option.</p> </li> <li> <p> <a>MergeBranchesByThreeWay</a>, which merges two branches using the three-way merge option.</p> </li> </ul> <p>Pull requests, by calling the following:</p> <ul> <li> <p> <a>CreatePullRequest</a>, which creates a pull request in a specified repository.</p> </li> <li> <p> <a>CreatePullRequestApprovalRule</a>, which creates an approval rule for a specified pull request.</p> </li> <li> <p> <a>DeletePullRequestApprovalRule</a>, which deletes an approval rule for a specified pull request.</p> </li> <li> <p> <a>DescribePullRequestEvents</a>, which returns information about one or more pull request events.</p> </li> <li> <p> <a>EvaluatePullRequestApprovalRules</a>, which evaluates whether a pull request has met all the conditions specified in its associated approval rules.</p> </li> <li> <p> <a>GetCommentsForPullRequest</a>, which returns information about comments on a specified pull request.</p> </li> <li> <p> <a>GetPullRequest</a>, which returns information about a specified pull request.</p> </li> <li> <p> <a>GetPullRequestApprovalStates</a>, which returns information about the approval states for a specified pull request.</p> </li> <li> <p> <a>GetPullRequestOverrideState</a>, which returns information about whether approval rules have been set aside (overriden) for a pull request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.</p> </li> <li> <p> <a>ListPullRequests</a>, which lists all pull requests for a repository.</p> </li> <li> <p> <a>MergePullRequestByFastForward</a>, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the fast-forward merge option.</p> </li> <li> <p> <a>MergePullRequestBySquash</a>, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the squash merge option.</p> </li> <li> <p> <a>MergePullRequestByThreeWay</a>. which merges the source destination branch of a pull request into the specified destination branch for that pull request using the three-way merge option.</p> </li> <li> <p> <a>OverridePullRequestApprovalRules</a>, which sets aside all approval rule requirements for a pull request.</p> </li> <li> <p> <a>PostCommentForPullRequest</a>, which posts a comment to a pull request at the specified line, file, or request.</p> </li> <li> <p> <a>UpdatePullRequestApprovalRuleContent</a>, which updates the structure of an approval rule for a pull request.</p> </li> <li> <p> <a>UpdatePullRequestApprovalState</a>, which updates the state of an approval on a pull request.</p> </li> <li> <p> <a>UpdatePullRequestDescription</a>, which updates the description of a pull request.</p> </li> <li> <p> <a>UpdatePullRequestStatus</a>, which updates the status of a pull request.</p> </li> <li> <p> <a>UpdatePullRequestTitle</a>, which updates the title of a pull request.</p> </li> </ul> <p>Approval rule templates, by calling the following:</p> <ul> <li> <p> <a>AssociateApprovalRuleTemplateWithRepository</a>, which associates a template with a specified repository. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repository.</p> </li> <li> <p> <a>BatchAssociateApprovalRuleTemplateWithRepositories</a>, which associates a template with one or more specified repositories. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repositories.</p> </li> <li> <p> <a>BatchDisassociateApprovalRuleTemplateFromRepositories</a>, which removes the association between a template and specified repositories so that approval rules based on the template are not automatically created when pull requests are created in those repositories.</p> </li> <li> <p> <a>CreateApprovalRuleTemplate</a>, which creates a template for approval rules that can then be associated with one or more repositories in your AWS account.</p> </li> <li> <p> <a>DeleteApprovalRuleTemplate</a>, which deletes the specified template. It does not remove approval rules on pull requests already created with the template.</p> </li> <li> <p> <a>DisassociateApprovalRuleTemplateFromRepository</a>, which removes the association between a template and a repository so that approval rules based on the template are not automatically created when pull requests are created in the specified repository.</p> </li> <li> <p> <a>GetApprovalRuleTemplate</a>, which returns information about an approval rule template.</p> </li> <li> <p> <a>ListApprovalRuleTemplates</a>, which lists all approval rule templates in the AWS Region in your AWS account.</p> </li> <li> <p> <a>ListAssociatedApprovalRuleTemplatesForRepository</a>, which lists all approval rule templates that are associated with a specified repository.</p> </li> <li> <p> <a>ListRepositoriesForApprovalRuleTemplate</a>, which lists all repositories associated with the specified approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateDescription</a>, which updates the description of an approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateName</a>, which updates the name of an approval rule template.</p> </li> <li> <p> <a>UpdateApprovalRuleTemplateContent</a>, which updates the content of an approval rule template.</p> </li> </ul> <p>Comments in a repository, by calling the following:</p> <ul> <li> <p> <a>DeleteCommentContent</a>, which deletes the content of a comment on a commit in a repository.</p> </li> <li> <p> <a>GetComment</a>, which returns information about a comment on a commit.</p> </li> <li> <p> <a>GetCommentReactions</a>, which returns information about emoji reactions to comments.</p> </li> <li> <p> <a>GetCommentsForComparedCommit</a>, which returns information about comments on the comparison between two commit specifiers in a repository.</p> </li> <li> <p> <a>PostCommentForComparedCommit</a>, which creates a comment on the comparison between two commit specifiers in a repository.</p> </li> <li> <p> <a>PostCommentReply</a>, which creates a reply to a comment.</p> </li> <li> <p> <a>PutCommentReaction</a>, which creates or updates an emoji reaction to a comment.</p> </li> <li> <p> <a>UpdateComment</a>, which updates the content of a comment on a commit in a repository.</p> </li> </ul> <p>Tags used to tag resources in AWS CodeCommit (not Git tags), by calling the following:</p> <ul> <li> <p> <a>ListTagsForResource</a>, which gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS CodeCommit.</p> </li> <li> <p> <a>TagResource</a>, which adds or updates tags for a resource in AWS CodeCommit.</p> </li> <li> <p> <a>UntagResource</a>, which removes tags for a resource in AWS CodeCommit.</p> </li> </ul> <p>Triggers, by calling the following:</p> <ul> <li> <p> <a>GetRepositoryTriggers</a>, which returns information about triggers configured for a repository.</p> </li> <li> <p> <a>PutRepositoryTriggers</a>, which replaces all triggers for a repository and can be used to create or delete triggers.</p> </li> <li> <p> <a>TestRepositoryTriggers</a>, which tests the functionality of a repository trigger by sending data to the trigger target.</p> </li> </ul> <p>For information about how to use AWS CodeCommit, see the <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html\">AWS CodeCommit User Guide</a>.</p>
 *
 * The version of the OpenAPI document: 2015-04-13
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.AssociateApprovalRuleTemplateWithRepositoryInput;
import org.openapitools.client.model.BatchAssociateApprovalRuleTemplateWithRepositoriesInput;
import org.openapitools.client.model.BatchAssociateApprovalRuleTemplateWithRepositoriesOutput;
import org.openapitools.client.model.BatchDescribeMergeConflictsInput;
import org.openapitools.client.model.BatchDescribeMergeConflictsOutput;
import org.openapitools.client.model.BatchDisassociateApprovalRuleTemplateFromRepositoriesInput;
import org.openapitools.client.model.BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput;
import org.openapitools.client.model.BatchGetCommitsInput;
import org.openapitools.client.model.BatchGetCommitsOutput;
import org.openapitools.client.model.BatchGetRepositoriesInput;
import org.openapitools.client.model.BatchGetRepositoriesOutput;
import org.openapitools.client.model.CreateApprovalRuleTemplateInput;
import org.openapitools.client.model.CreateApprovalRuleTemplateOutput;
import org.openapitools.client.model.CreateBranchInput;
import org.openapitools.client.model.CreateCommitInput;
import org.openapitools.client.model.CreateCommitOutput;
import org.openapitools.client.model.CreatePullRequestApprovalRuleInput;
import org.openapitools.client.model.CreatePullRequestApprovalRuleOutput;
import org.openapitools.client.model.CreatePullRequestInput;
import org.openapitools.client.model.CreatePullRequestOutput;
import org.openapitools.client.model.CreateRepositoryInput;
import org.openapitools.client.model.CreateRepositoryOutput;
import org.openapitools.client.model.CreateUnreferencedMergeCommitInput;
import org.openapitools.client.model.CreateUnreferencedMergeCommitOutput;
import org.openapitools.client.model.DeleteApprovalRuleTemplateInput;
import org.openapitools.client.model.DeleteApprovalRuleTemplateOutput;
import org.openapitools.client.model.DeleteBranchInput;
import org.openapitools.client.model.DeleteBranchOutput;
import org.openapitools.client.model.DeleteCommentContentInput;
import org.openapitools.client.model.DeleteCommentContentOutput;
import org.openapitools.client.model.DeleteFileInput;
import org.openapitools.client.model.DeleteFileOutput;
import org.openapitools.client.model.DeletePullRequestApprovalRuleInput;
import org.openapitools.client.model.DeletePullRequestApprovalRuleOutput;
import org.openapitools.client.model.DeleteRepositoryInput;
import org.openapitools.client.model.DeleteRepositoryOutput;
import org.openapitools.client.model.DescribeMergeConflictsInput;
import org.openapitools.client.model.DescribeMergeConflictsOutput;
import org.openapitools.client.model.DescribePullRequestEventsInput;
import org.openapitools.client.model.DescribePullRequestEventsOutput;
import org.openapitools.client.model.DisassociateApprovalRuleTemplateFromRepositoryInput;
import org.openapitools.client.model.EvaluatePullRequestApprovalRulesInput;
import org.openapitools.client.model.EvaluatePullRequestApprovalRulesOutput;
import org.openapitools.client.model.GetApprovalRuleTemplateInput;
import org.openapitools.client.model.GetApprovalRuleTemplateOutput;
import org.openapitools.client.model.GetBlobInput;
import org.openapitools.client.model.GetBlobOutput;
import org.openapitools.client.model.GetBranchInput;
import org.openapitools.client.model.GetBranchOutput;
import org.openapitools.client.model.GetCommentInput;
import org.openapitools.client.model.GetCommentOutput;
import org.openapitools.client.model.GetCommentReactionsInput;
import org.openapitools.client.model.GetCommentReactionsOutput;
import org.openapitools.client.model.GetCommentsForComparedCommitInput;
import org.openapitools.client.model.GetCommentsForComparedCommitOutput;
import org.openapitools.client.model.GetCommentsForPullRequestInput;
import org.openapitools.client.model.GetCommentsForPullRequestOutput;
import org.openapitools.client.model.GetCommitInput;
import org.openapitools.client.model.GetCommitOutput;
import org.openapitools.client.model.GetDifferencesInput;
import org.openapitools.client.model.GetDifferencesOutput;
import org.openapitools.client.model.GetFileInput;
import org.openapitools.client.model.GetFileOutput;
import org.openapitools.client.model.GetFolderInput;
import org.openapitools.client.model.GetFolderOutput;
import org.openapitools.client.model.GetMergeCommitInput;
import org.openapitools.client.model.GetMergeCommitOutput;
import org.openapitools.client.model.GetMergeConflictsInput;
import org.openapitools.client.model.GetMergeConflictsOutput;
import org.openapitools.client.model.GetMergeOptionsInput;
import org.openapitools.client.model.GetMergeOptionsOutput;
import org.openapitools.client.model.GetPullRequestApprovalStatesInput;
import org.openapitools.client.model.GetPullRequestApprovalStatesOutput;
import org.openapitools.client.model.GetPullRequestInput;
import org.openapitools.client.model.GetPullRequestOutput;
import org.openapitools.client.model.GetPullRequestOverrideStateInput;
import org.openapitools.client.model.GetPullRequestOverrideStateOutput;
import org.openapitools.client.model.GetRepositoryInput;
import org.openapitools.client.model.GetRepositoryOutput;
import org.openapitools.client.model.GetRepositoryTriggersInput;
import org.openapitools.client.model.GetRepositoryTriggersOutput;
import org.openapitools.client.model.ListApprovalRuleTemplatesInput;
import org.openapitools.client.model.ListApprovalRuleTemplatesOutput;
import org.openapitools.client.model.ListAssociatedApprovalRuleTemplatesForRepositoryInput;
import org.openapitools.client.model.ListAssociatedApprovalRuleTemplatesForRepositoryOutput;
import org.openapitools.client.model.ListBranchesInput;
import org.openapitools.client.model.ListBranchesOutput;
import org.openapitools.client.model.ListPullRequestsInput;
import org.openapitools.client.model.ListPullRequestsOutput;
import org.openapitools.client.model.ListRepositoriesForApprovalRuleTemplateInput;
import org.openapitools.client.model.ListRepositoriesForApprovalRuleTemplateOutput;
import org.openapitools.client.model.ListRepositoriesInput;
import org.openapitools.client.model.ListRepositoriesOutput;
import org.openapitools.client.model.ListTagsForResourceInput;
import org.openapitools.client.model.ListTagsForResourceOutput;
import org.openapitools.client.model.MergeBranchesByFastForwardInput;
import org.openapitools.client.model.MergeBranchesByFastForwardOutput;
import org.openapitools.client.model.MergeBranchesBySquashInput;
import org.openapitools.client.model.MergeBranchesBySquashOutput;
import org.openapitools.client.model.MergeBranchesByThreeWayInput;
import org.openapitools.client.model.MergeBranchesByThreeWayOutput;
import org.openapitools.client.model.MergePullRequestByFastForwardInput;
import org.openapitools.client.model.MergePullRequestByFastForwardOutput;
import org.openapitools.client.model.MergePullRequestBySquashInput;
import org.openapitools.client.model.MergePullRequestBySquashOutput;
import org.openapitools.client.model.MergePullRequestByThreeWayInput;
import org.openapitools.client.model.MergePullRequestByThreeWayOutput;
import org.openapitools.client.model.OverridePullRequestApprovalRulesInput;
import org.openapitools.client.model.PostCommentForComparedCommitInput;
import org.openapitools.client.model.PostCommentForComparedCommitOutput;
import org.openapitools.client.model.PostCommentForPullRequestInput;
import org.openapitools.client.model.PostCommentForPullRequestOutput;
import org.openapitools.client.model.PostCommentReplyInput;
import org.openapitools.client.model.PostCommentReplyOutput;
import org.openapitools.client.model.PutCommentReactionInput;
import org.openapitools.client.model.PutFileInput;
import org.openapitools.client.model.PutFileOutput;
import org.openapitools.client.model.PutRepositoryTriggersInput;
import org.openapitools.client.model.PutRepositoryTriggersOutput;
import org.openapitools.client.model.TagResourceInput;
import org.openapitools.client.model.TestRepositoryTriggersInput;
import org.openapitools.client.model.TestRepositoryTriggersOutput;
import org.openapitools.client.model.UntagResourceInput;
import org.openapitools.client.model.UpdateApprovalRuleTemplateContentInput;
import org.openapitools.client.model.UpdateApprovalRuleTemplateContentOutput;
import org.openapitools.client.model.UpdateApprovalRuleTemplateDescriptionInput;
import org.openapitools.client.model.UpdateApprovalRuleTemplateDescriptionOutput;
import org.openapitools.client.model.UpdateApprovalRuleTemplateNameInput;
import org.openapitools.client.model.UpdateApprovalRuleTemplateNameOutput;
import org.openapitools.client.model.UpdateCommentInput;
import org.openapitools.client.model.UpdateCommentOutput;
import org.openapitools.client.model.UpdateDefaultBranchInput;
import org.openapitools.client.model.UpdatePullRequestApprovalRuleContentInput;
import org.openapitools.client.model.UpdatePullRequestApprovalRuleContentOutput;
import org.openapitools.client.model.UpdatePullRequestApprovalStateInput;
import org.openapitools.client.model.UpdatePullRequestDescriptionInput;
import org.openapitools.client.model.UpdatePullRequestDescriptionOutput;
import org.openapitools.client.model.UpdatePullRequestStatusInput;
import org.openapitools.client.model.UpdatePullRequestStatusOutput;
import org.openapitools.client.model.UpdatePullRequestTitleInput;
import org.openapitools.client.model.UpdatePullRequestTitleOutput;
import org.openapitools.client.model.UpdateRepositoryDescriptionInput;
import org.openapitools.client.model.UpdateRepositoryNameInput;
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
     * Creates an association between an approval rule template and a specified repository. Then, the next time a pull request is created in the repository where the destination reference (if specified) matches the destination reference (branch) for the pull request, an approval rule that matches the template conditions is automatically created for that pull request. If no destination references are specified in the template, an approval rule that matches the template contents is created for all pull requests in that repository.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void associateApprovalRuleTemplateWithRepositoryTest() throws ApiException {
        String xAmzTarget = null;
        AssociateApprovalRuleTemplateWithRepositoryInput associateApprovalRuleTemplateWithRepositoryInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.associateApprovalRuleTemplateWithRepository(xAmzTarget, associateApprovalRuleTemplateWithRepositoryInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Creates an association between an approval rule template and one or more specified repositories. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void batchAssociateApprovalRuleTemplateWithRepositoriesTest() throws ApiException {
        String xAmzTarget = null;
        BatchAssociateApprovalRuleTemplateWithRepositoriesInput batchAssociateApprovalRuleTemplateWithRepositoriesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        BatchAssociateApprovalRuleTemplateWithRepositoriesOutput response = api.batchAssociateApprovalRuleTemplateWithRepositories(xAmzTarget, batchAssociateApprovalRuleTemplateWithRepositoriesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns information about one or more merge conflicts in the attempted merge of two commit specifiers using the squash or three-way merge strategy.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void batchDescribeMergeConflictsTest() throws ApiException {
        String xAmzTarget = null;
        BatchDescribeMergeConflictsInput batchDescribeMergeConflictsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        BatchDescribeMergeConflictsOutput response = api.batchDescribeMergeConflicts(xAmzTarget, batchDescribeMergeConflictsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Removes the association between an approval rule template and one or more specified repositories. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void batchDisassociateApprovalRuleTemplateFromRepositoriesTest() throws ApiException {
        String xAmzTarget = null;
        BatchDisassociateApprovalRuleTemplateFromRepositoriesInput batchDisassociateApprovalRuleTemplateFromRepositoriesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput response = api.batchDisassociateApprovalRuleTemplateFromRepositories(xAmzTarget, batchDisassociateApprovalRuleTemplateFromRepositoriesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns information about the contents of one or more commits in a repository.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void batchGetCommitsTest() throws ApiException {
        String xAmzTarget = null;
        BatchGetCommitsInput batchGetCommitsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        BatchGetCommitsOutput response = api.batchGetCommits(xAmzTarget, batchGetCommitsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Returns information about one or more repositories.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void batchGetRepositoriesTest() throws ApiException {
        String xAmzTarget = null;
        BatchGetRepositoriesInput batchGetRepositoriesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        BatchGetRepositoriesOutput response = api.batchGetRepositories(xAmzTarget, batchGetRepositoriesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Creates a template for approval rules that can then be associated with one or more repositories in your AWS account. When you associate a template with a repository, AWS CodeCommit creates an approval rule that matches the conditions of the template for all pull requests that meet the conditions of the template. For more information, see &lt;a&gt;AssociateApprovalRuleTemplateWithRepository&lt;/a&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createApprovalRuleTemplateTest() throws ApiException {
        String xAmzTarget = null;
        CreateApprovalRuleTemplateInput createApprovalRuleTemplateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateApprovalRuleTemplateOutput response = api.createApprovalRuleTemplate(xAmzTarget, createApprovalRuleTemplateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Creates a branch in a repository and points the branch to a commit.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Calling the create branch operation does not set a repository&#39;s default branch. To do this, call the update default branch operation.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createBranchTest() throws ApiException {
        String xAmzTarget = null;
        CreateBranchInput createBranchInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.createBranch(xAmzTarget, createBranchInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Creates a commit for a repository on the tip of a specified branch.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createCommitTest() throws ApiException {
        String xAmzTarget = null;
        CreateCommitInput createCommitInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateCommitOutput response = api.createCommit(xAmzTarget, createCommitInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Creates a pull request in the specified repository.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createPullRequestTest() throws ApiException {
        String xAmzTarget = null;
        CreatePullRequestInput createPullRequestInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreatePullRequestOutput response = api.createPullRequest(xAmzTarget, createPullRequestInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Creates an approval rule for a pull request.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createPullRequestApprovalRuleTest() throws ApiException {
        String xAmzTarget = null;
        CreatePullRequestApprovalRuleInput createPullRequestApprovalRuleInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreatePullRequestApprovalRuleOutput response = api.createPullRequestApprovalRule(xAmzTarget, createPullRequestApprovalRuleInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Creates a new, empty repository.
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
     * &lt;p&gt;Creates an unreferenced commit that represents the result of merging two branches using a specified merge strategy. This can help you determine the outcome of a potential merge. This API cannot be used with the fast-forward merge strategy because that strategy does not create a merge commit.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This unreferenced merge commit can only be accessed using the GetCommit API or through git commands such as git fetch. To retrieve this commit, you must specify its commit ID or otherwise reference it.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createUnreferencedMergeCommitTest() throws ApiException {
        String xAmzTarget = null;
        CreateUnreferencedMergeCommitInput createUnreferencedMergeCommitInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateUnreferencedMergeCommitOutput response = api.createUnreferencedMergeCommit(xAmzTarget, createUnreferencedMergeCommitInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Deletes a specified approval rule template. Deleting a template does not remove approval rules on pull requests already created with the template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteApprovalRuleTemplateTest() throws ApiException {
        String xAmzTarget = null;
        DeleteApprovalRuleTemplateInput deleteApprovalRuleTemplateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteApprovalRuleTemplateOutput response = api.deleteApprovalRuleTemplate(xAmzTarget, deleteApprovalRuleTemplateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Deletes a branch from a repository, unless that branch is the default branch for the repository. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteBranchTest() throws ApiException {
        String xAmzTarget = null;
        DeleteBranchInput deleteBranchInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteBranchOutput response = api.deleteBranch(xAmzTarget, deleteBranchInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Deletes the content of a comment made on a change, file, or commit in a repository.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteCommentContentTest() throws ApiException {
        String xAmzTarget = null;
        DeleteCommentContentInput deleteCommentContentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteCommentContentOutput response = api.deleteCommentContent(xAmzTarget, deleteCommentContentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Deletes a specified file from a specified branch. A commit is created on the branch that contains the revision. The file still exists in the commits earlier to the commit that contains the deletion.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteFileTest() throws ApiException {
        String xAmzTarget = null;
        DeleteFileInput deleteFileInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteFileOutput response = api.deleteFile(xAmzTarget, deleteFileInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Deletes an approval rule from a specified pull request. Approval rules can be deleted from a pull request only if the pull request is open, and if the approval rule was created specifically for a pull request and not generated from an approval rule template associated with the repository where the pull request was created. You cannot delete an approval rule from a merged or closed pull request.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deletePullRequestApprovalRuleTest() throws ApiException {
        String xAmzTarget = null;
        DeletePullRequestApprovalRuleInput deletePullRequestApprovalRuleInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeletePullRequestApprovalRuleOutput response = api.deletePullRequestApprovalRule(xAmzTarget, deletePullRequestApprovalRuleInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Deletes a repository. If a specified repository was already deleted, a null repository ID is returned.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Deleting a repository also deletes all associated objects and metadata. After a repository is deleted, all future push calls to the deleted repository fail.&lt;/p&gt; &lt;/important&gt;
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
     * Returns information about one or more merge conflicts in the attempted merge of two commit specifiers using the squash or three-way merge strategy. If the merge option for the attempted merge is specified as FAST_FORWARD_MERGE, an exception is thrown.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void describeMergeConflictsTest() throws ApiException {
        String xAmzTarget = null;
        DescribeMergeConflictsInput describeMergeConflictsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxMergeHunks = null;
        String nextToken = null;
        DescribeMergeConflictsOutput response = api.describeMergeConflicts(xAmzTarget, describeMergeConflictsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxMergeHunks, nextToken);
        // TODO: test validations
    }

    /**
     * Returns information about one or more pull request events.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void describePullRequestEventsTest() throws ApiException {
        String xAmzTarget = null;
        DescribePullRequestEventsInput describePullRequestEventsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        DescribePullRequestEventsOutput response = api.describePullRequestEvents(xAmzTarget, describePullRequestEventsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Removes the association between a template and a repository so that approval rules based on the template are not automatically created when pull requests are created in the specified repository. This does not delete any approval rules previously created for pull requests through the template association.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void disassociateApprovalRuleTemplateFromRepositoryTest() throws ApiException {
        String xAmzTarget = null;
        DisassociateApprovalRuleTemplateFromRepositoryInput disassociateApprovalRuleTemplateFromRepositoryInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.disassociateApprovalRuleTemplateFromRepository(xAmzTarget, disassociateApprovalRuleTemplateFromRepositoryInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Evaluates whether a pull request has met all the conditions specified in its associated approval rules.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void evaluatePullRequestApprovalRulesTest() throws ApiException {
        String xAmzTarget = null;
        EvaluatePullRequestApprovalRulesInput evaluatePullRequestApprovalRulesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        EvaluatePullRequestApprovalRulesOutput response = api.evaluatePullRequestApprovalRules(xAmzTarget, evaluatePullRequestApprovalRulesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns information about a specified approval rule template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getApprovalRuleTemplateTest() throws ApiException {
        String xAmzTarget = null;
        GetApprovalRuleTemplateInput getApprovalRuleTemplateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetApprovalRuleTemplateOutput response = api.getApprovalRuleTemplate(xAmzTarget, getApprovalRuleTemplateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns the base-64 encoded content of an individual blob in a repository.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getBlobTest() throws ApiException {
        String xAmzTarget = null;
        GetBlobInput getBlobInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetBlobOutput response = api.getBlob(xAmzTarget, getBlobInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns information about a repository branch, including its name and the last commit ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getBranchTest() throws ApiException {
        String xAmzTarget = null;
        GetBranchInput getBranchInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetBranchOutput response = api.getBranch(xAmzTarget, getBranchInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Returns the content of a comment made on a change, file, or commit in a repository. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Reaction counts might include numbers from user identities who were deleted after the reaction was made. For a count of reactions from active identities, use GetCommentReactions.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCommentTest() throws ApiException {
        String xAmzTarget = null;
        GetCommentInput getCommentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetCommentOutput response = api.getComment(xAmzTarget, getCommentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns information about reactions to a specified comment ID. Reactions from users who have been deleted will not be included in the count.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCommentReactionsTest() throws ApiException {
        String xAmzTarget = null;
        GetCommentReactionsInput getCommentReactionsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        GetCommentReactionsOutput response = api.getCommentReactions(xAmzTarget, getCommentReactionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Returns information about comments made on the comparison between two commits.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Reaction counts might include numbers from user identities who were deleted after the reaction was made. For a count of reactions from active identities, use GetCommentReactions.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCommentsForComparedCommitTest() throws ApiException {
        String xAmzTarget = null;
        GetCommentsForComparedCommitInput getCommentsForComparedCommitInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        GetCommentsForComparedCommitOutput response = api.getCommentsForComparedCommit(xAmzTarget, getCommentsForComparedCommitInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Returns comments made on a pull request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Reaction counts might include numbers from user identities who were deleted after the reaction was made. For a count of reactions from active identities, use GetCommentReactions.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCommentsForPullRequestTest() throws ApiException {
        String xAmzTarget = null;
        GetCommentsForPullRequestInput getCommentsForPullRequestInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        GetCommentsForPullRequestOutput response = api.getCommentsForPullRequest(xAmzTarget, getCommentsForPullRequestInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Returns information about a commit, including commit message and committer information.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCommitTest() throws ApiException {
        String xAmzTarget = null;
        GetCommitInput getCommitInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetCommitOutput response = api.getCommit(xAmzTarget, getCommitInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID, or other fully qualified reference). Results can be limited to a specified path.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDifferencesTest() throws ApiException {
        String xAmzTarget = null;
        GetDifferencesInput getDifferencesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        GetDifferencesOutput response = api.getDifferences(xAmzTarget, getDifferencesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Returns the base-64 encoded contents of a specified file and its metadata.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getFileTest() throws ApiException {
        String xAmzTarget = null;
        GetFileInput getFileInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetFileOutput response = api.getFile(xAmzTarget, getFileInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns the contents of a specified folder in a repository.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getFolderTest() throws ApiException {
        String xAmzTarget = null;
        GetFolderInput getFolderInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetFolderOutput response = api.getFolder(xAmzTarget, getFolderInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns information about a specified merge commit.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getMergeCommitTest() throws ApiException {
        String xAmzTarget = null;
        GetMergeCommitInput getMergeCommitInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetMergeCommitOutput response = api.getMergeCommit(xAmzTarget, getMergeCommitInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns information about merge conflicts between the before and after commit IDs for a pull request in a repository.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getMergeConflictsTest() throws ApiException {
        String xAmzTarget = null;
        GetMergeConflictsInput getMergeConflictsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxConflictFiles = null;
        String nextToken = null;
        GetMergeConflictsOutput response = api.getMergeConflicts(xAmzTarget, getMergeConflictsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxConflictFiles, nextToken);
        // TODO: test validations
    }

    /**
     * Returns information about the merge options available for merging two specified branches. For details about why a merge option is not available, use GetMergeConflicts or DescribeMergeConflicts.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getMergeOptionsTest() throws ApiException {
        String xAmzTarget = null;
        GetMergeOptionsInput getMergeOptionsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetMergeOptionsOutput response = api.getMergeOptions(xAmzTarget, getMergeOptionsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Gets information about a pull request in a specified repository.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPullRequestTest() throws ApiException {
        String xAmzTarget = null;
        GetPullRequestInput getPullRequestInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetPullRequestOutput response = api.getPullRequest(xAmzTarget, getPullRequestInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Gets information about the approval states for a specified pull request. Approval states only apply to pull requests that have one or more approval rules applied to them.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPullRequestApprovalStatesTest() throws ApiException {
        String xAmzTarget = null;
        GetPullRequestApprovalStatesInput getPullRequestApprovalStatesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetPullRequestApprovalStatesOutput response = api.getPullRequestApprovalStates(xAmzTarget, getPullRequestApprovalStatesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns information about whether approval rules have been set aside (overridden) for a pull request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPullRequestOverrideStateTest() throws ApiException {
        String xAmzTarget = null;
        GetPullRequestOverrideStateInput getPullRequestOverrideStateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetPullRequestOverrideStateOutput response = api.getPullRequestOverrideState(xAmzTarget, getPullRequestOverrideStateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Returns information about a repository.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.&lt;/p&gt; &lt;/note&gt;
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
     * Gets information about triggers configured for a repository.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getRepositoryTriggersTest() throws ApiException {
        String xAmzTarget = null;
        GetRepositoryTriggersInput getRepositoryTriggersInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetRepositoryTriggersOutput response = api.getRepositoryTriggers(xAmzTarget, getRepositoryTriggersInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Lists all approval rule templates in the specified AWS Region in your AWS account. If an AWS Region is not specified, the AWS Region where you are signed in is used.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listApprovalRuleTemplatesTest() throws ApiException {
        String xAmzTarget = null;
        ListApprovalRuleTemplatesInput listApprovalRuleTemplatesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListApprovalRuleTemplatesOutput response = api.listApprovalRuleTemplates(xAmzTarget, listApprovalRuleTemplatesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Lists all approval rule templates that are associated with a specified repository.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listAssociatedApprovalRuleTemplatesForRepositoryTest() throws ApiException {
        String xAmzTarget = null;
        ListAssociatedApprovalRuleTemplatesForRepositoryInput listAssociatedApprovalRuleTemplatesForRepositoryInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListAssociatedApprovalRuleTemplatesForRepositoryOutput response = api.listAssociatedApprovalRuleTemplatesForRepository(xAmzTarget, listAssociatedApprovalRuleTemplatesForRepositoryInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets information about one or more branches in a repository.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listBranchesTest() throws ApiException {
        String xAmzTarget = null;
        ListBranchesInput listBranchesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String nextToken = null;
        ListBranchesOutput response = api.listBranches(xAmzTarget, listBranchesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken);
        // TODO: test validations
    }

    /**
     * Returns a list of pull requests for a specified repository. The return list can be refined by pull request status or pull request author ARN.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listPullRequestsTest() throws ApiException {
        String xAmzTarget = null;
        ListPullRequestsInput listPullRequestsInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListPullRequestsOutput response = api.listPullRequests(xAmzTarget, listPullRequestsInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets information about one or more repositories.
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
        String nextToken = null;
        ListRepositoriesOutput response = api.listRepositories(xAmzTarget, listRepositoriesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken);
        // TODO: test validations
    }

    /**
     * Lists all repositories associated with the specified approval rule template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listRepositoriesForApprovalRuleTemplateTest() throws ApiException {
        String xAmzTarget = null;
        ListRepositoriesForApprovalRuleTemplateInput listRepositoriesForApprovalRuleTemplateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListRepositoriesForApprovalRuleTemplateOutput response = api.listRepositoriesForApprovalRuleTemplate(xAmzTarget, listRepositoriesForApprovalRuleTemplateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS CodeCommit. For a list of valid resources in AWS CodeCommit, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats\&quot;&gt;CodeCommit Resources and Operations&lt;/a&gt; in the&lt;i&gt; AWS CodeCommit User Guide&lt;/i&gt;.
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
        ListTagsForResourceOutput response = api.listTagsForResource(xAmzTarget, listTagsForResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Merges two branches using the fast-forward merge strategy.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void mergeBranchesByFastForwardTest() throws ApiException {
        String xAmzTarget = null;
        MergeBranchesByFastForwardInput mergeBranchesByFastForwardInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        MergeBranchesByFastForwardOutput response = api.mergeBranchesByFastForward(xAmzTarget, mergeBranchesByFastForwardInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Merges two branches using the squash merge strategy.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void mergeBranchesBySquashTest() throws ApiException {
        String xAmzTarget = null;
        MergeBranchesBySquashInput mergeBranchesBySquashInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        MergeBranchesBySquashOutput response = api.mergeBranchesBySquash(xAmzTarget, mergeBranchesBySquashInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Merges two specified branches using the three-way merge strategy.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void mergeBranchesByThreeWayTest() throws ApiException {
        String xAmzTarget = null;
        MergeBranchesByThreeWayInput mergeBranchesByThreeWayInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        MergeBranchesByThreeWayOutput response = api.mergeBranchesByThreeWay(xAmzTarget, mergeBranchesByThreeWayInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the fast-forward merge strategy. If the merge is successful, it closes the pull request.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void mergePullRequestByFastForwardTest() throws ApiException {
        String xAmzTarget = null;
        MergePullRequestByFastForwardInput mergePullRequestByFastForwardInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        MergePullRequestByFastForwardOutput response = api.mergePullRequestByFastForward(xAmzTarget, mergePullRequestByFastForwardInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the squash merge strategy. If the merge is successful, it closes the pull request.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void mergePullRequestBySquashTest() throws ApiException {
        String xAmzTarget = null;
        MergePullRequestBySquashInput mergePullRequestBySquashInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        MergePullRequestBySquashOutput response = api.mergePullRequestBySquash(xAmzTarget, mergePullRequestBySquashInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the three-way merge strategy. If the merge is successful, it closes the pull request.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void mergePullRequestByThreeWayTest() throws ApiException {
        String xAmzTarget = null;
        MergePullRequestByThreeWayInput mergePullRequestByThreeWayInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        MergePullRequestByThreeWayOutput response = api.mergePullRequestByThreeWay(xAmzTarget, mergePullRequestByThreeWayInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Sets aside (overrides) all approval rule requirements for a specified pull request.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void overridePullRequestApprovalRulesTest() throws ApiException {
        String xAmzTarget = null;
        OverridePullRequestApprovalRulesInput overridePullRequestApprovalRulesInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.overridePullRequestApprovalRules(xAmzTarget, overridePullRequestApprovalRulesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Posts a comment on the comparison between two commits.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postCommentForComparedCommitTest() throws ApiException {
        String xAmzTarget = null;
        PostCommentForComparedCommitInput postCommentForComparedCommitInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        PostCommentForComparedCommitOutput response = api.postCommentForComparedCommit(xAmzTarget, postCommentForComparedCommitInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Posts a comment on a pull request.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postCommentForPullRequestTest() throws ApiException {
        String xAmzTarget = null;
        PostCommentForPullRequestInput postCommentForPullRequestInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        PostCommentForPullRequestOutput response = api.postCommentForPullRequest(xAmzTarget, postCommentForPullRequestInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Posts a comment in reply to an existing comment on a comparison between commits or a pull request.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postCommentReplyTest() throws ApiException {
        String xAmzTarget = null;
        PostCommentReplyInput postCommentReplyInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        PostCommentReplyOutput response = api.postCommentReply(xAmzTarget, postCommentReplyInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Adds or updates a reaction to a specified comment for the user whose identity is used to make the request. You can only add or update a reaction for yourself. You cannot add, modify, or delete a reaction for another user.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putCommentReactionTest() throws ApiException {
        String xAmzTarget = null;
        PutCommentReactionInput putCommentReactionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.putCommentReaction(xAmzTarget, putCommentReactionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Adds or updates a file in a branch in an AWS CodeCommit repository, and generates a commit for the addition in the specified branch.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putFileTest() throws ApiException {
        String xAmzTarget = null;
        PutFileInput putFileInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        PutFileOutput response = api.putFile(xAmzTarget, putFileInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Replaces all triggers for a repository. Used to create or delete triggers.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putRepositoryTriggersTest() throws ApiException {
        String xAmzTarget = null;
        PutRepositoryTriggersInput putRepositoryTriggersInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        PutRepositoryTriggersOutput response = api.putRepositoryTriggers(xAmzTarget, putRepositoryTriggersInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Adds or updates tags for a resource in AWS CodeCommit. For a list of valid resources in AWS CodeCommit, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats\&quot;&gt;CodeCommit Resources and Operations&lt;/a&gt; in the &lt;i&gt;AWS CodeCommit User Guide&lt;/i&gt;.
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
        api.tagResource(xAmzTarget, tagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Tests the functionality of repository triggers by sending information to the trigger target. If real data is available in the repository, the test sends data from the last commit. If no data is available, sample data is generated.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void testRepositoryTriggersTest() throws ApiException {
        String xAmzTarget = null;
        TestRepositoryTriggersInput testRepositoryTriggersInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        TestRepositoryTriggersOutput response = api.testRepositoryTriggers(xAmzTarget, testRepositoryTriggersInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Removes tags for a resource in AWS CodeCommit. For a list of valid resources in AWS CodeCommit, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats\&quot;&gt;CodeCommit Resources and Operations&lt;/a&gt; in the &lt;i&gt;AWS CodeCommit User Guide&lt;/i&gt;.
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
        api.untagResource(xAmzTarget, untagResourceInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Updates the content of an approval rule template. You can change the number of required approvals, the membership of the approval rule, and whether an approval pool is defined.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateApprovalRuleTemplateContentTest() throws ApiException {
        String xAmzTarget = null;
        UpdateApprovalRuleTemplateContentInput updateApprovalRuleTemplateContentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateApprovalRuleTemplateContentOutput response = api.updateApprovalRuleTemplateContent(xAmzTarget, updateApprovalRuleTemplateContentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Updates the description for a specified approval rule template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateApprovalRuleTemplateDescriptionTest() throws ApiException {
        String xAmzTarget = null;
        UpdateApprovalRuleTemplateDescriptionInput updateApprovalRuleTemplateDescriptionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateApprovalRuleTemplateDescriptionOutput response = api.updateApprovalRuleTemplateDescription(xAmzTarget, updateApprovalRuleTemplateDescriptionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Updates the name of a specified approval rule template.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateApprovalRuleTemplateNameTest() throws ApiException {
        String xAmzTarget = null;
        UpdateApprovalRuleTemplateNameInput updateApprovalRuleTemplateNameInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateApprovalRuleTemplateNameOutput response = api.updateApprovalRuleTemplateName(xAmzTarget, updateApprovalRuleTemplateNameInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Replaces the contents of a comment.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateCommentTest() throws ApiException {
        String xAmzTarget = null;
        UpdateCommentInput updateCommentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateCommentOutput response = api.updateComment(xAmzTarget, updateCommentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Sets or changes the default branch name for the specified repository.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you use this operation to change the default branch name to the current default branch name, a success message is returned even though the default branch did not change.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateDefaultBranchTest() throws ApiException {
        String xAmzTarget = null;
        UpdateDefaultBranchInput updateDefaultBranchInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.updateDefaultBranch(xAmzTarget, updateDefaultBranchInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Updates the structure of an approval rule created specifically for a pull request. For example, you can change the number of required approvers and the approval pool for approvers. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updatePullRequestApprovalRuleContentTest() throws ApiException {
        String xAmzTarget = null;
        UpdatePullRequestApprovalRuleContentInput updatePullRequestApprovalRuleContentInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdatePullRequestApprovalRuleContentOutput response = api.updatePullRequestApprovalRuleContent(xAmzTarget, updatePullRequestApprovalRuleContentInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Updates the state of a user&#39;s approval on a pull request. The user is derived from the signed-in account when the request is made.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updatePullRequestApprovalStateTest() throws ApiException {
        String xAmzTarget = null;
        UpdatePullRequestApprovalStateInput updatePullRequestApprovalStateInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.updatePullRequestApprovalState(xAmzTarget, updatePullRequestApprovalStateInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Replaces the contents of the description of a pull request.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updatePullRequestDescriptionTest() throws ApiException {
        String xAmzTarget = null;
        UpdatePullRequestDescriptionInput updatePullRequestDescriptionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdatePullRequestDescriptionOutput response = api.updatePullRequestDescription(xAmzTarget, updatePullRequestDescriptionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Updates the status of a pull request. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updatePullRequestStatusTest() throws ApiException {
        String xAmzTarget = null;
        UpdatePullRequestStatusInput updatePullRequestStatusInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdatePullRequestStatusOutput response = api.updatePullRequestStatus(xAmzTarget, updatePullRequestStatusInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Replaces the title of a pull request.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updatePullRequestTitleTest() throws ApiException {
        String xAmzTarget = null;
        UpdatePullRequestTitleInput updatePullRequestTitleInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdatePullRequestTitleOutput response = api.updatePullRequestTitle(xAmzTarget, updatePullRequestTitleInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Sets or changes the comment or description for a repository.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateRepositoryDescriptionTest() throws ApiException {
        String xAmzTarget = null;
        UpdateRepositoryDescriptionInput updateRepositoryDescriptionInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.updateRepositoryDescription(xAmzTarget, updateRepositoryDescriptionInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Renames a repository. The repository name must be unique across the calling AWS account. Repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. The suffix .git is prohibited. For more information about the limits on repository names, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html\&quot;&gt;Limits&lt;/a&gt; in the AWS CodeCommit User Guide.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateRepositoryNameTest() throws ApiException {
        String xAmzTarget = null;
        UpdateRepositoryNameInput updateRepositoryNameInput = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.updateRepositoryName(xAmzTarget, updateRepositoryNameInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

}
