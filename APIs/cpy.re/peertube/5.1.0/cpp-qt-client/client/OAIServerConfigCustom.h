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
 * OAIServerConfigCustom.h
 *
 * 
 */

#ifndef OAIServerConfigCustom_H
#define OAIServerConfigCustom_H

#include <QJsonObject>

#include "OAIServerConfigCustom_admin.h"
#include "OAIServerConfigCustom_cache.h"
#include "OAIServerConfigCustom_followers.h"
#include "OAIServerConfigCustom_import.h"
#include "OAIServerConfigCustom_instance.h"
#include "OAIServerConfigCustom_services.h"
#include "OAIServerConfigCustom_signup.h"
#include "OAIServerConfigCustom_theme.h"
#include "OAIServerConfigCustom_transcoding.h"
#include "OAIServerConfigCustom_user.h"
#include "OAIServerConfig_autoBlacklist.h"
#include "OAIServerConfig_autoBlacklist_videos_ofUsers.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIServerConfigCustom_admin;
class OAIServerConfig_autoBlacklist;
class OAIServerConfigCustom_cache;
class OAIServerConfig_autoBlacklist_videos_ofUsers;
class OAIServerConfigCustom_followers;
class OAIServerConfigCustom_import;
class OAIServerConfigCustom_instance;
class OAIServerConfigCustom_services;
class OAIServerConfigCustom_signup;
class OAIServerConfigCustom_theme;
class OAIServerConfigCustom_transcoding;
class OAIServerConfigCustom_user;

class OAIServerConfigCustom : public OAIObject {
public:
    OAIServerConfigCustom();
    OAIServerConfigCustom(QString json);
    ~OAIServerConfigCustom() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIServerConfigCustom_admin getAdmin() const;
    void setAdmin(const OAIServerConfigCustom_admin &admin);
    bool is_admin_Set() const;
    bool is_admin_Valid() const;

    OAIServerConfig_autoBlacklist getAutoBlacklist() const;
    void setAutoBlacklist(const OAIServerConfig_autoBlacklist &auto_blacklist);
    bool is_auto_blacklist_Set() const;
    bool is_auto_blacklist_Valid() const;

    OAIServerConfigCustom_cache getCache() const;
    void setCache(const OAIServerConfigCustom_cache &cache);
    bool is_cache_Set() const;
    bool is_cache_Valid() const;

    OAIServerConfig_autoBlacklist_videos_ofUsers getContactForm() const;
    void setContactForm(const OAIServerConfig_autoBlacklist_videos_ofUsers &contact_form);
    bool is_contact_form_Set() const;
    bool is_contact_form_Valid() const;

    OAIServerConfigCustom_followers getFollowers() const;
    void setFollowers(const OAIServerConfigCustom_followers &followers);
    bool is_followers_Set() const;
    bool is_followers_Valid() const;

    OAIServerConfigCustom_import getImport() const;
    void setImport(const OAIServerConfigCustom_import &import);
    bool is_import_Set() const;
    bool is_import_Valid() const;

    OAIServerConfigCustom_instance getInstance() const;
    void setInstance(const OAIServerConfigCustom_instance &instance);
    bool is_instance_Set() const;
    bool is_instance_Valid() const;

    OAIServerConfigCustom_services getServices() const;
    void setServices(const OAIServerConfigCustom_services &services);
    bool is_services_Set() const;
    bool is_services_Valid() const;

    OAIServerConfigCustom_signup getSignup() const;
    void setSignup(const OAIServerConfigCustom_signup &signup);
    bool is_signup_Set() const;
    bool is_signup_Valid() const;

    OAIServerConfigCustom_theme getTheme() const;
    void setTheme(const OAIServerConfigCustom_theme &theme);
    bool is_theme_Set() const;
    bool is_theme_Valid() const;

    OAIServerConfigCustom_transcoding getTranscoding() const;
    void setTranscoding(const OAIServerConfigCustom_transcoding &transcoding);
    bool is_transcoding_Set() const;
    bool is_transcoding_Valid() const;

    OAIServerConfigCustom_user getUser() const;
    void setUser(const OAIServerConfigCustom_user &user);
    bool is_user_Set() const;
    bool is_user_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIServerConfigCustom_admin m_admin;
    bool m_admin_isSet;
    bool m_admin_isValid;

    OAIServerConfig_autoBlacklist m_auto_blacklist;
    bool m_auto_blacklist_isSet;
    bool m_auto_blacklist_isValid;

    OAIServerConfigCustom_cache m_cache;
    bool m_cache_isSet;
    bool m_cache_isValid;

    OAIServerConfig_autoBlacklist_videos_ofUsers m_contact_form;
    bool m_contact_form_isSet;
    bool m_contact_form_isValid;

    OAIServerConfigCustom_followers m_followers;
    bool m_followers_isSet;
    bool m_followers_isValid;

    OAIServerConfigCustom_import m_import;
    bool m_import_isSet;
    bool m_import_isValid;

    OAIServerConfigCustom_instance m_instance;
    bool m_instance_isSet;
    bool m_instance_isValid;

    OAIServerConfigCustom_services m_services;
    bool m_services_isSet;
    bool m_services_isValid;

    OAIServerConfigCustom_signup m_signup;
    bool m_signup_isSet;
    bool m_signup_isValid;

    OAIServerConfigCustom_theme m_theme;
    bool m_theme_isSet;
    bool m_theme_isValid;

    OAIServerConfigCustom_transcoding m_transcoding;
    bool m_transcoding_isSet;
    bool m_transcoding_isValid;

    OAIServerConfigCustom_user m_user;
    bool m_user_isSet;
    bool m_user_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIServerConfigCustom)

#endif // OAIServerConfigCustom_H
