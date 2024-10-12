/**
 * Azure Alerts Management Service Resource Provider
 * APIs for Azure Smart Detector Alert Rules CRUD operations.
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAlertRule.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAlertRule::OAIAlertRule(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAlertRule::OAIAlertRule() {
    this->initializeModel();
}

OAIAlertRule::~OAIAlertRule() {}

void OAIAlertRule::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIAlertRule::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAlertRule::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIAlertRule::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAlertRule::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAIAlertRuleProperties OAIAlertRule::getProperties() const {
    return m_properties;
}
void OAIAlertRule::setProperties(const OAIAlertRuleProperties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIAlertRule::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIAlertRule::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAIAlertRule::getId() const {
    return m_id;
}
void OAIAlertRule::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAlertRule::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAlertRule::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIAlertRule::getName() const {
    return m_name;
}
void OAIAlertRule::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAlertRule::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAlertRule::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIAlertRule::getType() const {
    return m_type;
}
void OAIAlertRule::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIAlertRule::is_type_Set() const{
    return m_type_isSet;
}

bool OAIAlertRule::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIAlertRule::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAlertRule::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
