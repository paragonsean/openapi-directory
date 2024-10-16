/**
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHeaderConstraint.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHeaderConstraint::OAIHeaderConstraint(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHeaderConstraint::OAIHeaderConstraint() {
    this->initializeModel();
}

OAIHeaderConstraint::~OAIHeaderConstraint() {}

void OAIHeaderConstraint::initializeModel() {

    m_case_sensitive_isSet = false;
    m_case_sensitive_isValid = false;

    m_invert_isSet = false;
    m_invert_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIHeaderConstraint::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHeaderConstraint::fromJsonObject(QJsonObject json) {

    m_case_sensitive_isValid = ::OpenAPI::fromJsonValue(m_case_sensitive, json[QString("case_sensitive")]);
    m_case_sensitive_isSet = !json[QString("case_sensitive")].isNull() && m_case_sensitive_isValid;

    m_invert_isValid = ::OpenAPI::fromJsonValue(m_invert, json[QString("invert")]);
    m_invert_isSet = !json[QString("invert")].isNull() && m_invert_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIHeaderConstraint::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHeaderConstraint::asJsonObject() const {
    QJsonObject obj;
    if (m_case_sensitive_isSet) {
        obj.insert(QString("case_sensitive"), ::OpenAPI::toJsonValue(m_case_sensitive));
    }
    if (m_invert_isSet) {
        obj.insert(QString("invert"), ::OpenAPI::toJsonValue(m_invert));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

bool OAIHeaderConstraint::isCaseSensitive() const {
    return m_case_sensitive;
}
void OAIHeaderConstraint::setCaseSensitive(const bool &case_sensitive) {
    m_case_sensitive = case_sensitive;
    m_case_sensitive_isSet = true;
}

bool OAIHeaderConstraint::is_case_sensitive_Set() const{
    return m_case_sensitive_isSet;
}

bool OAIHeaderConstraint::is_case_sensitive_Valid() const{
    return m_case_sensitive_isValid;
}

bool OAIHeaderConstraint::isInvert() const {
    return m_invert;
}
void OAIHeaderConstraint::setInvert(const bool &invert) {
    m_invert = invert;
    m_invert_isSet = true;
}

bool OAIHeaderConstraint::is_invert_Set() const{
    return m_invert_isSet;
}

bool OAIHeaderConstraint::is_invert_Valid() const{
    return m_invert_isValid;
}

QString OAIHeaderConstraint::getName() const {
    return m_name;
}
void OAIHeaderConstraint::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIHeaderConstraint::is_name_Set() const{
    return m_name_isSet;
}

bool OAIHeaderConstraint::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIHeaderConstraint::getValue() const {
    return m_value;
}
void OAIHeaderConstraint::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIHeaderConstraint::is_value_Set() const{
    return m_value_isSet;
}

bool OAIHeaderConstraint::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIHeaderConstraint::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_case_sensitive_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invert_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHeaderConstraint::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && true;
}

} // namespace OpenAPI
