/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIProductVariantUpdate.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProductVariantUpdate::OAIProductVariantUpdate(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProductVariantUpdate::OAIProductVariantUpdate() {
    this->initializeModel();
}

OAIProductVariantUpdate::~OAIProductVariantUpdate() {}

void OAIProductVariantUpdate::initializeModel() {

    m_available_for_sale_isSet = false;
    m_available_for_sale_isValid = false;

    m_backorder_status_isSet = false;
    m_backorder_status_isValid = false;

    m_barcode_isSet = false;
    m_barcode_isValid = false;

    m_clear_cache_isSet = false;
    m_clear_cache_isValid = false;

    m_cost_price_isSet = false;
    m_cost_price_isValid = false;

    m_country_of_origin_isSet = false;
    m_country_of_origin_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_gtin_isSet = false;
    m_gtin_isValid = false;

    m_harmonized_system_code_isSet = false;
    m_harmonized_system_code_isValid = false;

    m_height_isSet = false;
    m_height_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_in_stock_isSet = false;
    m_in_stock_isValid = false;

    m_increase_quantity_isSet = false;
    m_increase_quantity_isValid = false;

    m_lang_id_isSet = false;
    m_lang_id_isValid = false;

    m_length_isSet = false;
    m_length_isValid = false;

    m_manage_stock_isSet = false;
    m_manage_stock_isValid = false;

    m_meta_description_isSet = false;
    m_meta_description_isValid = false;

    m_meta_keywords_isSet = false;
    m_meta_keywords_isValid = false;

    m_meta_title_isSet = false;
    m_meta_title_isValid = false;

    m_model_isSet = false;
    m_model_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_old_price_isSet = false;
    m_old_price_isValid = false;

    m_options_isSet = false;
    m_options_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_product_id_isSet = false;
    m_product_id_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_reduce_quantity_isSet = false;
    m_reduce_quantity_isValid = false;

    m_reindex_isSet = false;
    m_reindex_isValid = false;

    m_reserve_quantity_isSet = false;
    m_reserve_quantity_isValid = false;

    m_retail_price_isSet = false;
    m_retail_price_isValid = false;

    m_short_description_isSet = false;
    m_short_description_isValid = false;

    m_sku_isSet = false;
    m_sku_isValid = false;

    m_special_price_isSet = false;
    m_special_price_isValid = false;

    m_sprice_create_isSet = false;
    m_sprice_create_isValid = false;

    m_sprice_expire_isSet = false;
    m_sprice_expire_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_store_id_isSet = false;
    m_store_id_isValid = false;

    m_taxable_isSet = false;
    m_taxable_isValid = false;

    m_visible_isSet = false;
    m_visible_isValid = false;

    m_warehouse_id_isSet = false;
    m_warehouse_id_isValid = false;

    m_weight_isSet = false;
    m_weight_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;
}

void OAIProductVariantUpdate::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProductVariantUpdate::fromJsonObject(QJsonObject json) {

    m_available_for_sale_isValid = ::OpenAPI::fromJsonValue(m_available_for_sale, json[QString("available_for_sale")]);
    m_available_for_sale_isSet = !json[QString("available_for_sale")].isNull() && m_available_for_sale_isValid;

    m_backorder_status_isValid = ::OpenAPI::fromJsonValue(m_backorder_status, json[QString("backorder_status")]);
    m_backorder_status_isSet = !json[QString("backorder_status")].isNull() && m_backorder_status_isValid;

    m_barcode_isValid = ::OpenAPI::fromJsonValue(m_barcode, json[QString("barcode")]);
    m_barcode_isSet = !json[QString("barcode")].isNull() && m_barcode_isValid;

    m_clear_cache_isValid = ::OpenAPI::fromJsonValue(m_clear_cache, json[QString("clear_cache")]);
    m_clear_cache_isSet = !json[QString("clear_cache")].isNull() && m_clear_cache_isValid;

    m_cost_price_isValid = ::OpenAPI::fromJsonValue(m_cost_price, json[QString("cost_price")]);
    m_cost_price_isSet = !json[QString("cost_price")].isNull() && m_cost_price_isValid;

    m_country_of_origin_isValid = ::OpenAPI::fromJsonValue(m_country_of_origin, json[QString("country_of_origin")]);
    m_country_of_origin_isSet = !json[QString("country_of_origin")].isNull() && m_country_of_origin_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_gtin_isValid = ::OpenAPI::fromJsonValue(m_gtin, json[QString("gtin")]);
    m_gtin_isSet = !json[QString("gtin")].isNull() && m_gtin_isValid;

    m_harmonized_system_code_isValid = ::OpenAPI::fromJsonValue(m_harmonized_system_code, json[QString("harmonized_system_code")]);
    m_harmonized_system_code_isSet = !json[QString("harmonized_system_code")].isNull() && m_harmonized_system_code_isValid;

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("height")]);
    m_height_isSet = !json[QString("height")].isNull() && m_height_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_in_stock_isValid = ::OpenAPI::fromJsonValue(m_in_stock, json[QString("in_stock")]);
    m_in_stock_isSet = !json[QString("in_stock")].isNull() && m_in_stock_isValid;

    m_increase_quantity_isValid = ::OpenAPI::fromJsonValue(m_increase_quantity, json[QString("increase_quantity")]);
    m_increase_quantity_isSet = !json[QString("increase_quantity")].isNull() && m_increase_quantity_isValid;

    m_lang_id_isValid = ::OpenAPI::fromJsonValue(m_lang_id, json[QString("lang_id")]);
    m_lang_id_isSet = !json[QString("lang_id")].isNull() && m_lang_id_isValid;

    m_length_isValid = ::OpenAPI::fromJsonValue(m_length, json[QString("length")]);
    m_length_isSet = !json[QString("length")].isNull() && m_length_isValid;

    m_manage_stock_isValid = ::OpenAPI::fromJsonValue(m_manage_stock, json[QString("manage_stock")]);
    m_manage_stock_isSet = !json[QString("manage_stock")].isNull() && m_manage_stock_isValid;

    m_meta_description_isValid = ::OpenAPI::fromJsonValue(m_meta_description, json[QString("meta_description")]);
    m_meta_description_isSet = !json[QString("meta_description")].isNull() && m_meta_description_isValid;

    m_meta_keywords_isValid = ::OpenAPI::fromJsonValue(m_meta_keywords, json[QString("meta_keywords")]);
    m_meta_keywords_isSet = !json[QString("meta_keywords")].isNull() && m_meta_keywords_isValid;

    m_meta_title_isValid = ::OpenAPI::fromJsonValue(m_meta_title, json[QString("meta_title")]);
    m_meta_title_isSet = !json[QString("meta_title")].isNull() && m_meta_title_isValid;

    m_model_isValid = ::OpenAPI::fromJsonValue(m_model, json[QString("model")]);
    m_model_isSet = !json[QString("model")].isNull() && m_model_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_old_price_isValid = ::OpenAPI::fromJsonValue(m_old_price, json[QString("old_price")]);
    m_old_price_isSet = !json[QString("old_price")].isNull() && m_old_price_isValid;

    m_options_isValid = ::OpenAPI::fromJsonValue(m_options, json[QString("options")]);
    m_options_isSet = !json[QString("options")].isNull() && m_options_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_product_id_isValid = ::OpenAPI::fromJsonValue(m_product_id, json[QString("product_id")]);
    m_product_id_isSet = !json[QString("product_id")].isNull() && m_product_id_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;

    m_reduce_quantity_isValid = ::OpenAPI::fromJsonValue(m_reduce_quantity, json[QString("reduce_quantity")]);
    m_reduce_quantity_isSet = !json[QString("reduce_quantity")].isNull() && m_reduce_quantity_isValid;

    m_reindex_isValid = ::OpenAPI::fromJsonValue(m_reindex, json[QString("reindex")]);
    m_reindex_isSet = !json[QString("reindex")].isNull() && m_reindex_isValid;

    m_reserve_quantity_isValid = ::OpenAPI::fromJsonValue(m_reserve_quantity, json[QString("reserve_quantity")]);
    m_reserve_quantity_isSet = !json[QString("reserve_quantity")].isNull() && m_reserve_quantity_isValid;

    m_retail_price_isValid = ::OpenAPI::fromJsonValue(m_retail_price, json[QString("retail_price")]);
    m_retail_price_isSet = !json[QString("retail_price")].isNull() && m_retail_price_isValid;

    m_short_description_isValid = ::OpenAPI::fromJsonValue(m_short_description, json[QString("short_description")]);
    m_short_description_isSet = !json[QString("short_description")].isNull() && m_short_description_isValid;

    m_sku_isValid = ::OpenAPI::fromJsonValue(m_sku, json[QString("sku")]);
    m_sku_isSet = !json[QString("sku")].isNull() && m_sku_isValid;

    m_special_price_isValid = ::OpenAPI::fromJsonValue(m_special_price, json[QString("special_price")]);
    m_special_price_isSet = !json[QString("special_price")].isNull() && m_special_price_isValid;

    m_sprice_create_isValid = ::OpenAPI::fromJsonValue(m_sprice_create, json[QString("sprice_create")]);
    m_sprice_create_isSet = !json[QString("sprice_create")].isNull() && m_sprice_create_isValid;

    m_sprice_expire_isValid = ::OpenAPI::fromJsonValue(m_sprice_expire, json[QString("sprice_expire")]);
    m_sprice_expire_isSet = !json[QString("sprice_expire")].isNull() && m_sprice_expire_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_store_id_isValid = ::OpenAPI::fromJsonValue(m_store_id, json[QString("store_id")]);
    m_store_id_isSet = !json[QString("store_id")].isNull() && m_store_id_isValid;

    m_taxable_isValid = ::OpenAPI::fromJsonValue(m_taxable, json[QString("taxable")]);
    m_taxable_isSet = !json[QString("taxable")].isNull() && m_taxable_isValid;

    m_visible_isValid = ::OpenAPI::fromJsonValue(m_visible, json[QString("visible")]);
    m_visible_isSet = !json[QString("visible")].isNull() && m_visible_isValid;

    m_warehouse_id_isValid = ::OpenAPI::fromJsonValue(m_warehouse_id, json[QString("warehouse_id")]);
    m_warehouse_id_isSet = !json[QString("warehouse_id")].isNull() && m_warehouse_id_isValid;

    m_weight_isValid = ::OpenAPI::fromJsonValue(m_weight, json[QString("weight")]);
    m_weight_isSet = !json[QString("weight")].isNull() && m_weight_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("width")]);
    m_width_isSet = !json[QString("width")].isNull() && m_width_isValid;
}

