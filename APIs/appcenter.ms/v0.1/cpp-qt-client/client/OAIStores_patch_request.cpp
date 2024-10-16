/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIStores_patch_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStores_patch_request::OAIStores_patch_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStores_patch_request::OAIStores_patch_request() {
    this->initializeModel();
}

OAIStores_patch_request::~OAIStores_patch_request() {}

void OAIStores_patch_request::initializeModel() {

    m_service_connection_id_isSet = false;
    m_service_connection_id_isValid = false;
}

void OAIStores_patch_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStores_patch_request::fromJsonObject(QJsonObject json) {

    m_service_connection_id_isValid = ::OpenAPI::fromJsonValue(m_service_connection_id, json[QString("service_connection_id")]);
    m_service_connection_id_isSet = !json[QString("service_connection_id")].isNull() && m_service_connection_id_isValid;
}

QString OAIStores_patch_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStores_patch_request::asJsonObject() const {
    QJsonObject obj;
    if (m_service_connection_id_isSet) {
        obj.insert(QString("service_connection_id"), ::OpenAPI::toJsonValue(m_service_connection_id));
    }
    return obj;
}

QString OAIStores_patch_request::getServiceConnectionId() const {
    return m_service_connection_id;
}
void OAIStores_patch_request::setServiceConnectionId(const QString &service_connection_id) {
    m_service_connection_id = service_connection_id;
    m_service_connection_id_isSet = true;
}

bool OAIStores_patch_request::is_service_connection_id_Set() const{
    return m_service_connection_id_isSet;
}

bool OAIStores_patch_request::is_service_connection_id_Valid() const{
    return m_service_connection_id_isValid;
}

bool OAIStores_patch_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_service_connection_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStores_patch_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_service_connection_id_isValid && true;
}

} // namespace OpenAPI
