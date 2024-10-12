/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner() {
    this->initializeModel();
}

OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::~OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner() {}

void OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::initializeModel() {

    m_actual_start_isSet = false;
    m_actual_start_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_territories_isSet = false;
    m_territories_isValid = false;
}

void OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::fromJsonObject(QJsonObject json) {

    m_actual_start_isValid = ::OpenAPI::fromJsonValue(m_actual_start, json[QString("actual_start")]);
    m_actual_start_isSet = !json[QString("actual_start")].isNull() && m_actual_start_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_territories_isValid = ::OpenAPI::fromJsonValue(m_territories, json[QString("territories")]);
    m_territories_isSet = !json[QString("territories")].isNull() && m_territories_isValid;
}

QString OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_actual_start_isSet) {
        obj.insert(QString("actual_start"), ::OpenAPI::toJsonValue(m_actual_start));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_territories.isSet()) {
        obj.insert(QString("territories"), ::OpenAPI::toJsonValue(m_territories));
    }
    return obj;
}

QDateTime OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::getActualStart() const {
    return m_actual_start;
}
void OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::setActualStart(const QDateTime &actual_start) {
    m_actual_start = actual_start;
    m_actual_start_isSet = true;
}

bool OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::is_actual_start_Set() const{
    return m_actual_start_isSet;
}

bool OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::is_actual_start_Valid() const{
    return m_actual_start_isValid;
}

QString OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::getName() const {
    return m_name;
}
void OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::is_name_Valid() const{
    return m_name_isValid;
}

OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner_territories OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::getTerritories() const {
    return m_territories;
}
void OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::setTerritories(const OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner_territories &territories) {
    m_territories = territories;
    m_territories_isSet = true;
}

bool OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::is_territories_Set() const{
    return m_territories_isSet;
}

bool OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::is_territories_Valid() const{
    return m_territories_isValid;
}

bool OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_actual_start_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_territories.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && true;
}

} // namespace OpenAPI
