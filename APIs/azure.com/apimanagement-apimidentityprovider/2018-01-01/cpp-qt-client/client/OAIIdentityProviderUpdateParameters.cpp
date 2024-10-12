/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
 *
 * The version of the OpenAPI document: 2018-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIdentityProviderUpdateParameters.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIdentityProviderUpdateParameters::OAIIdentityProviderUpdateParameters(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIdentityProviderUpdateParameters::OAIIdentityProviderUpdateParameters() {
    this->initializeModel();
}

OAIIdentityProviderUpdateParameters::~OAIIdentityProviderUpdateParameters() {}

void OAIIdentityProviderUpdateParameters::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;
}

void OAIIdentityProviderUpdateParameters::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIdentityProviderUpdateParameters::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;
}

QString OAIIdentityProviderUpdateParameters::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIdentityProviderUpdateParameters::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    return obj;
}

OAIIdentityProviderUpdateProperties OAIIdentityProviderUpdateParameters::getProperties() const {
    return m_properties;
}
void OAIIdentityProviderUpdateParameters::setProperties(const OAIIdentityProviderUpdateProperties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIIdentityProviderUpdateParameters::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIIdentityProviderUpdateParameters::is_properties_Valid() const{
    return m_properties_isValid;
}

bool OAIIdentityProviderUpdateParameters::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIdentityProviderUpdateParameters::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
