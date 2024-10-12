/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAdminReport.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAdminReport::OAIAdminReport(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAdminReport::OAIAdminReport() {
    this->initializeModel();
}

OAIAdminReport::~OAIAdminReport() {}

void OAIAdminReport::initializeModel() {

    m_account_isSet = false;
    m_account_isValid = false;

    m_action_taken_isSet = false;
    m_action_taken_isValid = false;

    m_assigned_account_isSet = false;
    m_assigned_account_isValid = false;

    m_comment_isSet = false;
    m_comment_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_statuses_isSet = false;
    m_statuses_isValid = false;

    m_target_account_isSet = false;
    m_target_account_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;
}

void OAIAdminReport::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAdminReport::fromJsonObject(QJsonObject json) {

    m_account_isValid = ::OpenAPI::fromJsonValue(m_account, json[QString("account")]);
    m_account_isSet = !json[QString("account")].isNull() && m_account_isValid;

    m_action_taken_isValid = ::OpenAPI::fromJsonValue(m_action_taken, json[QString("action_taken")]);
    m_action_taken_isSet = !json[QString("action_taken")].isNull() && m_action_taken_isValid;

    m_assigned_account_isValid = ::OpenAPI::fromJsonValue(m_assigned_account, json[QString("assigned_account")]);
    m_assigned_account_isSet = !json[QString("assigned_account")].isNull() && m_assigned_account_isValid;

    m_comment_isValid = ::OpenAPI::fromJsonValue(m_comment, json[QString("comment")]);
    m_comment_isSet = !json[QString("comment")].isNull() && m_comment_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_statuses_isValid = ::OpenAPI::fromJsonValue(m_statuses, json[QString("statuses")]);
    m_statuses_isSet = !json[QString("statuses")].isNull() && m_statuses_isValid;

    m_target_account_isValid = ::OpenAPI::fromJsonValue(m_target_account, json[QString("target_account")]);
    m_target_account_isSet = !json[QString("target_account")].isNull() && m_target_account_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;
}

QString OAIAdminReport::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAdminReport::asJsonObject() const {
    QJsonObject obj;
    if (m_account.isSet()) {
        obj.insert(QString("account"), ::OpenAPI::toJsonValue(m_account));
    }
    if (m_action_taken_isSet) {
        obj.insert(QString("action_taken"), ::OpenAPI::toJsonValue(m_action_taken));
    }
    if (m_assigned_account.isSet()) {
        obj.insert(QString("assigned_account"), ::OpenAPI::toJsonValue(m_assigned_account));
    }
    if (m_comment_isSet) {
        obj.insert(QString("comment"), ::OpenAPI::toJsonValue(m_comment));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_statuses.size() > 0) {
        obj.insert(QString("statuses"), ::OpenAPI::toJsonValue(m_statuses));
    }
    if (m_target_account.isSet()) {
        obj.insert(QString("target_account"), ::OpenAPI::toJsonValue(m_target_account));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    return obj;
}

OAIAccount OAIAdminReport::getAccount() const {
    return m_account;
}
void OAIAdminReport::setAccount(const OAIAccount &account) {
    m_account = account;
    m_account_isSet = true;
}

bool OAIAdminReport::is_account_Set() const{
    return m_account_isSet;
}

bool OAIAdminReport::is_account_Valid() const{
    return m_account_isValid;
}

QString OAIAdminReport::getActionTaken() const {
    return m_action_taken;
}
void OAIAdminReport::setActionTaken(const QString &action_taken) {
    m_action_taken = action_taken;
    m_action_taken_isSet = true;
}

bool OAIAdminReport::is_action_taken_Set() const{
    return m_action_taken_isSet;
}

bool OAIAdminReport::is_action_taken_Valid() const{
    return m_action_taken_isValid;
}

OAIAccount OAIAdminReport::getAssignedAccount() const {
    return m_assigned_account;
}
void OAIAdminReport::setAssignedAccount(const OAIAccount &assigned_account) {
    m_assigned_account = assigned_account;
    m_assigned_account_isSet = true;
}

bool OAIAdminReport::is_assigned_account_Set() const{
    return m_assigned_account_isSet;
}

bool OAIAdminReport::is_assigned_account_Valid() const{
    return m_assigned_account_isValid;
}

QString OAIAdminReport::getComment() const {
    return m_comment;
}
void OAIAdminReport::setComment(const QString &comment) {
    m_comment = comment;
    m_comment_isSet = true;
}

bool OAIAdminReport::is_comment_Set() const{
    return m_comment_isSet;
}

bool OAIAdminReport::is_comment_Valid() const{
    return m_comment_isValid;
}

QDateTime OAIAdminReport::getCreatedAt() const {
    return m_created_at;
}
void OAIAdminReport::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIAdminReport::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIAdminReport::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIAdminReport::getId() const {
    return m_id;
}
void OAIAdminReport::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAdminReport::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAdminReport::is_id_Valid() const{
    return m_id_isValid;
}

QList<OAIStatus> OAIAdminReport::getStatuses() const {
    return m_statuses;
}
void OAIAdminReport::setStatuses(const QList<OAIStatus> &statuses) {
    m_statuses = statuses;
    m_statuses_isSet = true;
}

bool OAIAdminReport::is_statuses_Set() const{
    return m_statuses_isSet;
}

bool OAIAdminReport::is_statuses_Valid() const{
    return m_statuses_isValid;
}

OAIAccount OAIAdminReport::getTargetAccount() const {
    return m_target_account;
}
void OAIAdminReport::setTargetAccount(const OAIAccount &target_account) {
    m_target_account = target_account;
    m_target_account_isSet = true;
}

bool OAIAdminReport::is_target_account_Set() const{
    return m_target_account_isSet;
}

bool OAIAdminReport::is_target_account_Valid() const{
    return m_target_account_isValid;
}

QDateTime OAIAdminReport::getUpdatedAt() const {
    return m_updated_at;
}
void OAIAdminReport::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIAdminReport::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIAdminReport::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

bool OAIAdminReport::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_action_taken_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_assigned_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_comment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_statuses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAdminReport::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
