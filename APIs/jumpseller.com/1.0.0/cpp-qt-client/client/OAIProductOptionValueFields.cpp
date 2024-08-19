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

#include "OAIProductOptionValueFields.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProductOptionValueFields::OAIProductOptionValueFields(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProductOptionValueFields::OAIProductOptionValueFields() {
    this->initializeModel();
}

OAIProductOptionValueFields::~OAIProductOptionValueFields() {}

void OAIProductOptionValueFields::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_position_isSet = false;
    m_position_isValid = false;

    m_product_option_isSet = false;
    m_product_option_isValid = false;

    m_variants_isSet = false;
    m_variants_isValid = false;
}

void OAIProductOptionValueFields::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProductOptionValueFields::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_position_isValid = ::OpenAPI::fromJsonValue(m_position, json[QString("position")]);
    m_position_isSet = !json[QString("position")].isNull() && m_position_isValid;

    m_product_option_isValid = ::OpenAPI::fromJsonValue(m_product_option, json[QString("product_option")]);
    m_product_option_isSet = !json[QString("product_option")].isNull() && m_product_option_isValid;

    m_variants_isValid = ::OpenAPI::fromJsonValue(m_variants, json[QString("variants")]);
    m_variants_isSet = !json[QString("variants")].isNull() && m_variants_isValid;
}

QString OAIProductOptionValueFields::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProductOptionValueFields::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_position_isSet) {
        obj.insert(QString("position"), ::OpenAPI::toJsonValue(m_position));
    }
    if (m_product_option.isSet()) {
        obj.insert(QString("product_option"), ::OpenAPI::toJsonValue(m_product_option));
    }
    if (m_variants.size() > 0) {
        obj.insert(QString("variants"), ::OpenAPI::toJsonValue(m_variants));
    }
    return obj;
}

qint32 OAIProductOptionValueFields::getId() const {
    return m_id;
}
void OAIProductOptionValueFields::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIProductOptionValueFields::is_id_Set() const{
    return m_id_isSet;
}

bool OAIProductOptionValueFields::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIProductOptionValueFields::getName() const {
    return m_name;
}
void OAIProductOptionValueFields::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIProductOptionValueFields::is_name_Set() const{
    return m_name_isSet;
}

bool OAIProductOptionValueFields::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIProductOptionValueFields::getPosition() const {
    return m_position;
}
void OAIProductOptionValueFields::setPosition(const qint32 &position) {
    m_position = position;
    m_position_isSet = true;
}

bool OAIProductOptionValueFields::is_position_Set() const{
    return m_position_isSet;
}

bool OAIProductOptionValueFields::is_position_Valid() const{
    return m_position_isValid;
}

OAIProductOption OAIProductOptionValueFields::getProductOption() const {
    return m_product_option;
}
void OAIProductOptionValueFields::setProductOption(const OAIProductOption &product_option) {
    m_product_option = product_option;
    m_product_option_isSet = true;
}

bool OAIProductOptionValueFields::is_product_option_Set() const{
    return m_product_option_isSet;
}

bool OAIProductOptionValueFields::is_product_option_Valid() const{
    return m_product_option_isValid;
}

QList<OAIVariant> OAIProductOptionValueFields::getVariants() const {
    return m_variants;
}
void OAIProductOptionValueFields::setVariants(const QList<OAIVariant> &variants) {
    m_variants = variants;
    m_variants_isSet = true;
}

bool OAIProductOptionValueFields::is_variants_Set() const{
    return m_variants_isSet;
}

bool OAIProductOptionValueFields::is_variants_Valid() const{
    return m_variants_isValid;
}

bool OAIProductOptionValueFields::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_option.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_variants.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProductOptionValueFields::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
