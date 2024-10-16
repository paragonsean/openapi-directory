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

#include "OAIUpdateDevicesResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateDevicesResponse::OAIUpdateDevicesResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateDevicesResponse::OAIUpdateDevicesResponse() {
    this->initializeModel();
}

OAIUpdateDevicesResponse::~OAIUpdateDevicesResponse() {}

void OAIUpdateDevicesResponse::initializeModel() {

    m_status_url_isSet = false;
    m_status_url_isValid = false;
}

void OAIUpdateDevicesResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateDevicesResponse::fromJsonObject(QJsonObject json) {

    m_status_url_isValid = ::OpenAPI::fromJsonValue(m_status_url, json[QString("status_url")]);
    m_status_url_isSet = !json[QString("status_url")].isNull() && m_status_url_isValid;
}

QString OAIUpdateDevicesResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateDevicesResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_status_url_isSet) {
        obj.insert(QString("status_url"), ::OpenAPI::toJsonValue(m_status_url));
    }
    return obj;
}

QString OAIUpdateDevicesResponse::getStatusUrl() const {
    return m_status_url;
}
void OAIUpdateDevicesResponse::setStatusUrl(const QString &status_url) {
    m_status_url = status_url;
    m_status_url_isSet = true;
}

bool OAIUpdateDevicesResponse::is_status_url_Set() const{
    return m_status_url_isSet;
}

bool OAIUpdateDevicesResponse::is_status_url_Valid() const{
    return m_status_url_isValid;
}

bool OAIUpdateDevicesResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_status_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateDevicesResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_status_url_isValid && true;
}

} // namespace OpenAPI
