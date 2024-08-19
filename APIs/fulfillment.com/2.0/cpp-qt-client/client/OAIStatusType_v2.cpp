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

#include "OAIStatusType_v2.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStatusType_v2::OAIStatusType_v2(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStatusType_v2::OAIStatusType_v2() {
    this->initializeModel();
}

OAIStatusType_v2::~OAIStatusType_v2() {}

void OAIStatusType_v2::initializeModel() {

    m_action_required_by_isSet = false;
    m_action_required_by_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;

    m_detail_isSet = false;
    m_detail_isValid = false;

    m_detail_code_isSet = false;
    m_detail_code_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_closed_isSet = false;
    m_is_closed_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_reason_isSet = false;
    m_reason_isValid = false;

    m_stage_isSet = false;
    m_stage_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;
}

void OAIStatusType_v2::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStatusType_v2::fromJsonObject(QJsonObject json) {

    m_action_required_by_isValid = ::OpenAPI::fromJsonValue(m_action_required_by, json[QString("actionRequiredBy")]);
    m_action_required_by_isSet = !json[QString("actionRequiredBy")].isNull() && m_action_required_by_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_detail_isValid = ::OpenAPI::fromJsonValue(m_detail, json[QString("detail")]);
    m_detail_isSet = !json[QString("detail")].isNull() && m_detail_isValid;

    m_detail_code_isValid = ::OpenAPI::fromJsonValue(m_detail_code, json[QString("detailCode")]);
    m_detail_code_isSet = !json[QString("detailCode")].isNull() && m_detail_code_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_closed_isValid = ::OpenAPI::fromJsonValue(m_is_closed, json[QString("isClosed")]);
    m_is_closed_isSet = !json[QString("isClosed")].isNull() && m_is_closed_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_reason_isValid = ::OpenAPI::fromJsonValue(m_reason, json[QString("reason")]);
    m_reason_isSet = !json[QString("reason")].isNull() && m_reason_isValid;

    m_stage_isValid = ::OpenAPI::fromJsonValue(m_stage, json[QString("stage")]);
    m_stage_isSet = !json[QString("stage")].isNull() && m_stage_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;
}

QString OAIStatusType_v2::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStatusType_v2::asJsonObject() const {
    QJsonObject obj;
    if (m_action_required_by.isSet()) {
        obj.insert(QString("actionRequiredBy"), ::OpenAPI::toJsonValue(m_action_required_by));
    }
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_detail_isSet) {
        obj.insert(QString("detail"), ::OpenAPI::toJsonValue(m_detail));
    }
    if (m_detail_code_isSet) {
        obj.insert(QString("detailCode"), ::OpenAPI::toJsonValue(m_detail_code));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_closed_isSet) {
        obj.insert(QString("isClosed"), ::OpenAPI::toJsonValue(m_is_closed));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_reason_isSet) {
        obj.insert(QString("reason"), ::OpenAPI::toJsonValue(m_reason));
    }
    if (m_stage.isSet()) {
        obj.insert(QString("stage"), ::OpenAPI::toJsonValue(m_stage));
    }
    if (m_state.isSet()) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    return obj;
}

OAIStatusType_v2_actionRequiredBy OAIStatusType_v2::getActionRequiredBy() const {
    return m_action_required_by;
}
void OAIStatusType_v2::setActionRequiredBy(const OAIStatusType_v2_actionRequiredBy &action_required_by) {
    m_action_required_by = action_required_by;
    m_action_required_by_isSet = true;
}

bool OAIStatusType_v2::is_action_required_by_Set() const{
    return m_action_required_by_isSet;
}

bool OAIStatusType_v2::is_action_required_by_Valid() const{
    return m_action_required_by_isValid;
}

QString OAIStatusType_v2::getCode() const {
    return m_code;
}
void OAIStatusType_v2::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIStatusType_v2::is_code_Set() const{
    return m_code_isSet;
}

bool OAIStatusType_v2::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIStatusType_v2::getDetail() const {
    return m_detail;
}
void OAIStatusType_v2::setDetail(const QString &detail) {
    m_detail = detail;
    m_detail_isSet = true;
}

bool OAIStatusType_v2::is_detail_Set() const{
    return m_detail_isSet;
}

bool OAIStatusType_v2::is_detail_Valid() const{
    return m_detail_isValid;
}

QString OAIStatusType_v2::getDetailCode() const {
    return m_detail_code;
}
void OAIStatusType_v2::setDetailCode(const QString &detail_code) {
    m_detail_code = detail_code;
    m_detail_code_isSet = true;
}

bool OAIStatusType_v2::is_detail_code_Set() const{
    return m_detail_code_isSet;
}

bool OAIStatusType_v2::is_detail_code_Valid() const{
    return m_detail_code_isValid;
}

qint32 OAIStatusType_v2::getId() const {
    return m_id;
}
void OAIStatusType_v2::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIStatusType_v2::is_id_Set() const{
    return m_id_isSet;
}

bool OAIStatusType_v2::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIStatusType_v2::isIsClosed() const {
    return m_is_closed;
}
void OAIStatusType_v2::setIsClosed(const bool &is_closed) {
    m_is_closed = is_closed;
    m_is_closed_isSet = true;
}

bool OAIStatusType_v2::is_is_closed_Set() const{
    return m_is_closed_isSet;
}

bool OAIStatusType_v2::is_is_closed_Valid() const{
    return m_is_closed_isValid;
}

QString OAIStatusType_v2::getName() const {
    return m_name;
}
void OAIStatusType_v2::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIStatusType_v2::is_name_Set() const{
    return m_name_isSet;
}

bool OAIStatusType_v2::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIStatusType_v2::getReason() const {
    return m_reason;
}
void OAIStatusType_v2::setReason(const QString &reason) {
    m_reason = reason;
    m_reason_isSet = true;
}

bool OAIStatusType_v2::is_reason_Set() const{
    return m_reason_isSet;
}

bool OAIStatusType_v2::is_reason_Valid() const{
    return m_reason_isValid;
}

OAIStatusType_v2_stage OAIStatusType_v2::getStage() const {
    return m_stage;
}
void OAIStatusType_v2::setStage(const OAIStatusType_v2_stage &stage) {
    m_stage = stage;
    m_stage_isSet = true;
}

bool OAIStatusType_v2::is_stage_Set() const{
    return m_stage_isSet;
}

bool OAIStatusType_v2::is_stage_Valid() const{
    return m_stage_isValid;
}

OAIStatusType_v2_stage OAIStatusType_v2::getState() const {
    return m_state;
}
void OAIStatusType_v2::setState(const OAIStatusType_v2_stage &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIStatusType_v2::is_state_Set() const{
    return m_state_isSet;
}

bool OAIStatusType_v2::is_state_Valid() const{
    return m_state_isValid;
}

bool OAIStatusType_v2::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_action_required_by.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_detail_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_detail_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_closed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stage.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_state.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStatusType_v2::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_code_isValid && m_detail_code_isValid && m_stage_isValid && m_state_isValid && true;
}

} // namespace OpenAPI
