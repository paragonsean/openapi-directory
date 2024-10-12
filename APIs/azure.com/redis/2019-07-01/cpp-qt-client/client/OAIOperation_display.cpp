/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2019-07-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOperation_display.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOperation_display::OAIOperation_display(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOperation_display::OAIOperation_display() {
    this->initializeModel();
}

OAIOperation_display::~OAIOperation_display() {}

void OAIOperation_display::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_operation_isSet = false;
    m_operation_isValid = false;

    m_provider_isSet = false;
    m_provider_isValid = false;

    m_resource_isSet = false;
    m_resource_isValid = false;
}

void OAIOperation_display::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOperation_display::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_operation_isValid = ::OpenAPI::fromJsonValue(m_operation, json[QString("operation")]);
    m_operation_isSet = !json[QString("operation")].isNull() && m_operation_isValid;

    m_provider_isValid = ::OpenAPI::fromJsonValue(m_provider, json[QString("provider")]);
    m_provider_isSet = !json[QString("provider")].isNull() && m_provider_isValid;

    m_resource_isValid = ::OpenAPI::fromJsonValue(m_resource, json[QString("resource")]);
    m_resource_isSet = !json[QString("resource")].isNull() && m_resource_isValid;
}

QString OAIOperation_display::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOperation_display::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_operation_isSet) {
        obj.insert(QString("operation"), ::OpenAPI::toJsonValue(m_operation));
    }
    if (m_provider_isSet) {
        obj.insert(QString("provider"), ::OpenAPI::toJsonValue(m_provider));
    }
    if (m_resource_isSet) {
        obj.insert(QString("resource"), ::OpenAPI::toJsonValue(m_resource));
    }
    return obj;
}

QString OAIOperation_display::getDescription() const {
    return m_description;
}
void OAIOperation_display::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIOperation_display::is_description_Set() const{
    return m_description_isSet;
}

bool OAIOperation_display::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIOperation_display::getOperation() const {
    return m_operation;
}
void OAIOperation_display::setOperation(const QString &operation) {
    m_operation = operation;
    m_operation_isSet = true;
}

bool OAIOperation_display::is_operation_Set() const{
    return m_operation_isSet;
}

bool OAIOperation_display::is_operation_Valid() const{
    return m_operation_isValid;
}

QString OAIOperation_display::getProvider() const {
    return m_provider;
}
void OAIOperation_display::setProvider(const QString &provider) {
    m_provider = provider;
    m_provider_isSet = true;
}

bool OAIOperation_display::is_provider_Set() const{
    return m_provider_isSet;
}

bool OAIOperation_display::is_provider_Valid() const{
    return m_provider_isValid;
}

QString OAIOperation_display::getResource() const {
    return m_resource;
}
void OAIOperation_display::setResource(const QString &resource) {
    m_resource = resource;
    m_resource_isSet = true;
}

bool OAIOperation_display::is_resource_Set() const{
    return m_resource_isSet;
}

bool OAIOperation_display::is_resource_Valid() const{
    return m_resource_isValid;
}

bool OAIOperation_display::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_provider_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resource_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOperation_display::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
