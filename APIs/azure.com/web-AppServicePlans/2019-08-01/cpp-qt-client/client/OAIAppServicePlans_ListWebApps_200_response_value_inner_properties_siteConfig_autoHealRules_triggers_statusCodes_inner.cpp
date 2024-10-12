/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner() {
    this->initializeModel();
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner() {}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::initializeModel() {

    m_count_isSet = false;
    m_count_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_sub_status_isSet = false;
    m_sub_status_isValid = false;

    m_time_interval_isSet = false;
    m_time_interval_isValid = false;

    m_win32_status_isSet = false;
    m_win32_status_isValid = false;
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::fromJsonObject(QJsonObject json) {

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("count")]);
    m_count_isSet = !json[QString("count")].isNull() && m_count_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_sub_status_isValid = ::OpenAPI::fromJsonValue(m_sub_status, json[QString("subStatus")]);
    m_sub_status_isSet = !json[QString("subStatus")].isNull() && m_sub_status_isValid;

    m_time_interval_isValid = ::OpenAPI::fromJsonValue(m_time_interval, json[QString("timeInterval")]);
    m_time_interval_isSet = !json[QString("timeInterval")].isNull() && m_time_interval_isValid;

    m_win32_status_isValid = ::OpenAPI::fromJsonValue(m_win32_status, json[QString("win32Status")]);
    m_win32_status_isSet = !json[QString("win32Status")].isNull() && m_win32_status_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_count_isSet) {
        obj.insert(QString("count"), ::OpenAPI::toJsonValue(m_count));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_sub_status_isSet) {
        obj.insert(QString("subStatus"), ::OpenAPI::toJsonValue(m_sub_status));
    }
    if (m_time_interval_isSet) {
        obj.insert(QString("timeInterval"), ::OpenAPI::toJsonValue(m_time_interval));
    }
    if (m_win32_status_isSet) {
        obj.insert(QString("win32Status"), ::OpenAPI::toJsonValue(m_win32_status));
    }
    return obj;
}

qint32 OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::getCount() const {
    return m_count;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::setCount(const qint32 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::is_count_Set() const{
    return m_count_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::is_count_Valid() const{
    return m_count_isValid;
}

qint32 OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::getStatus() const {
    return m_status;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::setStatus(const qint32 &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::is_status_Set() const{
    return m_status_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::is_status_Valid() const{
    return m_status_isValid;
}

qint32 OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::getSubStatus() const {
    return m_sub_status;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::setSubStatus(const qint32 &sub_status) {
    m_sub_status = sub_status;
    m_sub_status_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::is_sub_status_Set() const{
    return m_sub_status_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::is_sub_status_Valid() const{
    return m_sub_status_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::getTimeInterval() const {
    return m_time_interval;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::setTimeInterval(const QString &time_interval) {
    m_time_interval = time_interval;
    m_time_interval_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::is_time_interval_Set() const{
    return m_time_interval_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::is_time_interval_Valid() const{
    return m_time_interval_isValid;
}

qint32 OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::getWin32Status() const {
    return m_win32_status;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::setWin32Status(const qint32 &win32_status) {
    m_win32_status = win32_status;
    m_win32_status_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::is_win32_status_Set() const{
    return m_win32_status_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::is_win32_status_Valid() const{
    return m_win32_status_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sub_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_interval_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_win32_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_statusCodes_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
