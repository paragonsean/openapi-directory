/**
 * Airport Nearest Relevant
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, this API in test only returns a few selected cities. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.1.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDistance.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDistance::OAIDistance(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDistance::OAIDistance() {
    this->initializeModel();
}

OAIDistance::~OAIDistance() {}

void OAIDistance::initializeModel() {

    m_unit_isSet = false;
    m_unit_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIDistance::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDistance::fromJsonObject(QJsonObject json) {

    m_unit_isValid = ::OpenAPI::fromJsonValue(m_unit, json[QString("unit")]);
    m_unit_isSet = !json[QString("unit")].isNull() && m_unit_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIDistance::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDistance::asJsonObject() const {
    QJsonObject obj;
    if (m_unit_isSet) {
        obj.insert(QString("unit"), ::OpenAPI::toJsonValue(m_unit));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIDistance::getUnit() const {
    return m_unit;
}
void OAIDistance::setUnit(const QString &unit) {
    m_unit = unit;
    m_unit_isSet = true;
}

bool OAIDistance::is_unit_Set() const{
    return m_unit_isSet;
}

bool OAIDistance::is_unit_Valid() const{
    return m_unit_isValid;
}

qint32 OAIDistance::getValue() const {
    return m_value;
}
void OAIDistance::setValue(const qint32 &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIDistance::is_value_Set() const{
    return m_value_isSet;
}

bool OAIDistance::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIDistance::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_unit_isSet) {
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

bool OAIDistance::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
