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

/*
 * OAIServerConfig.h
 *
 * 
 */

#ifndef OAIServerConfig_H
#define OAIServerConfig_H

#include <QJsonObject>

#include "OAIServerConfig_autoBlacklist.h"
#include "OAIServerConfig_autoBlacklist_videos_ofUsers.h"
#include "OAIServerConfig_avatar.h"
#include "OAIServerConfig_followings.h"
#include "OAIServerConfig_import.h"
#include "OAIServerConfig_instance.h"
#include "OAIServerConfig_plugin.h"
#include "OAIServerConfig_search.h"
#include "OAIServerConfig_signup.h"
#include "OAIServerConfig_transcoding.h"
#include "OAIServerConfig_trending.h"
#include "OAIServerConfig_user.h"
#include "OAIServerConfig_video.h"
#include "OAIServerConfig_videoCaption.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIServerConfig_autoBlacklist;
class OAIServerConfig_avatar;
class OAIServerConfig_autoBlacklist_videos_ofUsers;
class OAIServerConfig_followings;
class OAIServerConfig_import;
class OAIServerConfig_instance;
class OAIServerConfig_plugin;
class OAIServerConfig_search;
class OAIServerConfig_signup;
class OAIServerConfig_transcoding;
class OAIServerConfig_trending;
class OAIServerConfig_user;
class OAIServerConfig_video;
class OAIServerConfig_videoCaption;

class OAIServerConfig : public OAIObject {
public:
    OAIServerConfig();
    OAIServerConfig(QString json);
    ~OAIServerConfig() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIServerConfig_autoBlacklist getAutoBlacklist() const;
    void setAutoBlacklist(const OAIServerConfig_autoBlacklist &auto_blacklist);
    bool is_auto_blacklist_Set() const;
    bool is_auto_blacklist_Valid() const;

    OAIServerConfig_avatar getAvatar() const;
    void setAvatar(const OAIServerConfig_avatar &avatar);
    bool is_avatar_Set() const;
    bool is_avatar_Valid() const;

    OAIServerConfig_autoBlacklist_videos_ofUsers getContactForm() const;
    void setContactForm(const OAIServerConfig_autoBlacklist_videos_ofUsers &contact_form);
    bool is_contact_form_Set() const;
    bool is_contact_form_Valid() const;

