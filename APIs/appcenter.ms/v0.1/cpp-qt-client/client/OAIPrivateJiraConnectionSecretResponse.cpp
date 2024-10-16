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

#include "OAIPrivateJiraConnectionSecretResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPrivateJiraConnectionSecretResponse::OAIPrivateJiraConnectionSecretResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPrivateJiraConnectionSecretResponse::OAIPrivateJiraConnectionSecretResponse() {
    this->initializeModel();
}

OAIPrivateJiraConnectionSecretResponse::~OAIPrivateJiraConnectionSecretResponse() {}

void OAIPrivateJiraConnectionSecretResponse::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is2_fa_isSet = false;
    m_is2_fa_isValid = false;

    m_is_valid_isSet = false;
    m_is_valid_isValid = false;

    m_service_type_isSet = false;
    m_service_type_isValid = false;
}

void OAIPrivateJiraConnectionSecretResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPrivateJiraConnectionSecretResponse::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("displayName")]);
    m_display_name_isSet = !json[QString("displayName")].isNull() && m_display_name_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is2_fa_isValid = ::OpenAPI::fromJsonValue(m_is2_fa, json[QString("is2FA")]);
    m_is2_fa_isSet = !json[QString("is2FA")].isNull() && m_is2_fa_isValid;

    m_is_valid_isValid = ::OpenAPI::fromJsonValue(m_is_valid, json[QString("isValid")]);
    m_is_valid_isSet = !json[QString("isValid")].isNull() && m_is_valid_isValid;

    m_service_type_isValid = ::OpenAPI::fromJsonValue(m_service_type, json[QString("serviceType")]);
    m_service_type_isSet = !json[QString("serviceType")].isNull() && m_service_type_isValid;
}

QString OAIPrivateJiraConnectionSecretResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPrivateJiraConnectionSecretResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_data.isSet()) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    if (m_display_name_isSet) {
        obj.insert(QString("displayName"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is2_fa_isSet) {
        obj.insert(QString("is2FA"), ::OpenAPI::toJsonValue(m_is2_fa));
    }
    if (m_is_valid_isSet) {
        obj.insert(QString("isValid"), ::OpenAPI::toJsonValue(m_is_valid));
    }
    if (m_service_type_isSet) {
        obj.insert(QString("serviceType"), ::OpenAPI::toJsonValue(m_service_type));
    }
    return obj;
}

OAIObject OAIPrivateJiraConnectionSecretResponse::getData() const {
    return m_data;
}
void OAIPrivateJiraConnectionSecretResponse::setData(const OAIObject &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAIPrivateJiraConnectionSecretResponse::is_data_Set() const{
    return m_data_isSet;
}

bool OAIPrivateJiraConnectionSecretResponse::is_data_Valid() const{
    return m_data_isValid;
}

QString OAIPrivateJiraConnectionSecretResponse::getDisplayName() const {
    return m_display_name;
}
void OAIPrivateJiraConnectionSecretResponse::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIPrivateJiraConnectionSecretResponse::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIPrivateJiraConnectionSecretResponse::is_display_name_Valid() const{
    return m_display_name_isValid;
}

QString OAIPrivateJiraConnectionSecretResponse::getId() const {
    return m_id;
}
void OAIPrivateJiraConnectionSecretResponse::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPrivateJiraConnectionSecretResponse::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPrivateJiraConnectionSecretResponse::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIPrivateJiraConnectionSecretResponse::isIs2Fa() const {
    return m_is2_fa;
}
void OAIPrivateJiraConnectionSecretResponse::setIs2Fa(const bool &is2_fa) {
    m_is2_fa = is2_fa;
    m_is2_fa_isSet = true;
}

bool OAIPrivateJiraConnectionSecretResponse::is_is2_fa_Set() const{
    return m_is2_fa_isSet;
}

bool OAIPrivateJiraConnectionSecretResponse::is_is2_fa_Valid() const{
    return m_is2_fa_isValid;
}

bool OAIPrivateJiraConnectionSecretResponse::isIsValid() const {
    return m_is_valid;
}
void OAIPrivateJiraConnectionSecretResponse::setIsValid(const bool &is_valid) {
    m_is_valid = is_valid;
    m_is_valid_isSet = true;
}

bool OAIPrivateJiraConnectionSecretResponse::is_is_valid_Set() const{
    return m_is_valid_isSet;
}

bool OAIPrivateJiraConnectionSecretResponse::is_is_valid_Valid() const{
    return m_is_valid_isValid;
}

QString OAIPrivateJiraConnectionSecretResponse::getServiceType() const {
    return m_service_type;
}
void OAIPrivateJiraConnectionSecretResponse::setServiceType(const QString &service_type) {
    m_service_type = service_type;
    m_service_type_isSet = true;
}

bool OAIPrivateJiraConnectionSecretResponse::is_service_type_Set() const{
    return m_service_type_isSet;
}

bool OAIPrivateJiraConnectionSecretResponse::is_service_type_Valid() const{
    return m_service_type_isValid;
}

bool OAIPrivateJiraConnectionSecretResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is2_fa_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_valid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPrivateJiraConnectionSecretResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_data_isValid && m_id_isValid && m_service_type_isValid && true;
}

} // namespace OpenAPI
