/**
 * TSAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIParentRef.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIParentRef::OAIParentRef(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIParentRef::OAIParentRef() {
    this->initializeModel();
}

OAIParentRef::~OAIParentRef() {}

void OAIParentRef::initializeModel() {

    m_parent_value_ident_isSet = false;
    m_parent_value_ident_isValid = false;

    m_parent_variable_ident_isSet = false;
    m_parent_variable_ident_isValid = false;
}

void OAIParentRef::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIParentRef::fromJsonObject(QJsonObject json) {

    m_parent_value_ident_isValid = ::OpenAPI::fromJsonValue(m_parent_value_ident, json[QString("parentValueIdent")]);
    m_parent_value_ident_isSet = !json[QString("parentValueIdent")].isNull() && m_parent_value_ident_isValid;

    m_parent_variable_ident_isValid = ::OpenAPI::fromJsonValue(m_parent_variable_ident, json[QString("parentVariableIdent")]);
    m_parent_variable_ident_isSet = !json[QString("parentVariableIdent")].isNull() && m_parent_variable_ident_isValid;
}

QString OAIParentRef::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIParentRef::asJsonObject() const {
    QJsonObject obj;
    if (m_parent_value_ident_isSet) {
        obj.insert(QString("parentValueIdent"), ::OpenAPI::toJsonValue(m_parent_value_ident));
    }
    if (m_parent_variable_ident_isSet) {
        obj.insert(QString("parentVariableIdent"), ::OpenAPI::toJsonValue(m_parent_variable_ident));
    }
    return obj;
}

QString OAIParentRef::getParentValueIdent() const {
    return m_parent_value_ident;
}
void OAIParentRef::setParentValueIdent(const QString &parent_value_ident) {
    m_parent_value_ident = parent_value_ident;
    m_parent_value_ident_isSet = true;
}

bool OAIParentRef::is_parent_value_ident_Set() const{
    return m_parent_value_ident_isSet;
}

bool OAIParentRef::is_parent_value_ident_Valid() const{
    return m_parent_value_ident_isValid;
}

QString OAIParentRef::getParentVariableIdent() const {
    return m_parent_variable_ident;
}
void OAIParentRef::setParentVariableIdent(const QString &parent_variable_ident) {
    m_parent_variable_ident = parent_variable_ident;
    m_parent_variable_ident_isSet = true;
}

bool OAIParentRef::is_parent_variable_ident_Set() const{
    return m_parent_variable_ident_isSet;
}

bool OAIParentRef::is_parent_variable_ident_Valid() const{
    return m_parent_variable_ident_isValid;
}

bool OAIParentRef::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_parent_value_ident_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_variable_ident_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIParentRef::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
