/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2019-12-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAINotification_ListByService_default_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINotification_ListByService_default_response::OAINotification_ListByService_default_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINotification_ListByService_default_response::OAINotification_ListByService_default_response() {
    this->initializeModel();
}

OAINotification_ListByService_default_response::~OAINotification_ListByService_default_response() {}

void OAINotification_ListByService_default_response::initializeModel() {

    m_error_isSet = false;
    m_error_isValid = false;
}

void OAINotification_ListByService_default_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINotification_ListByService_default_response::fromJsonObject(QJsonObject json) {

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;
}

QString OAINotification_ListByService_default_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINotification_ListByService_default_response::asJsonObject() const {
    QJsonObject obj;
    if (m_error.isSet()) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    return obj;
}

OAINotification_ListByService_default_response_error OAINotification_ListByService_default_response::getError() const {
    return m_error;
}
void OAINotification_ListByService_default_response::setError(const OAINotification_ListByService_default_response_error &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAINotification_ListByService_default_response::is_error_Set() const{
    return m_error_isSet;
}

bool OAINotification_ListByService_default_response::is_error_Valid() const{
    return m_error_isValid;
}

bool OAINotification_ListByService_default_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINotification_ListByService_default_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
