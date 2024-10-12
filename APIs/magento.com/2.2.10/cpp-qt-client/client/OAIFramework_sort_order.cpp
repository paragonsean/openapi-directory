/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFramework_sort_order.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFramework_sort_order::OAIFramework_sort_order(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFramework_sort_order::OAIFramework_sort_order() {
    this->initializeModel();
}

OAIFramework_sort_order::~OAIFramework_sort_order() {}

void OAIFramework_sort_order::initializeModel() {

    m_direction_isSet = false;
    m_direction_isValid = false;

    m_field_isSet = false;
    m_field_isValid = false;
}

void OAIFramework_sort_order::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFramework_sort_order::fromJsonObject(QJsonObject json) {

    m_direction_isValid = ::OpenAPI::fromJsonValue(m_direction, json[QString("direction")]);
    m_direction_isSet = !json[QString("direction")].isNull() && m_direction_isValid;

    m_field_isValid = ::OpenAPI::fromJsonValue(m_field, json[QString("field")]);
    m_field_isSet = !json[QString("field")].isNull() && m_field_isValid;
}

QString OAIFramework_sort_order::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFramework_sort_order::asJsonObject() const {
    QJsonObject obj;
    if (m_direction_isSet) {
        obj.insert(QString("direction"), ::OpenAPI::toJsonValue(m_direction));
    }
    if (m_field_isSet) {
        obj.insert(QString("field"), ::OpenAPI::toJsonValue(m_field));
    }
    return obj;
}

QString OAIFramework_sort_order::getDirection() const {
    return m_direction;
}
void OAIFramework_sort_order::setDirection(const QString &direction) {
    m_direction = direction;
    m_direction_isSet = true;
}

bool OAIFramework_sort_order::is_direction_Set() const{
    return m_direction_isSet;
}

bool OAIFramework_sort_order::is_direction_Valid() const{
    return m_direction_isValid;
}

QString OAIFramework_sort_order::getField() const {
    return m_field;
}
void OAIFramework_sort_order::setField(const QString &field) {
    m_field = field;
    m_field_isSet = true;
}

bool OAIFramework_sort_order::is_field_Set() const{
    return m_field_isSet;
}

bool OAIFramework_sort_order::is_field_Valid() const{
    return m_field_isValid;
}

bool OAIFramework_sort_order::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_direction_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_field_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFramework_sort_order::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_direction_isValid && m_field_isValid && true;
}

} // namespace OpenAPI
