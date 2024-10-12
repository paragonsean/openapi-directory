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

#include "OAIMoviesApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIMoviesApi::OAIMoviesApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIMoviesApi::~OAIMoviesApi() {
}

void OAIMoviesApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.trakt.tv"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("get_a_movie", defaultConf);
    _serverIndices.insert("get_a_movie", 0);
    _serverConfigs.insert("get_all_movie_aliases", defaultConf);
    _serverIndices.insert("get_all_movie_aliases", 0);
    _serverConfigs.insert("get_all_movie_comments", defaultConf);
    _serverIndices.insert("get_all_movie_comments", 0);
    _serverConfigs.insert("get_all_movie_releases", defaultConf);
    _serverIndices.insert("get_all_movie_releases", 0);
    _serverConfigs.insert("get_all_movie_translations", defaultConf);
    _serverIndices.insert("get_all_movie_translations", 0);
    _serverConfigs.insert("get_all_people_for_a_movie", defaultConf);
    _serverIndices.insert("get_all_people_for_a_movie", 0);
    _serverConfigs.insert("get_lists_containing_this_movie", defaultConf);
    _serverIndices.insert("get_lists_containing_this_movie", 0);
    _serverConfigs.insert("get_movie_ratings", defaultConf);
    _serverIndices.insert("get_movie_ratings", 0);
    _serverConfigs.insert("get_movie_stats", defaultConf);
    _serverIndices.insert("get_movie_stats", 0);
    _serverConfigs.insert("get_movie_studios", defaultConf);
    _serverIndices.insert("get_movie_studios", 0);
    _serverConfigs.insert("get_popular_movies", defaultConf);
    _serverIndices.insert("get_popular_movies", 0);
    _serverConfigs.insert("get_recently_updated_movie_Trakt_IDs", defaultConf);
    _serverIndices.insert("get_recently_updated_movie_Trakt_IDs", 0);
    _serverConfigs.insert("get_recently_updated_movies", defaultConf);
    _serverIndices.insert("get_recently_updated_movies", 0);
    _serverConfigs.insert("get_related_movies", defaultConf);
    _serverIndices.insert("get_related_movies", 0);
    _serverConfigs.insert("get_the_most_Collected_movies", defaultConf);
    _serverIndices.insert("get_the_most_Collected_movies", 0);
    _serverConfigs.insert("get_the_most_anticipated_movies", defaultConf);
    _serverIndices.insert("get_the_most_anticipated_movies", 0);
    _serverConfigs.insert("get_the_most_played_movies", defaultConf);
    _serverIndices.insert("get_the_most_played_movies", 0);
    _serverConfigs.insert("get_the_most_recommended_movies", defaultConf);
    _serverIndices.insert("get_the_most_recommended_movies", 0);
    _serverConfigs.insert("get_the_most_watched_movies", defaultConf);
    _serverIndices.insert("get_the_most_watched_movies", 0);
    _serverConfigs.insert("get_the_weekend_box_office", defaultConf);
    _serverIndices.insert("get_the_weekend_box_office", 0);
    _serverConfigs.insert("get_trending_movies", defaultConf);
    _serverIndices.insert("get_trending_movies", 0);
    _serverConfigs.insert("get_users_watching_right_now", defaultConf);
    _serverIndices.insert("get_users_watching_right_now", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIMoviesApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIMoviesApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIMoviesApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIMoviesApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIMoviesApi::setUsername(const QString &username) {
    _username = username;
}

void OAIMoviesApi::setPassword(const QString &password) {
    _password = password;
}


void OAIMoviesApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIMoviesApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIMoviesApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
    _manager = manager;
}

/**
    * Appends a new ServerConfiguration to the config map for a specific operation.
    * @param operation The id to the target operation.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    * returns the index of the new server config on success and -1 if the operation is not found
    */
int OAIMoviesApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    if (_serverConfigs.contains(operation)) {
        _serverConfigs[operation].append(OAIServerConfiguration(
                    url,
                    description,
                    variables));
        return _serverConfigs[operation].size()-1;
    } else {
        return -1;
    }
}

