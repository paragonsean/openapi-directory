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

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner() {
    this->initializeModel();
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner() {}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::getName() const {
    return m_name;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::getValue() const {
    return m_value;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_appSettings_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
