/**
 * Pims
 *  Hereafter is the documentation of the private API of [Pims: Pointages Intelligents pour le Monde du Spectacle](https://pims.io). This API is designed for 3rd-party softwares, editors and partners. Its main purpose is to give access the core data of a Pims customer (i.e. events, ticket counts and promotions).  ## Authentication The API uses [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), meaning you will need a username and password to get authorized.  As each customer in Pims has its own domain (e.g. caramba.pims.io, gdp.pims.io...), each credentials will be valid for one domain/customer only. If you need dedicated credentials for one domain, please contact us. (In any case, we will need an explicit agreement from the customer before we create these credentials.)  <div class=\"info\"> To make your life easy, you can try all endpoints with the public credentials below, pointing to our [demo domain](https://demo.pims.io):   <ul>     <li>Base path: `https://demo.pims.io/api`</li>     <li>Username: `demo`</li>     <li>Password: `q83792db2GCvgYVdKpU3yG3R`</li>   </ul> </div>  ## Response format The API returns JSON and matches the [HAL specification](http://stateless.co/hal_specification.html). The `Content-Type` of each response will be `application/hal+json`, unless an error occurs.  Please note that this documentation describes all responses “as if” they were plain JSON. The specificities of HAL are ignored on purpose, in order to remain compact and avoid repetition. <div style=\"-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;\">  <div style=\"display: inline-block; width:100%;\">   <strong>So when you read in the doc:</strong> <pre><code class=\"lang-json\">{  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,  <span class=\"token string\">\"property1\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,  <span class=\"token string\">\"object\"</span>: {   <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,   <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>  } }</code></pre>  </div>  <div style=\"display: inline-block; width:100%;\">   <strong>... you'll get in the Real World®:</strong> <pre><code class=\"lang-json\">{  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,  <span class=\"token string\">\"property2\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,  <span class=\"token string\">\"_embedded\"</span>: {   <span class=\"token string\">\"object\"</span>: {    <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,    <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>,    <span class=\"token string\">\"_links\"</span>: {     <span class=\"token string\">\"self\"</span>: {      <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/other-item/456\"</span>     }    }   }  }  <span class=\"token string\">\"_links\"</span>: {   <span class=\"token string\">\"self\"</span>: {    <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/item/123\"</span>   }  } }</code></pre>  </div> </div>  ### Errors Errors return JSON too and tries to match the [Problem Details for HTTP APIs specification](https://tools.ietf.org/html/rfc7807). If it does not match this spec, that's either a bug or a compatibility issue. Please contact us to solve the problem.  The `Content-Type` of errors will be `application/problem+json`. The content will match the following JSON: ```json {  \"type\": \"https://tools.ietf.org/html/rfc2616#section-10\",     \"title\": \"Not Found\",  \"status\": 404,     \"detail\": \"Entity not found\" } ```  ## Versioning The API is fully versionned, using an URL-versioning scheme: `https://demo.pims.io/api/v1/events`, `https://demo.pims.io/api/v2/events`,...  The version part of the URL is optional, and will be completed with the last stable version if omitted.  ## Pagination All responses corresponding to a collection of resources (e.g. `/venues` or `/series/:id/events`) are paginated. When so, you will only get the first 25 resources you asked for.  If you need to get more resources in one call, you can use the `page_size` query parameter. E.g. `/venues?page_size=50` to get the 50 first venues.  Also note that with HAL, the navigation in paginated responses is a piece of cake, as you can see below: ```json {  \"_links\": {   \"self\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=1\"   },   \"first\": {    \"href\": \"https://demo.pims.io/api/v1/events\"   },   \"last\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=14\"   },   \"next\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=2\"   }  },  \"_embedded\": {    ... // data content goes here  },  \"page_count\": 14,  \"page_size\": 25,  \"total_items\": 331,  \"page\": 1 } ```  ## Filtering and sorting Every textual filter (e.g. `/events?label=U2`) and/or sort (e.g. `/events?sort=label`) performed with the API uses UTF8_UNICODE_CI collation, meaning it is: - Case insensitive: “Chloé” will be considered the same as “CHLOÉ”; - Diacritic insensitive: “Chloé” will be considered the same as “Chloe”.  When performing a sort, it will always be *ascending* by default. To make it *descending*, just use a minus sign (`-`) in front of the parameter value (e.g. `/events?sort=-label`).  ## I18n In responses, some labels can be translated (e.g. promotion types, event input types, etc.). These translatable labels are clearly indicated in the documentation below.  By default, they will be displayed in English, but you can change this behaviour via the `Accept-Language` header. E.g., use `fr` as a value for French.  ## PHP SDK We provide a simple yet convenient SDK for the PHP language, see [the Github page of the project](https://github.com/pimssas/pims-api-client-php).  ## And now? Generaly, you will start by [fetching one or more events](#tag/Events). An <span class=\"definition\">event</span> can be anything that occurs in one venue at one given date and time: a concert, a play, a match, a conference, etc. Additionnally, you can explore the [series](#tag/Series): a <span class=\"definition\">series</span> is just a group of events (e.g. a tour or a festival).  Once you retrieved the events you were interested in, you can look for the sales (<span class=\"definition\">ticket counts</span>): - Get a quick overview with [`/events/:id/ticket-counts`](#operation/fetchAllTicketCounts) - Or get a full insight by calling these endpoints:     1. [`/events/:id/categories`](#operation/fetchAllEventsCategories)     2. [`/events/:id/channels`](#operation/fetchAllEventsChannels)     3. [`/events/:id/ticket-counts/detailed`](#operation/fetchAllDetailedTicketCounts)  Eventually, you may also want to fetch the [promotions](#tag/Promotions). A <span class=\"definition\">promotion</span> can be anything meant to leverage the sales: ads, marketing campaigns, buzz or news around the event, etc. A promotion can be linked to any combination of events and/or series.
 *
 * The version of the OpenAPI document: 1.0
 * Contact: support@pims.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEventsEntity.h
 *
 * 
 */

