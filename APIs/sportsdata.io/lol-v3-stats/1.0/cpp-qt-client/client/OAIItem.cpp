/**
 * LoL v3 Stats
 * LoL v3 Stats
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIItem.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIItem::OAIItem(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIItem::OAIItem() {
    this->initializeModel();
}

OAIItem::~OAIItem() {}

void OAIItem::initializeModel() {

    m_gold_base_isSet = false;
    m_gold_base_isValid = false;

    m_gold_sell_isSet = false;
    m_gold_sell_isValid = false;

    m_gold_total_isSet = false;
    m_gold_total_isValid = false;

    m_item_id_isSet = false;
    m_item_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIItem::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIItem::fromJsonObject(QJsonObject json) {

    m_gold_base_isValid = ::OpenAPI::fromJsonValue(m_gold_base, json[QString("GoldBase")]);
    m_gold_base_isSet = !json[QString("GoldBase")].isNull() && m_gold_base_isValid;

    m_gold_sell_isValid = ::OpenAPI::fromJsonValue(m_gold_sell, json[QString("GoldSell")]);
    m_gold_sell_isSet = !json[QString("GoldSell")].isNull() && m_gold_sell_isValid;

    m_gold_total_isValid = ::OpenAPI::fromJsonValue(m_gold_total, json[QString("GoldTotal")]);
    m_gold_total_isSet = !json[QString("GoldTotal")].isNull() && m_gold_total_isValid;

    m_item_id_isValid = ::OpenAPI::fromJsonValue(m_item_id, json[QString("ItemId")]);
    m_item_id_isSet = !json[QString("ItemId")].isNull() && m_item_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;
}

QString OAIItem::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIItem::asJsonObject() const {
    QJsonObject obj;
    if (m_gold_base_isSet) {
        obj.insert(QString("GoldBase"), ::OpenAPI::toJsonValue(m_gold_base));
    }
    if (m_gold_sell_isSet) {
        obj.insert(QString("GoldSell"), ::OpenAPI::toJsonValue(m_gold_sell));
    }
    if (m_gold_total_isSet) {
        obj.insert(QString("GoldTotal"), ::OpenAPI::toJsonValue(m_gold_total));
    }
    if (m_item_id_isSet) {
        obj.insert(QString("ItemId"), ::OpenAPI::toJsonValue(m_item_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

qint32 OAIItem::getGoldBase() const {
    return m_gold_base;
}
void OAIItem::setGoldBase(const qint32 &gold_base) {
    m_gold_base = gold_base;
    m_gold_base_isSet = true;
}

bool OAIItem::is_gold_base_Set() const{
    return m_gold_base_isSet;
}

bool OAIItem::is_gold_base_Valid() const{
    return m_gold_base_isValid;
}

qint32 OAIItem::getGoldSell() const {
    return m_gold_sell;
}
void OAIItem::setGoldSell(const qint32 &gold_sell) {
    m_gold_sell = gold_sell;
    m_gold_sell_isSet = true;
}

bool OAIItem::is_gold_sell_Set() const{
    return m_gold_sell_isSet;
}

bool OAIItem::is_gold_sell_Valid() const{
    return m_gold_sell_isValid;
}

qint32 OAIItem::getGoldTotal() const {
    return m_gold_total;
}
void OAIItem::setGoldTotal(const qint32 &gold_total) {
    m_gold_total = gold_total;
    m_gold_total_isSet = true;
}

bool OAIItem::is_gold_total_Set() const{
    return m_gold_total_isSet;
}

bool OAIItem::is_gold_total_Valid() const{
    return m_gold_total_isValid;
}

qint32 OAIItem::getItemId() const {
    return m_item_id;
}
void OAIItem::setItemId(const qint32 &item_id) {
    m_item_id = item_id;
    m_item_id_isSet = true;
}

bool OAIItem::is_item_id_Set() const{
    return m_item_id_isSet;
}

bool OAIItem::is_item_id_Valid() const{
    return m_item_id_isValid;
}

QString OAIItem::getName() const {
    return m_name;
}
void OAIItem::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIItem::is_name_Set() const{
    return m_name_isSet;
}

bool OAIItem::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIItem::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_gold_base_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gold_sell_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gold_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_item_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIItem::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
