/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors() {
    this->initializeModel();
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors::~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors() {}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors::initializeModel() {

    m_allowed_origins_isSet = false;
    m_allowed_origins_isValid = false;
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors::fromJsonObject(QJsonObject json) {

    m_allowed_origins_isValid = ::OpenAPI::fromJsonValue(m_allowed_origins, json[QString("allowedOrigins")]);
    m_allowed_origins_isSet = !json[QString("allowedOrigins")].isNull() && m_allowed_origins_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors::asJsonObject() const {
    QJsonObject obj;
    if (m_allowed_origins.size() > 0) {
        obj.insert(QString("allowedOrigins"), ::OpenAPI::toJsonValue(m_allowed_origins));
    }
    return obj;
}

QList<QString> OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors::getAllowedOrigins() const {
    return m_allowed_origins;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors::setAllowedOrigins(const QList<QString> &allowed_origins) {
    m_allowed_origins = allowed_origins;
    m_allowed_origins_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors::is_allowed_origins_Set() const{
    return m_allowed_origins_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors::is_allowed_origins_Valid() const{
    return m_allowed_origins_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_allowed_origins.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_cors::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
