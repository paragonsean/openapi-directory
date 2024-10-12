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

#include "OAIFeature.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFeature::OAIFeature(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFeature::OAIFeature() {
    this->initializeModel();
}

OAIFeature::~OAIFeature() {}

void OAIFeature::initializeModel() {

    m_bbox_isSet = false;
    m_bbox_isValid = false;

    m_centerline_isSet = false;
    m_centerline_isValid = false;

    m_geometry_isSet = false;
    m_geometry_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIFeature::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFeature::fromJsonObject(QJsonObject json) {

    m_bbox_isValid = ::OpenAPI::fromJsonValue(m_bbox, json[QString("bbox")]);
    m_bbox_isSet = !json[QString("bbox")].isNull() && m_bbox_isValid;

    m_centerline_isValid = ::OpenAPI::fromJsonValue(m_centerline, json[QString("centerline")]);
    m_centerline_isSet = !json[QString("centerline")].isNull() && m_centerline_isValid;

    m_geometry_isValid = ::OpenAPI::fromJsonValue(m_geometry, json[QString("geometry")]);
    m_geometry_isSet = !json[QString("geometry")].isNull() && m_geometry_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIFeature::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFeature::asJsonObject() const {
    QJsonObject obj;
    if (m_bbox.size() > 0) {
        obj.insert(QString("bbox"), ::OpenAPI::toJsonValue(m_bbox));
    }
    if (m_centerline.isSet()) {
        obj.insert(QString("centerline"), ::OpenAPI::toJsonValue(m_centerline));
    }
    if (m_geometry.isSet()) {
        obj.insert(QString("geometry"), ::OpenAPI::toJsonValue(m_geometry));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QList<QJsonValue> OAIFeature::getBbox() const {
    return m_bbox;
}
void OAIFeature::setBbox(const QList<QJsonValue> &bbox) {
    m_bbox = bbox;
    m_bbox_isSet = true;
}

bool OAIFeature::is_bbox_Set() const{
    return m_bbox_isSet;
}

bool OAIFeature::is_bbox_Valid() const{
    return m_bbox_isValid;
}

OAIObject OAIFeature::getCenterline() const {
    return m_centerline;
}
void OAIFeature::setCenterline(const OAIObject &centerline) {
    m_centerline = centerline;
    m_centerline_isSet = true;
}

bool OAIFeature::is_centerline_Set() const{
    return m_centerline_isSet;
}

bool OAIFeature::is_centerline_Valid() const{
    return m_centerline_isValid;
}

OAIGeometry OAIFeature::getGeometry() const {
    return m_geometry;
}
void OAIFeature::setGeometry(const OAIGeometry &geometry) {
    m_geometry = geometry;
    m_geometry_isSet = true;
}

bool OAIFeature::is_geometry_Set() const{
    return m_geometry_isSet;
}

bool OAIFeature::is_geometry_Valid() const{
    return m_geometry_isValid;
}

qint32 OAIFeature::getId() const {
    return m_id;
}
void OAIFeature::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIFeature::is_id_Set() const{
    return m_id_isSet;
}

bool OAIFeature::is_id_Valid() const{
    return m_id_isValid;
}

OAIFeature_properties OAIFeature::getProperties() const {
    return m_properties;
}
void OAIFeature::setProperties(const OAIFeature_properties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIFeature::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIFeature::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAIFeature::getTitle() const {
    return m_title;
}
void OAIFeature::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIFeature::is_title_Set() const{
    return m_title_isSet;
}

bool OAIFeature::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIFeature::getType() const {
    return m_type;
}
void OAIFeature::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIFeature::is_type_Set() const{
    return m_type_isSet;
}

bool OAIFeature::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIFeature::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bbox.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_centerline.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_geometry.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFeature::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_geometry_isValid && m_properties_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
