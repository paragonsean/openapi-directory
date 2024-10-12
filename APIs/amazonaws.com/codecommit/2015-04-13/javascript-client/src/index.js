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


import ApiClient from './ApiClient';
import Approval from './model/Approval';
import ApprovalRule from './model/ApprovalRule';
import ApprovalRuleEventMetadata from './model/ApprovalRuleEventMetadata';
import ApprovalRuleOriginApprovalRuleTemplate from './model/ApprovalRuleOriginApprovalRuleTemplate';
import ApprovalRuleOverriddenEventMetadata from './model/ApprovalRuleOverriddenEventMetadata';
import ApprovalRuleTemplate from './model/ApprovalRuleTemplate';
import ApprovalState from './model/ApprovalState';
import ApprovalStateChangedEventMetadata from './model/ApprovalStateChangedEventMetadata';
import AssociateApprovalRuleTemplateWithRepositoryInput from './model/AssociateApprovalRuleTemplateWithRepositoryInput';
import BatchAssociateApprovalRuleTemplateWithRepositoriesError from './model/BatchAssociateApprovalRuleTemplateWithRepositoriesError';
import BatchAssociateApprovalRuleTemplateWithRepositoriesInput from './model/BatchAssociateApprovalRuleTemplateWithRepositoriesInput';
import BatchAssociateApprovalRuleTemplateWithRepositoriesOutput from './model/BatchAssociateApprovalRuleTemplateWithRepositoriesOutput';
import BatchDescribeMergeConflictsError from './model/BatchDescribeMergeConflictsError';
import BatchDescribeMergeConflictsInput from './model/BatchDescribeMergeConflictsInput';
import BatchDescribeMergeConflictsOutput from './model/BatchDescribeMergeConflictsOutput';
import BatchDisassociateApprovalRuleTemplateFromRepositoriesError from './model/BatchDisassociateApprovalRuleTemplateFromRepositoriesError';
import BatchDisassociateApprovalRuleTemplateFromRepositoriesInput from './model/BatchDisassociateApprovalRuleTemplateFromRepositoriesInput';
import BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput from './model/BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput';
import BatchGetCommitsError from './model/BatchGetCommitsError';
import BatchGetCommitsInput from './model/BatchGetCommitsInput';
import BatchGetCommitsOutput from './model/BatchGetCommitsOutput';
import BatchGetRepositoriesInput from './model/BatchGetRepositoriesInput';
import BatchGetRepositoriesOutput from './model/BatchGetRepositoriesOutput';
import BlobMetadata from './model/BlobMetadata';
import BranchInfo from './model/BranchInfo';
import ChangeTypeEnum from './model/ChangeTypeEnum';
import Comment from './model/Comment';
import CommentsForComparedCommit from './model/CommentsForComparedCommit';
import CommentsForComparedCommitLocation from './model/CommentsForComparedCommitLocation';
import CommentsForPullRequest from './model/CommentsForPullRequest';
import CommentsForPullRequestLocation from './model/CommentsForPullRequestLocation';
import Commit from './model/Commit';
import CommitAuthor from './model/CommitAuthor';
import CommitCommitter from './model/CommitCommitter';
import Conflict from './model/Conflict';
import ConflictConflictMetadata from './model/ConflictConflictMetadata';
import ConflictDetailLevelTypeEnum from './model/ConflictDetailLevelTypeEnum';
import ConflictMetadata from './model/ConflictMetadata';
import ConflictMetadataFileModes from './model/ConflictMetadataFileModes';
import ConflictMetadataFileSizes from './model/ConflictMetadataFileSizes';
import ConflictMetadataIsBinaryFile from './model/ConflictMetadataIsBinaryFile';
import ConflictMetadataMergeOperations from './model/ConflictMetadataMergeOperations';
import ConflictMetadataObjectTypes from './model/ConflictMetadataObjectTypes';
import ConflictResolution from './model/ConflictResolution';
import ConflictResolutionStrategyTypeEnum from './model/ConflictResolutionStrategyTypeEnum';
import CreateApprovalRuleTemplateInput from './model/CreateApprovalRuleTemplateInput';
import CreateApprovalRuleTemplateOutput from './model/CreateApprovalRuleTemplateOutput';
import CreateApprovalRuleTemplateOutputApprovalRuleTemplate from './model/CreateApprovalRuleTemplateOutputApprovalRuleTemplate';
import CreateBranchInput from './model/CreateBranchInput';
import CreateCommitInput from './model/CreateCommitInput';
import CreateCommitOutput from './model/CreateCommitOutput';
import CreatePullRequestApprovalRuleInput from './model/CreatePullRequestApprovalRuleInput';
import CreatePullRequestApprovalRuleOutput from './model/CreatePullRequestApprovalRuleOutput';
import CreatePullRequestApprovalRuleOutputApprovalRule from './model/CreatePullRequestApprovalRuleOutputApprovalRule';
import CreatePullRequestInput from './model/CreatePullRequestInput';
import CreatePullRequestOutput from './model/CreatePullRequestOutput';
import CreatePullRequestOutputPullRequest from './model/CreatePullRequestOutputPullRequest';
import CreateRepositoryInput from './model/CreateRepositoryInput';
import CreateRepositoryOutput from './model/CreateRepositoryOutput';
import CreateRepositoryOutputRepositoryMetadata from './model/CreateRepositoryOutputRepositoryMetadata';
import CreateUnreferencedMergeCommitInput from './model/CreateUnreferencedMergeCommitInput';
import CreateUnreferencedMergeCommitInputConflictResolution from './model/CreateUnreferencedMergeCommitInputConflictResolution';
import CreateUnreferencedMergeCommitOutput from './model/CreateUnreferencedMergeCommitOutput';
import DeleteApprovalRuleTemplateInput from './model/DeleteApprovalRuleTemplateInput';
import DeleteApprovalRuleTemplateOutput from './model/DeleteApprovalRuleTemplateOutput';
import DeleteBranchInput from './model/DeleteBranchInput';
import DeleteBranchOutput from './model/DeleteBranchOutput';
import DeleteBranchOutputDeletedBranch from './model/DeleteBranchOutputDeletedBranch';
import DeleteCommentContentInput from './model/DeleteCommentContentInput';
import DeleteCommentContentOutput from './model/DeleteCommentContentOutput';
import DeleteCommentContentOutputComment from './model/DeleteCommentContentOutputComment';
import DeleteFileEntry from './model/DeleteFileEntry';
import DeleteFileInput from './model/DeleteFileInput';
import DeleteFileOutput from './model/DeleteFileOutput';
import DeletePullRequestApprovalRuleInput from './model/DeletePullRequestApprovalRuleInput';
import DeletePullRequestApprovalRuleOutput from './model/DeletePullRequestApprovalRuleOutput';
import DeleteRepositoryInput from './model/DeleteRepositoryInput';
import DeleteRepositoryOutput from './model/DeleteRepositoryOutput';
import DescribeMergeConflictsInput from './model/DescribeMergeConflictsInput';
import DescribeMergeConflictsOutput from './model/DescribeMergeConflictsOutput';
import DescribeMergeConflictsOutputConflictMetadata from './model/DescribeMergeConflictsOutputConflictMetadata';
import DescribePullRequestEventsInput from './model/DescribePullRequestEventsInput';
import DescribePullRequestEventsOutput from './model/DescribePullRequestEventsOutput';
import Difference from './model/Difference';
import DifferenceAfterBlob from './model/DifferenceAfterBlob';
import DifferenceBeforeBlob from './model/DifferenceBeforeBlob';
import DisassociateApprovalRuleTemplateFromRepositoryInput from './model/DisassociateApprovalRuleTemplateFromRepositoryInput';
import EvaluatePullRequestApprovalRulesInput from './model/EvaluatePullRequestApprovalRulesInput';
import EvaluatePullRequestApprovalRulesOutput from './model/EvaluatePullRequestApprovalRulesOutput';
import EvaluatePullRequestApprovalRulesOutputEvaluation from './model/EvaluatePullRequestApprovalRulesOutputEvaluation';
import Evaluation from './model/Evaluation';
import File from './model/File';
import FileMetadata from './model/FileMetadata';
import FileModeTypeEnum from './model/FileModeTypeEnum';
import FileModes from './model/FileModes';
import FileSizes from './model/FileSizes';
import Folder from './model/Folder';
import GetApprovalRuleTemplateInput from './model/GetApprovalRuleTemplateInput';
import GetApprovalRuleTemplateOutput from './model/GetApprovalRuleTemplateOutput';
import GetApprovalRuleTemplateOutputApprovalRuleTemplate from './model/GetApprovalRuleTemplateOutputApprovalRuleTemplate';
import GetBlobInput from './model/GetBlobInput';
import GetBlobOutput from './model/GetBlobOutput';
import GetBranchInput from './model/GetBranchInput';
import GetBranchOutput from './model/GetBranchOutput';
import GetBranchOutputBranch from './model/GetBranchOutputBranch';
import GetCommentInput from './model/GetCommentInput';
import GetCommentOutput from './model/GetCommentOutput';
import GetCommentOutputComment from './model/GetCommentOutputComment';
import GetCommentReactionsInput from './model/GetCommentReactionsInput';
import GetCommentReactionsOutput from './model/GetCommentReactionsOutput';
import GetCommentsForComparedCommitInput from './model/GetCommentsForComparedCommitInput';
import GetCommentsForComparedCommitOutput from './model/GetCommentsForComparedCommitOutput';
import GetCommentsForPullRequestInput from './model/GetCommentsForPullRequestInput';
import GetCommentsForPullRequestOutput from './model/GetCommentsForPullRequestOutput';
import GetCommitInput from './model/GetCommitInput';
import GetCommitOutput from './model/GetCommitOutput';
import GetCommitOutputCommit from './model/GetCommitOutputCommit';
import GetDifferencesInput from './model/GetDifferencesInput';
import GetDifferencesOutput from './model/GetDifferencesOutput';
import GetFileInput from './model/GetFileInput';
import GetFileOutput from './model/GetFileOutput';
import GetFolderInput from './model/GetFolderInput';
import GetFolderOutput from './model/GetFolderOutput';
import GetMergeCommitInput from './model/GetMergeCommitInput';
import GetMergeCommitOutput from './model/GetMergeCommitOutput';
import GetMergeConflictsInput from './model/GetMergeConflictsInput';
import GetMergeConflictsOutput from './model/GetMergeConflictsOutput';
import GetMergeOptionsInput from './model/GetMergeOptionsInput';
import GetMergeOptionsOutput from './model/GetMergeOptionsOutput';
import GetPullRequestApprovalStatesInput from './model/GetPullRequestApprovalStatesInput';
import GetPullRequestApprovalStatesOutput from './model/GetPullRequestApprovalStatesOutput';
import GetPullRequestInput from './model/GetPullRequestInput';
import GetPullRequestOutput from './model/GetPullRequestOutput';
import GetPullRequestOutputPullRequest from './model/GetPullRequestOutputPullRequest';
import GetPullRequestOverrideStateInput from './model/GetPullRequestOverrideStateInput';
import GetPullRequestOverrideStateOutput from './model/GetPullRequestOverrideStateOutput';
import GetRepositoryInput from './model/GetRepositoryInput';
import GetRepositoryOutput from './model/GetRepositoryOutput';
import GetRepositoryOutputRepositoryMetadata from './model/GetRepositoryOutputRepositoryMetadata';
import GetRepositoryTriggersInput from './model/GetRepositoryTriggersInput';
import GetRepositoryTriggersOutput from './model/GetRepositoryTriggersOutput';
import IsBinaryFile from './model/IsBinaryFile';
import ListApprovalRuleTemplatesInput from './model/ListApprovalRuleTemplatesInput';
import ListApprovalRuleTemplatesOutput from './model/ListApprovalRuleTemplatesOutput';
import ListAssociatedApprovalRuleTemplatesForRepositoryInput from './model/ListAssociatedApprovalRuleTemplatesForRepositoryInput';
import ListAssociatedApprovalRuleTemplatesForRepositoryOutput from './model/ListAssociatedApprovalRuleTemplatesForRepositoryOutput';
import ListBranchesInput from './model/ListBranchesInput';
import ListBranchesOutput from './model/ListBranchesOutput';
import ListPullRequestsInput from './model/ListPullRequestsInput';
import ListPullRequestsOutput from './model/ListPullRequestsOutput';
import ListRepositoriesForApprovalRuleTemplateInput from './model/ListRepositoriesForApprovalRuleTemplateInput';
import ListRepositoriesForApprovalRuleTemplateOutput from './model/ListRepositoriesForApprovalRuleTemplateOutput';
import ListRepositoriesInput from './model/ListRepositoriesInput';
import ListRepositoriesOutput from './model/ListRepositoriesOutput';
import ListTagsForResourceInput from './model/ListTagsForResourceInput';
import ListTagsForResourceOutput from './model/ListTagsForResourceOutput';
import Location from './model/Location';
import MergeBranchesByFastForwardInput from './model/MergeBranchesByFastForwardInput';
import MergeBranchesByFastForwardOutput from './model/MergeBranchesByFastForwardOutput';
import MergeBranchesBySquashInput from './model/MergeBranchesBySquashInput';
import MergeBranchesBySquashOutput from './model/MergeBranchesBySquashOutput';
import MergeBranchesByThreeWayInput from './model/MergeBranchesByThreeWayInput';
import MergeBranchesByThreeWayOutput from './model/MergeBranchesByThreeWayOutput';
import MergeHunk from './model/MergeHunk';
import MergeHunkBase from './model/MergeHunkBase';
import MergeHunkDestination from './model/MergeHunkDestination';
import MergeHunkDetail from './model/MergeHunkDetail';
import MergeHunkSource from './model/MergeHunkSource';
import MergeMetadata from './model/MergeMetadata';
import MergeOperations from './model/MergeOperations';
import MergeOptionTypeEnum from './model/MergeOptionTypeEnum';
import MergePullRequestByFastForwardInput from './model/MergePullRequestByFastForwardInput';
import MergePullRequestByFastForwardOutput from './model/MergePullRequestByFastForwardOutput';
import MergePullRequestByFastForwardOutputPullRequest from './model/MergePullRequestByFastForwardOutputPullRequest';
import MergePullRequestBySquashInput from './model/MergePullRequestBySquashInput';
import MergePullRequestBySquashOutput from './model/MergePullRequestBySquashOutput';
import MergePullRequestByThreeWayInput from './model/MergePullRequestByThreeWayInput';
import MergePullRequestByThreeWayOutput from './model/MergePullRequestByThreeWayOutput';
import ObjectTypeEnum from './model/ObjectTypeEnum';
import ObjectTypes from './model/ObjectTypes';
import OrderEnum from './model/OrderEnum';
import OriginApprovalRuleTemplate from './model/OriginApprovalRuleTemplate';
import OverridePullRequestApprovalRulesInput from './model/OverridePullRequestApprovalRulesInput';
import OverrideStatus from './model/OverrideStatus';
import PostCommentForComparedCommitInput from './model/PostCommentForComparedCommitInput';
import PostCommentForComparedCommitInputLocation from './model/PostCommentForComparedCommitInputLocation';
import PostCommentForComparedCommitOutput from './model/PostCommentForComparedCommitOutput';
import PostCommentForComparedCommitOutputComment from './model/PostCommentForComparedCommitOutputComment';
import PostCommentForComparedCommitOutputLocation from './model/PostCommentForComparedCommitOutputLocation';
import PostCommentForPullRequestInput from './model/PostCommentForPullRequestInput';
import PostCommentForPullRequestInputLocation from './model/PostCommentForPullRequestInputLocation';
import PostCommentForPullRequestOutput from './model/PostCommentForPullRequestOutput';
import PostCommentForPullRequestOutputLocation from './model/PostCommentForPullRequestOutputLocation';
import PostCommentReplyInput from './model/PostCommentReplyInput';
import PostCommentReplyOutput from './model/PostCommentReplyOutput';
import PostCommentReplyOutputComment from './model/PostCommentReplyOutputComment';
import PullRequest from './model/PullRequest';
import PullRequestCreatedEventMetadata from './model/PullRequestCreatedEventMetadata';
import PullRequestEvent from './model/PullRequestEvent';
import PullRequestEventApprovalRuleEventMetadata from './model/PullRequestEventApprovalRuleEventMetadata';
import PullRequestEventApprovalRuleOverriddenEventMetadata from './model/PullRequestEventApprovalRuleOverriddenEventMetadata';
import PullRequestEventApprovalStateChangedEventMetadata from './model/PullRequestEventApprovalStateChangedEventMetadata';
import PullRequestEventPullRequestCreatedEventMetadata from './model/PullRequestEventPullRequestCreatedEventMetadata';
import PullRequestEventPullRequestMergedStateChangedEventMetadata from './model/PullRequestEventPullRequestMergedStateChangedEventMetadata';
import PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata from './model/PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata';
import PullRequestEventPullRequestStatusChangedEventMetadata from './model/PullRequestEventPullRequestStatusChangedEventMetadata';
import PullRequestEventType from './model/PullRequestEventType';
import PullRequestMergedStateChangedEventMetadata from './model/PullRequestMergedStateChangedEventMetadata';
import PullRequestMergedStateChangedEventMetadataMergeMetadata from './model/PullRequestMergedStateChangedEventMetadataMergeMetadata';
import PullRequestSourceReferenceUpdatedEventMetadata from './model/PullRequestSourceReferenceUpdatedEventMetadata';
import PullRequestStatusChangedEventMetadata from './model/PullRequestStatusChangedEventMetadata';
import PullRequestStatusEnum from './model/PullRequestStatusEnum';
import PullRequestTarget from './model/PullRequestTarget';
import PullRequestTargetMergeMetadata from './model/PullRequestTargetMergeMetadata';
import PutCommentReactionInput from './model/PutCommentReactionInput';
import PutFileEntry from './model/PutFileEntry';
import PutFileEntrySourceFile from './model/PutFileEntrySourceFile';
import PutFileInput from './model/PutFileInput';
import PutFileOutput from './model/PutFileOutput';
import PutRepositoryTriggersInput from './model/PutRepositoryTriggersInput';
import PutRepositoryTriggersOutput from './model/PutRepositoryTriggersOutput';
import ReactionForComment from './model/ReactionForComment';
import ReactionForCommentReaction from './model/ReactionForCommentReaction';
import ReactionValueFormats from './model/ReactionValueFormats';
import RelativeFileVersionEnum from './model/RelativeFileVersionEnum';
import ReplaceContentEntry from './model/ReplaceContentEntry';
import ReplacementTypeEnum from './model/ReplacementTypeEnum';
import RepositoryMetadata from './model/RepositoryMetadata';
import RepositoryNameIdPair from './model/RepositoryNameIdPair';
import RepositoryTrigger from './model/RepositoryTrigger';
import RepositoryTriggerEventEnum from './model/RepositoryTriggerEventEnum';
import RepositoryTriggerExecutionFailure from './model/RepositoryTriggerExecutionFailure';
import SetFileModeEntry from './model/SetFileModeEntry';
import SortByEnum from './model/SortByEnum';
import SourceFileSpecifier from './model/SourceFileSpecifier';
import SubModule from './model/SubModule';
import SymbolicLink from './model/SymbolicLink';
import TagResourceInput from './model/TagResourceInput';
import Target from './model/Target';
import TestRepositoryTriggersInput from './model/TestRepositoryTriggersInput';
import TestRepositoryTriggersOutput from './model/TestRepositoryTriggersOutput';
import UntagResourceInput from './model/UntagResourceInput';
import UpdateApprovalRuleTemplateContentInput from './model/UpdateApprovalRuleTemplateContentInput';
import UpdateApprovalRuleTemplateContentOutput from './model/UpdateApprovalRuleTemplateContentOutput';
import UpdateApprovalRuleTemplateDescriptionInput from './model/UpdateApprovalRuleTemplateDescriptionInput';
import UpdateApprovalRuleTemplateDescriptionOutput from './model/UpdateApprovalRuleTemplateDescriptionOutput';
import UpdateApprovalRuleTemplateDescriptionOutputApprovalRuleTemplate from './model/UpdateApprovalRuleTemplateDescriptionOutputApprovalRuleTemplate';
import UpdateApprovalRuleTemplateNameInput from './model/UpdateApprovalRuleTemplateNameInput';
import UpdateApprovalRuleTemplateNameOutput from './model/UpdateApprovalRuleTemplateNameOutput';
import UpdateCommentInput from './model/UpdateCommentInput';
import UpdateCommentOutput from './model/UpdateCommentOutput';
import UpdateCommentOutputComment from './model/UpdateCommentOutputComment';
import UpdateDefaultBranchInput from './model/UpdateDefaultBranchInput';
import UpdatePullRequestApprovalRuleContentInput from './model/UpdatePullRequestApprovalRuleContentInput';
import UpdatePullRequestApprovalRuleContentOutput from './model/UpdatePullRequestApprovalRuleContentOutput';
import UpdatePullRequestApprovalRuleContentOutputApprovalRule from './model/UpdatePullRequestApprovalRuleContentOutputApprovalRule';
import UpdatePullRequestApprovalStateInput from './model/UpdatePullRequestApprovalStateInput';
import UpdatePullRequestDescriptionInput from './model/UpdatePullRequestDescriptionInput';
import UpdatePullRequestDescriptionOutput from './model/UpdatePullRequestDescriptionOutput';
import UpdatePullRequestDescriptionOutputPullRequest from './model/UpdatePullRequestDescriptionOutputPullRequest';
import UpdatePullRequestStatusInput from './model/UpdatePullRequestStatusInput';
import UpdatePullRequestStatusOutput from './model/UpdatePullRequestStatusOutput';
import UpdatePullRequestStatusOutputPullRequest from './model/UpdatePullRequestStatusOutputPullRequest';
import UpdatePullRequestTitleInput from './model/UpdatePullRequestTitleInput';
import UpdatePullRequestTitleOutput from './model/UpdatePullRequestTitleOutput';
import UpdateRepositoryDescriptionInput from './model/UpdateRepositoryDescriptionInput';
import UpdateRepositoryNameInput from './model/UpdateRepositoryNameInput';
import UserInfo from './model/UserInfo';
import DefaultApi from './api/DefaultApi';


