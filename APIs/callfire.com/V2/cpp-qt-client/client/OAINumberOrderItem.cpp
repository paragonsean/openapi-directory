/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAINumberOrderItem.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINumberOrderItem::OAINumberOrderItem(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINumberOrderItem::OAINumberOrderItem() {
    this->initializeModel();
}

OAINumberOrderItem::~OAINumberOrderItem() {}

void OAINumberOrderItem::initializeModel() {

    m_fulfilled_isSet = false;
    m_fulfilled_isValid = false;

    m_ordered_isSet = false;
    m_ordered_isValid = false;

    m_unit_cost_isSet = false;
    m_unit_cost_isValid = false;
}

void OAINumberOrderItem::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINumberOrderItem::fromJsonObject(QJsonObject json) {

    m_fulfilled_isValid = ::OpenAPI::fromJsonValue(m_fulfilled, json[QString("fulfilled")]);
    m_fulfilled_isSet = !json[QString("fulfilled")].isNull() && m_fulfilled_isValid;

    m_ordered_isValid = ::OpenAPI::fromJsonValue(m_ordered, json[QString("ordered")]);
    m_ordered_isSet = !json[QString("ordered")].isNull() && m_ordered_isValid;

    m_unit_cost_isValid = ::OpenAPI::fromJsonValue(m_unit_cost, json[QString("unitCost")]);
    m_unit_cost_isSet = !json[QString("unitCost")].isNull() && m_unit_cost_isValid;
}

QString OAINumberOrderItem::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINumberOrderItem::asJsonObject() const {
    QJsonObject obj;
    if (m_fulfilled.size() > 0) {
        obj.insert(QString("fulfilled"), ::OpenAPI::toJsonValue(m_fulfilled));
    }
    if (m_ordered_isSet) {
        obj.insert(QString("ordered"), ::OpenAPI::toJsonValue(m_ordered));
    }
    if (m_unit_cost_isSet) {
        obj.insert(QString("unitCost"), ::OpenAPI::toJsonValue(m_unit_cost));
    }
    return obj;
}

QList<QString> OAINumberOrderItem::getFulfilled() const {
    return m_fulfilled;
}
void OAINumberOrderItem::setFulfilled(const QList<QString> &fulfilled) {
    m_fulfilled = fulfilled;
    m_fulfilled_isSet = true;
}

bool OAINumberOrderItem::is_fulfilled_Set() const{
    return m_fulfilled_isSet;
}

bool OAINumberOrderItem::is_fulfilled_Valid() const{
    return m_fulfilled_isValid;
}

qint32 OAINumberOrderItem::getOrdered() const {
    return m_ordered;
}
void OAINumberOrderItem::setOrdered(const qint32 &ordered) {
    m_ordered = ordered;
    m_ordered_isSet = true;
}

bool OAINumberOrderItem::is_ordered_Set() const{
    return m_ordered_isSet;
}

bool OAINumberOrderItem::is_ordered_Valid() const{
    return m_ordered_isValid;
}

float OAINumberOrderItem::getUnitCost() const {
    return m_unit_cost;
}
void OAINumberOrderItem::setUnitCost(const float &unit_cost) {
    m_unit_cost = unit_cost;
    m_unit_cost_isSet = true;
}

bool OAINumberOrderItem::is_unit_cost_Set() const{
    return m_unit_cost_isSet;
}

bool OAINumberOrderItem::is_unit_cost_Valid() const{
    return m_unit_cost_isValid;
}

bool OAINumberOrderItem::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_fulfilled.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_ordered_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_cost_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINumberOrderItem::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
