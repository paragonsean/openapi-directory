/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIValueDescriptionPair_Currency.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIValueDescriptionPair_Currency::OAIIValueDescriptionPair_Currency(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIValueDescriptionPair_Currency::OAIIValueDescriptionPair_Currency() {
    this->initializeModel();
}

OAIIValueDescriptionPair_Currency::~OAIIValueDescriptionPair_Currency() {}

void OAIIValueDescriptionPair_Currency::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIIValueDescriptionPair_Currency::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIValueDescriptionPair_Currency::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIIValueDescriptionPair_Currency::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIValueDescriptionPair_Currency::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_value.isSet()) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIIValueDescriptionPair_Currency::getDescription() const {
    return m_description;
}
void OAIIValueDescriptionPair_Currency::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIIValueDescriptionPair_Currency::is_description_Set() const{
    return m_description_isSet;
}

bool OAIIValueDescriptionPair_Currency::is_description_Valid() const{
    return m_description_isValid;
}

OAICurrency OAIIValueDescriptionPair_Currency::getValue() const {
    return m_value;
}
void OAIIValueDescriptionPair_Currency::setValue(const OAICurrency &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIIValueDescriptionPair_Currency::is_value_Set() const{
    return m_value_isSet;
}

bool OAIIValueDescriptionPair_Currency::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIIValueDescriptionPair_Currency::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIValueDescriptionPair_Currency::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
