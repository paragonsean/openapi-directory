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

#include "OAITrafficSource.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITrafficSource::OAITrafficSource(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITrafficSource::OAITrafficSource() {
    this->initializeModel();
}

OAITrafficSource::~OAITrafficSource() {}

void OAITrafficSource::initializeModel() {

    m_campaign_isSet = false;
    m_campaign_isValid = false;

    m_first_page_visited_isSet = false;
    m_first_page_visited_isValid = false;

    m_first_page_visited_at_isSet = false;
    m_first_page_visited_at_isValid = false;

    m_medium_isSet = false;
    m_medium_isValid = false;

    m_referral_code_isSet = false;
    m_referral_code_isValid = false;

    m_referral_source_isSet = false;
    m_referral_source_isValid = false;

    m_referral_url_isSet = false;
    m_referral_url_isValid = false;

    m_source_name_isSet = false;
    m_source_name_isValid = false;

    m_user_agent_isSet = false;
    m_user_agent_isValid = false;
}

void OAITrafficSource::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITrafficSource::fromJsonObject(QJsonObject json) {

    m_campaign_isValid = ::OpenAPI::fromJsonValue(m_campaign, json[QString("campaign")]);
    m_campaign_isSet = !json[QString("campaign")].isNull() && m_campaign_isValid;

    m_first_page_visited_isValid = ::OpenAPI::fromJsonValue(m_first_page_visited, json[QString("first_page_visited")]);
    m_first_page_visited_isSet = !json[QString("first_page_visited")].isNull() && m_first_page_visited_isValid;

    m_first_page_visited_at_isValid = ::OpenAPI::fromJsonValue(m_first_page_visited_at, json[QString("first_page_visited_at")]);
    m_first_page_visited_at_isSet = !json[QString("first_page_visited_at")].isNull() && m_first_page_visited_at_isValid;

    m_medium_isValid = ::OpenAPI::fromJsonValue(m_medium, json[QString("medium")]);
    m_medium_isSet = !json[QString("medium")].isNull() && m_medium_isValid;

    m_referral_code_isValid = ::OpenAPI::fromJsonValue(m_referral_code, json[QString("referral_code")]);
    m_referral_code_isSet = !json[QString("referral_code")].isNull() && m_referral_code_isValid;

    m_referral_source_isValid = ::OpenAPI::fromJsonValue(m_referral_source, json[QString("referral_source")]);
    m_referral_source_isSet = !json[QString("referral_source")].isNull() && m_referral_source_isValid;

    m_referral_url_isValid = ::OpenAPI::fromJsonValue(m_referral_url, json[QString("referral_url")]);
    m_referral_url_isSet = !json[QString("referral_url")].isNull() && m_referral_url_isValid;

    m_source_name_isValid = ::OpenAPI::fromJsonValue(m_source_name, json[QString("source_name")]);
    m_source_name_isSet = !json[QString("source_name")].isNull() && m_source_name_isValid;

    m_user_agent_isValid = ::OpenAPI::fromJsonValue(m_user_agent, json[QString("user_agent")]);
    m_user_agent_isSet = !json[QString("user_agent")].isNull() && m_user_agent_isValid;
}

QString OAITrafficSource::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITrafficSource::asJsonObject() const {
    QJsonObject obj;
    if (m_campaign_isSet) {
        obj.insert(QString("campaign"), ::OpenAPI::toJsonValue(m_campaign));
    }
    if (m_first_page_visited_isSet) {
        obj.insert(QString("first_page_visited"), ::OpenAPI::toJsonValue(m_first_page_visited));
    }
    if (m_first_page_visited_at_isSet) {
        obj.insert(QString("first_page_visited_at"), ::OpenAPI::toJsonValue(m_first_page_visited_at));
    }
    if (m_medium_isSet) {
        obj.insert(QString("medium"), ::OpenAPI::toJsonValue(m_medium));
    }
    if (m_referral_code_isSet) {
        obj.insert(QString("referral_code"), ::OpenAPI::toJsonValue(m_referral_code));
    }
    if (m_referral_source_isSet) {
        obj.insert(QString("referral_source"), ::OpenAPI::toJsonValue(m_referral_source));
    }
    if (m_referral_url_isSet) {
        obj.insert(QString("referral_url"), ::OpenAPI::toJsonValue(m_referral_url));
    }
    if (m_source_name_isSet) {
        obj.insert(QString("source_name"), ::OpenAPI::toJsonValue(m_source_name));
    }
    if (m_user_agent_isSet) {
        obj.insert(QString("user_agent"), ::OpenAPI::toJsonValue(m_user_agent));
    }
    return obj;
}

