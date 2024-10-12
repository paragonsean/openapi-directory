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

#include "OAIRmaItem_v2.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRmaItem_v2::OAIRmaItem_v2(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRmaItem_v2::OAIRmaItem_v2() {
    this->initializeModel();
}

OAIRmaItem_v2::~OAIRmaItem_v2() {}

void OAIRmaItem_v2::initializeModel() {

    m_comments_isSet = false;
    m_comments_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_item_isSet = false;
    m_item_isValid = false;

    m_non_restocked_reason_isSet = false;
    m_non_restocked_reason_isValid = false;

    m_quantity_expected_isSet = false;
    m_quantity_expected_isValid = false;

    m_quantity_restocked_isSet = false;
    m_quantity_restocked_isValid = false;

    m_quantity_returned_isSet = false;
    m_quantity_returned_isValid = false;

    m_quantity_shipped_isSet = false;
    m_quantity_shipped_isValid = false;
}

void OAIRmaItem_v2::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRmaItem_v2::fromJsonObject(QJsonObject json) {

    m_comments_isValid = ::OpenAPI::fromJsonValue(m_comments, json[QString("comments")]);
    m_comments_isSet = !json[QString("comments")].isNull() && m_comments_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_item_isValid = ::OpenAPI::fromJsonValue(m_item, json[QString("item")]);
    m_item_isSet = !json[QString("item")].isNull() && m_item_isValid;

    m_non_restocked_reason_isValid = ::OpenAPI::fromJsonValue(m_non_restocked_reason, json[QString("nonRestockedReason")]);
    m_non_restocked_reason_isSet = !json[QString("nonRestockedReason")].isNull() && m_non_restocked_reason_isValid;

    m_quantity_expected_isValid = ::OpenAPI::fromJsonValue(m_quantity_expected, json[QString("quantityExpected")]);
    m_quantity_expected_isSet = !json[QString("quantityExpected")].isNull() && m_quantity_expected_isValid;

    m_quantity_restocked_isValid = ::OpenAPI::fromJsonValue(m_quantity_restocked, json[QString("quantityRestocked")]);
    m_quantity_restocked_isSet = !json[QString("quantityRestocked")].isNull() && m_quantity_restocked_isValid;

    m_quantity_returned_isValid = ::OpenAPI::fromJsonValue(m_quantity_returned, json[QString("quantityReturned")]);
    m_quantity_returned_isSet = !json[QString("quantityReturned")].isNull() && m_quantity_returned_isValid;

    m_quantity_shipped_isValid = ::OpenAPI::fromJsonValue(m_quantity_shipped, json[QString("quantityShipped")]);
    m_quantity_shipped_isSet = !json[QString("quantityShipped")].isNull() && m_quantity_shipped_isValid;
}

QString OAIRmaItem_v2::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRmaItem_v2::asJsonObject() const {
    QJsonObject obj;
    if (m_comments_isSet) {
        obj.insert(QString("comments"), ::OpenAPI::toJsonValue(m_comments));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_item.isSet()) {
        obj.insert(QString("item"), ::OpenAPI::toJsonValue(m_item));
    }
    if (m_non_restocked_reason.isSet()) {
        obj.insert(QString("nonRestockedReason"), ::OpenAPI::toJsonValue(m_non_restocked_reason));
    }
    if (m_quantity_expected_isSet) {
        obj.insert(QString("quantityExpected"), ::OpenAPI::toJsonValue(m_quantity_expected));
    }
    if (m_quantity_restocked_isSet) {
        obj.insert(QString("quantityRestocked"), ::OpenAPI::toJsonValue(m_quantity_restocked));
    }
    if (m_quantity_returned_isSet) {
        obj.insert(QString("quantityReturned"), ::OpenAPI::toJsonValue(m_quantity_returned));
    }
    if (m_quantity_shipped_isSet) {
        obj.insert(QString("quantityShipped"), ::OpenAPI::toJsonValue(m_quantity_shipped));
    }
    return obj;
}

