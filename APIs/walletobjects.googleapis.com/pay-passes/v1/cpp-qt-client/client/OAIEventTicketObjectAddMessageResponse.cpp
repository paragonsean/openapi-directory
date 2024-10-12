/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEventTicketObjectAddMessageResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEventTicketObjectAddMessageResponse::OAIEventTicketObjectAddMessageResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEventTicketObjectAddMessageResponse::OAIEventTicketObjectAddMessageResponse() {
    this->initializeModel();
}

OAIEventTicketObjectAddMessageResponse::~OAIEventTicketObjectAddMessageResponse() {}

void OAIEventTicketObjectAddMessageResponse::initializeModel() {

    m_resource_isSet = false;
    m_resource_isValid = false;
}

void OAIEventTicketObjectAddMessageResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEventTicketObjectAddMessageResponse::fromJsonObject(QJsonObject json) {

    m_resource_isValid = ::OpenAPI::fromJsonValue(m_resource, json[QString("resource")]);
    m_resource_isSet = !json[QString("resource")].isNull() && m_resource_isValid;
}

QString OAIEventTicketObjectAddMessageResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEventTicketObjectAddMessageResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_resource.isSet()) {
        obj.insert(QString("resource"), ::OpenAPI::toJsonValue(m_resource));
    }
    return obj;
}

OAIEventTicketObject OAIEventTicketObjectAddMessageResponse::getResource() const {
    return m_resource;
}
void OAIEventTicketObjectAddMessageResponse::setResource(const OAIEventTicketObject &resource) {
    m_resource = resource;
    m_resource_isSet = true;
}

bool OAIEventTicketObjectAddMessageResponse::is_resource_Set() const{
    return m_resource_isSet;
}

bool OAIEventTicketObjectAddMessageResponse::is_resource_Valid() const{
    return m_resource_isValid;
}

bool OAIEventTicketObjectAddMessageResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_resource.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEventTicketObjectAddMessageResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
