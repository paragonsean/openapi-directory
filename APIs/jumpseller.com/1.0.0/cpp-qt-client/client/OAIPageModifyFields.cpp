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

#include "OAIPageModifyFields.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPageModifyFields::OAIPageModifyFields(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPageModifyFields::OAIPageModifyFields() {
    this->initializeModel();
}

OAIPageModifyFields::~OAIPageModifyFields() {}

void OAIPageModifyFields::initializeModel() {

    m_body_isSet = false;
    m_body_isValid = false;

    m_categories_isSet = false;
    m_categories_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_meta_description_isSet = false;
    m_meta_description_isValid = false;

    m_page_title_isSet = false;
    m_page_title_isValid = false;

    m_permalink_isSet = false;
    m_permalink_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_r_template_isSet = false;
    m_r_template_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAIPageModifyFields::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPageModifyFields::fromJsonObject(QJsonObject json) {

    m_body_isValid = ::OpenAPI::fromJsonValue(m_body, json[QString("body")]);
    m_body_isSet = !json[QString("body")].isNull() && m_body_isValid;

    m_categories_isValid = ::OpenAPI::fromJsonValue(m_categories, json[QString("categories")]);
    m_categories_isSet = !json[QString("categories")].isNull() && m_categories_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_meta_description_isValid = ::OpenAPI::fromJsonValue(m_meta_description, json[QString("meta_description")]);
    m_meta_description_isSet = !json[QString("meta_description")].isNull() && m_meta_description_isValid;

    m_page_title_isValid = ::OpenAPI::fromJsonValue(m_page_title, json[QString("page_title")]);
    m_page_title_isSet = !json[QString("page_title")].isNull() && m_page_title_isValid;

    m_permalink_isValid = ::OpenAPI::fromJsonValue(m_permalink, json[QString("permalink")]);
    m_permalink_isSet = !json[QString("permalink")].isNull() && m_permalink_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_r_template_isValid = ::OpenAPI::fromJsonValue(m_r_template, json[QString("template")]);
    m_r_template_isSet = !json[QString("template")].isNull() && m_r_template_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;
}

QString OAIPageModifyFields::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPageModifyFields::asJsonObject() const {
    QJsonObject obj;
    if (m_body_isSet) {
        obj.insert(QString("body"), ::OpenAPI::toJsonValue(m_body));
    }
    if (m_categories.size() > 0) {
        obj.insert(QString("categories"), ::OpenAPI::toJsonValue(m_categories));
    }
    if (m_image.isSet()) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_meta_description_isSet) {
        obj.insert(QString("meta_description"), ::OpenAPI::toJsonValue(m_meta_description));
    }
    if (m_page_title_isSet) {
        obj.insert(QString("page_title"), ::OpenAPI::toJsonValue(m_page_title));
    }
    if (m_permalink_isSet) {
        obj.insert(QString("permalink"), ::OpenAPI::toJsonValue(m_permalink));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_r_template_isSet) {
        obj.insert(QString("template"), ::OpenAPI::toJsonValue(m_r_template));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

QString OAIPageModifyFields::getBody() const {
    return m_body;
}
void OAIPageModifyFields::setBody(const QString &body) {
    m_body = body;
    m_body_isSet = true;
}

bool OAIPageModifyFields::is_body_Set() const{
    return m_body_isSet;
}

bool OAIPageModifyFields::is_body_Valid() const{
    return m_body_isValid;
}

QList<OAIPageCategory> OAIPageModifyFields::getCategories() const {
    return m_categories;
}
void OAIPageModifyFields::setCategories(const QList<OAIPageCategory> &categories) {
    m_categories = categories;
    m_categories_isSet = true;
}

bool OAIPageModifyFields::is_categories_Set() const{
    return m_categories_isSet;
}

bool OAIPageModifyFields::is_categories_Valid() const{
    return m_categories_isValid;
}

OAIPageFields_image OAIPageModifyFields::getImage() const {
    return m_image;
}
void OAIPageModifyFields::setImage(const OAIPageFields_image &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAIPageModifyFields::is_image_Set() const{
    return m_image_isSet;
}

bool OAIPageModifyFields::is_image_Valid() const{
    return m_image_isValid;
}

QString OAIPageModifyFields::getMetaDescription() const {
    return m_meta_description;
}
void OAIPageModifyFields::setMetaDescription(const QString &meta_description) {
    m_meta_description = meta_description;
    m_meta_description_isSet = true;
}

bool OAIPageModifyFields::is_meta_description_Set() const{
    return m_meta_description_isSet;
}

bool OAIPageModifyFields::is_meta_description_Valid() const{
    return m_meta_description_isValid;
}

QString OAIPageModifyFields::getPageTitle() const {
    return m_page_title;
}
void OAIPageModifyFields::setPageTitle(const QString &page_title) {
    m_page_title = page_title;
    m_page_title_isSet = true;
}

bool OAIPageModifyFields::is_page_title_Set() const{
    return m_page_title_isSet;
}

bool OAIPageModifyFields::is_page_title_Valid() const{
    return m_page_title_isValid;
}

QString OAIPageModifyFields::getPermalink() const {
    return m_permalink;
}
void OAIPageModifyFields::setPermalink(const QString &permalink) {
    m_permalink = permalink;
    m_permalink_isSet = true;
}

bool OAIPageModifyFields::is_permalink_Set() const{
    return m_permalink_isSet;
}

bool OAIPageModifyFields::is_permalink_Valid() const{
    return m_permalink_isValid;
}

QString OAIPageModifyFields::getStatus() const {
    return m_status;
}
void OAIPageModifyFields::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIPageModifyFields::is_status_Set() const{
    return m_status_isSet;
}

bool OAIPageModifyFields::is_status_Valid() const{
    return m_status_isValid;
}

qint32 OAIPageModifyFields::getRTemplate() const {
    return m_r_template;
}
void OAIPageModifyFields::setRTemplate(const qint32 &r_template) {
    m_r_template = r_template;
    m_r_template_isSet = true;
}

bool OAIPageModifyFields::is_r_template_Set() const{
    return m_r_template_isSet;
}

bool OAIPageModifyFields::is_r_template_Valid() const{
    return m_r_template_isValid;
}

QString OAIPageModifyFields::getTitle() const {
    return m_title;
}
void OAIPageModifyFields::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIPageModifyFields::is_title_Set() const{
    return m_title_isSet;
}

bool OAIPageModifyFields::is_title_Valid() const{
    return m_title_isValid;
}

bool OAIPageModifyFields::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_body_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_categories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_image.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_meta_description_isSet) {
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

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_template_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPageModifyFields::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