QString OAITrafficSource::getCampaign() const {
    return m_campaign;
}
void OAITrafficSource::setCampaign(const QString &campaign) {
    m_campaign = campaign;
    m_campaign_isSet = true;
}

bool OAITrafficSource::is_campaign_Set() const{
    return m_campaign_isSet;
}

bool OAITrafficSource::is_campaign_Valid() const{
    return m_campaign_isValid;
}

QString OAITrafficSource::getFirstPageVisited() const {
    return m_first_page_visited;
}
void OAITrafficSource::setFirstPageVisited(const QString &first_page_visited) {
    m_first_page_visited = first_page_visited;
    m_first_page_visited_isSet = true;
}

bool OAITrafficSource::is_first_page_visited_Set() const{
    return m_first_page_visited_isSet;
}

bool OAITrafficSource::is_first_page_visited_Valid() const{
    return m_first_page_visited_isValid;
}

QString OAITrafficSource::getFirstPageVisitedAt() const {
    return m_first_page_visited_at;
}
void OAITrafficSource::setFirstPageVisitedAt(const QString &first_page_visited_at) {
    m_first_page_visited_at = first_page_visited_at;
    m_first_page_visited_at_isSet = true;
}

bool OAITrafficSource::is_first_page_visited_at_Set() const{
    return m_first_page_visited_at_isSet;
}

bool OAITrafficSource::is_first_page_visited_at_Valid() const{
    return m_first_page_visited_at_isValid;
}

QString OAITrafficSource::getMedium() const {
    return m_medium;
}
void OAITrafficSource::setMedium(const QString &medium) {
    m_medium = medium;
    m_medium_isSet = true;
}

bool OAITrafficSource::is_medium_Set() const{
    return m_medium_isSet;
}

bool OAITrafficSource::is_medium_Valid() const{
    return m_medium_isValid;
}

QString OAITrafficSource::getReferralCode() const {
    return m_referral_code;
}
void OAITrafficSource::setReferralCode(const QString &referral_code) {
    m_referral_code = referral_code;
    m_referral_code_isSet = true;
}

bool OAITrafficSource::is_referral_code_Set() const{
    return m_referral_code_isSet;
}

bool OAITrafficSource::is_referral_code_Valid() const{
    return m_referral_code_isValid;
}

QString OAITrafficSource::getReferralSource() const {
    return m_referral_source;
}
void OAITrafficSource::setReferralSource(const QString &referral_source) {
    m_referral_source = referral_source;
    m_referral_source_isSet = true;
}

bool OAITrafficSource::is_referral_source_Set() const{
    return m_referral_source_isSet;
}

bool OAITrafficSource::is_referral_source_Valid() const{
    return m_referral_source_isValid;
}

QString OAITrafficSource::getReferralUrl() const {
    return m_referral_url;
}
void OAITrafficSource::setReferralUrl(const QString &referral_url) {
    m_referral_url = referral_url;
    m_referral_url_isSet = true;
}

bool OAITrafficSource::is_referral_url_Set() const{
    return m_referral_url_isSet;
}

bool OAITrafficSource::is_referral_url_Valid() const{
    return m_referral_url_isValid;
}

QString OAITrafficSource::getSourceName() const {
    return m_source_name;
}
void OAITrafficSource::setSourceName(const QString &source_name) {
    m_source_name = source_name;
    m_source_name_isSet = true;
}

bool OAITrafficSource::is_source_name_Set() const{
    return m_source_name_isSet;
}

bool OAITrafficSource::is_source_name_Valid() const{
    return m_source_name_isValid;
}

QString OAITrafficSource::getUserAgent() const {
    return m_user_agent;
}
void OAITrafficSource::setUserAgent(const QString &user_agent) {
    m_user_agent = user_agent;
    m_user_agent_isSet = true;
}

bool OAITrafficSource::is_user_agent_Set() const{
    return m_user_agent_isSet;
}

bool OAITrafficSource::is_user_agent_Valid() const{
    return m_user_agent_isValid;
}

bool OAITrafficSource::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_campaign_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_page_visited_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_page_visited_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_medium_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_referral_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_referral_source_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_referral_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_agent_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITrafficSource::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
