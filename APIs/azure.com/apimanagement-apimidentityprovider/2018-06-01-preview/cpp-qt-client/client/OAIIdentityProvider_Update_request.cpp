/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIdentityProvider_Update_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIdentityProvider_Update_request::OAIIdentityProvider_Update_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIdentityProvider_Update_request::OAIIdentityProvider_Update_request() {
    this->initializeModel();
}

OAIIdentityProvider_Update_request::~OAIIdentityProvider_Update_request() {}

void OAIIdentityProvider_Update_request::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;
}

void OAIIdentityProvider_Update_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIdentityProvider_Update_request::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;
}

QString OAIIdentityProvider_Update_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIdentityProvider_Update_request::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    return obj;
}

OAIIdentityProvider_Update_request_properties OAIIdentityProvider_Update_request::getProperties() const {
    return m_properties;
}
void OAIIdentityProvider_Update_request::setProperties(const OAIIdentityProvider_Update_request_properties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIIdentityProvider_Update_request::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIIdentityProvider_Update_request::is_properties_Valid() const{
    return m_properties_isValid;
}

bool OAIIdentityProvider_Update_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIdentityProvider_Update_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
