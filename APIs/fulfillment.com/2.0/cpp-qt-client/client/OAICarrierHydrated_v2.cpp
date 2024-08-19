/**
 * Fulfillment.com APIv2
 * Welcome to our current iteration of our REST API. While we encourage you to upgrade to v2.0 we will continue support for our [SOAP API](https://github.com/fulfillment/soap-integration).  # Versioning  The Fulfillment.com (FDC) REST API is version controlled and backwards compatible. We have many future APIs scheduled for publication within our v2.0 spec so please be prepared for us to add data nodes in our responses, however, we will not remove knowledge from previously published APIs.  #### A Current Response  ```javascript {   id: 123 } ```  #### A Potential Future Response  ```javascript {   id: 123,   reason: \"More Knowledge\" } ```  # Getting Started  We use OAuth v2.0 to authenticate clients, you can choose [implicit](https://oauth.net/2/grant-types/implicit/) or [password](https://oauth.net/2/grant-types/password/) grant type. To obtain an OAuth `client_id` and `client_secret` contact your account executive.  **Tip**: Generate an additional login and use those credentials for your integration so that changes are accredited to that \"user\".  You are now ready to make requests to our other APIs by filling your `Authorization` header with `Bearer {access_token}`.  ## Perpetuating Access  Perpetuating access to FDC without storing your password locally can be achieved using the `refresh_token` returned by [POST /oauth/access_token](#operation/generateToken).  A simple concept to achieve this is outlined below.  1. Your application/script will ask you for your `username` and `password`, your `client_id` and `client_secret` will be accessible via a DB or ENV. 2. [Request an access_token](#operation/generateToken)   + Your function should be capable of formatting your request for both a `grant_type` of \\\"password\\\" (step 1) and \\\"refresh_token\\\" (step 4). 3. Store the `access_token` and `refresh_token` so future requests can skip step 1 4. When the `access_token` expires request anew using your `refresh_token`, replace both tokens in local storage.  + If this fails you will have to revert to step 1.  Alternatively if you choose for your application/script to have access to your `username` and `password` you can skip step 4.  In all scenarios we recommend storing all credentials outside your codebase.  ## Date Time Definitions  We will report all date-time stamps using the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard. When using listing API's where fromDate and toDate are available note that both dates are inclusive while requiring the fromDate to be before or at the toDate.  ### The Fulfillment Process  Many steps are required to fulfill your order we report back to you three fundamental milestones inside the orders model.  * `recordedOn` When we received your order. This will never change.  * `dispatchDate` When the current iteration of your order was scheduled for fulfillment. This may change however it is an indicator that the physical process of fulfillment has begun and a tracking number has been **assigned** to your order. The tracking number **MAY CHANGE**. You will not be able to cancel an order once it has been dispatched. If you need to recall an order that has been dispatched please contact your account executive.  * `departDate` When we recorded your order passing our final inspection and placed with the carrier. At this point it is **safe to inform the consignee** of the tracking number as it will not change.  ## Evaluating Error Responses  We currently return two different error models, with and without context. All errors will include a `message` node while errors with `context` will include additional information designed to save you time when encountering highly probable errors. For example, when you send us a request to create a duplicate order, we will reject your request and the context will include the FDC order `id` so that you may record it for your records.  ### Without Context  New order with missing required fields.  | Header | Response | | ------ | -------- | | Status | `400 Bad Request` |  ```javascript {       \"message\": \"Invalid request body\" } ```  ### With Context  New order with duplicate `merchantOrderId`.  | Header | Response | | ------ | -------- | | Status | `409 Conflict` |  ```javascript {   \"message\": \"Duplicate Order\",   \"context\": {     \"id\": 123   } } ```  ## Status Codes  Codes are a concatenation of State, Stage, and Detail.  `^([0-9]{2})([0-9]{2})([0-9]{2})$`  | Code | State              | Stage    | Detail         | | ---- | ------------------ | -------- | -------------- | | 010101 | Processing Order | Recieved | Customer Order | | 010102 | Processing Order | Recieved | Recieved | | 010201 | Processing Order | Approved | | | 010301 | Processing Order | Hold | Merchant Stock | | 010302 | Processing Order | Hold | Merchant Funds | | 010303 | Processing Order | Hold | For Merchant | | 010304 | Processing Order | Hold | Oversized Shipment | | 010305 | Processing Order | Hold | Invalid Parent Order | | 010306 | Processing Order | Hold | Invalid Address | | 010307 | Processing Order | Hold | By Admin | | 010401 | Processing Order | Address Problem | Incomplete Address | | 010402 | Processing Order | Address Problem | Invalid Locality | | 010403 | Processing Order | Address Problem | Invalid Region | | 010404 | Processing Order | Address Problem | Address Not Found | | 010405 | Processing Order | Address Problem | Many Addresses Found | | 010406 | Processing Order | Address Problem | Invalid Postal Code | | 010407 | Processing Order | Address Problem | Country Not Mapped | | 010408 | Processing Order | Address Problem | Invalid Recipient Name | | 010409 | Processing Order | Address Problem | Bad UK Address | | 010410 | Processing Order | Address Problem | Invalid Address Line 1 or 2 | | 010501 | Processing Order | Sku Problem | Invalid SKU | | 010501 | Processing Order | Sku Problem | Child Order has Invalid SKUs | | 010601 | Processing Order | Facility Problem | Facility Not Mapped | | 010701 | Processing Order | Ship Method Problem | Unmapped Ship Method | | 010702 | Processing Order | Ship Method Problem | Unmapped Ship Cost | | 010703 | Processing Order | Ship Method Problem | Missing Ship Method | | 010704 | Processing Order | Ship Method Problem | Invalid Ship Method | | 010705 | Processing Order | Ship Method Problem | Order Weight Outside of Ship Method Weight | | 010801 | Processing Order | Inventory Problem | Insufficient Inventory In Facility | | 010802 | Processing Order | Inventory Problem | Issue Encountered During Inventory Adjustment | | 010901 | Processing Order | Released To WMS | Released | | 020101 | Fulfillment In Progress | Postage Problem | Address Issue | | 020102 | Fulfillment In Progress | Postage Problem | Postage OK, OMS Issue Occurred | | 020103 | Fulfillment In Progress | Postage Problem | Postage Void Failed | | 020201 | Fulfillment In Progress | Postage Acquired | | | 020301 | Fulfillment In Progress | Postage Voided | Postage Void Failed Gracefully | | 020301 | Fulfillment In Progress | Hold | Departure Hold Requested | | 020401 | Fulfillment In Progress | 4PL Processing | | | 020501 | Fulfillment In Progress | 4PL Problem | Order is Proccessable, Postage Issue Occurred | | 020601 | Fulfillment In Progress | Label Printed | | | 020701 | Fulfillment In Progress | Shipment Cubed | | | 020801 | Fulfillment In Progress | Picking Inventory | | | 020901 | Fulfillment In Progress | Label Print Verified | | | 021001 | Fulfillment In Progress | Passed Final Inspection | | | 030101 | Shipped | Fulfilled By 4PL | | | 030102 | Shipped | Fulfilled By 4PL | Successfully Fulfilled, OMS Encountered Issue During Processing | | 030201 | Shipped | Fulfilled By FDC | | | 040101 | Returned | Returned | | | 050101 | Cancelled | Cancelled | | | 060101 | Test | Test | Test | 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: dev@fulfillment.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICarrierHydrated_v2.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICarrierHydrated_v2::OAICarrierHydrated_v2(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICarrierHydrated_v2::OAICarrierHydrated_v2() {
    this->initializeModel();
}

OAICarrierHydrated_v2::~OAICarrierHydrated_v2() {}

void OAICarrierHydrated_v2::initializeModel() {

    m_can_reprint_postage_isSet = false;
    m_can_reprint_postage_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_include_peripherals_isSet = false;
    m_include_peripherals_isValid = false;

    m_internal_rates_only_isSet = false;
    m_internal_rates_only_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_requires_dimensions_isSet = false;
    m_requires_dimensions_isValid = false;

    m_symbol_isSet = false;
    m_symbol_isValid = false;
}

void OAICarrierHydrated_v2::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICarrierHydrated_v2::fromJsonObject(QJsonObject json) {

    m_can_reprint_postage_isValid = ::OpenAPI::fromJsonValue(m_can_reprint_postage, json[QString("canReprintPostage")]);
    m_can_reprint_postage_isSet = !json[QString("canReprintPostage")].isNull() && m_can_reprint_postage_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_include_peripherals_isValid = ::OpenAPI::fromJsonValue(m_include_peripherals, json[QString("includePeripherals")]);
    m_include_peripherals_isSet = !json[QString("includePeripherals")].isNull() && m_include_peripherals_isValid;

    m_internal_rates_only_isValid = ::OpenAPI::fromJsonValue(m_internal_rates_only, json[QString("internalRatesOnly")]);
    m_internal_rates_only_isSet = !json[QString("internalRatesOnly")].isNull() && m_internal_rates_only_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_requires_dimensions_isValid = ::OpenAPI::fromJsonValue(m_requires_dimensions, json[QString("requiresDimensions")]);
    m_requires_dimensions_isSet = !json[QString("requiresDimensions")].isNull() && m_requires_dimensions_isValid;

    m_symbol_isValid = ::OpenAPI::fromJsonValue(m_symbol, json[QString("symbol")]);
    m_symbol_isSet = !json[QString("symbol")].isNull() && m_symbol_isValid;
}

QString OAICarrierHydrated_v2::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICarrierHydrated_v2::asJsonObject() const {
    QJsonObject obj;
    if (m_can_reprint_postage_isSet) {
        obj.insert(QString("canReprintPostage"), ::OpenAPI::toJsonValue(m_can_reprint_postage));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_include_peripherals_isSet) {
        obj.insert(QString("includePeripherals"), ::OpenAPI::toJsonValue(m_include_peripherals));
    }
    if (m_internal_rates_only_isSet) {
        obj.insert(QString("internalRatesOnly"), ::OpenAPI::toJsonValue(m_internal_rates_only));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_requires_dimensions_isSet) {
        obj.insert(QString("requiresDimensions"), ::OpenAPI::toJsonValue(m_requires_dimensions));
    }
    if (m_symbol_isSet) {
        obj.insert(QString("symbol"), ::OpenAPI::toJsonValue(m_symbol));
    }
    return obj;
}

bool OAICarrierHydrated_v2::isCanReprintPostage() const {
    return m_can_reprint_postage;
}
void OAICarrierHydrated_v2::setCanReprintPostage(const bool &can_reprint_postage) {
    m_can_reprint_postage = can_reprint_postage;
    m_can_reprint_postage_isSet = true;
}

bool OAICarrierHydrated_v2::is_can_reprint_postage_Set() const{
    return m_can_reprint_postage_isSet;
}

bool OAICarrierHydrated_v2::is_can_reprint_postage_Valid() const{
    return m_can_reprint_postage_isValid;
}

bool OAICarrierHydrated_v2::isEnabled() const {
    return m_enabled;
}
void OAICarrierHydrated_v2::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAICarrierHydrated_v2::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAICarrierHydrated_v2::is_enabled_Valid() const{
    return m_enabled_isValid;
}

qint32 OAICarrierHydrated_v2::getId() const {
    return m_id;
}
void OAICarrierHydrated_v2::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICarrierHydrated_v2::is_id_Set() const{
    return m_id_isSet;
}

bool OAICarrierHydrated_v2::is_id_Valid() const{
    return m_id_isValid;
}

bool OAICarrierHydrated_v2::isIncludePeripherals() const {
    return m_include_peripherals;
}
void OAICarrierHydrated_v2::setIncludePeripherals(const bool &include_peripherals) {
    m_include_peripherals = include_peripherals;
    m_include_peripherals_isSet = true;
}

bool OAICarrierHydrated_v2::is_include_peripherals_Set() const{
    return m_include_peripherals_isSet;
}

bool OAICarrierHydrated_v2::is_include_peripherals_Valid() const{
    return m_include_peripherals_isValid;
}

bool OAICarrierHydrated_v2::isInternalRatesOnly() const {
    return m_internal_rates_only;
}
void OAICarrierHydrated_v2::setInternalRatesOnly(const bool &internal_rates_only) {
    m_internal_rates_only = internal_rates_only;
    m_internal_rates_only_isSet = true;
}

bool OAICarrierHydrated_v2::is_internal_rates_only_Set() const{
    return m_internal_rates_only_isSet;
}

bool OAICarrierHydrated_v2::is_internal_rates_only_Valid() const{
    return m_internal_rates_only_isValid;
}

QString OAICarrierHydrated_v2::getName() const {
    return m_name;
}
void OAICarrierHydrated_v2::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICarrierHydrated_v2::is_name_Set() const{
    return m_name_isSet;
}

bool OAICarrierHydrated_v2::is_name_Valid() const{
    return m_name_isValid;
}

bool OAICarrierHydrated_v2::isRequiresDimensions() const {
    return m_requires_dimensions;
}
void OAICarrierHydrated_v2::setRequiresDimensions(const bool &requires_dimensions) {
    m_requires_dimensions = requires_dimensions;
    m_requires_dimensions_isSet = true;
}

bool OAICarrierHydrated_v2::is_requires_dimensions_Set() const{
    return m_requires_dimensions_isSet;
}

bool OAICarrierHydrated_v2::is_requires_dimensions_Valid() const{
    return m_requires_dimensions_isValid;
}

QString OAICarrierHydrated_v2::getSymbol() const {
    return m_symbol;
}
void OAICarrierHydrated_v2::setSymbol(const QString &symbol) {
    m_symbol = symbol;
    m_symbol_isSet = true;
}

bool OAICarrierHydrated_v2::is_symbol_Set() const{
    return m_symbol_isSet;
}

bool OAICarrierHydrated_v2::is_symbol_Valid() const{
    return m_symbol_isValid;
}

bool OAICarrierHydrated_v2::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_can_reprint_postage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_include_peripherals_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_internal_rates_only_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_requires_dimensions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_symbol_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICarrierHydrated_v2::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_name_isValid && m_symbol_isValid && true;
}

} // namespace OpenAPI
