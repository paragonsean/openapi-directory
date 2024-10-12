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

#ifndef OAI_OAIMoviesApi_H
#define OAI_OAIMoviesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIMoviesApi : public QObject {
    Q_OBJECT

public:
    OAIMoviesApi(const int timeOut = 0);
    ~OAIMoviesApi();

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
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_a_movie(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_all_movie_aliases(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  sort QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_all_movie_comments(const QString &id, const QString &sort, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  country QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_all_movie_releases(const QString &id, const QString &country, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  language QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_all_movie_translations(const QString &id, const QString &language, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_all_people_for_a_movie(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  type QString [required]
    * @param[in]  sort QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_lists_containing_this_movie(const QString &id, const QString &type, const QString &sort, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_movie_ratings(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_movie_stats(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_movie_studios(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_popular_movies(const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  start_date QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_recently_updated_movie_Trakt_IDs(const QString &start_date, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  start_date QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_recently_updated_movies(const QString &start_date, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_related_movies(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  period QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_the_most_Collected_movies(const QString &period, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_the_most_anticipated_movies(const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  period QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_the_most_played_movies(const QString &period, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  period QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_the_most_recommended_movies(const QString &period, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  period QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_the_most_watched_movies(const QString &period, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_the_weekend_box_office(const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_trending_movies(const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  trakt_api_version QString [optional]
    * @param[in]  trakt_api_key QString [optional]
    */
    virtual void get_users_watching_right_now(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trakt_api_key = ::OpenAPI::OptionalParam<QString>());


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

    void get_a_movieCallback(OAIHttpRequestWorker *worker);
    void get_all_movie_aliasesCallback(OAIHttpRequestWorker *worker);
    void get_all_movie_commentsCallback(OAIHttpRequestWorker *worker);
    void get_all_movie_releasesCallback(OAIHttpRequestWorker *worker);
    void get_all_movie_translationsCallback(OAIHttpRequestWorker *worker);
    void get_all_people_for_a_movieCallback(OAIHttpRequestWorker *worker);
    void get_lists_containing_this_movieCallback(OAIHttpRequestWorker *worker);
    void get_movie_ratingsCallback(OAIHttpRequestWorker *worker);
    void get_movie_statsCallback(OAIHttpRequestWorker *worker);
    void get_movie_studiosCallback(OAIHttpRequestWorker *worker);
    void get_popular_moviesCallback(OAIHttpRequestWorker *worker);
    void get_recently_updated_movie_Trakt_IDsCallback(OAIHttpRequestWorker *worker);
    void get_recently_updated_moviesCallback(OAIHttpRequestWorker *worker);
    void get_related_moviesCallback(OAIHttpRequestWorker *worker);
    void get_the_most_Collected_moviesCallback(OAIHttpRequestWorker *worker);
    void get_the_most_anticipated_moviesCallback(OAIHttpRequestWorker *worker);
    void get_the_most_played_moviesCallback(OAIHttpRequestWorker *worker);
    void get_the_most_recommended_moviesCallback(OAIHttpRequestWorker *worker);
    void get_the_most_watched_moviesCallback(OAIHttpRequestWorker *worker);
    void get_the_weekend_box_officeCallback(OAIHttpRequestWorker *worker);
    void get_trending_moviesCallback(OAIHttpRequestWorker *worker);
    void get_users_watching_right_nowCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void get_a_movieSignal();
    void get_all_movie_aliasesSignal();
    void get_all_movie_commentsSignal();
    void get_all_movie_releasesSignal();
    void get_all_movie_translationsSignal();
    void get_all_people_for_a_movieSignal();
    void get_lists_containing_this_movieSignal();
    void get_movie_ratingsSignal();
    void get_movie_statsSignal();
    void get_movie_studiosSignal();
    void get_popular_moviesSignal();
    void get_recently_updated_movie_Trakt_IDsSignal();
    void get_recently_updated_moviesSignal();
    void get_related_moviesSignal();
    void get_the_most_Collected_moviesSignal();
    void get_the_most_anticipated_moviesSignal();
    void get_the_most_played_moviesSignal();
    void get_the_most_recommended_moviesSignal();
    void get_the_most_watched_moviesSignal();
    void get_the_weekend_box_officeSignal();
    void get_trending_moviesSignal();
    void get_users_watching_right_nowSignal();


    void get_a_movieSignalFull(OAIHttpRequestWorker *worker);
    void get_all_movie_aliasesSignalFull(OAIHttpRequestWorker *worker);
    void get_all_movie_commentsSignalFull(OAIHttpRequestWorker *worker);
    void get_all_movie_releasesSignalFull(OAIHttpRequestWorker *worker);
    void get_all_movie_translationsSignalFull(OAIHttpRequestWorker *worker);
    void get_all_people_for_a_movieSignalFull(OAIHttpRequestWorker *worker);
    void get_lists_containing_this_movieSignalFull(OAIHttpRequestWorker *worker);
    void get_movie_ratingsSignalFull(OAIHttpRequestWorker *worker);
    void get_movie_statsSignalFull(OAIHttpRequestWorker *worker);
    void get_movie_studiosSignalFull(OAIHttpRequestWorker *worker);
    void get_popular_moviesSignalFull(OAIHttpRequestWorker *worker);
    void get_recently_updated_movie_Trakt_IDsSignalFull(OAIHttpRequestWorker *worker);
    void get_recently_updated_moviesSignalFull(OAIHttpRequestWorker *worker);
    void get_related_moviesSignalFull(OAIHttpRequestWorker *worker);
    void get_the_most_Collected_moviesSignalFull(OAIHttpRequestWorker *worker);
    void get_the_most_anticipated_moviesSignalFull(OAIHttpRequestWorker *worker);
    void get_the_most_played_moviesSignalFull(OAIHttpRequestWorker *worker);
    void get_the_most_recommended_moviesSignalFull(OAIHttpRequestWorker *worker);
    void get_the_most_watched_moviesSignalFull(OAIHttpRequestWorker *worker);
    void get_the_weekend_box_officeSignalFull(OAIHttpRequestWorker *worker);
    void get_trending_moviesSignalFull(OAIHttpRequestWorker *worker);
    void get_users_watching_right_nowSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use get_a_movieSignalError() instead")
    void get_a_movieSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_a_movieSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_all_movie_aliasesSignalError() instead")
    void get_all_movie_aliasesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_all_movie_aliasesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_all_movie_commentsSignalError() instead")
    void get_all_movie_commentsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_all_movie_commentsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_all_movie_releasesSignalError() instead")
    void get_all_movie_releasesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_all_movie_releasesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_all_movie_translationsSignalError() instead")
    void get_all_movie_translationsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_all_movie_translationsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_all_people_for_a_movieSignalError() instead")
    void get_all_people_for_a_movieSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_all_people_for_a_movieSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_lists_containing_this_movieSignalError() instead")
    void get_lists_containing_this_movieSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_lists_containing_this_movieSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_movie_ratingsSignalError() instead")
    void get_movie_ratingsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_movie_ratingsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_movie_statsSignalError() instead")
    void get_movie_statsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_movie_statsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_movie_studiosSignalError() instead")
    void get_movie_studiosSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_movie_studiosSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_popular_moviesSignalError() instead")
    void get_popular_moviesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_popular_moviesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_recently_updated_movie_Trakt_IDsSignalError() instead")
    void get_recently_updated_movie_Trakt_IDsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_recently_updated_movie_Trakt_IDsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_recently_updated_moviesSignalError() instead")
    void get_recently_updated_moviesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_recently_updated_moviesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_related_moviesSignalError() instead")
    void get_related_moviesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_related_moviesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_the_most_Collected_moviesSignalError() instead")
    void get_the_most_Collected_moviesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_the_most_Collected_moviesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_the_most_anticipated_moviesSignalError() instead")
    void get_the_most_anticipated_moviesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_the_most_anticipated_moviesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_the_most_played_moviesSignalError() instead")
    void get_the_most_played_moviesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_the_most_played_moviesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_the_most_recommended_moviesSignalError() instead")
    void get_the_most_recommended_moviesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_the_most_recommended_moviesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_the_most_watched_moviesSignalError() instead")
    void get_the_most_watched_moviesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_the_most_watched_moviesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_the_weekend_box_officeSignalError() instead")
    void get_the_weekend_box_officeSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_the_weekend_box_officeSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_trending_moviesSignalError() instead")
    void get_trending_moviesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_trending_moviesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_users_watching_right_nowSignalError() instead")
    void get_users_watching_right_nowSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void get_users_watching_right_nowSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use get_a_movieSignalErrorFull() instead")
    void get_a_movieSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_a_movieSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_all_movie_aliasesSignalErrorFull() instead")
    void get_all_movie_aliasesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_all_movie_aliasesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_all_movie_commentsSignalErrorFull() instead")
    void get_all_movie_commentsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_all_movie_commentsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_all_movie_releasesSignalErrorFull() instead")
    void get_all_movie_releasesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_all_movie_releasesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_all_movie_translationsSignalErrorFull() instead")
    void get_all_movie_translationsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_all_movie_translationsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_all_people_for_a_movieSignalErrorFull() instead")
    void get_all_people_for_a_movieSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_all_people_for_a_movieSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_lists_containing_this_movieSignalErrorFull() instead")
    void get_lists_containing_this_movieSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_lists_containing_this_movieSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_movie_ratingsSignalErrorFull() instead")
    void get_movie_ratingsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_movie_ratingsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_movie_statsSignalErrorFull() instead")
    void get_movie_statsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_movie_statsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_movie_studiosSignalErrorFull() instead")
    void get_movie_studiosSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_movie_studiosSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_popular_moviesSignalErrorFull() instead")
    void get_popular_moviesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_popular_moviesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_recently_updated_movie_Trakt_IDsSignalErrorFull() instead")
    void get_recently_updated_movie_Trakt_IDsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_recently_updated_movie_Trakt_IDsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_recently_updated_moviesSignalErrorFull() instead")
    void get_recently_updated_moviesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_recently_updated_moviesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_related_moviesSignalErrorFull() instead")
    void get_related_moviesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_related_moviesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_the_most_Collected_moviesSignalErrorFull() instead")
    void get_the_most_Collected_moviesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_the_most_Collected_moviesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_the_most_anticipated_moviesSignalErrorFull() instead")
    void get_the_most_anticipated_moviesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_the_most_anticipated_moviesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_the_most_played_moviesSignalErrorFull() instead")
    void get_the_most_played_moviesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_the_most_played_moviesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_the_most_recommended_moviesSignalErrorFull() instead")
    void get_the_most_recommended_moviesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_the_most_recommended_moviesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_the_most_watched_moviesSignalErrorFull() instead")
    void get_the_most_watched_moviesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_the_most_watched_moviesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_the_weekend_box_officeSignalErrorFull() instead")
    void get_the_weekend_box_officeSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_the_weekend_box_officeSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_trending_moviesSignalErrorFull() instead")
    void get_trending_moviesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_trending_moviesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use get_users_watching_right_nowSignalErrorFull() instead")
    void get_users_watching_right_nowSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void get_users_watching_right_nowSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