QString OAIRmaItem_v2::getComments() const {
    return m_comments;
}
void OAIRmaItem_v2::setComments(const QString &comments) {
    m_comments = comments;
    m_comments_isSet = true;
}

bool OAIRmaItem_v2::is_comments_Set() const{
    return m_comments_isSet;
}

bool OAIRmaItem_v2::is_comments_Valid() const{
    return m_comments_isValid;
}

qint32 OAIRmaItem_v2::getId() const {
    return m_id;
}
void OAIRmaItem_v2::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIRmaItem_v2::is_id_Set() const{
    return m_id_isSet;
}

bool OAIRmaItem_v2::is_id_Valid() const{
    return m_id_isValid;
}

OAIRmaItem_v2_item OAIRmaItem_v2::getItem() const {
    return m_item;
}
void OAIRmaItem_v2::setItem(const OAIRmaItem_v2_item &item) {
    m_item = item;
    m_item_isSet = true;
}

bool OAIRmaItem_v2::is_item_Set() const{
    return m_item_isSet;
}

bool OAIRmaItem_v2::is_item_Valid() const{
    return m_item_isValid;
}

OAIRmaItem_v2_nonRestockedReason OAIRmaItem_v2::getNonRestockedReason() const {
    return m_non_restocked_reason;
}
void OAIRmaItem_v2::setNonRestockedReason(const OAIRmaItem_v2_nonRestockedReason &non_restocked_reason) {
    m_non_restocked_reason = non_restocked_reason;
    m_non_restocked_reason_isSet = true;
}

bool OAIRmaItem_v2::is_non_restocked_reason_Set() const{
    return m_non_restocked_reason_isSet;
}

bool OAIRmaItem_v2::is_non_restocked_reason_Valid() const{
    return m_non_restocked_reason_isValid;
}

qint32 OAIRmaItem_v2::getQuantityExpected() const {
    return m_quantity_expected;
}
void OAIRmaItem_v2::setQuantityExpected(const qint32 &quantity_expected) {
    m_quantity_expected = quantity_expected;
    m_quantity_expected_isSet = true;
}

bool OAIRmaItem_v2::is_quantity_expected_Set() const{
    return m_quantity_expected_isSet;
}

bool OAIRmaItem_v2::is_quantity_expected_Valid() const{
    return m_quantity_expected_isValid;
}

qint32 OAIRmaItem_v2::getQuantityRestocked() const {
    return m_quantity_restocked;
}
void OAIRmaItem_v2::setQuantityRestocked(const qint32 &quantity_restocked) {
    m_quantity_restocked = quantity_restocked;
    m_quantity_restocked_isSet = true;
}

bool OAIRmaItem_v2::is_quantity_restocked_Set() const{
    return m_quantity_restocked_isSet;
}

bool OAIRmaItem_v2::is_quantity_restocked_Valid() const{
    return m_quantity_restocked_isValid;
}

qint32 OAIRmaItem_v2::getQuantityReturned() const {
    return m_quantity_returned;
}
void OAIRmaItem_v2::setQuantityReturned(const qint32 &quantity_returned) {
    m_quantity_returned = quantity_returned;
    m_quantity_returned_isSet = true;
}

bool OAIRmaItem_v2::is_quantity_returned_Set() const{
    return m_quantity_returned_isSet;
}

bool OAIRmaItem_v2::is_quantity_returned_Valid() const{
    return m_quantity_returned_isValid;
}

qint32 OAIRmaItem_v2::getQuantityShipped() const {
    return m_quantity_shipped;
}
void OAIRmaItem_v2::setQuantityShipped(const qint32 &quantity_shipped) {
    m_quantity_shipped = quantity_shipped;
    m_quantity_shipped_isSet = true;
}

bool OAIRmaItem_v2::is_quantity_shipped_Set() const{
    return m_quantity_shipped_isSet;
}

bool OAIRmaItem_v2::is_quantity_shipped_Valid() const{
    return m_quantity_shipped_isValid;
}

bool OAIRmaItem_v2::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_comments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_item.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_non_restocked_reason.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_expected_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_restocked_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_returned_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_shipped_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRmaItem_v2::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
