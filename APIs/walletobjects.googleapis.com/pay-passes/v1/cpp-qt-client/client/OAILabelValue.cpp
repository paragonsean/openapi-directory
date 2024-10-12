/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILabelValue.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILabelValue::OAILabelValue(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILabelValue::OAILabelValue() {
    this->initializeModel();
}

OAILabelValue::~OAILabelValue() {}

void OAILabelValue::initializeModel() {

    m_label_isSet = false;
    m_label_isValid = false;

    m_localized_label_isSet = false;
    m_localized_label_isValid = false;

    m_localized_value_isSet = false;
    m_localized_value_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAILabelValue::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILabelValue::fromJsonObject(QJsonObject json) {

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;

    m_localized_label_isValid = ::OpenAPI::fromJsonValue(m_localized_label, json[QString("localizedLabel")]);
    m_localized_label_isSet = !json[QString("localizedLabel")].isNull() && m_localized_label_isValid;

    m_localized_value_isValid = ::OpenAPI::fromJsonValue(m_localized_value, json[QString("localizedValue")]);
    m_localized_value_isSet = !json[QString("localizedValue")].isNull() && m_localized_value_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAILabelValue::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILabelValue::asJsonObject() const {
    QJsonObject obj;
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    if (m_localized_label.isSet()) {
        obj.insert(QString("localizedLabel"), ::OpenAPI::toJsonValue(m_localized_label));
    }
    if (m_localized_value.isSet()) {
        obj.insert(QString("localizedValue"), ::OpenAPI::toJsonValue(m_localized_value));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAILabelValue::getLabel() const {
    return m_label;
}
void OAILabelValue::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAILabelValue::is_label_Set() const{
    return m_label_isSet;
}

bool OAILabelValue::is_label_Valid() const{
    return m_label_isValid;
}

OAILocalizedString OAILabelValue::getLocalizedLabel() const {
    return m_localized_label;
}
void OAILabelValue::setLocalizedLabel(const OAILocalizedString &localized_label) {
    m_localized_label = localized_label;
    m_localized_label_isSet = true;
}

bool OAILabelValue::is_localized_label_Set() const{
    return m_localized_label_isSet;
}

bool OAILabelValue::is_localized_label_Valid() const{
    return m_localized_label_isValid;
}

OAILocalizedString OAILabelValue::getLocalizedValue() const {
    return m_localized_value;
}
void OAILabelValue::setLocalizedValue(const OAILocalizedString &localized_value) {
    m_localized_value = localized_value;
    m_localized_value_isSet = true;
}

bool OAILabelValue::is_localized_value_Set() const{
    return m_localized_value_isSet;
}

bool OAILabelValue::is_localized_value_Valid() const{
    return m_localized_value_isValid;
}

QString OAILabelValue::getValue() const {
    return m_value;
}
void OAILabelValue::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAILabelValue::is_value_Set() const{
    return m_value_isSet;
}

bool OAILabelValue::is_value_Valid() const{
    return m_value_isValid;
}

bool OAILabelValue::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_localized_label.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_localized_value.isSet()) {
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

bool OAILabelValue::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
