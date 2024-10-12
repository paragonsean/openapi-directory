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

#include "OAIVideosForXML_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVideosForXML_inner::OAIVideosForXML_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVideosForXML_inner::OAIVideosForXML_inner() {
    this->initializeModel();
}

OAIVideosForXML_inner::~OAIVideosForXML_inner() {}

void OAIVideosForXML_inner::initializeModel() {

    m_contentencoded_isSet = false;
    m_contentencoded_isValid = false;

    m_dccreator_isSet = false;
    m_dccreator_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_enclosure_isSet = false;
    m_enclosure_isValid = false;

    m_guid_isSet = false;
    m_guid_isValid = false;

    m_link_isSet = false;
    m_link_isValid = false;

    m_mediacategory_isSet = false;
    m_mediacategory_isValid = false;

    m_mediacommunity_isSet = false;
    m_mediacommunity_isValid = false;

    m_mediadescription_isSet = false;
    m_mediadescription_isValid = false;

    m_mediaembed_isSet = false;
    m_mediaembed_isValid = false;

    m_mediagroup_isSet = false;
    m_mediagroup_isValid = false;

    m_mediaplayer_isSet = false;
    m_mediaplayer_isValid = false;

    m_mediarating_isSet = false;
    m_mediarating_isValid = false;

    m_mediathumbnail_isSet = false;
    m_mediathumbnail_isValid = false;

    m_mediatitle_isSet = false;
    m_mediatitle_isValid = false;

    m_pub_date_isSet = false;
    m_pub_date_isValid = false;
}

void OAIVideosForXML_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVideosForXML_inner::fromJsonObject(QJsonObject json) {

    m_contentencoded_isValid = ::OpenAPI::fromJsonValue(m_contentencoded, json[QString("content:encoded")]);
    m_contentencoded_isSet = !json[QString("content:encoded")].isNull() && m_contentencoded_isValid;

    m_dccreator_isValid = ::OpenAPI::fromJsonValue(m_dccreator, json[QString("dc:creator")]);
    m_dccreator_isSet = !json[QString("dc:creator")].isNull() && m_dccreator_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_enclosure_isValid = ::OpenAPI::fromJsonValue(m_enclosure, json[QString("enclosure")]);
    m_enclosure_isSet = !json[QString("enclosure")].isNull() && m_enclosure_isValid;

    m_guid_isValid = ::OpenAPI::fromJsonValue(m_guid, json[QString("guid")]);
    m_guid_isSet = !json[QString("guid")].isNull() && m_guid_isValid;

    m_link_isValid = ::OpenAPI::fromJsonValue(m_link, json[QString("link")]);
    m_link_isSet = !json[QString("link")].isNull() && m_link_isValid;

    m_mediacategory_isValid = ::OpenAPI::fromJsonValue(m_mediacategory, json[QString("media:category")]);
    m_mediacategory_isSet = !json[QString("media:category")].isNull() && m_mediacategory_isValid;

    m_mediacommunity_isValid = ::OpenAPI::fromJsonValue(m_mediacommunity, json[QString("media:community")]);
    m_mediacommunity_isSet = !json[QString("media:community")].isNull() && m_mediacommunity_isValid;

    m_mediadescription_isValid = ::OpenAPI::fromJsonValue(m_mediadescription, json[QString("media:description")]);
    m_mediadescription_isSet = !json[QString("media:description")].isNull() && m_mediadescription_isValid;

    m_mediaembed_isValid = ::OpenAPI::fromJsonValue(m_mediaembed, json[QString("media:embed")]);
    m_mediaembed_isSet = !json[QString("media:embed")].isNull() && m_mediaembed_isValid;

    m_mediagroup_isValid = ::OpenAPI::fromJsonValue(m_mediagroup, json[QString("media:group")]);
    m_mediagroup_isSet = !json[QString("media:group")].isNull() && m_mediagroup_isValid;

    m_mediaplayer_isValid = ::OpenAPI::fromJsonValue(m_mediaplayer, json[QString("media:player")]);
    m_mediaplayer_isSet = !json[QString("media:player")].isNull() && m_mediaplayer_isValid;

    m_mediarating_isValid = ::OpenAPI::fromJsonValue(m_mediarating, json[QString("media:rating")]);
    m_mediarating_isSet = !json[QString("media:rating")].isNull() && m_mediarating_isValid;

    m_mediathumbnail_isValid = ::OpenAPI::fromJsonValue(m_mediathumbnail, json[QString("media:thumbnail")]);
    m_mediathumbnail_isSet = !json[QString("media:thumbnail")].isNull() && m_mediathumbnail_isValid;

    m_mediatitle_isValid = ::OpenAPI::fromJsonValue(m_mediatitle, json[QString("media:title")]);
    m_mediatitle_isSet = !json[QString("media:title")].isNull() && m_mediatitle_isValid;

    m_pub_date_isValid = ::OpenAPI::fromJsonValue(m_pub_date, json[QString("pubDate")]);
    m_pub_date_isSet = !json[QString("pubDate")].isNull() && m_pub_date_isValid;
}

