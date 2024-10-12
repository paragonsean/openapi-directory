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

#include "OAISales_data_creditmemo_item_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISales_data_creditmemo_item_interface::OAISales_data_creditmemo_item_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISales_data_creditmemo_item_interface::OAISales_data_creditmemo_item_interface() {
    this->initializeModel();
}

OAISales_data_creditmemo_item_interface::~OAISales_data_creditmemo_item_interface() {}

void OAISales_data_creditmemo_item_interface::initializeModel() {

    m_additional_data_isSet = false;
    m_additional_data_isValid = false;

    m_base_cost_isSet = false;
    m_base_cost_isValid = false;

    m_base_discount_amount_isSet = false;
    m_base_discount_amount_isValid = false;

    m_base_discount_tax_compensation_amount_isSet = false;
    m_base_discount_tax_compensation_amount_isValid = false;

    m_base_price_isSet = false;
    m_base_price_isValid = false;

    m_base_price_incl_tax_isSet = false;
    m_base_price_incl_tax_isValid = false;

    m_base_row_total_isSet = false;
    m_base_row_total_isValid = false;

    m_base_row_total_incl_tax_isSet = false;
    m_base_row_total_incl_tax_isValid = false;

    m_base_tax_amount_isSet = false;
    m_base_tax_amount_isValid = false;

    m_base_weee_tax_applied_amount_isSet = false;
    m_base_weee_tax_applied_amount_isValid = false;

    m_base_weee_tax_applied_row_amnt_isSet = false;
    m_base_weee_tax_applied_row_amnt_isValid = false;

    m_base_weee_tax_disposition_isSet = false;
    m_base_weee_tax_disposition_isValid = false;

    m_base_weee_tax_row_disposition_isSet = false;
    m_base_weee_tax_row_disposition_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_discount_amount_isSet = false;
    m_discount_amount_isValid = false;

    m_discount_tax_compensation_amount_isSet = false;
    m_discount_tax_compensation_amount_isValid = false;

    m_entity_id_isSet = false;
    m_entity_id_isValid = false;

    m_extension_attributes_isSet = false;
    m_extension_attributes_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_order_item_id_isSet = false;
    m_order_item_id_isValid = false;

    m_parent_id_isSet = false;
    m_parent_id_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_price_incl_tax_isSet = false;
    m_price_incl_tax_isValid = false;

    m_product_id_isSet = false;
    m_product_id_isValid = false;

    m_qty_isSet = false;
    m_qty_isValid = false;

    m_row_total_isSet = false;
    m_row_total_isValid = false;

    m_row_total_incl_tax_isSet = false;
    m_row_total_incl_tax_isValid = false;

    m_sku_isSet = false;
    m_sku_isValid = false;

    m_tax_amount_isSet = false;
    m_tax_amount_isValid = false;

    m_weee_tax_applied_isSet = false;
    m_weee_tax_applied_isValid = false;

    m_weee_tax_applied_amount_isSet = false;
    m_weee_tax_applied_amount_isValid = false;

    m_weee_tax_applied_row_amount_isSet = false;
    m_weee_tax_applied_row_amount_isValid = false;

    m_weee_tax_disposition_isSet = false;
    m_weee_tax_disposition_isValid = false;

    m_weee_tax_row_disposition_isSet = false;
    m_weee_tax_row_disposition_isValid = false;
}

