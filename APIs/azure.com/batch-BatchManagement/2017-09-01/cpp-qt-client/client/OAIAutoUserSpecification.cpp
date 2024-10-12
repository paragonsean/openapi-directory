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

#include "OAIAutoUserSpecification.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAutoUserSpecification::OAIAutoUserSpecification(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAutoUserSpecification::OAIAutoUserSpecification() {
    this->initializeModel();
}

OAIAutoUserSpecification::~OAIAutoUserSpecification() {}

void OAIAutoUserSpecification::initializeModel() {

    m_elevation_level_isSet = false;
    m_elevation_level_isValid = false;

    m_scope_isSet = false;
    m_scope_isValid = false;
}

void OAIAutoUserSpecification::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAutoUserSpecification::fromJsonObject(QJsonObject json) {

    m_elevation_level_isValid = ::OpenAPI::fromJsonValue(m_elevation_level, json[QString("elevationLevel")]);
    m_elevation_level_isSet = !json[QString("elevationLevel")].isNull() && m_elevation_level_isValid;

    m_scope_isValid = ::OpenAPI::fromJsonValue(m_scope, json[QString("scope")]);
    m_scope_isSet = !json[QString("scope")].isNull() && m_scope_isValid;
}

QString OAIAutoUserSpecification::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAutoUserSpecification::asJsonObject() const {
    QJsonObject obj;
    if (m_elevation_level.isSet()) {
        obj.insert(QString("elevationLevel"), ::OpenAPI::toJsonValue(m_elevation_level));
    }
    if (m_scope_isSet) {
        obj.insert(QString("scope"), ::OpenAPI::toJsonValue(m_scope));
    }
    return obj;
}

OAIElevationLevel OAIAutoUserSpecification::getElevationLevel() const {
    return m_elevation_level;
}
void OAIAutoUserSpecification::setElevationLevel(const OAIElevationLevel &elevation_level) {
    m_elevation_level = elevation_level;
    m_elevation_level_isSet = true;
}

bool OAIAutoUserSpecification::is_elevation_level_Set() const{
    return m_elevation_level_isSet;
}

bool OAIAutoUserSpecification::is_elevation_level_Valid() const{
    return m_elevation_level_isValid;
}

QString OAIAutoUserSpecification::getScope() const {
    return m_scope;
}
void OAIAutoUserSpecification::setScope(const QString &scope) {
    m_scope = scope;
    m_scope_isSet = true;
}

bool OAIAutoUserSpecification::is_scope_Set() const{
    return m_scope_isSet;
}

bool OAIAutoUserSpecification::is_scope_Valid() const{
    return m_scope_isValid;
}

bool OAIAutoUserSpecification::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_elevation_level.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_scope_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAutoUserSpecification::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