QString OAIProductVariantUpdate::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProductVariantUpdate::asJsonObject() const {
    QJsonObject obj;
    if (m_available_for_sale_isSet) {
        obj.insert(QString("available_for_sale"), ::OpenAPI::toJsonValue(m_available_for_sale));
    }
    if (m_backorder_status_isSet) {
        obj.insert(QString("backorder_status"), ::OpenAPI::toJsonValue(m_backorder_status));
    }
    if (m_barcode_isSet) {
        obj.insert(QString("barcode"), ::OpenAPI::toJsonValue(m_barcode));
    }
    if (m_clear_cache_isSet) {
        obj.insert(QString("clear_cache"), ::OpenAPI::toJsonValue(m_clear_cache));
    }
    if (m_cost_price_isSet) {
        obj.insert(QString("cost_price"), ::OpenAPI::toJsonValue(m_cost_price));
    }
    if (m_country_of_origin_isSet) {
        obj.insert(QString("country_of_origin"), ::OpenAPI::toJsonValue(m_country_of_origin));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_gtin_isSet) {
        obj.insert(QString("gtin"), ::OpenAPI::toJsonValue(m_gtin));
    }
    if (m_harmonized_system_code_isSet) {
        obj.insert(QString("harmonized_system_code"), ::OpenAPI::toJsonValue(m_harmonized_system_code));
    }
    if (m_height_isSet) {
        obj.insert(QString("height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_in_stock_isSet) {
        obj.insert(QString("in_stock"), ::OpenAPI::toJsonValue(m_in_stock));
    }
    if (m_increase_quantity_isSet) {
        obj.insert(QString("increase_quantity"), ::OpenAPI::toJsonValue(m_increase_quantity));
    }
    if (m_lang_id_isSet) {
        obj.insert(QString("lang_id"), ::OpenAPI::toJsonValue(m_lang_id));
    }
    if (m_length_isSet) {
        obj.insert(QString("length"), ::OpenAPI::toJsonValue(m_length));
    }
    if (m_manage_stock_isSet) {
        obj.insert(QString("manage_stock"), ::OpenAPI::toJsonValue(m_manage_stock));
    }
    if (m_meta_description_isSet) {
        obj.insert(QString("meta_description"), ::OpenAPI::toJsonValue(m_meta_description));
    }
    if (m_meta_keywords_isSet) {
        obj.insert(QString("meta_keywords"), ::OpenAPI::toJsonValue(m_meta_keywords));
    }
    if (m_meta_title_isSet) {
        obj.insert(QString("meta_title"), ::OpenAPI::toJsonValue(m_meta_title));
    }
    if (m_model_isSet) {
        obj.insert(QString("model"), ::OpenAPI::toJsonValue(m_model));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_old_price_isSet) {
        obj.insert(QString("old_price"), ::OpenAPI::toJsonValue(m_old_price));
    }
    if (m_options.size() > 0) {
        obj.insert(QString("options"), ::OpenAPI::toJsonValue(m_options));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_product_id_isSet) {
        obj.insert(QString("product_id"), ::OpenAPI::toJsonValue(m_product_id));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_reduce_quantity_isSet) {
        obj.insert(QString("reduce_quantity"), ::OpenAPI::toJsonValue(m_reduce_quantity));
    }
    if (m_reindex_isSet) {
        obj.insert(QString("reindex"), ::OpenAPI::toJsonValue(m_reindex));
    }
    if (m_reserve_quantity_isSet) {
        obj.insert(QString("reserve_quantity"), ::OpenAPI::toJsonValue(m_reserve_quantity));
    }
    if (m_retail_price_isSet) {
        obj.insert(QString("retail_price"), ::OpenAPI::toJsonValue(m_retail_price));
    }
    if (m_short_description_isSet) {
        obj.insert(QString("short_description"), ::OpenAPI::toJsonValue(m_short_description));
    }
    if (m_sku_isSet) {
        obj.insert(QString("sku"), ::OpenAPI::toJsonValue(m_sku));
    }
    if (m_special_price_isSet) {
        obj.insert(QString("special_price"), ::OpenAPI::toJsonValue(m_special_price));
    }
    if (m_sprice_create_isSet) {
        obj.insert(QString("sprice_create"), ::OpenAPI::toJsonValue(m_sprice_create));
    }
    if (m_sprice_expire_isSet) {
        obj.insert(QString("sprice_expire"), ::OpenAPI::toJsonValue(m_sprice_expire));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_store_id_isSet) {
        obj.insert(QString("store_id"), ::OpenAPI::toJsonValue(m_store_id));
    }
    if (m_taxable_isSet) {
        obj.insert(QString("taxable"), ::OpenAPI::toJsonValue(m_taxable));
    }
    if (m_visible_isSet) {
        obj.insert(QString("visible"), ::OpenAPI::toJsonValue(m_visible));
    }
    if (m_warehouse_id_isSet) {
        obj.insert(QString("warehouse_id"), ::OpenAPI::toJsonValue(m_warehouse_id));
    }
    if (m_weight_isSet) {
        obj.insert(QString("weight"), ::OpenAPI::toJsonValue(m_weight));
    }
    if (m_width_isSet) {
        obj.insert(QString("width"), ::OpenAPI::toJsonValue(m_width));
    }
    return obj;
}

bool OAIProductVariantUpdate::isAvailableForSale() const {
    return m_available_for_sale;
}
void OAIProductVariantUpdate::setAvailableForSale(const bool &available_for_sale) {
    m_available_for_sale = available_for_sale;
    m_available_for_sale_isSet = true;
}

bool OAIProductVariantUpdate::is_available_for_sale_Set() const{
    return m_available_for_sale_isSet;
}

bool OAIProductVariantUpdate::is_available_for_sale_Valid() const{
    return m_available_for_sale_isValid;
}

QString OAIProductVariantUpdate::getBackorderStatus() const {
    return m_backorder_status;
}
void OAIProductVariantUpdate::setBackorderStatus(const QString &backorder_status) {
    m_backorder_status = backorder_status;
    m_backorder_status_isSet = true;
}

bool OAIProductVariantUpdate::is_backorder_status_Set() const{
    return m_backorder_status_isSet;
}

bool OAIProductVariantUpdate::is_backorder_status_Valid() const{
    return m_backorder_status_isValid;
}

QString OAIProductVariantUpdate::getBarcode() const {
    return m_barcode;
}
void OAIProductVariantUpdate::setBarcode(const QString &barcode) {
    m_barcode = barcode;
    m_barcode_isSet = true;
}

bool OAIProductVariantUpdate::is_barcode_Set() const{
    return m_barcode_isSet;
}

bool OAIProductVariantUpdate::is_barcode_Valid() const{
    return m_barcode_isValid;
}

bool OAIProductVariantUpdate::isClearCache() const {
    return m_clear_cache;
}
void OAIProductVariantUpdate::setClearCache(const bool &clear_cache) {
    m_clear_cache = clear_cache;
    m_clear_cache_isSet = true;
}

bool OAIProductVariantUpdate::is_clear_cache_Set() const{
    return m_clear_cache_isSet;
}

bool OAIProductVariantUpdate::is_clear_cache_Valid() const{
    return m_clear_cache_isValid;
}

double OAIProductVariantUpdate::getCostPrice() const {
    return m_cost_price;
}
void OAIProductVariantUpdate::setCostPrice(const double &cost_price) {
    m_cost_price = cost_price;
    m_cost_price_isSet = true;
}

bool OAIProductVariantUpdate::is_cost_price_Set() const{
    return m_cost_price_isSet;
}

bool OAIProductVariantUpdate::is_cost_price_Valid() const{
    return m_cost_price_isValid;
}

QString OAIProductVariantUpdate::getCountryOfOrigin() const {
    return m_country_of_origin;
}
void OAIProductVariantUpdate::setCountryOfOrigin(const QString &country_of_origin) {
    m_country_of_origin = country_of_origin;
    m_country_of_origin_isSet = true;
}

bool OAIProductVariantUpdate::is_country_of_origin_Set() const{
    return m_country_of_origin_isSet;
}

bool OAIProductVariantUpdate::is_country_of_origin_Valid() const{
    return m_country_of_origin_isValid;
}

QString OAIProductVariantUpdate::getDescription() const {
    return m_description;
}
void OAIProductVariantUpdate::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIProductVariantUpdate::is_description_Set() const{
    return m_description_isSet;
}

bool OAIProductVariantUpdate::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIProductVariantUpdate::getGtin() const {
    return m_gtin;
}
void OAIProductVariantUpdate::setGtin(const QString &gtin) {
    m_gtin = gtin;
    m_gtin_isSet = true;
}

bool OAIProductVariantUpdate::is_gtin_Set() const{
    return m_gtin_isSet;
}

bool OAIProductVariantUpdate::is_gtin_Valid() const{
    return m_gtin_isValid;
}

QString OAIProductVariantUpdate::getHarmonizedSystemCode() const {
    return m_harmonized_system_code;
}
void OAIProductVariantUpdate::setHarmonizedSystemCode(const QString &harmonized_system_code) {
    m_harmonized_system_code = harmonized_system_code;
    m_harmonized_system_code_isSet = true;
}

bool OAIProductVariantUpdate::is_harmonized_system_code_Set() const{
    return m_harmonized_system_code_isSet;
}

bool OAIProductVariantUpdate::is_harmonized_system_code_Valid() const{
    return m_harmonized_system_code_isValid;
}

double OAIProductVariantUpdate::getHeight() const {
    return m_height;
}
void OAIProductVariantUpdate::setHeight(const double &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAIProductVariantUpdate::is_height_Set() const{
    return m_height_isSet;
}

bool OAIProductVariantUpdate::is_height_Valid() const{
    return m_height_isValid;
}

QString OAIProductVariantUpdate::getId() const {
    return m_id;
}
void OAIProductVariantUpdate::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIProductVariantUpdate::is_id_Set() const{
    return m_id_isSet;
}

bool OAIProductVariantUpdate::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIProductVariantUpdate::isInStock() const {
    return m_in_stock;
}
void OAIProductVariantUpdate::setInStock(const bool &in_stock) {
    m_in_stock = in_stock;
    m_in_stock_isSet = true;
}

bool OAIProductVariantUpdate::is_in_stock_Set() const{
    return m_in_stock_isSet;
}

bool OAIProductVariantUpdate::is_in_stock_Valid() const{
    return m_in_stock_isValid;
}

double OAIProductVariantUpdate::getIncreaseQuantity() const {
    return m_increase_quantity;
}
void OAIProductVariantUpdate::setIncreaseQuantity(const double &increase_quantity) {
    m_increase_quantity = increase_quantity;
    m_increase_quantity_isSet = true;
}

bool OAIProductVariantUpdate::is_increase_quantity_Set() const{
    return m_increase_quantity_isSet;
}

bool OAIProductVariantUpdate::is_increase_quantity_Valid() const{
    return m_increase_quantity_isValid;
}

QString OAIProductVariantUpdate::getLangId() const {
    return m_lang_id;
}
void OAIProductVariantUpdate::setLangId(const QString &lang_id) {
    m_lang_id = lang_id;
    m_lang_id_isSet = true;
}

bool OAIProductVariantUpdate::is_lang_id_Set() const{
    return m_lang_id_isSet;
}

bool OAIProductVariantUpdate::is_lang_id_Valid() const{
    return m_lang_id_isValid;
}

double OAIProductVariantUpdate::getLength() const {
    return m_length;
}
void OAIProductVariantUpdate::setLength(const double &length) {
    m_length = length;
    m_length_isSet = true;
}

bool OAIProductVariantUpdate::is_length_Set() const{
    return m_length_isSet;
}

bool OAIProductVariantUpdate::is_length_Valid() const{
    return m_length_isValid;
}

bool OAIProductVariantUpdate::isManageStock() const {
    return m_manage_stock;
}
void OAIProductVariantUpdate::setManageStock(const bool &manage_stock) {
    m_manage_stock = manage_stock;
    m_manage_stock_isSet = true;
}

bool OAIProductVariantUpdate::is_manage_stock_Set() const{
    return m_manage_stock_isSet;
}

bool OAIProductVariantUpdate::is_manage_stock_Valid() const{
    return m_manage_stock_isValid;
}

QString OAIProductVariantUpdate::getMetaDescription() const {
    return m_meta_description;
}
void OAIProductVariantUpdate::setMetaDescription(const QString &meta_description) {
    m_meta_description = meta_description;
    m_meta_description_isSet = true;
}

bool OAIProductVariantUpdate::is_meta_description_Set() const{
    return m_meta_description_isSet;
}

bool OAIProductVariantUpdate::is_meta_description_Valid() const{
    return m_meta_description_isValid;
}

QString OAIProductVariantUpdate::getMetaKeywords() const {
    return m_meta_keywords;
}
void OAIProductVariantUpdate::setMetaKeywords(const QString &meta_keywords) {
    m_meta_keywords = meta_keywords;
    m_meta_keywords_isSet = true;
}

bool OAIProductVariantUpdate::is_meta_keywords_Set() const{
    return m_meta_keywords_isSet;
}

bool OAIProductVariantUpdate::is_meta_keywords_Valid() const{
    return m_meta_keywords_isValid;
}

QString OAIProductVariantUpdate::getMetaTitle() const {
    return m_meta_title;
}
void OAIProductVariantUpdate::setMetaTitle(const QString &meta_title) {
    m_meta_title = meta_title;
    m_meta_title_isSet = true;
}

bool OAIProductVariantUpdate::is_meta_title_Set() const{
    return m_meta_title_isSet;
}

bool OAIProductVariantUpdate::is_meta_title_Valid() const{
    return m_meta_title_isValid;
}

QString OAIProductVariantUpdate::getModel() const {
    return m_model;
}
void OAIProductVariantUpdate::setModel(const QString &model) {
    m_model = model;
    m_model_isSet = true;
}

bool OAIProductVariantUpdate::is_model_Set() const{
    return m_model_isSet;
}

bool OAIProductVariantUpdate::is_model_Valid() const{
    return m_model_isValid;
}

QString OAIProductVariantUpdate::getName() const {
    return m_name;
}
void OAIProductVariantUpdate::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIProductVariantUpdate::is_name_Set() const{
    return m_name_isSet;
}

bool OAIProductVariantUpdate::is_name_Valid() const{
    return m_name_isValid;
}

double OAIProductVariantUpdate::getOldPrice() const {
    return m_old_price;
}
void OAIProductVariantUpdate::setOldPrice(const double &old_price) {
    m_old_price = old_price;
    m_old_price_isSet = true;
}

bool OAIProductVariantUpdate::is_old_price_Set() const{
    return m_old_price_isSet;
}

bool OAIProductVariantUpdate::is_old_price_Valid() const{
    return m_old_price_isValid;
}

QList<OAIProductVariantUpdate_options_inner> OAIProductVariantUpdate::getOptions() const {
    return m_options;
}
void OAIProductVariantUpdate::setOptions(const QList<OAIProductVariantUpdate_options_inner> &options) {
    m_options = options;
    m_options_isSet = true;
}

bool OAIProductVariantUpdate::is_options_Set() const{
    return m_options_isSet;
}

bool OAIProductVariantUpdate::is_options_Valid() const{
    return m_options_isValid;
}

double OAIProductVariantUpdate::getPrice() const {
    return m_price;
}
void OAIProductVariantUpdate::setPrice(const double &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAIProductVariantUpdate::is_price_Set() const{
    return m_price_isSet;
}

bool OAIProductVariantUpdate::is_price_Valid() const{
    return m_price_isValid;
}

QString OAIProductVariantUpdate::getProductId() const {
    return m_product_id;
}
void OAIProductVariantUpdate::setProductId(const QString &product_id) {
    m_product_id = product_id;
    m_product_id_isSet = true;
}

bool OAIProductVariantUpdate::is_product_id_Set() const{
    return m_product_id_isSet;
}

bool OAIProductVariantUpdate::is_product_id_Valid() const{
    return m_product_id_isValid;
}

double OAIProductVariantUpdate::getQuantity() const {
    return m_quantity;
}
void OAIProductVariantUpdate::setQuantity(const double &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAIProductVariantUpdate::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAIProductVariantUpdate::is_quantity_Valid() const{
    return m_quantity_isValid;
}

double OAIProductVariantUpdate::getReduceQuantity() const {
    return m_reduce_quantity;
}
void OAIProductVariantUpdate::setReduceQuantity(const double &reduce_quantity) {
    m_reduce_quantity = reduce_quantity;
    m_reduce_quantity_isSet = true;
}

bool OAIProductVariantUpdate::is_reduce_quantity_Set() const{
    return m_reduce_quantity_isSet;
}

bool OAIProductVariantUpdate::is_reduce_quantity_Valid() const{
    return m_reduce_quantity_isValid;
}

bool OAIProductVariantUpdate::isReindex() const {
    return m_reindex;
}
void OAIProductVariantUpdate::setReindex(const bool &reindex) {
    m_reindex = reindex;
    m_reindex_isSet = true;
}

bool OAIProductVariantUpdate::is_reindex_Set() const{
    return m_reindex_isSet;
}

bool OAIProductVariantUpdate::is_reindex_Valid() const{
    return m_reindex_isValid;
}

double OAIProductVariantUpdate::getReserveQuantity() const {
    return m_reserve_quantity;
}
void OAIProductVariantUpdate::setReserveQuantity(const double &reserve_quantity) {
    m_reserve_quantity = reserve_quantity;
    m_reserve_quantity_isSet = true;
}

bool OAIProductVariantUpdate::is_reserve_quantity_Set() const{
    return m_reserve_quantity_isSet;
}

bool OAIProductVariantUpdate::is_reserve_quantity_Valid() const{
    return m_reserve_quantity_isValid;
}

double OAIProductVariantUpdate::getRetailPrice() const {
    return m_retail_price;
}
void OAIProductVariantUpdate::setRetailPrice(const double &retail_price) {
    m_retail_price = retail_price;
    m_retail_price_isSet = true;
}

bool OAIProductVariantUpdate::is_retail_price_Set() const{
    return m_retail_price_isSet;
}

bool OAIProductVariantUpdate::is_retail_price_Valid() const{
    return m_retail_price_isValid;
}

QString OAIProductVariantUpdate::getShortDescription() const {
    return m_short_description;
}
void OAIProductVariantUpdate::setShortDescription(const QString &short_description) {
    m_short_description = short_description;
    m_short_description_isSet = true;
}

bool OAIProductVariantUpdate::is_short_description_Set() const{
    return m_short_description_isSet;
}

bool OAIProductVariantUpdate::is_short_description_Valid() const{
    return m_short_description_isValid;
}

QString OAIProductVariantUpdate::getSku() const {
    return m_sku;
}
void OAIProductVariantUpdate::setSku(const QString &sku) {
    m_sku = sku;
    m_sku_isSet = true;
}

bool OAIProductVariantUpdate::is_sku_Set() const{
    return m_sku_isSet;
}

bool OAIProductVariantUpdate::is_sku_Valid() const{
    return m_sku_isValid;
}

double OAIProductVariantUpdate::getSpecialPrice() const {
    return m_special_price;
}
void OAIProductVariantUpdate::setSpecialPrice(const double &special_price) {
    m_special_price = special_price;
    m_special_price_isSet = true;
}

bool OAIProductVariantUpdate::is_special_price_Set() const{
    return m_special_price_isSet;
}

bool OAIProductVariantUpdate::is_special_price_Valid() const{
    return m_special_price_isValid;
}

QString OAIProductVariantUpdate::getSpriceCreate() const {
    return m_sprice_create;
}
void OAIProductVariantUpdate::setSpriceCreate(const QString &sprice_create) {
    m_sprice_create = sprice_create;
    m_sprice_create_isSet = true;
}

bool OAIProductVariantUpdate::is_sprice_create_Set() const{
    return m_sprice_create_isSet;
}

bool OAIProductVariantUpdate::is_sprice_create_Valid() const{
    return m_sprice_create_isValid;
}

QString OAIProductVariantUpdate::getSpriceExpire() const {
    return m_sprice_expire;
}
void OAIProductVariantUpdate::setSpriceExpire(const QString &sprice_expire) {
    m_sprice_expire = sprice_expire;
    m_sprice_expire_isSet = true;
}

bool OAIProductVariantUpdate::is_sprice_expire_Set() const{
    return m_sprice_expire_isSet;
}

bool OAIProductVariantUpdate::is_sprice_expire_Valid() const{
    return m_sprice_expire_isValid;
}

QString OAIProductVariantUpdate::getStatus() const {
    return m_status;
}
void OAIProductVariantUpdate::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIProductVariantUpdate::is_status_Set() const{
    return m_status_isSet;
}

bool OAIProductVariantUpdate::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIProductVariantUpdate::getStoreId() const {
    return m_store_id;
}
void OAIProductVariantUpdate::setStoreId(const QString &store_id) {
    m_store_id = store_id;
    m_store_id_isSet = true;
}

bool OAIProductVariantUpdate::is_store_id_Set() const{
    return m_store_id_isSet;
}

bool OAIProductVariantUpdate::is_store_id_Valid() const{
    return m_store_id_isValid;
}

bool OAIProductVariantUpdate::isTaxable() const {
    return m_taxable;
}
void OAIProductVariantUpdate::setTaxable(const bool &taxable) {
    m_taxable = taxable;
    m_taxable_isSet = true;
}

bool OAIProductVariantUpdate::is_taxable_Set() const{
    return m_taxable_isSet;
}

bool OAIProductVariantUpdate::is_taxable_Valid() const{
    return m_taxable_isValid;
}

QString OAIProductVariantUpdate::getVisible() const {
    return m_visible;
}
void OAIProductVariantUpdate::setVisible(const QString &visible) {
    m_visible = visible;
    m_visible_isSet = true;
}

bool OAIProductVariantUpdate::is_visible_Set() const{
    return m_visible_isSet;
}

bool OAIProductVariantUpdate::is_visible_Valid() const{
    return m_visible_isValid;
}

QString OAIProductVariantUpdate::getWarehouseId() const {
    return m_warehouse_id;
}
void OAIProductVariantUpdate::setWarehouseId(const QString &warehouse_id) {
    m_warehouse_id = warehouse_id;
    m_warehouse_id_isSet = true;
}

bool OAIProductVariantUpdate::is_warehouse_id_Set() const{
    return m_warehouse_id_isSet;
}

bool OAIProductVariantUpdate::is_warehouse_id_Valid() const{
    return m_warehouse_id_isValid;
}

double OAIProductVariantUpdate::getWeight() const {
    return m_weight;
}
void OAIProductVariantUpdate::setWeight(const double &weight) {
    m_weight = weight;
    m_weight_isSet = true;
}

bool OAIProductVariantUpdate::is_weight_Set() const{
    return m_weight_isSet;
}

bool OAIProductVariantUpdate::is_weight_Valid() const{
    return m_weight_isValid;
}

double OAIProductVariantUpdate::getWidth() const {
    return m_width;
}
void OAIProductVariantUpdate::setWidth(const double &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAIProductVariantUpdate::is_width_Set() const{
    return m_width_isSet;
}

bool OAIProductVariantUpdate::is_width_Valid() const{
    return m_width_isValid;
}

bool OAIProductVariantUpdate::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_available_for_sale_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_backorder_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_barcode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_clear_cache_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cost_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_of_origin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gtin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_harmonized_system_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_in_stock_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_increase_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lang_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_manage_stock_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_meta_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_meta_keywords_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_meta_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_model_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_old_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_options.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reduce_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reindex_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reserve_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_retail_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_short_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_special_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sprice_create_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sprice_expire_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_store_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_taxable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_visible_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_warehouse_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_weight_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_width_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProductVariantUpdate::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
