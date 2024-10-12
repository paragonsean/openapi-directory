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

#include "OAIConflictMetadata.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConflictMetadata::OAIConflictMetadata(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConflictMetadata::OAIConflictMetadata() {
    this->initializeModel();
}

OAIConflictMetadata::~OAIConflictMetadata() {}

void OAIConflictMetadata::initializeModel() {

    m_file_path_isSet = false;
    m_file_path_isValid = false;

    m_file_sizes_isSet = false;
    m_file_sizes_isValid = false;

    m_file_modes_isSet = false;
    m_file_modes_isValid = false;

    m_object_types_isSet = false;
    m_object_types_isValid = false;

    m_number_of_conflicts_isSet = false;
    m_number_of_conflicts_isValid = false;

    m_is_binary_file_isSet = false;
    m_is_binary_file_isValid = false;

    m_content_conflict_isSet = false;
    m_content_conflict_isValid = false;

    m_file_mode_conflict_isSet = false;
    m_file_mode_conflict_isValid = false;

    m_object_type_conflict_isSet = false;
    m_object_type_conflict_isValid = false;

    m_merge_operations_isSet = false;
    m_merge_operations_isValid = false;
}

void OAIConflictMetadata::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConflictMetadata::fromJsonObject(QJsonObject json) {

    m_file_path_isValid = ::OpenAPI::fromJsonValue(m_file_path, json[QString("filePath")]);
    m_file_path_isSet = !json[QString("filePath")].isNull() && m_file_path_isValid;

    m_file_sizes_isValid = ::OpenAPI::fromJsonValue(m_file_sizes, json[QString("fileSizes")]);
    m_file_sizes_isSet = !json[QString("fileSizes")].isNull() && m_file_sizes_isValid;

    m_file_modes_isValid = ::OpenAPI::fromJsonValue(m_file_modes, json[QString("fileModes")]);
    m_file_modes_isSet = !json[QString("fileModes")].isNull() && m_file_modes_isValid;

    m_object_types_isValid = ::OpenAPI::fromJsonValue(m_object_types, json[QString("objectTypes")]);
    m_object_types_isSet = !json[QString("objectTypes")].isNull() && m_object_types_isValid;

    m_number_of_conflicts_isValid = ::OpenAPI::fromJsonValue(m_number_of_conflicts, json[QString("numberOfConflicts")]);
    m_number_of_conflicts_isSet = !json[QString("numberOfConflicts")].isNull() && m_number_of_conflicts_isValid;

    m_is_binary_file_isValid = ::OpenAPI::fromJsonValue(m_is_binary_file, json[QString("isBinaryFile")]);
    m_is_binary_file_isSet = !json[QString("isBinaryFile")].isNull() && m_is_binary_file_isValid;

    m_content_conflict_isValid = ::OpenAPI::fromJsonValue(m_content_conflict, json[QString("contentConflict")]);
    m_content_conflict_isSet = !json[QString("contentConflict")].isNull() && m_content_conflict_isValid;

    m_file_mode_conflict_isValid = ::OpenAPI::fromJsonValue(m_file_mode_conflict, json[QString("fileModeConflict")]);
    m_file_mode_conflict_isSet = !json[QString("fileModeConflict")].isNull() && m_file_mode_conflict_isValid;

    m_object_type_conflict_isValid = ::OpenAPI::fromJsonValue(m_object_type_conflict, json[QString("objectTypeConflict")]);
    m_object_type_conflict_isSet = !json[QString("objectTypeConflict")].isNull() && m_object_type_conflict_isValid;

    m_merge_operations_isValid = ::OpenAPI::fromJsonValue(m_merge_operations, json[QString("mergeOperations")]);
    m_merge_operations_isSet = !json[QString("mergeOperations")].isNull() && m_merge_operations_isValid;
}

QString OAIConflictMetadata::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConflictMetadata::asJsonObject() const {
    QJsonObject obj;
    if (m_file_path_isSet) {
        obj.insert(QString("filePath"), ::OpenAPI::toJsonValue(m_file_path));
    }
    if (m_file_sizes.isSet()) {
        obj.insert(QString("fileSizes"), ::OpenAPI::toJsonValue(m_file_sizes));
    }
    if (m_file_modes.isSet()) {
        obj.insert(QString("fileModes"), ::OpenAPI::toJsonValue(m_file_modes));
    }
    if (m_object_types.isSet()) {
        obj.insert(QString("objectTypes"), ::OpenAPI::toJsonValue(m_object_types));
    }
    if (m_number_of_conflicts_isSet) {
        obj.insert(QString("numberOfConflicts"), ::OpenAPI::toJsonValue(m_number_of_conflicts));
    }
    if (m_is_binary_file.isSet()) {
        obj.insert(QString("isBinaryFile"), ::OpenAPI::toJsonValue(m_is_binary_file));
    }
    if (m_content_conflict_isSet) {
        obj.insert(QString("contentConflict"), ::OpenAPI::toJsonValue(m_content_conflict));
    }
    if (m_file_mode_conflict_isSet) {
        obj.insert(QString("fileModeConflict"), ::OpenAPI::toJsonValue(m_file_mode_conflict));
    }
    if (m_object_type_conflict_isSet) {
        obj.insert(QString("objectTypeConflict"), ::OpenAPI::toJsonValue(m_object_type_conflict));
    }
    if (m_merge_operations.isSet()) {
        obj.insert(QString("mergeOperations"), ::OpenAPI::toJsonValue(m_merge_operations));
    }
    return obj;
}

