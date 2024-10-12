/**
 * Trakt API
 * At Trakt, we collect lots of interesting information about what tv shows and movies everyone is watching. Part of the fun with such data is making it available for anyone to mash up and use on their own site or app. The Trakt API was made just for this purpose. It is very easy to use, you basically call a URL and get some JSON back.  More complex API calls (such as adding a movie or show to your collection) involve sending us data. These are still easy to use, you simply POST some JSON data to a specific URL.  Make sure to check out the [**Required Headers**](#introduction/required-headers) and [**Authentication**](#reference/authentication-oauth) sections for more info on what needs to be sent with each API call. Also check out the [**Terminology**](#introduction/terminology) section insight into the features Trakt supports.  # Create an App  To use the Trakt API, you'll need to [**create a new API app**](https://trakt.tv/oauth/applications/new).  # Stay Connected  API discussion and bugs should be posted in the [**GitHub Developer Forum**](https://github.com/trakt/api-help/issues) and *watch* the repository if you'd like to get notifications. Make sure to follow our [**API Blog**](https://apiblog.trakt.tv) and [**@traktapi on Twitter**](https://twitter.com/traktapi) too.  # API URL  The API should always be accessed over SSL.  ``` https://api.trakt.tv ```  If you would like to use our sandbox environment to not fill production with test data, use this URL over SSL. **Note:** Staging is a completely separate environment, so you'll need to [**create a new API app on staging**](https://staging.trakt.tv/oauth/applications/new).  ``` https://api-staging.trakt.tv ```  # Verbs  The API uses restful verbs.  | Verb | Description | |---|---| | `GET` | Select one or more items. Success returns `200` status code. | | `POST` | Create a new item. Success returns `201` status code. | | `PUT` | Update an item. Success returns `200` status code. | | `DELETE` | Delete an item. Success returns `200` or `204` status code. |  # Status Codes  The API will respond with one of the following HTTP status codes.  | Code | Description | |---|---| | `200` | Success | `201` | Success - *new resource created (POST)* | `204` | Success - *no content to return (DELETE)* | `400` | Bad Request - *request couldn't be parsed* | `401` | Unauthorized - *OAuth must be provided* | `403` | Forbidden - *invalid API key or unapproved app* | `404` | Not Found - *method exists, but no record found* | `405` | Method Not Found - *method doesn't exist* | `409` | Conflict - *resource already created* | `412` | Precondition Failed - *use application/json content type* | `420` | Account Limit Exceeded - *list count, item count, etc* | `422` | Unprocessable Entity - *validation errors* | `423` | Locked User Account - *have the user contact support* | `426` | VIP Only - *user must upgrade to VIP* | `429` | Rate Limit Exceeded | `500` | Server Error - *please open a support ticket* | `502` | Service Unavailable - *server overloaded (try again in 30s)* | `503` | Service Unavailable - *server overloaded (try again in 30s)* | `504` | Service Unavailable - *server overloaded (try again in 30s)* | `520` | Service Unavailable - *Cloudflare error* | `521` | Service Unavailable - *Cloudflare error* | `522` | Service Unavailable - *Cloudflare error*  # Required Headers  You'll need to send some headers when making API calls to identify your application, set the version and set the content type to JSON.  | Header | Value | |---|---| | `Content-type` <span style=\"color:red;\">*</a> | `application/json` | | `trakt-api-key` <span style=\"color:red;\">*</a> | Your `client_id` listed under your Trakt applications. | | `trakt-api-version` <span style=\"color:red;\">*</a> | `2` | API version to use.  All `POST`, `PUT`, and `DELETE` methods require a valid OAuth `access_token`. Some `GET` calls require OAuth and others will return user specific data if OAuth is sent. Methods that &#128274; **require** or have &#128275; **optional** OAuth will be indicated.  Your OAuth library should take care of sending the auth headers for you, but for reference here's how the Bearer token should be sent.  | Header | Value | |---|---| | `Authorization` | `Bearer [access_token]` |  # Rate Limiting  All API methods are rate limited. A `429` HTTP status code is returned when the limit has been exceeded. Check the headers for detailed info, then try your API call in `Retry-After` seconds.  | Header | Value | |---|---| | `X-Ratelimit` | `{\"name\":\"UNAUTHED_API_GET_LIMIT\",\"period\":300,\"limit\":1000,\"remaining\":0,\"until\":\"2020-10-10T00:24:00Z\"}` | | `Retry-After` | `10` |  Here are the current limits. There are separate limits for authed (user level) and unauthed (application level) calls. We'll continue to adjust these limits to optimize API performance for everyone. The goal is to prevent API abuse and poor coding, but allow users to use apps normally.  | Name | Verb | Methods | Limit | |---|---|---|---| | `AUTHED_API_POST_LIMIT` | `POST`, `PUT`, `DELETE` | all | 1 call per second | | `AUTHED_API_GET_LIMIT` | `GET` | all | 1000 calls every 5 minutes | | `UNAUTHED_API_GET_LIMIT` | `GET` | all | 1000 calls every 5 minutes |  # Locked User Account  A `423` HTTP status code is returned when the OAuth user has a locked user account. Please instruct the user to [**contact Trakt support**](https://support.trakt.tv) so we can fix their account. API access will be suspended for the user until we fix their account.  # VIP Methods  Some API methods are tagged 🔥 **VIP Only**. A `426` HTTP status code is returned when the user isn't a VIP, indicating they need to sign up for [**Trakt VIP**](https://trakt.tv/vip) in order to use this method. In your app, please open a browser to `X-Upgrade-URL` so the user can sign up for Trakt VIP.  | Header | Value | |---|---| | `X-Upgrade-URL` | `https://trakt.tv/vip` |  Some API methods are tagged 🔥 **VIP Enhanced**. A `420` HTTP status code is returned when the user has exceeded their account limit. Signing up for [**Trakt VIP**](https://trakt.tv/vip) will increase these limits. If the user isn't a VIP, please open a browser to `X-Upgrade-URL` so the user can sign up for Trakt VIP. If they are already VIP and still exceeded the limit, please display a message indicating this.  | Header | Value | |---|---| | `X-Upgrade-URL` | `https://trakt.tv/vip` | | `X-VIP-User` | `true` or `false` | | `X-Account-Limit` | Limit allowed. |  # Pagination  Some methods are paginated. Methods with &#128196; **Pagination** will load 1 page of 10 items by default. Methods with &#128196; **Pagination Optional** will load all items by default. In either case, append a query string like `?page={page}&limit={limit}` to the URL to influence the results.  | Parameter | Type | Default | Value | |---|---|---|---| | `page` | integer | `1` | Number of page of results to be returned. | | `limit` | integer | `10` | Number of results to return per page. |  All paginated methods will return these HTTP headers.  | Header | Value | |---|---| | `X-Pagination-Page` | Current page. | | `X-Pagination-Limit` | Items per page. | | `X-Pagination-Page-Count` | Total number of pages. | | `X-Pagination-Item-Count` | Total number of items. |  # Extended Info  By default, all methods will return minimal info for movies, shows, episodes, people, and users. Minimal info is typically all you need to match locally cached items and includes the `title`, `year`, and `ids`. However, you can request different extended levels of information by adding `?extended={level}` to the URL. Send a comma separated string to get multiple types of extended info.  **Note:** This returns a lot of extra data, so please only use extended parameters if you actually need them!  | Level | Description | |---|---| | `full` | Complete info for an item. | `metadata` | **Collection only.** Additional video and audio info.  # Filters  Some `movies`, `shows`, `calendars`,  and `search` methods support additional filters and will be tagged with &#127898; **Filters**. Applying these filters refines the results and helps your users to more easily discover new items.  Add a query string (i.e. `?years=2016&genres=action`) with any filters you want to use. Some filters allow multiples which can be sent as comma delimited parameters. For example, `?genres=action,adventure` would match the `action` OR `adventure` genre.  **Note:** Make sure to properly URL encode the parameters including spaces and special characters.  #### Common Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | `query` | | `batman` | Search titles and descriptions. | | `years` | | `2016` | 4 digit year or range of years. | | `genres` | &#10003; | `action` | [Genre slugs.](#reference/genres) | | `languages` | &#10003; | `en` | [2 character language code.](#reference/languages) | | `countries` | &#10003; | `us` | [2 character country code.](#reference/countries) | | `runtimes` | | `30-90` | Range in minutes. | | `studios` | &#10003; | `marvel-studios` | Studio slugs. |  #### Rating Filters  Trakt, TMDB, and IMDB ratings apply to `movies`, `shows`, and `episodes`. Rotten Tomatoes and Metacritic apply to `movies`.  | Parameter | Multiples | Example | Value | |---|---|---|---| | `ratings` | | `75-100` | Trakt rating range between `0` and `100`. | | `votes` | | `5000-10000` | Trakt vote count between `0` and `100000`. | | `tmdb_ratings` | | `5.5-10.0` | TMDB rating range between `0.0` and `10.0`. | | `tmdb_votes` | | `5000-10000` | TMDB vote count between `0` and `100000`. | | `imdb_ratings` | | `5.5-10.0` | IMDB rating range between `0.0` and `10.0`. | | `imdb_votes` | | `5000-10000` | IMDB vote count between `0` and `3000000`. | | `rt_meters` | | `5.5-10.0` | Rotten Tomatoes meter range between `0` and `100`. | | `metascores` | | `5.5-10.0` | Metacritic score range between `0` and `100`. |  #### Movie Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | `certifications` | &#10003; | `pg-13` | US content certification. |  #### Show Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | `certifications` | &#10003; | `tv-pg` | US content certification. | | `networks` | &#10003; | `HBO` | Network name. | | `status` | &#10003; | `ended` | Set to `returning series`, `continuing`, `in production`, `planned`, `upcoming`,  `pilot`, `canceled`, or `ended`. |  # CORS  When creating your API app, specify the JavaScript (CORS) origins you'll be using. We use these origins to return the headers needed for CORS.  # Dates  All dates will be GMT and returned in the ISO 8601 format like `2014-09-01T09:10:11.000Z`. Adjust accordingly in your app for the user's local timezone.  # Emojis  We use short codes for emojis like `:smiley:` and `:raised_hands:` and render them on the Trakt website using [**JoyPixels**](https://www.joypixels.com/) _(verion 6.6.0)_. Methods that support emojis are tagged with &#128513; **Emojis**. For POST methods, you can send standard unicode emojis and we'll automatically convert them to short codes. For GET methods, we'll return the short codes and it's up to your app to convert them back to unicode emojis.  # Standard Media Objects  All methods will accept or return standard media objects for `movie`, `show`, `season`, `episode`, `person`, and `user` items. Here are examples for all minimal objects.  #### movie  ``` {     \"title\": \"Batman Begins\",     \"year\": 2005,     \"ids\": {         \"trakt\": 1,         \"slug\": \"batman-begins-2005\",         \"imdb\": \"tt0372784\",         \"tmdb\": 272     } } ```  #### show  ``` {     \"title\": \"Breaking Bad\",     \"year\": 2008,     \"ids\": {         \"trakt\": 1,         \"slug\": \"breaking-bad\",         \"tvdb\": 81189,         \"imdb\": \"tt0903747\",         \"tmdb\": 1396     } } ```  #### season  ``` {     \"number\": 0,     \"ids\": {         \"trakt\": 1,         \"tvdb\": 439371,         \"tmdb\": 3577     } } ```  #### episode  ``` {     \"season\": 1,     \"number\": 1,     \"title\": \"Pilot\",     \"ids\": {         \"trakt\": 16,         \"tvdb\": 349232,         \"imdb\": \"tt0959621\",         \"tmdb\": 62085     } } ```  #### person  ``` {     \"name\": \"Bryan Cranston\",     \"ids\": {         \"trakt\": 142,         \"slug\": \"bryan-cranston\",         \"imdb\": \"nm0186505\",         \"tmdb\": 17419     } } ```  #### user  ``` {     \"username\": \"sean\",     \"private\": false,     \"name\": \"Sean Rudford\",     \"vip\": true,     \"vip_ep\": true,     \"ids\": {         \"slug\": \"sean\"     } } ```  # Images  The standard media objects for all `movie`, `show`, `season`, `episode`, and `person` items include an `ids` object. These `ids` map to other services like [TMDB](https://www.themoviedb.org), [TVDB](https://thetvdb.com), [Fanart.tv](https://fanart.tv), [IMDB](https://www.imdb.com), and [OMDB](https://www.omdbapi.com/).  Most of these services have free APIs you can use to grab lots of great looking images. Here’s a chart to help you find the best artwork for your app. [**We also wrote an article to help with this.**](https://apiblog.trakt.tv/how-to-find-the-best-images-516045bcc3b6)  | Media | Type | [TMDB](https://developers.themoviedb.org/3) | [TVDB](https://api.thetvdb.com/swagger) | [Fanart.tv](http://docs.fanarttv.apiary.io) | [OMDB](https://www.omdbapi.com) | |---|---|---|---|---|---| | `shows` | `poster` | &#10003; | &#10003; | &#10003; | &#10003; | |  | `fanart` | &#10003; | &#10003; | &#10003; |  | |  | `banner` |  | &#10003; | &#10003; |  | |  | `logo` |  |  | &#10003; |  | |  | `clearart` |  |  | &#10003; |  | |  | `thumb` |  |  | &#10003; |  | | `seasons` | `poster` | &#10003; | &#10003; | &#10003; |  | |  | `banner` |  | &#10003; | &#10003; |  | |  | `thumb` |  |  | &#10003; |  | | `episodes` | `screenshot` | &#10003; | &#10003; |  |  | | `movies` | `poster` | &#10003; |  | &#10003; | &#10003; | |  | `fanart` | &#10003; |  | &#10003; |  | |  | `banner` |  |  | &#10003; |  | |  | `logo` |  |  | &#10003; |  | |  | `clearart` |  |  | &#10003; |  | |  | `thumb` |  |  | &#10003; |  | | `person` | `headshot` | &#10003; |  |  |  | |  | `character` |  | &#10003; |  |  |  # Website Media Links  There are several ways to construct direct links to media on the Trakt website. The website itself uses slugs so the URLs are more readable.  | Type | URL | |---|---| | `movie` | `/movies/:slug` | | `show` | `/shows/:slug` | | `season` | `/shows/:slug/seasons/:num` | | `episode` | `/shows/:slug/seasons/:num/episodes/:num` | | `person` | `/people/:slug` | | `comment` | `/comments/:id` | | `list` | `/lists/:id` |  You can also create links using the Trakt, IMDB, TMDB, or TVDB IDs. We recommend using the Trakt ID if possible since that will always have full coverage. If you use the search url without an `id_type` it will return search results if multiple items are found.  | Type | URL | |---|---| | `trakt` | `/search/trakt/:id` | |  | `/search/trakt/:id?id_type=movie` | |  | `/search/trakt/:id?id_type=show` | |  | `/search/trakt/:id?id_type=season` | |  | `/search/trakt/:id?id_type=episode` | |  | `/search/trakt/:id?id_type=person` | | `imdb` | `/search/imdb/:id` | | `tmdb` | `/search/tmdb/:id` | |  | `/search/tmdb/:id?id_type=movie` | |  | `/search/tmdb/:id?id_type=show` | |  | `/search/tmdb/:id?id_type=episode` | |  | `/search/tmdb/:id?id_type=person` | | `tvdb` | `/search/tvdb/:id` | |  | `/search/tvdb/:id?id_type=show` | |  | `/search/tvdb/:id?id_type=episode` |  # Third Party Libraries  All of the libraries listed below are user contributed. If you find a bug or missing feature, please contact the developer directly. These might help give your project a head start, but we can't provide direct support for any of these libraries. Please help us keep this list up to date.  | Language | Name | Repository | |---|---|---| | `C#` | `Trakt.NET` | https://github.com/henrikfroehling/Trakt.NET | |  | `TraktSharp` | https://github.com/wwarby/TraktSharp | | `C++` | `libtraqt` | https://github.com/RobertMe/libtraqt | | `Clojure` | `clj-trakt` | https://github.com/niamu/clj-trakt | | `Java` | `trakt-java` | https://github.com/UweTrottmann/trakt-java | | `Kotlin` | `trakt-api` | https://github.com/MoviebaseApp/trakt-api | | `Node.js` | `Trakt.tv` | https://github.com/vankasteelj/trakt.tv | |  | `TraktApi2` | https://github.com/PatrickE94/traktapi2 | | `Python` | `trakt.py` | https://github.com/fuzeman/trakt.py | |  | `pyTrakt` | https://github.com/moogar0880/PyTrakt | | `R` | `tRakt` | https://github.com/jemus42/tRakt | | `React Native` | `nodeless-trakt` | https://github.com/kdemoya/nodeless-trakt | | `Ruby` | `omniauth-trakt` | https://github.com/wafcio/omniauth-trakt | |  | `omniauth-trakt` | https://github.com/alextakitani/omniauth-trakt | | `Swift` | `TraktKit` | https://github.com/MaxHasADHD/TraktKit | |  | `AKTrakt` | https://github.com/arsonik/AKTrakt |  # Terminology  Trakt has a lot of features and here's a chart to help explain the differences between some of them.  | Term | Description | |---|---| | `scrobble` | Automatic way to track what a user is watching in a media center. | | `checkin` | Manual action used by mobile apps allowing the user to indicate what they are watching right now. | | `history` | All watched items (scrobbles, checkins, watched) for a user. | | `collection` | Items a user has available to watch including Blu-Rays, DVDs, and digital downloads. | | `watchlist` | Items a user wants to watch in the future. Once watched, they are auto removed from this list. | | `list` | Personal list for any purpose. Items are not auto removed from any personal lists. | | `recommendations` | Movies and TV shows a user personally recommends to others. |
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIUsersApi_H
#define OAI_OAIUsersApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAdd_hidden_items_request.h"
#include "OAIAdd_items_to_personal_list_request.h"
#include "OAICreate_personal_list_request.h"
#include "OAIRemove_items_from_personal_list_request.h"
#include "OAIReorder_a_user_s_lists_request.h"
#include "OAIReorder_personally_recommended_items_request.h"
#include "OAIUpdate_personal_list_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIUsersApi : public QObject {
    Q_OBJECT

public:
    OAIUsersApi(const int timeOut = 0);
    ~OAIUsersApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  section QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    * @param[in]  oai_add_hidden_items_request OAIAdd_hidden_items_request [optional]
    */
    virtual void add_hidden_items(const QString &section, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIAdd_hidden_items_request> &oai_add_hidden_items_request = ::OpenAPI::OptionalParam<OAIAdd_hidden_items_request>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  list_id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    * @param[in]  oai_add_items_to_personal_list_request OAIAdd_items_to_personal_list_request [optional]
    */
    virtual void add_items_to_personal_list(const QString &id, const QString &list_id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIAdd_items_to_personal_list_request> &oai_add_items_to_personal_list_request = ::OpenAPI::OptionalParam<OAIAdd_items_to_personal_list_request>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void approve_follow_request(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    * @param[in]  oai_create_personal_list_request OAICreate_personal_list_request [optional]
    */
    virtual void create_personal_list(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAICreate_personal_list_request> &oai_create_personal_list_request = ::OpenAPI::OptionalParam<OAICreate_personal_list_request>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  list_id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void delete_a_users_personal_list(const QString &id, const QString &list_id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void deny_follow_request(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void follow_this_user(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_a_users_personal_lists(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_all_lists_a_user_can_collaborate_on(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  comment_type QString [required]
    * @param[in]  type QString [required]
    * @param[in]  include_replies QString [optional]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_comments(const QString &id, const QString &comment_type, const QString &type, const ::OpenAPI::OptionalParam<QString> &include_replies = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_follow_requests(const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_followers(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_following(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_friends(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  section QString [required]
    * @param[in]  type QString [optional]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_hidden_items(const QString &section, const ::OpenAPI::OptionalParam<QString> &type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  list_id QString [required]
    * @param[in]  type QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_items_on_a_personal_list(const QString &id, const QString &list_id, const QString &type, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  type QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_likes(const QString &id, const QString &type, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_pending_following_requests(const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  list_id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_personal_list(const QString &id, const QString &list_id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  section QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_saved_filters(const QString &section, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_stats(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_user_profile(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_watching(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  list_id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void like_a_list(const QString &id, const QString &list_id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  section QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    * @param[in]  oai_add_hidden_items_request OAIAdd_hidden_items_request [optional]
    */
    virtual void remove_hidden_items(const QString &section, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIAdd_hidden_items_request> &oai_add_hidden_items_request = ::OpenAPI::OptionalParam<OAIAdd_hidden_items_request>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  list_id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    * @param[in]  oai_remove_items_from_personal_list_request OAIRemove_items_from_personal_list_request [optional]
    */
    virtual void remove_items_from_personal_list(const QString &id, const QString &list_id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIRemove_items_from_personal_list_request> &oai_remove_items_from_personal_list_request = ::OpenAPI::OptionalParam<OAIRemove_items_from_personal_list_request>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  list_id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void remove_like_on_a_list(const QString &id, const QString &list_id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    * @param[in]  oai_reorder_a_user_s_lists_request OAIReorder_a_user_s_lists_request [optional]
    */
    virtual void reorder_a_users_lists(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIReorder_a_user_s_lists_request> &oai_reorder_a_user_s_lists_request = ::OpenAPI::OptionalParam<OAIReorder_a_user_s_lists_request>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  list_id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    * @param[in]  oai_reorder_personally_recommended_items_request OAIReorder_personally_recommended_items_request [optional]
    */
    virtual void reorder_items_on_a_list(const QString &id, const QString &list_id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIReorder_personally_recommended_items_request> &oai_reorder_personally_recommended_items_request = ::OpenAPI::OptionalParam<OAIReorder_personally_recommended_items_request>());

    /**
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void retrieve_settings(const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void unfollow_this_user(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  list_id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    * @param[in]  oai_update_personal_list_request OAIUpdate_personal_list_request [optional]
    */
    virtual void update_personal_list(const QString &id, const QString &list_id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIUpdate_personal_list_request> &oai_update_personal_list_request = ::OpenAPI::OptionalParam<OAIUpdate_personal_list_request>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  type QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void usersIdCollectionTypeGet(const QString &id, const QString &type, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  type QString [required]
    * @param[in]  item_id qint32 [required]
    * @param[in]  start_at QString [optional]
    * @param[in]  end_at QString [optional]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void usersIdHistoryTypeItemIdGet(const QString &id, const QString &type, const qint32 &item_id, const ::OpenAPI::OptionalParam<QString> &start_at = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &end_at = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  list_id QString [required]
    * @param[in]  sort QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void usersIdListsListIdCommentsSortGet(const QString &id, const QString &list_id, const QString &sort, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  list_id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void usersIdListsListIdLikesGet(const QString &id, const QString &list_id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  type QString [required]
    * @param[in]  rating qint32 [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void usersIdRatingsTypeRatingGet(const QString &id, const QString &type, const qint32 &rating, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  type QString [required]
    * @param[in]  sort QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void usersIdRecommendationsTypeSortGet(const QString &id, const QString &type, const QString &sort, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  type QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void usersIdWatchedTypeGet(const QString &id, const QString &type, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  type QString [required]
    * @param[in]  sort QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void usersIdWatchlistTypeSortGet(const QString &id, const QString &type, const QString &sort, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void add_hidden_itemsCallback(OAIHttpRequestWorker *worker);
    void add_items_to_personal_listCallback(OAIHttpRequestWorker *worker);
    void approve_follow_requestCallback(OAIHttpRequestWorker *worker);
    void create_personal_listCallback(OAIHttpRequestWorker *worker);
    void delete_a_users_personal_listCallback(OAIHttpRequestWorker *worker);
    void deny_follow_requestCallback(OAIHttpRequestWorker *worker);
    void follow_this_userCallback(OAIHttpRequestWorker *worker);
    void get_a_users_personal_listsCallback(OAIHttpRequestWorker *worker);
    void get_all_lists_a_user_can_collaborate_onCallback(OAIHttpRequestWorker *worker);
    void get_commentsCallback(OAIHttpRequestWorker *worker);
    void get_follow_requestsCallback(OAIHttpRequestWorker *worker);
    void get_followersCallback(OAIHttpRequestWorker *worker);
    void get_followingCallback(OAIHttpRequestWorker *worker);
    void get_friendsCallback(OAIHttpRequestWorker *worker);
    void get_hidden_itemsCallback(OAIHttpRequestWorker *worker);
    void get_items_on_a_personal_listCallback(OAIHttpRequestWorker *worker);
    void get_likesCallback(OAIHttpRequestWorker *worker);
    void get_pending_following_requestsCallback(OAIHttpRequestWorker *worker);
    void get_personal_listCallback(OAIHttpRequestWorker *worker);
    void get_saved_filtersCallback(OAIHttpRequestWorker *worker);
    void get_statsCallback(OAIHttpRequestWorker *worker);
    void get_user_profileCallback(OAIHttpRequestWorker *worker);
    void get_watchingCallback(OAIHttpRequestWorker *worker);
    void like_a_listCallback(OAIHttpRequestWorker *worker);
    void remove_hidden_itemsCallback(OAIHttpRequestWorker *worker);
    void remove_items_from_personal_listCallback(OAIHttpRequestWorker *worker);
    void remove_like_on_a_listCallback(OAIHttpRequestWorker *worker);
    void reorder_a_users_listsCallback(OAIHttpRequestWorker *worker);
    void reorder_items_on_a_listCallback(OAIHttpRequestWorker *worker);
    void retrieve_settingsCallback(OAIHttpRequestWorker *worker);
    void unfollow_this_userCallback(OAIHttpRequestWorker *worker);
    void update_personal_listCallback(OAIHttpRequestWorker *worker);
    void usersIdCollectionTypeGetCallback(OAIHttpRequestWorker *worker);
    void usersIdHistoryTypeItemIdGetCallback(OAIHttpRequestWorker *worker);
    void usersIdListsListIdCommentsSortGetCallback(OAIHttpRequestWorker *worker);
    void usersIdListsListIdLikesGetCallback(OAIHttpRequestWorker *worker);
    void usersIdRatingsTypeRatingGetCallback(OAIHttpRequestWorker *worker);
    void usersIdRecommendationsTypeSortGetCallback(OAIHttpRequestWorker *worker);
    void usersIdWatchedTypeGetCallback(OAIHttpRequestWorker *worker);
    void usersIdWatchlistTypeSortGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void add_hidden_itemsSignal();
    void add_items_to_personal_listSignal();
    void approve_follow_requestSignal();
    void create_personal_listSignal();
    void delete_a_users_personal_listSignal();
    void deny_follow_requestSignal();
    void follow_this_userSignal();
    void get_a_users_personal_listsSignal();
    void get_all_lists_a_user_can_collaborate_onSignal();
    void get_commentsSignal();
    void get_follow_requestsSignal();
    void get_followersSignal();
    void get_followingSignal();
    void get_friendsSignal();
    void get_hidden_itemsSignal();
    void get_items_on_a_personal_listSignal();
    void get_likesSignal();
    void get_pending_following_requestsSignal();
    void get_personal_listSignal();
    void get_saved_filtersSignal();
    void get_statsSignal();
    void get_user_profileSignal();
    void get_watchingSignal();
    void like_a_listSignal();
    void remove_hidden_itemsSignal();
    void remove_items_from_personal_listSignal();
    void remove_like_on_a_listSignal();
    void reorder_a_users_listsSignal();
    void reorder_items_on_a_listSignal();
    void retrieve_settingsSignal();
    void unfollow_this_userSignal();
    void update_personal_listSignal();
    void usersIdCollectionTypeGetSignal();
    void usersIdHistoryTypeItemIdGetSignal();
    void usersIdListsListIdCommentsSortGetSignal();
    void usersIdListsListIdLikesGetSignal();
    void usersIdRatingsTypeRatingGetSignal();
    void usersIdRecommendationsTypeSortGetSignal();
    void usersIdWatchedTypeGetSignal();
    void usersIdWatchlistTypeSortGetSignal();


    void add_hidden_itemsSignalFull(OAIHttpRequestWorker *worker);
    void add_items_to_personal_listSignalFull(OAIHttpRequestWorker *worker);
    void approve_follow_requestSignalFull(OAIHttpRequestWorker *worker);
    void create_personal_listSignalFull(OAIHttpRequestWorker *worker);
    void delete_a_users_personal_listSignalFull(OAIHttpRequestWorker *worker);
    void deny_follow_requestSignalFull(OAIHttpRequestWorker *worker);
    void follow_this_userSignalFull(OAIHttpRequestWorker *worker);
    void get_a_users_personal_listsSignalFull(OAIHttpRequestWorker *worker);
    void get_all_lists_a_user_can_collaborate_onSignalFull(OAIHttpRequestWorker *worker);
    void get_commentsSignalFull(OAIHttpRequestWorker *worker);
    void get_follow_requestsSignalFull(OAIHttpRequestWorker *worker);
    void get_followersSignalFull(OAIHttpRequestWorker *worker);
    void get_followingSignalFull(OAIHttpRequestWorker *worker);
    void get_friendsSignalFull(OAIHttpRequestWorker *worker);
    void get_hidden_itemsSignalFull(OAIHttpRequestWorker *worker);
    void get_items_on_a_personal_listSignalFull(OAIHttpRequestWorker *worker);
    void get_likesSignalFull(OAIHttpRequestWorker *worker);
    void get_pending_following_requestsSignalFull(OAIHttpRequestWorker *worker);
    void get_personal_listSignalFull(OAIHttpRequestWorker *worker);
    void get_saved_filtersSignalFull(OAIHttpRequestWorker *worker);
    void get_statsSignalFull(OAIHttpRequestWorker *worker);
    void get_user_profileSignalFull(OAIHttpRequestWorker *worker);
    void get_watchingSignalFull(OAIHttpRequestWorker *worker);
    void like_a_listSignalFull(OAIHttpRequestWorker *worker);
    void remove_hidden_itemsSignalFull(OAIHttpRequestWorker *worker);
    void remove_items_from_personal_listSignalFull(OAIHttpRequestWorker *worker);
    void remove_like_on_a_listSignalFull(OAIHttpRequestWorker *worker);
    void reorder_a_users_listsSignalFull(OAIHttpRequestWorker *worker);
    void reorder_items_on_a_listSignalFull(OAIHttpRequestWorker *worker);
    void retrieve_settingsSignalFull(OAIHttpRequestWorker *worker);
    void unfollow_this_userSignalFull(OAIHttpRequestWorker *worker);
    void update_personal_listSignalFull(OAIHttpRequestWorker *worker);
    void usersIdCollectionTypeGetSignalFull(OAIHttpRequestWorker *worker);
    void usersIdHistoryTypeItemIdGetSignalFull(OAIHttpRequestWorker *worker);
    void usersIdListsListIdCommentsSortGetSignalFull(OAIHttpRequestWorker *worker);
    void usersIdListsListIdLikesGetSignalFull(OAIHttpRequestWorker *worker);
    void usersIdRatingsTypeRatingGetSignalFull(OAIHttpRequestWorker *worker);
    void usersIdRecommendationsTypeSortGetSignalFull(OAIHttpRequestWorker *worker);
    void usersIdWatchedTypeGetSignalFull(OAIHttpRequestWorker *worker);
    void usersIdWatchlistTypeSortGetSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use add_hidden_itemsSignalError() instead")
    void add_hidden_itemsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void add_hidden_itemsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use add_items_to_personal_listSignalError() instead")
    void add_items_to_personal_listSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void add_items_to_personal_listSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use approve_follow_requestSignalError() instead")
    void approve_follow_requestSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void approve_follow_requestSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use create_personal_listSignalError() instead")
    void create_personal_listSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void create_personal_listSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use delete_a_users_personal_listSignalError() instead")
    void delete_a_users_personal_listSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void delete_a_users_personal_listSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deny_follow_requestSignalError() instead")
    void deny_follow_requestSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deny_follow_requestSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use follow_this_userSignalError() instead")
    void follow_this_userSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void follow_this_userSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_a_users_personal_listsSignalError() instead")
    void get_a_users_personal_listsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_a_users_personal_listsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_all_lists_a_user_can_collaborate_onSignalError() instead")
    void get_all_lists_a_user_can_collaborate_onSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_all_lists_a_user_can_collaborate_onSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_commentsSignalError() instead")
    void get_commentsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_commentsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_follow_requestsSignalError() instead")
    void get_follow_requestsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_follow_requestsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_followersSignalError() instead")
    void get_followersSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_followersSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_followingSignalError() instead")
    void get_followingSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_followingSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_friendsSignalError() instead")
    void get_friendsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_friendsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_hidden_itemsSignalError() instead")
    void get_hidden_itemsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_hidden_itemsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_items_on_a_personal_listSignalError() instead")
    void get_items_on_a_personal_listSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_items_on_a_personal_listSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_likesSignalError() instead")
    void get_likesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_likesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_pending_following_requestsSignalError() instead")
    void get_pending_following_requestsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_pending_following_requestsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_personal_listSignalError() instead")
    void get_personal_listSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_personal_listSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_saved_filtersSignalError() instead")
    void get_saved_filtersSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_saved_filtersSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_statsSignalError() instead")
    void get_statsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_statsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_user_profileSignalError() instead")
    void get_user_profileSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_user_profileSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_watchingSignalError() instead")
    void get_watchingSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_watchingSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use like_a_listSignalError() instead")
    void like_a_listSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void like_a_listSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use remove_hidden_itemsSignalError() instead")
    void remove_hidden_itemsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void remove_hidden_itemsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use remove_items_from_personal_listSignalError() instead")
    void remove_items_from_personal_listSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void remove_items_from_personal_listSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use remove_like_on_a_listSignalError() instead")
    void remove_like_on_a_listSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void remove_like_on_a_listSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reorder_a_users_listsSignalError() instead")
    void reorder_a_users_listsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void reorder_a_users_listsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reorder_items_on_a_listSignalError() instead")
    void reorder_items_on_a_listSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void reorder_items_on_a_listSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use retrieve_settingsSignalError() instead")
    void retrieve_settingsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void retrieve_settingsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use unfollow_this_userSignalError() instead")
    void unfollow_this_userSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void unfollow_this_userSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use update_personal_listSignalError() instead")
    void update_personal_listSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void update_personal_listSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdCollectionTypeGetSignalError() instead")
    void usersIdCollectionTypeGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdCollectionTypeGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdHistoryTypeItemIdGetSignalError() instead")
    void usersIdHistoryTypeItemIdGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdHistoryTypeItemIdGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdListsListIdCommentsSortGetSignalError() instead")
    void usersIdListsListIdCommentsSortGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdListsListIdCommentsSortGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdListsListIdLikesGetSignalError() instead")
    void usersIdListsListIdLikesGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdListsListIdLikesGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdRatingsTypeRatingGetSignalError() instead")
    void usersIdRatingsTypeRatingGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdRatingsTypeRatingGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdRecommendationsTypeSortGetSignalError() instead")
    void usersIdRecommendationsTypeSortGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdRecommendationsTypeSortGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdWatchedTypeGetSignalError() instead")
    void usersIdWatchedTypeGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdWatchedTypeGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdWatchlistTypeSortGetSignalError() instead")
    void usersIdWatchlistTypeSortGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdWatchlistTypeSortGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use add_hidden_itemsSignalErrorFull() instead")
    void add_hidden_itemsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void add_hidden_itemsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use add_items_to_personal_listSignalErrorFull() instead")
    void add_items_to_personal_listSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void add_items_to_personal_listSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use approve_follow_requestSignalErrorFull() instead")
    void approve_follow_requestSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void approve_follow_requestSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use create_personal_listSignalErrorFull() instead")
    void create_personal_listSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void create_personal_listSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use delete_a_users_personal_listSignalErrorFull() instead")
    void delete_a_users_personal_listSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void delete_a_users_personal_listSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deny_follow_requestSignalErrorFull() instead")
    void deny_follow_requestSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deny_follow_requestSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use follow_this_userSignalErrorFull() instead")
    void follow_this_userSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void follow_this_userSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_a_users_personal_listsSignalErrorFull() instead")
    void get_a_users_personal_listsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_a_users_personal_listsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_all_lists_a_user_can_collaborate_onSignalErrorFull() instead")
    void get_all_lists_a_user_can_collaborate_onSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_all_lists_a_user_can_collaborate_onSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_commentsSignalErrorFull() instead")
    void get_commentsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_commentsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_follow_requestsSignalErrorFull() instead")
    void get_follow_requestsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_follow_requestsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_followersSignalErrorFull() instead")
    void get_followersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_followersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_followingSignalErrorFull() instead")
    void get_followingSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_followingSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_friendsSignalErrorFull() instead")
    void get_friendsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_friendsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_hidden_itemsSignalErrorFull() instead")
    void get_hidden_itemsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_hidden_itemsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_items_on_a_personal_listSignalErrorFull() instead")
    void get_items_on_a_personal_listSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_items_on_a_personal_listSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_likesSignalErrorFull() instead")
    void get_likesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_likesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_pending_following_requestsSignalErrorFull() instead")
    void get_pending_following_requestsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_pending_following_requestsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_personal_listSignalErrorFull() instead")
    void get_personal_listSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_personal_listSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_saved_filtersSignalErrorFull() instead")
    void get_saved_filtersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_saved_filtersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_statsSignalErrorFull() instead")
    void get_statsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_statsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_user_profileSignalErrorFull() instead")
    void get_user_profileSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_user_profileSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_watchingSignalErrorFull() instead")
    void get_watchingSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_watchingSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use like_a_listSignalErrorFull() instead")
    void like_a_listSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void like_a_listSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use remove_hidden_itemsSignalErrorFull() instead")
    void remove_hidden_itemsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void remove_hidden_itemsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use remove_items_from_personal_listSignalErrorFull() instead")
    void remove_items_from_personal_listSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void remove_items_from_personal_listSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use remove_like_on_a_listSignalErrorFull() instead")
    void remove_like_on_a_listSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void remove_like_on_a_listSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reorder_a_users_listsSignalErrorFull() instead")
    void reorder_a_users_listsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reorder_a_users_listsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reorder_items_on_a_listSignalErrorFull() instead")
    void reorder_items_on_a_listSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reorder_items_on_a_listSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use retrieve_settingsSignalErrorFull() instead")
    void retrieve_settingsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void retrieve_settingsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use unfollow_this_userSignalErrorFull() instead")
    void unfollow_this_userSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void unfollow_this_userSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use update_personal_listSignalErrorFull() instead")
    void update_personal_listSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void update_personal_listSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdCollectionTypeGetSignalErrorFull() instead")
    void usersIdCollectionTypeGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdCollectionTypeGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdHistoryTypeItemIdGetSignalErrorFull() instead")
    void usersIdHistoryTypeItemIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdHistoryTypeItemIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdListsListIdCommentsSortGetSignalErrorFull() instead")
    void usersIdListsListIdCommentsSortGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdListsListIdCommentsSortGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdListsListIdLikesGetSignalErrorFull() instead")
    void usersIdListsListIdLikesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdListsListIdLikesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdRatingsTypeRatingGetSignalErrorFull() instead")
    void usersIdRatingsTypeRatingGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdRatingsTypeRatingGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdRecommendationsTypeSortGetSignalErrorFull() instead")
    void usersIdRecommendationsTypeSortGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdRecommendationsTypeSortGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdWatchedTypeGetSignalErrorFull() instead")
    void usersIdWatchedTypeGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdWatchedTypeGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usersIdWatchlistTypeSortGetSignalErrorFull() instead")
    void usersIdWatchlistTypeSortGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usersIdWatchlistTypeSortGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