/**
* &lt;fullname&gt;AWS CodeCommit&lt;/fullname&gt; &lt;p&gt;This is the &lt;i&gt;AWS CodeCommit API Reference&lt;/i&gt;. This reference provides descriptions of the operations and data types for AWS CodeCommit API along with usage examples.&lt;/p&gt; &lt;p&gt;You can use the AWS CodeCommit API to work with the following objects:&lt;/p&gt; &lt;p&gt;Repositories, by calling the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;BatchGetRepositories&lt;/a&gt;, which returns information about one or more repositories associated with your AWS account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateRepository&lt;/a&gt;, which creates an AWS CodeCommit repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteRepository&lt;/a&gt;, which deletes an AWS CodeCommit repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetRepository&lt;/a&gt;, which returns information about a specified repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListRepositories&lt;/a&gt;, which lists all AWS CodeCommit repositories associated with your AWS account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateRepositoryDescription&lt;/a&gt;, which sets or updates the description of the repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateRepositoryName&lt;/a&gt;, which changes the name of the repository. If you change the name of a repository, no other users of that repository can access it until you send them the new HTTPS or SSH URL to use.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Branches, by calling the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateBranch&lt;/a&gt;, which creates a branch in a specified repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteBranch&lt;/a&gt;, which deletes the specified branch in a repository unless it is the default branch.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetBranch&lt;/a&gt;, which returns information about a specified branch.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListBranches&lt;/a&gt;, which lists all branches for a specified repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateDefaultBranch&lt;/a&gt;, which changes the default branch for a repository.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Files, by calling the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteFile&lt;/a&gt;, which deletes the content of a specified file from a specified branch.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetBlob&lt;/a&gt;, which returns the base-64 encoded content of an individual Git blob object in a repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetFile&lt;/a&gt;, which returns the base-64 encoded content of a specified file.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetFolder&lt;/a&gt;, which returns the contents of a specified folder or directory.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PutFile&lt;/a&gt;, which adds or modifies a single file in a specified repository and branch.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Commits, by calling the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;BatchGetCommits&lt;/a&gt;, which returns information about one or more commits in a repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateCommit&lt;/a&gt;, which creates a commit for changes to a repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetCommit&lt;/a&gt;, which returns information about a commit, including commit messages and author and committer information.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetDifferences&lt;/a&gt;, which returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID, or other fully qualified reference).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Merges, by calling the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;BatchDescribeMergeConflicts&lt;/a&gt;, which returns information about conflicts in a merge between commits in a repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateUnreferencedMergeCommit&lt;/a&gt;, which creates an unreferenced commit between two branches or commits for the purpose of comparing them and identifying any potential conflicts.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeMergeConflicts&lt;/a&gt;, which returns information about merge conflicts between the base, source, and destination versions of a file in a potential merge.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetMergeCommit&lt;/a&gt;, which returns information about the merge between a source and destination commit. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetMergeConflicts&lt;/a&gt;, which returns information about merge conflicts between the source and destination branch in a pull request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetMergeOptions&lt;/a&gt;, which returns information about the available merge options between two branches or commit specifiers.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;MergeBranchesByFastForward&lt;/a&gt;, which merges two branches using the fast-forward merge option.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;MergeBranchesBySquash&lt;/a&gt;, which merges two branches using the squash merge option.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;MergeBranchesByThreeWay&lt;/a&gt;, which merges two branches using the three-way merge option.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Pull requests, by calling the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreatePullRequest&lt;/a&gt;, which creates a pull request in a specified repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreatePullRequestApprovalRule&lt;/a&gt;, which creates an approval rule for a specified pull request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeletePullRequestApprovalRule&lt;/a&gt;, which deletes an approval rule for a specified pull request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribePullRequestEvents&lt;/a&gt;, which returns information about one or more pull request events.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;EvaluatePullRequestApprovalRules&lt;/a&gt;, which evaluates whether a pull request has met all the conditions specified in its associated approval rules.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetCommentsForPullRequest&lt;/a&gt;, which returns information about comments on a specified pull request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetPullRequest&lt;/a&gt;, which returns information about a specified pull request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetPullRequestApprovalStates&lt;/a&gt;, which returns information about the approval states for a specified pull request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetPullRequestOverrideState&lt;/a&gt;, which returns information about whether approval rules have been set aside (overriden) for a pull request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListPullRequests&lt;/a&gt;, which lists all pull requests for a repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;MergePullRequestByFastForward&lt;/a&gt;, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the fast-forward merge option.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;MergePullRequestBySquash&lt;/a&gt;, which merges the source destination branch of a pull request into the specified destination branch for that pull request using the squash merge option.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;MergePullRequestByThreeWay&lt;/a&gt;. which merges the source destination branch of a pull request into the specified destination branch for that pull request using the three-way merge option.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;OverridePullRequestApprovalRules&lt;/a&gt;, which sets aside all approval rule requirements for a pull request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PostCommentForPullRequest&lt;/a&gt;, which posts a comment to a pull request at the specified line, file, or request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdatePullRequestApprovalRuleContent&lt;/a&gt;, which updates the structure of an approval rule for a pull request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdatePullRequestApprovalState&lt;/a&gt;, which updates the state of an approval on a pull request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdatePullRequestDescription&lt;/a&gt;, which updates the description of a pull request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdatePullRequestStatus&lt;/a&gt;, which updates the status of a pull request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdatePullRequestTitle&lt;/a&gt;, which updates the title of a pull request.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Approval rule templates, by calling the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;AssociateApprovalRuleTemplateWithRepository&lt;/a&gt;, which associates a template with a specified repository. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;BatchAssociateApprovalRuleTemplateWithRepositories&lt;/a&gt;, which associates a template with one or more specified repositories. After the template is associated with a repository, AWS CodeCommit creates approval rules that match the template conditions on every pull request created in the specified repositories.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;BatchDisassociateApprovalRuleTemplateFromRepositories&lt;/a&gt;, which removes the association between a template and specified repositories so that approval rules based on the template are not automatically created when pull requests are created in those repositories.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateApprovalRuleTemplate&lt;/a&gt;, which creates a template for approval rules that can then be associated with one or more repositories in your AWS account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteApprovalRuleTemplate&lt;/a&gt;, which deletes the specified template. It does not remove approval rules on pull requests already created with the template.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DisassociateApprovalRuleTemplateFromRepository&lt;/a&gt;, which removes the association between a template and a repository so that approval rules based on the template are not automatically created when pull requests are created in the specified repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetApprovalRuleTemplate&lt;/a&gt;, which returns information about an approval rule template.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListApprovalRuleTemplates&lt;/a&gt;, which lists all approval rule templates in the AWS Region in your AWS account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListAssociatedApprovalRuleTemplatesForRepository&lt;/a&gt;, which lists all approval rule templates that are associated with a specified repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListRepositoriesForApprovalRuleTemplate&lt;/a&gt;, which lists all repositories associated with the specified approval rule template.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateApprovalRuleTemplateDescription&lt;/a&gt;, which updates the description of an approval rule template.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateApprovalRuleTemplateName&lt;/a&gt;, which updates the name of an approval rule template.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateApprovalRuleTemplateContent&lt;/a&gt;, which updates the content of an approval rule template.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Comments in a repository, by calling the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteCommentContent&lt;/a&gt;, which deletes the content of a comment on a commit in a repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetComment&lt;/a&gt;, which returns information about a comment on a commit.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetCommentReactions&lt;/a&gt;, which returns information about emoji reactions to comments.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetCommentsForComparedCommit&lt;/a&gt;, which returns information about comments on the comparison between two commit specifiers in a repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PostCommentForComparedCommit&lt;/a&gt;, which creates a comment on the comparison between two commit specifiers in a repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PostCommentReply&lt;/a&gt;, which creates a reply to a comment.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PutCommentReaction&lt;/a&gt;, which creates or updates an emoji reaction to a comment.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateComment&lt;/a&gt;, which updates the content of a comment on a commit in a repository.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Tags used to tag resources in AWS CodeCommit (not Git tags), by calling the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListTagsForResource&lt;/a&gt;, which gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS CodeCommit.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;TagResource&lt;/a&gt;, which adds or updates tags for a resource in AWS CodeCommit.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UntagResource&lt;/a&gt;, which removes tags for a resource in AWS CodeCommit.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Triggers, by calling the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetRepositoryTriggers&lt;/a&gt;, which returns information about triggers configured for a repository.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PutRepositoryTriggers&lt;/a&gt;, which replaces all triggers for a repository and can be used to create or delete triggers.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;TestRepositoryTriggers&lt;/a&gt;, which tests the functionality of a repository trigger by sending data to the trigger target.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For information about how to use AWS CodeCommit, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html\&quot;&gt;AWS CodeCommit User Guide&lt;/a&gt;.&lt;/p&gt;.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var AwsCodeCommit = require('index'); // See note below*.
* var xxxSvc = new AwsCodeCommit.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new AwsCodeCommit.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new AwsCodeCommit.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new AwsCodeCommit.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2015-04-13
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Approval model constructor.
     * @property {module:model/Approval}
     */
    Approval,

    /**
     * The ApprovalRule model constructor.
     * @property {module:model/ApprovalRule}
     */
    ApprovalRule,

    /**
     * The ApprovalRuleEventMetadata model constructor.
     * @property {module:model/ApprovalRuleEventMetadata}
     */
    ApprovalRuleEventMetadata,

    /**
     * The ApprovalRuleOriginApprovalRuleTemplate model constructor.
     * @property {module:model/ApprovalRuleOriginApprovalRuleTemplate}
     */
    ApprovalRuleOriginApprovalRuleTemplate,

    /**
     * The ApprovalRuleOverriddenEventMetadata model constructor.
     * @property {module:model/ApprovalRuleOverriddenEventMetadata}
     */
    ApprovalRuleOverriddenEventMetadata,

    /**
     * The ApprovalRuleTemplate model constructor.
     * @property {module:model/ApprovalRuleTemplate}
     */
    ApprovalRuleTemplate,

    /**
     * The ApprovalState model constructor.
     * @property {module:model/ApprovalState}
     */
    ApprovalState,

    /**
     * The ApprovalStateChangedEventMetadata model constructor.
     * @property {module:model/ApprovalStateChangedEventMetadata}
     */
    ApprovalStateChangedEventMetadata,

    /**
     * The AssociateApprovalRuleTemplateWithRepositoryInput model constructor.
     * @property {module:model/AssociateApprovalRuleTemplateWithRepositoryInput}
     */
    AssociateApprovalRuleTemplateWithRepositoryInput,

    /**
     * The BatchAssociateApprovalRuleTemplateWithRepositoriesError model constructor.
     * @property {module:model/BatchAssociateApprovalRuleTemplateWithRepositoriesError}
     */
    BatchAssociateApprovalRuleTemplateWithRepositoriesError,

    /**
     * The BatchAssociateApprovalRuleTemplateWithRepositoriesInput model constructor.
     * @property {module:model/BatchAssociateApprovalRuleTemplateWithRepositoriesInput}
     */
    BatchAssociateApprovalRuleTemplateWithRepositoriesInput,

    /**
     * The BatchAssociateApprovalRuleTemplateWithRepositoriesOutput model constructor.
     * @property {module:model/BatchAssociateApprovalRuleTemplateWithRepositoriesOutput}
     */
    BatchAssociateApprovalRuleTemplateWithRepositoriesOutput,

    /**
     * The BatchDescribeMergeConflictsError model constructor.
     * @property {module:model/BatchDescribeMergeConflictsError}
     */
    BatchDescribeMergeConflictsError,

    /**
     * The BatchDescribeMergeConflictsInput model constructor.
     * @property {module:model/BatchDescribeMergeConflictsInput}
     */
    BatchDescribeMergeConflictsInput,

    /**
     * The BatchDescribeMergeConflictsOutput model constructor.
     * @property {module:model/BatchDescribeMergeConflictsOutput}
     */
    BatchDescribeMergeConflictsOutput,

    /**
     * The BatchDisassociateApprovalRuleTemplateFromRepositoriesError model constructor.
     * @property {module:model/BatchDisassociateApprovalRuleTemplateFromRepositoriesError}
     */
    BatchDisassociateApprovalRuleTemplateFromRepositoriesError,

    /**
     * The BatchDisassociateApprovalRuleTemplateFromRepositoriesInput model constructor.
     * @property {module:model/BatchDisassociateApprovalRuleTemplateFromRepositoriesInput}
     */
    BatchDisassociateApprovalRuleTemplateFromRepositoriesInput,

    /**
     * The BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput model constructor.
     * @property {module:model/BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput}
     */
    BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput,

    /**
     * The BatchGetCommitsError model constructor.
     * @property {module:model/BatchGetCommitsError}
     */
    BatchGetCommitsError,

    /**
     * The BatchGetCommitsInput model constructor.
     * @property {module:model/BatchGetCommitsInput}
     */
    BatchGetCommitsInput,

    /**
     * The BatchGetCommitsOutput model constructor.
     * @property {module:model/BatchGetCommitsOutput}
     */
    BatchGetCommitsOutput,

    /**
     * The BatchGetRepositoriesInput model constructor.
     * @property {module:model/BatchGetRepositoriesInput}
     */
    BatchGetRepositoriesInput,

    /**
     * The BatchGetRepositoriesOutput model constructor.
     * @property {module:model/BatchGetRepositoriesOutput}
     */
    BatchGetRepositoriesOutput,

    /**
     * The BlobMetadata model constructor.
     * @property {module:model/BlobMetadata}
     */
    BlobMetadata,

    /**
     * The BranchInfo model constructor.
     * @property {module:model/BranchInfo}
     */
    BranchInfo,

    /**
     * The ChangeTypeEnum model constructor.
     * @property {module:model/ChangeTypeEnum}
     */
    ChangeTypeEnum,

    /**
     * The Comment model constructor.
     * @property {module:model/Comment}
     */
    Comment,

    /**
     * The CommentsForComparedCommit model constructor.
     * @property {module:model/CommentsForComparedCommit}
     */
    CommentsForComparedCommit,

    /**
     * The CommentsForComparedCommitLocation model constructor.
     * @property {module:model/CommentsForComparedCommitLocation}
     */
    CommentsForComparedCommitLocation,

    /**
     * The CommentsForPullRequest model constructor.
     * @property {module:model/CommentsForPullRequest}
     */
    CommentsForPullRequest,

    /**
     * The CommentsForPullRequestLocation model constructor.
     * @property {module:model/CommentsForPullRequestLocation}
     */
    CommentsForPullRequestLocation,

    /**
     * The Commit model constructor.
     * @property {module:model/Commit}
     */
    Commit,

    /**
     * The CommitAuthor model constructor.
     * @property {module:model/CommitAuthor}
     */
    CommitAuthor,

    /**
     * The CommitCommitter model constructor.
     * @property {module:model/CommitCommitter}
     */
    CommitCommitter,

    /**
     * The Conflict model constructor.
     * @property {module:model/Conflict}
     */
    Conflict,

    /**
     * The ConflictConflictMetadata model constructor.
     * @property {module:model/ConflictConflictMetadata}
     */
    ConflictConflictMetadata,

    /**
     * The ConflictDetailLevelTypeEnum model constructor.
     * @property {module:model/ConflictDetailLevelTypeEnum}
     */
    ConflictDetailLevelTypeEnum,

    /**
     * The ConflictMetadata model constructor.
     * @property {module:model/ConflictMetadata}
     */
    ConflictMetadata,

    /**
     * The ConflictMetadataFileModes model constructor.
     * @property {module:model/ConflictMetadataFileModes}
     */
    ConflictMetadataFileModes,

    /**
     * The ConflictMetadataFileSizes model constructor.
     * @property {module:model/ConflictMetadataFileSizes}
     */
    ConflictMetadataFileSizes,

    /**
     * The ConflictMetadataIsBinaryFile model constructor.
     * @property {module:model/ConflictMetadataIsBinaryFile}
     */
    ConflictMetadataIsBinaryFile,

    /**
     * The ConflictMetadataMergeOperations model constructor.
     * @property {module:model/ConflictMetadataMergeOperations}
     */
    ConflictMetadataMergeOperations,

    /**
     * The ConflictMetadataObjectTypes model constructor.
     * @property {module:model/ConflictMetadataObjectTypes}
     */
    ConflictMetadataObjectTypes,

    /**
     * The ConflictResolution model constructor.
     * @property {module:model/ConflictResolution}
     */
    ConflictResolution,

    /**
     * The ConflictResolutionStrategyTypeEnum model constructor.
     * @property {module:model/ConflictResolutionStrategyTypeEnum}
     */
    ConflictResolutionStrategyTypeEnum,

    /**
     * The CreateApprovalRuleTemplateInput model constructor.
     * @property {module:model/CreateApprovalRuleTemplateInput}
     */
    CreateApprovalRuleTemplateInput,

    /**
     * The CreateApprovalRuleTemplateOutput model constructor.
     * @property {module:model/CreateApprovalRuleTemplateOutput}
     */
    CreateApprovalRuleTemplateOutput,

    /**
     * The CreateApprovalRuleTemplateOutputApprovalRuleTemplate model constructor.
     * @property {module:model/CreateApprovalRuleTemplateOutputApprovalRuleTemplate}
     */
    CreateApprovalRuleTemplateOutputApprovalRuleTemplate,

    /**
     * The CreateBranchInput model constructor.
     * @property {module:model/CreateBranchInput}
     */
    CreateBranchInput,

    /**
     * The CreateCommitInput model constructor.
     * @property {module:model/CreateCommitInput}
     */
    CreateCommitInput,

    /**
     * The CreateCommitOutput model constructor.
     * @property {module:model/CreateCommitOutput}
     */
    CreateCommitOutput,

    /**
     * The CreatePullRequestApprovalRuleInput model constructor.
     * @property {module:model/CreatePullRequestApprovalRuleInput}
     */
    CreatePullRequestApprovalRuleInput,

    /**
     * The CreatePullRequestApprovalRuleOutput model constructor.
     * @property {module:model/CreatePullRequestApprovalRuleOutput}
     */
    CreatePullRequestApprovalRuleOutput,

    /**
     * The CreatePullRequestApprovalRuleOutputApprovalRule model constructor.
     * @property {module:model/CreatePullRequestApprovalRuleOutputApprovalRule}
     */
    CreatePullRequestApprovalRuleOutputApprovalRule,

    /**
     * The CreatePullRequestInput model constructor.
     * @property {module:model/CreatePullRequestInput}
     */
    CreatePullRequestInput,

    /**
     * The CreatePullRequestOutput model constructor.
     * @property {module:model/CreatePullRequestOutput}
     */
    CreatePullRequestOutput,

    /**
     * The CreatePullRequestOutputPullRequest model constructor.
     * @property {module:model/CreatePullRequestOutputPullRequest}
     */
    CreatePullRequestOutputPullRequest,

    /**
     * The CreateRepositoryInput model constructor.
     * @property {module:model/CreateRepositoryInput}
     */
    CreateRepositoryInput,

    /**
     * The CreateRepositoryOutput model constructor.
     * @property {module:model/CreateRepositoryOutput}
     */
    CreateRepositoryOutput,

    /**
     * The CreateRepositoryOutputRepositoryMetadata model constructor.
     * @property {module:model/CreateRepositoryOutputRepositoryMetadata}
     */
    CreateRepositoryOutputRepositoryMetadata,

    /**
     * The CreateUnreferencedMergeCommitInput model constructor.
     * @property {module:model/CreateUnreferencedMergeCommitInput}
     */
    CreateUnreferencedMergeCommitInput,

    /**
     * The CreateUnreferencedMergeCommitInputConflictResolution model constructor.
     * @property {module:model/CreateUnreferencedMergeCommitInputConflictResolution}
     */
    CreateUnreferencedMergeCommitInputConflictResolution,

    /**
     * The CreateUnreferencedMergeCommitOutput model constructor.
     * @property {module:model/CreateUnreferencedMergeCommitOutput}
     */
    CreateUnreferencedMergeCommitOutput,

    /**
     * The DeleteApprovalRuleTemplateInput model constructor.
     * @property {module:model/DeleteApprovalRuleTemplateInput}
     */
    DeleteApprovalRuleTemplateInput,

    /**
     * The DeleteApprovalRuleTemplateOutput model constructor.
     * @property {module:model/DeleteApprovalRuleTemplateOutput}
     */
    DeleteApprovalRuleTemplateOutput,

    /**
     * The DeleteBranchInput model constructor.
     * @property {module:model/DeleteBranchInput}
     */
    DeleteBranchInput,

    /**
     * The DeleteBranchOutput model constructor.
     * @property {module:model/DeleteBranchOutput}
     */
    DeleteBranchOutput,

    /**
     * The DeleteBranchOutputDeletedBranch model constructor.
     * @property {module:model/DeleteBranchOutputDeletedBranch}
     */
    DeleteBranchOutputDeletedBranch,

    /**
     * The DeleteCommentContentInput model constructor.
     * @property {module:model/DeleteCommentContentInput}
     */
    DeleteCommentContentInput,

    /**
     * The DeleteCommentContentOutput model constructor.
     * @property {module:model/DeleteCommentContentOutput}
     */
    DeleteCommentContentOutput,

    /**
     * The DeleteCommentContentOutputComment model constructor.
     * @property {module:model/DeleteCommentContentOutputComment}
     */
    DeleteCommentContentOutputComment,

    /**
     * The DeleteFileEntry model constructor.
     * @property {module:model/DeleteFileEntry}
     */
    DeleteFileEntry,

    /**
     * The DeleteFileInput model constructor.
     * @property {module:model/DeleteFileInput}
     */
    DeleteFileInput,

    /**
     * The DeleteFileOutput model constructor.
     * @property {module:model/DeleteFileOutput}
     */
    DeleteFileOutput,

    /**
     * The DeletePullRequestApprovalRuleInput model constructor.
     * @property {module:model/DeletePullRequestApprovalRuleInput}
     */
    DeletePullRequestApprovalRuleInput,

    /**
     * The DeletePullRequestApprovalRuleOutput model constructor.
     * @property {module:model/DeletePullRequestApprovalRuleOutput}
     */
    DeletePullRequestApprovalRuleOutput,

    /**
     * The DeleteRepositoryInput model constructor.
     * @property {module:model/DeleteRepositoryInput}
     */
    DeleteRepositoryInput,

    /**
     * The DeleteRepositoryOutput model constructor.
     * @property {module:model/DeleteRepositoryOutput}
     */
    DeleteRepositoryOutput,

    /**
     * The DescribeMergeConflictsInput model constructor.
     * @property {module:model/DescribeMergeConflictsInput}
     */
    DescribeMergeConflictsInput,

    /**
     * The DescribeMergeConflictsOutput model constructor.
     * @property {module:model/DescribeMergeConflictsOutput}
     */
    DescribeMergeConflictsOutput,

    /**
     * The DescribeMergeConflictsOutputConflictMetadata model constructor.
     * @property {module:model/DescribeMergeConflictsOutputConflictMetadata}
     */
    DescribeMergeConflictsOutputConflictMetadata,

    /**
     * The DescribePullRequestEventsInput model constructor.
     * @property {module:model/DescribePullRequestEventsInput}
     */
    DescribePullRequestEventsInput,

    /**
     * The DescribePullRequestEventsOutput model constructor.
     * @property {module:model/DescribePullRequestEventsOutput}
     */
    DescribePullRequestEventsOutput,

    /**
     * The Difference model constructor.
     * @property {module:model/Difference}
     */
    Difference,

    /**
     * The DifferenceAfterBlob model constructor.
     * @property {module:model/DifferenceAfterBlob}
     */
    DifferenceAfterBlob,

    /**
     * The DifferenceBeforeBlob model constructor.
     * @property {module:model/DifferenceBeforeBlob}
     */
    DifferenceBeforeBlob,

    /**
     * The DisassociateApprovalRuleTemplateFromRepositoryInput model constructor.
     * @property {module:model/DisassociateApprovalRuleTemplateFromRepositoryInput}
     */
    DisassociateApprovalRuleTemplateFromRepositoryInput,

    /**
     * The EvaluatePullRequestApprovalRulesInput model constructor.
     * @property {module:model/EvaluatePullRequestApprovalRulesInput}
     */
    EvaluatePullRequestApprovalRulesInput,

    /**
     * The EvaluatePullRequestApprovalRulesOutput model constructor.
     * @property {module:model/EvaluatePullRequestApprovalRulesOutput}
     */
    EvaluatePullRequestApprovalRulesOutput,

    /**
     * The EvaluatePullRequestApprovalRulesOutputEvaluation model constructor.
     * @property {module:model/EvaluatePullRequestApprovalRulesOutputEvaluation}
     */
    EvaluatePullRequestApprovalRulesOutputEvaluation,

    /**
     * The Evaluation model constructor.
     * @property {module:model/Evaluation}
     */
    Evaluation,

    /**
     * The File model constructor.
     * @property {module:model/File}
     */
    File,

    /**
     * The FileMetadata model constructor.
     * @property {module:model/FileMetadata}
     */
    FileMetadata,

    /**
     * The FileModeTypeEnum model constructor.
     * @property {module:model/FileModeTypeEnum}
     */
    FileModeTypeEnum,

    /**
     * The FileModes model constructor.
     * @property {module:model/FileModes}
     */
    FileModes,

    /**
     * The FileSizes model constructor.
     * @property {module:model/FileSizes}
     */
    FileSizes,

    /**
     * The Folder model constructor.
     * @property {module:model/Folder}
     */
    Folder,

    /**
     * The GetApprovalRuleTemplateInput model constructor.
     * @property {module:model/GetApprovalRuleTemplateInput}
     */
    GetApprovalRuleTemplateInput,

    /**
     * The GetApprovalRuleTemplateOutput model constructor.
     * @property {module:model/GetApprovalRuleTemplateOutput}
     */
    GetApprovalRuleTemplateOutput,

    /**
     * The GetApprovalRuleTemplateOutputApprovalRuleTemplate model constructor.
     * @property {module:model/GetApprovalRuleTemplateOutputApprovalRuleTemplate}
     */
    GetApprovalRuleTemplateOutputApprovalRuleTemplate,

    /**
     * The GetBlobInput model constructor.
     * @property {module:model/GetBlobInput}
     */
    GetBlobInput,

    /**
     * The GetBlobOutput model constructor.
     * @property {module:model/GetBlobOutput}
     */
    GetBlobOutput,

    /**
     * The GetBranchInput model constructor.
     * @property {module:model/GetBranchInput}
     */
    GetBranchInput,

    /**
     * The GetBranchOutput model constructor.
     * @property {module:model/GetBranchOutput}
     */
    GetBranchOutput,

    /**
     * The GetBranchOutputBranch model constructor.
     * @property {module:model/GetBranchOutputBranch}
     */
    GetBranchOutputBranch,

    /**
     * The GetCommentInput model constructor.
     * @property {module:model/GetCommentInput}
     */
    GetCommentInput,

    /**
     * The GetCommentOutput model constructor.
     * @property {module:model/GetCommentOutput}
     */
    GetCommentOutput,

    /**
     * The GetCommentOutputComment model constructor.
     * @property {module:model/GetCommentOutputComment}
     */
    GetCommentOutputComment,

    /**
     * The GetCommentReactionsInput model constructor.
     * @property {module:model/GetCommentReactionsInput}
     */
    GetCommentReactionsInput,

    /**
     * The GetCommentReactionsOutput model constructor.
     * @property {module:model/GetCommentReactionsOutput}
     */
    GetCommentReactionsOutput,

    /**
     * The GetCommentsForComparedCommitInput model constructor.
     * @property {module:model/GetCommentsForComparedCommitInput}
     */
    GetCommentsForComparedCommitInput,

    /**
     * The GetCommentsForComparedCommitOutput model constructor.
     * @property {module:model/GetCommentsForComparedCommitOutput}
     */
    GetCommentsForComparedCommitOutput,

    /**
     * The GetCommentsForPullRequestInput model constructor.
     * @property {module:model/GetCommentsForPullRequestInput}
     */
    GetCommentsForPullRequestInput,

    /**
     * The GetCommentsForPullRequestOutput model constructor.
     * @property {module:model/GetCommentsForPullRequestOutput}
     */
    GetCommentsForPullRequestOutput,

    /**
     * The GetCommitInput model constructor.
     * @property {module:model/GetCommitInput}
     */
    GetCommitInput,

    /**
     * The GetCommitOutput model constructor.
     * @property {module:model/GetCommitOutput}
     */
    GetCommitOutput,

    /**
     * The GetCommitOutputCommit model constructor.
     * @property {module:model/GetCommitOutputCommit}
     */
    GetCommitOutputCommit,

    /**
     * The GetDifferencesInput model constructor.
     * @property {module:model/GetDifferencesInput}
     */
    GetDifferencesInput,

    /**
     * The GetDifferencesOutput model constructor.
     * @property {module:model/GetDifferencesOutput}
     */
    GetDifferencesOutput,

    /**
     * The GetFileInput model constructor.
     * @property {module:model/GetFileInput}
     */
    GetFileInput,

    /**
     * The GetFileOutput model constructor.
     * @property {module:model/GetFileOutput}
     */
    GetFileOutput,

    /**
     * The GetFolderInput model constructor.
     * @property {module:model/GetFolderInput}
     */
    GetFolderInput,

    /**
     * The GetFolderOutput model constructor.
     * @property {module:model/GetFolderOutput}
     */
    GetFolderOutput,

    /**
     * The GetMergeCommitInput model constructor.
     * @property {module:model/GetMergeCommitInput}
     */
    GetMergeCommitInput,

    /**
     * The GetMergeCommitOutput model constructor.
     * @property {module:model/GetMergeCommitOutput}
     */
    GetMergeCommitOutput,

    /**
     * The GetMergeConflictsInput model constructor.
     * @property {module:model/GetMergeConflictsInput}
     */
    GetMergeConflictsInput,

    /**
     * The GetMergeConflictsOutput model constructor.
     * @property {module:model/GetMergeConflictsOutput}
     */
    GetMergeConflictsOutput,

    /**
     * The GetMergeOptionsInput model constructor.
     * @property {module:model/GetMergeOptionsInput}
     */
    GetMergeOptionsInput,

    /**
     * The GetMergeOptionsOutput model constructor.
     * @property {module:model/GetMergeOptionsOutput}
     */
    GetMergeOptionsOutput,

    /**
     * The GetPullRequestApprovalStatesInput model constructor.
     * @property {module:model/GetPullRequestApprovalStatesInput}
     */
    GetPullRequestApprovalStatesInput,

    /**
     * The GetPullRequestApprovalStatesOutput model constructor.
     * @property {module:model/GetPullRequestApprovalStatesOutput}
     */
    GetPullRequestApprovalStatesOutput,

    /**
     * The GetPullRequestInput model constructor.
     * @property {module:model/GetPullRequestInput}
     */
    GetPullRequestInput,

    /**
     * The GetPullRequestOutput model constructor.
     * @property {module:model/GetPullRequestOutput}
     */
    GetPullRequestOutput,

    /**
     * The GetPullRequestOutputPullRequest model constructor.
     * @property {module:model/GetPullRequestOutputPullRequest}
     */
    GetPullRequestOutputPullRequest,

    /**
     * The GetPullRequestOverrideStateInput model constructor.
     * @property {module:model/GetPullRequestOverrideStateInput}
     */
    GetPullRequestOverrideStateInput,

    /**
     * The GetPullRequestOverrideStateOutput model constructor.
     * @property {module:model/GetPullRequestOverrideStateOutput}
     */
    GetPullRequestOverrideStateOutput,

    /**
     * The GetRepositoryInput model constructor.
     * @property {module:model/GetRepositoryInput}
     */
    GetRepositoryInput,

    /**
     * The GetRepositoryOutput model constructor.
     * @property {module:model/GetRepositoryOutput}
     */
    GetRepositoryOutput,

    /**
     * The GetRepositoryOutputRepositoryMetadata model constructor.
     * @property {module:model/GetRepositoryOutputRepositoryMetadata}
     */
    GetRepositoryOutputRepositoryMetadata,

    /**
     * The GetRepositoryTriggersInput model constructor.
     * @property {module:model/GetRepositoryTriggersInput}
     */
    GetRepositoryTriggersInput,

    /**
     * The GetRepositoryTriggersOutput model constructor.
     * @property {module:model/GetRepositoryTriggersOutput}
     */
    GetRepositoryTriggersOutput,

    /**
     * The IsBinaryFile model constructor.
     * @property {module:model/IsBinaryFile}
     */
    IsBinaryFile,

    /**
     * The ListApprovalRuleTemplatesInput model constructor.
     * @property {module:model/ListApprovalRuleTemplatesInput}
     */
    ListApprovalRuleTemplatesInput,

    /**
     * The ListApprovalRuleTemplatesOutput model constructor.
     * @property {module:model/ListApprovalRuleTemplatesOutput}
     */
    ListApprovalRuleTemplatesOutput,

    /**
     * The ListAssociatedApprovalRuleTemplatesForRepositoryInput model constructor.
     * @property {module:model/ListAssociatedApprovalRuleTemplatesForRepositoryInput}
     */
    ListAssociatedApprovalRuleTemplatesForRepositoryInput,

    /**
     * The ListAssociatedApprovalRuleTemplatesForRepositoryOutput model constructor.
     * @property {module:model/ListAssociatedApprovalRuleTemplatesForRepositoryOutput}
     */
    ListAssociatedApprovalRuleTemplatesForRepositoryOutput,

    /**
     * The ListBranchesInput model constructor.
     * @property {module:model/ListBranchesInput}
     */
    ListBranchesInput,

    /**
     * The ListBranchesOutput model constructor.
     * @property {module:model/ListBranchesOutput}
     */
    ListBranchesOutput,

    /**
     * The ListPullRequestsInput model constructor.
     * @property {module:model/ListPullRequestsInput}
     */
    ListPullRequestsInput,

    /**
     * The ListPullRequestsOutput model constructor.
     * @property {module:model/ListPullRequestsOutput}
     */
    ListPullRequestsOutput,

    /**
     * The ListRepositoriesForApprovalRuleTemplateInput model constructor.
     * @property {module:model/ListRepositoriesForApprovalRuleTemplateInput}
     */
    ListRepositoriesForApprovalRuleTemplateInput,

    /**
     * The ListRepositoriesForApprovalRuleTemplateOutput model constructor.
     * @property {module:model/ListRepositoriesForApprovalRuleTemplateOutput}
     */
    ListRepositoriesForApprovalRuleTemplateOutput,

    /**
     * The ListRepositoriesInput model constructor.
     * @property {module:model/ListRepositoriesInput}
     */
    ListRepositoriesInput,

    /**
     * The ListRepositoriesOutput model constructor.
     * @property {module:model/ListRepositoriesOutput}
     */
    ListRepositoriesOutput,

    /**
     * The ListTagsForResourceInput model constructor.
     * @property {module:model/ListTagsForResourceInput}
     */
    ListTagsForResourceInput,

    /**
     * The ListTagsForResourceOutput model constructor.
     * @property {module:model/ListTagsForResourceOutput}
     */
    ListTagsForResourceOutput,

    /**
     * The Location model constructor.
     * @property {module:model/Location}
     */
    Location,

    /**
     * The MergeBranchesByFastForwardInput model constructor.
     * @property {module:model/MergeBranchesByFastForwardInput}
     */
    MergeBranchesByFastForwardInput,

    /**
     * The MergeBranchesByFastForwardOutput model constructor.
     * @property {module:model/MergeBranchesByFastForwardOutput}
     */
    MergeBranchesByFastForwardOutput,

    /**
     * The MergeBranchesBySquashInput model constructor.
     * @property {module:model/MergeBranchesBySquashInput}
     */
    MergeBranchesBySquashInput,

    /**
     * The MergeBranchesBySquashOutput model constructor.
     * @property {module:model/MergeBranchesBySquashOutput}
     */
    MergeBranchesBySquashOutput,

    /**
     * The MergeBranchesByThreeWayInput model constructor.
     * @property {module:model/MergeBranchesByThreeWayInput}
     */
    MergeBranchesByThreeWayInput,

    /**
     * The MergeBranchesByThreeWayOutput model constructor.
     * @property {module:model/MergeBranchesByThreeWayOutput}
     */
    MergeBranchesByThreeWayOutput,

    /**
     * The MergeHunk model constructor.
     * @property {module:model/MergeHunk}
     */
    MergeHunk,

    /**
     * The MergeHunkBase model constructor.
     * @property {module:model/MergeHunkBase}
     */
    MergeHunkBase,

    /**
     * The MergeHunkDestination model constructor.
     * @property {module:model/MergeHunkDestination}
     */
    MergeHunkDestination,

    /**
     * The MergeHunkDetail model constructor.
     * @property {module:model/MergeHunkDetail}
     */
    MergeHunkDetail,

    /**
     * The MergeHunkSource model constructor.
     * @property {module:model/MergeHunkSource}
     */
    MergeHunkSource,

    /**
     * The MergeMetadata model constructor.
     * @property {module:model/MergeMetadata}
     */
    MergeMetadata,

    /**
     * The MergeOperations model constructor.
     * @property {module:model/MergeOperations}
     */
    MergeOperations,

    /**
     * The MergeOptionTypeEnum model constructor.
     * @property {module:model/MergeOptionTypeEnum}
     */
    MergeOptionTypeEnum,

    /**
     * The MergePullRequestByFastForwardInput model constructor.
     * @property {module:model/MergePullRequestByFastForwardInput}
     */
    MergePullRequestByFastForwardInput,

    /**
     * The MergePullRequestByFastForwardOutput model constructor.
     * @property {module:model/MergePullRequestByFastForwardOutput}
     */
    MergePullRequestByFastForwardOutput,

    /**
     * The MergePullRequestByFastForwardOutputPullRequest model constructor.
     * @property {module:model/MergePullRequestByFastForwardOutputPullRequest}
     */
    MergePullRequestByFastForwardOutputPullRequest,

    /**
     * The MergePullRequestBySquashInput model constructor.
     * @property {module:model/MergePullRequestBySquashInput}
     */
    MergePullRequestBySquashInput,

    /**
     * The MergePullRequestBySquashOutput model constructor.
     * @property {module:model/MergePullRequestBySquashOutput}
     */
    MergePullRequestBySquashOutput,

    /**
     * The MergePullRequestByThreeWayInput model constructor.
     * @property {module:model/MergePullRequestByThreeWayInput}
     */
    MergePullRequestByThreeWayInput,

    /**
     * The MergePullRequestByThreeWayOutput model constructor.
     * @property {module:model/MergePullRequestByThreeWayOutput}
     */
    MergePullRequestByThreeWayOutput,

    /**
     * The ObjectTypeEnum model constructor.
     * @property {module:model/ObjectTypeEnum}
     */
    ObjectTypeEnum,

    /**
     * The ObjectTypes model constructor.
     * @property {module:model/ObjectTypes}
     */
    ObjectTypes,

    /**
     * The OrderEnum model constructor.
     * @property {module:model/OrderEnum}
     */
    OrderEnum,

    /**
     * The OriginApprovalRuleTemplate model constructor.
     * @property {module:model/OriginApprovalRuleTemplate}
     */
    OriginApprovalRuleTemplate,

    /**
     * The OverridePullRequestApprovalRulesInput model constructor.
     * @property {module:model/OverridePullRequestApprovalRulesInput}
     */
    OverridePullRequestApprovalRulesInput,

    /**
     * The OverrideStatus model constructor.
     * @property {module:model/OverrideStatus}
     */
    OverrideStatus,

    /**
     * The PostCommentForComparedCommitInput model constructor.
     * @property {module:model/PostCommentForComparedCommitInput}
     */
    PostCommentForComparedCommitInput,

    /**
     * The PostCommentForComparedCommitInputLocation model constructor.
     * @property {module:model/PostCommentForComparedCommitInputLocation}
     */
    PostCommentForComparedCommitInputLocation,

    /**
     * The PostCommentForComparedCommitOutput model constructor.
     * @property {module:model/PostCommentForComparedCommitOutput}
     */
    PostCommentForComparedCommitOutput,

    /**
     * The PostCommentForComparedCommitOutputComment model constructor.
     * @property {module:model/PostCommentForComparedCommitOutputComment}
     */
    PostCommentForComparedCommitOutputComment,

    /**
     * The PostCommentForComparedCommitOutputLocation model constructor.
     * @property {module:model/PostCommentForComparedCommitOutputLocation}
     */
    PostCommentForComparedCommitOutputLocation,

    /**
     * The PostCommentForPullRequestInput model constructor.
     * @property {module:model/PostCommentForPullRequestInput}
     */
    PostCommentForPullRequestInput,

    /**
     * The PostCommentForPullRequestInputLocation model constructor.
     * @property {module:model/PostCommentForPullRequestInputLocation}
     */
    PostCommentForPullRequestInputLocation,

    /**
     * The PostCommentForPullRequestOutput model constructor.
     * @property {module:model/PostCommentForPullRequestOutput}
     */
    PostCommentForPullRequestOutput,

    /**
     * The PostCommentForPullRequestOutputLocation model constructor.
     * @property {module:model/PostCommentForPullRequestOutputLocation}
     */
    PostCommentForPullRequestOutputLocation,

    /**
     * The PostCommentReplyInput model constructor.
     * @property {module:model/PostCommentReplyInput}
     */
    PostCommentReplyInput,

    /**
     * The PostCommentReplyOutput model constructor.
     * @property {module:model/PostCommentReplyOutput}
     */
    PostCommentReplyOutput,

    /**
     * The PostCommentReplyOutputComment model constructor.
     * @property {module:model/PostCommentReplyOutputComment}
     */
    PostCommentReplyOutputComment,

    /**
     * The PullRequest model constructor.
     * @property {module:model/PullRequest}
     */
    PullRequest,

    /**
     * The PullRequestCreatedEventMetadata model constructor.
     * @property {module:model/PullRequestCreatedEventMetadata}
     */
    PullRequestCreatedEventMetadata,

    /**
     * The PullRequestEvent model constructor.
     * @property {module:model/PullRequestEvent}
     */
    PullRequestEvent,

    /**
     * The PullRequestEventApprovalRuleEventMetadata model constructor.
     * @property {module:model/PullRequestEventApprovalRuleEventMetadata}
     */
    PullRequestEventApprovalRuleEventMetadata,

    /**
     * The PullRequestEventApprovalRuleOverriddenEventMetadata model constructor.
     * @property {module:model/PullRequestEventApprovalRuleOverriddenEventMetadata}
     */
    PullRequestEventApprovalRuleOverriddenEventMetadata,

    /**
     * The PullRequestEventApprovalStateChangedEventMetadata model constructor.
     * @property {module:model/PullRequestEventApprovalStateChangedEventMetadata}
     */
    PullRequestEventApprovalStateChangedEventMetadata,

    /**
     * The PullRequestEventPullRequestCreatedEventMetadata model constructor.
     * @property {module:model/PullRequestEventPullRequestCreatedEventMetadata}
     */
    PullRequestEventPullRequestCreatedEventMetadata,

    /**
     * The PullRequestEventPullRequestMergedStateChangedEventMetadata model constructor.
     * @property {module:model/PullRequestEventPullRequestMergedStateChangedEventMetadata}
     */
    PullRequestEventPullRequestMergedStateChangedEventMetadata,

    /**
     * The PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata model constructor.
     * @property {module:model/PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata}
     */
    PullRequestEventPullRequestSourceReferenceUpdatedEventMetadata,

    /**
     * The PullRequestEventPullRequestStatusChangedEventMetadata model constructor.
     * @property {module:model/PullRequestEventPullRequestStatusChangedEventMetadata}
     */
    PullRequestEventPullRequestStatusChangedEventMetadata,

    /**
     * The PullRequestEventType model constructor.
     * @property {module:model/PullRequestEventType}
     */
    PullRequestEventType,

    /**
     * The PullRequestMergedStateChangedEventMetadata model constructor.
     * @property {module:model/PullRequestMergedStateChangedEventMetadata}
     */
    PullRequestMergedStateChangedEventMetadata,

    /**
     * The PullRequestMergedStateChangedEventMetadataMergeMetadata model constructor.
     * @property {module:model/PullRequestMergedStateChangedEventMetadataMergeMetadata}
     */
    PullRequestMergedStateChangedEventMetadataMergeMetadata,

    /**
     * The PullRequestSourceReferenceUpdatedEventMetadata model constructor.
     * @property {module:model/PullRequestSourceReferenceUpdatedEventMetadata}
     */
    PullRequestSourceReferenceUpdatedEventMetadata,

    /**
     * The PullRequestStatusChangedEventMetadata model constructor.
     * @property {module:model/PullRequestStatusChangedEventMetadata}
     */
    PullRequestStatusChangedEventMetadata,

    /**
     * The PullRequestStatusEnum model constructor.
     * @property {module:model/PullRequestStatusEnum}
     */
    PullRequestStatusEnum,

    /**
     * The PullRequestTarget model constructor.
     * @property {module:model/PullRequestTarget}
     */
    PullRequestTarget,

    /**
     * The PullRequestTargetMergeMetadata model constructor.
     * @property {module:model/PullRequestTargetMergeMetadata}
     */
    PullRequestTargetMergeMetadata,

    /**
     * The PutCommentReactionInput model constructor.
     * @property {module:model/PutCommentReactionInput}
     */
    PutCommentReactionInput,

    /**
     * The PutFileEntry model constructor.
     * @property {module:model/PutFileEntry}
     */
    PutFileEntry,

    /**
     * The PutFileEntrySourceFile model constructor.
     * @property {module:model/PutFileEntrySourceFile}
     */
    PutFileEntrySourceFile,

    /**
     * The PutFileInput model constructor.
     * @property {module:model/PutFileInput}
     */
    PutFileInput,

    /**
     * The PutFileOutput model constructor.
     * @property {module:model/PutFileOutput}
     */
    PutFileOutput,

    /**
     * The PutRepositoryTriggersInput model constructor.
     * @property {module:model/PutRepositoryTriggersInput}
     */
    PutRepositoryTriggersInput,

    /**
     * The PutRepositoryTriggersOutput model constructor.
     * @property {module:model/PutRepositoryTriggersOutput}
     */
    PutRepositoryTriggersOutput,

    /**
     * The ReactionForComment model constructor.
     * @property {module:model/ReactionForComment}
     */
    ReactionForComment,

    /**
     * The ReactionForCommentReaction model constructor.
     * @property {module:model/ReactionForCommentReaction}
     */
    ReactionForCommentReaction,

    /**
     * The ReactionValueFormats model constructor.
     * @property {module:model/ReactionValueFormats}
     */
    ReactionValueFormats,

    /**
     * The RelativeFileVersionEnum model constructor.
     * @property {module:model/RelativeFileVersionEnum}
     */
    RelativeFileVersionEnum,

    /**
     * The ReplaceContentEntry model constructor.
     * @property {module:model/ReplaceContentEntry}
     */
    ReplaceContentEntry,

    /**
     * The ReplacementTypeEnum model constructor.
     * @property {module:model/ReplacementTypeEnum}
     */
    ReplacementTypeEnum,

    /**
     * The RepositoryMetadata model constructor.
     * @property {module:model/RepositoryMetadata}
     */
    RepositoryMetadata,

    /**
     * The RepositoryNameIdPair model constructor.
     * @property {module:model/RepositoryNameIdPair}
     */
    RepositoryNameIdPair,

    /**
     * The RepositoryTrigger model constructor.
     * @property {module:model/RepositoryTrigger}
     */
    RepositoryTrigger,

    /**
     * The RepositoryTriggerEventEnum model constructor.
     * @property {module:model/RepositoryTriggerEventEnum}
     */
    RepositoryTriggerEventEnum,

    /**
     * The RepositoryTriggerExecutionFailure model constructor.
     * @property {module:model/RepositoryTriggerExecutionFailure}
     */
    RepositoryTriggerExecutionFailure,

    /**
     * The SetFileModeEntry model constructor.
     * @property {module:model/SetFileModeEntry}
     */
    SetFileModeEntry,

    /**
     * The SortByEnum model constructor.
     * @property {module:model/SortByEnum}
     */
    SortByEnum,

    /**
     * The SourceFileSpecifier model constructor.
     * @property {module:model/SourceFileSpecifier}
     */
    SourceFileSpecifier,

    /**
     * The SubModule model constructor.
     * @property {module:model/SubModule}
     */
    SubModule,

    /**
     * The SymbolicLink model constructor.
     * @property {module:model/SymbolicLink}
     */
    SymbolicLink,

    /**
     * The TagResourceInput model constructor.
     * @property {module:model/TagResourceInput}
     */
    TagResourceInput,

    /**
     * The Target model constructor.
     * @property {module:model/Target}
     */
    Target,

    /**
     * The TestRepositoryTriggersInput model constructor.
     * @property {module:model/TestRepositoryTriggersInput}
     */
    TestRepositoryTriggersInput,

    /**
     * The TestRepositoryTriggersOutput model constructor.
     * @property {module:model/TestRepositoryTriggersOutput}
     */
    TestRepositoryTriggersOutput,

    /**
     * The UntagResourceInput model constructor.
     * @property {module:model/UntagResourceInput}
     */
    UntagResourceInput,

    /**
     * The UpdateApprovalRuleTemplateContentInput model constructor.
     * @property {module:model/UpdateApprovalRuleTemplateContentInput}
     */
    UpdateApprovalRuleTemplateContentInput,

    /**
     * The UpdateApprovalRuleTemplateContentOutput model constructor.
     * @property {module:model/UpdateApprovalRuleTemplateContentOutput}
     */
    UpdateApprovalRuleTemplateContentOutput,

    /**
     * The UpdateApprovalRuleTemplateDescriptionInput model constructor.
     * @property {module:model/UpdateApprovalRuleTemplateDescriptionInput}
     */
    UpdateApprovalRuleTemplateDescriptionInput,

    /**
     * The UpdateApprovalRuleTemplateDescriptionOutput model constructor.
     * @property {module:model/UpdateApprovalRuleTemplateDescriptionOutput}
     */
    UpdateApprovalRuleTemplateDescriptionOutput,

    /**
     * The UpdateApprovalRuleTemplateDescriptionOutputApprovalRuleTemplate model constructor.
     * @property {module:model/UpdateApprovalRuleTemplateDescriptionOutputApprovalRuleTemplate}
     */
    UpdateApprovalRuleTemplateDescriptionOutputApprovalRuleTemplate,

    /**
     * The UpdateApprovalRuleTemplateNameInput model constructor.
     * @property {module:model/UpdateApprovalRuleTemplateNameInput}
     */
    UpdateApprovalRuleTemplateNameInput,

    /**
     * The UpdateApprovalRuleTemplateNameOutput model constructor.
     * @property {module:model/UpdateApprovalRuleTemplateNameOutput}
     */
    UpdateApprovalRuleTemplateNameOutput,

    /**
     * The UpdateCommentInput model constructor.
     * @property {module:model/UpdateCommentInput}
     */
    UpdateCommentInput,

    /**
     * The UpdateCommentOutput model constructor.
     * @property {module:model/UpdateCommentOutput}
     */
    UpdateCommentOutput,

    /**
     * The UpdateCommentOutputComment model constructor.
     * @property {module:model/UpdateCommentOutputComment}
     */
    UpdateCommentOutputComment,

    /**
     * The UpdateDefaultBranchInput model constructor.
     * @property {module:model/UpdateDefaultBranchInput}
     */
    UpdateDefaultBranchInput,

    /**
     * The UpdatePullRequestApprovalRuleContentInput model constructor.
     * @property {module:model/UpdatePullRequestApprovalRuleContentInput}
     */
    UpdatePullRequestApprovalRuleContentInput,

    /**
     * The UpdatePullRequestApprovalRuleContentOutput model constructor.
     * @property {module:model/UpdatePullRequestApprovalRuleContentOutput}
     */
    UpdatePullRequestApprovalRuleContentOutput,

    /**
     * The UpdatePullRequestApprovalRuleContentOutputApprovalRule model constructor.
     * @property {module:model/UpdatePullRequestApprovalRuleContentOutputApprovalRule}
     */
    UpdatePullRequestApprovalRuleContentOutputApprovalRule,

    /**
     * The UpdatePullRequestApprovalStateInput model constructor.
     * @property {module:model/UpdatePullRequestApprovalStateInput}
     */
    UpdatePullRequestApprovalStateInput,

    /**
     * The UpdatePullRequestDescriptionInput model constructor.
     * @property {module:model/UpdatePullRequestDescriptionInput}
     */
    UpdatePullRequestDescriptionInput,

    /**
     * The UpdatePullRequestDescriptionOutput model constructor.
     * @property {module:model/UpdatePullRequestDescriptionOutput}
     */
    UpdatePullRequestDescriptionOutput,

    /**
     * The UpdatePullRequestDescriptionOutputPullRequest model constructor.
     * @property {module:model/UpdatePullRequestDescriptionOutputPullRequest}
     */
    UpdatePullRequestDescriptionOutputPullRequest,

    /**
     * The UpdatePullRequestStatusInput model constructor.
     * @property {module:model/UpdatePullRequestStatusInput}
     */
    UpdatePullRequestStatusInput,

    /**
     * The UpdatePullRequestStatusOutput model constructor.
     * @property {module:model/UpdatePullRequestStatusOutput}
     */
    UpdatePullRequestStatusOutput,

    /**
     * The UpdatePullRequestStatusOutputPullRequest model constructor.
     * @property {module:model/UpdatePullRequestStatusOutputPullRequest}
     */
    UpdatePullRequestStatusOutputPullRequest,

    /**
     * The UpdatePullRequestTitleInput model constructor.
     * @property {module:model/UpdatePullRequestTitleInput}
     */
    UpdatePullRequestTitleInput,

    /**
     * The UpdatePullRequestTitleOutput model constructor.
     * @property {module:model/UpdatePullRequestTitleOutput}
     */
    UpdatePullRequestTitleOutput,

    /**
     * The UpdateRepositoryDescriptionInput model constructor.
     * @property {module:model/UpdateRepositoryDescriptionInput}
     */
    UpdateRepositoryDescriptionInput,

    /**
     * The UpdateRepositoryNameInput model constructor.
     * @property {module:model/UpdateRepositoryNameInput}
     */
    UpdateRepositoryNameInput,

    /**
     * The UserInfo model constructor.
     * @property {module:model/UserInfo}
     */
    UserInfo,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