/**
    * Appends a new ServerConfiguration to the config map for a all operations and sets the index to that server.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAIMoviesApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    for (auto keyIt = _serverIndices.keyBegin(); keyIt != _serverIndices.keyEnd(); keyIt++) {
        setServerIndex(*keyIt, addServerConfiguration(*keyIt, url, description, variables));
    }
}

/**
    * Appends a new ServerConfiguration to the config map for an operations and sets the index to that server.
    * @param URL A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAIMoviesApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIMoviesApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIMoviesApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIMoviesApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIMoviesApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIMoviesApi::getParamStylePrefix(const QString &style) {
    if (style == "matrix") {
        return ";";
    } else if (style == "label") {
        return ".";
    } else if (style == "form") {
        return "&";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "&";
    } else if (style == "pipeDelimited") {
        return "&";
    } else {
        return "none";
    }
}

QString OAIMoviesApi::getParamStyleSuffix(const QString &style) {
    if (style == "matrix") {
        return "=";
    } else if (style == "label") {
        return "";
    } else if (style == "form") {
        return "=";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "=";
    } else if (style == "pipeDelimited") {
        return "=";
    } else {
        return "none";
    }
}

QString OAIMoviesApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

    if (style == "matrix") {
        return (isExplode) ? ";" + name + "=" : ",";

    } else if (style == "label") {
        return (isExplode) ? "." : ",";

    } else if (style == "form") {
        return (isExplode) ? "&" + name + "=" : ",";

    } else if (style == "simple") {
        return ",";
    } else if (style == "spaceDelimited") {
        return (isExplode) ? "&" + name + "=" : " ";

    } else if (style == "pipeDelimited") {
        return (isExplode) ? "&" + name + "=" : "|";

    } else if (style == "deepObject") {
        return (isExplode) ? "&" : "none";

    } else {
        return "none";
    }
}

void OAIMoviesApi::get_a_movie(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_a_movie"][_serverIndices.value("get_a_movie")].URL()+"/movies/{id}");
    
    
    {
        QString idPathParam("{");
        idPathParam.append("id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_a_movieCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_a_movieCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_a_movieSignal();
        Q_EMIT get_a_movieSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_a_movieSignalE(error_type, error_str);
        Q_EMIT get_a_movieSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_a_movieSignalError(error_type, error_str);
        Q_EMIT get_a_movieSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_all_movie_aliases(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_all_movie_aliases"][_serverIndices.value("get_all_movie_aliases")].URL()+"/movies/{id}/aliases");
    
    
    {
        QString idPathParam("{");
        idPathParam.append("id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_all_movie_aliasesCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_all_movie_aliasesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_all_movie_aliasesSignal();
        Q_EMIT get_all_movie_aliasesSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_all_movie_aliasesSignalE(error_type, error_str);
        Q_EMIT get_all_movie_aliasesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_all_movie_aliasesSignalError(error_type, error_str);
        Q_EMIT get_all_movie_aliasesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_all_movie_comments(const QString &id, const QString &sort, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_all_movie_comments"][_serverIndices.value("get_all_movie_comments")].URL()+"/movies/{id}/comments/{sort}");
    
    
    {
        QString idPathParam("{");
        idPathParam.append("id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    
    {
        QString sortPathParam("{");
        sortPathParam.append("sort").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "sort", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"sort"+pathSuffix : pathPrefix;
        fullPath.replace(sortPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sort)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_all_movie_commentsCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_all_movie_commentsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_all_movie_commentsSignal();
        Q_EMIT get_all_movie_commentsSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_all_movie_commentsSignalE(error_type, error_str);
        Q_EMIT get_all_movie_commentsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_all_movie_commentsSignalError(error_type, error_str);
        Q_EMIT get_all_movie_commentsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_all_movie_releases(const QString &id, const QString &country, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_all_movie_releases"][_serverIndices.value("get_all_movie_releases")].URL()+"/movies/{id}/releases/{country}");
    
    
    {
        QString idPathParam("{");
        idPathParam.append("id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    
    {
        QString countryPathParam("{");
        countryPathParam.append("country").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "country", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"country"+pathSuffix : pathPrefix;
        fullPath.replace(countryPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(country)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_all_movie_releasesCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_all_movie_releasesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_all_movie_releasesSignal();
        Q_EMIT get_all_movie_releasesSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_all_movie_releasesSignalE(error_type, error_str);
        Q_EMIT get_all_movie_releasesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_all_movie_releasesSignalError(error_type, error_str);
        Q_EMIT get_all_movie_releasesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_all_movie_translations(const QString &id, const QString &language, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_all_movie_translations"][_serverIndices.value("get_all_movie_translations")].URL()+"/movies/{id}/translations/{language}");
    
    
    {
        QString idPathParam("{");
        idPathParam.append("id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    
    {
        QString languagePathParam("{");
        languagePathParam.append("language").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "language", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"language"+pathSuffix : pathPrefix;
        fullPath.replace(languagePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(language)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_all_movie_translationsCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_all_movie_translationsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_all_movie_translationsSignal();
        Q_EMIT get_all_movie_translationsSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_all_movie_translationsSignalE(error_type, error_str);
        Q_EMIT get_all_movie_translationsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_all_movie_translationsSignalError(error_type, error_str);
        Q_EMIT get_all_movie_translationsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_all_people_for_a_movie(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_all_people_for_a_movie"][_serverIndices.value("get_all_people_for_a_movie")].URL()+"/movies/{id}/people");
    
    
    {
        QString idPathParam("{");
        idPathParam.append("id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_all_people_for_a_movieCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_all_people_for_a_movieCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_all_people_for_a_movieSignal();
        Q_EMIT get_all_people_for_a_movieSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_all_people_for_a_movieSignalE(error_type, error_str);
        Q_EMIT get_all_people_for_a_movieSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_all_people_for_a_movieSignalError(error_type, error_str);
        Q_EMIT get_all_people_for_a_movieSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_lists_containing_this_movie(const QString &id, const QString &type, const QString &sort, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_lists_containing_this_movie"][_serverIndices.value("get_lists_containing_this_movie")].URL()+"/movies/{id}/lists/{type}/{sort}");
    
    
    {
        QString idPathParam("{");
        idPathParam.append("id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    
    {
        QString typePathParam("{");
        typePathParam.append("type").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "type", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"type"+pathSuffix : pathPrefix;
        fullPath.replace(typePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(type)));
    }
    
    {
        QString sortPathParam("{");
        sortPathParam.append("sort").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "sort", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"sort"+pathSuffix : pathPrefix;
        fullPath.replace(sortPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sort)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_lists_containing_this_movieCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_lists_containing_this_movieCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_lists_containing_this_movieSignal();
        Q_EMIT get_lists_containing_this_movieSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_lists_containing_this_movieSignalE(error_type, error_str);
        Q_EMIT get_lists_containing_this_movieSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_lists_containing_this_movieSignalError(error_type, error_str);
        Q_EMIT get_lists_containing_this_movieSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_movie_ratings(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_movie_ratings"][_serverIndices.value("get_movie_ratings")].URL()+"/movies/{id}/ratings");
    
    
    {
        QString idPathParam("{");
        idPathParam.append("id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_movie_ratingsCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_movie_ratingsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_movie_ratingsSignal();
        Q_EMIT get_movie_ratingsSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_movie_ratingsSignalE(error_type, error_str);
        Q_EMIT get_movie_ratingsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_movie_ratingsSignalError(error_type, error_str);
        Q_EMIT get_movie_ratingsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_movie_stats(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_movie_stats"][_serverIndices.value("get_movie_stats")].URL()+"/movies/{id}/stats");
    
    
    {
        QString idPathParam("{");
        idPathParam.append("id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_movie_statsCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_movie_statsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_movie_statsSignal();
        Q_EMIT get_movie_statsSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_movie_statsSignalE(error_type, error_str);
        Q_EMIT get_movie_statsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_movie_statsSignalError(error_type, error_str);
        Q_EMIT get_movie_statsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_movie_studios(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_movie_studios"][_serverIndices.value("get_movie_studios")].URL()+"/movies/{id}/studios");
    
    
    {
        QString idPathParam("{");
        idPathParam.append("id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_movie_studiosCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_movie_studiosCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_movie_studiosSignal();
        Q_EMIT get_movie_studiosSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_movie_studiosSignalE(error_type, error_str);
        Q_EMIT get_movie_studiosSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_movie_studiosSignalError(error_type, error_str);
        Q_EMIT get_movie_studiosSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_popular_movies(const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_popular_movies"][_serverIndices.value("get_popular_movies")].URL()+"/movies/popular");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_popular_moviesCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_popular_moviesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_popular_moviesSignal();
        Q_EMIT get_popular_moviesSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_popular_moviesSignalE(error_type, error_str);
        Q_EMIT get_popular_moviesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_popular_moviesSignalError(error_type, error_str);
        Q_EMIT get_popular_moviesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_recently_updated_movie_Trakt_IDs(const QString &start_date, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_recently_updated_movie_Trakt_IDs"][_serverIndices.value("get_recently_updated_movie_Trakt_IDs")].URL()+"/movies/updates/id/{start_date}");
    
    
    {
        QString start_datePathParam("{");
        start_datePathParam.append("start_date").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "start_date", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"start_date"+pathSuffix : pathPrefix;
        fullPath.replace(start_datePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(start_date)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_recently_updated_movie_Trakt_IDsCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_recently_updated_movie_Trakt_IDsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_recently_updated_movie_Trakt_IDsSignal();
        Q_EMIT get_recently_updated_movie_Trakt_IDsSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_recently_updated_movie_Trakt_IDsSignalE(error_type, error_str);
        Q_EMIT get_recently_updated_movie_Trakt_IDsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_recently_updated_movie_Trakt_IDsSignalError(error_type, error_str);
        Q_EMIT get_recently_updated_movie_Trakt_IDsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_recently_updated_movies(const QString &start_date, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_recently_updated_movies"][_serverIndices.value("get_recently_updated_movies")].URL()+"/movies/updates/{start_date}");
    
    
    {
        QString start_datePathParam("{");
        start_datePathParam.append("start_date").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "start_date", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"start_date"+pathSuffix : pathPrefix;
        fullPath.replace(start_datePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(start_date)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_recently_updated_moviesCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_recently_updated_moviesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_recently_updated_moviesSignal();
        Q_EMIT get_recently_updated_moviesSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_recently_updated_moviesSignalE(error_type, error_str);
        Q_EMIT get_recently_updated_moviesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_recently_updated_moviesSignalError(error_type, error_str);
        Q_EMIT get_recently_updated_moviesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_related_movies(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_related_movies"][_serverIndices.value("get_related_movies")].URL()+"/movies/{id}/related");
    
    
    {
        QString idPathParam("{");
        idPathParam.append("id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_related_moviesCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_related_moviesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_related_moviesSignal();
        Q_EMIT get_related_moviesSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_related_moviesSignalE(error_type, error_str);
        Q_EMIT get_related_moviesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_related_moviesSignalError(error_type, error_str);
        Q_EMIT get_related_moviesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_the_most_Collected_movies(const QString &period, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_the_most_Collected_movies"][_serverIndices.value("get_the_most_Collected_movies")].URL()+"/movies/collected/{period}");
    
    
    {
        QString periodPathParam("{");
        periodPathParam.append("period").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "period", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"period"+pathSuffix : pathPrefix;
        fullPath.replace(periodPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(period)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_the_most_Collected_moviesCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_the_most_Collected_moviesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_the_most_Collected_moviesSignal();
        Q_EMIT get_the_most_Collected_moviesSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_the_most_Collected_moviesSignalE(error_type, error_str);
        Q_EMIT get_the_most_Collected_moviesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_the_most_Collected_moviesSignalError(error_type, error_str);
        Q_EMIT get_the_most_Collected_moviesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_the_most_anticipated_movies(const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_the_most_anticipated_movies"][_serverIndices.value("get_the_most_anticipated_movies")].URL()+"/movies/anticipated");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_the_most_anticipated_moviesCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_the_most_anticipated_moviesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_the_most_anticipated_moviesSignal();
        Q_EMIT get_the_most_anticipated_moviesSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_the_most_anticipated_moviesSignalE(error_type, error_str);
        Q_EMIT get_the_most_anticipated_moviesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_the_most_anticipated_moviesSignalError(error_type, error_str);
        Q_EMIT get_the_most_anticipated_moviesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_the_most_played_movies(const QString &period, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_the_most_played_movies"][_serverIndices.value("get_the_most_played_movies")].URL()+"/movies/played/{period}");
    
    
    {
        QString periodPathParam("{");
        periodPathParam.append("period").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "period", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"period"+pathSuffix : pathPrefix;
        fullPath.replace(periodPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(period)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_the_most_played_moviesCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_the_most_played_moviesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_the_most_played_moviesSignal();
        Q_EMIT get_the_most_played_moviesSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_the_most_played_moviesSignalE(error_type, error_str);
        Q_EMIT get_the_most_played_moviesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_the_most_played_moviesSignalError(error_type, error_str);
        Q_EMIT get_the_most_played_moviesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_the_most_recommended_movies(const QString &period, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_the_most_recommended_movies"][_serverIndices.value("get_the_most_recommended_movies")].URL()+"/movies/recommended/{period}");
    
    
    {
        QString periodPathParam("{");
        periodPathParam.append("period").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "period", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"period"+pathSuffix : pathPrefix;
        fullPath.replace(periodPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(period)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_the_most_recommended_moviesCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_the_most_recommended_moviesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_the_most_recommended_moviesSignal();
        Q_EMIT get_the_most_recommended_moviesSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_the_most_recommended_moviesSignalE(error_type, error_str);
        Q_EMIT get_the_most_recommended_moviesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_the_most_recommended_moviesSignalError(error_type, error_str);
        Q_EMIT get_the_most_recommended_moviesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_the_most_watched_movies(const QString &period, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_the_most_watched_movies"][_serverIndices.value("get_the_most_watched_movies")].URL()+"/movies/watched/{period}");
    
    
    {
        QString periodPathParam("{");
        periodPathParam.append("period").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "period", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"period"+pathSuffix : pathPrefix;
        fullPath.replace(periodPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(period)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_the_most_watched_moviesCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_the_most_watched_moviesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_the_most_watched_moviesSignal();
        Q_EMIT get_the_most_watched_moviesSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_the_most_watched_moviesSignalE(error_type, error_str);
        Q_EMIT get_the_most_watched_moviesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_the_most_watched_moviesSignalError(error_type, error_str);
        Q_EMIT get_the_most_watched_moviesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_the_weekend_box_office(const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_the_weekend_box_office"][_serverIndices.value("get_the_weekend_box_office")].URL()+"/movies/boxoffice");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_the_weekend_box_officeCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_the_weekend_box_officeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_the_weekend_box_officeSignal();
        Q_EMIT get_the_weekend_box_officeSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_the_weekend_box_officeSignalE(error_type, error_str);
        Q_EMIT get_the_weekend_box_officeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_the_weekend_box_officeSignalError(error_type, error_str);
        Q_EMIT get_the_weekend_box_officeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_trending_movies(const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_trending_movies"][_serverIndices.value("get_trending_movies")].URL()+"/movies/trending");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_trending_moviesCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_trending_moviesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_trending_moviesSignal();
        Q_EMIT get_trending_moviesSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_trending_moviesSignalE(error_type, error_str);
        Q_EMIT get_trending_moviesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_trending_moviesSignalError(error_type, error_str);
        Q_EMIT get_trending_moviesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::get_users_watching_right_now(const QString &id, const ::OpenAPI::OptionalParam<QString> &trakt_api_version, const ::OpenAPI::OptionalParam<QString> &trakt_api_key) {
    QString fullPath = QString(_serverConfigs["get_users_watching_right_now"][_serverIndices.value("get_users_watching_right_now")].URL()+"/movies/{id}/watching");
    
    
    {
        QString idPathParam("{");
        idPathParam.append("id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (trakt_api_version.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_version.value()).isEmpty()) {
            input.headers.insert("trakt-api-version", ::OpenAPI::toStringValue(trakt_api_version.value()));
        }
        }
    if (trakt_api_key.hasValue())
    {
        if (!::OpenAPI::toStringValue(trakt_api_key.value()).isEmpty()) {
            input.headers.insert("trakt-api-key", ::OpenAPI::toStringValue(trakt_api_key.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMoviesApi::get_users_watching_right_nowCallback);
    connect(this, &OAIMoviesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMoviesApi::get_users_watching_right_nowCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_users_watching_right_nowSignal();
        Q_EMIT get_users_watching_right_nowSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_users_watching_right_nowSignalE(error_type, error_str);
        Q_EMIT get_users_watching_right_nowSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_users_watching_right_nowSignalError(error_type, error_str);
        Q_EMIT get_users_watching_right_nowSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMoviesApi::tokenAvailable(){

    oauthToken token;
    switch (_OauthMethod) {
    case 1: //implicit flow
        token = _implicitFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _implicitFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 2: //authorization flow
        token = _authFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _authFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 3: //client credentials flow
        token = _credentialFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 4: //resource owner password flow
        token = _passwordFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    default:
        qDebug() << "No Oauth method set!";
        break;
    }
}
} // namespace OpenAPI