void OAISales_data_creditmemo_item_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISales_data_creditmemo_item_interface::fromJsonObject(QJsonObject json) {

    m_additional_data_isValid = ::OpenAPI::fromJsonValue(m_additional_data, json[QString("additional_data")]);
    m_additional_data_isSet = !json[QString("additional_data")].isNull() && m_additional_data_isValid;

    m_base_cost_isValid = ::OpenAPI::fromJsonValue(m_base_cost, json[QString("base_cost")]);
    m_base_cost_isSet = !json[QString("base_cost")].isNull() && m_base_cost_isValid;

    m_base_discount_amount_isValid = ::OpenAPI::fromJsonValue(m_base_discount_amount, json[QString("base_discount_amount")]);
    m_base_discount_amount_isSet = !json[QString("base_discount_amount")].isNull() && m_base_discount_amount_isValid;

    m_base_discount_tax_compensation_amount_isValid = ::OpenAPI::fromJsonValue(m_base_discount_tax_compensation_amount, json[QString("base_discount_tax_compensation_amount")]);
    m_base_discount_tax_compensation_amount_isSet = !json[QString("base_discount_tax_compensation_amount")].isNull() && m_base_discount_tax_compensation_amount_isValid;

    m_base_price_isValid = ::OpenAPI::fromJsonValue(m_base_price, json[QString("base_price")]);
    m_base_price_isSet = !json[QString("base_price")].isNull() && m_base_price_isValid;

    m_base_price_incl_tax_isValid = ::OpenAPI::fromJsonValue(m_base_price_incl_tax, json[QString("base_price_incl_tax")]);
    m_base_price_incl_tax_isSet = !json[QString("base_price_incl_tax")].isNull() && m_base_price_incl_tax_isValid;

    m_base_row_total_isValid = ::OpenAPI::fromJsonValue(m_base_row_total, json[QString("base_row_total")]);
    m_base_row_total_isSet = !json[QString("base_row_total")].isNull() && m_base_row_total_isValid;

    m_base_row_total_incl_tax_isValid = ::OpenAPI::fromJsonValue(m_base_row_total_incl_tax, json[QString("base_row_total_incl_tax")]);
    m_base_row_total_incl_tax_isSet = !json[QString("base_row_total_incl_tax")].isNull() && m_base_row_total_incl_tax_isValid;

    m_base_tax_amount_isValid = ::OpenAPI::fromJsonValue(m_base_tax_amount, json[QString("base_tax_amount")]);
    m_base_tax_amount_isSet = !json[QString("base_tax_amount")].isNull() && m_base_tax_amount_isValid;

    m_base_weee_tax_applied_amount_isValid = ::OpenAPI::fromJsonValue(m_base_weee_tax_applied_amount, json[QString("base_weee_tax_applied_amount")]);
    m_base_weee_tax_applied_amount_isSet = !json[QString("base_weee_tax_applied_amount")].isNull() && m_base_weee_tax_applied_amount_isValid;

    m_base_weee_tax_applied_row_amnt_isValid = ::OpenAPI::fromJsonValue(m_base_weee_tax_applied_row_amnt, json[QString("base_weee_tax_applied_row_amnt")]);
    m_base_weee_tax_applied_row_amnt_isSet = !json[QString("base_weee_tax_applied_row_amnt")].isNull() && m_base_weee_tax_applied_row_amnt_isValid;

    m_base_weee_tax_disposition_isValid = ::OpenAPI::fromJsonValue(m_base_weee_tax_disposition, json[QString("base_weee_tax_disposition")]);
    m_base_weee_tax_disposition_isSet = !json[QString("base_weee_tax_disposition")].isNull() && m_base_weee_tax_disposition_isValid;

    m_base_weee_tax_row_disposition_isValid = ::OpenAPI::fromJsonValue(m_base_weee_tax_row_disposition, json[QString("base_weee_tax_row_disposition")]);
    m_base_weee_tax_row_disposition_isSet = !json[QString("base_weee_tax_row_disposition")].isNull() && m_base_weee_tax_row_disposition_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_discount_amount_isValid = ::OpenAPI::fromJsonValue(m_discount_amount, json[QString("discount_amount")]);
    m_discount_amount_isSet = !json[QString("discount_amount")].isNull() && m_discount_amount_isValid;

    m_discount_tax_compensation_amount_isValid = ::OpenAPI::fromJsonValue(m_discount_tax_compensation_amount, json[QString("discount_tax_compensation_amount")]);
    m_discount_tax_compensation_amount_isSet = !json[QString("discount_tax_compensation_amount")].isNull() && m_discount_tax_compensation_amount_isValid;

    m_entity_id_isValid = ::OpenAPI::fromJsonValue(m_entity_id, json[QString("entity_id")]);
    m_entity_id_isSet = !json[QString("entity_id")].isNull() && m_entity_id_isValid;

    m_extension_attributes_isValid = ::OpenAPI::fromJsonValue(m_extension_attributes, json[QString("extension_attributes")]);
    m_extension_attributes_isSet = !json[QString("extension_attributes")].isNull() && m_extension_attributes_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_order_item_id_isValid = ::OpenAPI::fromJsonValue(m_order_item_id, json[QString("order_item_id")]);
    m_order_item_id_isSet = !json[QString("order_item_id")].isNull() && m_order_item_id_isValid;

    m_parent_id_isValid = ::OpenAPI::fromJsonValue(m_parent_id, json[QString("parent_id")]);
    m_parent_id_isSet = !json[QString("parent_id")].isNull() && m_parent_id_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_price_incl_tax_isValid = ::OpenAPI::fromJsonValue(m_price_incl_tax, json[QString("price_incl_tax")]);
    m_price_incl_tax_isSet = !json[QString("price_incl_tax")].isNull() && m_price_incl_tax_isValid;

    m_product_id_isValid = ::OpenAPI::fromJsonValue(m_product_id, json[QString("product_id")]);
    m_product_id_isSet = !json[QString("product_id")].isNull() && m_product_id_isValid;

    m_qty_isValid = ::OpenAPI::fromJsonValue(m_qty, json[QString("qty")]);
    m_qty_isSet = !json[QString("qty")].isNull() && m_qty_isValid;

    m_row_total_isValid = ::OpenAPI::fromJsonValue(m_row_total, json[QString("row_total")]);
    m_row_total_isSet = !json[QString("row_total")].isNull() && m_row_total_isValid;

    m_row_total_incl_tax_isValid = ::OpenAPI::fromJsonValue(m_row_total_incl_tax, json[QString("row_total_incl_tax")]);
    m_row_total_incl_tax_isSet = !json[QString("row_total_incl_tax")].isNull() && m_row_total_incl_tax_isValid;

    m_sku_isValid = ::OpenAPI::fromJsonValue(m_sku, json[QString("sku")]);
    m_sku_isSet = !json[QString("sku")].isNull() && m_sku_isValid;

    m_tax_amount_isValid = ::OpenAPI::fromJsonValue(m_tax_amount, json[QString("tax_amount")]);
    m_tax_amount_isSet = !json[QString("tax_amount")].isNull() && m_tax_amount_isValid;

    m_weee_tax_applied_isValid = ::OpenAPI::fromJsonValue(m_weee_tax_applied, json[QString("weee_tax_applied")]);
    m_weee_tax_applied_isSet = !json[QString("weee_tax_applied")].isNull() && m_weee_tax_applied_isValid;

    m_weee_tax_applied_amount_isValid = ::OpenAPI::fromJsonValue(m_weee_tax_applied_amount, json[QString("weee_tax_applied_amount")]);
    m_weee_tax_applied_amount_isSet = !json[QString("weee_tax_applied_amount")].isNull() && m_weee_tax_applied_amount_isValid;

    m_weee_tax_applied_row_amount_isValid = ::OpenAPI::fromJsonValue(m_weee_tax_applied_row_amount, json[QString("weee_tax_applied_row_amount")]);
    m_weee_tax_applied_row_amount_isSet = !json[QString("weee_tax_applied_row_amount")].isNull() && m_weee_tax_applied_row_amount_isValid;

    m_weee_tax_disposition_isValid = ::OpenAPI::fromJsonValue(m_weee_tax_disposition, json[QString("weee_tax_disposition")]);
    m_weee_tax_disposition_isSet = !json[QString("weee_tax_disposition")].isNull() && m_weee_tax_disposition_isValid;

    m_weee_tax_row_disposition_isValid = ::OpenAPI::fromJsonValue(m_weee_tax_row_disposition, json[QString("weee_tax_row_disposition")]);
    m_weee_tax_row_disposition_isSet = !json[QString("weee_tax_row_disposition")].isNull() && m_weee_tax_row_disposition_isValid;
}

