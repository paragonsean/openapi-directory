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

#include "OAISplitNetwork_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISplitNetwork_200_response::OAISplitNetwork_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISplitNetwork_200_response::OAISplitNetwork_200_response() {
    this->initializeModel();
}

OAISplitNetwork_200_response::~OAISplitNetwork_200_response() {}

void OAISplitNetwork_200_response::initializeModel() {

    m_resulting_networks_isSet = false;
    m_resulting_networks_isValid = false;
}

void OAISplitNetwork_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISplitNetwork_200_response::fromJsonObject(QJsonObject json) {

    m_resulting_networks_isValid = ::OpenAPI::fromJsonValue(m_resulting_networks, json[QString("resultingNetworks")]);
    m_resulting_networks_isSet = !json[QString("resultingNetworks")].isNull() && m_resulting_networks_isValid;
}

QString OAISplitNetwork_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISplitNetwork_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_resulting_networks.size() > 0) {
        obj.insert(QString("resultingNetworks"), ::OpenAPI::toJsonValue(m_resulting_networks));
    }
    return obj;
}

QList<OAIGetNetwork_200_response> OAISplitNetwork_200_response::getResultingNetworks() const {
    return m_resulting_networks;
}
void OAISplitNetwork_200_response::setResultingNetworks(const QList<OAIGetNetwork_200_response> &resulting_networks) {
    m_resulting_networks = resulting_networks;
    m_resulting_networks_isSet = true;
}

bool OAISplitNetwork_200_response::is_resulting_networks_Set() const{
    return m_resulting_networks_isSet;
}

bool OAISplitNetwork_200_response::is_resulting_networks_Valid() const{
    return m_resulting_networks_isValid;
}

bool OAISplitNetwork_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_resulting_networks.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISplitNetwork_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
