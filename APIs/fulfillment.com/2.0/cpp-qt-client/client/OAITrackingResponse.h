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

/*
 * OAITrackingResponse.h
 *
 * 
 */

#ifndef OAITrackingResponse_H
#define OAITrackingResponse_H

#include <QJsonObject>

#include "OAIFeature.h"
#include "OAIObject.h"
#include "OAITrackingEvent_v2.h"
#include "OAITrackingNumber_v2.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFeature;
class OAITrackingEvent_v2;
class OAITrackingNumber_v2;

class OAITrackingResponse : public OAIObject {
public:
    OAITrackingResponse();
    OAITrackingResponse(QString json);
    ~OAITrackingResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getDestination() const;
    void setDestination(const OAIObject &destination);
    bool is_destination_Set() const;
    bool is_destination_Valid() const;

    qint32 getFdcOrderId() const;
    void setFdcOrderId(const qint32 &fdc_order_id);
    bool is_fdc_order_id_Set() const;
    bool is_fdc_order_id_Valid() const;

    QDateTime getFirstCheckedDateTime() const;
    void setFirstCheckedDateTime(const QDateTime &first_checked_date_time);
    bool is_first_checked_date_time_Set() const;
    bool is_first_checked_date_time_Valid() const;

    QDateTime getFirstTransitEvent() const;
    void setFirstTransitEvent(const QDateTime &first_transit_event);
    bool is_first_transit_event_Set() const;
    bool is_first_transit_event_Valid() const;

    QDateTime getLastCheckedDateTime() const;
    void setLastCheckedDateTime(const QDateTime &last_checked_date_time);
    bool is_last_checked_date_time_Set() const;
    bool is_last_checked_date_time_Valid() const;

    QDateTime getLastUpdatedDateTime() const;
    void setLastUpdatedDateTime(const QDateTime &last_updated_date_time);
    bool is_last_updated_date_time_Set() const;
    bool is_last_updated_date_time_Valid() const;

    OAIFeature getOrigin() const;
    void setOrigin(const OAIFeature &origin);
    bool is_origin_Set() const;
    bool is_origin_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    qint32 getStatusCategoryCode() const;
    void setStatusCategoryCode(const qint32 &status_category_code);
    bool is_status_category_code_Set() const;
    bool is_status_category_code_Valid() const;

    QDateTime getStatusDateTime() const;
    void setStatusDateTime(const QDateTime &status_date_time);
    bool is_status_date_time_Set() const;
    bool is_status_date_time_Valid() const;

    QString getStatusMessage() const;
    void setStatusMessage(const QString &status_message);
    bool is_status_message_Set() const;
    bool is_status_message_Valid() const;

    QList<OAITrackingEvent_v2> getTrackedEvents() const;
    void setTrackedEvents(const QList<OAITrackingEvent_v2> &tracked_events);
    bool is_tracked_events_Set() const;
    bool is_tracked_events_Valid() const;

    OAITrackingNumber_v2 getTrackingNumber() const;
    void setTrackingNumber(const OAITrackingNumber_v2 &tracking_number);
    bool is_tracking_number_Set() const;
    bool is_tracking_number_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_destination;
    bool m_destination_isSet;
    bool m_destination_isValid;

    qint32 m_fdc_order_id;
    bool m_fdc_order_id_isSet;
    bool m_fdc_order_id_isValid;

    QDateTime m_first_checked_date_time;
    bool m_first_checked_date_time_isSet;
    bool m_first_checked_date_time_isValid;

    QDateTime m_first_transit_event;
    bool m_first_transit_event_isSet;
    bool m_first_transit_event_isValid;

    QDateTime m_last_checked_date_time;
    bool m_last_checked_date_time_isSet;
    bool m_last_checked_date_time_isValid;

    QDateTime m_last_updated_date_time;
    bool m_last_updated_date_time_isSet;
    bool m_last_updated_date_time_isValid;

    OAIFeature m_origin;
    bool m_origin_isSet;
    bool m_origin_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    qint32 m_status_category_code;
    bool m_status_category_code_isSet;
    bool m_status_category_code_isValid;

    QDateTime m_status_date_time;
    bool m_status_date_time_isSet;
    bool m_status_date_time_isValid;

    QString m_status_message;
    bool m_status_message_isSet;
    bool m_status_message_isValid;

    QList<OAITrackingEvent_v2> m_tracked_events;
    bool m_tracked_events_isSet;
    bool m_tracked_events_isValid;

    OAITrackingNumber_v2 m_tracking_number;
    bool m_tracking_number_isSet;
    bool m_tracking_number_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITrackingResponse)

#endif // OAITrackingResponse_H
