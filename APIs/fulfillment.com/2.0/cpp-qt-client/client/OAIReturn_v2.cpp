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

#include "OAIReturn_v2.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIReturn_v2::OAIReturn_v2(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIReturn_v2::OAIReturn_v2() {
    this->initializeModel();
}

OAIReturn_v2::~OAIReturn_v2() {}

void OAIReturn_v2::initializeModel() {

    m_comments_isSet = false;
    m_comments_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_order_isSet = false;
    m_order_isValid = false;

    m_reason_isSet = false;
    m_reason_isValid = false;

    m_returned_by_isSet = false;
    m_returned_by_isValid = false;

    m_rma_items_isSet = false;
    m_rma_items_isValid = false;

    m_rma_number_isSet = false;
    m_rma_number_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_updated_by_isSet = false;
    m_updated_by_isValid = false;
}

void OAIReturn_v2::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIReturn_v2::fromJsonObject(QJsonObject json) {

    m_comments_isValid = ::OpenAPI::fromJsonValue(m_comments, json[QString("comments")]);
    m_comments_isSet = !json[QString("comments")].isNull() && m_comments_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("createdBy")]);
    m_created_by_isSet = !json[QString("createdBy")].isNull() && m_created_by_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_order_isValid = ::OpenAPI::fromJsonValue(m_order, json[QString("order")]);
    m_order_isSet = !json[QString("order")].isNull() && m_order_isValid;

    m_reason_isValid = ::OpenAPI::fromJsonValue(m_reason, json[QString("reason")]);
    m_reason_isSet = !json[QString("reason")].isNull() && m_reason_isValid;

    m_returned_by_isValid = ::OpenAPI::fromJsonValue(m_returned_by, json[QString("returnedBy")]);
    m_returned_by_isSet = !json[QString("returnedBy")].isNull() && m_returned_by_isValid;

    m_rma_items_isValid = ::OpenAPI::fromJsonValue(m_rma_items, json[QString("rmaItems")]);
    m_rma_items_isSet = !json[QString("rmaItems")].isNull() && m_rma_items_isValid;

    m_rma_number_isValid = ::OpenAPI::fromJsonValue(m_rma_number, json[QString("rmaNumber")]);
    m_rma_number_isSet = !json[QString("rmaNumber")].isNull() && m_rma_number_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;

    m_updated_by_isValid = ::OpenAPI::fromJsonValue(m_updated_by, json[QString("updatedBy")]);
    m_updated_by_isSet = !json[QString("updatedBy")].isNull() && m_updated_by_isValid;
}

QString OAIReturn_v2::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIReturn_v2::asJsonObject() const {
    QJsonObject obj;
    if (m_comments_isSet) {
        obj.insert(QString("comments"), ::OpenAPI::toJsonValue(m_comments));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_created_by.isSet()) {
        obj.insert(QString("createdBy"), ::OpenAPI::toJsonValue(m_created_by));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_order.isSet()) {
        obj.insert(QString("order"), ::OpenAPI::toJsonValue(m_order));
    }
    if (m_reason.isSet()) {
        obj.insert(QString("reason"), ::OpenAPI::toJsonValue(m_reason));
    }
    if (m_returned_by_isSet) {
        obj.insert(QString("returnedBy"), ::OpenAPI::toJsonValue(m_returned_by));
    }
    if (m_rma_items.size() > 0) {
        obj.insert(QString("rmaItems"), ::OpenAPI::toJsonValue(m_rma_items));
    }
    if (m_rma_number_isSet) {
        obj.insert(QString("rmaNumber"), ::OpenAPI::toJsonValue(m_rma_number));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_updated_by.isSet()) {
        obj.insert(QString("updatedBy"), ::OpenAPI::toJsonValue(m_updated_by));
    }
    return obj;
}

QString OAIReturn_v2::getComments() const {
    return m_comments;
}
void OAIReturn_v2::setComments(const QString &comments) {
    m_comments = comments;
    m_comments_isSet = true;
}

bool OAIReturn_v2::is_comments_Set() const{
    return m_comments_isSet;
}

bool OAIReturn_v2::is_comments_Valid() const{
    return m_comments_isValid;
}

