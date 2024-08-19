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

#include "OAIProductEditFields.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProductEditFields::OAIProductEditFields(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProductEditFields::OAIProductEditFields() {
    this->initializeModel();
}

OAIProductEditFields::~OAIProductEditFields() {}

void OAIProductEditFields::initializeModel() {

    m_barcode_isSet = false;
    m_barcode_isValid = false;

    m_categories_isSet = false;
    m_categories_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_diameter_isSet = false;
    m_diameter_isValid = false;

    m_featured_isSet = false;
    m_featured_isValid = false;

    m_google_product_category_isSet = false;
    m_google_product_category_isValid = false;

    m_height_isSet = false;
    m_height_isValid = false;

    m_length_isSet = false;
    m_length_isValid = false;

    m_meta_description_isSet = false;
    m_meta_description_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_package_format_isSet = false;
    m_package_format_isValid = false;

    m_page_title_isSet = false;
    m_page_title_isValid = false;

    m_permalink_isSet = false;
    m_permalink_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_shipping_required_isSet = false;
    m_shipping_required_isValid = false;

    m_sku_isSet = false;
    m_sku_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_stock_isSet = false;
    m_stock_isValid = false;

    m_stock_unlimited_isSet = false;
    m_stock_unlimited_isValid = false;

    m_weight_isSet = false;
    m_weight_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;
}

void OAIProductEditFields::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProductEditFields::fromJsonObject(QJsonObject json) {

    m_barcode_isValid = ::OpenAPI::fromJsonValue(m_barcode, json[QString("barcode")]);
    m_barcode_isSet = !json[QString("barcode")].isNull() && m_barcode_isValid;

    m_categories_isValid = ::OpenAPI::fromJsonValue(m_categories, json[QString("categories")]);
    m_categories_isSet = !json[QString("categories")].isNull() && m_categories_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_diameter_isValid = ::OpenAPI::fromJsonValue(m_diameter, json[QString("diameter")]);
    m_diameter_isSet = !json[QString("diameter")].isNull() && m_diameter_isValid;

    m_featured_isValid = ::OpenAPI::fromJsonValue(m_featured, json[QString("featured")]);
    m_featured_isSet = !json[QString("featured")].isNull() && m_featured_isValid;

    m_google_product_category_isValid = ::OpenAPI::fromJsonValue(m_google_product_category, json[QString("google_product_category")]);
    m_google_product_category_isSet = !json[QString("google_product_category")].isNull() && m_google_product_category_isValid;

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("height")]);
    m_height_isSet = !json[QString("height")].isNull() && m_height_isValid;

    m_length_isValid = ::OpenAPI::fromJsonValue(m_length, json[QString("length")]);
    m_length_isSet = !json[QString("length")].isNull() && m_length_isValid;

    m_meta_description_isValid = ::OpenAPI::fromJsonValue(m_meta_description, json[QString("meta_description")]);
    m_meta_description_isSet = !json[QString("meta_description")].isNull() && m_meta_description_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_package_format_isValid = ::OpenAPI::fromJsonValue(m_package_format, json[QString("package_format")]);
    m_package_format_isSet = !json[QString("package_format")].isNull() && m_package_format_isValid;

    m_page_title_isValid = ::OpenAPI::fromJsonValue(m_page_title, json[QString("page_title")]);
    m_page_title_isSet = !json[QString("page_title")].isNull() && m_page_title_isValid;

    m_permalink_isValid = ::OpenAPI::fromJsonValue(m_permalink, json[QString("permalink")]);
    m_permalink_isSet = !json[QString("permalink")].isNull() && m_permalink_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_shipping_required_isValid = ::OpenAPI::fromJsonValue(m_shipping_required, json[QString("shipping_required")]);
    m_shipping_required_isSet = !json[QString("shipping_required")].isNull() && m_shipping_required_isValid;

    m_sku_isValid = ::OpenAPI::fromJsonValue(m_sku, json[QString("sku")]);
    m_sku_isSet = !json[QString("sku")].isNull() && m_sku_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_stock_isValid = ::OpenAPI::fromJsonValue(m_stock, json[QString("stock")]);
    m_stock_isSet = !json[QString("stock")].isNull() && m_stock_isValid;

    m_stock_unlimited_isValid = ::OpenAPI::fromJsonValue(m_stock_unlimited, json[QString("stock_unlimited")]);
    m_stock_unlimited_isSet = !json[QString("stock_unlimited")].isNull() && m_stock_unlimited_isValid;

    m_weight_isValid = ::OpenAPI::fromJsonValue(m_weight, json[QString("weight")]);
    m_weight_isSet = !json[QString("weight")].isNull() && m_weight_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("width")]);
    m_width_isSet = !json[QString("width")].isNull() && m_width_isValid;
}

