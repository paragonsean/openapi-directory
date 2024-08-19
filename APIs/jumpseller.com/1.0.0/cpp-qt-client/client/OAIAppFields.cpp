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

#include "OAIAppFields.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppFields::OAIAppFields(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppFields::OAIAppFields() {
    this->initializeModel();
}

OAIAppFields::~OAIAppFields() {}

void OAIAppFields::initializeModel() {

    m_author_isSet = false;
    m_author_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_js_isSet = false;
    m_js_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_page_isSet = false;
    m_page_isValid = false;
}

void OAIAppFields::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppFields::fromJsonObject(QJsonObject json) {

    m_author_isValid = ::OpenAPI::fromJsonValue(m_author, json[QString("author")]);
    m_author_isSet = !json[QString("author")].isNull() && m_author_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_js_isValid = ::OpenAPI::fromJsonValue(m_js, json[QString("js")]);
    m_js_isSet = !json[QString("js")].isNull() && m_js_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_page_isValid = ::OpenAPI::fromJsonValue(m_page, json[QString("page")]);
    m_page_isSet = !json[QString("page")].isNull() && m_page_isValid;
}

QString OAIAppFields::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppFields::asJsonObject() const {
    QJsonObject obj;
    if (m_author_isSet) {
        obj.insert(QString("author"), ::OpenAPI::toJsonValue(m_author));
    }
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_js_isSet) {
        obj.insert(QString("js"), ::OpenAPI::toJsonValue(m_js));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_page_isSet) {
        obj.insert(QString("page"), ::OpenAPI::toJsonValue(m_page));
    }
    return obj;
}

QString OAIAppFields::getAuthor() const {
    return m_author;
}
void OAIAppFields::setAuthor(const QString &author) {
    m_author = author;
    m_author_isSet = true;
}

bool OAIAppFields::is_author_Set() const{
    return m_author_isSet;
}

bool OAIAppFields::is_author_Valid() const{
    return m_author_isValid;
}

QString OAIAppFields::getCode() const {
    return m_code;
}
void OAIAppFields::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIAppFields::is_code_Set() const{
    return m_code_isSet;
}

bool OAIAppFields::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIAppFields::getDescription() const {
    return m_description;
}
void OAIAppFields::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIAppFields::is_description_Set() const{
    return m_description_isSet;
}

bool OAIAppFields::is_description_Valid() const{
    return m_description_isValid;
}

bool OAIAppFields::isJs() const {
    return m_js;
}
void OAIAppFields::setJs(const bool &js) {
    m_js = js;
    m_js_isSet = true;
}

bool OAIAppFields::is_js_Set() const{
    return m_js_isSet;
}

bool OAIAppFields::is_js_Valid() const{
    return m_js_isValid;
}

QString OAIAppFields::getName() const {
    return m_name;
}
void OAIAppFields::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAppFields::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAppFields::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIAppFields::getPage() const {
    return m_page;
}
void OAIAppFields::setPage(const QString &page) {
    m_page = page;
    m_page_isSet = true;
}

bool OAIAppFields::is_page_Set() const{
    return m_page_isSet;
}

bool OAIAppFields::is_page_Valid() const{
    return m_page_isValid;
}

bool OAIAppFields::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_author_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_js_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppFields::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