    OAIServerConfig_autoBlacklist_videos_ofUsers getEmail() const;
    void setEmail(const OAIServerConfig_autoBlacklist_videos_ofUsers &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    OAIServerConfig_followings getFollowings() const;
    void setFollowings(const OAIServerConfig_followings &followings);
    bool is_followings_Set() const;
    bool is_followings_Valid() const;

    OAIServerConfig_autoBlacklist_videos_ofUsers getHomepage() const;
    void setHomepage(const OAIServerConfig_autoBlacklist_videos_ofUsers &homepage);
    bool is_homepage_Set() const;
    bool is_homepage_Valid() const;

    OAIServerConfig_import getImport() const;
    void setImport(const OAIServerConfig_import &import);
    bool is_import_Set() const;
    bool is_import_Valid() const;

    OAIServerConfig_instance getInstance() const;
    void setInstance(const OAIServerConfig_instance &instance);
    bool is_instance_Set() const;
    bool is_instance_Valid() const;

    OAIServerConfig_plugin getPlugin() const;
    void setPlugin(const OAIServerConfig_plugin &plugin);
    bool is_plugin_Set() const;
    bool is_plugin_Valid() const;

    OAIServerConfig_search getSearch() const;
    void setSearch(const OAIServerConfig_search &search);
    bool is_search_Set() const;
    bool is_search_Valid() const;

    QString getServerCommit() const;
    void setServerCommit(const QString &server_commit);
    bool is_server_commit_Set() const;
    bool is_server_commit_Valid() const;

    QString getServerVersion() const;
    void setServerVersion(const QString &server_version);
    bool is_server_version_Set() const;
    bool is_server_version_Valid() const;

    OAIServerConfig_signup getSignup() const;
    void setSignup(const OAIServerConfig_signup &signup);
    bool is_signup_Set() const;
    bool is_signup_Valid() const;

    OAIServerConfig_plugin getTheme() const;
    void setTheme(const OAIServerConfig_plugin &theme);
    bool is_theme_Set() const;
    bool is_theme_Valid() const;

    OAIServerConfig_autoBlacklist_videos_ofUsers getTracker() const;
    void setTracker(const OAIServerConfig_autoBlacklist_videos_ofUsers &tracker);
    bool is_tracker_Set() const;
    bool is_tracker_Valid() const;

    OAIServerConfig_transcoding getTranscoding() const;
    void setTranscoding(const OAIServerConfig_transcoding &transcoding);
    bool is_transcoding_Set() const;
    bool is_transcoding_Valid() const;

    OAIServerConfig_trending getTrending() const;
    void setTrending(const OAIServerConfig_trending &trending);
    bool is_trending_Set() const;
    bool is_trending_Valid() const;

    OAIServerConfig_user getUser() const;
    void setUser(const OAIServerConfig_user &user);
    bool is_user_Set() const;
    bool is_user_Valid() const;

    OAIServerConfig_video getVideo() const;
    void setVideo(const OAIServerConfig_video &video);
    bool is_video_Set() const;
    bool is_video_Valid() const;

    OAIServerConfig_videoCaption getVideoCaption() const;
    void setVideoCaption(const OAIServerConfig_videoCaption &video_caption);
    bool is_video_caption_Set() const;
    bool is_video_caption_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIServerConfig_autoBlacklist m_auto_blacklist;
    bool m_auto_blacklist_isSet;
    bool m_auto_blacklist_isValid;

    OAIServerConfig_avatar m_avatar;
    bool m_avatar_isSet;
    bool m_avatar_isValid;

    OAIServerConfig_autoBlacklist_videos_ofUsers m_contact_form;
    bool m_contact_form_isSet;
    bool m_contact_form_isValid;

    OAIServerConfig_autoBlacklist_videos_ofUsers m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    OAIServerConfig_followings m_followings;
    bool m_followings_isSet;
    bool m_followings_isValid;

    OAIServerConfig_autoBlacklist_videos_ofUsers m_homepage;
    bool m_homepage_isSet;
    bool m_homepage_isValid;

    OAIServerConfig_import m_import;
    bool m_import_isSet;
    bool m_import_isValid;

    OAIServerConfig_instance m_instance;
    bool m_instance_isSet;
    bool m_instance_isValid;

    OAIServerConfig_plugin m_plugin;
    bool m_plugin_isSet;
    bool m_plugin_isValid;

    OAIServerConfig_search m_search;
    bool m_search_isSet;
    bool m_search_isValid;

    QString m_server_commit;
    bool m_server_commit_isSet;
    bool m_server_commit_isValid;

    QString m_server_version;
    bool m_server_version_isSet;
    bool m_server_version_isValid;

    OAIServerConfig_signup m_signup;
    bool m_signup_isSet;
    bool m_signup_isValid;

    OAIServerConfig_plugin m_theme;
    bool m_theme_isSet;
    bool m_theme_isValid;

    OAIServerConfig_autoBlacklist_videos_ofUsers m_tracker;
    bool m_tracker_isSet;
    bool m_tracker_isValid;

    OAIServerConfig_transcoding m_transcoding;
    bool m_transcoding_isSet;
    bool m_transcoding_isValid;

    OAIServerConfig_trending m_trending;
    bool m_trending_isSet;
    bool m_trending_isValid;

    OAIServerConfig_user m_user;
    bool m_user_isSet;
    bool m_user_isValid;

    OAIServerConfig_video m_video;
    bool m_video_isSet;
    bool m_video_isValid;

    OAIServerConfig_videoCaption m_video_caption;
    bool m_video_caption_isSet;
    bool m_video_caption_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIServerConfig)

#endif // OAIServerConfig_H
