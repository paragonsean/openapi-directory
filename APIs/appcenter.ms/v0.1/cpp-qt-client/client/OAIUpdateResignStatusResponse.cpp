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

#include "OAIUpdateResignStatusResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateResignStatusResponse::OAIUpdateResignStatusResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateResignStatusResponse::OAIUpdateResignStatusResponse() {
    this->initializeModel();
}

OAIUpdateResignStatusResponse::~OAIUpdateResignStatusResponse() {}

void OAIUpdateResignStatusResponse::initializeModel() {

    m_profiles_zip_base64_isSet = false;
    m_profiles_zip_base64_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIUpdateResignStatusResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateResignStatusResponse::fromJsonObject(QJsonObject json) {

    m_profiles_zip_base64_isValid = ::OpenAPI::fromJsonValue(m_profiles_zip_base64, json[QString("profiles_zip_base64")]);
    m_profiles_zip_base64_isSet = !json[QString("profiles_zip_base64")].isNull() && m_profiles_zip_base64_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIUpdateResignStatusResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateResignStatusResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_profiles_zip_base64_isSet) {
        obj.insert(QString("profiles_zip_base64"), ::OpenAPI::toJsonValue(m_profiles_zip_base64));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAIUpdateResignStatusResponse::getProfilesZipBase64() const {
    return m_profiles_zip_base64;
}
void OAIUpdateResignStatusResponse::setProfilesZipBase64(const QString &profiles_zip_base64) {
    m_profiles_zip_base64 = profiles_zip_base64;
    m_profiles_zip_base64_isSet = true;
}

bool OAIUpdateResignStatusResponse::is_profiles_zip_base64_Set() const{
    return m_profiles_zip_base64_isSet;
}

bool OAIUpdateResignStatusResponse::is_profiles_zip_base64_Valid() const{
    return m_profiles_zip_base64_isValid;
}

QString OAIUpdateResignStatusResponse::getStatus() const {
    return m_status;
}
void OAIUpdateResignStatusResponse::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIUpdateResignStatusResponse::is_status_Set() const{
    return m_status_isSet;
}

bool OAIUpdateResignStatusResponse::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIUpdateResignStatusResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_profiles_zip_base64_isSet) {
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

bool OAIUpdateResignStatusResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_status_isValid && true;
}

} // namespace OpenAPI
