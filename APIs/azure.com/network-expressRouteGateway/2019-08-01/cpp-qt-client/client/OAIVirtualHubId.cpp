/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVirtualHubId.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVirtualHubId::OAIVirtualHubId(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVirtualHubId::OAIVirtualHubId() {
    this->initializeModel();
}

OAIVirtualHubId::~OAIVirtualHubId() {}

void OAIVirtualHubId::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;
}

void OAIVirtualHubId::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVirtualHubId::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;
}

QString OAIVirtualHubId::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVirtualHubId::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    return obj;
}

QString OAIVirtualHubId::getId() const {
    return m_id;
}
void OAIVirtualHubId::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIVirtualHubId::is_id_Set() const{
    return m_id_isSet;
}

bool OAIVirtualHubId::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIVirtualHubId::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVirtualHubId::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
