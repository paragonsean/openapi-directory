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

#include "OAIVideoChannelList_data_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVideoChannelList_data_inner::OAIVideoChannelList_data_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVideoChannelList_data_inner::OAIVideoChannelList_data_inner() {
    this->initializeModel();
}

OAIVideoChannelList_data_inner::~OAIVideoChannelList_data_inner() {}

void OAIVideoChannelList_data_inner::initializeModel() {

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_followers_count_isSet = false;
    m_followers_count_isValid = false;

    m_following_count_isSet = false;
    m_following_count_isValid = false;

    m_host_isSet = false;
    m_host_isValid = false;

    m_host_redundancy_allowed_isSet = false;
    m_host_redundancy_allowed_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;

    m_banners_isSet = false;
    m_banners_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_is_local_isSet = false;
    m_is_local_isValid = false;

    m_owner_account_isSet = false;
    m_owner_account_isValid = false;

    m_support_isSet = false;
    m_support_isValid = false;
}

void OAIVideoChannelList_data_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVideoChannelList_data_inner::fromJsonObject(QJsonObject json) {

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_followers_count_isValid = ::OpenAPI::fromJsonValue(m_followers_count, json[QString("followersCount")]);
    m_followers_count_isSet = !json[QString("followersCount")].isNull() && m_followers_count_isValid;

    m_following_count_isValid = ::OpenAPI::fromJsonValue(m_following_count, json[QString("followingCount")]);
    m_following_count_isSet = !json[QString("followingCount")].isNull() && m_following_count_isValid;

    m_host_isValid = ::OpenAPI::fromJsonValue(m_host, json[QString("host")]);
    m_host_isSet = !json[QString("host")].isNull() && m_host_isValid;

    m_host_redundancy_allowed_isValid = ::OpenAPI::fromJsonValue(m_host_redundancy_allowed, json[QString("hostRedundancyAllowed")]);
    m_host_redundancy_allowed_isSet = !json[QString("hostRedundancyAllowed")].isNull() && m_host_redundancy_allowed_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;

    m_banners_isValid = ::OpenAPI::fromJsonValue(m_banners, json[QString("banners")]);
    m_banners_isSet = !json[QString("banners")].isNull() && m_banners_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("displayName")]);
    m_display_name_isSet = !json[QString("displayName")].isNull() && m_display_name_isValid;

    m_is_local_isValid = ::OpenAPI::fromJsonValue(m_is_local, json[QString("isLocal")]);
    m_is_local_isSet = !json[QString("isLocal")].isNull() && m_is_local_isValid;

    m_owner_account_isValid = ::OpenAPI::fromJsonValue(m_owner_account, json[QString("ownerAccount")]);
    m_owner_account_isSet = !json[QString("ownerAccount")].isNull() && m_owner_account_isValid;

    m_support_isValid = ::OpenAPI::fromJsonValue(m_support, json[QString("support")]);
    m_support_isSet = !json[QString("support")].isNull() && m_support_isValid;
}

