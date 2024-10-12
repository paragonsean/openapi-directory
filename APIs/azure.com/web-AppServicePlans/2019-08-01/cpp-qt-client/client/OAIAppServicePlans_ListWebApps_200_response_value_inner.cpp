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

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListWebApps_200_response_value_inner::OAIAppServicePlans_ListWebApps_200_response_value_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListWebApps_200_response_value_inner::OAIAppServicePlans_ListWebApps_200_response_value_inner() {
    this->initializeModel();
}

OAIAppServicePlans_ListWebApps_200_response_value_inner::~OAIAppServicePlans_ListWebApps_200_response_value_inner() {}

void OAIAppServicePlans_ListWebApps_200_response_value_inner::initializeModel() {

    m_identity_isSet = false;
    m_identity_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner::fromJsonObject(QJsonObject json) {

    m_identity_isValid = ::OpenAPI::fromJsonValue(m_identity, json[QString("identity")]);
    m_identity_isSet = !json[QString("identity")].isNull() && m_identity_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListWebApps_200_response_value_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_identity.isSet()) {
        obj.insert(QString("identity"), ::OpenAPI::toJsonValue(m_identity));
    }
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    return obj;
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_identity OAIAppServicePlans_ListWebApps_200_response_value_inner::getIdentity() const {
    return m_identity;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner::setIdentity(const OAIAppServicePlans_ListWebApps_200_response_value_inner_identity &identity) {
    m_identity = identity;
    m_identity_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner::is_identity_Set() const{
    return m_identity_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner::is_identity_Valid() const{
    return m_identity_isValid;
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties OAIAppServicePlans_ListWebApps_200_response_value_inner::getProperties() const {
    return m_properties;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner::setProperties(const OAIAppServicePlans_ListWebApps_200_response_value_inner_properties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner::is_properties_Valid() const{
    return m_properties_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_identity.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
