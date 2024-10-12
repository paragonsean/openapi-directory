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

#include "OAIAccounting_v2_fees.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAccounting_v2_fees::OAIAccounting_v2_fees(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAccounting_v2_fees::OAIAccounting_v2_fees() {
    this->initializeModel();
}

OAIAccounting_v2_fees::~OAIAccounting_v2_fees() {}

void OAIAccounting_v2_fees::initializeModel() {

    m_box_isSet = false;
    m_box_isValid = false;

    m_envelope_isSet = false;
    m_envelope_isValid = false;

    m_fulfillment_isSet = false;
    m_fulfillment_isValid = false;

    m_insert_isSet = false;
    m_insert_isValid = false;

    m_kitting_isSet = false;
    m_kitting_isValid = false;

    m_picking_isSet = false;
    m_picking_isValid = false;

    m_postage_isSet = false;
    m_postage_isValid = false;

    m_print_isSet = false;
    m_print_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;
}

void OAIAccounting_v2_fees::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAccounting_v2_fees::fromJsonObject(QJsonObject json) {

    m_box_isValid = ::OpenAPI::fromJsonValue(m_box, json[QString("box")]);
    m_box_isSet = !json[QString("box")].isNull() && m_box_isValid;

    m_envelope_isValid = ::OpenAPI::fromJsonValue(m_envelope, json[QString("envelope")]);
    m_envelope_isSet = !json[QString("envelope")].isNull() && m_envelope_isValid;

    m_fulfillment_isValid = ::OpenAPI::fromJsonValue(m_fulfillment, json[QString("fulfillment")]);
    m_fulfillment_isSet = !json[QString("fulfillment")].isNull() && m_fulfillment_isValid;

    m_insert_isValid = ::OpenAPI::fromJsonValue(m_insert, json[QString("insert")]);
    m_insert_isSet = !json[QString("insert")].isNull() && m_insert_isValid;

    m_kitting_isValid = ::OpenAPI::fromJsonValue(m_kitting, json[QString("kitting")]);
    m_kitting_isSet = !json[QString("kitting")].isNull() && m_kitting_isValid;

    m_picking_isValid = ::OpenAPI::fromJsonValue(m_picking, json[QString("picking")]);
    m_picking_isSet = !json[QString("picking")].isNull() && m_picking_isValid;

    m_postage_isValid = ::OpenAPI::fromJsonValue(m_postage, json[QString("postage")]);
    m_postage_isSet = !json[QString("postage")].isNull() && m_postage_isValid;

    m_print_isValid = ::OpenAPI::fromJsonValue(m_print, json[QString("print")]);
    m_print_isSet = !json[QString("print")].isNull() && m_print_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;
}