#ifndef OAIEventsEntity_H
#define OAIEventsEntity_H

#include <QJsonObject>

#include "OAIEventsEntity_contract.h"
#include "OAIEventsEntity_input_type.h"
#include "OAIVenuesEntity.h"
#include <QDate>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIEventsEntity_contract;
class OAIEventsEntity_input_type;
class OAIVenuesEntity;

class OAIEventsEntity : public OAIObject {
public:
    OAIEventsEntity();
    OAIEventsEntity(QString json);
    ~OAIEventsEntity() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getBreakEven() const;
    void setBreakEven(const qint32 &break_even);
    bool is_break_even_Set() const;
    bool is_break_even_Valid() const;

    QDate getCancellationDate() const;
    void setCancellationDate(const QDate &cancellation_date);
    bool is_cancellation_date_Set() const;
    bool is_cancellation_date_Valid() const;

    OAIEventsEntity_contract getContract() const;
    void setContract(const OAIEventsEntity_contract &contract);
    bool is_contract_Set() const;
    bool is_contract_Valid() const;

    qint32 getCostingCapacity() const;
    void setCostingCapacity(const qint32 &costing_capacity);
    bool is_costing_capacity_Set() const;
    bool is_costing_capacity_Valid() const;

    qint64 getCreationTimestamp() const;
    void setCreationTimestamp(const qint64 &creation_timestamp);
    bool is_creation_timestamp_Set() const;
    bool is_creation_timestamp_Valid() const;

    QString getCurrency() const;
    void setCurrency(const QString &currency);
    bool is_currency_Set() const;
    bool is_currency_Valid() const;

    QString getDatetime() const;
    void setDatetime(const QString &datetime);
    bool is_datetime_Set() const;
    bool is_datetime_Valid() const;

    bool isFree() const;
    void setFree(const bool &free);
    bool is_free_Set() const;
    bool is_free_Valid() const;

    QDate getGeneralSalesDate() const;
    void setGeneralSalesDate(const QDate &general_sales_date);
    bool is_general_sales_date_Set() const;
    bool is_general_sales_date_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAIEventsEntity_input_type getInputType() const;
    void setInputType(const OAIEventsEntity_input_type &input_type);
    bool is_input_type_Set() const;
    bool is_input_type_Valid() const;

    QString getLabel() const;
    void setLabel(const QString &label);
    bool is_label_Set() const;
    bool is_label_Valid() const;

    qint64 getLastUpdateTimestamp() const;
    void setLastUpdateTimestamp(const qint64 &last_update_timestamp);
    bool is_last_update_timestamp_Set() const;
    bool is_last_update_timestamp_Valid() const;

    qint32 getMaxCapacity() const;
    void setMaxCapacity(const qint32 &max_capacity);
    bool is_max_capacity_Set() const;
    bool is_max_capacity_Valid() const;

    QDate getPresalesDate() const;
    void setPresalesDate(const QDate &presales_date);
    bool is_presales_date_Set() const;
    bool is_presales_date_Valid() const;

    qint32 getSeriesId() const;
    void setSeriesId(const qint32 &series_id);
    bool is_series_id_Set() const;
    bool is_series_id_Valid() const;

    QDate getSoldOutDate() const;
    void setSoldOutDate(const QDate &sold_out_date);
    bool is_sold_out_date_Set() const;
    bool is_sold_out_date_Valid() const;

    OAIVenuesEntity getVenue() const;
    void setVenue(const OAIVenuesEntity &venue);
    bool is_venue_Set() const;
    bool is_venue_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_break_even;
    bool m_break_even_isSet;
    bool m_break_even_isValid;

    QDate m_cancellation_date;
    bool m_cancellation_date_isSet;
    bool m_cancellation_date_isValid;

    OAIEventsEntity_contract m_contract;
    bool m_contract_isSet;
    bool m_contract_isValid;

    qint32 m_costing_capacity;
    bool m_costing_capacity_isSet;
    bool m_costing_capacity_isValid;

    qint64 m_creation_timestamp;
    bool m_creation_timestamp_isSet;
    bool m_creation_timestamp_isValid;

    QString m_currency;
    bool m_currency_isSet;
    bool m_currency_isValid;

    QString m_datetime;
    bool m_datetime_isSet;
    bool m_datetime_isValid;

    bool m_free;
    bool m_free_isSet;
    bool m_free_isValid;

    QDate m_general_sales_date;
    bool m_general_sales_date_isSet;
    bool m_general_sales_date_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIEventsEntity_input_type m_input_type;
    bool m_input_type_isSet;
    bool m_input_type_isValid;

    QString m_label;
    bool m_label_isSet;
    bool m_label_isValid;

    qint64 m_last_update_timestamp;
    bool m_last_update_timestamp_isSet;
    bool m_last_update_timestamp_isValid;

    qint32 m_max_capacity;
    bool m_max_capacity_isSet;
    bool m_max_capacity_isValid;

    QDate m_presales_date;
    bool m_presales_date_isSet;
    bool m_presales_date_isValid;

    qint32 m_series_id;
    bool m_series_id_isSet;
    bool m_series_id_isValid;

    QDate m_sold_out_date;
    bool m_sold_out_date_isSet;
    bool m_sold_out_date_isValid;

    OAIVenuesEntity m_venue;
    bool m_venue_isSet;
    bool m_venue_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEventsEntity)

#endif // OAIEventsEntity_H
