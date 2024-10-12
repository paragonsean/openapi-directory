/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests() {
    this->initializeModel();
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests() {}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::initializeModel() {

    m_count_isSet = false;
    m_count_isValid = false;

    m_time_interval_isSet = false;
    m_time_interval_isValid = false;
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::fromJsonObject(QJsonObject json) {

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("count")]);
    m_count_isSet = !json[QString("count")].isNull() && m_count_isValid;

    m_time_interval_isValid = ::OpenAPI::fromJsonValue(m_time_interval, json[QString("timeInterval")]);
    m_time_interval_isSet = !json[QString("timeInterval")].isNull() && m_time_interval_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::asJsonObject() const {
    QJsonObject obj;
    if (m_count_isSet) {
        obj.insert(QString("count"), ::OpenAPI::toJsonValue(m_count));
    }
    if (m_time_interval_isSet) {
        obj.insert(QString("timeInterval"), ::OpenAPI::toJsonValue(m_time_interval));
    }
    return obj;
}

qint32 OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::getCount() const {
    return m_count;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::setCount(const qint32 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::is_count_Set() const{
    return m_count_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::is_count_Valid() const{
    return m_count_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::getTimeInterval() const {
    return m_time_interval;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::setTimeInterval(const QString &time_interval) {
    m_time_interval = time_interval;
    m_time_interval_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::is_time_interval_Set() const{
    return m_time_interval_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::is_time_interval_Valid() const{
    return m_time_interval_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_interval_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers_requests::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
