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

#include "OAIMoveNetworkSmDevices_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMoveNetworkSmDevices_200_response::OAIMoveNetworkSmDevices_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMoveNetworkSmDevices_200_response::OAIMoveNetworkSmDevices_200_response() {
    this->initializeModel();
}

OAIMoveNetworkSmDevices_200_response::~OAIMoveNetworkSmDevices_200_response() {}

void OAIMoveNetworkSmDevices_200_response::initializeModel() {

    m_ids_isSet = false;
    m_ids_isValid = false;

    m_new_network_isSet = false;
    m_new_network_isValid = false;
}

void OAIMoveNetworkSmDevices_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMoveNetworkSmDevices_200_response::fromJsonObject(QJsonObject json) {

    m_ids_isValid = ::OpenAPI::fromJsonValue(m_ids, json[QString("ids")]);
    m_ids_isSet = !json[QString("ids")].isNull() && m_ids_isValid;

    m_new_network_isValid = ::OpenAPI::fromJsonValue(m_new_network, json[QString("newNetwork")]);
    m_new_network_isSet = !json[QString("newNetwork")].isNull() && m_new_network_isValid;
}

QString OAIMoveNetworkSmDevices_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMoveNetworkSmDevices_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_ids.size() > 0) {
        obj.insert(QString("ids"), ::OpenAPI::toJsonValue(m_ids));
    }
    if (m_new_network_isSet) {
        obj.insert(QString("newNetwork"), ::OpenAPI::toJsonValue(m_new_network));
    }
    return obj;
}

QList<QString> OAIMoveNetworkSmDevices_200_response::getIds() const {
    return m_ids;
}
void OAIMoveNetworkSmDevices_200_response::setIds(const QList<QString> &ids) {
    m_ids = ids;
    m_ids_isSet = true;
}

bool OAIMoveNetworkSmDevices_200_response::is_ids_Set() const{
    return m_ids_isSet;
}

bool OAIMoveNetworkSmDevices_200_response::is_ids_Valid() const{
    return m_ids_isValid;
}

QString OAIMoveNetworkSmDevices_200_response::getNewNetwork() const {
    return m_new_network;
}
void OAIMoveNetworkSmDevices_200_response::setNewNetwork(const QString &new_network) {
    m_new_network = new_network;
    m_new_network_isSet = true;
}

bool OAIMoveNetworkSmDevices_200_response::is_new_network_Set() const{
    return m_new_network_isSet;
}

bool OAIMoveNetworkSmDevices_200_response::is_new_network_Valid() const{
    return m_new_network_isValid;
}

bool OAIMoveNetworkSmDevices_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_new_network_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMoveNetworkSmDevices_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
