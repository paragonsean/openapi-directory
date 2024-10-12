/**
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIServerConfigCustom.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIServerConfigCustom::OAIServerConfigCustom(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIServerConfigCustom::OAIServerConfigCustom() {
    this->initializeModel();
}

OAIServerConfigCustom::~OAIServerConfigCustom() {}

void OAIServerConfigCustom::initializeModel() {

    m_admin_isSet = false;
    m_admin_isValid = false;

    m_auto_blacklist_isSet = false;
    m_auto_blacklist_isValid = false;

    m_cache_isSet = false;
    m_cache_isValid = false;

    m_contact_form_isSet = false;
    m_contact_form_isValid = false;

    m_followers_isSet = false;
    m_followers_isValid = false;

    m_import_isSet = false;
    m_import_isValid = false;

    m_instance_isSet = false;
    m_instance_isValid = false;

    m_services_isSet = false;
    m_services_isValid = false;

    m_signup_isSet = false;
    m_signup_isValid = false;

    m_theme_isSet = false;
    m_theme_isValid = false;

    m_transcoding_isSet = false;
    m_transcoding_isValid = false;

    m_user_isSet = false;
    m_user_isValid = false;
}

void OAIServerConfigCustom::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIServerConfigCustom::fromJsonObject(QJsonObject json) {

    m_admin_isValid = ::OpenAPI::fromJsonValue(m_admin, json[QString("admin")]);
    m_admin_isSet = !json[QString("admin")].isNull() && m_admin_isValid;

    m_auto_blacklist_isValid = ::OpenAPI::fromJsonValue(m_auto_blacklist, json[QString("autoBlacklist")]);
    m_auto_blacklist_isSet = !json[QString("autoBlacklist")].isNull() && m_auto_blacklist_isValid;

    m_cache_isValid = ::OpenAPI::fromJsonValue(m_cache, json[QString("cache")]);
    m_cache_isSet = !json[QString("cache")].isNull() && m_cache_isValid;

    m_contact_form_isValid = ::OpenAPI::fromJsonValue(m_contact_form, json[QString("contactForm")]);
    m_contact_form_isSet = !json[QString("contactForm")].isNull() && m_contact_form_isValid;

    m_followers_isValid = ::OpenAPI::fromJsonValue(m_followers, json[QString("followers")]);
    m_followers_isSet = !json[QString("followers")].isNull() && m_followers_isValid;

    m_import_isValid = ::OpenAPI::fromJsonValue(m_import, json[QString("import")]);
    m_import_isSet = !json[QString("import")].isNull() && m_import_isValid;

    m_instance_isValid = ::OpenAPI::fromJsonValue(m_instance, json[QString("instance")]);
    m_instance_isSet = !json[QString("instance")].isNull() && m_instance_isValid;

    m_services_isValid = ::OpenAPI::fromJsonValue(m_services, json[QString("services")]);
    m_services_isSet = !json[QString("services")].isNull() && m_services_isValid;

    m_signup_isValid = ::OpenAPI::fromJsonValue(m_signup, json[QString("signup")]);
    m_signup_isSet = !json[QString("signup")].isNull() && m_signup_isValid;

    m_theme_isValid = ::OpenAPI::fromJsonValue(m_theme, json[QString("theme")]);
    m_theme_isSet = !json[QString("theme")].isNull() && m_theme_isValid;

    m_transcoding_isValid = ::OpenAPI::fromJsonValue(m_transcoding, json[QString("transcoding")]);
    m_transcoding_isSet = !json[QString("transcoding")].isNull() && m_transcoding_isValid;

    m_user_isValid = ::OpenAPI::fromJsonValue(m_user, json[QString("user")]);
    m_user_isSet = !json[QString("user")].isNull() && m_user_isValid;
}

QString OAIServerConfigCustom::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIServerConfigCustom::asJsonObject() const {
    QJsonObject obj;
    if (m_admin.isSet()) {
        obj.insert(QString("admin"), ::OpenAPI::toJsonValue(m_admin));
    }
    if (m_auto_blacklist.isSet()) {
        obj.insert(QString("autoBlacklist"), ::OpenAPI::toJsonValue(m_auto_blacklist));
    }
    if (m_cache.isSet()) {
        obj.insert(QString("cache"), ::OpenAPI::toJsonValue(m_cache));
    }
    if (m_contact_form.isSet()) {
        obj.insert(QString("contactForm"), ::OpenAPI::toJsonValue(m_contact_form));
    }
    if (m_followers.isSet()) {
        obj.insert(QString("followers"), ::OpenAPI::toJsonValue(m_followers));
    }
    if (m_import.isSet()) {
        obj.insert(QString("import"), ::OpenAPI::toJsonValue(m_import));
    }
    if (m_instance.isSet()) {
        obj.insert(QString("instance"), ::OpenAPI::toJsonValue(m_instance));
    }
    if (m_services.isSet()) {
        obj.insert(QString("services"), ::OpenAPI::toJsonValue(m_services));
    }
    if (m_signup.isSet()) {
        obj.insert(QString("signup"), ::OpenAPI::toJsonValue(m_signup));
    }
    if (m_theme.isSet()) {
        obj.insert(QString("theme"), ::OpenAPI::toJsonValue(m_theme));
    }
    if (m_transcoding.isSet()) {
        obj.insert(QString("transcoding"), ::OpenAPI::toJsonValue(m_transcoding));
    }
    if (m_user.isSet()) {
        obj.insert(QString("user"), ::OpenAPI::toJsonValue(m_user));
    }
    return obj;
}

OAIServerConfigCustom_admin OAIServerConfigCustom::getAdmin() const {
    return m_admin;
}
void OAIServerConfigCustom::setAdmin(const OAIServerConfigCustom_admin &admin) {
    m_admin = admin;
    m_admin_isSet = true;
}

bool OAIServerConfigCustom::is_admin_Set() const{
    return m_admin_isSet;
}

bool OAIServerConfigCustom::is_admin_Valid() const{
    return m_admin_isValid;
}

OAIServerConfig_autoBlacklist OAIServerConfigCustom::getAutoBlacklist() const {
    return m_auto_blacklist;
}
void OAIServerConfigCustom::setAutoBlacklist(const OAIServerConfig_autoBlacklist &auto_blacklist) {
    m_auto_blacklist = auto_blacklist;
    m_auto_blacklist_isSet = true;
}

bool OAIServerConfigCustom::is_auto_blacklist_Set() const{
    return m_auto_blacklist_isSet;
}

bool OAIServerConfigCustom::is_auto_blacklist_Valid() const{
    return m_auto_blacklist_isValid;
}

OAIServerConfigCustom_cache OAIServerConfigCustom::getCache() const {
    return m_cache;
}
void OAIServerConfigCustom::setCache(const OAIServerConfigCustom_cache &cache) {
    m_cache = cache;
    m_cache_isSet = true;
}

bool OAIServerConfigCustom::is_cache_Set() const{
    return m_cache_isSet;
}

bool OAIServerConfigCustom::is_cache_Valid() const{
    return m_cache_isValid;
}

OAIServerConfig_autoBlacklist_videos_ofUsers OAIServerConfigCustom::getContactForm() const {
    return m_contact_form;
}
void OAIServerConfigCustom::setContactForm(const OAIServerConfig_autoBlacklist_videos_ofUsers &contact_form) {
    m_contact_form = contact_form;
    m_contact_form_isSet = true;
}

bool OAIServerConfigCustom::is_contact_form_Set() const{
    return m_contact_form_isSet;
}

bool OAIServerConfigCustom::is_contact_form_Valid() const{
    return m_contact_form_isValid;
}

OAIServerConfigCustom_followers OAIServerConfigCustom::getFollowers() const {
    return m_followers;
}
void OAIServerConfigCustom::setFollowers(const OAIServerConfigCustom_followers &followers) {
    m_followers = followers;
    m_followers_isSet = true;
}

bool OAIServerConfigCustom::is_followers_Set() const{
    return m_followers_isSet;
}

bool OAIServerConfigCustom::is_followers_Valid() const{
    return m_followers_isValid;
}

OAIServerConfigCustom_import OAIServerConfigCustom::getImport() const {
    return m_import;
}
void OAIServerConfigCustom::setImport(const OAIServerConfigCustom_import &import) {
    m_import = import;
    m_import_isSet = true;
}

bool OAIServerConfigCustom::is_import_Set() const{
    return m_import_isSet;
}

bool OAIServerConfigCustom::is_import_Valid() const{
    return m_import_isValid;
}

OAIServerConfigCustom_instance OAIServerConfigCustom::getInstance() const {
    return m_instance;
}
void OAIServerConfigCustom::setInstance(const OAIServerConfigCustom_instance &instance) {
    m_instance = instance;
    m_instance_isSet = true;
}

bool OAIServerConfigCustom::is_instance_Set() const{
    return m_instance_isSet;
}

bool OAIServerConfigCustom::is_instance_Valid() const{
    return m_instance_isValid;
}

OAIServerConfigCustom_services OAIServerConfigCustom::getServices() const {
    return m_services;
}
void OAIServerConfigCustom::setServices(const OAIServerConfigCustom_services &services) {
    m_services = services;
    m_services_isSet = true;
}

bool OAIServerConfigCustom::is_services_Set() const{
    return m_services_isSet;
}

bool OAIServerConfigCustom::is_services_Valid() const{
    return m_services_isValid;
}

OAIServerConfigCustom_signup OAIServerConfigCustom::getSignup() const {
    return m_signup;
}
void OAIServerConfigCustom::setSignup(const OAIServerConfigCustom_signup &signup) {
    m_signup = signup;
    m_signup_isSet = true;
}

bool OAIServerConfigCustom::is_signup_Set() const{
    return m_signup_isSet;
}

bool OAIServerConfigCustom::is_signup_Valid() const{
    return m_signup_isValid;
}

OAIServerConfigCustom_theme OAIServerConfigCustom::getTheme() const {
    return m_theme;
}
void OAIServerConfigCustom::setTheme(const OAIServerConfigCustom_theme &theme) {
    m_theme = theme;
    m_theme_isSet = true;
}

bool OAIServerConfigCustom::is_theme_Set() const{
    return m_theme_isSet;
}

bool OAIServerConfigCustom::is_theme_Valid() const{
    return m_theme_isValid;
}

OAIServerConfigCustom_transcoding OAIServerConfigCustom::getTranscoding() const {
    return m_transcoding;
}
void OAIServerConfigCustom::setTranscoding(const OAIServerConfigCustom_transcoding &transcoding) {
    m_transcoding = transcoding;
    m_transcoding_isSet = true;
}

bool OAIServerConfigCustom::is_transcoding_Set() const{
    return m_transcoding_isSet;
}

bool OAIServerConfigCustom::is_transcoding_Valid() const{
    return m_transcoding_isValid;
}

OAIServerConfigCustom_user OAIServerConfigCustom::getUser() const {
    return m_user;
}
void OAIServerConfigCustom::setUser(const OAIServerConfigCustom_user &user) {
    m_user = user;
    m_user_isSet = true;
}

bool OAIServerConfigCustom::is_user_Set() const{
    return m_user_isSet;
}

bool OAIServerConfigCustom::is_user_Valid() const{
    return m_user_isValid;
}

bool OAIServerConfigCustom::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_admin.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_auto_blacklist.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_cache.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_contact_form.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_followers.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_import.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_instance.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_services.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_signup.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_theme.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_transcoding.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_user.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIServerConfigCustom::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