QString OAIVideoChannelList_data_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVideoChannelList_data_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_followers_count_isSet) {
        obj.insert(QString("followersCount"), ::OpenAPI::toJsonValue(m_followers_count));
    }
    if (m_following_count_isSet) {
        obj.insert(QString("followingCount"), ::OpenAPI::toJsonValue(m_following_count));
    }
    if (m_host_isSet) {
        obj.insert(QString("host"), ::OpenAPI::toJsonValue(m_host));
    }
    if (m_host_redundancy_allowed_isSet) {
        obj.insert(QString("hostRedundancyAllowed"), ::OpenAPI::toJsonValue(m_host_redundancy_allowed));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    if (m_banners.size() > 0) {
        obj.insert(QString("banners"), ::OpenAPI::toJsonValue(m_banners));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_display_name_isSet) {
        obj.insert(QString("displayName"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_is_local_isSet) {
        obj.insert(QString("isLocal"), ::OpenAPI::toJsonValue(m_is_local));
    }
    if (m_owner_account.isSet()) {
        obj.insert(QString("ownerAccount"), ::OpenAPI::toJsonValue(m_owner_account));
    }
    if (m_support_isSet) {
        obj.insert(QString("support"), ::OpenAPI::toJsonValue(m_support));
    }
    return obj;
}

QDateTime OAIVideoChannelList_data_inner::getCreatedAt() const {
    return m_created_at;
}
void OAIVideoChannelList_data_inner::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIVideoChannelList_data_inner::is_created_at_Valid() const{
    return m_created_at_isValid;
}

qint32 OAIVideoChannelList_data_inner::getFollowersCount() const {
    return m_followers_count;
}
void OAIVideoChannelList_data_inner::setFollowersCount(const qint32 &followers_count) {
    m_followers_count = followers_count;
    m_followers_count_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_followers_count_Set() const{
    return m_followers_count_isSet;
}

bool OAIVideoChannelList_data_inner::is_followers_count_Valid() const{
    return m_followers_count_isValid;
}

qint32 OAIVideoChannelList_data_inner::getFollowingCount() const {
    return m_following_count;
}
void OAIVideoChannelList_data_inner::setFollowingCount(const qint32 &following_count) {
    m_following_count = following_count;
    m_following_count_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_following_count_Set() const{
    return m_following_count_isSet;
}

bool OAIVideoChannelList_data_inner::is_following_count_Valid() const{
    return m_following_count_isValid;
}

QString OAIVideoChannelList_data_inner::getHost() const {
    return m_host;
}
void OAIVideoChannelList_data_inner::setHost(const QString &host) {
    m_host = host;
    m_host_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_host_Set() const{
    return m_host_isSet;
}

bool OAIVideoChannelList_data_inner::is_host_Valid() const{
    return m_host_isValid;
}

bool OAIVideoChannelList_data_inner::isHostRedundancyAllowed() const {
    return m_host_redundancy_allowed;
}
void OAIVideoChannelList_data_inner::setHostRedundancyAllowed(const bool &host_redundancy_allowed) {
    m_host_redundancy_allowed = host_redundancy_allowed;
    m_host_redundancy_allowed_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_host_redundancy_allowed_Set() const{
    return m_host_redundancy_allowed_isSet;
}

bool OAIVideoChannelList_data_inner::is_host_redundancy_allowed_Valid() const{
    return m_host_redundancy_allowed_isValid;
}

qint32 OAIVideoChannelList_data_inner::getId() const {
    return m_id;
}
void OAIVideoChannelList_data_inner::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIVideoChannelList_data_inner::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIVideoChannelList_data_inner::getName() const {
    return m_name;
}
void OAIVideoChannelList_data_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIVideoChannelList_data_inner::is_name_Valid() const{
    return m_name_isValid;
}

QDateTime OAIVideoChannelList_data_inner::getUpdatedAt() const {
    return m_updated_at;
}
void OAIVideoChannelList_data_inner::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIVideoChannelList_data_inner::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAIVideoChannelList_data_inner::getUrl() const {
    return m_url;
}
void OAIVideoChannelList_data_inner::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_url_Set() const{
    return m_url_isSet;
}

bool OAIVideoChannelList_data_inner::is_url_Valid() const{
    return m_url_isValid;
}

QList<OAIActorImage> OAIVideoChannelList_data_inner::getBanners() const {
    return m_banners;
}
void OAIVideoChannelList_data_inner::setBanners(const QList<OAIActorImage> &banners) {
    m_banners = banners;
    m_banners_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_banners_Set() const{
    return m_banners_isSet;
}

bool OAIVideoChannelList_data_inner::is_banners_Valid() const{
    return m_banners_isValid;
}

QString OAIVideoChannelList_data_inner::getDescription() const {
    return m_description;
}
void OAIVideoChannelList_data_inner::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_description_Set() const{
    return m_description_isSet;
}

bool OAIVideoChannelList_data_inner::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIVideoChannelList_data_inner::getDisplayName() const {
    return m_display_name;
}
void OAIVideoChannelList_data_inner::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIVideoChannelList_data_inner::is_display_name_Valid() const{
    return m_display_name_isValid;
}

bool OAIVideoChannelList_data_inner::isIsLocal() const {
    return m_is_local;
}
void OAIVideoChannelList_data_inner::setIsLocal(const bool &is_local) {
    m_is_local = is_local;
    m_is_local_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_is_local_Set() const{
    return m_is_local_isSet;
}

bool OAIVideoChannelList_data_inner::is_is_local_Valid() const{
    return m_is_local_isValid;
}

OAIVideoChannel_allOf_ownerAccount OAIVideoChannelList_data_inner::getOwnerAccount() const {
    return m_owner_account;
}
void OAIVideoChannelList_data_inner::setOwnerAccount(const OAIVideoChannel_allOf_ownerAccount &owner_account) {
    m_owner_account = owner_account;
    m_owner_account_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_owner_account_Set() const{
    return m_owner_account_isSet;
}

bool OAIVideoChannelList_data_inner::is_owner_account_Valid() const{
    return m_owner_account_isValid;
}

QString OAIVideoChannelList_data_inner::getSupport() const {
    return m_support;
}
void OAIVideoChannelList_data_inner::setSupport(const QString &support) {
    m_support = support;
    m_support_isSet = true;
}

bool OAIVideoChannelList_data_inner::is_support_Set() const{
    return m_support_isSet;
}

bool OAIVideoChannelList_data_inner::is_support_Valid() const{
    return m_support_isValid;
}

bool OAIVideoChannelList_data_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_followers_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_following_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_host_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_host_redundancy_allowed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_banners.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_local_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_support_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVideoChannelList_data_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