QString OAIConflictMetadata::getFilePath() const {
    return m_file_path;
}
void OAIConflictMetadata::setFilePath(const QString &file_path) {
    m_file_path = file_path;
    m_file_path_isSet = true;
}

bool OAIConflictMetadata::is_file_path_Set() const{
    return m_file_path_isSet;
}

bool OAIConflictMetadata::is_file_path_Valid() const{
    return m_file_path_isValid;
}

OAIConflictMetadata_fileSizes OAIConflictMetadata::getFileSizes() const {
    return m_file_sizes;
}
void OAIConflictMetadata::setFileSizes(const OAIConflictMetadata_fileSizes &file_sizes) {
    m_file_sizes = file_sizes;
    m_file_sizes_isSet = true;
}

bool OAIConflictMetadata::is_file_sizes_Set() const{
    return m_file_sizes_isSet;
}

bool OAIConflictMetadata::is_file_sizes_Valid() const{
    return m_file_sizes_isValid;
}

OAIConflictMetadata_fileModes OAIConflictMetadata::getFileModes() const {
    return m_file_modes;
}
void OAIConflictMetadata::setFileModes(const OAIConflictMetadata_fileModes &file_modes) {
    m_file_modes = file_modes;
    m_file_modes_isSet = true;
}

bool OAIConflictMetadata::is_file_modes_Set() const{
    return m_file_modes_isSet;
}

bool OAIConflictMetadata::is_file_modes_Valid() const{
    return m_file_modes_isValid;
}

OAIConflictMetadata_objectTypes OAIConflictMetadata::getObjectTypes() const {
    return m_object_types;
}
void OAIConflictMetadata::setObjectTypes(const OAIConflictMetadata_objectTypes &object_types) {
    m_object_types = object_types;
    m_object_types_isSet = true;
}

bool OAIConflictMetadata::is_object_types_Set() const{
    return m_object_types_isSet;
}

bool OAIConflictMetadata::is_object_types_Valid() const{
    return m_object_types_isValid;
}

qint32 OAIConflictMetadata::getNumberOfConflicts() const {
    return m_number_of_conflicts;
}
void OAIConflictMetadata::setNumberOfConflicts(const qint32 &number_of_conflicts) {
    m_number_of_conflicts = number_of_conflicts;
    m_number_of_conflicts_isSet = true;
}

bool OAIConflictMetadata::is_number_of_conflicts_Set() const{
    return m_number_of_conflicts_isSet;
}

bool OAIConflictMetadata::is_number_of_conflicts_Valid() const{
    return m_number_of_conflicts_isValid;
}

OAIConflictMetadata_isBinaryFile OAIConflictMetadata::getIsBinaryFile() const {
    return m_is_binary_file;
}
void OAIConflictMetadata::setIsBinaryFile(const OAIConflictMetadata_isBinaryFile &is_binary_file) {
    m_is_binary_file = is_binary_file;
    m_is_binary_file_isSet = true;
}

bool OAIConflictMetadata::is_is_binary_file_Set() const{
    return m_is_binary_file_isSet;
}

bool OAIConflictMetadata::is_is_binary_file_Valid() const{
    return m_is_binary_file_isValid;
}

bool OAIConflictMetadata::getContentConflict() const {
    return m_content_conflict;
}
void OAIConflictMetadata::setContentConflict(const bool &content_conflict) {
    m_content_conflict = content_conflict;
    m_content_conflict_isSet = true;
}

bool OAIConflictMetadata::is_content_conflict_Set() const{
    return m_content_conflict_isSet;
}

bool OAIConflictMetadata::is_content_conflict_Valid() const{
    return m_content_conflict_isValid;
}

bool OAIConflictMetadata::getFileModeConflict() const {
    return m_file_mode_conflict;
}
void OAIConflictMetadata::setFileModeConflict(const bool &file_mode_conflict) {
    m_file_mode_conflict = file_mode_conflict;
    m_file_mode_conflict_isSet = true;
}

bool OAIConflictMetadata::is_file_mode_conflict_Set() const{
    return m_file_mode_conflict_isSet;
}

bool OAIConflictMetadata::is_file_mode_conflict_Valid() const{
    return m_file_mode_conflict_isValid;
}

bool OAIConflictMetadata::getObjectTypeConflict() const {
    return m_object_type_conflict;
}
void OAIConflictMetadata::setObjectTypeConflict(const bool &object_type_conflict) {
    m_object_type_conflict = object_type_conflict;
    m_object_type_conflict_isSet = true;
}

bool OAIConflictMetadata::is_object_type_conflict_Set() const{
    return m_object_type_conflict_isSet;
}

bool OAIConflictMetadata::is_object_type_conflict_Valid() const{
    return m_object_type_conflict_isValid;
}

OAIConflictMetadata_mergeOperations OAIConflictMetadata::getMergeOperations() const {
    return m_merge_operations;
}
void OAIConflictMetadata::setMergeOperations(const OAIConflictMetadata_mergeOperations &merge_operations) {
    m_merge_operations = merge_operations;
    m_merge_operations_isSet = true;
}

bool OAIConflictMetadata::is_merge_operations_Set() const{
    return m_merge_operations_isSet;
}

bool OAIConflictMetadata::is_merge_operations_Valid() const{
    return m_merge_operations_isValid;
}

bool OAIConflictMetadata::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_file_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_sizes.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_modes.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_object_types.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_of_conflicts_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_binary_file.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_content_conflict_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_mode_conflict_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_object_type_conflict_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_merge_operations.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConflictMetadata::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
