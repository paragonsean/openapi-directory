/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
 *
 * The version of the OpenAPI document: 2019-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIdentityProvider_ListByService_default_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIdentityProvider_ListByService_default_response::OAIIdentityProvider_ListByService_default_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIdentityProvider_ListByService_default_response::OAIIdentityProvider_ListByService_default_response() {
    this->initializeModel();
}

OAIIdentityProvider_ListByService_default_response::~OAIIdentityProvider_ListByService_default_response() {}

void OAIIdentityProvider_ListByService_default_response::initializeModel() {

    m_error_isSet = false;
    m_error_isValid = false;
}

void OAIIdentityProvider_ListByService_default_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIdentityProvider_ListByService_default_response::fromJsonObject(QJsonObject json) {

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;
}

QString OAIIdentityProvider_ListByService_default_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIdentityProvider_ListByService_default_response::asJsonObject() const {
    QJsonObject obj;
    if (m_error.isSet()) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    return obj;
}

OAIIdentityProvider_ListByService_default_response_error OAIIdentityProvider_ListByService_default_response::getError() const {
    return m_error;
}
void OAIIdentityProvider_ListByService_default_response::setError(const OAIIdentityProvider_ListByService_default_response_error &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIIdentityProvider_ListByService_default_response::is_error_Set() const{
    return m_error_isSet;
}

bool OAIIdentityProvider_ListByService_default_response::is_error_Valid() const{
    return m_error_isValid;
}

bool OAIIdentityProvider_ListByService_default_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIdentityProvider_ListByService_default_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
