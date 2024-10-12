/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork() {
    this->initializeModel();
}

OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::~OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork() {}

void OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_subnet_isSet = false;
    m_subnet_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_subnet_isValid = ::OpenAPI::fromJsonValue(m_subnet, json[QString("subnet")]);
    m_subnet_isSet = !json[QString("subnet")].isNull() && m_subnet_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_subnet_isSet) {
        obj.insert(QString("subnet"), ::OpenAPI::toJsonValue(m_subnet));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::getId() const {
    return m_id;
}
void OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::is_id_Set() const{
    return m_id_isSet;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::getName() const {
    return m_name;
}
void OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::is_name_Set() const{
    return m_name_isSet;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::getSubnet() const {
    return m_subnet;
}
void OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::setSubnet(const QString &subnet) {
    m_subnet = subnet;
    m_subnet_isSet = true;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::is_subnet_Set() const{
    return m_subnet_isSet;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::is_subnet_Valid() const{
    return m_subnet_isValid;
}

QString OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::getType() const {
    return m_type;
}
void OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::is_type_Set() const{
    return m_type_isSet;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subnet_isSet) {
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

bool OAIDeploymentLocations_hostingEnvironments_inner_virtualNetwork::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
