/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAlertFilter.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAlertFilter::OAIAlertFilter(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAlertFilter::OAIAlertFilter() {
    this->initializeModel();
}

OAIAlertFilter::~OAIAlertFilter() {}

void OAIAlertFilter::initializeModel() {

    m_appeared_on_time_isSet = false;
    m_appeared_on_time_isValid = false;

    m_severity_isSet = false;
    m_severity_isValid = false;

    m_source_name_isSet = false;
    m_source_name_isValid = false;

    m_source_type_isSet = false;
    m_source_type_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIAlertFilter::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAlertFilter::fromJsonObject(QJsonObject json) {

    m_appeared_on_time_isValid = ::OpenAPI::fromJsonValue(m_appeared_on_time, json[QString("appearedOnTime")]);
    m_appeared_on_time_isSet = !json[QString("appearedOnTime")].isNull() && m_appeared_on_time_isValid;

    m_severity_isValid = ::OpenAPI::fromJsonValue(m_severity, json[QString("severity")]);
    m_severity_isSet = !json[QString("severity")].isNull() && m_severity_isValid;

    m_source_name_isValid = ::OpenAPI::fromJsonValue(m_source_name, json[QString("sourceName")]);
    m_source_name_isSet = !json[QString("sourceName")].isNull() && m_source_name_isValid;

    m_source_type_isValid = ::OpenAPI::fromJsonValue(m_source_type, json[QString("sourceType")]);
    m_source_type_isSet = !json[QString("sourceType")].isNull() && m_source_type_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIAlertFilter::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAlertFilter::asJsonObject() const {
    QJsonObject obj;
    if (m_appeared_on_time_isSet) {
        obj.insert(QString("appearedOnTime"), ::OpenAPI::toJsonValue(m_appeared_on_time));
    }
    if (m_severity_isSet) {
        obj.insert(QString("severity"), ::OpenAPI::toJsonValue(m_severity));
    }
    if (m_source_name_isSet) {
        obj.insert(QString("sourceName"), ::OpenAPI::toJsonValue(m_source_name));
    }
    if (m_source_type_isSet) {
        obj.insert(QString("sourceType"), ::OpenAPI::toJsonValue(m_source_type));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QDateTime OAIAlertFilter::getAppearedOnTime() const {
    return m_appeared_on_time;
}
void OAIAlertFilter::setAppearedOnTime(const QDateTime &appeared_on_time) {
    m_appeared_on_time = appeared_on_time;
    m_appeared_on_time_isSet = true;
}

bool OAIAlertFilter::is_appeared_on_time_Set() const{
    return m_appeared_on_time_isSet;
}

bool OAIAlertFilter::is_appeared_on_time_Valid() const{
    return m_appeared_on_time_isValid;
}

QString OAIAlertFilter::getSeverity() const {
    return m_severity;
}
void OAIAlertFilter::setSeverity(const QString &severity) {
    m_severity = severity;
    m_severity_isSet = true;
}

bool OAIAlertFilter::is_severity_Set() const{
    return m_severity_isSet;
}

bool OAIAlertFilter::is_severity_Valid() const{
    return m_severity_isValid;
}

QString OAIAlertFilter::getSourceName() const {
    return m_source_name;
}
void OAIAlertFilter::setSourceName(const QString &source_name) {
    m_source_name = source_name;
    m_source_name_isSet = true;
}

bool OAIAlertFilter::is_source_name_Set() const{
    return m_source_name_isSet;
}

bool OAIAlertFilter::is_source_name_Valid() const{
    return m_source_name_isValid;
}

QString OAIAlertFilter::getSourceType() const {
    return m_source_type;
}
void OAIAlertFilter::setSourceType(const QString &source_type) {
    m_source_type = source_type;
    m_source_type_isSet = true;
}

bool OAIAlertFilter::is_source_type_Set() const{
    return m_source_type_isSet;
}

bool OAIAlertFilter::is_source_type_Valid() const{
    return m_source_type_isValid;
}

QString OAIAlertFilter::getStatus() const {
    return m_status;
}
void OAIAlertFilter::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIAlertFilter::is_status_Set() const{
    return m_status_isSet;
}

bool OAIAlertFilter::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIAlertFilter::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_appeared_on_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_severity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_type_isSet) {
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

bool OAIAlertFilter::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
