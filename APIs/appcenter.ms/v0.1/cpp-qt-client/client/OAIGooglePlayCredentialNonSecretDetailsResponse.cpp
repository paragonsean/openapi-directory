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

#include "OAIGooglePlayCredentialNonSecretDetailsResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGooglePlayCredentialNonSecretDetailsResponse::OAIGooglePlayCredentialNonSecretDetailsResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGooglePlayCredentialNonSecretDetailsResponse::OAIGooglePlayCredentialNonSecretDetailsResponse() {
    this->initializeModel();
}

OAIGooglePlayCredentialNonSecretDetailsResponse::~OAIGooglePlayCredentialNonSecretDetailsResponse() {}

void OAIGooglePlayCredentialNonSecretDetailsResponse::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;

    m_credential_type_isSet = false;
    m_credential_type_isValid = false;

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_service_type_isSet = false;
    m_service_type_isValid = false;
}

void OAIGooglePlayCredentialNonSecretDetailsResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGooglePlayCredentialNonSecretDetailsResponse::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;

    m_credential_type_isValid = ::OpenAPI::fromJsonValue(m_credential_type, json[QString("credentialType")]);
    m_credential_type_isSet = !json[QString("credentialType")].isNull() && m_credential_type_isValid;

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("displayName")]);
    m_display_name_isSet = !json[QString("displayName")].isNull() && m_display_name_isValid;

    m_service_type_isValid = ::OpenAPI::fromJsonValue(m_service_type, json[QString("serviceType")]);
    m_service_type_isSet = !json[QString("serviceType")].isNull() && m_service_type_isValid;
}

QString OAIGooglePlayCredentialNonSecretDetailsResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGooglePlayCredentialNonSecretDetailsResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_data_isSet) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    if (m_credential_type_isSet) {
        obj.insert(QString("credentialType"), ::OpenAPI::toJsonValue(m_credential_type));
    }
    if (m_display_name_isSet) {
        obj.insert(QString("displayName"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_service_type_isSet) {
        obj.insert(QString("serviceType"), ::OpenAPI::toJsonValue(m_service_type));
    }
    return obj;
}

OAIObject OAIGooglePlayCredentialNonSecretDetailsResponse::getData() const {
    return m_data;
}
void OAIGooglePlayCredentialNonSecretDetailsResponse::setData(const OAIObject &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAIGooglePlayCredentialNonSecretDetailsResponse::is_data_Set() const{
    return m_data_isSet;
}

bool OAIGooglePlayCredentialNonSecretDetailsResponse::is_data_Valid() const{
    return m_data_isValid;
}

QString OAIGooglePlayCredentialNonSecretDetailsResponse::getCredentialType() const {
    return m_credential_type;
}
void OAIGooglePlayCredentialNonSecretDetailsResponse::setCredentialType(const QString &credential_type) {
    m_credential_type = credential_type;
    m_credential_type_isSet = true;
}

bool OAIGooglePlayCredentialNonSecretDetailsResponse::is_credential_type_Set() const{
    return m_credential_type_isSet;
}

bool OAIGooglePlayCredentialNonSecretDetailsResponse::is_credential_type_Valid() const{
    return m_credential_type_isValid;
}

QString OAIGooglePlayCredentialNonSecretDetailsResponse::getDisplayName() const {
    return m_display_name;
}
void OAIGooglePlayCredentialNonSecretDetailsResponse::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIGooglePlayCredentialNonSecretDetailsResponse::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIGooglePlayCredentialNonSecretDetailsResponse::is_display_name_Valid() const{
    return m_display_name_isValid;
}

QString OAIGooglePlayCredentialNonSecretDetailsResponse::getServiceType() const {
    return m_service_type;
}
void OAIGooglePlayCredentialNonSecretDetailsResponse::setServiceType(const QString &service_type) {
    m_service_type = service_type;
    m_service_type_isSet = true;
}

bool OAIGooglePlayCredentialNonSecretDetailsResponse::is_service_type_Set() const{
    return m_service_type_isSet;
}

bool OAIGooglePlayCredentialNonSecretDetailsResponse::is_service_type_Valid() const{
    return m_service_type_isValid;
}

bool OAIGooglePlayCredentialNonSecretDetailsResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_credential_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_name_isSet) {
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

bool OAIGooglePlayCredentialNonSecretDetailsResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_data_isValid && m_display_name_isValid && m_service_type_isValid && true;
}

} // namespace OpenAPI