QString OAIVideosForXML_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVideosForXML_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_contentencoded_isSet) {
        obj.insert(QString("content:encoded"), ::OpenAPI::toJsonValue(m_contentencoded));
    }
    if (m_dccreator_isSet) {
        obj.insert(QString("dc:creator"), ::OpenAPI::toJsonValue(m_dccreator));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_enclosure.isSet()) {
        obj.insert(QString("enclosure"), ::OpenAPI::toJsonValue(m_enclosure));
    }
    if (m_guid_isSet) {
        obj.insert(QString("guid"), ::OpenAPI::toJsonValue(m_guid));
    }
    if (m_link_isSet) {
        obj.insert(QString("link"), ::OpenAPI::toJsonValue(m_link));
    }
    if (m_mediacategory_isSet) {
        obj.insert(QString("media:category"), ::OpenAPI::toJsonValue(m_mediacategory));
    }
    if (m_mediacommunity.isSet()) {
        obj.insert(QString("media:community"), ::OpenAPI::toJsonValue(m_mediacommunity));
    }
    if (m_mediadescription_isSet) {
        obj.insert(QString("media:description"), ::OpenAPI::toJsonValue(m_mediadescription));
    }
    if (m_mediaembed.isSet()) {
        obj.insert(QString("media:embed"), ::OpenAPI::toJsonValue(m_mediaembed));
    }
    if (m_mediagroup.size() > 0) {
        obj.insert(QString("media:group"), ::OpenAPI::toJsonValue(m_mediagroup));
    }
    if (m_mediaplayer.isSet()) {
        obj.insert(QString("media:player"), ::OpenAPI::toJsonValue(m_mediaplayer));
    }
    if (m_mediarating_isSet) {
        obj.insert(QString("media:rating"), ::OpenAPI::toJsonValue(m_mediarating));
    }
    if (m_mediathumbnail.isSet()) {
        obj.insert(QString("media:thumbnail"), ::OpenAPI::toJsonValue(m_mediathumbnail));
    }
    if (m_mediatitle_isSet) {
        obj.insert(QString("media:title"), ::OpenAPI::toJsonValue(m_mediatitle));
    }
    if (m_pub_date_isSet) {
        obj.insert(QString("pubDate"), ::OpenAPI::toJsonValue(m_pub_date));
    }
    return obj;
}

QString OAIVideosForXML_inner::getContentencoded() const {
    return m_contentencoded;
}
void OAIVideosForXML_inner::setContentencoded(const QString &contentencoded) {
    m_contentencoded = contentencoded;
    m_contentencoded_isSet = true;
}

bool OAIVideosForXML_inner::is_contentencoded_Set() const{
    return m_contentencoded_isSet;
}

bool OAIVideosForXML_inner::is_contentencoded_Valid() const{
    return m_contentencoded_isValid;
}

