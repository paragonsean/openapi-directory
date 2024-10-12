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

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner() {
    this->initializeModel();
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner() {}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::initializeModel() {

    m_connection_string_isSet = false;
    m_connection_string_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::fromJsonObject(QJsonObject json) {

    m_connection_string_isValid = ::OpenAPI::fromJsonValue(m_connection_string, json[QString("connectionString")]);
    m_connection_string_isSet = !json[QString("connectionString")].isNull() && m_connection_string_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_connection_string_isSet) {
        obj.insert(QString("connectionString"), ::OpenAPI::toJsonValue(m_connection_string));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::getConnectionString() const {
    return m_connection_string;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::setConnectionString(const QString &connection_string) {
    m_connection_string = connection_string;
    m_connection_string_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::is_connection_string_Set() const{
    return m_connection_string_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::is_connection_string_Valid() const{
    return m_connection_string_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::getName() const {
    return m_name;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::getType() const {
    return m_type;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_connection_string_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_connectionStrings_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
