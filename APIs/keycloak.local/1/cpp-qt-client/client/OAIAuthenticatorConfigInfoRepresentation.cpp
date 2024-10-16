/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAuthenticatorConfigInfoRepresentation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAuthenticatorConfigInfoRepresentation::OAIAuthenticatorConfigInfoRepresentation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAuthenticatorConfigInfoRepresentation::OAIAuthenticatorConfigInfoRepresentation() {
    this->initializeModel();
}

OAIAuthenticatorConfigInfoRepresentation::~OAIAuthenticatorConfigInfoRepresentation() {}

void OAIAuthenticatorConfigInfoRepresentation::initializeModel() {

    m_help_text_isSet = false;
    m_help_text_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_provider_id_isSet = false;
    m_provider_id_isValid = false;
}

void OAIAuthenticatorConfigInfoRepresentation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAuthenticatorConfigInfoRepresentation::fromJsonObject(QJsonObject json) {

    m_help_text_isValid = ::OpenAPI::fromJsonValue(m_help_text, json[QString("helpText")]);
    m_help_text_isSet = !json[QString("helpText")].isNull() && m_help_text_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_provider_id_isValid = ::OpenAPI::fromJsonValue(m_provider_id, json[QString("providerId")]);
    m_provider_id_isSet = !json[QString("providerId")].isNull() && m_provider_id_isValid;
}

QString OAIAuthenticatorConfigInfoRepresentation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAuthenticatorConfigInfoRepresentation::asJsonObject() const {
    QJsonObject obj;
    if (m_help_text_isSet) {
        obj.insert(QString("helpText"), ::OpenAPI::toJsonValue(m_help_text));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_properties.size() > 0) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_provider_id_isSet) {
        obj.insert(QString("providerId"), ::OpenAPI::toJsonValue(m_provider_id));
    }
    return obj;
}

QString OAIAuthenticatorConfigInfoRepresentation::getHelpText() const {
    return m_help_text;
}
void OAIAuthenticatorConfigInfoRepresentation::setHelpText(const QString &help_text) {
    m_help_text = help_text;
    m_help_text_isSet = true;
}

bool OAIAuthenticatorConfigInfoRepresentation::is_help_text_Set() const{
    return m_help_text_isSet;
}

bool OAIAuthenticatorConfigInfoRepresentation::is_help_text_Valid() const{
    return m_help_text_isValid;
}

QString OAIAuthenticatorConfigInfoRepresentation::getName() const {
    return m_name;
}
void OAIAuthenticatorConfigInfoRepresentation::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAuthenticatorConfigInfoRepresentation::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAuthenticatorConfigInfoRepresentation::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIConfigPropertyRepresentation> OAIAuthenticatorConfigInfoRepresentation::getProperties() const {
    return m_properties;
}
void OAIAuthenticatorConfigInfoRepresentation::setProperties(const QList<OAIConfigPropertyRepresentation> &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIAuthenticatorConfigInfoRepresentation::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIAuthenticatorConfigInfoRepresentation::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAIAuthenticatorConfigInfoRepresentation::getProviderId() const {
    return m_provider_id;
}
void OAIAuthenticatorConfigInfoRepresentation::setProviderId(const QString &provider_id) {
    m_provider_id = provider_id;
    m_provider_id_isSet = true;
}

bool OAIAuthenticatorConfigInfoRepresentation::is_provider_id_Set() const{
    return m_provider_id_isSet;
}

bool OAIAuthenticatorConfigInfoRepresentation::is_provider_id_Valid() const{
    return m_provider_id_isValid;
}

bool OAIAuthenticatorConfigInfoRepresentation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_help_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_provider_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAuthenticatorConfigInfoRepresentation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