QString OAIVideosForXML_inner::getDccreator() const {
    return m_dccreator;
}
void OAIVideosForXML_inner::setDccreator(const QString &dccreator) {
    m_dccreator = dccreator;
    m_dccreator_isSet = true;
}

bool OAIVideosForXML_inner::is_dccreator_Set() const{
    return m_dccreator_isSet;
}

bool OAIVideosForXML_inner::is_dccreator_Valid() const{
    return m_dccreator_isValid;
}

QString OAIVideosForXML_inner::getDescription() const {
    return m_description;
}
void OAIVideosForXML_inner::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIVideosForXML_inner::is_description_Set() const{
    return m_description_isSet;
}

bool OAIVideosForXML_inner::is_description_Valid() const{
    return m_description_isValid;
}

OAIVideosForXML_inner_enclosure OAIVideosForXML_inner::getEnclosure() const {
    return m_enclosure;
}
void OAIVideosForXML_inner::setEnclosure(const OAIVideosForXML_inner_enclosure &enclosure) {
    m_enclosure = enclosure;
    m_enclosure_isSet = true;
}

bool OAIVideosForXML_inner::is_enclosure_Set() const{
    return m_enclosure_isSet;
}

bool OAIVideosForXML_inner::is_enclosure_Valid() const{
    return m_enclosure_isValid;
}

QString OAIVideosForXML_inner::getGuid() const {
    return m_guid;
}
void OAIVideosForXML_inner::setGuid(const QString &guid) {
    m_guid = guid;
    m_guid_isSet = true;
}

bool OAIVideosForXML_inner::is_guid_Set() const{
    return m_guid_isSet;
}

bool OAIVideosForXML_inner::is_guid_Valid() const{
    return m_guid_isValid;
}

QString OAIVideosForXML_inner::getLink() const {
    return m_link;
}
void OAIVideosForXML_inner::setLink(const QString &link) {
    m_link = link;
    m_link_isSet = true;
}

bool OAIVideosForXML_inner::is_link_Set() const{
    return m_link_isSet;
}

bool OAIVideosForXML_inner::is_link_Valid() const{
    return m_link_isValid;
}

qint32 OAIVideosForXML_inner::getMediacategory() const {
    return m_mediacategory;
}
void OAIVideosForXML_inner::setMediacategory(const qint32 &mediacategory) {
    m_mediacategory = mediacategory;
    m_mediacategory_isSet = true;
}

bool OAIVideosForXML_inner::is_mediacategory_Set() const{
    return m_mediacategory_isSet;
}

bool OAIVideosForXML_inner::is_mediacategory_Valid() const{
    return m_mediacategory_isValid;
}

OAIVideosForXML_inner_media_community OAIVideosForXML_inner::getMediacommunity() const {
    return m_mediacommunity;
}
void OAIVideosForXML_inner::setMediacommunity(const OAIVideosForXML_inner_media_community &mediacommunity) {
    m_mediacommunity = mediacommunity;
    m_mediacommunity_isSet = true;
}

bool OAIVideosForXML_inner::is_mediacommunity_Set() const{
    return m_mediacommunity_isSet;
}

bool OAIVideosForXML_inner::is_mediacommunity_Valid() const{
    return m_mediacommunity_isValid;
}

QString OAIVideosForXML_inner::getMediadescription() const {
    return m_mediadescription;
}
void OAIVideosForXML_inner::setMediadescription(const QString &mediadescription) {
    m_mediadescription = mediadescription;
    m_mediadescription_isSet = true;
}

bool OAIVideosForXML_inner::is_mediadescription_Set() const{
    return m_mediadescription_isSet;
}

bool OAIVideosForXML_inner::is_mediadescription_Valid() const{
    return m_mediadescription_isValid;
}

OAIVideosForXML_inner_media_embed OAIVideosForXML_inner::getMediaembed() const {
    return m_mediaembed;
}
void OAIVideosForXML_inner::setMediaembed(const OAIVideosForXML_inner_media_embed &mediaembed) {
    m_mediaembed = mediaembed;
    m_mediaembed_isSet = true;
}

