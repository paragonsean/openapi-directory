/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAvailableProviderOperation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAvailableProviderOperation::OAIAvailableProviderOperation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAvailableProviderOperation::OAIAvailableProviderOperation() {
    this->initializeModel();
}

OAIAvailableProviderOperation::~OAIAvailableProviderOperation() {}

void OAIAvailableProviderOperation::initializeModel() {

    m_display_isSet = false;
    m_display_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_origin_isSet = false;
    m_origin_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;
}

void OAIAvailableProviderOperation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAvailableProviderOperation::fromJsonObject(QJsonObject json) {

    m_display_isValid = ::OpenAPI::fromJsonValue(m_display, json[QString("display")]);
    m_display_isSet = !json[QString("display")].isNull() && m_display_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_origin_isValid = ::OpenAPI::fromJsonValue(m_origin, json[QString("origin")]);
    m_origin_isSet = !json[QString("origin")].isNull() && m_origin_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;
}

QString OAIAvailableProviderOperation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAvailableProviderOperation::asJsonObject() const {
    QJsonObject obj;
    if (m_display.isSet()) {
        obj.insert(QString("display"), ::OpenAPI::toJsonValue(m_display));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_origin_isSet) {
        obj.insert(QString("origin"), ::OpenAPI::toJsonValue(m_origin));
    }
    if (m_properties_isSet) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    return obj;
}

OAIAvailableProviderOperationDisplay OAIAvailableProviderOperation::getDisplay() const {
    return m_display;
}
void OAIAvailableProviderOperation::setDisplay(const OAIAvailableProviderOperationDisplay &display) {
    m_display = display;
    m_display_isSet = true;
}

bool OAIAvailableProviderOperation::is_display_Set() const{
    return m_display_isSet;
}

bool OAIAvailableProviderOperation::is_display_Valid() const{
    return m_display_isValid;
}

QString OAIAvailableProviderOperation::getName() const {
    return m_name;
}
void OAIAvailableProviderOperation::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAvailableProviderOperation::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAvailableProviderOperation::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIAvailableProviderOperation::getOrigin() const {
    return m_origin;
}
void OAIAvailableProviderOperation::setOrigin(const QString &origin) {
    m_origin = origin;
    m_origin_isSet = true;
}

bool OAIAvailableProviderOperation::is_origin_Set() const{
    return m_origin_isSet;
}

bool OAIAvailableProviderOperation::is_origin_Valid() const{
    return m_origin_isValid;
}

OAIObject OAIAvailableProviderOperation::getProperties() const {
    return m_properties;
}
void OAIAvailableProviderOperation::setProperties(const OAIObject &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIAvailableProviderOperation::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIAvailableProviderOperation::is_properties_Valid() const{
    return m_properties_isValid;
}

bool OAIAvailableProviderOperation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_display.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_origin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAvailableProviderOperation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
