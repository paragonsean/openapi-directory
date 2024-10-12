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

#include "OAIUserContact_v2.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserContact_v2::OAIUserContact_v2(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserContact_v2::OAIUserContact_v2() {
    this->initializeModel();
}

OAIUserContact_v2::~OAIUserContact_v2() {}

void OAIUserContact_v2::initializeModel() {

    m_api_key_isSet = false;
    m_api_key_isValid = false;

    m_contact_info_isSet = false;
    m_contact_info_isValid = false;

    m_create_date_isSet = false;
    m_create_date_isValid = false;

    m_dept_leader_isSet = false;
    m_dept_leader_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_merchant_isSet = false;
    m_merchant_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_updated_by_isSet = false;
    m_updated_by_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;
}

void OAIUserContact_v2::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserContact_v2::fromJsonObject(QJsonObject json) {

    m_api_key_isValid = ::OpenAPI::fromJsonValue(m_api_key, json[QString("apiKey")]);
    m_api_key_isSet = !json[QString("apiKey")].isNull() && m_api_key_isValid;

    m_contact_info_isValid = ::OpenAPI::fromJsonValue(m_contact_info, json[QString("contactInfo")]);
    m_contact_info_isSet = !json[QString("contactInfo")].isNull() && m_contact_info_isValid;

    m_create_date_isValid = ::OpenAPI::fromJsonValue(m_create_date, json[QString("createDate")]);
    m_create_date_isSet = !json[QString("createDate")].isNull() && m_create_date_isValid;

    m_dept_leader_isValid = ::OpenAPI::fromJsonValue(m_dept_leader, json[QString("deptLeader")]);
    m_dept_leader_isSet = !json[QString("deptLeader")].isNull() && m_dept_leader_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_merchant_isValid = ::OpenAPI::fromJsonValue(m_merchant, json[QString("merchant")]);
    m_merchant_isSet = !json[QString("merchant")].isNull() && m_merchant_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;

    m_updated_by_isValid = ::OpenAPI::fromJsonValue(m_updated_by, json[QString("updatedBy")]);
    m_updated_by_isSet = !json[QString("updatedBy")].isNull() && m_updated_by_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;
}

QString OAIUserContact_v2::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserContact_v2::asJsonObject() const {
    QJsonObject obj;
    if (m_api_key_isSet) {
        obj.insert(QString("apiKey"), ::OpenAPI::toJsonValue(m_api_key));
    }
    if (m_contact_info.isSet()) {
        obj.insert(QString("contactInfo"), ::OpenAPI::toJsonValue(m_contact_info));
    }
    if (m_create_date_isSet) {
        obj.insert(QString("createDate"), ::OpenAPI::toJsonValue(m_create_date));
    }
    if (m_dept_leader_isSet) {
        obj.insert(QString("deptLeader"), ::OpenAPI::toJsonValue(m_dept_leader));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_merchant.isSet()) {
        obj.insert(QString("merchant"), ::OpenAPI::toJsonValue(m_merchant));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_updated_by_isSet) {
        obj.insert(QString("updatedBy"), ::OpenAPI::toJsonValue(m_updated_by));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    return obj;
}

QString OAIUserContact_v2::getApiKey() const {
    return m_api_key;
}
void OAIUserContact_v2::setApiKey(const QString &api_key) {
    m_api_key = api_key;
    m_api_key_isSet = true;
}

bool OAIUserContact_v2::is_api_key_Set() const{
    return m_api_key_isSet;
}

bool OAIUserContact_v2::is_api_key_Valid() const{
    return m_api_key_isValid;
}

OAIUserContact_v2 OAIUserContact_v2::getContactInfo() const {
    return m_contact_info;
}
void OAIUserContact_v2::setContactInfo(const OAIUserContact_v2 &contact_info) {
    m_contact_info = contact_info;
    m_contact_info_isSet = true;
}

bool OAIUserContact_v2::is_contact_info_Set() const{
    return m_contact_info_isSet;
}

bool OAIUserContact_v2::is_contact_info_Valid() const{
    return m_contact_info_isValid;
}

QDateTime OAIUserContact_v2::getCreateDate() const {
    return m_create_date;
}
void OAIUserContact_v2::setCreateDate(const QDateTime &create_date) {
    m_create_date = create_date;
    m_create_date_isSet = true;
}

bool OAIUserContact_v2::is_create_date_Set() const{
    return m_create_date_isSet;
}

bool OAIUserContact_v2::is_create_date_Valid() const{
    return m_create_date_isValid;
}

bool OAIUserContact_v2::isDeptLeader() const {
    return m_dept_leader;
}
void OAIUserContact_v2::setDeptLeader(const bool &dept_leader) {
    m_dept_leader = dept_leader;
    m_dept_leader_isSet = true;
}

bool OAIUserContact_v2::is_dept_leader_Set() const{
    return m_dept_leader_isSet;
}

bool OAIUserContact_v2::is_dept_leader_Valid() const{
    return m_dept_leader_isValid;
}

qint32 OAIUserContact_v2::getId() const {
    return m_id;
}
void OAIUserContact_v2::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIUserContact_v2::is_id_Set() const{
    return m_id_isSet;
}

bool OAIUserContact_v2::is_id_Valid() const{
    return m_id_isValid;
}

OAIUserContact_v2_merchant OAIUserContact_v2::getMerchant() const {
    return m_merchant;
}
void OAIUserContact_v2::setMerchant(const OAIUserContact_v2_merchant &merchant) {
    m_merchant = merchant;
    m_merchant_isSet = true;
}

bool OAIUserContact_v2::is_merchant_Set() const{
    return m_merchant_isSet;
}

bool OAIUserContact_v2::is_merchant_Valid() const{
    return m_merchant_isValid;
}

QString OAIUserContact_v2::getName() const {
    return m_name;
}
void OAIUserContact_v2::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUserContact_v2::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUserContact_v2::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIUserContact_v2::isStatus() const {
    return m_status;
}
void OAIUserContact_v2::setStatus(const bool &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIUserContact_v2::is_status_Set() const{
    return m_status_isSet;
}

bool OAIUserContact_v2::is_status_Valid() const{
    return m_status_isValid;
}

QDateTime OAIUserContact_v2::getUpdatedAt() const {
    return m_updated_at;
}
void OAIUserContact_v2::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIUserContact_v2::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIUserContact_v2::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QDateTime OAIUserContact_v2::getUpdatedBy() const {
    return m_updated_by;
}
void OAIUserContact_v2::setUpdatedBy(const QDateTime &updated_by) {
    m_updated_by = updated_by;
    m_updated_by_isSet = true;
}

bool OAIUserContact_v2::is_updated_by_Set() const{
    return m_updated_by_isSet;
}

bool OAIUserContact_v2::is_updated_by_Valid() const{
    return m_updated_by_isValid;
}

QString OAIUserContact_v2::getUsername() const {
    return m_username;
}
void OAIUserContact_v2::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIUserContact_v2::is_username_Set() const{
    return m_username_isSet;
}

bool OAIUserContact_v2::is_username_Valid() const{
    return m_username_isValid;
}

bool OAIUserContact_v2::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_api_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_contact_info.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_create_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dept_leader_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_merchant.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_username_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserContact_v2::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && true;
}

} // namespace OpenAPI