bool OAIVideosForXML_inner::is_mediaembed_Set() const{
    return m_mediaembed_isSet;
}

bool OAIVideosForXML_inner::is_mediaembed_Valid() const{
    return m_mediaembed_isValid;
}

QList<OAIVideosForXML_inner_media_group_inner> OAIVideosForXML_inner::getMediagroup() const {
    return m_mediagroup;
}
void OAIVideosForXML_inner::setMediagroup(const QList<OAIVideosForXML_inner_media_group_inner> &mediagroup) {
    m_mediagroup = mediagroup;
    m_mediagroup_isSet = true;
}

bool OAIVideosForXML_inner::is_mediagroup_Set() const{
    return m_mediagroup_isSet;
}

bool OAIVideosForXML_inner::is_mediagroup_Valid() const{
    return m_mediagroup_isValid;
}

OAIVideosForXML_inner_media_player OAIVideosForXML_inner::getMediaplayer() const {
    return m_mediaplayer;
}
void OAIVideosForXML_inner::setMediaplayer(const OAIVideosForXML_inner_media_player &mediaplayer) {
    m_mediaplayer = mediaplayer;
    m_mediaplayer_isSet = true;
}

bool OAIVideosForXML_inner::is_mediaplayer_Set() const{
    return m_mediaplayer_isSet;
}

bool OAIVideosForXML_inner::is_mediaplayer_Valid() const{
    return m_mediaplayer_isValid;
}

QString OAIVideosForXML_inner::getMediarating() const {
    return m_mediarating;
}
void OAIVideosForXML_inner::setMediarating(const QString &mediarating) {
    m_mediarating = mediarating;
    m_mediarating_isSet = true;
}

bool OAIVideosForXML_inner::is_mediarating_Set() const{
    return m_mediarating_isSet;
}

bool OAIVideosForXML_inner::is_mediarating_Valid() const{
    return m_mediarating_isValid;
}

OAIVideosForXML_inner_media_thumbnail OAIVideosForXML_inner::getMediathumbnail() const {
    return m_mediathumbnail;
}
void OAIVideosForXML_inner::setMediathumbnail(const OAIVideosForXML_inner_media_thumbnail &mediathumbnail) {
    m_mediathumbnail = mediathumbnail;
    m_mediathumbnail_isSet = true;
}

bool OAIVideosForXML_inner::is_mediathumbnail_Set() const{
    return m_mediathumbnail_isSet;
}

bool OAIVideosForXML_inner::is_mediathumbnail_Valid() const{
    return m_mediathumbnail_isValid;
}

QString OAIVideosForXML_inner::getMediatitle() const {
    return m_mediatitle;
}
void OAIVideosForXML_inner::setMediatitle(const QString &mediatitle) {
    m_mediatitle = mediatitle;
    m_mediatitle_isSet = true;
}

bool OAIVideosForXML_inner::is_mediatitle_Set() const{
    return m_mediatitle_isSet;
}

bool OAIVideosForXML_inner::is_mediatitle_Valid() const{
    return m_mediatitle_isValid;
}

QDateTime OAIVideosForXML_inner::getPubDate() const {
    return m_pub_date;
}
void OAIVideosForXML_inner::setPubDate(const QDateTime &pub_date) {
    m_pub_date = pub_date;
    m_pub_date_isSet = true;
}

bool OAIVideosForXML_inner::is_pub_date_Set() const{
    return m_pub_date_isSet;
}

bool OAIVideosForXML_inner::is_pub_date_Valid() const{
    return m_pub_date_isValid;
}

bool OAIVideosForXML_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_contentencoded_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dccreator_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enclosure.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_guid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mediacategory_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mediacommunity.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_mediadescription_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mediaembed.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_mediagroup.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_mediaplayer.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_mediarating_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mediathumbnail.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_mediatitle_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pub_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVideosForXML_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
