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

#include "OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner() {
    this->initializeModel();
}

OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::~OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner() {}

void OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::initializeModel() {

    m_action_isSet = false;
    m_action_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_order_isSet = false;
    m_order_isValid = false;

    m_remote_subnet_isSet = false;
    m_remote_subnet_isValid = false;
}

void OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::fromJsonObject(QJsonObject json) {

    m_action_isValid = ::OpenAPI::fromJsonValue(m_action, json[QString("action")]);
    m_action_isSet = !json[QString("action")].isNull() && m_action_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_order_isValid = ::OpenAPI::fromJsonValue(m_order, json[QString("order")]);
    m_order_isSet = !json[QString("order")].isNull() && m_order_isValid;

    m_remote_subnet_isValid = ::OpenAPI::fromJsonValue(m_remote_subnet, json[QString("remoteSubnet")]);
    m_remote_subnet_isSet = !json[QString("remoteSubnet")].isNull() && m_remote_subnet_isValid;
}

QString OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_action_isSet) {
        obj.insert(QString("action"), ::OpenAPI::toJsonValue(m_action));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_order_isSet) {
        obj.insert(QString("order"), ::OpenAPI::toJsonValue(m_order));
    }
    if (m_remote_subnet_isSet) {
        obj.insert(QString("remoteSubnet"), ::OpenAPI::toJsonValue(m_remote_subnet));
    }
    return obj;
}

QString OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::getAction() const {
    return m_action;
}
void OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::setAction(const QString &action) {
    m_action = action;
    m_action_isSet = true;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::is_action_Set() const{
    return m_action_isSet;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::is_action_Valid() const{
    return m_action_isValid;
}

QString OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::getDescription() const {
    return m_description;
}
void OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::is_description_Set() const{
    return m_description_isSet;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::getOrder() const {
    return m_order;
}
void OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::setOrder(const qint32 &order) {
    m_order = order;
    m_order_isSet = true;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::is_order_Set() const{
    return m_order_isSet;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::is_order_Valid() const{
    return m_order_isValid;
}

QString OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::getRemoteSubnet() const {
    return m_remote_subnet;
}
void OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::setRemoteSubnet(const QString &remote_subnet) {
    m_remote_subnet = remote_subnet;
    m_remote_subnet_isSet = true;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::is_remote_subnet_Set() const{
    return m_remote_subnet_isSet;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::is_remote_subnet_Valid() const{
    return m_remote_subnet_isValid;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_action_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_remote_subnet_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_networkAccessControlList_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
