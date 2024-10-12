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

#include "OAIItem1.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIItem1::OAIItem1(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIItem1::OAIItem1() {
    this->initializeModel();
}

OAIItem1::~OAIItem1() {}

void OAIItem1::initializeModel() {

    m_cost_price_isSet = false;
    m_cost_price_isValid = false;

    m_index_isSet = false;
    m_index_isValid = false;

    m_list_price_isSet = false;
    m_list_price_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_price_table_isSet = false;
    m_price_table_isValid = false;

    m_price_valid_until_isSet = false;
    m_price_valid_until_isValid = false;

    m_sku_id_isSet = false;
    m_sku_id_isValid = false;
}

void OAIItem1::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIItem1::fromJsonObject(QJsonObject json) {

    m_cost_price_isValid = ::OpenAPI::fromJsonValue(m_cost_price, json[QString("costPrice")]);
    m_cost_price_isSet = !json[QString("costPrice")].isNull() && m_cost_price_isValid;

    m_index_isValid = ::OpenAPI::fromJsonValue(m_index, json[QString("index")]);
    m_index_isSet = !json[QString("index")].isNull() && m_index_isValid;

    m_list_price_isValid = ::OpenAPI::fromJsonValue(m_list_price, json[QString("listPrice")]);
    m_list_price_isSet = !json[QString("listPrice")].isNull() && m_list_price_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_price_table_isValid = ::OpenAPI::fromJsonValue(m_price_table, json[QString("priceTable")]);
    m_price_table_isSet = !json[QString("priceTable")].isNull() && m_price_table_isValid;

    m_price_valid_until_isValid = ::OpenAPI::fromJsonValue(m_price_valid_until, json[QString("priceValidUntil")]);
    m_price_valid_until_isSet = !json[QString("priceValidUntil")].isNull() && m_price_valid_until_isValid;

    m_sku_id_isValid = ::OpenAPI::fromJsonValue(m_sku_id, json[QString("skuId")]);
    m_sku_id_isSet = !json[QString("skuId")].isNull() && m_sku_id_isValid;
}

QString OAIItem1::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIItem1::asJsonObject() const {
    QJsonObject obj;
    if (m_cost_price_isSet) {
        obj.insert(QString("costPrice"), ::OpenAPI::toJsonValue(m_cost_price));
    }
    if (m_index_isSet) {
        obj.insert(QString("index"), ::OpenAPI::toJsonValue(m_index));
    }
    if (m_list_price_isSet) {
        obj.insert(QString("listPrice"), ::OpenAPI::toJsonValue(m_list_price));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_price_table_isSet) {
        obj.insert(QString("priceTable"), ::OpenAPI::toJsonValue(m_price_table));
    }
    if (m_price_valid_until_isSet) {
        obj.insert(QString("priceValidUntil"), ::OpenAPI::toJsonValue(m_price_valid_until));
    }
    if (m_sku_id_isSet) {
        obj.insert(QString("skuId"), ::OpenAPI::toJsonValue(m_sku_id));
    }
    return obj;
}

double OAIItem1::getCostPrice() const {
    return m_cost_price;
}
void OAIItem1::setCostPrice(const double &cost_price) {
    m_cost_price = cost_price;
    m_cost_price_isSet = true;
}

bool OAIItem1::is_cost_price_Set() const{
    return m_cost_price_isSet;
}

bool OAIItem1::is_cost_price_Valid() const{
    return m_cost_price_isValid;
}

qint32 OAIItem1::getIndex() const {
    return m_index;
}
void OAIItem1::setIndex(const qint32 &index) {
    m_index = index;
    m_index_isSet = true;
}

bool OAIItem1::is_index_Set() const{
    return m_index_isSet;
}

bool OAIItem1::is_index_Valid() const{
    return m_index_isValid;
}

double OAIItem1::getListPrice() const {
    return m_list_price;
}
void OAIItem1::setListPrice(const double &list_price) {
    m_list_price = list_price;
    m_list_price_isSet = true;
}

bool OAIItem1::is_list_price_Set() const{
    return m_list_price_isSet;
}

bool OAIItem1::is_list_price_Valid() const{
    return m_list_price_isValid;
}

double OAIItem1::getPrice() const {
    return m_price;
}
void OAIItem1::setPrice(const double &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAIItem1::is_price_Set() const{
    return m_price_isSet;
}

bool OAIItem1::is_price_Valid() const{
    return m_price_isValid;
}

QString OAIItem1::getPriceTable() const {
    return m_price_table;
}
void OAIItem1::setPriceTable(const QString &price_table) {
    m_price_table = price_table;
    m_price_table_isSet = true;
}

bool OAIItem1::is_price_table_Set() const{
    return m_price_table_isSet;
}

bool OAIItem1::is_price_table_Valid() const{
    return m_price_table_isValid;
}

QString OAIItem1::getPriceValidUntil() const {
    return m_price_valid_until;
}
void OAIItem1::setPriceValidUntil(const QString &price_valid_until) {
    m_price_valid_until = price_valid_until;
    m_price_valid_until_isSet = true;
}

bool OAIItem1::is_price_valid_until_Set() const{
    return m_price_valid_until_isSet;
}

bool OAIItem1::is_price_valid_until_Valid() const{
    return m_price_valid_until_isValid;
}

QString OAIItem1::getSkuId() const {
    return m_sku_id;
}
void OAIItem1::setSkuId(const QString &sku_id) {
    m_sku_id = sku_id;
    m_sku_id_isSet = true;
}

bool OAIItem1::is_sku_id_Set() const{
    return m_sku_id_isSet;
}

bool OAIItem1::is_sku_id_Valid() const{
    return m_sku_id_isValid;
}

bool OAIItem1::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_cost_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_index_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_list_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_table_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_valid_until_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIItem1::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_cost_price_isValid && m_index_isValid && m_list_price_isValid && m_price_isValid && m_price_table_isValid && m_price_valid_until_isValid && m_sku_id_isValid && true;
}

} // namespace OpenAPI
