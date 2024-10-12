/**
 * Jumpseller API
 * # Endpoint Structure  All URLs are in the format:   ```text https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken   ```  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. <br/><br/> ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls. <br/><br/> ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. <br/><br/> ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX ```  In curl, you can invoque that URL with:    ```text curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" ```  To create a product, you will include the JSON data and specify the MIME Type:    ```text curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  and to update the product identified with 123:    ```text curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  or delete it:    ```text curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ``` <br/><br/> ***  # PHP Examples  Create a new Product (POST method)  ```php $url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX; $ch = curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');  $result = curl_exec($ch); print_r($result); curl_close($ch); ``` <br/><br/> ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \"created_at\").   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**. <br/><br/> ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  ```ruby tries = 0; max_tries = 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries += 1 rescue   unless tries >= max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end ```  Finally, you can review the Response Headers of each request:  ```text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval ```   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted. <br/><br/> ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.  ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100 ``` <br/><br/> ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. <br/><br/> *** <br/><br/> 
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVariantEditFields.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVariantEditFields::OAIVariantEditFields(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVariantEditFields::OAIVariantEditFields() {
    this->initializeModel();
}

OAIVariantEditFields::~OAIVariantEditFields() {}

void OAIVariantEditFields::initializeModel() {

    m_image_id_isSet = false;
    m_image_id_isValid = false;

    m_options_isSet = false;
    m_options_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_sku_isSet = false;
    m_sku_isValid = false;

    m_stock_isSet = false;
    m_stock_isValid = false;

    m_stock_unlimited_isSet = false;
    m_stock_unlimited_isValid = false;
}

void OAIVariantEditFields::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVariantEditFields::fromJsonObject(QJsonObject json) {

    m_image_id_isValid = ::OpenAPI::fromJsonValue(m_image_id, json[QString("image_id")]);
    m_image_id_isSet = !json[QString("image_id")].isNull() && m_image_id_isValid;

    m_options_isValid = ::OpenAPI::fromJsonValue(m_options, json[QString("options")]);
    m_options_isSet = !json[QString("options")].isNull() && m_options_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_sku_isValid = ::OpenAPI::fromJsonValue(m_sku, json[QString("sku")]);
    m_sku_isSet = !json[QString("sku")].isNull() && m_sku_isValid;

    m_stock_isValid = ::OpenAPI::fromJsonValue(m_stock, json[QString("stock")]);
    m_stock_isSet = !json[QString("stock")].isNull() && m_stock_isValid;

    m_stock_unlimited_isValid = ::OpenAPI::fromJsonValue(m_stock_unlimited, json[QString("stock_unlimited")]);
    m_stock_unlimited_isSet = !json[QString("stock_unlimited")].isNull() && m_stock_unlimited_isValid;
}

QString OAIVariantEditFields::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVariantEditFields::asJsonObject() const {
    QJsonObject obj;
    if (m_image_id_isSet) {
        obj.insert(QString("image_id"), ::OpenAPI::toJsonValue(m_image_id));
    }
    if (m_options.size() > 0) {
        obj.insert(QString("options"), ::OpenAPI::toJsonValue(m_options));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_sku_isSet) {
        obj.insert(QString("sku"), ::OpenAPI::toJsonValue(m_sku));
    }
    if (m_stock_isSet) {
        obj.insert(QString("stock"), ::OpenAPI::toJsonValue(m_stock));
    }
    if (m_stock_unlimited_isSet) {
        obj.insert(QString("stock_unlimited"), ::OpenAPI::toJsonValue(m_stock_unlimited));
    }
    return obj;
}

qint32 OAIVariantEditFields::getImageId() const {
    return m_image_id;
}
void OAIVariantEditFields::setImageId(const qint32 &image_id) {
    m_image_id = image_id;
    m_image_id_isSet = true;
}

bool OAIVariantEditFields::is_image_id_Set() const{
    return m_image_id_isSet;
}

bool OAIVariantEditFields::is_image_id_Valid() const{
    return m_image_id_isValid;
}

QList<OAIProductOptionVariantEdit> OAIVariantEditFields::getOptions() const {
    return m_options;
}
void OAIVariantEditFields::setOptions(const QList<OAIProductOptionVariantEdit> &options) {
    m_options = options;
    m_options_isSet = true;
}

bool OAIVariantEditFields::is_options_Set() const{
    return m_options_isSet;
}

bool OAIVariantEditFields::is_options_Valid() const{
    return m_options_isValid;
}

float OAIVariantEditFields::getPrice() const {
    return m_price;
}
void OAIVariantEditFields::setPrice(const float &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAIVariantEditFields::is_price_Set() const{
    return m_price_isSet;
}

bool OAIVariantEditFields::is_price_Valid() const{
    return m_price_isValid;
}

QString OAIVariantEditFields::getSku() const {
    return m_sku;
}
void OAIVariantEditFields::setSku(const QString &sku) {
    m_sku = sku;
    m_sku_isSet = true;
}

bool OAIVariantEditFields::is_sku_Set() const{
    return m_sku_isSet;
}

bool OAIVariantEditFields::is_sku_Valid() const{
    return m_sku_isValid;
}

qint32 OAIVariantEditFields::getStock() const {
    return m_stock;
}
void OAIVariantEditFields::setStock(const qint32 &stock) {
    m_stock = stock;
    m_stock_isSet = true;
}

bool OAIVariantEditFields::is_stock_Set() const{
    return m_stock_isSet;
}

bool OAIVariantEditFields::is_stock_Valid() const{
    return m_stock_isValid;
}

bool OAIVariantEditFields::isStockUnlimited() const {
    return m_stock_unlimited;
}
void OAIVariantEditFields::setStockUnlimited(const bool &stock_unlimited) {
    m_stock_unlimited = stock_unlimited;
    m_stock_unlimited_isSet = true;
}

bool OAIVariantEditFields::is_stock_unlimited_Set() const{
    return m_stock_unlimited_isSet;
}

bool OAIVariantEditFields::is_stock_unlimited_Valid() const{
    return m_stock_unlimited_isValid;
}

bool OAIVariantEditFields::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_image_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_options.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stock_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stock_unlimited_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVariantEditFields::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
