/**
 * Pricing Hub
 * > This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests).      In the B2B scenario, it is common for stores to have personalized prices per customer and complex pricing systems that require external integrations. Pricing Hub is a system developed for the B2B context that works as an intermediary between VTEX and external pricing systems.     In VTEX, B2B stores have the option to use our internal pricing system or an external one. If the store chooses to operate with an external pricing system, Pricing Hub will query an external price calculation API. The external API should then respond with the price for all items in the shopping cart according to its predefined tax rules.    ![Pricing hub protocal diagram](https://user-images.githubusercontent.com/77292838/211634260-e4f7a516-91df-416e-ab43-d9c79d56bc91.png)    ## Implementation    To connect with external pricing systems using Pricing Hub, it is necessary to build a VTEX IO middleware app. We offer two reference implementation templates to simplify this process:    - [C# template](https://github.com/vtex-apps/external-prices-app)  - [Node template](https://github.com/vtex-apps/external-prices-node)    Read the documentation on each repository to learn more about the required steps to use and customize the app.    > The app used by Pricing Hub to connect must be a `major 0`.     ## Specifications    See below all the specifications of the request and the response expected when communicating with Pricing Hub.    ### Price calculation request    The external prices calculation tool must provide an endpoint that will receive a `POST` [Get Prices](https://developers.vtex.com/docs/api-reference/pricing-hub#post-/api/pricing-hub/prices) request. This route retrieves and applies prices for the items that are passed in the request. Pricing Hub will select the pricing method that will be used for each item and will fetch their respective price from the selected pricing method.    >⚠️ Responses from Pricing Hub tend to have a greater delay when compared to other VTEX systems. That is expected, however, due to the complexity of its nested requests. The timeout for this request is 900 milliseconds.    In this request, Pricing Hub provides a body in a specific format, exemplified below. This means that either the endpoint must be prepared to receive this body format, or the app must contain a parser to adapt it to the correct format.    #### Request body example    ```json  {      \"item\":           {              \"index\": 0,              \"skuId\": \"880011\",              \"quantity\": 1          },      \"context\":{          \"email\": \"john@email.com\"      }  }  ```    The request body should have the following properties:    | **Attribute** | **Type** | **Description**                                                                                                                                                                                          |  |---------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  | `item`        | object   | The item whose price is supposed to be fetched by Pricing Hub.                                                                                                                                           |  | ↪ `index`     | integer  | This is the index of the item at Checkout's cart. It has to be unique in the items array.                                                                                                                |  | ↪ `skuId`     | string   | This is the SKU ID of the item that will be priced.                                                                                                                                                      |  | ↪ `quantity`  | integer  | This is the amount of items that will be priced. It is possible to have a volume discount for many repeated items. Hence, the price may not be the quantity of the item multiplied by the unitary price. |  | `context`     | object   | The object that contains the context to inform the query.                                                                                                                                                |  | ↪ `email`     | string   | The customer's email address. If there is no value, use an empty string.                                                                                                                                 |    ### External prices provider response    In response to the request sent by Pricing Hub, we expect an outcome in the following format:    ```json  {      \"item\": {          \"price\": 54035,          \"priceTables\": \"special\",          \"index\": 0,          \"skuId\": \"880011\",          \"listPrice\": 54035,          \"costPrice\": 50000,          \"sellingPrice\": 54035,          \"priceValidUntil\": \"2023-01-27T20:29:57Z\",          \"tradePolicyId\": \"special\"      }  }  ```    The response should have the following properties:    | **Attribute**       | **Type** | **Description**                                                                                                                                        |  |---------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|  | `item`              | object   | The object that contains the price data.                                                                                                               |  | ↪ `price`           | integer  | The price returned by the pricing API that was used by Pricing-Hub. It is measured in cents, so 5000 means 50,00 in local currency.                    |  | ↪ `priceTables`     | string   | The price table that was used to price the item.                                                                                                       |  | ↪ `index`           | integer  | The same index referring to Checkout's cart that was passed to the API.                                                                                |  | ↪ `skuId`           | string   | The same SKU ID that was passed to the API.                                                                                                            |  | ↪ `listPrice`       | integer  | The list price returned by the pricing API that was used by Pricing Hub. It is measured in cents, so 5000 means 50,00 in local currency.               |  | ↪ `costPrice`       | integer  | The cost price returned by the pricing API that was used by Pricing-Hub. It is measured in cents, so 5000 means 50,00 in local currency.               |  | ↪ `sellingPrice`    | integer  | The computed price before applying coupons, taxes or promotions.                                                                                       |  | ↪ `priceValidUntil` | string   | The moment up until the price is valid. After that moment, it will be necessary to call the pricing API again. The format of the string is in RFC3339. |  | ↪ `tradePolicyId`   | string   | Trade Policy ID.                                                                                                                                       |    ## Index - Pricing Hub API    `POST` [Get Prices](https://developers.vtex.com/docs/api-reference/pricing-hub#post-/api/pricing-hub/prices)  `PUT` [Configure External Price Source](https://developers.vtex.com/docs/api-reference/pricing-hub#put-/config)  
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetPricesRequestObject.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetPricesRequestObject::OAIGetPricesRequestObject(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetPricesRequestObject::OAIGetPricesRequestObject() {
    this->initializeModel();
}

OAIGetPricesRequestObject::~OAIGetPricesRequestObject() {}

void OAIGetPricesRequestObject::initializeModel() {

    m_utm_campaign_isSet = false;
    m_utm_campaign_isValid = false;

    m_utm_internal_campaign_isSet = false;
    m_utm_internal_campaign_isValid = false;

    m_utm_medium_isSet = false;
    m_utm_medium_isValid = false;

    m_utm_source_isSet = false;
    m_utm_source_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_items_isSet = false;
    m_items_isValid = false;

    m_sales_channel_isSet = false;
    m_sales_channel_isValid = false;
}

void OAIGetPricesRequestObject::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetPricesRequestObject::fromJsonObject(QJsonObject json) {

    m_utm_campaign_isValid = ::OpenAPI::fromJsonValue(m_utm_campaign, json[QString("UtmCampaign")]);
    m_utm_campaign_isSet = !json[QString("UtmCampaign")].isNull() && m_utm_campaign_isValid;

    m_utm_internal_campaign_isValid = ::OpenAPI::fromJsonValue(m_utm_internal_campaign, json[QString("UtmInternalCampaign")]);
    m_utm_internal_campaign_isSet = !json[QString("UtmInternalCampaign")].isNull() && m_utm_internal_campaign_isValid;

    m_utm_medium_isValid = ::OpenAPI::fromJsonValue(m_utm_medium, json[QString("UtmMedium")]);
    m_utm_medium_isSet = !json[QString("UtmMedium")].isNull() && m_utm_medium_isValid;

    m_utm_source_isValid = ::OpenAPI::fromJsonValue(m_utm_source, json[QString("UtmSource")]);
    m_utm_source_isSet = !json[QString("UtmSource")].isNull() && m_utm_source_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;

    m_sales_channel_isValid = ::OpenAPI::fromJsonValue(m_sales_channel, json[QString("salesChannel")]);
    m_sales_channel_isSet = !json[QString("salesChannel")].isNull() && m_sales_channel_isValid;
}

QString OAIGetPricesRequestObject::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetPricesRequestObject::asJsonObject() const {
    QJsonObject obj;
    if (m_utm_campaign_isSet) {
        obj.insert(QString("UtmCampaign"), ::OpenAPI::toJsonValue(m_utm_campaign));
    }
    if (m_utm_internal_campaign_isSet) {
        obj.insert(QString("UtmInternalCampaign"), ::OpenAPI::toJsonValue(m_utm_internal_campaign));
    }
    if (m_utm_medium_isSet) {
        obj.insert(QString("UtmMedium"), ::OpenAPI::toJsonValue(m_utm_medium));
    }
    if (m_utm_source_isSet) {
        obj.insert(QString("UtmSource"), ::OpenAPI::toJsonValue(m_utm_source));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_sales_channel_isSet) {
        obj.insert(QString("salesChannel"), ::OpenAPI::toJsonValue(m_sales_channel));
    }
    return obj;
}

QString OAIGetPricesRequestObject::getUtmCampaign() const {
    return m_utm_campaign;
}
void OAIGetPricesRequestObject::setUtmCampaign(const QString &utm_campaign) {
    m_utm_campaign = utm_campaign;
    m_utm_campaign_isSet = true;
}

bool OAIGetPricesRequestObject::is_utm_campaign_Set() const{
    return m_utm_campaign_isSet;
}

bool OAIGetPricesRequestObject::is_utm_campaign_Valid() const{
    return m_utm_campaign_isValid;
}

QString OAIGetPricesRequestObject::getUtmInternalCampaign() const {
    return m_utm_internal_campaign;
}
void OAIGetPricesRequestObject::setUtmInternalCampaign(const QString &utm_internal_campaign) {
    m_utm_internal_campaign = utm_internal_campaign;
    m_utm_internal_campaign_isSet = true;
}

bool OAIGetPricesRequestObject::is_utm_internal_campaign_Set() const{
    return m_utm_internal_campaign_isSet;
}

bool OAIGetPricesRequestObject::is_utm_internal_campaign_Valid() const{
    return m_utm_internal_campaign_isValid;
}

QString OAIGetPricesRequestObject::getUtmMedium() const {
    return m_utm_medium;
}
void OAIGetPricesRequestObject::setUtmMedium(const QString &utm_medium) {
    m_utm_medium = utm_medium;
    m_utm_medium_isSet = true;
}

bool OAIGetPricesRequestObject::is_utm_medium_Set() const{
    return m_utm_medium_isSet;
}

bool OAIGetPricesRequestObject::is_utm_medium_Valid() const{
    return m_utm_medium_isValid;
}

QString OAIGetPricesRequestObject::getUtmSource() const {
    return m_utm_source;
}
void OAIGetPricesRequestObject::setUtmSource(const QString &utm_source) {
    m_utm_source = utm_source;
    m_utm_source_isSet = true;
}

bool OAIGetPricesRequestObject::is_utm_source_Set() const{
    return m_utm_source_isSet;
}

bool OAIGetPricesRequestObject::is_utm_source_Valid() const{
    return m_utm_source_isValid;
}

QString OAIGetPricesRequestObject::getEmail() const {
    return m_email;
}
void OAIGetPricesRequestObject::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIGetPricesRequestObject::is_email_Set() const{
    return m_email_isSet;
}

bool OAIGetPricesRequestObject::is_email_Valid() const{
    return m_email_isValid;
}

QList<OAIItems_inner> OAIGetPricesRequestObject::getItems() const {
    return m_items;
}
void OAIGetPricesRequestObject::setItems(const QList<OAIItems_inner> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIGetPricesRequestObject::is_items_Set() const{
    return m_items_isSet;
}

bool OAIGetPricesRequestObject::is_items_Valid() const{
    return m_items_isValid;
}

QString OAIGetPricesRequestObject::getSalesChannel() const {
    return m_sales_channel;
}
void OAIGetPricesRequestObject::setSalesChannel(const QString &sales_channel) {
    m_sales_channel = sales_channel;
    m_sales_channel_isSet = true;
}

bool OAIGetPricesRequestObject::is_sales_channel_Set() const{
    return m_sales_channel_isSet;
}

bool OAIGetPricesRequestObject::is_sales_channel_Valid() const{
    return m_sales_channel_isValid;
}

bool OAIGetPricesRequestObject::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_utm_campaign_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_utm_internal_campaign_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_utm_medium_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_utm_source_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_sales_channel_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetPricesRequestObject::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_email_isValid && m_items_isValid && m_sales_channel_isValid && true;
}

} // namespace OpenAPI
