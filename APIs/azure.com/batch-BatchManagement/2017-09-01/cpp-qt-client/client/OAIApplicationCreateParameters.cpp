/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIApplicationCreateParameters.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApplicationCreateParameters::OAIApplicationCreateParameters(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApplicationCreateParameters::OAIApplicationCreateParameters() {
    this->initializeModel();
}

OAIApplicationCreateParameters::~OAIApplicationCreateParameters() {}

void OAIApplicationCreateParameters::initializeModel() {

    m_allow_updates_isSet = false;
    m_allow_updates_isValid = false;

    m_display_name_isSet = false;
    m_display_name_isValid = false;
}

void OAIApplicationCreateParameters::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApplicationCreateParameters::fromJsonObject(QJsonObject json) {

    m_allow_updates_isValid = ::OpenAPI::fromJsonValue(m_allow_updates, json[QString("allowUpdates")]);
    m_allow_updates_isSet = !json[QString("allowUpdates")].isNull() && m_allow_updates_isValid;

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("displayName")]);
    m_display_name_isSet = !json[QString("displayName")].isNull() && m_display_name_isValid;
}

QString OAIApplicationCreateParameters::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApplicationCreateParameters::asJsonObject() const {
    QJsonObject obj;
    if (m_allow_updates_isSet) {
        obj.insert(QString("allowUpdates"), ::OpenAPI::toJsonValue(m_allow_updates));
    }
    if (m_display_name_isSet) {
        obj.insert(QString("displayName"), ::OpenAPI::toJsonValue(m_display_name));
    }
    return obj;
}

bool OAIApplicationCreateParameters::isAllowUpdates() const {
    return m_allow_updates;
}
void OAIApplicationCreateParameters::setAllowUpdates(const bool &allow_updates) {
    m_allow_updates = allow_updates;
    m_allow_updates_isSet = true;
}

bool OAIApplicationCreateParameters::is_allow_updates_Set() const{
    return m_allow_updates_isSet;
}

bool OAIApplicationCreateParameters::is_allow_updates_Valid() const{
    return m_allow_updates_isValid;
}

QString OAIApplicationCreateParameters::getDisplayName() const {
    return m_display_name;
}
void OAIApplicationCreateParameters::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIApplicationCreateParameters::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIApplicationCreateParameters::is_display_name_Valid() const{
    return m_display_name_isValid;
}

bool OAIApplicationCreateParameters::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_allow_updates_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApplicationCreateParameters::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
