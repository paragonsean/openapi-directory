/**
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAPI_Status_App_Version.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAPI_Status_App_Version::OAIAPI_Status_App_Version(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAPI_Status_App_Version::OAIAPI_Status_App_Version() {
    this->initializeModel();
}

OAIAPI_Status_App_Version::~OAIAPI_Status_App_Version() {}

void OAIAPI_Status_App_Version::initializeModel() {

    m_latest_app_version_isSet = false;
    m_latest_app_version_isValid = false;

    m_min_app_version_isSet = false;
    m_min_app_version_isValid = false;
}

void OAIAPI_Status_App_Version::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAPI_Status_App_Version::fromJsonObject(QJsonObject json) {

    m_latest_app_version_isValid = ::OpenAPI::fromJsonValue(m_latest_app_version, json[QString("latest_app_version")]);
    m_latest_app_version_isSet = !json[QString("latest_app_version")].isNull() && m_latest_app_version_isValid;

    m_min_app_version_isValid = ::OpenAPI::fromJsonValue(m_min_app_version, json[QString("min_app_version")]);
    m_min_app_version_isSet = !json[QString("min_app_version")].isNull() && m_min_app_version_isValid;
}

QString OAIAPI_Status_App_Version::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAPI_Status_App_Version::asJsonObject() const {
    QJsonObject obj;
    if (m_latest_app_version_isSet) {
        obj.insert(QString("latest_app_version"), ::OpenAPI::toJsonValue(m_latest_app_version));
    }
    if (m_min_app_version_isSet) {
        obj.insert(QString("min_app_version"), ::OpenAPI::toJsonValue(m_min_app_version));
    }
    return obj;
}

qint32 OAIAPI_Status_App_Version::getLatestAppVersion() const {
    return m_latest_app_version;
}
void OAIAPI_Status_App_Version::setLatestAppVersion(const qint32 &latest_app_version) {
    m_latest_app_version = latest_app_version;
    m_latest_app_version_isSet = true;
}

bool OAIAPI_Status_App_Version::is_latest_app_version_Set() const{
    return m_latest_app_version_isSet;
}

bool OAIAPI_Status_App_Version::is_latest_app_version_Valid() const{
    return m_latest_app_version_isValid;
}

qint32 OAIAPI_Status_App_Version::getMinAppVersion() const {
    return m_min_app_version;
}
void OAIAPI_Status_App_Version::setMinAppVersion(const qint32 &min_app_version) {
    m_min_app_version = min_app_version;
    m_min_app_version_isSet = true;
}

bool OAIAPI_Status_App_Version::is_min_app_version_Set() const{
    return m_min_app_version_isSet;
}

bool OAIAPI_Status_App_Version::is_min_app_version_Valid() const{
    return m_min_app_version_isValid;
}

bool OAIAPI_Status_App_Version::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_latest_app_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_min_app_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAPI_Status_App_Version::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_latest_app_version_isValid && m_min_app_version_isValid && true;
}

} // namespace OpenAPI
