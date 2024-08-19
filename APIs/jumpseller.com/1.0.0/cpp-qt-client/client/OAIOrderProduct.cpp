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

#include "OAIOrderProduct.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrderProduct::OAIOrderProduct(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrderProduct::OAIOrderProduct() {
    this->initializeModel();
}

OAIOrderProduct::~OAIOrderProduct() {}

void OAIOrderProduct::initializeModel() {

    m_discount_isSet = false;
    m_discount_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_qty_isSet = false;
    m_qty_isValid = false;

    m_sku_isSet = false;
    m_sku_isValid = false;

    m_taxes_isSet = false;
    m_taxes_isValid = false;

    m_variant_id_isSet = false;
    m_variant_id_isValid = false;

    m_weight_isSet = false;
    m_weight_isValid = false;
}

void OAIOrderProduct::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrderProduct::fromJsonObject(QJsonObject json) {

    m_discount_isValid = ::OpenAPI::fromJsonValue(m_discount, json[QString("discount")]);
    m_discount_isSet = !json[QString("discount")].isNull() && m_discount_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_qty_isValid = ::OpenAPI::fromJsonValue(m_qty, json[QString("qty")]);
    m_qty_isSet = !json[QString("qty")].isNull() && m_qty_isValid;

    m_sku_isValid = ::OpenAPI::fromJsonValue(m_sku, json[QString("sku")]);
    m_sku_isSet = !json[QString("sku")].isNull() && m_sku_isValid;

    m_taxes_isValid = ::OpenAPI::fromJsonValue(m_taxes, json[QString("taxes")]);
    m_taxes_isSet = !json[QString("taxes")].isNull() && m_taxes_isValid;

    m_variant_id_isValid = ::OpenAPI::fromJsonValue(m_variant_id, json[QString("variant_id")]);
    m_variant_id_isSet = !json[QString("variant_id")].isNull() && m_variant_id_isValid;

    m_weight_isValid = ::OpenAPI::fromJsonValue(m_weight, json[QString("weight")]);
    m_weight_isSet = !json[QString("weight")].isNull() && m_weight_isValid;
}

QString OAIOrderProduct::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrderProduct::asJsonObject() const {
    QJsonObject obj;
    if (m_discount_isSet) {
        obj.insert(QString("discount"), ::OpenAPI::toJsonValue(m_discount));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_isSet) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_qty_isSet) {
        obj.insert(QString("qty"), ::OpenAPI::toJsonValue(m_qty));
    }
    if (m_sku_isSet) {
        obj.insert(QString("sku"), ::OpenAPI::toJsonValue(m_sku));
    }
    if (m_taxes.size() > 0) {
        obj.insert(QString("taxes"), ::OpenAPI::toJsonValue(m_taxes));
    }
    if (m_variant_id_isSet) {
        obj.insert(QString("variant_id"), ::OpenAPI::toJsonValue(m_variant_id));
    }
    if (m_weight_isSet) {
        obj.insert(QString("weight"), ::OpenAPI::toJsonValue(m_weight));
    }
    return obj;
}

float OAIOrderProduct::getDiscount() const {
    return m_discount;
}
void OAIOrderProduct::setDiscount(const float &discount) {
    m_discount = discount;
    m_discount_isSet = true;
}

bool OAIOrderProduct::is_discount_Set() const{
    return m_discount_isSet;
}

bool OAIOrderProduct::is_discount_Valid() const{
    return m_discount_isValid;
}

qint32 OAIOrderProduct::getId() const {
    return m_id;
}
void OAIOrderProduct::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOrderProduct::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOrderProduct::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIOrderProduct::getImage() const {
    return m_image;
}
void OAIOrderProduct::setImage(const QString &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAIOrderProduct::is_image_Set() const{
    return m_image_isSet;
}

bool OAIOrderProduct::is_image_Valid() const{
    return m_image_isValid;
}

QString OAIOrderProduct::getName() const {
    return m_name;
}
void OAIOrderProduct::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIOrderProduct::is_name_Set() const{
    return m_name_isSet;
}

bool OAIOrderProduct::is_name_Valid() const{
    return m_name_isValid;
}

float OAIOrderProduct::getPrice() const {
    return m_price;
}
void OAIOrderProduct::setPrice(const float &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAIOrderProduct::is_price_Set() const{
    return m_price_isSet;
}

bool OAIOrderProduct::is_price_Valid() const{
    return m_price_isValid;
}

qint32 OAIOrderProduct::getQty() const {
    return m_qty;
}
void OAIOrderProduct::setQty(const qint32 &qty) {
    m_qty = qty;
    m_qty_isSet = true;
}

bool OAIOrderProduct::is_qty_Set() const{
    return m_qty_isSet;
}

bool OAIOrderProduct::is_qty_Valid() const{
    return m_qty_isValid;
}

QString OAIOrderProduct::getSku() const {
    return m_sku;
}
void OAIOrderProduct::setSku(const QString &sku) {
    m_sku = sku;
    m_sku_isSet = true;
}

bool OAIOrderProduct::is_sku_Set() const{
    return m_sku_isSet;
}

bool OAIOrderProduct::is_sku_Valid() const{
    return m_sku_isValid;
}

QList<OAIOrderProductTax> OAIOrderProduct::getTaxes() const {
    return m_taxes;
}
void OAIOrderProduct::setTaxes(const QList<OAIOrderProductTax> &taxes) {
    m_taxes = taxes;
    m_taxes_isSet = true;
}

bool OAIOrderProduct::is_taxes_Set() const{
    return m_taxes_isSet;
}

bool OAIOrderProduct::is_taxes_Valid() const{
    return m_taxes_isValid;
}

qint32 OAIOrderProduct::getVariantId() const {
    return m_variant_id;
}
void OAIOrderProduct::setVariantId(const qint32 &variant_id) {
    m_variant_id = variant_id;
    m_variant_id_isSet = true;
}

bool OAIOrderProduct::is_variant_id_Set() const{
    return m_variant_id_isSet;
}

bool OAIOrderProduct::is_variant_id_Valid() const{
    return m_variant_id_isValid;
}

float OAIOrderProduct::getWeight() const {
    return m_weight;
}
void OAIOrderProduct::setWeight(const float &weight) {
    m_weight = weight;
    m_weight_isSet = true;
}

bool OAIOrderProduct::is_weight_Set() const{
    return m_weight_isSet;
}

bool OAIOrderProduct::is_weight_Valid() const{
    return m_weight_isValid;
}

bool OAIOrderProduct::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_discount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_qty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_taxes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_variant_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_weight_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrderProduct::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
