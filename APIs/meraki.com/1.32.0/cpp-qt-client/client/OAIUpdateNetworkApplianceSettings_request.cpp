/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUpdateNetworkApplianceSettings_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkApplianceSettings_request::OAIUpdateNetworkApplianceSettings_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkApplianceSettings_request::OAIUpdateNetworkApplianceSettings_request() {
    this->initializeModel();
}

OAIUpdateNetworkApplianceSettings_request::~OAIUpdateNetworkApplianceSettings_request() {}

void OAIUpdateNetworkApplianceSettings_request::initializeModel() {

    m_client_tracking_method_isSet = false;
    m_client_tracking_method_isValid = false;

    m_deployment_mode_isSet = false;
    m_deployment_mode_isValid = false;

    m_dynamic_dns_isSet = false;
    m_dynamic_dns_isValid = false;
}

void OAIUpdateNetworkApplianceSettings_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkApplianceSettings_request::fromJsonObject(QJsonObject json) {

    m_client_tracking_method_isValid = ::OpenAPI::fromJsonValue(m_client_tracking_method, json[QString("clientTrackingMethod")]);
    m_client_tracking_method_isSet = !json[QString("clientTrackingMethod")].isNull() && m_client_tracking_method_isValid;

    m_deployment_mode_isValid = ::OpenAPI::fromJsonValue(m_deployment_mode, json[QString("deploymentMode")]);
    m_deployment_mode_isSet = !json[QString("deploymentMode")].isNull() && m_deployment_mode_isValid;

    m_dynamic_dns_isValid = ::OpenAPI::fromJsonValue(m_dynamic_dns, json[QString("dynamicDns")]);
    m_dynamic_dns_isSet = !json[QString("dynamicDns")].isNull() && m_dynamic_dns_isValid;
}

QString OAIUpdateNetworkApplianceSettings_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkApplianceSettings_request::asJsonObject() const {
    QJsonObject obj;
    if (m_client_tracking_method_isSet) {
        obj.insert(QString("clientTrackingMethod"), ::OpenAPI::toJsonValue(m_client_tracking_method));
    }
    if (m_deployment_mode_isSet) {
        obj.insert(QString("deploymentMode"), ::OpenAPI::toJsonValue(m_deployment_mode));
    }
    if (m_dynamic_dns.isSet()) {
        obj.insert(QString("dynamicDns"), ::OpenAPI::toJsonValue(m_dynamic_dns));
    }
    return obj;
}

QString OAIUpdateNetworkApplianceSettings_request::getClientTrackingMethod() const {
    return m_client_tracking_method;
}
void OAIUpdateNetworkApplianceSettings_request::setClientTrackingMethod(const QString &client_tracking_method) {
    m_client_tracking_method = client_tracking_method;
    m_client_tracking_method_isSet = true;
}

bool OAIUpdateNetworkApplianceSettings_request::is_client_tracking_method_Set() const{
    return m_client_tracking_method_isSet;
}

bool OAIUpdateNetworkApplianceSettings_request::is_client_tracking_method_Valid() const{
    return m_client_tracking_method_isValid;
}

QString OAIUpdateNetworkApplianceSettings_request::getDeploymentMode() const {
    return m_deployment_mode;
}
void OAIUpdateNetworkApplianceSettings_request::setDeploymentMode(const QString &deployment_mode) {
    m_deployment_mode = deployment_mode;
    m_deployment_mode_isSet = true;
}

bool OAIUpdateNetworkApplianceSettings_request::is_deployment_mode_Set() const{
    return m_deployment_mode_isSet;
}

bool OAIUpdateNetworkApplianceSettings_request::is_deployment_mode_Valid() const{
    return m_deployment_mode_isValid;
}

OAIUpdateNetworkApplianceSettings_request_dynamicDns OAIUpdateNetworkApplianceSettings_request::getDynamicDns() const {
    return m_dynamic_dns;
}
void OAIUpdateNetworkApplianceSettings_request::setDynamicDns(const OAIUpdateNetworkApplianceSettings_request_dynamicDns &dynamic_dns) {
    m_dynamic_dns = dynamic_dns;
    m_dynamic_dns_isSet = true;
}

bool OAIUpdateNetworkApplianceSettings_request::is_dynamic_dns_Set() const{
    return m_dynamic_dns_isSet;
}

bool OAIUpdateNetworkApplianceSettings_request::is_dynamic_dns_Valid() const{
    return m_dynamic_dns_isValid;
}

bool OAIUpdateNetworkApplianceSettings_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client_tracking_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deployment_mode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dynamic_dns.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkApplianceSettings_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
