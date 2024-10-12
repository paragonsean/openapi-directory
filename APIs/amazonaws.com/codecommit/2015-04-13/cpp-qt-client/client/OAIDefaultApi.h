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
 */

#ifndef OAI_OAIDefaultApi_H
#define OAI_OAIDefaultApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAssociateApprovalRuleTemplateWithRepositoryInput.h"
#include "OAIBatchAssociateApprovalRuleTemplateWithRepositoriesInput.h"
#include "OAIBatchAssociateApprovalRuleTemplateWithRepositoriesOutput.h"
#include "OAIBatchDescribeMergeConflictsInput.h"
#include "OAIBatchDescribeMergeConflictsOutput.h"
#include "OAIBatchDisassociateApprovalRuleTemplateFromRepositoriesInput.h"
#include "OAIBatchDisassociateApprovalRuleTemplateFromRepositoriesOutput.h"
#include "OAIBatchGetCommitsInput.h"
#include "OAIBatchGetCommitsOutput.h"
#include "OAIBatchGetRepositoriesInput.h"
#include "OAIBatchGetRepositoriesOutput.h"
#include "OAICreateApprovalRuleTemplateInput.h"
#include "OAICreateApprovalRuleTemplateOutput.h"
#include "OAICreateBranchInput.h"
#include "OAICreateCommitInput.h"
#include "OAICreateCommitOutput.h"
#include "OAICreatePullRequestApprovalRuleInput.h"
#include "OAICreatePullRequestApprovalRuleOutput.h"
#include "OAICreatePullRequestInput.h"
#include "OAICreatePullRequestOutput.h"
#include "OAICreateRepositoryInput.h"
#include "OAICreateRepositoryOutput.h"
#include "OAICreateUnreferencedMergeCommitInput.h"
#include "OAICreateUnreferencedMergeCommitOutput.h"
#include "OAIDeleteApprovalRuleTemplateInput.h"
#include "OAIDeleteApprovalRuleTemplateOutput.h"
#include "OAIDeleteBranchInput.h"
#include "OAIDeleteBranchOutput.h"
#include "OAIDeleteCommentContentInput.h"
#include "OAIDeleteCommentContentOutput.h"
#include "OAIDeleteFileInput.h"
#include "OAIDeleteFileOutput.h"
#include "OAIDeletePullRequestApprovalRuleInput.h"
#include "OAIDeletePullRequestApprovalRuleOutput.h"
#include "OAIDeleteRepositoryInput.h"
#include "OAIDeleteRepositoryOutput.h"
#include "OAIDescribeMergeConflictsInput.h"
#include "OAIDescribeMergeConflictsOutput.h"
#include "OAIDescribePullRequestEventsInput.h"
#include "OAIDescribePullRequestEventsOutput.h"
#include "OAIDisassociateApprovalRuleTemplateFromRepositoryInput.h"
#include "OAIEvaluatePullRequestApprovalRulesInput.h"
#include "OAIEvaluatePullRequestApprovalRulesOutput.h"
#include "OAIGetApprovalRuleTemplateInput.h"
#include "OAIGetApprovalRuleTemplateOutput.h"
#include "OAIGetBlobInput.h"
#include "OAIGetBlobOutput.h"
#include "OAIGetBranchInput.h"
#include "OAIGetBranchOutput.h"
#include "OAIGetCommentInput.h"
#include "OAIGetCommentOutput.h"
#include "OAIGetCommentReactionsInput.h"
#include "OAIGetCommentReactionsOutput.h"
#include "OAIGetCommentsForComparedCommitInput.h"
#include "OAIGetCommentsForComparedCommitOutput.h"
#include "OAIGetCommentsForPullRequestInput.h"
#include "OAIGetCommentsForPullRequestOutput.h"
#include "OAIGetCommitInput.h"
#include "OAIGetCommitOutput.h"
#include "OAIGetDifferencesInput.h"
#include "OAIGetDifferencesOutput.h"
#include "OAIGetFileInput.h"
#include "OAIGetFileOutput.h"
#include "OAIGetFolderInput.h"
#include "OAIGetFolderOutput.h"
#include "OAIGetMergeCommitInput.h"
#include "OAIGetMergeCommitOutput.h"
#include "OAIGetMergeConflictsInput.h"
#include "OAIGetMergeConflictsOutput.h"
#include "OAIGetMergeOptionsInput.h"
#include "OAIGetMergeOptionsOutput.h"
#include "OAIGetPullRequestApprovalStatesInput.h"
#include "OAIGetPullRequestApprovalStatesOutput.h"
#include "OAIGetPullRequestInput.h"
#include "OAIGetPullRequestOutput.h"
#include "OAIGetPullRequestOverrideStateInput.h"
#include "OAIGetPullRequestOverrideStateOutput.h"
#include "OAIGetRepositoryInput.h"
#include "OAIGetRepositoryOutput.h"
#include "OAIGetRepositoryTriggersInput.h"
#include "OAIGetRepositoryTriggersOutput.h"
#include "OAIListApprovalRuleTemplatesInput.h"
#include "OAIListApprovalRuleTemplatesOutput.h"
#include "OAIListAssociatedApprovalRuleTemplatesForRepositoryInput.h"
#include "OAIListAssociatedApprovalRuleTemplatesForRepositoryOutput.h"
#include "OAIListBranchesInput.h"
#include "OAIListBranchesOutput.h"
#include "OAIListPullRequestsInput.h"
#include "OAIListPullRequestsOutput.h"
#include "OAIListRepositoriesForApprovalRuleTemplateInput.h"
#include "OAIListRepositoriesForApprovalRuleTemplateOutput.h"
#include "OAIListRepositoriesInput.h"
#include "OAIListRepositoriesOutput.h"
#include "OAIListTagsForResourceInput.h"
#include "OAIListTagsForResourceOutput.h"
#include "OAIMergeBranchesByFastForwardInput.h"
#include "OAIMergeBranchesByFastForwardOutput.h"
#include "OAIMergeBranchesBySquashInput.h"
#include "OAIMergeBranchesBySquashOutput.h"
#include "OAIMergeBranchesByThreeWayInput.h"
#include "OAIMergeBranchesByThreeWayOutput.h"
#include "OAIMergePullRequestByFastForwardInput.h"
#include "OAIMergePullRequestByFastForwardOutput.h"
#include "OAIMergePullRequestBySquashInput.h"
#include "OAIMergePullRequestBySquashOutput.h"
#include "OAIMergePullRequestByThreeWayInput.h"
#include "OAIMergePullRequestByThreeWayOutput.h"
#include "OAIOverridePullRequestApprovalRulesInput.h"
#include "OAIPostCommentForComparedCommitInput.h"
#include "OAIPostCommentForComparedCommitOutput.h"
#include "OAIPostCommentForPullRequestInput.h"
#include "OAIPostCommentForPullRequestOutput.h"
#include "OAIPostCommentReplyInput.h"
#include "OAIPostCommentReplyOutput.h"
#include "OAIPutCommentReactionInput.h"
#include "OAIPutFileInput.h"
#include "OAIPutFileOutput.h"
#include "OAIPutRepositoryTriggersInput.h"
#include "OAIPutRepositoryTriggersOutput.h"
#include "OAITagResourceInput.h"
#include "OAITestRepositoryTriggersInput.h"
#include "OAITestRepositoryTriggersOutput.h"
#include "OAIUntagResourceInput.h"
#include "OAIUpdateApprovalRuleTemplateContentInput.h"
#include "OAIUpdateApprovalRuleTemplateContentOutput.h"
#include "OAIUpdateApprovalRuleTemplateDescriptionInput.h"
#include "OAIUpdateApprovalRuleTemplateDescriptionOutput.h"
#include "OAIUpdateApprovalRuleTemplateNameInput.h"
#include "OAIUpdateApprovalRuleTemplateNameOutput.h"
#include "OAIUpdateCommentInput.h"
#include "OAIUpdateCommentOutput.h"
#include "OAIUpdateDefaultBranchInput.h"
#include "OAIUpdatePullRequestApprovalRuleContentInput.h"
#include "OAIUpdatePullRequestApprovalRuleContentOutput.h"
#include "OAIUpdatePullRequestApprovalStateInput.h"
#include "OAIUpdatePullRequestDescriptionInput.h"
#include "OAIUpdatePullRequestDescriptionOutput.h"
#include "OAIUpdatePullRequestStatusInput.h"
#include "OAIUpdatePullRequestStatusOutput.h"
#include "OAIUpdatePullRequestTitleInput.h"
#include "OAIUpdatePullRequestTitleOutput.h"
#include "OAIUpdateRepositoryDescriptionInput.h"
#include "OAIUpdateRepositoryNameInput.h"
#include <QJsonValue>
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDefaultApi : public QObject {
    Q_OBJECT

public:
    OAIDefaultApi(const int timeOut = 0);
    ~OAIDefaultApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_associate_approval_rule_template_with_repository_input OAIAssociateApprovalRuleTemplateWithRepositoryInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void associateApprovalRuleTemplateWithRepository(const QString &x_amz_target, const OAIAssociateApprovalRuleTemplateWithRepositoryInput &oai_associate_approval_rule_template_with_repository_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_batch_associate_approval_rule_template_with_repositories_input OAIBatchAssociateApprovalRuleTemplateWithRepositoriesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void batchAssociateApprovalRuleTemplateWithRepositories(const QString &x_amz_target, const OAIBatchAssociateApprovalRuleTemplateWithRepositoriesInput &oai_batch_associate_approval_rule_template_with_repositories_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_batch_describe_merge_conflicts_input OAIBatchDescribeMergeConflictsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void batchDescribeMergeConflicts(const QString &x_amz_target, const OAIBatchDescribeMergeConflictsInput &oai_batch_describe_merge_conflicts_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_batch_disassociate_approval_rule_template_from_repositories_input OAIBatchDisassociateApprovalRuleTemplateFromRepositoriesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void batchDisassociateApprovalRuleTemplateFromRepositories(const QString &x_amz_target, const OAIBatchDisassociateApprovalRuleTemplateFromRepositoriesInput &oai_batch_disassociate_approval_rule_template_from_repositories_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_batch_get_commits_input OAIBatchGetCommitsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void batchGetCommits(const QString &x_amz_target, const OAIBatchGetCommitsInput &oai_batch_get_commits_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_batch_get_repositories_input OAIBatchGetRepositoriesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void batchGetRepositories(const QString &x_amz_target, const OAIBatchGetRepositoriesInput &oai_batch_get_repositories_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_approval_rule_template_input OAICreateApprovalRuleTemplateInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createApprovalRuleTemplate(const QString &x_amz_target, const OAICreateApprovalRuleTemplateInput &oai_create_approval_rule_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_branch_input OAICreateBranchInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createBranch(const QString &x_amz_target, const OAICreateBranchInput &oai_create_branch_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_commit_input OAICreateCommitInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createCommit(const QString &x_amz_target, const OAICreateCommitInput &oai_create_commit_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_pull_request_input OAICreatePullRequestInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createPullRequest(const QString &x_amz_target, const OAICreatePullRequestInput &oai_create_pull_request_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_pull_request_approval_rule_input OAICreatePullRequestApprovalRuleInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createPullRequestApprovalRule(const QString &x_amz_target, const OAICreatePullRequestApprovalRuleInput &oai_create_pull_request_approval_rule_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_repository_input OAICreateRepositoryInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createRepository(const QString &x_amz_target, const OAICreateRepositoryInput &oai_create_repository_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_unreferenced_merge_commit_input OAICreateUnreferencedMergeCommitInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createUnreferencedMergeCommit(const QString &x_amz_target, const OAICreateUnreferencedMergeCommitInput &oai_create_unreferenced_merge_commit_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_approval_rule_template_input OAIDeleteApprovalRuleTemplateInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteApprovalRuleTemplate(const QString &x_amz_target, const OAIDeleteApprovalRuleTemplateInput &oai_delete_approval_rule_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_branch_input OAIDeleteBranchInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteBranch(const QString &x_amz_target, const OAIDeleteBranchInput &oai_delete_branch_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_comment_content_input OAIDeleteCommentContentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteCommentContent(const QString &x_amz_target, const OAIDeleteCommentContentInput &oai_delete_comment_content_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_file_input OAIDeleteFileInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteFile(const QString &x_amz_target, const OAIDeleteFileInput &oai_delete_file_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_pull_request_approval_rule_input OAIDeletePullRequestApprovalRuleInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deletePullRequestApprovalRule(const QString &x_amz_target, const OAIDeletePullRequestApprovalRuleInput &oai_delete_pull_request_approval_rule_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_repository_input OAIDeleteRepositoryInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteRepository(const QString &x_amz_target, const OAIDeleteRepositoryInput &oai_delete_repository_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_describe_merge_conflicts_input OAIDescribeMergeConflictsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_merge_hunks QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void describeMergeConflicts(const QString &x_amz_target, const OAIDescribeMergeConflictsInput &oai_describe_merge_conflicts_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_merge_hunks = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_describe_pull_request_events_input OAIDescribePullRequestEventsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void describePullRequestEvents(const QString &x_amz_target, const OAIDescribePullRequestEventsInput &oai_describe_pull_request_events_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_disassociate_approval_rule_template_from_repository_input OAIDisassociateApprovalRuleTemplateFromRepositoryInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void disassociateApprovalRuleTemplateFromRepository(const QString &x_amz_target, const OAIDisassociateApprovalRuleTemplateFromRepositoryInput &oai_disassociate_approval_rule_template_from_repository_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_evaluate_pull_request_approval_rules_input OAIEvaluatePullRequestApprovalRulesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void evaluatePullRequestApprovalRules(const QString &x_amz_target, const OAIEvaluatePullRequestApprovalRulesInput &oai_evaluate_pull_request_approval_rules_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_approval_rule_template_input OAIGetApprovalRuleTemplateInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getApprovalRuleTemplate(const QString &x_amz_target, const OAIGetApprovalRuleTemplateInput &oai_get_approval_rule_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_blob_input OAIGetBlobInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getBlob(const QString &x_amz_target, const OAIGetBlobInput &oai_get_blob_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_branch_input OAIGetBranchInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getBranch(const QString &x_amz_target, const OAIGetBranchInput &oai_get_branch_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_comment_input OAIGetCommentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getComment(const QString &x_amz_target, const OAIGetCommentInput &oai_get_comment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_comment_reactions_input OAIGetCommentReactionsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void getCommentReactions(const QString &x_amz_target, const OAIGetCommentReactionsInput &oai_get_comment_reactions_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_comments_for_compared_commit_input OAIGetCommentsForComparedCommitInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void getCommentsForComparedCommit(const QString &x_amz_target, const OAIGetCommentsForComparedCommitInput &oai_get_comments_for_compared_commit_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_comments_for_pull_request_input OAIGetCommentsForPullRequestInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void getCommentsForPullRequest(const QString &x_amz_target, const OAIGetCommentsForPullRequestInput &oai_get_comments_for_pull_request_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_commit_input OAIGetCommitInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getCommit(const QString &x_amz_target, const OAIGetCommitInput &oai_get_commit_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_differences_input OAIGetDifferencesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void getDifferences(const QString &x_amz_target, const OAIGetDifferencesInput &oai_get_differences_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_file_input OAIGetFileInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getFile(const QString &x_amz_target, const OAIGetFileInput &oai_get_file_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_folder_input OAIGetFolderInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getFolder(const QString &x_amz_target, const OAIGetFolderInput &oai_get_folder_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_merge_commit_input OAIGetMergeCommitInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getMergeCommit(const QString &x_amz_target, const OAIGetMergeCommitInput &oai_get_merge_commit_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_merge_conflicts_input OAIGetMergeConflictsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_conflict_files QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void getMergeConflicts(const QString &x_amz_target, const OAIGetMergeConflictsInput &oai_get_merge_conflicts_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_conflict_files = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_merge_options_input OAIGetMergeOptionsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getMergeOptions(const QString &x_amz_target, const OAIGetMergeOptionsInput &oai_get_merge_options_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_pull_request_input OAIGetPullRequestInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getPullRequest(const QString &x_amz_target, const OAIGetPullRequestInput &oai_get_pull_request_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_pull_request_approval_states_input OAIGetPullRequestApprovalStatesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getPullRequestApprovalStates(const QString &x_amz_target, const OAIGetPullRequestApprovalStatesInput &oai_get_pull_request_approval_states_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_pull_request_override_state_input OAIGetPullRequestOverrideStateInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getPullRequestOverrideState(const QString &x_amz_target, const OAIGetPullRequestOverrideStateInput &oai_get_pull_request_override_state_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_repository_input OAIGetRepositoryInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getRepository(const QString &x_amz_target, const OAIGetRepositoryInput &oai_get_repository_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_repository_triggers_input OAIGetRepositoryTriggersInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getRepositoryTriggers(const QString &x_amz_target, const OAIGetRepositoryTriggersInput &oai_get_repository_triggers_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_approval_rule_templates_input OAIListApprovalRuleTemplatesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listApprovalRuleTemplates(const QString &x_amz_target, const OAIListApprovalRuleTemplatesInput &oai_list_approval_rule_templates_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_associated_approval_rule_templates_for_repository_input OAIListAssociatedApprovalRuleTemplatesForRepositoryInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listAssociatedApprovalRuleTemplatesForRepository(const QString &x_amz_target, const OAIListAssociatedApprovalRuleTemplatesForRepositoryInput &oai_list_associated_approval_rule_templates_for_repository_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_branches_input OAIListBranchesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listBranches(const QString &x_amz_target, const OAIListBranchesInput &oai_list_branches_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_pull_requests_input OAIListPullRequestsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listPullRequests(const QString &x_amz_target, const OAIListPullRequestsInput &oai_list_pull_requests_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_repositories_input OAIListRepositoriesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listRepositories(const QString &x_amz_target, const OAIListRepositoriesInput &oai_list_repositories_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_repositories_for_approval_rule_template_input OAIListRepositoriesForApprovalRuleTemplateInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listRepositoriesForApprovalRuleTemplate(const QString &x_amz_target, const OAIListRepositoriesForApprovalRuleTemplateInput &oai_list_repositories_for_approval_rule_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_tags_for_resource_input OAIListTagsForResourceInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void listTagsForResource(const QString &x_amz_target, const OAIListTagsForResourceInput &oai_list_tags_for_resource_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_merge_branches_by_fast_forward_input OAIMergeBranchesByFastForwardInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void mergeBranchesByFastForward(const QString &x_amz_target, const OAIMergeBranchesByFastForwardInput &oai_merge_branches_by_fast_forward_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_merge_branches_by_squash_input OAIMergeBranchesBySquashInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void mergeBranchesBySquash(const QString &x_amz_target, const OAIMergeBranchesBySquashInput &oai_merge_branches_by_squash_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_merge_branches_by_three_way_input OAIMergeBranchesByThreeWayInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void mergeBranchesByThreeWay(const QString &x_amz_target, const OAIMergeBranchesByThreeWayInput &oai_merge_branches_by_three_way_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_merge_pull_request_by_fast_forward_input OAIMergePullRequestByFastForwardInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void mergePullRequestByFastForward(const QString &x_amz_target, const OAIMergePullRequestByFastForwardInput &oai_merge_pull_request_by_fast_forward_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_merge_pull_request_by_squash_input OAIMergePullRequestBySquashInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void mergePullRequestBySquash(const QString &x_amz_target, const OAIMergePullRequestBySquashInput &oai_merge_pull_request_by_squash_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_merge_pull_request_by_three_way_input OAIMergePullRequestByThreeWayInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void mergePullRequestByThreeWay(const QString &x_amz_target, const OAIMergePullRequestByThreeWayInput &oai_merge_pull_request_by_three_way_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_override_pull_request_approval_rules_input OAIOverridePullRequestApprovalRulesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void overridePullRequestApprovalRules(const QString &x_amz_target, const OAIOverridePullRequestApprovalRulesInput &oai_override_pull_request_approval_rules_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_post_comment_for_compared_commit_input OAIPostCommentForComparedCommitInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void postCommentForComparedCommit(const QString &x_amz_target, const OAIPostCommentForComparedCommitInput &oai_post_comment_for_compared_commit_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_post_comment_for_pull_request_input OAIPostCommentForPullRequestInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void postCommentForPullRequest(const QString &x_amz_target, const OAIPostCommentForPullRequestInput &oai_post_comment_for_pull_request_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_post_comment_reply_input OAIPostCommentReplyInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void postCommentReply(const QString &x_amz_target, const OAIPostCommentReplyInput &oai_post_comment_reply_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_put_comment_reaction_input OAIPutCommentReactionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void putCommentReaction(const QString &x_amz_target, const OAIPutCommentReactionInput &oai_put_comment_reaction_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_put_file_input OAIPutFileInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void putFile(const QString &x_amz_target, const OAIPutFileInput &oai_put_file_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_put_repository_triggers_input OAIPutRepositoryTriggersInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void putRepositoryTriggers(const QString &x_amz_target, const OAIPutRepositoryTriggersInput &oai_put_repository_triggers_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_tag_resource_input OAITagResourceInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void tagResource(const QString &x_amz_target, const OAITagResourceInput &oai_tag_resource_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_test_repository_triggers_input OAITestRepositoryTriggersInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void testRepositoryTriggers(const QString &x_amz_target, const OAITestRepositoryTriggersInput &oai_test_repository_triggers_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_untag_resource_input OAIUntagResourceInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void untagResource(const QString &x_amz_target, const OAIUntagResourceInput &oai_untag_resource_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_approval_rule_template_content_input OAIUpdateApprovalRuleTemplateContentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateApprovalRuleTemplateContent(const QString &x_amz_target, const OAIUpdateApprovalRuleTemplateContentInput &oai_update_approval_rule_template_content_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_approval_rule_template_description_input OAIUpdateApprovalRuleTemplateDescriptionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateApprovalRuleTemplateDescription(const QString &x_amz_target, const OAIUpdateApprovalRuleTemplateDescriptionInput &oai_update_approval_rule_template_description_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_approval_rule_template_name_input OAIUpdateApprovalRuleTemplateNameInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateApprovalRuleTemplateName(const QString &x_amz_target, const OAIUpdateApprovalRuleTemplateNameInput &oai_update_approval_rule_template_name_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_comment_input OAIUpdateCommentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateComment(const QString &x_amz_target, const OAIUpdateCommentInput &oai_update_comment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_default_branch_input OAIUpdateDefaultBranchInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateDefaultBranch(const QString &x_amz_target, const OAIUpdateDefaultBranchInput &oai_update_default_branch_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_pull_request_approval_rule_content_input OAIUpdatePullRequestApprovalRuleContentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updatePullRequestApprovalRuleContent(const QString &x_amz_target, const OAIUpdatePullRequestApprovalRuleContentInput &oai_update_pull_request_approval_rule_content_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_pull_request_approval_state_input OAIUpdatePullRequestApprovalStateInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updatePullRequestApprovalState(const QString &x_amz_target, const OAIUpdatePullRequestApprovalStateInput &oai_update_pull_request_approval_state_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_pull_request_description_input OAIUpdatePullRequestDescriptionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updatePullRequestDescription(const QString &x_amz_target, const OAIUpdatePullRequestDescriptionInput &oai_update_pull_request_description_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_pull_request_status_input OAIUpdatePullRequestStatusInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updatePullRequestStatus(const QString &x_amz_target, const OAIUpdatePullRequestStatusInput &oai_update_pull_request_status_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_pull_request_title_input OAIUpdatePullRequestTitleInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updatePullRequestTitle(const QString &x_amz_target, const OAIUpdatePullRequestTitleInput &oai_update_pull_request_title_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_repository_description_input OAIUpdateRepositoryDescriptionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateRepositoryDescription(const QString &x_amz_target, const OAIUpdateRepositoryDescriptionInput &oai_update_repository_description_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_repository_name_input OAIUpdateRepositoryNameInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateRepositoryName(const QString &x_amz_target, const OAIUpdateRepositoryNameInput &oai_update_repository_name_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void associateApprovalRuleTemplateWithRepositoryCallback(OAIHttpRequestWorker *worker);
    void batchAssociateApprovalRuleTemplateWithRepositoriesCallback(OAIHttpRequestWorker *worker);
    void batchDescribeMergeConflictsCallback(OAIHttpRequestWorker *worker);
    void batchDisassociateApprovalRuleTemplateFromRepositoriesCallback(OAIHttpRequestWorker *worker);
    void batchGetCommitsCallback(OAIHttpRequestWorker *worker);
    void batchGetRepositoriesCallback(OAIHttpRequestWorker *worker);
    void createApprovalRuleTemplateCallback(OAIHttpRequestWorker *worker);
    void createBranchCallback(OAIHttpRequestWorker *worker);
    void createCommitCallback(OAIHttpRequestWorker *worker);
    void createPullRequestCallback(OAIHttpRequestWorker *worker);
    void createPullRequestApprovalRuleCallback(OAIHttpRequestWorker *worker);
    void createRepositoryCallback(OAIHttpRequestWorker *worker);
    void createUnreferencedMergeCommitCallback(OAIHttpRequestWorker *worker);
    void deleteApprovalRuleTemplateCallback(OAIHttpRequestWorker *worker);
    void deleteBranchCallback(OAIHttpRequestWorker *worker);
    void deleteCommentContentCallback(OAIHttpRequestWorker *worker);
    void deleteFileCallback(OAIHttpRequestWorker *worker);
    void deletePullRequestApprovalRuleCallback(OAIHttpRequestWorker *worker);
    void deleteRepositoryCallback(OAIHttpRequestWorker *worker);
    void describeMergeConflictsCallback(OAIHttpRequestWorker *worker);
    void describePullRequestEventsCallback(OAIHttpRequestWorker *worker);
    void disassociateApprovalRuleTemplateFromRepositoryCallback(OAIHttpRequestWorker *worker);
    void evaluatePullRequestApprovalRulesCallback(OAIHttpRequestWorker *worker);
    void getApprovalRuleTemplateCallback(OAIHttpRequestWorker *worker);
    void getBlobCallback(OAIHttpRequestWorker *worker);
    void getBranchCallback(OAIHttpRequestWorker *worker);
    void getCommentCallback(OAIHttpRequestWorker *worker);
    void getCommentReactionsCallback(OAIHttpRequestWorker *worker);
    void getCommentsForComparedCommitCallback(OAIHttpRequestWorker *worker);
    void getCommentsForPullRequestCallback(OAIHttpRequestWorker *worker);
    void getCommitCallback(OAIHttpRequestWorker *worker);
    void getDifferencesCallback(OAIHttpRequestWorker *worker);
    void getFileCallback(OAIHttpRequestWorker *worker);
    void getFolderCallback(OAIHttpRequestWorker *worker);
    void getMergeCommitCallback(OAIHttpRequestWorker *worker);
    void getMergeConflictsCallback(OAIHttpRequestWorker *worker);
    void getMergeOptionsCallback(OAIHttpRequestWorker *worker);
    void getPullRequestCallback(OAIHttpRequestWorker *worker);
    void getPullRequestApprovalStatesCallback(OAIHttpRequestWorker *worker);
    void getPullRequestOverrideStateCallback(OAIHttpRequestWorker *worker);
    void getRepositoryCallback(OAIHttpRequestWorker *worker);
    void getRepositoryTriggersCallback(OAIHttpRequestWorker *worker);
    void listApprovalRuleTemplatesCallback(OAIHttpRequestWorker *worker);
    void listAssociatedApprovalRuleTemplatesForRepositoryCallback(OAIHttpRequestWorker *worker);
    void listBranchesCallback(OAIHttpRequestWorker *worker);
    void listPullRequestsCallback(OAIHttpRequestWorker *worker);
    void listRepositoriesCallback(OAIHttpRequestWorker *worker);
    void listRepositoriesForApprovalRuleTemplateCallback(OAIHttpRequestWorker *worker);
    void listTagsForResourceCallback(OAIHttpRequestWorker *worker);
    void mergeBranchesByFastForwardCallback(OAIHttpRequestWorker *worker);
    void mergeBranchesBySquashCallback(OAIHttpRequestWorker *worker);
    void mergeBranchesByThreeWayCallback(OAIHttpRequestWorker *worker);
    void mergePullRequestByFastForwardCallback(OAIHttpRequestWorker *worker);
    void mergePullRequestBySquashCallback(OAIHttpRequestWorker *worker);
    void mergePullRequestByThreeWayCallback(OAIHttpRequestWorker *worker);
    void overridePullRequestApprovalRulesCallback(OAIHttpRequestWorker *worker);
    void postCommentForComparedCommitCallback(OAIHttpRequestWorker *worker);
    void postCommentForPullRequestCallback(OAIHttpRequestWorker *worker);
    void postCommentReplyCallback(OAIHttpRequestWorker *worker);
    void putCommentReactionCallback(OAIHttpRequestWorker *worker);
    void putFileCallback(OAIHttpRequestWorker *worker);
    void putRepositoryTriggersCallback(OAIHttpRequestWorker *worker);
    void tagResourceCallback(OAIHttpRequestWorker *worker);
    void testRepositoryTriggersCallback(OAIHttpRequestWorker *worker);
    void untagResourceCallback(OAIHttpRequestWorker *worker);
    void updateApprovalRuleTemplateContentCallback(OAIHttpRequestWorker *worker);
    void updateApprovalRuleTemplateDescriptionCallback(OAIHttpRequestWorker *worker);
    void updateApprovalRuleTemplateNameCallback(OAIHttpRequestWorker *worker);
    void updateCommentCallback(OAIHttpRequestWorker *worker);
    void updateDefaultBranchCallback(OAIHttpRequestWorker *worker);
    void updatePullRequestApprovalRuleContentCallback(OAIHttpRequestWorker *worker);
    void updatePullRequestApprovalStateCallback(OAIHttpRequestWorker *worker);
    void updatePullRequestDescriptionCallback(OAIHttpRequestWorker *worker);
    void updatePullRequestStatusCallback(OAIHttpRequestWorker *worker);
    void updatePullRequestTitleCallback(OAIHttpRequestWorker *worker);
    void updateRepositoryDescriptionCallback(OAIHttpRequestWorker *worker);
    void updateRepositoryNameCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void associateApprovalRuleTemplateWithRepositorySignal();
    void batchAssociateApprovalRuleTemplateWithRepositoriesSignal(OAIBatchAssociateApprovalRuleTemplateWithRepositoriesOutput summary);
    void batchDescribeMergeConflictsSignal(OAIBatchDescribeMergeConflictsOutput summary);
    void batchDisassociateApprovalRuleTemplateFromRepositoriesSignal(OAIBatchDisassociateApprovalRuleTemplateFromRepositoriesOutput summary);
    void batchGetCommitsSignal(OAIBatchGetCommitsOutput summary);
    void batchGetRepositoriesSignal(OAIBatchGetRepositoriesOutput summary);
    void createApprovalRuleTemplateSignal(OAICreateApprovalRuleTemplateOutput summary);
    void createBranchSignal();
    void createCommitSignal(OAICreateCommitOutput summary);
    void createPullRequestSignal(OAICreatePullRequestOutput summary);
    void createPullRequestApprovalRuleSignal(OAICreatePullRequestApprovalRuleOutput summary);
    void createRepositorySignal(OAICreateRepositoryOutput summary);
    void createUnreferencedMergeCommitSignal(OAICreateUnreferencedMergeCommitOutput summary);
    void deleteApprovalRuleTemplateSignal(OAIDeleteApprovalRuleTemplateOutput summary);
    void deleteBranchSignal(OAIDeleteBranchOutput summary);
    void deleteCommentContentSignal(OAIDeleteCommentContentOutput summary);
    void deleteFileSignal(OAIDeleteFileOutput summary);
    void deletePullRequestApprovalRuleSignal(OAIDeletePullRequestApprovalRuleOutput summary);
    void deleteRepositorySignal(OAIDeleteRepositoryOutput summary);
    void describeMergeConflictsSignal(OAIDescribeMergeConflictsOutput summary);
    void describePullRequestEventsSignal(OAIDescribePullRequestEventsOutput summary);
    void disassociateApprovalRuleTemplateFromRepositorySignal();
    void evaluatePullRequestApprovalRulesSignal(OAIEvaluatePullRequestApprovalRulesOutput summary);
    void getApprovalRuleTemplateSignal(OAIGetApprovalRuleTemplateOutput summary);
    void getBlobSignal(OAIGetBlobOutput summary);
    void getBranchSignal(OAIGetBranchOutput summary);
    void getCommentSignal(OAIGetCommentOutput summary);
    void getCommentReactionsSignal(OAIGetCommentReactionsOutput summary);
    void getCommentsForComparedCommitSignal(OAIGetCommentsForComparedCommitOutput summary);
    void getCommentsForPullRequestSignal(OAIGetCommentsForPullRequestOutput summary);
    void getCommitSignal(OAIGetCommitOutput summary);
    void getDifferencesSignal(OAIGetDifferencesOutput summary);
    void getFileSignal(OAIGetFileOutput summary);
    void getFolderSignal(OAIGetFolderOutput summary);
    void getMergeCommitSignal(OAIGetMergeCommitOutput summary);
    void getMergeConflictsSignal(OAIGetMergeConflictsOutput summary);
    void getMergeOptionsSignal(OAIGetMergeOptionsOutput summary);
    void getPullRequestSignal(OAIGetPullRequestOutput summary);
    void getPullRequestApprovalStatesSignal(OAIGetPullRequestApprovalStatesOutput summary);
    void getPullRequestOverrideStateSignal(OAIGetPullRequestOverrideStateOutput summary);
    void getRepositorySignal(OAIGetRepositoryOutput summary);
    void getRepositoryTriggersSignal(OAIGetRepositoryTriggersOutput summary);
    void listApprovalRuleTemplatesSignal(OAIListApprovalRuleTemplatesOutput summary);
    void listAssociatedApprovalRuleTemplatesForRepositorySignal(OAIListAssociatedApprovalRuleTemplatesForRepositoryOutput summary);
    void listBranchesSignal(OAIListBranchesOutput summary);
    void listPullRequestsSignal(OAIListPullRequestsOutput summary);
    void listRepositoriesSignal(OAIListRepositoriesOutput summary);
    void listRepositoriesForApprovalRuleTemplateSignal(OAIListRepositoriesForApprovalRuleTemplateOutput summary);
    void listTagsForResourceSignal(OAIListTagsForResourceOutput summary);
    void mergeBranchesByFastForwardSignal(OAIMergeBranchesByFastForwardOutput summary);
    void mergeBranchesBySquashSignal(OAIMergeBranchesBySquashOutput summary);
    void mergeBranchesByThreeWaySignal(OAIMergeBranchesByThreeWayOutput summary);
    void mergePullRequestByFastForwardSignal(OAIMergePullRequestByFastForwardOutput summary);
    void mergePullRequestBySquashSignal(OAIMergePullRequestBySquashOutput summary);
    void mergePullRequestByThreeWaySignal(OAIMergePullRequestByThreeWayOutput summary);
    void overridePullRequestApprovalRulesSignal();
    void postCommentForComparedCommitSignal(OAIPostCommentForComparedCommitOutput summary);
    void postCommentForPullRequestSignal(OAIPostCommentForPullRequestOutput summary);
    void postCommentReplySignal(OAIPostCommentReplyOutput summary);
    void putCommentReactionSignal();
    void putFileSignal(OAIPutFileOutput summary);
    void putRepositoryTriggersSignal(OAIPutRepositoryTriggersOutput summary);
    void tagResourceSignal();
    void testRepositoryTriggersSignal(OAITestRepositoryTriggersOutput summary);
    void untagResourceSignal();
    void updateApprovalRuleTemplateContentSignal(OAIUpdateApprovalRuleTemplateContentOutput summary);
    void updateApprovalRuleTemplateDescriptionSignal(OAIUpdateApprovalRuleTemplateDescriptionOutput summary);
    void updateApprovalRuleTemplateNameSignal(OAIUpdateApprovalRuleTemplateNameOutput summary);
    void updateCommentSignal(OAIUpdateCommentOutput summary);
    void updateDefaultBranchSignal();
    void updatePullRequestApprovalRuleContentSignal(OAIUpdatePullRequestApprovalRuleContentOutput summary);
    void updatePullRequestApprovalStateSignal();
    void updatePullRequestDescriptionSignal(OAIUpdatePullRequestDescriptionOutput summary);
    void updatePullRequestStatusSignal(OAIUpdatePullRequestStatusOutput summary);
    void updatePullRequestTitleSignal(OAIUpdatePullRequestTitleOutput summary);
    void updateRepositoryDescriptionSignal();
    void updateRepositoryNameSignal();


    void associateApprovalRuleTemplateWithRepositorySignalFull(OAIHttpRequestWorker *worker);
    void batchAssociateApprovalRuleTemplateWithRepositoriesSignalFull(OAIHttpRequestWorker *worker, OAIBatchAssociateApprovalRuleTemplateWithRepositoriesOutput summary);
    void batchDescribeMergeConflictsSignalFull(OAIHttpRequestWorker *worker, OAIBatchDescribeMergeConflictsOutput summary);
    void batchDisassociateApprovalRuleTemplateFromRepositoriesSignalFull(OAIHttpRequestWorker *worker, OAIBatchDisassociateApprovalRuleTemplateFromRepositoriesOutput summary);
    void batchGetCommitsSignalFull(OAIHttpRequestWorker *worker, OAIBatchGetCommitsOutput summary);
    void batchGetRepositoriesSignalFull(OAIHttpRequestWorker *worker, OAIBatchGetRepositoriesOutput summary);
    void createApprovalRuleTemplateSignalFull(OAIHttpRequestWorker *worker, OAICreateApprovalRuleTemplateOutput summary);
    void createBranchSignalFull(OAIHttpRequestWorker *worker);
    void createCommitSignalFull(OAIHttpRequestWorker *worker, OAICreateCommitOutput summary);
    void createPullRequestSignalFull(OAIHttpRequestWorker *worker, OAICreatePullRequestOutput summary);
    void createPullRequestApprovalRuleSignalFull(OAIHttpRequestWorker *worker, OAICreatePullRequestApprovalRuleOutput summary);
    void createRepositorySignalFull(OAIHttpRequestWorker *worker, OAICreateRepositoryOutput summary);
    void createUnreferencedMergeCommitSignalFull(OAIHttpRequestWorker *worker, OAICreateUnreferencedMergeCommitOutput summary);
    void deleteApprovalRuleTemplateSignalFull(OAIHttpRequestWorker *worker, OAIDeleteApprovalRuleTemplateOutput summary);
    void deleteBranchSignalFull(OAIHttpRequestWorker *worker, OAIDeleteBranchOutput summary);
    void deleteCommentContentSignalFull(OAIHttpRequestWorker *worker, OAIDeleteCommentContentOutput summary);
    void deleteFileSignalFull(OAIHttpRequestWorker *worker, OAIDeleteFileOutput summary);
    void deletePullRequestApprovalRuleSignalFull(OAIHttpRequestWorker *worker, OAIDeletePullRequestApprovalRuleOutput summary);
    void deleteRepositorySignalFull(OAIHttpRequestWorker *worker, OAIDeleteRepositoryOutput summary);
    void describeMergeConflictsSignalFull(OAIHttpRequestWorker *worker, OAIDescribeMergeConflictsOutput summary);
    void describePullRequestEventsSignalFull(OAIHttpRequestWorker *worker, OAIDescribePullRequestEventsOutput summary);
    void disassociateApprovalRuleTemplateFromRepositorySignalFull(OAIHttpRequestWorker *worker);
    void evaluatePullRequestApprovalRulesSignalFull(OAIHttpRequestWorker *worker, OAIEvaluatePullRequestApprovalRulesOutput summary);
    void getApprovalRuleTemplateSignalFull(OAIHttpRequestWorker *worker, OAIGetApprovalRuleTemplateOutput summary);
    void getBlobSignalFull(OAIHttpRequestWorker *worker, OAIGetBlobOutput summary);
    void getBranchSignalFull(OAIHttpRequestWorker *worker, OAIGetBranchOutput summary);
    void getCommentSignalFull(OAIHttpRequestWorker *worker, OAIGetCommentOutput summary);
    void getCommentReactionsSignalFull(OAIHttpRequestWorker *worker, OAIGetCommentReactionsOutput summary);
    void getCommentsForComparedCommitSignalFull(OAIHttpRequestWorker *worker, OAIGetCommentsForComparedCommitOutput summary);
    void getCommentsForPullRequestSignalFull(OAIHttpRequestWorker *worker, OAIGetCommentsForPullRequestOutput summary);
    void getCommitSignalFull(OAIHttpRequestWorker *worker, OAIGetCommitOutput summary);
    void getDifferencesSignalFull(OAIHttpRequestWorker *worker, OAIGetDifferencesOutput summary);
    void getFileSignalFull(OAIHttpRequestWorker *worker, OAIGetFileOutput summary);
    void getFolderSignalFull(OAIHttpRequestWorker *worker, OAIGetFolderOutput summary);
    void getMergeCommitSignalFull(OAIHttpRequestWorker *worker, OAIGetMergeCommitOutput summary);
    void getMergeConflictsSignalFull(OAIHttpRequestWorker *worker, OAIGetMergeConflictsOutput summary);
    void getMergeOptionsSignalFull(OAIHttpRequestWorker *worker, OAIGetMergeOptionsOutput summary);
    void getPullRequestSignalFull(OAIHttpRequestWorker *worker, OAIGetPullRequestOutput summary);
    void getPullRequestApprovalStatesSignalFull(OAIHttpRequestWorker *worker, OAIGetPullRequestApprovalStatesOutput summary);
    void getPullRequestOverrideStateSignalFull(OAIHttpRequestWorker *worker, OAIGetPullRequestOverrideStateOutput summary);
    void getRepositorySignalFull(OAIHttpRequestWorker *worker, OAIGetRepositoryOutput summary);
    void getRepositoryTriggersSignalFull(OAIHttpRequestWorker *worker, OAIGetRepositoryTriggersOutput summary);
    void listApprovalRuleTemplatesSignalFull(OAIHttpRequestWorker *worker, OAIListApprovalRuleTemplatesOutput summary);
    void listAssociatedApprovalRuleTemplatesForRepositorySignalFull(OAIHttpRequestWorker *worker, OAIListAssociatedApprovalRuleTemplatesForRepositoryOutput summary);
    void listBranchesSignalFull(OAIHttpRequestWorker *worker, OAIListBranchesOutput summary);
    void listPullRequestsSignalFull(OAIHttpRequestWorker *worker, OAIListPullRequestsOutput summary);
    void listRepositoriesSignalFull(OAIHttpRequestWorker *worker, OAIListRepositoriesOutput summary);
    void listRepositoriesForApprovalRuleTemplateSignalFull(OAIHttpRequestWorker *worker, OAIListRepositoriesForApprovalRuleTemplateOutput summary);
    void listTagsForResourceSignalFull(OAIHttpRequestWorker *worker, OAIListTagsForResourceOutput summary);
    void mergeBranchesByFastForwardSignalFull(OAIHttpRequestWorker *worker, OAIMergeBranchesByFastForwardOutput summary);
    void mergeBranchesBySquashSignalFull(OAIHttpRequestWorker *worker, OAIMergeBranchesBySquashOutput summary);
    void mergeBranchesByThreeWaySignalFull(OAIHttpRequestWorker *worker, OAIMergeBranchesByThreeWayOutput summary);
    void mergePullRequestByFastForwardSignalFull(OAIHttpRequestWorker *worker, OAIMergePullRequestByFastForwardOutput summary);
    void mergePullRequestBySquashSignalFull(OAIHttpRequestWorker *worker, OAIMergePullRequestBySquashOutput summary);
    void mergePullRequestByThreeWaySignalFull(OAIHttpRequestWorker *worker, OAIMergePullRequestByThreeWayOutput summary);
    void overridePullRequestApprovalRulesSignalFull(OAIHttpRequestWorker *worker);
    void postCommentForComparedCommitSignalFull(OAIHttpRequestWorker *worker, OAIPostCommentForComparedCommitOutput summary);
    void postCommentForPullRequestSignalFull(OAIHttpRequestWorker *worker, OAIPostCommentForPullRequestOutput summary);
    void postCommentReplySignalFull(OAIHttpRequestWorker *worker, OAIPostCommentReplyOutput summary);
    void putCommentReactionSignalFull(OAIHttpRequestWorker *worker);
    void putFileSignalFull(OAIHttpRequestWorker *worker, OAIPutFileOutput summary);
    void putRepositoryTriggersSignalFull(OAIHttpRequestWorker *worker, OAIPutRepositoryTriggersOutput summary);
    void tagResourceSignalFull(OAIHttpRequestWorker *worker);
    void testRepositoryTriggersSignalFull(OAIHttpRequestWorker *worker, OAITestRepositoryTriggersOutput summary);
    void untagResourceSignalFull(OAIHttpRequestWorker *worker);
    void updateApprovalRuleTemplateContentSignalFull(OAIHttpRequestWorker *worker, OAIUpdateApprovalRuleTemplateContentOutput summary);
    void updateApprovalRuleTemplateDescriptionSignalFull(OAIHttpRequestWorker *worker, OAIUpdateApprovalRuleTemplateDescriptionOutput summary);
    void updateApprovalRuleTemplateNameSignalFull(OAIHttpRequestWorker *worker, OAIUpdateApprovalRuleTemplateNameOutput summary);
    void updateCommentSignalFull(OAIHttpRequestWorker *worker, OAIUpdateCommentOutput summary);
    void updateDefaultBranchSignalFull(OAIHttpRequestWorker *worker);
    void updatePullRequestApprovalRuleContentSignalFull(OAIHttpRequestWorker *worker, OAIUpdatePullRequestApprovalRuleContentOutput summary);
    void updatePullRequestApprovalStateSignalFull(OAIHttpRequestWorker *worker);
    void updatePullRequestDescriptionSignalFull(OAIHttpRequestWorker *worker, OAIUpdatePullRequestDescriptionOutput summary);
    void updatePullRequestStatusSignalFull(OAIHttpRequestWorker *worker, OAIUpdatePullRequestStatusOutput summary);
    void updatePullRequestTitleSignalFull(OAIHttpRequestWorker *worker, OAIUpdatePullRequestTitleOutput summary);
    void updateRepositoryDescriptionSignalFull(OAIHttpRequestWorker *worker);
    void updateRepositoryNameSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use associateApprovalRuleTemplateWithRepositorySignalError() instead")
    void associateApprovalRuleTemplateWithRepositorySignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void associateApprovalRuleTemplateWithRepositorySignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use batchAssociateApprovalRuleTemplateWithRepositoriesSignalError() instead")
    void batchAssociateApprovalRuleTemplateWithRepositoriesSignalE(OAIBatchAssociateApprovalRuleTemplateWithRepositoriesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void batchAssociateApprovalRuleTemplateWithRepositoriesSignalError(OAIBatchAssociateApprovalRuleTemplateWithRepositoriesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use batchDescribeMergeConflictsSignalError() instead")
    void batchDescribeMergeConflictsSignalE(OAIBatchDescribeMergeConflictsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void batchDescribeMergeConflictsSignalError(OAIBatchDescribeMergeConflictsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use batchDisassociateApprovalRuleTemplateFromRepositoriesSignalError() instead")
    void batchDisassociateApprovalRuleTemplateFromRepositoriesSignalE(OAIBatchDisassociateApprovalRuleTemplateFromRepositoriesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void batchDisassociateApprovalRuleTemplateFromRepositoriesSignalError(OAIBatchDisassociateApprovalRuleTemplateFromRepositoriesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use batchGetCommitsSignalError() instead")
    void batchGetCommitsSignalE(OAIBatchGetCommitsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void batchGetCommitsSignalError(OAIBatchGetCommitsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use batchGetRepositoriesSignalError() instead")
    void batchGetRepositoriesSignalE(OAIBatchGetRepositoriesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void batchGetRepositoriesSignalError(OAIBatchGetRepositoriesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createApprovalRuleTemplateSignalError() instead")
    void createApprovalRuleTemplateSignalE(OAICreateApprovalRuleTemplateOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createApprovalRuleTemplateSignalError(OAICreateApprovalRuleTemplateOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createBranchSignalError() instead")
    void createBranchSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void createBranchSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createCommitSignalError() instead")
    void createCommitSignalE(OAICreateCommitOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createCommitSignalError(OAICreateCommitOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createPullRequestSignalError() instead")
    void createPullRequestSignalE(OAICreatePullRequestOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createPullRequestSignalError(OAICreatePullRequestOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createPullRequestApprovalRuleSignalError() instead")
    void createPullRequestApprovalRuleSignalE(OAICreatePullRequestApprovalRuleOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createPullRequestApprovalRuleSignalError(OAICreatePullRequestApprovalRuleOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createRepositorySignalError() instead")
    void createRepositorySignalE(OAICreateRepositoryOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createRepositorySignalError(OAICreateRepositoryOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createUnreferencedMergeCommitSignalError() instead")
    void createUnreferencedMergeCommitSignalE(OAICreateUnreferencedMergeCommitOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createUnreferencedMergeCommitSignalError(OAICreateUnreferencedMergeCommitOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteApprovalRuleTemplateSignalError() instead")
    void deleteApprovalRuleTemplateSignalE(OAIDeleteApprovalRuleTemplateOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteApprovalRuleTemplateSignalError(OAIDeleteApprovalRuleTemplateOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteBranchSignalError() instead")
    void deleteBranchSignalE(OAIDeleteBranchOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteBranchSignalError(OAIDeleteBranchOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteCommentContentSignalError() instead")
    void deleteCommentContentSignalE(OAIDeleteCommentContentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteCommentContentSignalError(OAIDeleteCommentContentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteFileSignalError() instead")
    void deleteFileSignalE(OAIDeleteFileOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteFileSignalError(OAIDeleteFileOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deletePullRequestApprovalRuleSignalError() instead")
    void deletePullRequestApprovalRuleSignalE(OAIDeletePullRequestApprovalRuleOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deletePullRequestApprovalRuleSignalError(OAIDeletePullRequestApprovalRuleOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteRepositorySignalError() instead")
    void deleteRepositorySignalE(OAIDeleteRepositoryOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteRepositorySignalError(OAIDeleteRepositoryOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use describeMergeConflictsSignalError() instead")
    void describeMergeConflictsSignalE(OAIDescribeMergeConflictsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void describeMergeConflictsSignalError(OAIDescribeMergeConflictsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use describePullRequestEventsSignalError() instead")
    void describePullRequestEventsSignalE(OAIDescribePullRequestEventsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void describePullRequestEventsSignalError(OAIDescribePullRequestEventsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use disassociateApprovalRuleTemplateFromRepositorySignalError() instead")
    void disassociateApprovalRuleTemplateFromRepositorySignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void disassociateApprovalRuleTemplateFromRepositorySignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use evaluatePullRequestApprovalRulesSignalError() instead")
    void evaluatePullRequestApprovalRulesSignalE(OAIEvaluatePullRequestApprovalRulesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void evaluatePullRequestApprovalRulesSignalError(OAIEvaluatePullRequestApprovalRulesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getApprovalRuleTemplateSignalError() instead")
    void getApprovalRuleTemplateSignalE(OAIGetApprovalRuleTemplateOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getApprovalRuleTemplateSignalError(OAIGetApprovalRuleTemplateOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getBlobSignalError() instead")
    void getBlobSignalE(OAIGetBlobOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getBlobSignalError(OAIGetBlobOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getBranchSignalError() instead")
    void getBranchSignalE(OAIGetBranchOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getBranchSignalError(OAIGetBranchOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCommentSignalError() instead")
    void getCommentSignalE(OAIGetCommentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getCommentSignalError(OAIGetCommentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCommentReactionsSignalError() instead")
    void getCommentReactionsSignalE(OAIGetCommentReactionsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getCommentReactionsSignalError(OAIGetCommentReactionsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCommentsForComparedCommitSignalError() instead")
    void getCommentsForComparedCommitSignalE(OAIGetCommentsForComparedCommitOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getCommentsForComparedCommitSignalError(OAIGetCommentsForComparedCommitOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCommentsForPullRequestSignalError() instead")
    void getCommentsForPullRequestSignalE(OAIGetCommentsForPullRequestOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getCommentsForPullRequestSignalError(OAIGetCommentsForPullRequestOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCommitSignalError() instead")
    void getCommitSignalE(OAIGetCommitOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getCommitSignalError(OAIGetCommitOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDifferencesSignalError() instead")
    void getDifferencesSignalE(OAIGetDifferencesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDifferencesSignalError(OAIGetDifferencesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFileSignalError() instead")
    void getFileSignalE(OAIGetFileOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getFileSignalError(OAIGetFileOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFolderSignalError() instead")
    void getFolderSignalE(OAIGetFolderOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getFolderSignalError(OAIGetFolderOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMergeCommitSignalError() instead")
    void getMergeCommitSignalE(OAIGetMergeCommitOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMergeCommitSignalError(OAIGetMergeCommitOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMergeConflictsSignalError() instead")
    void getMergeConflictsSignalE(OAIGetMergeConflictsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMergeConflictsSignalError(OAIGetMergeConflictsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMergeOptionsSignalError() instead")
    void getMergeOptionsSignalE(OAIGetMergeOptionsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMergeOptionsSignalError(OAIGetMergeOptionsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPullRequestSignalError() instead")
    void getPullRequestSignalE(OAIGetPullRequestOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPullRequestSignalError(OAIGetPullRequestOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPullRequestApprovalStatesSignalError() instead")
    void getPullRequestApprovalStatesSignalE(OAIGetPullRequestApprovalStatesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPullRequestApprovalStatesSignalError(OAIGetPullRequestApprovalStatesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPullRequestOverrideStateSignalError() instead")
    void getPullRequestOverrideStateSignalE(OAIGetPullRequestOverrideStateOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPullRequestOverrideStateSignalError(OAIGetPullRequestOverrideStateOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRepositorySignalError() instead")
    void getRepositorySignalE(OAIGetRepositoryOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getRepositorySignalError(OAIGetRepositoryOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRepositoryTriggersSignalError() instead")
    void getRepositoryTriggersSignalE(OAIGetRepositoryTriggersOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getRepositoryTriggersSignalError(OAIGetRepositoryTriggersOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listApprovalRuleTemplatesSignalError() instead")
    void listApprovalRuleTemplatesSignalE(OAIListApprovalRuleTemplatesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listApprovalRuleTemplatesSignalError(OAIListApprovalRuleTemplatesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listAssociatedApprovalRuleTemplatesForRepositorySignalError() instead")
    void listAssociatedApprovalRuleTemplatesForRepositorySignalE(OAIListAssociatedApprovalRuleTemplatesForRepositoryOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listAssociatedApprovalRuleTemplatesForRepositorySignalError(OAIListAssociatedApprovalRuleTemplatesForRepositoryOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listBranchesSignalError() instead")
    void listBranchesSignalE(OAIListBranchesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listBranchesSignalError(OAIListBranchesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listPullRequestsSignalError() instead")
    void listPullRequestsSignalE(OAIListPullRequestsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listPullRequestsSignalError(OAIListPullRequestsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRepositoriesSignalError() instead")
    void listRepositoriesSignalE(OAIListRepositoriesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listRepositoriesSignalError(OAIListRepositoriesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRepositoriesForApprovalRuleTemplateSignalError() instead")
    void listRepositoriesForApprovalRuleTemplateSignalE(OAIListRepositoriesForApprovalRuleTemplateOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listRepositoriesForApprovalRuleTemplateSignalError(OAIListRepositoriesForApprovalRuleTemplateOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listTagsForResourceSignalError() instead")
    void listTagsForResourceSignalE(OAIListTagsForResourceOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listTagsForResourceSignalError(OAIListTagsForResourceOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use mergeBranchesByFastForwardSignalError() instead")
    void mergeBranchesByFastForwardSignalE(OAIMergeBranchesByFastForwardOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void mergeBranchesByFastForwardSignalError(OAIMergeBranchesByFastForwardOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use mergeBranchesBySquashSignalError() instead")
    void mergeBranchesBySquashSignalE(OAIMergeBranchesBySquashOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void mergeBranchesBySquashSignalError(OAIMergeBranchesBySquashOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use mergeBranchesByThreeWaySignalError() instead")
    void mergeBranchesByThreeWaySignalE(OAIMergeBranchesByThreeWayOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void mergeBranchesByThreeWaySignalError(OAIMergeBranchesByThreeWayOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use mergePullRequestByFastForwardSignalError() instead")
    void mergePullRequestByFastForwardSignalE(OAIMergePullRequestByFastForwardOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void mergePullRequestByFastForwardSignalError(OAIMergePullRequestByFastForwardOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use mergePullRequestBySquashSignalError() instead")
    void mergePullRequestBySquashSignalE(OAIMergePullRequestBySquashOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void mergePullRequestBySquashSignalError(OAIMergePullRequestBySquashOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use mergePullRequestByThreeWaySignalError() instead")
    void mergePullRequestByThreeWaySignalE(OAIMergePullRequestByThreeWayOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void mergePullRequestByThreeWaySignalError(OAIMergePullRequestByThreeWayOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use overridePullRequestApprovalRulesSignalError() instead")
    void overridePullRequestApprovalRulesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void overridePullRequestApprovalRulesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postCommentForComparedCommitSignalError() instead")
    void postCommentForComparedCommitSignalE(OAIPostCommentForComparedCommitOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postCommentForComparedCommitSignalError(OAIPostCommentForComparedCommitOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postCommentForPullRequestSignalError() instead")
    void postCommentForPullRequestSignalE(OAIPostCommentForPullRequestOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postCommentForPullRequestSignalError(OAIPostCommentForPullRequestOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postCommentReplySignalError() instead")
    void postCommentReplySignalE(OAIPostCommentReplyOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postCommentReplySignalError(OAIPostCommentReplyOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putCommentReactionSignalError() instead")
    void putCommentReactionSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void putCommentReactionSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putFileSignalError() instead")
    void putFileSignalE(OAIPutFileOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void putFileSignalError(OAIPutFileOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putRepositoryTriggersSignalError() instead")
    void putRepositoryTriggersSignalE(OAIPutRepositoryTriggersOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void putRepositoryTriggersSignalError(OAIPutRepositoryTriggersOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tagResourceSignalError() instead")
    void tagResourceSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void tagResourceSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use testRepositoryTriggersSignalError() instead")
    void testRepositoryTriggersSignalE(OAITestRepositoryTriggersOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void testRepositoryTriggersSignalError(OAITestRepositoryTriggersOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use untagResourceSignalError() instead")
    void untagResourceSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void untagResourceSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateApprovalRuleTemplateContentSignalError() instead")
    void updateApprovalRuleTemplateContentSignalE(OAIUpdateApprovalRuleTemplateContentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateApprovalRuleTemplateContentSignalError(OAIUpdateApprovalRuleTemplateContentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateApprovalRuleTemplateDescriptionSignalError() instead")
    void updateApprovalRuleTemplateDescriptionSignalE(OAIUpdateApprovalRuleTemplateDescriptionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateApprovalRuleTemplateDescriptionSignalError(OAIUpdateApprovalRuleTemplateDescriptionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateApprovalRuleTemplateNameSignalError() instead")
    void updateApprovalRuleTemplateNameSignalE(OAIUpdateApprovalRuleTemplateNameOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateApprovalRuleTemplateNameSignalError(OAIUpdateApprovalRuleTemplateNameOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateCommentSignalError() instead")
    void updateCommentSignalE(OAIUpdateCommentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateCommentSignalError(OAIUpdateCommentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDefaultBranchSignalError() instead")
    void updateDefaultBranchSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void updateDefaultBranchSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updatePullRequestApprovalRuleContentSignalError() instead")
    void updatePullRequestApprovalRuleContentSignalE(OAIUpdatePullRequestApprovalRuleContentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updatePullRequestApprovalRuleContentSignalError(OAIUpdatePullRequestApprovalRuleContentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updatePullRequestApprovalStateSignalError() instead")
    void updatePullRequestApprovalStateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void updatePullRequestApprovalStateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updatePullRequestDescriptionSignalError() instead")
    void updatePullRequestDescriptionSignalE(OAIUpdatePullRequestDescriptionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updatePullRequestDescriptionSignalError(OAIUpdatePullRequestDescriptionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updatePullRequestStatusSignalError() instead")
    void updatePullRequestStatusSignalE(OAIUpdatePullRequestStatusOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updatePullRequestStatusSignalError(OAIUpdatePullRequestStatusOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updatePullRequestTitleSignalError() instead")
    void updatePullRequestTitleSignalE(OAIUpdatePullRequestTitleOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updatePullRequestTitleSignalError(OAIUpdatePullRequestTitleOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateRepositoryDescriptionSignalError() instead")
    void updateRepositoryDescriptionSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void updateRepositoryDescriptionSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateRepositoryNameSignalError() instead")
    void updateRepositoryNameSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void updateRepositoryNameSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use associateApprovalRuleTemplateWithRepositorySignalErrorFull() instead")
    void associateApprovalRuleTemplateWithRepositorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void associateApprovalRuleTemplateWithRepositorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use batchAssociateApprovalRuleTemplateWithRepositoriesSignalErrorFull() instead")
    void batchAssociateApprovalRuleTemplateWithRepositoriesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void batchAssociateApprovalRuleTemplateWithRepositoriesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use batchDescribeMergeConflictsSignalErrorFull() instead")
    void batchDescribeMergeConflictsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void batchDescribeMergeConflictsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use batchDisassociateApprovalRuleTemplateFromRepositoriesSignalErrorFull() instead")
    void batchDisassociateApprovalRuleTemplateFromRepositoriesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void batchDisassociateApprovalRuleTemplateFromRepositoriesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use batchGetCommitsSignalErrorFull() instead")
    void batchGetCommitsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void batchGetCommitsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use batchGetRepositoriesSignalErrorFull() instead")
    void batchGetRepositoriesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void batchGetRepositoriesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createApprovalRuleTemplateSignalErrorFull() instead")
    void createApprovalRuleTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createApprovalRuleTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createBranchSignalErrorFull() instead")
    void createBranchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createBranchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createCommitSignalErrorFull() instead")
    void createCommitSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createCommitSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createPullRequestSignalErrorFull() instead")
    void createPullRequestSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createPullRequestSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createPullRequestApprovalRuleSignalErrorFull() instead")
    void createPullRequestApprovalRuleSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createPullRequestApprovalRuleSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createRepositorySignalErrorFull() instead")
    void createRepositorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createRepositorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createUnreferencedMergeCommitSignalErrorFull() instead")
    void createUnreferencedMergeCommitSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createUnreferencedMergeCommitSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteApprovalRuleTemplateSignalErrorFull() instead")
    void deleteApprovalRuleTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteApprovalRuleTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteBranchSignalErrorFull() instead")
    void deleteBranchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteBranchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteCommentContentSignalErrorFull() instead")
    void deleteCommentContentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteCommentContentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteFileSignalErrorFull() instead")
    void deleteFileSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteFileSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deletePullRequestApprovalRuleSignalErrorFull() instead")
    void deletePullRequestApprovalRuleSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deletePullRequestApprovalRuleSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteRepositorySignalErrorFull() instead")
    void deleteRepositorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteRepositorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use describeMergeConflictsSignalErrorFull() instead")
    void describeMergeConflictsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void describeMergeConflictsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use describePullRequestEventsSignalErrorFull() instead")
    void describePullRequestEventsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void describePullRequestEventsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use disassociateApprovalRuleTemplateFromRepositorySignalErrorFull() instead")
    void disassociateApprovalRuleTemplateFromRepositorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void disassociateApprovalRuleTemplateFromRepositorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use evaluatePullRequestApprovalRulesSignalErrorFull() instead")
    void evaluatePullRequestApprovalRulesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void evaluatePullRequestApprovalRulesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getApprovalRuleTemplateSignalErrorFull() instead")
    void getApprovalRuleTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getApprovalRuleTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getBlobSignalErrorFull() instead")
    void getBlobSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getBlobSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getBranchSignalErrorFull() instead")
    void getBranchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getBranchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCommentSignalErrorFull() instead")
    void getCommentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCommentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCommentReactionsSignalErrorFull() instead")
    void getCommentReactionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCommentReactionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCommentsForComparedCommitSignalErrorFull() instead")
    void getCommentsForComparedCommitSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCommentsForComparedCommitSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCommentsForPullRequestSignalErrorFull() instead")
    void getCommentsForPullRequestSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCommentsForPullRequestSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCommitSignalErrorFull() instead")
    void getCommitSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCommitSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDifferencesSignalErrorFull() instead")
    void getDifferencesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDifferencesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFileSignalErrorFull() instead")
    void getFileSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getFileSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFolderSignalErrorFull() instead")
    void getFolderSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getFolderSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMergeCommitSignalErrorFull() instead")
    void getMergeCommitSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMergeCommitSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMergeConflictsSignalErrorFull() instead")
    void getMergeConflictsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMergeConflictsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMergeOptionsSignalErrorFull() instead")
    void getMergeOptionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMergeOptionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPullRequestSignalErrorFull() instead")
    void getPullRequestSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPullRequestSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPullRequestApprovalStatesSignalErrorFull() instead")
    void getPullRequestApprovalStatesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPullRequestApprovalStatesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPullRequestOverrideStateSignalErrorFull() instead")
    void getPullRequestOverrideStateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPullRequestOverrideStateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRepositorySignalErrorFull() instead")
    void getRepositorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getRepositorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRepositoryTriggersSignalErrorFull() instead")
    void getRepositoryTriggersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getRepositoryTriggersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listApprovalRuleTemplatesSignalErrorFull() instead")
    void listApprovalRuleTemplatesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listApprovalRuleTemplatesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listAssociatedApprovalRuleTemplatesForRepositorySignalErrorFull() instead")
    void listAssociatedApprovalRuleTemplatesForRepositorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listAssociatedApprovalRuleTemplatesForRepositorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listBranchesSignalErrorFull() instead")
    void listBranchesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listBranchesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listPullRequestsSignalErrorFull() instead")
    void listPullRequestsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listPullRequestsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRepositoriesSignalErrorFull() instead")
    void listRepositoriesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listRepositoriesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRepositoriesForApprovalRuleTemplateSignalErrorFull() instead")
    void listRepositoriesForApprovalRuleTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listRepositoriesForApprovalRuleTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listTagsForResourceSignalErrorFull() instead")
    void listTagsForResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listTagsForResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use mergeBranchesByFastForwardSignalErrorFull() instead")
    void mergeBranchesByFastForwardSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void mergeBranchesByFastForwardSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use mergeBranchesBySquashSignalErrorFull() instead")
    void mergeBranchesBySquashSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void mergeBranchesBySquashSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use mergeBranchesByThreeWaySignalErrorFull() instead")
    void mergeBranchesByThreeWaySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void mergeBranchesByThreeWaySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use mergePullRequestByFastForwardSignalErrorFull() instead")
    void mergePullRequestByFastForwardSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void mergePullRequestByFastForwardSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use mergePullRequestBySquashSignalErrorFull() instead")
    void mergePullRequestBySquashSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void mergePullRequestBySquashSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use mergePullRequestByThreeWaySignalErrorFull() instead")
    void mergePullRequestByThreeWaySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void mergePullRequestByThreeWaySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use overridePullRequestApprovalRulesSignalErrorFull() instead")
    void overridePullRequestApprovalRulesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void overridePullRequestApprovalRulesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postCommentForComparedCommitSignalErrorFull() instead")
    void postCommentForComparedCommitSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postCommentForComparedCommitSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postCommentForPullRequestSignalErrorFull() instead")
    void postCommentForPullRequestSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postCommentForPullRequestSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postCommentReplySignalErrorFull() instead")
    void postCommentReplySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postCommentReplySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putCommentReactionSignalErrorFull() instead")
    void putCommentReactionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putCommentReactionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putFileSignalErrorFull() instead")
    void putFileSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putFileSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putRepositoryTriggersSignalErrorFull() instead")
    void putRepositoryTriggersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putRepositoryTriggersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tagResourceSignalErrorFull() instead")
    void tagResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tagResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use testRepositoryTriggersSignalErrorFull() instead")
    void testRepositoryTriggersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void testRepositoryTriggersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use untagResourceSignalErrorFull() instead")
    void untagResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void untagResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateApprovalRuleTemplateContentSignalErrorFull() instead")
    void updateApprovalRuleTemplateContentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateApprovalRuleTemplateContentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateApprovalRuleTemplateDescriptionSignalErrorFull() instead")
    void updateApprovalRuleTemplateDescriptionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateApprovalRuleTemplateDescriptionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateApprovalRuleTemplateNameSignalErrorFull() instead")
    void updateApprovalRuleTemplateNameSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateApprovalRuleTemplateNameSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateCommentSignalErrorFull() instead")
    void updateCommentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateCommentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDefaultBranchSignalErrorFull() instead")
    void updateDefaultBranchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDefaultBranchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updatePullRequestApprovalRuleContentSignalErrorFull() instead")
    void updatePullRequestApprovalRuleContentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updatePullRequestApprovalRuleContentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updatePullRequestApprovalStateSignalErrorFull() instead")
    void updatePullRequestApprovalStateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updatePullRequestApprovalStateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updatePullRequestDescriptionSignalErrorFull() instead")
    void updatePullRequestDescriptionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updatePullRequestDescriptionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updatePullRequestStatusSignalErrorFull() instead")
    void updatePullRequestStatusSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updatePullRequestStatusSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updatePullRequestTitleSignalErrorFull() instead")
    void updatePullRequestTitleSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updatePullRequestTitleSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateRepositoryDescriptionSignalErrorFull() instead")
    void updateRepositoryDescriptionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateRepositoryDescriptionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateRepositoryNameSignalErrorFull() instead")
    void updateRepositoryNameSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateRepositoryNameSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
