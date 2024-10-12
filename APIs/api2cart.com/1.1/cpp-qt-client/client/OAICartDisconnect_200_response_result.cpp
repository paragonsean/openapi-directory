/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICartDisconnect_200_response_result.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICartDisconnect_200_response_result::OAICartDisconnect_200_response_result(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICartDisconnect_200_response_result::OAICartDisconnect_200_response_result() {
    this->initializeModel();
}

OAICartDisconnect_200_response_result::~OAICartDisconnect_200_response_result() {}

void OAICartDisconnect_200_response_result::initializeModel() {

    m_connection_isSet = false;
    m_connection_isValid = false;
}

void OAICartDisconnect_200_response_result::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICartDisconnect_200_response_result::fromJsonObject(QJsonObject json) {

    m_connection_isValid = ::OpenAPI::fromJsonValue(m_connection, json[QString("connection")]);
    m_connection_isSet = !json[QString("connection")].isNull() && m_connection_isValid;
}

QString OAICartDisconnect_200_response_result::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICartDisconnect_200_response_result::asJsonObject() const {
    QJsonObject obj;
    if (m_connection_isSet) {
        obj.insert(QString("connection"), ::OpenAPI::toJsonValue(m_connection));
    }
    return obj;
}

QString OAICartDisconnect_200_response_result::getConnection() const {
    return m_connection;
}
void OAICartDisconnect_200_response_result::setConnection(const QString &connection) {
    m_connection = connection;
    m_connection_isSet = true;
}

bool OAICartDisconnect_200_response_result::is_connection_Set() const{
    return m_connection_isSet;
}

bool OAICartDisconnect_200_response_result::is_connection_Valid() const{
    return m_connection_isValid;
}

bool OAICartDisconnect_200_response_result::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_connection_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICartDisconnect_200_response_result::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
