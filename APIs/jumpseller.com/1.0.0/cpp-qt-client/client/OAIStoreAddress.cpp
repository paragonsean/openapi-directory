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

#include "OAIStoreAddress.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStoreAddress::OAIStoreAddress(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStoreAddress::OAIStoreAddress() {
    this->initializeModel();
}

OAIStoreAddress::~OAIStoreAddress() {}

void OAIStoreAddress::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_country_code_isSet = false;
    m_country_code_isValid = false;

    m_postal_isSet = false;
    m_postal_isValid = false;

    m_region_isSet = false;
    m_region_isValid = false;

    m_region_code_isSet = false;
    m_region_code_isValid = false;
}

void OAIStoreAddress::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStoreAddress::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_country_code_isValid = ::OpenAPI::fromJsonValue(m_country_code, json[QString("country_code")]);
    m_country_code_isSet = !json[QString("country_code")].isNull() && m_country_code_isValid;

    m_postal_isValid = ::OpenAPI::fromJsonValue(m_postal, json[QString("postal")]);
    m_postal_isSet = !json[QString("postal")].isNull() && m_postal_isValid;

    m_region_isValid = ::OpenAPI::fromJsonValue(m_region, json[QString("region")]);
    m_region_isSet = !json[QString("region")].isNull() && m_region_isValid;

    m_region_code_isValid = ::OpenAPI::fromJsonValue(m_region_code, json[QString("region_code")]);
    m_region_code_isSet = !json[QString("region_code")].isNull() && m_region_code_isValid;
}

QString OAIStoreAddress::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStoreAddress::asJsonObject() const {
    QJsonObject obj;
    if (m_address_isSet) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_country_code_isSet) {
        obj.insert(QString("country_code"), ::OpenAPI::toJsonValue(m_country_code));
    }
    if (m_postal_isSet) {
        obj.insert(QString("postal"), ::OpenAPI::toJsonValue(m_postal));
    }
    if (m_region_isSet) {
        obj.insert(QString("region"), ::OpenAPI::toJsonValue(m_region));
    }
    if (m_region_code_isSet) {
        obj.insert(QString("region_code"), ::OpenAPI::toJsonValue(m_region_code));
    }
    return obj;
}

QString OAIStoreAddress::getAddress() const {
    return m_address;
}
void OAIStoreAddress::setAddress(const QString &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIStoreAddress::is_address_Set() const{
    return m_address_isSet;
}

bool OAIStoreAddress::is_address_Valid() const{
    return m_address_isValid;
}

QString OAIStoreAddress::getCity() const {
    return m_city;
}
void OAIStoreAddress::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIStoreAddress::is_city_Set() const{
    return m_city_isSet;
}

bool OAIStoreAddress::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIStoreAddress::getCountry() const {
    return m_country;
}
void OAIStoreAddress::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIStoreAddress::is_country_Set() const{
    return m_country_isSet;
}

bool OAIStoreAddress::is_country_Valid() const{
    return m_country_isValid;
}

QString OAIStoreAddress::getCountryCode() const {
    return m_country_code;
}
void OAIStoreAddress::setCountryCode(const QString &country_code) {
    m_country_code = country_code;
    m_country_code_isSet = true;
}

bool OAIStoreAddress::is_country_code_Set() const{
    return m_country_code_isSet;
}

bool OAIStoreAddress::is_country_code_Valid() const{
    return m_country_code_isValid;
}

QString OAIStoreAddress::getPostal() const {
    return m_postal;
}
void OAIStoreAddress::setPostal(const QString &postal) {
    m_postal = postal;
    m_postal_isSet = true;
}

bool OAIStoreAddress::is_postal_Set() const{
    return m_postal_isSet;
}

bool OAIStoreAddress::is_postal_Valid() const{
    return m_postal_isValid;
}

QString OAIStoreAddress::getRegion() const {
    return m_region;
}
void OAIStoreAddress::setRegion(const QString &region) {
    m_region = region;
    m_region_isSet = true;
}

bool OAIStoreAddress::is_region_Set() const{
    return m_region_isSet;
}

bool OAIStoreAddress::is_region_Valid() const{
    return m_region_isValid;
}

QString OAIStoreAddress::getRegionCode() const {
    return m_region_code;
}
void OAIStoreAddress::setRegionCode(const QString &region_code) {
    m_region_code = region_code;
    m_region_code_isSet = true;
}

bool OAIStoreAddress::is_region_code_Set() const{
    return m_region_code_isSet;
}

bool OAIStoreAddress::is_region_code_Valid() const{
    return m_region_code_isValid;
}

bool OAIStoreAddress::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_postal_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStoreAddress::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