QString OAIProductEditFields::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProductEditFields::asJsonObject() const {
    QJsonObject obj;
    if (m_barcode_isSet) {
        obj.insert(QString("barcode"), ::OpenAPI::toJsonValue(m_barcode));
    }
    if (m_categories.size() > 0) {
        obj.insert(QString("categories"), ::OpenAPI::toJsonValue(m_categories));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_diameter_isSet) {
        obj.insert(QString("diameter"), ::OpenAPI::toJsonValue(m_diameter));
    }
    if (m_featured_isSet) {
        obj.insert(QString("featured"), ::OpenAPI::toJsonValue(m_featured));
    }
    if (m_google_product_category_isSet) {
        obj.insert(QString("google_product_category"), ::OpenAPI::toJsonValue(m_google_product_category));
    }
    if (m_height_isSet) {
        obj.insert(QString("height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_length_isSet) {
        obj.insert(QString("length"), ::OpenAPI::toJsonValue(m_length));
    }
    if (m_meta_description_isSet) {
        obj.insert(QString("meta_description"), ::OpenAPI::toJsonValue(m_meta_description));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_package_format_isSet) {
        obj.insert(QString("package_format"), ::OpenAPI::toJsonValue(m_package_format));
    }
    if (m_page_title_isSet) {
        obj.insert(QString("page_title"), ::OpenAPI::toJsonValue(m_page_title));
    }
    if (m_permalink_isSet) {
        obj.insert(QString("permalink"), ::OpenAPI::toJsonValue(m_permalink));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_shipping_required_isSet) {
        obj.insert(QString("shipping_required"), ::OpenAPI::toJsonValue(m_shipping_required));
    }
    if (m_sku_isSet) {
        obj.insert(QString("sku"), ::OpenAPI::toJsonValue(m_sku));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_stock_isSet) {
        obj.insert(QString("stock"), ::OpenAPI::toJsonValue(m_stock));
    }
    if (m_stock_unlimited_isSet) {
        obj.insert(QString("stock_unlimited"), ::OpenAPI::toJsonValue(m_stock_unlimited));
    }
    if (m_weight_isSet) {
        obj.insert(QString("weight"), ::OpenAPI::toJsonValue(m_weight));
    }
    if (m_width_isSet) {
        obj.insert(QString("width"), ::OpenAPI::toJsonValue(m_width));
    }
    return obj;
}

QString OAIProductEditFields::getBarcode() const {
    return m_barcode;
}
void OAIProductEditFields::setBarcode(const QString &barcode) {
    m_barcode = barcode;
    m_barcode_isSet = true;
}

bool OAIProductEditFields::is_barcode_Set() const{
    return m_barcode_isSet;
}

bool OAIProductEditFields::is_barcode_Valid() const{
    return m_barcode_isValid;
}

QList<OAICategoryFields> OAIProductEditFields::getCategories() const {
    return m_categories;
}
void OAIProductEditFields::setCategories(const QList<OAICategoryFields> &categories) {
    m_categories = categories;
    m_categories_isSet = true;
}

bool OAIProductEditFields::is_categories_Set() const{
    return m_categories_isSet;
}

bool OAIProductEditFields::is_categories_Valid() const{
    return m_categories_isValid;
}

QString OAIProductEditFields::getDescription() const {
    return m_description;
}
void OAIProductEditFields::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIProductEditFields::is_description_Set() const{
    return m_description_isSet;
}

bool OAIProductEditFields::is_description_Valid() const{
    return m_description_isValid;
}

float OAIProductEditFields::getDiameter() const {
    return m_diameter;
}
void OAIProductEditFields::setDiameter(const float &diameter) {
    m_diameter = diameter;
    m_diameter_isSet = true;
}

bool OAIProductEditFields::is_diameter_Set() const{
    return m_diameter_isSet;
}

bool OAIProductEditFields::is_diameter_Valid() const{
    return m_diameter_isValid;
}

bool OAIProductEditFields::isFeatured() const {
    return m_featured;
}
void OAIProductEditFields::setFeatured(const bool &featured) {
    m_featured = featured;
    m_featured_isSet = true;
}

bool OAIProductEditFields::is_featured_Set() const{
    return m_featured_isSet;
}

bool OAIProductEditFields::is_featured_Valid() const{
    return m_featured_isValid;
}

QString OAIProductEditFields::getGoogleProductCategory() const {
    return m_google_product_category;
}
void OAIProductEditFields::setGoogleProductCategory(const QString &google_product_category) {
    m_google_product_category = google_product_category;
    m_google_product_category_isSet = true;
}

bool OAIProductEditFields::is_google_product_category_Set() const{
    return m_google_product_category_isSet;
}

bool OAIProductEditFields::is_google_product_category_Valid() const{
    return m_google_product_category_isValid;
}

float OAIProductEditFields::getHeight() const {
    return m_height;
}
void OAIProductEditFields::setHeight(const float &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAIProductEditFields::is_height_Set() const{
    return m_height_isSet;
}

bool OAIProductEditFields::is_height_Valid() const{
    return m_height_isValid;
}

float OAIProductEditFields::getLength() const {
    return m_length;
}
void OAIProductEditFields::setLength(const float &length) {
    m_length = length;
    m_length_isSet = true;
}

bool OAIProductEditFields::is_length_Set() const{
    return m_length_isSet;
}

bool OAIProductEditFields::is_length_Valid() const{
    return m_length_isValid;
}

QString OAIProductEditFields::getMetaDescription() const {
    return m_meta_description;
}
void OAIProductEditFields::setMetaDescription(const QString &meta_description) {
    m_meta_description = meta_description;
    m_meta_description_isSet = true;
}

bool OAIProductEditFields::is_meta_description_Set() const{
    return m_meta_description_isSet;
}

bool OAIProductEditFields::is_meta_description_Valid() const{
    return m_meta_description_isValid;
}

QString OAIProductEditFields::getName() const {
    return m_name;
}
void OAIProductEditFields::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIProductEditFields::is_name_Set() const{
    return m_name_isSet;
}

bool OAIProductEditFields::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIProductEditFields::getPackageFormat() const {
    return m_package_format;
}
void OAIProductEditFields::setPackageFormat(const QString &package_format) {
    m_package_format = package_format;
    m_package_format_isSet = true;
}

bool OAIProductEditFields::is_package_format_Set() const{
    return m_package_format_isSet;
}

bool OAIProductEditFields::is_package_format_Valid() const{
    return m_package_format_isValid;
}

QString OAIProductEditFields::getPageTitle() const {
    return m_page_title;
}
void OAIProductEditFields::setPageTitle(const QString &page_title) {
    m_page_title = page_title;
    m_page_title_isSet = true;
}

bool OAIProductEditFields::is_page_title_Set() const{
    return m_page_title_isSet;
}

bool OAIProductEditFields::is_page_title_Valid() const{
    return m_page_title_isValid;
}

QString OAIProductEditFields::getPermalink() const {
    return m_permalink;
}
void OAIProductEditFields::setPermalink(const QString &permalink) {
    m_permalink = permalink;
    m_permalink_isSet = true;
}

bool OAIProductEditFields::is_permalink_Set() const{
    return m_permalink_isSet;
}

bool OAIProductEditFields::is_permalink_Valid() const{
    return m_permalink_isValid;
}

float OAIProductEditFields::getPrice() const {
    return m_price;
}
void OAIProductEditFields::setPrice(const float &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAIProductEditFields::is_price_Set() const{
    return m_price_isSet;
}

bool OAIProductEditFields::is_price_Valid() const{
    return m_price_isValid;
}

bool OAIProductEditFields::isShippingRequired() const {
    return m_shipping_required;
}
void OAIProductEditFields::setShippingRequired(const bool &shipping_required) {
    m_shipping_required = shipping_required;
    m_shipping_required_isSet = true;
}

bool OAIProductEditFields::is_shipping_required_Set() const{
    return m_shipping_required_isSet;
}

bool OAIProductEditFields::is_shipping_required_Valid() const{
    return m_shipping_required_isValid;
}

QString OAIProductEditFields::getSku() const {
    return m_sku;
}
void OAIProductEditFields::setSku(const QString &sku) {
    m_sku = sku;
    m_sku_isSet = true;
}

bool OAIProductEditFields::is_sku_Set() const{
    return m_sku_isSet;
}

bool OAIProductEditFields::is_sku_Valid() const{
    return m_sku_isValid;
}

QString OAIProductEditFields::getStatus() const {
    return m_status;
}
void OAIProductEditFields::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIProductEditFields::is_status_Set() const{
    return m_status_isSet;
}

bool OAIProductEditFields::is_status_Valid() const{
    return m_status_isValid;
}

qint32 OAIProductEditFields::getStock() const {
    return m_stock;
}
void OAIProductEditFields::setStock(const qint32 &stock) {
    m_stock = stock;
    m_stock_isSet = true;
}

bool OAIProductEditFields::is_stock_Set() const{
    return m_stock_isSet;
}

bool OAIProductEditFields::is_stock_Valid() const{
    return m_stock_isValid;
}

bool OAIProductEditFields::isStockUnlimited() const {
    return m_stock_unlimited;
}
void OAIProductEditFields::setStockUnlimited(const bool &stock_unlimited) {
    m_stock_unlimited = stock_unlimited;
    m_stock_unlimited_isSet = true;
}

bool OAIProductEditFields::is_stock_unlimited_Set() const{
    return m_stock_unlimited_isSet;
}

bool OAIProductEditFields::is_stock_unlimited_Valid() const{
    return m_stock_unlimited_isValid;
}

float OAIProductEditFields::getWeight() const {
    return m_weight;
}
void OAIProductEditFields::setWeight(const float &weight) {
    m_weight = weight;
    m_weight_isSet = true;
}

bool OAIProductEditFields::is_weight_Set() const{
    return m_weight_isSet;
}

bool OAIProductEditFields::is_weight_Valid() const{
    return m_weight_isValid;
}

float OAIProductEditFields::getWidth() const {
    return m_width;
}
void OAIProductEditFields::setWidth(const float &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAIProductEditFields::is_width_Set() const{
    return m_width_isSet;
}

bool OAIProductEditFields::is_width_Valid() const{
    return m_width_isValid;
}

bool OAIProductEditFields::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_barcode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_categories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_diameter_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_featured_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_google_product_category_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_meta_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_package_format_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_permalink_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_required_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
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

        if (m_weight_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_width_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProductEditFields::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && m_price_isValid && true;
}

} // namespace OpenAPI
