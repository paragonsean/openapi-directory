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

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner() {
    this->initializeModel();
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner() {}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::initializeModel() {

    m_host_type_isSet = false;
    m_host_type_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_ssl_state_isSet = false;
    m_ssl_state_isValid = false;

    m_thumbprint_isSet = false;
    m_thumbprint_isValid = false;

    m_to_update_isSet = false;
    m_to_update_isValid = false;

    m_virtual_ip_isSet = false;
    m_virtual_ip_isValid = false;
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::fromJsonObject(QJsonObject json) {

    m_host_type_isValid = ::OpenAPI::fromJsonValue(m_host_type, json[QString("hostType")]);
    m_host_type_isSet = !json[QString("hostType")].isNull() && m_host_type_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_ssl_state_isValid = ::OpenAPI::fromJsonValue(m_ssl_state, json[QString("sslState")]);
    m_ssl_state_isSet = !json[QString("sslState")].isNull() && m_ssl_state_isValid;

    m_thumbprint_isValid = ::OpenAPI::fromJsonValue(m_thumbprint, json[QString("thumbprint")]);
    m_thumbprint_isSet = !json[QString("thumbprint")].isNull() && m_thumbprint_isValid;

    m_to_update_isValid = ::OpenAPI::fromJsonValue(m_to_update, json[QString("toUpdate")]);
    m_to_update_isSet = !json[QString("toUpdate")].isNull() && m_to_update_isValid;

    m_virtual_ip_isValid = ::OpenAPI::fromJsonValue(m_virtual_ip, json[QString("virtualIP")]);
    m_virtual_ip_isSet = !json[QString("virtualIP")].isNull() && m_virtual_ip_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_host_type_isSet) {
        obj.insert(QString("hostType"), ::OpenAPI::toJsonValue(m_host_type));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_ssl_state_isSet) {
        obj.insert(QString("sslState"), ::OpenAPI::toJsonValue(m_ssl_state));
    }
    if (m_thumbprint_isSet) {
        obj.insert(QString("thumbprint"), ::OpenAPI::toJsonValue(m_thumbprint));
    }
    if (m_to_update_isSet) {
        obj.insert(QString("toUpdate"), ::OpenAPI::toJsonValue(m_to_update));
    }
    if (m_virtual_ip_isSet) {
        obj.insert(QString("virtualIP"), ::OpenAPI::toJsonValue(m_virtual_ip));
    }
    return obj;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::getHostType() const {
    return m_host_type;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::setHostType(const QString &host_type) {
    m_host_type = host_type;
    m_host_type_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::is_host_type_Set() const{
    return m_host_type_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::is_host_type_Valid() const{
    return m_host_type_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::getName() const {
    return m_name;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::getSslState() const {
    return m_ssl_state;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::setSslState(const QString &ssl_state) {
    m_ssl_state = ssl_state;
    m_ssl_state_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::is_ssl_state_Set() const{
    return m_ssl_state_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::is_ssl_state_Valid() const{
    return m_ssl_state_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::getThumbprint() const {
    return m_thumbprint;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::setThumbprint(const QString &thumbprint) {
    m_thumbprint = thumbprint;
    m_thumbprint_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::is_thumbprint_Set() const{
    return m_thumbprint_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::is_thumbprint_Valid() const{
    return m_thumbprint_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::isToUpdate() const {
    return m_to_update;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::setToUpdate(const bool &to_update) {
    m_to_update = to_update;
    m_to_update_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::is_to_update_Set() const{
    return m_to_update_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::is_to_update_Valid() const{
    return m_to_update_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::getVirtualIp() const {
    return m_virtual_ip;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::setVirtualIp(const QString &virtual_ip) {
    m_virtual_ip = virtual_ip;
    m_virtual_ip_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::is_virtual_ip_Set() const{
    return m_virtual_ip_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::is_virtual_ip_Valid() const{
    return m_virtual_ip_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_host_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ssl_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_thumbprint_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_to_update_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_virtual_ip_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_hostNameSslStates_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