QString OAISales_data_creditmemo_item_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISales_data_creditmemo_item_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_data_isSet) {
        obj.insert(QString("additional_data"), ::OpenAPI::toJsonValue(m_additional_data));
    }
    if (m_base_cost_isSet) {
        obj.insert(QString("base_cost"), ::OpenAPI::toJsonValue(m_base_cost));
    }
    if (m_base_discount_amount_isSet) {
        obj.insert(QString("base_discount_amount"), ::OpenAPI::toJsonValue(m_base_discount_amount));
    }
    if (m_base_discount_tax_compensation_amount_isSet) {
        obj.insert(QString("base_discount_tax_compensation_amount"), ::OpenAPI::toJsonValue(m_base_discount_tax_compensation_amount));
    }
    if (m_base_price_isSet) {
        obj.insert(QString("base_price"), ::OpenAPI::toJsonValue(m_base_price));
    }
    if (m_base_price_incl_tax_isSet) {
        obj.insert(QString("base_price_incl_tax"), ::OpenAPI::toJsonValue(m_base_price_incl_tax));
    }
    if (m_base_row_total_isSet) {
        obj.insert(QString("base_row_total"), ::OpenAPI::toJsonValue(m_base_row_total));
    }
    if (m_base_row_total_incl_tax_isSet) {
        obj.insert(QString("base_row_total_incl_tax"), ::OpenAPI::toJsonValue(m_base_row_total_incl_tax));
    }
    if (m_base_tax_amount_isSet) {
        obj.insert(QString("base_tax_amount"), ::OpenAPI::toJsonValue(m_base_tax_amount));
    }
    if (m_base_weee_tax_applied_amount_isSet) {
        obj.insert(QString("base_weee_tax_applied_amount"), ::OpenAPI::toJsonValue(m_base_weee_tax_applied_amount));
    }
    if (m_base_weee_tax_applied_row_amnt_isSet) {
        obj.insert(QString("base_weee_tax_applied_row_amnt"), ::OpenAPI::toJsonValue(m_base_weee_tax_applied_row_amnt));
    }
    if (m_base_weee_tax_disposition_isSet) {
        obj.insert(QString("base_weee_tax_disposition"), ::OpenAPI::toJsonValue(m_base_weee_tax_disposition));
    }
    if (m_base_weee_tax_row_disposition_isSet) {
        obj.insert(QString("base_weee_tax_row_disposition"), ::OpenAPI::toJsonValue(m_base_weee_tax_row_disposition));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_discount_amount_isSet) {
        obj.insert(QString("discount_amount"), ::OpenAPI::toJsonValue(m_discount_amount));
    }
    if (m_discount_tax_compensation_amount_isSet) {
        obj.insert(QString("discount_tax_compensation_amount"), ::OpenAPI::toJsonValue(m_discount_tax_compensation_amount));
    }
    if (m_entity_id_isSet) {
        obj.insert(QString("entity_id"), ::OpenAPI::toJsonValue(m_entity_id));
    }
    if (m_extension_attributes.isSet()) {
        obj.insert(QString("extension_attributes"), ::OpenAPI::toJsonValue(m_extension_attributes));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_order_item_id_isSet) {
        obj.insert(QString("order_item_id"), ::OpenAPI::toJsonValue(m_order_item_id));
    }
    if (m_parent_id_isSet) {
        obj.insert(QString("parent_id"), ::OpenAPI::toJsonValue(m_parent_id));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_price_incl_tax_isSet) {
        obj.insert(QString("price_incl_tax"), ::OpenAPI::toJsonValue(m_price_incl_tax));
    }
    if (m_product_id_isSet) {
        obj.insert(QString("product_id"), ::OpenAPI::toJsonValue(m_product_id));
    }
    if (m_qty_isSet) {
        obj.insert(QString("qty"), ::OpenAPI::toJsonValue(m_qty));
    }
    if (m_row_total_isSet) {
        obj.insert(QString("row_total"), ::OpenAPI::toJsonValue(m_row_total));
    }
    if (m_row_total_incl_tax_isSet) {
        obj.insert(QString("row_total_incl_tax"), ::OpenAPI::toJsonValue(m_row_total_incl_tax));
    }
    if (m_sku_isSet) {
        obj.insert(QString("sku"), ::OpenAPI::toJsonValue(m_sku));
    }
    if (m_tax_amount_isSet) {
        obj.insert(QString("tax_amount"), ::OpenAPI::toJsonValue(m_tax_amount));
    }
    if (m_weee_tax_applied_isSet) {
        obj.insert(QString("weee_tax_applied"), ::OpenAPI::toJsonValue(m_weee_tax_applied));
    }
    if (m_weee_tax_applied_amount_isSet) {
        obj.insert(QString("weee_tax_applied_amount"), ::OpenAPI::toJsonValue(m_weee_tax_applied_amount));
    }
    if (m_weee_tax_applied_row_amount_isSet) {
        obj.insert(QString("weee_tax_applied_row_amount"), ::OpenAPI::toJsonValue(m_weee_tax_applied_row_amount));
    }
    if (m_weee_tax_disposition_isSet) {
        obj.insert(QString("weee_tax_disposition"), ::OpenAPI::toJsonValue(m_weee_tax_disposition));
    }
    if (m_weee_tax_row_disposition_isSet) {
        obj.insert(QString("weee_tax_row_disposition"), ::OpenAPI::toJsonValue(m_weee_tax_row_disposition));
    }
    return obj;
}

