/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDistributionGroupAadGroupsDeleteResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDistributionGroupAadGroupsDeleteResponse::OAIDistributionGroupAadGroupsDeleteResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDistributionGroupAadGroupsDeleteResponse::OAIDistributionGroupAadGroupsDeleteResponse() {
    this->initializeModel();
}

OAIDistributionGroupAadGroupsDeleteResponse::~OAIDistributionGroupAadGroupsDeleteResponse() {}

void OAIDistributionGroupAadGroupsDeleteResponse::initializeModel() {

    m_aad_group_id_isSet = false;
    m_aad_group_id_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIDistributionGroupAadGroupsDeleteResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDistributionGroupAadGroupsDeleteResponse::fromJsonObject(QJsonObject json) {

    m_aad_group_id_isValid = ::OpenAPI::fromJsonValue(m_aad_group_id, json[QString("aad_group_id")]);
    m_aad_group_id_isSet = !json[QString("aad_group_id")].isNull() && m_aad_group_id_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIDistributionGroupAadGroupsDeleteResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDistributionGroupAadGroupsDeleteResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_aad_group_id_isSet) {
        obj.insert(QString("aad_group_id"), ::OpenAPI::toJsonValue(m_aad_group_id));
    }
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAIDistributionGroupAadGroupsDeleteResponse::getAadGroupId() const {
    return m_aad_group_id;
}
void OAIDistributionGroupAadGroupsDeleteResponse::setAadGroupId(const QString &aad_group_id) {
    m_aad_group_id = aad_group_id;
    m_aad_group_id_isSet = true;
}

bool OAIDistributionGroupAadGroupsDeleteResponse::is_aad_group_id_Set() const{
    return m_aad_group_id_isSet;
}

bool OAIDistributionGroupAadGroupsDeleteResponse::is_aad_group_id_Valid() const{
    return m_aad_group_id_isValid;
}

QString OAIDistributionGroupAadGroupsDeleteResponse::getCode() const {
    return m_code;
}
void OAIDistributionGroupAadGroupsDeleteResponse::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIDistributionGroupAadGroupsDeleteResponse::is_code_Set() const{
    return m_code_isSet;
}

bool OAIDistributionGroupAadGroupsDeleteResponse::is_code_Valid() const{
    return m_code_isValid;
}

qint32 OAIDistributionGroupAadGroupsDeleteResponse::getMessage() const {
    return m_message;
}
void OAIDistributionGroupAadGroupsDeleteResponse::setMessage(const qint32 &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIDistributionGroupAadGroupsDeleteResponse::is_message_Set() const{
    return m_message_isSet;
}

bool OAIDistributionGroupAadGroupsDeleteResponse::is_message_Valid() const{
    return m_message_isValid;
}

qint32 OAIDistributionGroupAadGroupsDeleteResponse::getStatus() const {
    return m_status;
}
void OAIDistributionGroupAadGroupsDeleteResponse::setStatus(const qint32 &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIDistributionGroupAadGroupsDeleteResponse::is_status_Set() const{
    return m_status_isSet;
}

bool OAIDistributionGroupAadGroupsDeleteResponse::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIDistributionGroupAadGroupsDeleteResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_aad_group_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDistributionGroupAadGroupsDeleteResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_status_isValid && true;
}

} // namespace OpenAPI
