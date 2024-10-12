/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAINetworkConfiguration.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINetworkConfiguration::OAINetworkConfiguration(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINetworkConfiguration::OAINetworkConfiguration() {
    this->initializeModel();
}

OAINetworkConfiguration::~OAINetworkConfiguration() {}

void OAINetworkConfiguration::initializeModel() {

    m_endpoint_configuration_isSet = false;
    m_endpoint_configuration_isValid = false;

    m_subnet_id_isSet = false;
    m_subnet_id_isValid = false;
}

void OAINetworkConfiguration::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINetworkConfiguration::fromJsonObject(QJsonObject json) {

    m_endpoint_configuration_isValid = ::OpenAPI::fromJsonValue(m_endpoint_configuration, json[QString("endpointConfiguration")]);
    m_endpoint_configuration_isSet = !json[QString("endpointConfiguration")].isNull() && m_endpoint_configuration_isValid;

    m_subnet_id_isValid = ::OpenAPI::fromJsonValue(m_subnet_id, json[QString("subnetId")]);
    m_subnet_id_isSet = !json[QString("subnetId")].isNull() && m_subnet_id_isValid;
}

QString OAINetworkConfiguration::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINetworkConfiguration::asJsonObject() const {
    QJsonObject obj;
    if (m_endpoint_configuration.isSet()) {
        obj.insert(QString("endpointConfiguration"), ::OpenAPI::toJsonValue(m_endpoint_configuration));
    }
    if (m_subnet_id_isSet) {
        obj.insert(QString("subnetId"), ::OpenAPI::toJsonValue(m_subnet_id));
    }
    return obj;
}

OAIPoolEndpointConfiguration OAINetworkConfiguration::getEndpointConfiguration() const {
    return m_endpoint_configuration;
}
void OAINetworkConfiguration::setEndpointConfiguration(const OAIPoolEndpointConfiguration &endpoint_configuration) {
    m_endpoint_configuration = endpoint_configuration;
    m_endpoint_configuration_isSet = true;
}

bool OAINetworkConfiguration::is_endpoint_configuration_Set() const{
    return m_endpoint_configuration_isSet;
}

bool OAINetworkConfiguration::is_endpoint_configuration_Valid() const{
    return m_endpoint_configuration_isValid;
}

QString OAINetworkConfiguration::getSubnetId() const {
    return m_subnet_id;
}
void OAINetworkConfiguration::setSubnetId(const QString &subnet_id) {
    m_subnet_id = subnet_id;
    m_subnet_id_isSet = true;
}

bool OAINetworkConfiguration::is_subnet_id_Set() const{
    return m_subnet_id_isSet;
}

bool OAINetworkConfiguration::is_subnet_id_Valid() const{
    return m_subnet_id_isValid;
}

bool OAINetworkConfiguration::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_endpoint_configuration.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_subnet_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINetworkConfiguration::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
