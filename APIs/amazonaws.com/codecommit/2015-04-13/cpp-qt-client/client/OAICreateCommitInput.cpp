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

#include "OAICreateCommitInput.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateCommitInput::OAICreateCommitInput(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateCommitInput::OAICreateCommitInput() {
    this->initializeModel();
}

OAICreateCommitInput::~OAICreateCommitInput() {}

void OAICreateCommitInput::initializeModel() {

    m_repository_name_isSet = false;
    m_repository_name_isValid = false;

    m_branch_name_isSet = false;
    m_branch_name_isValid = false;

    m_parent_commit_id_isSet = false;
    m_parent_commit_id_isValid = false;

    m_author_name_isSet = false;
    m_author_name_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_commit_message_isSet = false;
    m_commit_message_isValid = false;

    m_keep_empty_folders_isSet = false;
    m_keep_empty_folders_isValid = false;

    m_put_files_isSet = false;
    m_put_files_isValid = false;

    m_delete_files_isSet = false;
    m_delete_files_isValid = false;

    m_set_file_modes_isSet = false;
    m_set_file_modes_isValid = false;
}

void OAICreateCommitInput::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateCommitInput::fromJsonObject(QJsonObject json) {

    m_repository_name_isValid = ::OpenAPI::fromJsonValue(m_repository_name, json[QString("repositoryName")]);
    m_repository_name_isSet = !json[QString("repositoryName")].isNull() && m_repository_name_isValid;

    m_branch_name_isValid = ::OpenAPI::fromJsonValue(m_branch_name, json[QString("branchName")]);
    m_branch_name_isSet = !json[QString("branchName")].isNull() && m_branch_name_isValid;

    m_parent_commit_id_isValid = ::OpenAPI::fromJsonValue(m_parent_commit_id, json[QString("parentCommitId")]);
    m_parent_commit_id_isSet = !json[QString("parentCommitId")].isNull() && m_parent_commit_id_isValid;

    m_author_name_isValid = ::OpenAPI::fromJsonValue(m_author_name, json[QString("authorName")]);
    m_author_name_isSet = !json[QString("authorName")].isNull() && m_author_name_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_commit_message_isValid = ::OpenAPI::fromJsonValue(m_commit_message, json[QString("commitMessage")]);
    m_commit_message_isSet = !json[QString("commitMessage")].isNull() && m_commit_message_isValid;

    m_keep_empty_folders_isValid = ::OpenAPI::fromJsonValue(m_keep_empty_folders, json[QString("keepEmptyFolders")]);
    m_keep_empty_folders_isSet = !json[QString("keepEmptyFolders")].isNull() && m_keep_empty_folders_isValid;

    m_put_files_isValid = ::OpenAPI::fromJsonValue(m_put_files, json[QString("putFiles")]);
    m_put_files_isSet = !json[QString("putFiles")].isNull() && m_put_files_isValid;

    m_delete_files_isValid = ::OpenAPI::fromJsonValue(m_delete_files, json[QString("deleteFiles")]);
    m_delete_files_isSet = !json[QString("deleteFiles")].isNull() && m_delete_files_isValid;

    m_set_file_modes_isValid = ::OpenAPI::fromJsonValue(m_set_file_modes, json[QString("setFileModes")]);
    m_set_file_modes_isSet = !json[QString("setFileModes")].isNull() && m_set_file_modes_isValid;
}

QString OAICreateCommitInput::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateCommitInput::asJsonObject() const {
    QJsonObject obj;
    if (m_repository_name_isSet) {
        obj.insert(QString("repositoryName"), ::OpenAPI::toJsonValue(m_repository_name));
    }
    if (m_branch_name_isSet) {
        obj.insert(QString("branchName"), ::OpenAPI::toJsonValue(m_branch_name));
    }
    if (m_parent_commit_id_isSet) {
        obj.insert(QString("parentCommitId"), ::OpenAPI::toJsonValue(m_parent_commit_id));
    }
    if (m_author_name_isSet) {
        obj.insert(QString("authorName"), ::OpenAPI::toJsonValue(m_author_name));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_commit_message_isSet) {
        obj.insert(QString("commitMessage"), ::OpenAPI::toJsonValue(m_commit_message));
    }
    if (m_keep_empty_folders_isSet) {
        obj.insert(QString("keepEmptyFolders"), ::OpenAPI::toJsonValue(m_keep_empty_folders));
    }
    if (m_put_files.isSet()) {
        obj.insert(QString("putFiles"), ::OpenAPI::toJsonValue(m_put_files));
    }
    if (m_delete_files.isSet()) {
        obj.insert(QString("deleteFiles"), ::OpenAPI::toJsonValue(m_delete_files));
    }
    if (m_set_file_modes.isSet()) {
        obj.insert(QString("setFileModes"), ::OpenAPI::toJsonValue(m_set_file_modes));
    }
    return obj;
}