QDateTime OAIReturn_v2::getCreatedAt() const {
    return m_created_at;
}
void OAIReturn_v2::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIReturn_v2::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIReturn_v2::is_created_at_Valid() const{
    return m_created_at_isValid;
}

OAIObject OAIReturn_v2::getCreatedBy() const {
    return m_created_by;
}
void OAIReturn_v2::setCreatedBy(const OAIObject &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIReturn_v2::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIReturn_v2::is_created_by_Valid() const{
    return m_created_by_isValid;
}

qint32 OAIReturn_v2::getId() const {
    return m_id;
}
void OAIReturn_v2::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIReturn_v2::is_id_Set() const{
    return m_id_isSet;
}

bool OAIReturn_v2::is_id_Valid() const{
    return m_id_isValid;
}

OAIReturn_v2_order OAIReturn_v2::getOrder() const {
    return m_order;
}
void OAIReturn_v2::setOrder(const OAIReturn_v2_order &order) {
    m_order = order;
    m_order_isSet = true;
}

bool OAIReturn_v2::is_order_Set() const{
    return m_order_isSet;
}

bool OAIReturn_v2::is_order_Valid() const{
    return m_order_isValid;
}

OAIReturn_v2_reason OAIReturn_v2::getReason() const {
    return m_reason;
}
void OAIReturn_v2::setReason(const OAIReturn_v2_reason &reason) {
    m_reason = reason;
    m_reason_isSet = true;
}

bool OAIReturn_v2::is_reason_Set() const{
    return m_reason_isSet;
}

bool OAIReturn_v2::is_reason_Valid() const{
    return m_reason_isValid;
}

QString OAIReturn_v2::getReturnedBy() const {
    return m_returned_by;
}
void OAIReturn_v2::setReturnedBy(const QString &returned_by) {
    m_returned_by = returned_by;
    m_returned_by_isSet = true;
}

bool OAIReturn_v2::is_returned_by_Set() const{
    return m_returned_by_isSet;
}

bool OAIReturn_v2::is_returned_by_Valid() const{
    return m_returned_by_isValid;
}

QList<OAIRmaItem_v2> OAIReturn_v2::getRmaItems() const {
    return m_rma_items;
}
void OAIReturn_v2::setRmaItems(const QList<OAIRmaItem_v2> &rma_items) {
    m_rma_items = rma_items;
    m_rma_items_isSet = true;
}

bool OAIReturn_v2::is_rma_items_Set() const{
    return m_rma_items_isSet;
}

bool OAIReturn_v2::is_rma_items_Valid() const{
    return m_rma_items_isValid;
}

QString OAIReturn_v2::getRmaNumber() const {
    return m_rma_number;
}
void OAIReturn_v2::setRmaNumber(const QString &rma_number) {
    m_rma_number = rma_number;
    m_rma_number_isSet = true;
}

bool OAIReturn_v2::is_rma_number_Set() const{
    return m_rma_number_isSet;
}

bool OAIReturn_v2::is_rma_number_Valid() const{
    return m_rma_number_isValid;
}

OAIReturn_v2_reason OAIReturn_v2::getStatus() const {
    return m_status;
}
void OAIReturn_v2::setStatus(const OAIReturn_v2_reason &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIReturn_v2::is_status_Set() const{
    return m_status_isSet;
}

bool OAIReturn_v2::is_status_Valid() const{
    return m_status_isValid;
}

QDateTime OAIReturn_v2::getUpdatedAt() const {
    return m_updated_at;
}
void OAIReturn_v2::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIReturn_v2::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIReturn_v2::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

OAIUser_v2 OAIReturn_v2::getUpdatedBy() const {
    return m_updated_by;
}
void OAIReturn_v2::setUpdatedBy(const OAIUser_v2 &updated_by) {
    m_updated_by = updated_by;
    m_updated_by_isSet = true;
}

bool OAIReturn_v2::is_updated_by_Set() const{
    return m_updated_by_isSet;
}

bool OAIReturn_v2::is_updated_by_Valid() const{
    return m_updated_by_isValid;
}

bool OAIReturn_v2::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_comments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_by.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_returned_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rma_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_rma_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_by.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIReturn_v2::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_created_at_isValid && m_created_by_isValid && m_id_isValid && m_reason_isValid && m_status_isValid && m_updated_at_isValid && m_updated_by_isValid && true;
}

} // namespace OpenAPI
