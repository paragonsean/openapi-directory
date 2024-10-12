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

#include "OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request::OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request::OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request() {
    this->initializeModel();
}

OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request::~OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request() {}

void OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request::initializeModel() {

    m_stock_item_isSet = false;
    m_stock_item_isValid = false;
}

void OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request::fromJsonObject(QJsonObject json) {

    m_stock_item_isValid = ::OpenAPI::fromJsonValue(m_stock_item, json[QString("stockItem")]);
    m_stock_item_isSet = !json[QString("stockItem")].isNull() && m_stock_item_isValid;
}

QString OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request::asJsonObject() const {
    QJsonObject obj;
    if (m_stock_item.isSet()) {
        obj.insert(QString("stockItem"), ::OpenAPI::toJsonValue(m_stock_item));
    }
    return obj;
}

OAICatalog_inventory_data_stock_item_interface OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request::getStockItem() const {
    return m_stock_item;
}
void OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request::setStockItem(const OAICatalog_inventory_data_stock_item_interface &stock_item) {
    m_stock_item = stock_item;
    m_stock_item_isSet = true;
}

bool OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request::is_stock_item_Set() const{
    return m_stock_item_isSet;
}

bool OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request::is_stock_item_Valid() const{
    return m_stock_item_isValid;
}

bool OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_stock_item.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICatalogInventoryStockRegistryV1UpdateStockItemBySkuPut_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_stock_item_isValid && true;
}

} // namespace OpenAPI
