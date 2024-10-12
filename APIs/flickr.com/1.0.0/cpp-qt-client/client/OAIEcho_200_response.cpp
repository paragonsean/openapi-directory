/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEcho_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEcho_200_response::OAIEcho_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEcho_200_response::OAIEcho_200_response() {
    this->initializeModel();
}

OAIEcho_200_response::~OAIEcho_200_response() {}

void OAIEcho_200_response::initializeModel() {

    m_echo_isSet = false;
    m_echo_isValid = false;
}

void OAIEcho_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEcho_200_response::fromJsonObject(QJsonObject json) {

    m_echo_isValid = ::OpenAPI::fromJsonValue(m_echo, json[QString("echo")]);
    m_echo_isSet = !json[QString("echo")].isNull() && m_echo_isValid;
}

QString OAIEcho_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEcho_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_echo.isSet()) {
        obj.insert(QString("echo"), ::OpenAPI::toJsonValue(m_echo));
    }
    return obj;
}

OAIGetFavoritesContextByID_200_response_count OAIEcho_200_response::getEcho() const {
    return m_echo;
}
void OAIEcho_200_response::setEcho(const OAIGetFavoritesContextByID_200_response_count &echo) {
    m_echo = echo;
    m_echo_isSet = true;
}

bool OAIEcho_200_response::is_echo_Set() const{
    return m_echo_isSet;
}

bool OAIEcho_200_response::is_echo_Valid() const{
    return m_echo_isValid;
}

bool OAIEcho_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_echo.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEcho_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
