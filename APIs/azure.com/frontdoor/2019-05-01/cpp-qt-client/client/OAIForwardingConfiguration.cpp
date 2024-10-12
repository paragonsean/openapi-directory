/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIForwardingConfiguration.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIForwardingConfiguration::OAIForwardingConfiguration(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIForwardingConfiguration::OAIForwardingConfiguration() {
    this->initializeModel();
}

OAIForwardingConfiguration::~OAIForwardingConfiguration() {}

void OAIForwardingConfiguration::initializeModel() {

    m_backend_pool_isSet = false;
    m_backend_pool_isValid = false;

    m_cache_configuration_isSet = false;
    m_cache_configuration_isValid = false;

    m_custom_forwarding_path_isSet = false;
    m_custom_forwarding_path_isValid = false;

    m_forwarding_protocol_isSet = false;
    m_forwarding_protocol_isValid = false;

    m_odata_type_isSet = false;
    m_odata_type_isValid = false;
}

void OAIForwardingConfiguration::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIForwardingConfiguration::fromJsonObject(QJsonObject json) {

    m_backend_pool_isValid = ::OpenAPI::fromJsonValue(m_backend_pool, json[QString("backendPool")]);
    m_backend_pool_isSet = !json[QString("backendPool")].isNull() && m_backend_pool_isValid;

    m_cache_configuration_isValid = ::OpenAPI::fromJsonValue(m_cache_configuration, json[QString("cacheConfiguration")]);
    m_cache_configuration_isSet = !json[QString("cacheConfiguration")].isNull() && m_cache_configuration_isValid;

    m_custom_forwarding_path_isValid = ::OpenAPI::fromJsonValue(m_custom_forwarding_path, json[QString("customForwardingPath")]);
    m_custom_forwarding_path_isSet = !json[QString("customForwardingPath")].isNull() && m_custom_forwarding_path_isValid;

    m_forwarding_protocol_isValid = ::OpenAPI::fromJsonValue(m_forwarding_protocol, json[QString("forwardingProtocol")]);
    m_forwarding_protocol_isSet = !json[QString("forwardingProtocol")].isNull() && m_forwarding_protocol_isValid;

    m_odata_type_isValid = ::OpenAPI::fromJsonValue(m_odata_type, json[QString("@odata.type")]);
    m_odata_type_isSet = !json[QString("@odata.type")].isNull() && m_odata_type_isValid;
}

QString OAIForwardingConfiguration::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIForwardingConfiguration::asJsonObject() const {
    QJsonObject obj;
    if (m_backend_pool.isSet()) {
        obj.insert(QString("backendPool"), ::OpenAPI::toJsonValue(m_backend_pool));
    }
    if (m_cache_configuration.isSet()) {
        obj.insert(QString("cacheConfiguration"), ::OpenAPI::toJsonValue(m_cache_configuration));
    }
    if (m_custom_forwarding_path_isSet) {
        obj.insert(QString("customForwardingPath"), ::OpenAPI::toJsonValue(m_custom_forwarding_path));
    }
    if (m_forwarding_protocol_isSet) {
        obj.insert(QString("forwardingProtocol"), ::OpenAPI::toJsonValue(m_forwarding_protocol));
    }
    if (m_odata_type_isSet) {
        obj.insert(QString("@odata.type"), ::OpenAPI::toJsonValue(m_odata_type));
    }
    return obj;
}

OAIObject OAIForwardingConfiguration::getBackendPool() const {
    return m_backend_pool;
}
void OAIForwardingConfiguration::setBackendPool(const OAIObject &backend_pool) {
    m_backend_pool = backend_pool;
    m_backend_pool_isSet = true;
}

bool OAIForwardingConfiguration::is_backend_pool_Set() const{
    return m_backend_pool_isSet;
}

bool OAIForwardingConfiguration::is_backend_pool_Valid() const{
    return m_backend_pool_isValid;
}

OAICacheConfiguration OAIForwardingConfiguration::getCacheConfiguration() const {
    return m_cache_configuration;
}
void OAIForwardingConfiguration::setCacheConfiguration(const OAICacheConfiguration &cache_configuration) {
    m_cache_configuration = cache_configuration;
    m_cache_configuration_isSet = true;
}

bool OAIForwardingConfiguration::is_cache_configuration_Set() const{
    return m_cache_configuration_isSet;
}

bool OAIForwardingConfiguration::is_cache_configuration_Valid() const{
    return m_cache_configuration_isValid;
}

QString OAIForwardingConfiguration::getCustomForwardingPath() const {
    return m_custom_forwarding_path;
}
void OAIForwardingConfiguration::setCustomForwardingPath(const QString &custom_forwarding_path) {
    m_custom_forwarding_path = custom_forwarding_path;
    m_custom_forwarding_path_isSet = true;
}

bool OAIForwardingConfiguration::is_custom_forwarding_path_Set() const{
    return m_custom_forwarding_path_isSet;
}

bool OAIForwardingConfiguration::is_custom_forwarding_path_Valid() const{
    return m_custom_forwarding_path_isValid;
}

QString OAIForwardingConfiguration::getForwardingProtocol() const {
    return m_forwarding_protocol;
}
void OAIForwardingConfiguration::setForwardingProtocol(const QString &forwarding_protocol) {
    m_forwarding_protocol = forwarding_protocol;
    m_forwarding_protocol_isSet = true;
}

bool OAIForwardingConfiguration::is_forwarding_protocol_Set() const{
    return m_forwarding_protocol_isSet;
}

bool OAIForwardingConfiguration::is_forwarding_protocol_Valid() const{
    return m_forwarding_protocol_isValid;
}

QString OAIForwardingConfiguration::getOdataType() const {
    return m_odata_type;
}
void OAIForwardingConfiguration::setOdataType(const QString &odata_type) {
    m_odata_type = odata_type;
    m_odata_type_isSet = true;
}

bool OAIForwardingConfiguration::is_odata_type_Set() const{
    return m_odata_type_isSet;
}

bool OAIForwardingConfiguration::is_odata_type_Valid() const{
    return m_odata_type_isValid;
}

bool OAIForwardingConfiguration::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_backend_pool.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_cache_configuration.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_forwarding_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_forwarding_protocol_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_odata_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIForwardingConfiguration::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_odata_type_isValid && true;
}

} // namespace OpenAPI
