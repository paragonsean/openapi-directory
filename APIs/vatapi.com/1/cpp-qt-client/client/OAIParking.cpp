/**
 * VAT API
 * A developer friendly API to help your business achieve VAT compliance
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIParking.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIParking::OAIParking(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIParking::OAIParking() {
    this->initializeModel();
}

OAIParking::~OAIParking() {}

void OAIParking::initializeModel() {

    m_applies_to_isSet = false;
    m_applies_to_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIParking::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIParking::fromJsonObject(QJsonObject json) {

    m_applies_to_isValid = ::OpenAPI::fromJsonValue(m_applies_to, json[QString("applies_to")]);
    m_applies_to_isSet = !json[QString("applies_to")].isNull() && m_applies_to_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIParking::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIParking::asJsonObject() const {
    QJsonObject obj;
    if (m_applies_to_isSet) {
        obj.insert(QString("applies_to"), ::OpenAPI::toJsonValue(m_applies_to));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIParking::getAppliesTo() const {
    return m_applies_to;
}
void OAIParking::setAppliesTo(const QString &applies_to) {
    m_applies_to = applies_to;
    m_applies_to_isSet = true;
}

bool OAIParking::is_applies_to_Set() const{
    return m_applies_to_isSet;
}

bool OAIParking::is_applies_to_Valid() const{
    return m_applies_to_isValid;
}

qint32 OAIParking::getValue() const {
    return m_value;
}
void OAIParking::setValue(const qint32 &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIParking::is_value_Set() const{
    return m_value_isSet;
}

bool OAIParking::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIParking::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_applies_to_isSet) {
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

bool OAIParking::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_applies_to_isValid && m_value_isValid && true;
}

} // namespace OpenAPI
