/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord() {
    this->initializeModel();
}

OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::~OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord() {}

void OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::initializeModel() {

    m_client_count_isSet = false;
    m_client_count_isValid = false;

    m_error_code_isSet = false;
    m_error_code_isValid = false;

    m_long_description_isSet = false;
    m_long_description_isValid = false;

    m_short_description_isSet = false;
    m_short_description_isValid = false;
}

void OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::fromJsonObject(QJsonObject json) {

    m_client_count_isValid = ::OpenAPI::fromJsonValue(m_client_count, json[QString("ClientCount")]);
    m_client_count_isSet = !json[QString("ClientCount")].isNull() && m_client_count_isValid;

    m_error_code_isValid = ::OpenAPI::fromJsonValue(m_error_code, json[QString("ErrorCode")]);
    m_error_code_isSet = !json[QString("ErrorCode")].isNull() && m_error_code_isValid;

    m_long_description_isValid = ::OpenAPI::fromJsonValue(m_long_description, json[QString("LongDescription")]);
    m_long_description_isSet = !json[QString("LongDescription")].isNull() && m_long_description_isValid;

    m_short_description_isValid = ::OpenAPI::fromJsonValue(m_short_description, json[QString("ShortDescription")]);
    m_short_description_isSet = !json[QString("ShortDescription")].isNull() && m_short_description_isValid;
}

QString OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::asJsonObject() const {
    QJsonObject obj;
    if (m_client_count_isSet) {
        obj.insert(QString("ClientCount"), ::OpenAPI::toJsonValue(m_client_count));
    }
    if (m_error_code_isSet) {
        obj.insert(QString("ErrorCode"), ::OpenAPI::toJsonValue(m_error_code));
    }
    if (m_long_description_isSet) {
        obj.insert(QString("LongDescription"), ::OpenAPI::toJsonValue(m_long_description));
    }
    if (m_short_description_isSet) {
        obj.insert(QString("ShortDescription"), ::OpenAPI::toJsonValue(m_short_description));
    }
    return obj;
}

qint32 OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::getClientCount() const {
    return m_client_count;
}
void OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::setClientCount(const qint32 &client_count) {
    m_client_count = client_count;
    m_client_count_isSet = true;
}

bool OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::is_client_count_Set() const{
    return m_client_count_isSet;
}

bool OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::is_client_count_Valid() const{
    return m_client_count_isValid;
}

QString OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::getErrorCode() const {
    return m_error_code;
}
void OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::setErrorCode(const QString &error_code) {
    m_error_code = error_code;
    m_error_code_isSet = true;
}

bool OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::is_error_code_Set() const{
    return m_error_code_isSet;
}

bool OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::is_error_code_Valid() const{
    return m_error_code_isValid;
}

QString OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::getLongDescription() const {
    return m_long_description;
}
void OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::setLongDescription(const QString &long_description) {
    m_long_description = long_description;
    m_long_description_isSet = true;
}

bool OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::is_long_description_Set() const{
    return m_long_description_isSet;
}

bool OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::is_long_description_Valid() const{
    return m_long_description_isValid;
}

QString OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::getShortDescription() const {
    return m_short_description;
}
void OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::setShortDescription(const QString &short_description) {
    m_short_description = short_description;
    m_short_description_isSet = true;
}

bool OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::is_short_description_Set() const{
    return m_short_description_isSet;
}

bool OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::is_short_description_Valid() const{
    return m_short_description_isValid;
}

bool OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_long_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_short_description_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateSystem_Models_UpdateMetricsData_PackageErrorsRecord::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