QString OAISales_data_creditmemo_item_interface::getAdditionalData() const {
    return m_additional_data;
}
void OAISales_data_creditmemo_item_interface::setAdditionalData(const QString &additional_data) {
    m_additional_data = additional_data;
    m_additional_data_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_additional_data_Set() const{
    return m_additional_data_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_additional_data_Valid() const{
    return m_additional_data_isValid;
}

double OAISales_data_creditmemo_item_interface::getBaseCost() const {
    return m_base_cost;
}
void OAISales_data_creditmemo_item_interface::setBaseCost(const double &base_cost) {
    m_base_cost = base_cost;
    m_base_cost_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_base_cost_Set() const{
    return m_base_cost_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_base_cost_Valid() const{
    return m_base_cost_isValid;
}

double OAISales_data_creditmemo_item_interface::getBaseDiscountAmount() const {
    return m_base_discount_amount;
}
void OAISales_data_creditmemo_item_interface::setBaseDiscountAmount(const double &base_discount_amount) {
    m_base_discount_amount = base_discount_amount;
    m_base_discount_amount_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_base_discount_amount_Set() const{
    return m_base_discount_amount_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_base_discount_amount_Valid() const{
    return m_base_discount_amount_isValid;
}

double OAISales_data_creditmemo_item_interface::getBaseDiscountTaxCompensationAmount() const {
    return m_base_discount_tax_compensation_amount;
}
void OAISales_data_creditmemo_item_interface::setBaseDiscountTaxCompensationAmount(const double &base_discount_tax_compensation_amount) {
    m_base_discount_tax_compensation_amount = base_discount_tax_compensation_amount;
    m_base_discount_tax_compensation_amount_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_base_discount_tax_compensation_amount_Set() const{
    return m_base_discount_tax_compensation_amount_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_base_discount_tax_compensation_amount_Valid() const{
    return m_base_discount_tax_compensation_amount_isValid;
}

double OAISales_data_creditmemo_item_interface::getBasePrice() const {
    return m_base_price;
}
void OAISales_data_creditmemo_item_interface::setBasePrice(const double &base_price) {
    m_base_price = base_price;
    m_base_price_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_base_price_Set() const{
    return m_base_price_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_base_price_Valid() const{
    return m_base_price_isValid;
}

double OAISales_data_creditmemo_item_interface::getBasePriceInclTax() const {
    return m_base_price_incl_tax;
}
void OAISales_data_creditmemo_item_interface::setBasePriceInclTax(const double &base_price_incl_tax) {
    m_base_price_incl_tax = base_price_incl_tax;
    m_base_price_incl_tax_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_base_price_incl_tax_Set() const{
    return m_base_price_incl_tax_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_base_price_incl_tax_Valid() const{
    return m_base_price_incl_tax_isValid;
}

double OAISales_data_creditmemo_item_interface::getBaseRowTotal() const {
    return m_base_row_total;
}
void OAISales_data_creditmemo_item_interface::setBaseRowTotal(const double &base_row_total) {
    m_base_row_total = base_row_total;
    m_base_row_total_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_base_row_total_Set() const{
    return m_base_row_total_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_base_row_total_Valid() const{
    return m_base_row_total_isValid;
}

double OAISales_data_creditmemo_item_interface::getBaseRowTotalInclTax() const {
    return m_base_row_total_incl_tax;
}
void OAISales_data_creditmemo_item_interface::setBaseRowTotalInclTax(const double &base_row_total_incl_tax) {
    m_base_row_total_incl_tax = base_row_total_incl_tax;
    m_base_row_total_incl_tax_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_base_row_total_incl_tax_Set() const{
    return m_base_row_total_incl_tax_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_base_row_total_incl_tax_Valid() const{
    return m_base_row_total_incl_tax_isValid;
}

double OAISales_data_creditmemo_item_interface::getBaseTaxAmount() const {
    return m_base_tax_amount;
}
void OAISales_data_creditmemo_item_interface::setBaseTaxAmount(const double &base_tax_amount) {
    m_base_tax_amount = base_tax_amount;
    m_base_tax_amount_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_base_tax_amount_Set() const{
    return m_base_tax_amount_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_base_tax_amount_Valid() const{
    return m_base_tax_amount_isValid;
}

double OAISales_data_creditmemo_item_interface::getBaseWeeeTaxAppliedAmount() const {
    return m_base_weee_tax_applied_amount;
}
void OAISales_data_creditmemo_item_interface::setBaseWeeeTaxAppliedAmount(const double &base_weee_tax_applied_amount) {
    m_base_weee_tax_applied_amount = base_weee_tax_applied_amount;
    m_base_weee_tax_applied_amount_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_base_weee_tax_applied_amount_Set() const{
    return m_base_weee_tax_applied_amount_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_base_weee_tax_applied_amount_Valid() const{
    return m_base_weee_tax_applied_amount_isValid;
}

double OAISales_data_creditmemo_item_interface::getBaseWeeeTaxAppliedRowAmnt() const {
    return m_base_weee_tax_applied_row_amnt;
}
void OAISales_data_creditmemo_item_interface::setBaseWeeeTaxAppliedRowAmnt(const double &base_weee_tax_applied_row_amnt) {
    m_base_weee_tax_applied_row_amnt = base_weee_tax_applied_row_amnt;
    m_base_weee_tax_applied_row_amnt_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_base_weee_tax_applied_row_amnt_Set() const{
    return m_base_weee_tax_applied_row_amnt_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_base_weee_tax_applied_row_amnt_Valid() const{
    return m_base_weee_tax_applied_row_amnt_isValid;
}

double OAISales_data_creditmemo_item_interface::getBaseWeeeTaxDisposition() const {
    return m_base_weee_tax_disposition;
}
void OAISales_data_creditmemo_item_interface::setBaseWeeeTaxDisposition(const double &base_weee_tax_disposition) {
    m_base_weee_tax_disposition = base_weee_tax_disposition;
    m_base_weee_tax_disposition_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_base_weee_tax_disposition_Set() const{
    return m_base_weee_tax_disposition_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_base_weee_tax_disposition_Valid() const{
    return m_base_weee_tax_disposition_isValid;
}

double OAISales_data_creditmemo_item_interface::getBaseWeeeTaxRowDisposition() const {
    return m_base_weee_tax_row_disposition;
}
void OAISales_data_creditmemo_item_interface::setBaseWeeeTaxRowDisposition(const double &base_weee_tax_row_disposition) {
    m_base_weee_tax_row_disposition = base_weee_tax_row_disposition;
    m_base_weee_tax_row_disposition_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_base_weee_tax_row_disposition_Set() const{
    return m_base_weee_tax_row_disposition_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_base_weee_tax_row_disposition_Valid() const{
    return m_base_weee_tax_row_disposition_isValid;
}

QString OAISales_data_creditmemo_item_interface::getDescription() const {
    return m_description;
}
void OAISales_data_creditmemo_item_interface::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_description_Set() const{
    return m_description_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_description_Valid() const{
    return m_description_isValid;
}

double OAISales_data_creditmemo_item_interface::getDiscountAmount() const {
    return m_discount_amount;
}
void OAISales_data_creditmemo_item_interface::setDiscountAmount(const double &discount_amount) {
    m_discount_amount = discount_amount;
    m_discount_amount_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_discount_amount_Set() const{
    return m_discount_amount_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_discount_amount_Valid() const{
    return m_discount_amount_isValid;
}

double OAISales_data_creditmemo_item_interface::getDiscountTaxCompensationAmount() const {
    return m_discount_tax_compensation_amount;
}
void OAISales_data_creditmemo_item_interface::setDiscountTaxCompensationAmount(const double &discount_tax_compensation_amount) {
    m_discount_tax_compensation_amount = discount_tax_compensation_amount;
    m_discount_tax_compensation_amount_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_discount_tax_compensation_amount_Set() const{
    return m_discount_tax_compensation_amount_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_discount_tax_compensation_amount_Valid() const{
    return m_discount_tax_compensation_amount_isValid;
}

qint32 OAISales_data_creditmemo_item_interface::getEntityId() const {
    return m_entity_id;
}
void OAISales_data_creditmemo_item_interface::setEntityId(const qint32 &entity_id) {
    m_entity_id = entity_id;
    m_entity_id_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_entity_id_Set() const{
    return m_entity_id_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_entity_id_Valid() const{
    return m_entity_id_isValid;
}

OAISales_data_creditmemo_item_extension_interface OAISales_data_creditmemo_item_interface::getExtensionAttributes() const {
    return m_extension_attributes;
}
void OAISales_data_creditmemo_item_interface::setExtensionAttributes(const OAISales_data_creditmemo_item_extension_interface &extension_attributes) {
    m_extension_attributes = extension_attributes;
    m_extension_attributes_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_extension_attributes_Set() const{
    return m_extension_attributes_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_extension_attributes_Valid() const{
    return m_extension_attributes_isValid;
}

QString OAISales_data_creditmemo_item_interface::getName() const {
    return m_name;
}
void OAISales_data_creditmemo_item_interface::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_name_Set() const{
    return m_name_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAISales_data_creditmemo_item_interface::getOrderItemId() const {
    return m_order_item_id;
}
void OAISales_data_creditmemo_item_interface::setOrderItemId(const qint32 &order_item_id) {
    m_order_item_id = order_item_id;
    m_order_item_id_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_order_item_id_Set() const{
    return m_order_item_id_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_order_item_id_Valid() const{
    return m_order_item_id_isValid;
}

qint32 OAISales_data_creditmemo_item_interface::getParentId() const {
    return m_parent_id;
}
void OAISales_data_creditmemo_item_interface::setParentId(const qint32 &parent_id) {
    m_parent_id = parent_id;
    m_parent_id_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_parent_id_Set() const{
    return m_parent_id_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_parent_id_Valid() const{
    return m_parent_id_isValid;
}

double OAISales_data_creditmemo_item_interface::getPrice() const {
    return m_price;
}
void OAISales_data_creditmemo_item_interface::setPrice(const double &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_price_Set() const{
    return m_price_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_price_Valid() const{
    return m_price_isValid;
}

double OAISales_data_creditmemo_item_interface::getPriceInclTax() const {
    return m_price_incl_tax;
}
void OAISales_data_creditmemo_item_interface::setPriceInclTax(const double &price_incl_tax) {
    m_price_incl_tax = price_incl_tax;
    m_price_incl_tax_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_price_incl_tax_Set() const{
    return m_price_incl_tax_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_price_incl_tax_Valid() const{
    return m_price_incl_tax_isValid;
}

qint32 OAISales_data_creditmemo_item_interface::getProductId() const {
    return m_product_id;
}
void OAISales_data_creditmemo_item_interface::setProductId(const qint32 &product_id) {
    m_product_id = product_id;
    m_product_id_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_product_id_Set() const{
    return m_product_id_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_product_id_Valid() const{
    return m_product_id_isValid;
}

double OAISales_data_creditmemo_item_interface::getQty() const {
    return m_qty;
}
void OAISales_data_creditmemo_item_interface::setQty(const double &qty) {
    m_qty = qty;
    m_qty_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_qty_Set() const{
    return m_qty_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_qty_Valid() const{
    return m_qty_isValid;
}

double OAISales_data_creditmemo_item_interface::getRowTotal() const {
    return m_row_total;
}
void OAISales_data_creditmemo_item_interface::setRowTotal(const double &row_total) {
    m_row_total = row_total;
    m_row_total_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_row_total_Set() const{
    return m_row_total_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_row_total_Valid() const{
    return m_row_total_isValid;
}

double OAISales_data_creditmemo_item_interface::getRowTotalInclTax() const {
    return m_row_total_incl_tax;
}
void OAISales_data_creditmemo_item_interface::setRowTotalInclTax(const double &row_total_incl_tax) {
    m_row_total_incl_tax = row_total_incl_tax;
    m_row_total_incl_tax_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_row_total_incl_tax_Set() const{
    return m_row_total_incl_tax_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_row_total_incl_tax_Valid() const{
    return m_row_total_incl_tax_isValid;
}

QString OAISales_data_creditmemo_item_interface::getSku() const {
    return m_sku;
}
void OAISales_data_creditmemo_item_interface::setSku(const QString &sku) {
    m_sku = sku;
    m_sku_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_sku_Set() const{
    return m_sku_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_sku_Valid() const{
    return m_sku_isValid;
}

double OAISales_data_creditmemo_item_interface::getTaxAmount() const {
    return m_tax_amount;
}
void OAISales_data_creditmemo_item_interface::setTaxAmount(const double &tax_amount) {
    m_tax_amount = tax_amount;
    m_tax_amount_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_tax_amount_Set() const{
    return m_tax_amount_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_tax_amount_Valid() const{
    return m_tax_amount_isValid;
}

QString OAISales_data_creditmemo_item_interface::getWeeeTaxApplied() const {
    return m_weee_tax_applied;
}
void OAISales_data_creditmemo_item_interface::setWeeeTaxApplied(const QString &weee_tax_applied) {
    m_weee_tax_applied = weee_tax_applied;
    m_weee_tax_applied_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_weee_tax_applied_Set() const{
    return m_weee_tax_applied_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_weee_tax_applied_Valid() const{
    return m_weee_tax_applied_isValid;
}

double OAISales_data_creditmemo_item_interface::getWeeeTaxAppliedAmount() const {
    return m_weee_tax_applied_amount;
}
void OAISales_data_creditmemo_item_interface::setWeeeTaxAppliedAmount(const double &weee_tax_applied_amount) {
    m_weee_tax_applied_amount = weee_tax_applied_amount;
    m_weee_tax_applied_amount_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_weee_tax_applied_amount_Set() const{
    return m_weee_tax_applied_amount_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_weee_tax_applied_amount_Valid() const{
    return m_weee_tax_applied_amount_isValid;
}

double OAISales_data_creditmemo_item_interface::getWeeeTaxAppliedRowAmount() const {
    return m_weee_tax_applied_row_amount;
}
void OAISales_data_creditmemo_item_interface::setWeeeTaxAppliedRowAmount(const double &weee_tax_applied_row_amount) {
    m_weee_tax_applied_row_amount = weee_tax_applied_row_amount;
    m_weee_tax_applied_row_amount_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_weee_tax_applied_row_amount_Set() const{
    return m_weee_tax_applied_row_amount_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_weee_tax_applied_row_amount_Valid() const{
    return m_weee_tax_applied_row_amount_isValid;
}

double OAISales_data_creditmemo_item_interface::getWeeeTaxDisposition() const {
    return m_weee_tax_disposition;
}
void OAISales_data_creditmemo_item_interface::setWeeeTaxDisposition(const double &weee_tax_disposition) {
    m_weee_tax_disposition = weee_tax_disposition;
    m_weee_tax_disposition_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_weee_tax_disposition_Set() const{
    return m_weee_tax_disposition_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_weee_tax_disposition_Valid() const{
    return m_weee_tax_disposition_isValid;
}

double OAISales_data_creditmemo_item_interface::getWeeeTaxRowDisposition() const {
    return m_weee_tax_row_disposition;
}
void OAISales_data_creditmemo_item_interface::setWeeeTaxRowDisposition(const double &weee_tax_row_disposition) {
    m_weee_tax_row_disposition = weee_tax_row_disposition;
    m_weee_tax_row_disposition_isSet = true;
}

bool OAISales_data_creditmemo_item_interface::is_weee_tax_row_disposition_Set() const{
    return m_weee_tax_row_disposition_isSet;
}

bool OAISales_data_creditmemo_item_interface::is_weee_tax_row_disposition_Valid() const{
    return m_weee_tax_row_disposition_isValid;
}

bool OAISales_data_creditmemo_item_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_additional_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_cost_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_discount_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_discount_tax_compensation_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_price_incl_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_row_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_row_total_incl_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_tax_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_weee_tax_applied_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_weee_tax_applied_row_amnt_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_weee_tax_disposition_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_weee_tax_row_disposition_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_tax_compensation_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_entity_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extension_attributes.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_item_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_incl_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_qty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_row_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_row_total_incl_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_weee_tax_applied_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_weee_tax_applied_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_weee_tax_applied_row_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_weee_tax_disposition_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_weee_tax_row_disposition_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISales_data_creditmemo_item_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_base_cost_isValid && m_base_price_isValid && m_entity_id_isValid && m_order_item_id_isValid && m_qty_isValid && true;
}

} // namespace OpenAPI
