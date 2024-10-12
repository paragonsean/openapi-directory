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

#include "OAITransitClassAddMessageResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITransitClassAddMessageResponse::OAITransitClassAddMessageResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITransitClassAddMessageResponse::OAITransitClassAddMessageResponse() {
    this->initializeModel();
}

OAITransitClassAddMessageResponse::~OAITransitClassAddMessageResponse() {}

void OAITransitClassAddMessageResponse::initializeModel() {

    m_resource_isSet = false;
    m_resource_isValid = false;
}

void OAITransitClassAddMessageResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITransitClassAddMessageResponse::fromJsonObject(QJsonObject json) {

    m_resource_isValid = ::OpenAPI::fromJsonValue(m_resource, json[QString("resource")]);
    m_resource_isSet = !json[QString("resource")].isNull() && m_resource_isValid;
}

QString OAITransitClassAddMessageResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITransitClassAddMessageResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_resource.isSet()) {
        obj.insert(QString("resource"), ::OpenAPI::toJsonValue(m_resource));
    }
    return obj;
}

OAITransitClass OAITransitClassAddMessageResponse::getResource() const {
    return m_resource;
}
void OAITransitClassAddMessageResponse::setResource(const OAITransitClass &resource) {
    m_resource = resource;
    m_resource_isSet = true;
}

bool OAITransitClassAddMessageResponse::is_resource_Set() const{
    return m_resource_isSet;
}

bool OAITransitClassAddMessageResponse::is_resource_Valid() const{
    return m_resource_isValid;
}

bool OAITransitClassAddMessageResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_resource.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITransitClassAddMessageResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