QString OAIAccounting_v2_fees::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAccounting_v2_fees::asJsonObject() const {
    QJsonObject obj;
    if (m_box_isSet) {
        obj.insert(QString("box"), ::OpenAPI::toJsonValue(m_box));
    }
    if (m_envelope_isSet) {
        obj.insert(QString("envelope"), ::OpenAPI::toJsonValue(m_envelope));
    }
    if (m_fulfillment_isSet) {
        obj.insert(QString("fulfillment"), ::OpenAPI::toJsonValue(m_fulfillment));
    }
    if (m_insert_isSet) {
        obj.insert(QString("insert"), ::OpenAPI::toJsonValue(m_insert));
    }
    if (m_kitting_isSet) {
        obj.insert(QString("kitting"), ::OpenAPI::toJsonValue(m_kitting));
    }
    if (m_picking_isSet) {
        obj.insert(QString("picking"), ::OpenAPI::toJsonValue(m_picking));
    }
    if (m_postage_isSet) {
        obj.insert(QString("postage"), ::OpenAPI::toJsonValue(m_postage));
    }
    if (m_print_isSet) {
        obj.insert(QString("print"), ::OpenAPI::toJsonValue(m_print));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    return obj;
}

float OAIAccounting_v2_fees::getBox() const {
    return m_box;
}
void OAIAccounting_v2_fees::setBox(const float &box) {
    m_box = box;
    m_box_isSet = true;
}

bool OAIAccounting_v2_fees::is_box_Set() const{
    return m_box_isSet;
}

bool OAIAccounting_v2_fees::is_box_Valid() const{
    return m_box_isValid;
}

float OAIAccounting_v2_fees::getEnvelope() const {
    return m_envelope;
}
void OAIAccounting_v2_fees::setEnvelope(const float &envelope) {
    m_envelope = envelope;
    m_envelope_isSet = true;
}

bool OAIAccounting_v2_fees::is_envelope_Set() const{
    return m_envelope_isSet;
}

bool OAIAccounting_v2_fees::is_envelope_Valid() const{
    return m_envelope_isValid;
}

float OAIAccounting_v2_fees::getFulfillment() const {
    return m_fulfillment;
}
void OAIAccounting_v2_fees::setFulfillment(const float &fulfillment) {
    m_fulfillment = fulfillment;
    m_fulfillment_isSet = true;
}

bool OAIAccounting_v2_fees::is_fulfillment_Set() const{
    return m_fulfillment_isSet;
}

bool OAIAccounting_v2_fees::is_fulfillment_Valid() const{
    return m_fulfillment_isValid;
}

float OAIAccounting_v2_fees::getInsert() const {
    return m_insert;
}
void OAIAccounting_v2_fees::setInsert(const float &insert) {
    m_insert = insert;
    m_insert_isSet = true;
}

bool OAIAccounting_v2_fees::is_insert_Set() const{
    return m_insert_isSet;
}

bool OAIAccounting_v2_fees::is_insert_Valid() const{
    return m_insert_isValid;
}

float OAIAccounting_v2_fees::getKitting() const {
    return m_kitting;
}
void OAIAccounting_v2_fees::setKitting(const float &kitting) {
    m_kitting = kitting;
    m_kitting_isSet = true;
}

bool OAIAccounting_v2_fees::is_kitting_Set() const{
    return m_kitting_isSet;
}

bool OAIAccounting_v2_fees::is_kitting_Valid() const{
    return m_kitting_isValid;
}

float OAIAccounting_v2_fees::getPicking() const {
    return m_picking;
}
void OAIAccounting_v2_fees::setPicking(const float &picking) {
    m_picking = picking;
    m_picking_isSet = true;
}

bool OAIAccounting_v2_fees::is_picking_Set() const{
    return m_picking_isSet;
}

bool OAIAccounting_v2_fees::is_picking_Valid() const{
    return m_picking_isValid;
}

float OAIAccounting_v2_fees::getPostage() const {
    return m_postage;
}
void OAIAccounting_v2_fees::setPostage(const float &postage) {
    m_postage = postage;
    m_postage_isSet = true;
}

bool OAIAccounting_v2_fees::is_postage_Set() const{
    return m_postage_isSet;
}

bool OAIAccounting_v2_fees::is_postage_Valid() const{
    return m_postage_isValid;
}

float OAIAccounting_v2_fees::getPrint() const {
    return m_print;
}
void OAIAccounting_v2_fees::setPrint(const float &print) {
    m_print = print;
    m_print_isSet = true;
}

bool OAIAccounting_v2_fees::is_print_Set() const{
    return m_print_isSet;
}

bool OAIAccounting_v2_fees::is_print_Valid() const{
    return m_print_isValid;
}

float OAIAccounting_v2_fees::getTotal() const {
    return m_total;
}
void OAIAccounting_v2_fees::setTotal(const float &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAIAccounting_v2_fees::is_total_Set() const{
    return m_total_isSet;
}

bool OAIAccounting_v2_fees::is_total_Valid() const{
    return m_total_isValid;
}

bool OAIAccounting_v2_fees::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_box_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_envelope_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fulfillment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_insert_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_kitting_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_picking_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_postage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_print_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAccounting_v2_fees::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