QString OAICreateCommitInput::getRepositoryName() const {
    return m_repository_name;
}
void OAICreateCommitInput::setRepositoryName(const QString &repository_name) {
    m_repository_name = repository_name;
    m_repository_name_isSet = true;
}

bool OAICreateCommitInput::is_repository_name_Set() const{
    return m_repository_name_isSet;
}

bool OAICreateCommitInput::is_repository_name_Valid() const{
    return m_repository_name_isValid;
}

QString OAICreateCommitInput::getBranchName() const {
    return m_branch_name;
}
void OAICreateCommitInput::setBranchName(const QString &branch_name) {
    m_branch_name = branch_name;
    m_branch_name_isSet = true;
}

bool OAICreateCommitInput::is_branch_name_Set() const{
    return m_branch_name_isSet;
}

bool OAICreateCommitInput::is_branch_name_Valid() const{
    return m_branch_name_isValid;
}

QString OAICreateCommitInput::getParentCommitId() const {
    return m_parent_commit_id;
}
void OAICreateCommitInput::setParentCommitId(const QString &parent_commit_id) {
    m_parent_commit_id = parent_commit_id;
    m_parent_commit_id_isSet = true;
}

bool OAICreateCommitInput::is_parent_commit_id_Set() const{
    return m_parent_commit_id_isSet;
}

bool OAICreateCommitInput::is_parent_commit_id_Valid() const{
    return m_parent_commit_id_isValid;
}

QString OAICreateCommitInput::getAuthorName() const {
    return m_author_name;
}
void OAICreateCommitInput::setAuthorName(const QString &author_name) {
    m_author_name = author_name;
    m_author_name_isSet = true;
}

bool OAICreateCommitInput::is_author_name_Set() const{
    return m_author_name_isSet;
}

bool OAICreateCommitInput::is_author_name_Valid() const{
    return m_author_name_isValid;
}

QString OAICreateCommitInput::getEmail() const {
    return m_email;
}
void OAICreateCommitInput::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAICreateCommitInput::is_email_Set() const{
    return m_email_isSet;
}

bool OAICreateCommitInput::is_email_Valid() const{
    return m_email_isValid;
}

QString OAICreateCommitInput::getCommitMessage() const {
    return m_commit_message;
}
void OAICreateCommitInput::setCommitMessage(const QString &commit_message) {
    m_commit_message = commit_message;
    m_commit_message_isSet = true;
}

bool OAICreateCommitInput::is_commit_message_Set() const{
    return m_commit_message_isSet;
}

bool OAICreateCommitInput::is_commit_message_Valid() const{
    return m_commit_message_isValid;
}

bool OAICreateCommitInput::getKeepEmptyFolders() const {
    return m_keep_empty_folders;
}
void OAICreateCommitInput::setKeepEmptyFolders(const bool &keep_empty_folders) {
    m_keep_empty_folders = keep_empty_folders;
    m_keep_empty_folders_isSet = true;
}

bool OAICreateCommitInput::is_keep_empty_folders_Set() const{
    return m_keep_empty_folders_isSet;
}

bool OAICreateCommitInput::is_keep_empty_folders_Valid() const{
    return m_keep_empty_folders_isValid;
}

QList OAICreateCommitInput::getPutFiles() const {
    return m_put_files;
}
void OAICreateCommitInput::setPutFiles(const QList &put_files) {
    m_put_files = put_files;
    m_put_files_isSet = true;
}

bool OAICreateCommitInput::is_put_files_Set() const{
    return m_put_files_isSet;
}

bool OAICreateCommitInput::is_put_files_Valid() const{
    return m_put_files_isValid;
}

QList OAICreateCommitInput::getDeleteFiles() const {
    return m_delete_files;
}
void OAICreateCommitInput::setDeleteFiles(const QList &delete_files) {
    m_delete_files = delete_files;
    m_delete_files_isSet = true;
}

bool OAICreateCommitInput::is_delete_files_Set() const{
    return m_delete_files_isSet;
}

bool OAICreateCommitInput::is_delete_files_Valid() const{
    return m_delete_files_isValid;
}

QList OAICreateCommitInput::getSetFileModes() const {
    return m_set_file_modes;
}
void OAICreateCommitInput::setSetFileModes(const QList &set_file_modes) {
    m_set_file_modes = set_file_modes;
    m_set_file_modes_isSet = true;
}

bool OAICreateCommitInput::is_set_file_modes_Set() const{
    return m_set_file_modes_isSet;
}

bool OAICreateCommitInput::is_set_file_modes_Valid() const{
    return m_set_file_modes_isValid;
}

bool OAICreateCommitInput::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_repository_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_branch_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_commit_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_author_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_commit_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_keep_empty_folders_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_put_files.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_delete_files.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_set_file_modes.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateCommitInput::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_repository_name_isValid && m_branch_name_isValid && true;
}

} // namespace OpenAPI
