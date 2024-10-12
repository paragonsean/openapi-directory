/**
 * Trakt API
 * At Trakt, we collect lots of interesting information about what tv shows and movies everyone is watching. Part of the fun with such data is making it available for anyone to mash up and use on their own site or app. The Trakt API was made just for this purpose. It is very easy to use, you basically call a URL and get some JSON back.  More complex API calls (such as adding a movie or show to your collection) involve sending us data. These are still easy to use, you simply POST some JSON data to a specific URL.  Make sure to check out the [**Required Headers**](#introduction/required-headers) and [**Authentication**](#reference/authentication-oauth) sections for more info on what needs to be sent with each API call. Also check out the [**Terminology**](#introduction/terminology) section insight into the features Trakt supports.  # Create an App  To use the Trakt API, you'll need to [**create a new API app**](https://trakt.tv/oauth/applications/new).  # Stay Connected  API discussion and bugs should be posted in the [**GitHub Developer Forum**](https://github.com/trakt/api-help/issues) and *watch* the repository if you'd like to get notifications. Make sure to follow our [**API Blog**](https://apiblog.trakt.tv) and [**@traktapi on Twitter**](https://twitter.com/traktapi) too.  # API URL  The API should always be accessed over SSL.  ``` https://api.trakt.tv ```  If you would like to use our sandbox environment to not fill production with test data, use this URL over SSL. **Note:** Staging is a completely separate environment, so you'll need to [**create a new API app on staging**](https://staging.trakt.tv/oauth/applications/new).  ``` https://api-staging.trakt.tv ```  # Verbs  The API uses restful verbs.  | Verb | Description | |---|---| | `GET` | Select one or more items. Success returns `200` status code. | | `POST` | Create a new item. Success returns `201` status code. | | `PUT` | Update an item. Success returns `200` status code. | | `DELETE` | Delete an item. Success returns `200` or `204` status code. |  # Status Codes  The API will respond with one of the following HTTP status codes.  | Code | Description | |---|---| | `200` | Success | `201` | Success - *new resource created (POST)* | `204` | Success - *no content to return (DELETE)* | `400` | Bad Request - *request couldn't be parsed* | `401` | Unauthorized - *OAuth must be provided* | `403` | Forbidden - *invalid API key or unapproved app* | `404` | Not Found - *method exists, but no record found* | `405` | Method Not Found - *method doesn't exist* | `409` | Conflict - *resource already created* | `412` | Precondition Failed - *use application/json content type* | `420` | Account Limit Exceeded - *list count, item count, etc* | `422` | Unprocessable Entity - *validation errors* | `423` | Locked User Account - *have the user contact support* | `426` | VIP Only - *user must upgrade to VIP* | `429` | Rate Limit Exceeded | `500` | Server Error - *please open a support ticket* | `502` | Service Unavailable - *server overloaded (try again in 30s)* | `503` | Service Unavailable - *server overloaded (try again in 30s)* | `504` | Service Unavailable - *server overloaded (try again in 30s)* | `520` | Service Unavailable - *Cloudflare error* | `521` | Service Unavailable - *Cloudflare error* | `522` | Service Unavailable - *Cloudflare error*  # Required Headers  You'll need to send some headers when making API calls to identify your application, set the version and set the content type to JSON.  | Header | Value | |---|---| | `Content-type` <span style=\"color:red;\">*</a> | `application/json` | | `trakt-api-key` <span style=\"color:red;\">*</a> | Your `client_id` listed under your Trakt applications. | | `trakt-api-version` <span style=\"color:red;\">*</a> | `2` | API version to use.  All `POST`, `PUT`, and `DELETE` methods require a valid OAuth `access_token`. Some `GET` calls require OAuth and others will return user specific data if OAuth is sent. Methods that &#128274; **require** or have &#128275; **optional** OAuth will be indicated.  Your OAuth library should take care of sending the auth headers for you, but for reference here's how the Bearer token should be sent.  | Header | Value | |---|---| | `Authorization` | `Bearer [access_token]` |  # Rate Limiting  All API methods are rate limited. A `429` HTTP status code is returned when the limit has been exceeded. Check the headers for detailed info, then try your API call in `Retry-After` seconds.  | Header | Value | |---|---| | `X-Ratelimit` | `{\"name\":\"UNAUTHED_API_GET_LIMIT\",\"period\":300,\"limit\":1000,\"remaining\":0,\"until\":\"2020-10-10T00:24:00Z\"}` | | `Retry-After` | `10` |  Here are the current limits. There are separate limits for authed (user level) and unauthed (application level) calls. We'll continue to adjust these limits to optimize API performance for everyone. The goal is to prevent API abuse and poor coding, but allow users to use apps normally.  | Name | Verb | Methods | Limit | |---|---|---|---| | `AUTHED_API_POST_LIMIT` | `POST`, `PUT`, `DELETE` | all | 1 call per second | | `AUTHED_API_GET_LIMIT` | `GET` | all | 1000 calls every 5 minutes | | `UNAUTHED_API_GET_LIMIT` | `GET` | all | 1000 calls every 5 minutes |  # Locked User Account  A `423` HTTP status code is returned when the OAuth user has a locked user account. Please instruct the user to [**contact Trakt support**](https://support.trakt.tv) so we can fix their account. API access will be suspended for the user until we fix their account.  # VIP Methods  Some API methods are tagged 🔥 **VIP Only**. A `426` HTTP status code is returned when the user isn't a VIP, indicating they need to sign up for [**Trakt VIP**](https://trakt.tv/vip) in order to use this method. In your app, please open a browser to `X-Upgrade-URL` so the user can sign up for Trakt VIP.  | Header | Value | |---|---| | `X-Upgrade-URL` | `https://trakt.tv/vip` |  Some API methods are tagged 🔥 **VIP Enhanced**. A `420` HTTP status code is returned when the user has exceeded their account limit. Signing up for [**Trakt VIP**](https://trakt.tv/vip) will increase these limits. If the user isn't a VIP, please open a browser to `X-Upgrade-URL` so the user can sign up for Trakt VIP. If they are already VIP and still exceeded the limit, please display a message indicating this.  | Header | Value | |---|---| | `X-Upgrade-URL` | `https://trakt.tv/vip` | | `X-VIP-User` | `true` or `false` | | `X-Account-Limit` | Limit allowed. |  # Pagination  Some methods are paginated. Methods with &#128196; **Pagination** will load 1 page of 10 items by default. Methods with &#128196; **Pagination Optional** will load all items by default. In either case, append a query string like `?page={page}&limit={limit}` to the URL to influence the results.  | Parameter | Type | Default | Value | |---|---|---|---| | `page` | integer | `1` | Number of page of results to be returned. | | `limit` | integer | `10` | Number of results to return per page. |  All paginated methods will return these HTTP headers.  | Header | Value | |---|---| | `X-Pagination-Page` | Current page. | | `X-Pagination-Limit` | Items per page. | | `X-Pagination-Page-Count` | Total number of pages. | | `X-Pagination-Item-Count` | Total number of items. |  # Extended Info  By default, all methods will return minimal info for movies, shows, episodes, people, and users. Minimal info is typically all you need to match locally cached items and includes the `title`, `year`, and `ids`. However, you can request different extended levels of information by adding `?extended={level}` to the URL. Send a comma separated string to get multiple types of extended info.  **Note:** This returns a lot of extra data, so please only use extended parameters if you actually need them!  | Level | Description | |---|---| | `full` | Complete info for an item. | `metadata` | **Collection only.** Additional video and audio info.  # Filters  Some `movies`, `shows`, `calendars`,  and `search` methods support additional filters and will be tagged with &#127898; **Filters**. Applying these filters refines the results and helps your users to more easily discover new items.  Add a query string (i.e. `?years=2016&genres=action`) with any filters you want to use. Some filters allow multiples which can be sent as comma delimited parameters. For example, `?genres=action,adventure` would match the `action` OR `adventure` genre.  **Note:** Make sure to properly URL encode the parameters including spaces and special characters.  #### Common Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | `query` | | `batman` | Search titles and descriptions. | | `years` | | `2016` | 4 digit year or range of years. | | `genres` | &#10003; | `action` | [Genre slugs.](#reference/genres) | | `languages` | &#10003; | `en` | [2 character language code.](#reference/languages) | | `countries` | &#10003; | `us` | [2 character country code.](#reference/countries) | | `runtimes` | | `30-90` | Range in minutes. | | `studios` | &#10003; | `marvel-studios` | Studio slugs. |  #### Rating Filters  Trakt, TMDB, and IMDB ratings apply to `movies`, `shows`, and `episodes`. Rotten Tomatoes and Metacritic apply to `movies`.  | Parameter | Multiples | Example | Value | |---|---|---|---| | `ratings` | | `75-100` | Trakt rating range between `0` and `100`. | | `votes` | | `5000-10000` | Trakt vote count between `0` and `100000`. | | `tmdb_ratings` | | `5.5-10.0` | TMDB rating range between `0.0` and `10.0`. | | `tmdb_votes` | | `5000-10000` | TMDB vote count between `0` and `100000`. | | `imdb_ratings` | | `5.5-10.0` | IMDB rating range between `0.0` and `10.0`. | | `imdb_votes` | | `5000-10000` | IMDB vote count between `0` and `3000000`. | | `rt_meters` | | `5.5-10.0` | Rotten Tomatoes meter range between `0` and `100`. | | `metascores` | | `5.5-10.0` | Metacritic score range between `0` and `100`. |  #### Movie Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | `certifications` | &#10003; | `pg-13` | US content certification. |  #### Show Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | `certifications` | &#10003; | `tv-pg` | US content certification. | | `networks` | &#10003; | `HBO` | Network name. | | `status` | &#10003; | `ended` | Set to `returning series`, `continuing`, `in production`, `planned`, `upcoming`,  `pilot`, `canceled`, or `ended`. |  # CORS  When creating your API app, specify the JavaScript (CORS) origins you'll be using. We use these origins to return the headers needed for CORS.  # Dates  All dates will be GMT and returned in the ISO 8601 format like `2014-09-01T09:10:11.000Z`. Adjust accordingly in your app for the user's local timezone.  # Emojis  We use short codes for emojis like `:smiley:` and `:raised_hands:` and render them on the Trakt website using [**JoyPixels**](https://www.joypixels.com/) _(verion 6.6.0)_. Methods that support emojis are tagged with &#128513; **Emojis**. For POST methods, you can send standard unicode emojis and we'll automatically convert them to short codes. For GET methods, we'll return the short codes and it's up to your app to convert them back to unicode emojis.  # Standard Media Objects  All methods will accept or return standard media objects for `movie`, `show`, `season`, `episode`, `person`, and `user` items. Here are examples for all minimal objects.  #### movie  ``` {     \"title\": \"Batman Begins\",     \"year\": 2005,     \"ids\": {         \"trakt\": 1,         \"slug\": \"batman-begins-2005\",         \"imdb\": \"tt0372784\",         \"tmdb\": 272     } } ```  #### show  ``` {     \"title\": \"Breaking Bad\",     \"year\": 2008,     \"ids\": {         \"trakt\": 1,         \"slug\": \"breaking-bad\",         \"tvdb\": 81189,         \"imdb\": \"tt0903747\",         \"tmdb\": 1396     } } ```  #### season  ``` {     \"number\": 0,     \"ids\": {         \"trakt\": 1,         \"tvdb\": 439371,         \"tmdb\": 3577     } } ```  #### episode  ``` {     \"season\": 1,     \"number\": 1,     \"title\": \"Pilot\",     \"ids\": {         \"trakt\": 16,         \"tvdb\": 349232,         \"imdb\": \"tt0959621\",         \"tmdb\": 62085     } } ```  #### person  ``` {     \"name\": \"Bryan Cranston\",     \"ids\": {         \"trakt\": 142,         \"slug\": \"bryan-cranston\",         \"imdb\": \"nm0186505\",         \"tmdb\": 17419     } } ```  #### user  ``` {     \"username\": \"sean\",     \"private\": false,     \"name\": \"Sean Rudford\",     \"vip\": true,     \"vip_ep\": true,     \"ids\": {         \"slug\": \"sean\"     } } ```  # Images  The standard media objects for all `movie`, `show`, `season`, `episode`, and `person` items include an `ids` object. These `ids` map to other services like [TMDB](https://www.themoviedb.org), [TVDB](https://thetvdb.com), [Fanart.tv](https://fanart.tv), [IMDB](https://www.imdb.com), and [OMDB](https://www.omdbapi.com/).  Most of these services have free APIs you can use to grab lots of great looking images. Here’s a chart to help you find the best artwork for your app. [**We also wrote an article to help with this.**](https://apiblog.trakt.tv/how-to-find-the-best-images-516045bcc3b6)  | Media | Type | [TMDB](https://developers.themoviedb.org/3) | [TVDB](https://api.thetvdb.com/swagger) | [Fanart.tv](http://docs.fanarttv.apiary.io) | [OMDB](https://www.omdbapi.com) | |---|---|---|---|---|---| | `shows` | `poster` | &#10003; | &#10003; | &#10003; | &#10003; | |  | `fanart` | &#10003; | &#10003; | &#10003; |  | |  | `banner` |  | &#10003; | &#10003; |  | |  | `logo` |  |  | &#10003; |  | |  | `clearart` |  |  | &#10003; |  | |  | `thumb` |  |  | &#10003; |  | | `seasons` | `poster` | &#10003; | &#10003; | &#10003; |  | |  | `banner` |  | &#10003; | &#10003; |  | |  | `thumb` |  |  | &#10003; |  | | `episodes` | `screenshot` | &#10003; | &#10003; |  |  | | `movies` | `poster` | &#10003; |  | &#10003; | &#10003; | |  | `fanart` | &#10003; |  | &#10003; |  | |  | `banner` |  |  | &#10003; |  | |  | `logo` |  |  | &#10003; |  | |  | `clearart` |  |  | &#10003; |  | |  | `thumb` |  |  | &#10003; |  | | `person` | `headshot` | &#10003; |  |  |  | |  | `character` |  | &#10003; |  |  |  # Website Media Links  There are several ways to construct direct links to media on the Trakt website. The website itself uses slugs so the URLs are more readable.  | Type | URL | |---|---| | `movie` | `/movies/:slug` | | `show` | `/shows/:slug` | | `season` | `/shows/:slug/seasons/:num` | | `episode` | `/shows/:slug/seasons/:num/episodes/:num` | | `person` | `/people/:slug` | | `comment` | `/comments/:id` | | `list` | `/lists/:id` |  You can also create links using the Trakt, IMDB, TMDB, or TVDB IDs. We recommend using the Trakt ID if possible since that will always have full coverage. If you use the search url without an `id_type` it will return search results if multiple items are found.  | Type | URL | |---|---| | `trakt` | `/search/trakt/:id` | |  | `/search/trakt/:id?id_type=movie` | |  | `/search/trakt/:id?id_type=show` | |  | `/search/trakt/:id?id_type=season` | |  | `/search/trakt/:id?id_type=episode` | |  | `/search/trakt/:id?id_type=person` | | `imdb` | `/search/imdb/:id` | | `tmdb` | `/search/tmdb/:id` | |  | `/search/tmdb/:id?id_type=movie` | |  | `/search/tmdb/:id?id_type=show` | |  | `/search/tmdb/:id?id_type=episode` | |  | `/search/tmdb/:id?id_type=person` | | `tvdb` | `/search/tvdb/:id` | |  | `/search/tvdb/:id?id_type=show` | |  | `/search/tvdb/:id?id_type=episode` |  # Third Party Libraries  All of the libraries listed below are user contributed. If you find a bug or missing feature, please contact the developer directly. These might help give your project a head start, but we can't provide direct support for any of these libraries. Please help us keep this list up to date.  | Language | Name | Repository | |---|---|---| | `C#` | `Trakt.NET` | https://github.com/henrikfroehling/Trakt.NET | |  | `TraktSharp` | https://github.com/wwarby/TraktSharp | | `C++` | `libtraqt` | https://github.com/RobertMe/libtraqt | | `Clojure` | `clj-trakt` | https://github.com/niamu/clj-trakt | | `Java` | `trakt-java` | https://github.com/UweTrottmann/trakt-java | | `Kotlin` | `trakt-api` | https://github.com/MoviebaseApp/trakt-api | | `Node.js` | `Trakt.tv` | https://github.com/vankasteelj/trakt.tv | |  | `TraktApi2` | https://github.com/PatrickE94/traktapi2 | | `Python` | `trakt.py` | https://github.com/fuzeman/trakt.py | |  | `pyTrakt` | https://github.com/moogar0880/PyTrakt | | `R` | `tRakt` | https://github.com/jemus42/tRakt | | `React Native` | `nodeless-trakt` | https://github.com/kdemoya/nodeless-trakt | | `Ruby` | `omniauth-trakt` | https://github.com/wafcio/omniauth-trakt | |  | `omniauth-trakt` | https://github.com/alextakitani/omniauth-trakt | | `Swift` | `TraktKit` | https://github.com/MaxHasADHD/TraktKit | |  | `AKTrakt` | https://github.com/arsonik/AKTrakt |  # Terminology  Trakt has a lot of features and here's a chart to help explain the differences between some of them.  | Term | Description | |---|---| | `scrobble` | Automatic way to track what a user is watching in a media center. | | `checkin` | Manual action used by mobile apps allowing the user to indicate what they are watching right now. | | `history` | All watched items (scrobbles, checkins, watched) for a user. | | `collection` | Items a user has available to watch including Blu-Rays, DVDs, and digital downloads. | | `watchlist` | Items a user wants to watch in the future. Once watched, they are auto removed from this list. | | `list` | Personal list for any purpose. Items are not auto removed from any personal lists. | | `recommendations` | Movies and TV shows a user personally recommends to others. |
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import AddHiddenItemsRequest from './model/AddHiddenItemsRequest';
import AddHiddenItemsRequestSeasonsInner from './model/AddHiddenItemsRequestSeasonsInner';
import AddHiddenItemsRequestSeasonsInnerIds from './model/AddHiddenItemsRequestSeasonsInnerIds';
import AddHiddenItemsRequestShowsInner from './model/AddHiddenItemsRequestShowsInner';
import AddHiddenItemsRequestShowsInnerSeasonsInner from './model/AddHiddenItemsRequestShowsInnerSeasonsInner';
import AddItemsToCollectionRequest from './model/AddItemsToCollectionRequest';
import AddItemsToCollectionRequestEpisodesInner from './model/AddItemsToCollectionRequestEpisodesInner';
import AddItemsToCollectionRequestEpisodesInnerIds from './model/AddItemsToCollectionRequestEpisodesInnerIds';
import AddItemsToCollectionRequestMoviesInner from './model/AddItemsToCollectionRequestMoviesInner';
import AddItemsToCollectionRequestSeasonsInner from './model/AddItemsToCollectionRequestSeasonsInner';
import AddItemsToCollectionRequestSeasonsInnerIds from './model/AddItemsToCollectionRequestSeasonsInnerIds';
import AddItemsToCollectionRequestShowsInner from './model/AddItemsToCollectionRequestShowsInner';
import AddItemsToCollectionRequestShowsInnerIds from './model/AddItemsToCollectionRequestShowsInnerIds';
import AddItemsToCollectionRequestShowsInnerSeasonsInner from './model/AddItemsToCollectionRequestShowsInnerSeasonsInner';
import AddItemsToCollectionRequestShowsInnerSeasonsInnerEpisodesInner from './model/AddItemsToCollectionRequestShowsInnerSeasonsInnerEpisodesInner';
import AddItemsToPersonalListRequest from './model/AddItemsToPersonalListRequest';
import AddItemsToPersonalListRequestMoviesInner from './model/AddItemsToPersonalListRequestMoviesInner';
import AddItemsToPersonalListRequestMoviesInnerIds from './model/AddItemsToPersonalListRequestMoviesInnerIds';
import AddItemsToPersonalListRequestPeopleInner from './model/AddItemsToPersonalListRequestPeopleInner';
import AddItemsToPersonalListRequestShowsInner from './model/AddItemsToPersonalListRequestShowsInner';
import AddItemsToPersonalRecommendationsRequest from './model/AddItemsToPersonalRecommendationsRequest';
import AddItemsToPersonalRecommendationsRequestMoviesInner from './model/AddItemsToPersonalRecommendationsRequestMoviesInner';
import AddItemsToPersonalRecommendationsRequestShowsInner from './model/AddItemsToPersonalRecommendationsRequestShowsInner';
import AddItemsToWatchedHistoryRequest from './model/AddItemsToWatchedHistoryRequest';
import AddItemsToWatchedHistoryRequestEpisodesInner from './model/AddItemsToWatchedHistoryRequestEpisodesInner';
import AddItemsToWatchedHistoryRequestMoviesInner from './model/AddItemsToWatchedHistoryRequestMoviesInner';
import AddItemsToWatchedHistoryRequestSeasonsInner from './model/AddItemsToWatchedHistoryRequestSeasonsInner';
import AddItemsToWatchedHistoryRequestShowsInner from './model/AddItemsToWatchedHistoryRequestShowsInner';
import AddItemsToWatchedHistoryRequestShowsInnerSeasonsInner from './model/AddItemsToWatchedHistoryRequestShowsInnerSeasonsInner';
import AddItemsToWatchedHistoryRequestShowsInnerSeasonsInnerEpisodesInner from './model/AddItemsToWatchedHistoryRequestShowsInnerSeasonsInnerEpisodesInner';
import AddItemsToWatchlistRequest from './model/AddItemsToWatchlistRequest';
import AddItemsToWatchlistRequestShowsInner from './model/AddItemsToWatchlistRequestShowsInner';
import AddNewRatingsRequest from './model/AddNewRatingsRequest';
import AddNewRatingsRequestEpisodesInner from './model/AddNewRatingsRequestEpisodesInner';
import AddNewRatingsRequestMoviesInner from './model/AddNewRatingsRequestMoviesInner';
import AddNewRatingsRequestSeasonsInner from './model/AddNewRatingsRequestSeasonsInner';
import AddNewRatingsRequestShowsInner from './model/AddNewRatingsRequestShowsInner';
import AddNewRatingsRequestShowsInnerSeasonsInner from './model/AddNewRatingsRequestShowsInnerSeasonsInner';
import AddNewRatingsRequestShowsInnerSeasonsInnerEpisodesInner from './model/AddNewRatingsRequestShowsInnerSeasonsInnerEpisodesInner';
import CheckIntoAnItemRequest from './model/CheckIntoAnItemRequest';
import CheckIntoAnItemRequestMovie from './model/CheckIntoAnItemRequestMovie';
import CheckIntoAnItemRequestMovieIds from './model/CheckIntoAnItemRequestMovieIds';
import CheckIntoAnItemRequestSharing from './model/CheckIntoAnItemRequestSharing';
import CreatePersonalListRequest from './model/CreatePersonalListRequest';
import ExchangeRefreshTokenForAccessTokenRequest from './model/ExchangeRefreshTokenForAccessTokenRequest';
import GenerateNewDeviceCodesRequest from './model/GenerateNewDeviceCodesRequest';
import PauseWatchingInAMediaCenterRequest from './model/PauseWatchingInAMediaCenterRequest';
import PollForTheAccessTokenRequest from './model/PollForTheAccessTokenRequest';
import PostACommentRequest from './model/PostACommentRequest';
import PostACommentRequestSharing from './model/PostACommentRequestSharing';
import PostAReplyForACommentRequest from './model/PostAReplyForACommentRequest';
import RemoveItemsFromCollectionRequest from './model/RemoveItemsFromCollectionRequest';
import RemoveItemsFromCollectionRequestMoviesInner from './model/RemoveItemsFromCollectionRequestMoviesInner';
import RemoveItemsFromCollectionRequestShowsInner from './model/RemoveItemsFromCollectionRequestShowsInner';
import RemoveItemsFromCollectionRequestShowsInnerSeasonsInner from './model/RemoveItemsFromCollectionRequestShowsInnerSeasonsInner';
import RemoveItemsFromCollectionRequestShowsInnerSeasonsInnerEpisodesInner from './model/RemoveItemsFromCollectionRequestShowsInnerSeasonsInnerEpisodesInner';
import RemoveItemsFromHistoryRequest from './model/RemoveItemsFromHistoryRequest';
import RemoveItemsFromPersonalListRequest from './model/RemoveItemsFromPersonalListRequest';
import RemoveItemsFromPersonalListRequestMoviesInner from './model/RemoveItemsFromPersonalListRequestMoviesInner';
import RemoveItemsFromPersonalListRequestShowsInner from './model/RemoveItemsFromPersonalListRequestShowsInner';
import RemoveItemsFromPersonalRecommendationsRequest from './model/RemoveItemsFromPersonalRecommendationsRequest';
import RemoveItemsFromPersonalRecommendationsRequestShowsInner from './model/RemoveItemsFromPersonalRecommendationsRequestShowsInner';
import ReorderAUserSListsRequest from './model/ReorderAUserSListsRequest';
import ReorderPersonallyRecommendedItemsRequest from './model/ReorderPersonallyRecommendedItemsRequest';
import RevokeAnAccessTokenRequest from './model/RevokeAnAccessTokenRequest';
import StartWatchingInAMediaCenterRequest from './model/StartWatchingInAMediaCenterRequest';
import StopOrFinishWatchingInAMediaCenterRequest from './model/StopOrFinishWatchingInAMediaCenterRequest';
import UpdateACommentOrReplyRequest from './model/UpdateACommentOrReplyRequest';
import UpdatePersonalListRequest from './model/UpdatePersonalListRequest';
import AuthenticationDevicesApi from './api/AuthenticationDevicesApi';
import AuthenticationOAuthApi from './api/AuthenticationOAuthApi';
import CalendarsApi from './api/CalendarsApi';
import CertificationsApi from './api/CertificationsApi';
import CheckinApi from './api/CheckinApi';
import CommentsApi from './api/CommentsApi';
import CountriesApi from './api/CountriesApi';
import EpisodesApi from './api/EpisodesApi';
import GenresApi from './api/GenresApi';
import LanguagesApi from './api/LanguagesApi';
import ListsApi from './api/ListsApi';
import MoviesApi from './api/MoviesApi';
import NetworksApi from './api/NetworksApi';
import PeopleApi from './api/PeopleApi';
import RecommendationsApi from './api/RecommendationsApi';
import ScrobbleApi from './api/ScrobbleApi';
import SearchApi from './api/SearchApi';
import SeasonsApi from './api/SeasonsApi';
import ShowsApi from './api/ShowsApi';
import SyncApi from './api/SyncApi';
import UsersApi from './api/UsersApi';


/**
* At Trakt, we collect lots of interesting information about what tv shows and movies everyone is watching. Part of the fun with such data is making it available for anyone to mash up and use on their own site or app. The Trakt API was made just for this purpose. It is very easy to use, you basically call a URL and get some JSON back.  More complex API calls (such as adding a movie or show to your collection) involve sending us data. These are still easy to use, you simply POST some JSON data to a specific URL.  Make sure to check out the [**Required Headers**](#introduction/required-headers) and [**Authentication**](#reference/authentication-oauth) sections for more info on what needs to be sent with each API call. Also check out the [**Terminology**](#introduction/terminology) section insight into the features Trakt supports.  # Create an App  To use the Trakt API, you&#39;ll need to [**create a new API app**](https://trakt.tv/oauth/applications/new).  # Stay Connected  API discussion and bugs should be posted in the [**GitHub Developer Forum**](https://github.com/trakt/api-help/issues) and *watch* the repository if you&#39;d like to get notifications. Make sure to follow our [**API Blog**](https://apiblog.trakt.tv) and [**@traktapi on Twitter**](https://twitter.com/traktapi) too.  # API URL  The API should always be accessed over SSL.  &#x60;&#x60;&#x60; https://api.trakt.tv &#x60;&#x60;&#x60;  If you would like to use our sandbox environment to not fill production with test data, use this URL over SSL. **Note:** Staging is a completely separate environment, so you&#39;ll need to [**create a new API app on staging**](https://staging.trakt.tv/oauth/applications/new).  &#x60;&#x60;&#x60; https://api-staging.trakt.tv &#x60;&#x60;&#x60;  # Verbs  The API uses restful verbs.  | Verb | Description | |---|---| | &#x60;GET&#x60; | Select one or more items. Success returns &#x60;200&#x60; status code. | | &#x60;POST&#x60; | Create a new item. Success returns &#x60;201&#x60; status code. | | &#x60;PUT&#x60; | Update an item. Success returns &#x60;200&#x60; status code. | | &#x60;DELETE&#x60; | Delete an item. Success returns &#x60;200&#x60; or &#x60;204&#x60; status code. |  # Status Codes  The API will respond with one of the following HTTP status codes.  | Code | Description | |---|---| | &#x60;200&#x60; | Success | &#x60;201&#x60; | Success - *new resource created (POST)* | &#x60;204&#x60; | Success - *no content to return (DELETE)* | &#x60;400&#x60; | Bad Request - *request couldn&#39;t be parsed* | &#x60;401&#x60; | Unauthorized - *OAuth must be provided* | &#x60;403&#x60; | Forbidden - *invalid API key or unapproved app* | &#x60;404&#x60; | Not Found - *method exists, but no record found* | &#x60;405&#x60; | Method Not Found - *method doesn&#39;t exist* | &#x60;409&#x60; | Conflict - *resource already created* | &#x60;412&#x60; | Precondition Failed - *use application/json content type* | &#x60;420&#x60; | Account Limit Exceeded - *list count, item count, etc* | &#x60;422&#x60; | Unprocessable Entity - *validation errors* | &#x60;423&#x60; | Locked User Account - *have the user contact support* | &#x60;426&#x60; | VIP Only - *user must upgrade to VIP* | &#x60;429&#x60; | Rate Limit Exceeded | &#x60;500&#x60; | Server Error - *please open a support ticket* | &#x60;502&#x60; | Service Unavailable - *server overloaded (try again in 30s)* | &#x60;503&#x60; | Service Unavailable - *server overloaded (try again in 30s)* | &#x60;504&#x60; | Service Unavailable - *server overloaded (try again in 30s)* | &#x60;520&#x60; | Service Unavailable - *Cloudflare error* | &#x60;521&#x60; | Service Unavailable - *Cloudflare error* | &#x60;522&#x60; | Service Unavailable - *Cloudflare error*  # Required Headers  You&#39;ll need to send some headers when making API calls to identify your application, set the version and set the content type to JSON.  | Header | Value | |---|---| | &#x60;Content-type&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | &#x60;application/json&#x60; | | &#x60;trakt-api-key&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | Your &#x60;client_id&#x60; listed under your Trakt applications. | | &#x60;trakt-api-version&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | &#x60;2&#x60; | API version to use.  All &#x60;POST&#x60;, &#x60;PUT&#x60;, and &#x60;DELETE&#x60; methods require a valid OAuth &#x60;access_token&#x60;. Some &#x60;GET&#x60; calls require OAuth and others will return user specific data if OAuth is sent. Methods that &amp;#128274; **require** or have &amp;#128275; **optional** OAuth will be indicated.  Your OAuth library should take care of sending the auth headers for you, but for reference here&#39;s how the Bearer token should be sent.  | Header | Value | |---|---| | &#x60;Authorization&#x60; | &#x60;Bearer [access_token]&#x60; |  # Rate Limiting  All API methods are rate limited. A &#x60;429&#x60; HTTP status code is returned when the limit has been exceeded. Check the headers for detailed info, then try your API call in &#x60;Retry-After&#x60; seconds.  | Header | Value | |---|---| | &#x60;X-Ratelimit&#x60; | &#x60;{\&quot;name\&quot;:\&quot;UNAUTHED_API_GET_LIMIT\&quot;,\&quot;period\&quot;:300,\&quot;limit\&quot;:1000,\&quot;remaining\&quot;:0,\&quot;until\&quot;:\&quot;2020-10-10T00:24:00Z\&quot;}&#x60; | | &#x60;Retry-After&#x60; | &#x60;10&#x60; |  Here are the current limits. There are separate limits for authed (user level) and unauthed (application level) calls. We&#39;ll continue to adjust these limits to optimize API performance for everyone. The goal is to prevent API abuse and poor coding, but allow users to use apps normally.  | Name | Verb | Methods | Limit | |---|---|---|---| | &#x60;AUTHED_API_POST_LIMIT&#x60; | &#x60;POST&#x60;, &#x60;PUT&#x60;, &#x60;DELETE&#x60; | all | 1 call per second | | &#x60;AUTHED_API_GET_LIMIT&#x60; | &#x60;GET&#x60; | all | 1000 calls every 5 minutes | | &#x60;UNAUTHED_API_GET_LIMIT&#x60; | &#x60;GET&#x60; | all | 1000 calls every 5 minutes |  # Locked User Account  A &#x60;423&#x60; HTTP status code is returned when the OAuth user has a locked user account. Please instruct the user to [**contact Trakt support**](https://support.trakt.tv) so we can fix their account. API access will be suspended for the user until we fix their account.  # VIP Methods  Some API methods are tagged 🔥 **VIP Only**. A &#x60;426&#x60; HTTP status code is returned when the user isn&#39;t a VIP, indicating they need to sign up for [**Trakt VIP**](https://trakt.tv/vip) in order to use this method. In your app, please open a browser to &#x60;X-Upgrade-URL&#x60; so the user can sign up for Trakt VIP.  | Header | Value | |---|---| | &#x60;X-Upgrade-URL&#x60; | &#x60;https://trakt.tv/vip&#x60; |  Some API methods are tagged 🔥 **VIP Enhanced**. A &#x60;420&#x60; HTTP status code is returned when the user has exceeded their account limit. Signing up for [**Trakt VIP**](https://trakt.tv/vip) will increase these limits. If the user isn&#39;t a VIP, please open a browser to &#x60;X-Upgrade-URL&#x60; so the user can sign up for Trakt VIP. If they are already VIP and still exceeded the limit, please display a message indicating this.  | Header | Value | |---|---| | &#x60;X-Upgrade-URL&#x60; | &#x60;https://trakt.tv/vip&#x60; | | &#x60;X-VIP-User&#x60; | &#x60;true&#x60; or &#x60;false&#x60; | | &#x60;X-Account-Limit&#x60; | Limit allowed. |  # Pagination  Some methods are paginated. Methods with &amp;#128196; **Pagination** will load 1 page of 10 items by default. Methods with &amp;#128196; **Pagination Optional** will load all items by default. In either case, append a query string like &#x60;?page&#x3D;{page}&amp;limit&#x3D;{limit}&#x60; to the URL to influence the results.  | Parameter | Type | Default | Value | |---|---|---|---| | &#x60;page&#x60; | integer | &#x60;1&#x60; | Number of page of results to be returned. | | &#x60;limit&#x60; | integer | &#x60;10&#x60; | Number of results to return per page. |  All paginated methods will return these HTTP headers.  | Header | Value | |---|---| | &#x60;X-Pagination-Page&#x60; | Current page. | | &#x60;X-Pagination-Limit&#x60; | Items per page. | | &#x60;X-Pagination-Page-Count&#x60; | Total number of pages. | | &#x60;X-Pagination-Item-Count&#x60; | Total number of items. |  # Extended Info  By default, all methods will return minimal info for movies, shows, episodes, people, and users. Minimal info is typically all you need to match locally cached items and includes the &#x60;title&#x60;, &#x60;year&#x60;, and &#x60;ids&#x60;. However, you can request different extended levels of information by adding &#x60;?extended&#x3D;{level}&#x60; to the URL. Send a comma separated string to get multiple types of extended info.  **Note:** This returns a lot of extra data, so please only use extended parameters if you actually need them!  | Level | Description | |---|---| | &#x60;full&#x60; | Complete info for an item. | &#x60;metadata&#x60; | **Collection only.** Additional video and audio info.  # Filters  Some &#x60;movies&#x60;, &#x60;shows&#x60;, &#x60;calendars&#x60;,  and &#x60;search&#x60; methods support additional filters and will be tagged with &amp;#127898; **Filters**. Applying these filters refines the results and helps your users to more easily discover new items.  Add a query string (i.e. &#x60;?years&#x3D;2016&amp;genres&#x3D;action&#x60;) with any filters you want to use. Some filters allow multiples which can be sent as comma delimited parameters. For example, &#x60;?genres&#x3D;action,adventure&#x60; would match the &#x60;action&#x60; OR &#x60;adventure&#x60; genre.  **Note:** Make sure to properly URL encode the parameters including spaces and special characters.  #### Common Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | &#x60;query&#x60; | | &#x60;batman&#x60; | Search titles and descriptions. | | &#x60;years&#x60; | | &#x60;2016&#x60; | 4 digit year or range of years. | | &#x60;genres&#x60; | &amp;#10003; | &#x60;action&#x60; | [Genre slugs.](#reference/genres) | | &#x60;languages&#x60; | &amp;#10003; | &#x60;en&#x60; | [2 character language code.](#reference/languages) | | &#x60;countries&#x60; | &amp;#10003; | &#x60;us&#x60; | [2 character country code.](#reference/countries) | | &#x60;runtimes&#x60; | | &#x60;30-90&#x60; | Range in minutes. | | &#x60;studios&#x60; | &amp;#10003; | &#x60;marvel-studios&#x60; | Studio slugs. |  #### Rating Filters  Trakt, TMDB, and IMDB ratings apply to &#x60;movies&#x60;, &#x60;shows&#x60;, and &#x60;episodes&#x60;. Rotten Tomatoes and Metacritic apply to &#x60;movies&#x60;.  | Parameter | Multiples | Example | Value | |---|---|---|---| | &#x60;ratings&#x60; | | &#x60;75-100&#x60; | Trakt rating range between &#x60;0&#x60; and &#x60;100&#x60;. | | &#x60;votes&#x60; | | &#x60;5000-10000&#x60; | Trakt vote count between &#x60;0&#x60; and &#x60;100000&#x60;. | | &#x60;tmdb_ratings&#x60; | | &#x60;5.5-10.0&#x60; | TMDB rating range between &#x60;0.0&#x60; and &#x60;10.0&#x60;. | | &#x60;tmdb_votes&#x60; | | &#x60;5000-10000&#x60; | TMDB vote count between &#x60;0&#x60; and &#x60;100000&#x60;. | | &#x60;imdb_ratings&#x60; | | &#x60;5.5-10.0&#x60; | IMDB rating range between &#x60;0.0&#x60; and &#x60;10.0&#x60;. | | &#x60;imdb_votes&#x60; | | &#x60;5000-10000&#x60; | IMDB vote count between &#x60;0&#x60; and &#x60;3000000&#x60;. | | &#x60;rt_meters&#x60; | | &#x60;5.5-10.0&#x60; | Rotten Tomatoes meter range between &#x60;0&#x60; and &#x60;100&#x60;. | | &#x60;metascores&#x60; | | &#x60;5.5-10.0&#x60; | Metacritic score range between &#x60;0&#x60; and &#x60;100&#x60;. |  #### Movie Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | &#x60;certifications&#x60; | &amp;#10003; | &#x60;pg-13&#x60; | US content certification. |  #### Show Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | &#x60;certifications&#x60; | &amp;#10003; | &#x60;tv-pg&#x60; | US content certification. | | &#x60;networks&#x60; | &amp;#10003; | &#x60;HBO&#x60; | Network name. | | &#x60;status&#x60; | &amp;#10003; | &#x60;ended&#x60; | Set to &#x60;returning series&#x60;, &#x60;continuing&#x60;, &#x60;in production&#x60;, &#x60;planned&#x60;, &#x60;upcoming&#x60;,  &#x60;pilot&#x60;, &#x60;canceled&#x60;, or &#x60;ended&#x60;. |  # CORS  When creating your API app, specify the JavaScript (CORS) origins you&#39;ll be using. We use these origins to return the headers needed for CORS.  # Dates  All dates will be GMT and returned in the ISO 8601 format like &#x60;2014-09-01T09:10:11.000Z&#x60;. Adjust accordingly in your app for the user&#39;s local timezone.  # Emojis  We use short codes for emojis like &#x60;:smiley:&#x60; and &#x60;:raised_hands:&#x60; and render them on the Trakt website using [**JoyPixels**](https://www.joypixels.com/) _(verion 6.6.0)_. Methods that support emojis are tagged with &amp;#128513; **Emojis**. For POST methods, you can send standard unicode emojis and we&#39;ll automatically convert them to short codes. For GET methods, we&#39;ll return the short codes and it&#39;s up to your app to convert them back to unicode emojis.  # Standard Media Objects  All methods will accept or return standard media objects for &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, &#x60;person&#x60;, and &#x60;user&#x60; items. Here are examples for all minimal objects.  #### movie  &#x60;&#x60;&#x60; {     \&quot;title\&quot;: \&quot;Batman Begins\&quot;,     \&quot;year\&quot;: 2005,     \&quot;ids\&quot;: {         \&quot;trakt\&quot;: 1,         \&quot;slug\&quot;: \&quot;batman-begins-2005\&quot;,         \&quot;imdb\&quot;: \&quot;tt0372784\&quot;,         \&quot;tmdb\&quot;: 272     } } &#x60;&#x60;&#x60;  #### show  &#x60;&#x60;&#x60; {     \&quot;title\&quot;: \&quot;Breaking Bad\&quot;,     \&quot;year\&quot;: 2008,     \&quot;ids\&quot;: {         \&quot;trakt\&quot;: 1,         \&quot;slug\&quot;: \&quot;breaking-bad\&quot;,         \&quot;tvdb\&quot;: 81189,         \&quot;imdb\&quot;: \&quot;tt0903747\&quot;,         \&quot;tmdb\&quot;: 1396     } } &#x60;&#x60;&#x60;  #### season  &#x60;&#x60;&#x60; {     \&quot;number\&quot;: 0,     \&quot;ids\&quot;: {         \&quot;trakt\&quot;: 1,         \&quot;tvdb\&quot;: 439371,         \&quot;tmdb\&quot;: 3577     } } &#x60;&#x60;&#x60;  #### episode  &#x60;&#x60;&#x60; {     \&quot;season\&quot;: 1,     \&quot;number\&quot;: 1,     \&quot;title\&quot;: \&quot;Pilot\&quot;,     \&quot;ids\&quot;: {         \&quot;trakt\&quot;: 16,         \&quot;tvdb\&quot;: 349232,         \&quot;imdb\&quot;: \&quot;tt0959621\&quot;,         \&quot;tmdb\&quot;: 62085     } } &#x60;&#x60;&#x60;  #### person  &#x60;&#x60;&#x60; {     \&quot;name\&quot;: \&quot;Bryan Cranston\&quot;,     \&quot;ids\&quot;: {         \&quot;trakt\&quot;: 142,         \&quot;slug\&quot;: \&quot;bryan-cranston\&quot;,         \&quot;imdb\&quot;: \&quot;nm0186505\&quot;,         \&quot;tmdb\&quot;: 17419     } } &#x60;&#x60;&#x60;  #### user  &#x60;&#x60;&#x60; {     \&quot;username\&quot;: \&quot;sean\&quot;,     \&quot;private\&quot;: false,     \&quot;name\&quot;: \&quot;Sean Rudford\&quot;,     \&quot;vip\&quot;: true,     \&quot;vip_ep\&quot;: true,     \&quot;ids\&quot;: {         \&quot;slug\&quot;: \&quot;sean\&quot;     } } &#x60;&#x60;&#x60;  # Images  The standard media objects for all &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, and &#x60;person&#x60; items include an &#x60;ids&#x60; object. These &#x60;ids&#x60; map to other services like [TMDB](https://www.themoviedb.org), [TVDB](https://thetvdb.com), [Fanart.tv](https://fanart.tv), [IMDB](https://www.imdb.com), and [OMDB](https://www.omdbapi.com/).  Most of these services have free APIs you can use to grab lots of great looking images. Here’s a chart to help you find the best artwork for your app. [**We also wrote an article to help with this.**](https://apiblog.trakt.tv/how-to-find-the-best-images-516045bcc3b6)  | Media | Type | [TMDB](https://developers.themoviedb.org/3) | [TVDB](https://api.thetvdb.com/swagger) | [Fanart.tv](http://docs.fanarttv.apiary.io) | [OMDB](https://www.omdbapi.com) | |---|---|---|---|---|---| | &#x60;shows&#x60; | &#x60;poster&#x60; | &amp;#10003; | &amp;#10003; | &amp;#10003; | &amp;#10003; | |  | &#x60;fanart&#x60; | &amp;#10003; | &amp;#10003; | &amp;#10003; |  | |  | &#x60;banner&#x60; |  | &amp;#10003; | &amp;#10003; |  | |  | &#x60;logo&#x60; |  |  | &amp;#10003; |  | |  | &#x60;clearart&#x60; |  |  | &amp;#10003; |  | |  | &#x60;thumb&#x60; |  |  | &amp;#10003; |  | | &#x60;seasons&#x60; | &#x60;poster&#x60; | &amp;#10003; | &amp;#10003; | &amp;#10003; |  | |  | &#x60;banner&#x60; |  | &amp;#10003; | &amp;#10003; |  | |  | &#x60;thumb&#x60; |  |  | &amp;#10003; |  | | &#x60;episodes&#x60; | &#x60;screenshot&#x60; | &amp;#10003; | &amp;#10003; |  |  | | &#x60;movies&#x60; | &#x60;poster&#x60; | &amp;#10003; |  | &amp;#10003; | &amp;#10003; | |  | &#x60;fanart&#x60; | &amp;#10003; |  | &amp;#10003; |  | |  | &#x60;banner&#x60; |  |  | &amp;#10003; |  | |  | &#x60;logo&#x60; |  |  | &amp;#10003; |  | |  | &#x60;clearart&#x60; |  |  | &amp;#10003; |  | |  | &#x60;thumb&#x60; |  |  | &amp;#10003; |  | | &#x60;person&#x60; | &#x60;headshot&#x60; | &amp;#10003; |  |  |  | |  | &#x60;character&#x60; |  | &amp;#10003; |  |  |  # Website Media Links  There are several ways to construct direct links to media on the Trakt website. The website itself uses slugs so the URLs are more readable.  | Type | URL | |---|---| | &#x60;movie&#x60; | &#x60;/movies/:slug&#x60; | | &#x60;show&#x60; | &#x60;/shows/:slug&#x60; | | &#x60;season&#x60; | &#x60;/shows/:slug/seasons/:num&#x60; | | &#x60;episode&#x60; | &#x60;/shows/:slug/seasons/:num/episodes/:num&#x60; | | &#x60;person&#x60; | &#x60;/people/:slug&#x60; | | &#x60;comment&#x60; | &#x60;/comments/:id&#x60; | | &#x60;list&#x60; | &#x60;/lists/:id&#x60; |  You can also create links using the Trakt, IMDB, TMDB, or TVDB IDs. We recommend using the Trakt ID if possible since that will always have full coverage. If you use the search url without an &#x60;id_type&#x60; it will return search results if multiple items are found.  | Type | URL | |---|---| | &#x60;trakt&#x60; | &#x60;/search/trakt/:id&#x60; | |  | &#x60;/search/trakt/:id?id_type&#x3D;movie&#x60; | |  | &#x60;/search/trakt/:id?id_type&#x3D;show&#x60; | |  | &#x60;/search/trakt/:id?id_type&#x3D;season&#x60; | |  | &#x60;/search/trakt/:id?id_type&#x3D;episode&#x60; | |  | &#x60;/search/trakt/:id?id_type&#x3D;person&#x60; | | &#x60;imdb&#x60; | &#x60;/search/imdb/:id&#x60; | | &#x60;tmdb&#x60; | &#x60;/search/tmdb/:id&#x60; | |  | &#x60;/search/tmdb/:id?id_type&#x3D;movie&#x60; | |  | &#x60;/search/tmdb/:id?id_type&#x3D;show&#x60; | |  | &#x60;/search/tmdb/:id?id_type&#x3D;episode&#x60; | |  | &#x60;/search/tmdb/:id?id_type&#x3D;person&#x60; | | &#x60;tvdb&#x60; | &#x60;/search/tvdb/:id&#x60; | |  | &#x60;/search/tvdb/:id?id_type&#x3D;show&#x60; | |  | &#x60;/search/tvdb/:id?id_type&#x3D;episode&#x60; |  # Third Party Libraries  All of the libraries listed below are user contributed. If you find a bug or missing feature, please contact the developer directly. These might help give your project a head start, but we can&#39;t provide direct support for any of these libraries. Please help us keep this list up to date.  | Language | Name | Repository | |---|---|---| | &#x60;C#&#x60; | &#x60;Trakt.NET&#x60; | https://github.com/henrikfroehling/Trakt.NET | |  | &#x60;TraktSharp&#x60; | https://github.com/wwarby/TraktSharp | | &#x60;C++&#x60; | &#x60;libtraqt&#x60; | https://github.com/RobertMe/libtraqt | | &#x60;Clojure&#x60; | &#x60;clj-trakt&#x60; | https://github.com/niamu/clj-trakt | | &#x60;Java&#x60; | &#x60;trakt-java&#x60; | https://github.com/UweTrottmann/trakt-java | | &#x60;Kotlin&#x60; | &#x60;trakt-api&#x60; | https://github.com/MoviebaseApp/trakt-api | | &#x60;Node.js&#x60; | &#x60;Trakt.tv&#x60; | https://github.com/vankasteelj/trakt.tv | |  | &#x60;TraktApi2&#x60; | https://github.com/PatrickE94/traktapi2 | | &#x60;Python&#x60; | &#x60;trakt.py&#x60; | https://github.com/fuzeman/trakt.py | |  | &#x60;pyTrakt&#x60; | https://github.com/moogar0880/PyTrakt | | &#x60;R&#x60; | &#x60;tRakt&#x60; | https://github.com/jemus42/tRakt | | &#x60;React Native&#x60; | &#x60;nodeless-trakt&#x60; | https://github.com/kdemoya/nodeless-trakt | | &#x60;Ruby&#x60; | &#x60;omniauth-trakt&#x60; | https://github.com/wafcio/omniauth-trakt | |  | &#x60;omniauth-trakt&#x60; | https://github.com/alextakitani/omniauth-trakt | | &#x60;Swift&#x60; | &#x60;TraktKit&#x60; | https://github.com/MaxHasADHD/TraktKit | |  | &#x60;AKTrakt&#x60; | https://github.com/arsonik/AKTrakt |  # Terminology  Trakt has a lot of features and here&#39;s a chart to help explain the differences between some of them.  | Term | Description | |---|---| | &#x60;scrobble&#x60; | Automatic way to track what a user is watching in a media center. | | &#x60;checkin&#x60; | Manual action used by mobile apps allowing the user to indicate what they are watching right now. | | &#x60;history&#x60; | All watched items (scrobbles, checkins, watched) for a user. | | &#x60;collection&#x60; | Items a user has available to watch including Blu-Rays, DVDs, and digital downloads. | | &#x60;watchlist&#x60; | Items a user wants to watch in the future. Once watched, they are auto removed from this list. | | &#x60;list&#x60; | Personal list for any purpose. Items are not auto removed from any personal lists. | | &#x60;recommendations&#x60; | Movies and TV shows a user personally recommends to others. |.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var TraktApi = require('index'); // See note below*.
* var xxxSvc = new TraktApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new TraktApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new TraktApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new TraktApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AddHiddenItemsRequest model constructor.
     * @property {module:model/AddHiddenItemsRequest}
     */
    AddHiddenItemsRequest,

    /**
     * The AddHiddenItemsRequestSeasonsInner model constructor.
     * @property {module:model/AddHiddenItemsRequestSeasonsInner}
     */
    AddHiddenItemsRequestSeasonsInner,

    /**
     * The AddHiddenItemsRequestSeasonsInnerIds model constructor.
     * @property {module:model/AddHiddenItemsRequestSeasonsInnerIds}
     */
    AddHiddenItemsRequestSeasonsInnerIds,

    /**
     * The AddHiddenItemsRequestShowsInner model constructor.
     * @property {module:model/AddHiddenItemsRequestShowsInner}
     */
    AddHiddenItemsRequestShowsInner,

    /**
     * The AddHiddenItemsRequestShowsInnerSeasonsInner model constructor.
     * @property {module:model/AddHiddenItemsRequestShowsInnerSeasonsInner}
     */
    AddHiddenItemsRequestShowsInnerSeasonsInner,

    /**
     * The AddItemsToCollectionRequest model constructor.
     * @property {module:model/AddItemsToCollectionRequest}
     */
    AddItemsToCollectionRequest,

    /**
     * The AddItemsToCollectionRequestEpisodesInner model constructor.
     * @property {module:model/AddItemsToCollectionRequestEpisodesInner}
     */
    AddItemsToCollectionRequestEpisodesInner,

    /**
     * The AddItemsToCollectionRequestEpisodesInnerIds model constructor.
     * @property {module:model/AddItemsToCollectionRequestEpisodesInnerIds}
     */
    AddItemsToCollectionRequestEpisodesInnerIds,

    /**
     * The AddItemsToCollectionRequestMoviesInner model constructor.
     * @property {module:model/AddItemsToCollectionRequestMoviesInner}
     */
    AddItemsToCollectionRequestMoviesInner,

    /**
     * The AddItemsToCollectionRequestSeasonsInner model constructor.
     * @property {module:model/AddItemsToCollectionRequestSeasonsInner}
     */
    AddItemsToCollectionRequestSeasonsInner,

    /**
     * The AddItemsToCollectionRequestSeasonsInnerIds model constructor.
     * @property {module:model/AddItemsToCollectionRequestSeasonsInnerIds}
     */
    AddItemsToCollectionRequestSeasonsInnerIds,

    /**
     * The AddItemsToCollectionRequestShowsInner model constructor.
     * @property {module:model/AddItemsToCollectionRequestShowsInner}
     */
    AddItemsToCollectionRequestShowsInner,

    /**
     * The AddItemsToCollectionRequestShowsInnerIds model constructor.
     * @property {module:model/AddItemsToCollectionRequestShowsInnerIds}
     */
    AddItemsToCollectionRequestShowsInnerIds,

    /**
     * The AddItemsToCollectionRequestShowsInnerSeasonsInner model constructor.
     * @property {module:model/AddItemsToCollectionRequestShowsInnerSeasonsInner}
     */
    AddItemsToCollectionRequestShowsInnerSeasonsInner,

    /**
     * The AddItemsToCollectionRequestShowsInnerSeasonsInnerEpisodesInner model constructor.
     * @property {module:model/AddItemsToCollectionRequestShowsInnerSeasonsInnerEpisodesInner}
     */
    AddItemsToCollectionRequestShowsInnerSeasonsInnerEpisodesInner,

    /**
     * The AddItemsToPersonalListRequest model constructor.
     * @property {module:model/AddItemsToPersonalListRequest}
     */
    AddItemsToPersonalListRequest,

    /**
     * The AddItemsToPersonalListRequestMoviesInner model constructor.
     * @property {module:model/AddItemsToPersonalListRequestMoviesInner}
     */
    AddItemsToPersonalListRequestMoviesInner,

    /**
     * The AddItemsToPersonalListRequestMoviesInnerIds model constructor.
     * @property {module:model/AddItemsToPersonalListRequestMoviesInnerIds}
     */
    AddItemsToPersonalListRequestMoviesInnerIds,

    /**
     * The AddItemsToPersonalListRequestPeopleInner model constructor.
     * @property {module:model/AddItemsToPersonalListRequestPeopleInner}
     */
    AddItemsToPersonalListRequestPeopleInner,

    /**
     * The AddItemsToPersonalListRequestShowsInner model constructor.
     * @property {module:model/AddItemsToPersonalListRequestShowsInner}
     */
    AddItemsToPersonalListRequestShowsInner,

    /**
     * The AddItemsToPersonalRecommendationsRequest model constructor.
     * @property {module:model/AddItemsToPersonalRecommendationsRequest}
     */
    AddItemsToPersonalRecommendationsRequest,

    /**
     * The AddItemsToPersonalRecommendationsRequestMoviesInner model constructor.
     * @property {module:model/AddItemsToPersonalRecommendationsRequestMoviesInner}
     */
    AddItemsToPersonalRecommendationsRequestMoviesInner,

    /**
     * The AddItemsToPersonalRecommendationsRequestShowsInner model constructor.
     * @property {module:model/AddItemsToPersonalRecommendationsRequestShowsInner}
     */
    AddItemsToPersonalRecommendationsRequestShowsInner,

    /**
     * The AddItemsToWatchedHistoryRequest model constructor.
     * @property {module:model/AddItemsToWatchedHistoryRequest}
     */
    AddItemsToWatchedHistoryRequest,

    /**
     * The AddItemsToWatchedHistoryRequestEpisodesInner model constructor.
     * @property {module:model/AddItemsToWatchedHistoryRequestEpisodesInner}
     */
    AddItemsToWatchedHistoryRequestEpisodesInner,

    /**
     * The AddItemsToWatchedHistoryRequestMoviesInner model constructor.
     * @property {module:model/AddItemsToWatchedHistoryRequestMoviesInner}
     */
    AddItemsToWatchedHistoryRequestMoviesInner,

    /**
     * The AddItemsToWatchedHistoryRequestSeasonsInner model constructor.
     * @property {module:model/AddItemsToWatchedHistoryRequestSeasonsInner}
     */
    AddItemsToWatchedHistoryRequestSeasonsInner,

    /**
     * The AddItemsToWatchedHistoryRequestShowsInner model constructor.
     * @property {module:model/AddItemsToWatchedHistoryRequestShowsInner}
     */
    AddItemsToWatchedHistoryRequestShowsInner,

    /**
     * The AddItemsToWatchedHistoryRequestShowsInnerSeasonsInner model constructor.
     * @property {module:model/AddItemsToWatchedHistoryRequestShowsInnerSeasonsInner}
     */
    AddItemsToWatchedHistoryRequestShowsInnerSeasonsInner,

    /**
     * The AddItemsToWatchedHistoryRequestShowsInnerSeasonsInnerEpisodesInner model constructor.
     * @property {module:model/AddItemsToWatchedHistoryRequestShowsInnerSeasonsInnerEpisodesInner}
     */
    AddItemsToWatchedHistoryRequestShowsInnerSeasonsInnerEpisodesInner,

    /**
     * The AddItemsToWatchlistRequest model constructor.
     * @property {module:model/AddItemsToWatchlistRequest}
     */
    AddItemsToWatchlistRequest,

    /**
     * The AddItemsToWatchlistRequestShowsInner model constructor.
     * @property {module:model/AddItemsToWatchlistRequestShowsInner}
     */
    AddItemsToWatchlistRequestShowsInner,

    /**
     * The AddNewRatingsRequest model constructor.
     * @property {module:model/AddNewRatingsRequest}
     */
    AddNewRatingsRequest,

    /**
     * The AddNewRatingsRequestEpisodesInner model constructor.
     * @property {module:model/AddNewRatingsRequestEpisodesInner}
     */
    AddNewRatingsRequestEpisodesInner,

    /**
     * The AddNewRatingsRequestMoviesInner model constructor.
     * @property {module:model/AddNewRatingsRequestMoviesInner}
     */
    AddNewRatingsRequestMoviesInner,

    /**
     * The AddNewRatingsRequestSeasonsInner model constructor.
     * @property {module:model/AddNewRatingsRequestSeasonsInner}
     */
    AddNewRatingsRequestSeasonsInner,

    /**
     * The AddNewRatingsRequestShowsInner model constructor.
     * @property {module:model/AddNewRatingsRequestShowsInner}
     */
    AddNewRatingsRequestShowsInner,

    /**
     * The AddNewRatingsRequestShowsInnerSeasonsInner model constructor.
     * @property {module:model/AddNewRatingsRequestShowsInnerSeasonsInner}
     */
    AddNewRatingsRequestShowsInnerSeasonsInner,

    /**
     * The AddNewRatingsRequestShowsInnerSeasonsInnerEpisodesInner model constructor.
     * @property {module:model/AddNewRatingsRequestShowsInnerSeasonsInnerEpisodesInner}
     */
    AddNewRatingsRequestShowsInnerSeasonsInnerEpisodesInner,

    /**
     * The CheckIntoAnItemRequest model constructor.
     * @property {module:model/CheckIntoAnItemRequest}
     */
    CheckIntoAnItemRequest,

    /**
     * The CheckIntoAnItemRequestMovie model constructor.
     * @property {module:model/CheckIntoAnItemRequestMovie}
     */
    CheckIntoAnItemRequestMovie,

    /**
     * The CheckIntoAnItemRequestMovieIds model constructor.
     * @property {module:model/CheckIntoAnItemRequestMovieIds}
     */
    CheckIntoAnItemRequestMovieIds,

    /**
     * The CheckIntoAnItemRequestSharing model constructor.
     * @property {module:model/CheckIntoAnItemRequestSharing}
     */
    CheckIntoAnItemRequestSharing,

    /**
     * The CreatePersonalListRequest model constructor.
     * @property {module:model/CreatePersonalListRequest}
     */
    CreatePersonalListRequest,

    /**
     * The ExchangeRefreshTokenForAccessTokenRequest model constructor.
     * @property {module:model/ExchangeRefreshTokenForAccessTokenRequest}
     */
    ExchangeRefreshTokenForAccessTokenRequest,

    /**
     * The GenerateNewDeviceCodesRequest model constructor.
     * @property {module:model/GenerateNewDeviceCodesRequest}
     */
    GenerateNewDeviceCodesRequest,

    /**
     * The PauseWatchingInAMediaCenterRequest model constructor.
     * @property {module:model/PauseWatchingInAMediaCenterRequest}
     */
    PauseWatchingInAMediaCenterRequest,

    /**
     * The PollForTheAccessTokenRequest model constructor.
     * @property {module:model/PollForTheAccessTokenRequest}
     */
    PollForTheAccessTokenRequest,

    /**
     * The PostACommentRequest model constructor.
     * @property {module:model/PostACommentRequest}
     */
    PostACommentRequest,

    /**
     * The PostACommentRequestSharing model constructor.
     * @property {module:model/PostACommentRequestSharing}
     */
    PostACommentRequestSharing,

    /**
     * The PostAReplyForACommentRequest model constructor.
     * @property {module:model/PostAReplyForACommentRequest}
     */
    PostAReplyForACommentRequest,

    /**
     * The RemoveItemsFromCollectionRequest model constructor.
     * @property {module:model/RemoveItemsFromCollectionRequest}
     */
    RemoveItemsFromCollectionRequest,

    /**
     * The RemoveItemsFromCollectionRequestMoviesInner model constructor.
     * @property {module:model/RemoveItemsFromCollectionRequestMoviesInner}
     */
    RemoveItemsFromCollectionRequestMoviesInner,

    /**
     * The RemoveItemsFromCollectionRequestShowsInner model constructor.
     * @property {module:model/RemoveItemsFromCollectionRequestShowsInner}
     */
    RemoveItemsFromCollectionRequestShowsInner,

    /**
     * The RemoveItemsFromCollectionRequestShowsInnerSeasonsInner model constructor.
     * @property {module:model/RemoveItemsFromCollectionRequestShowsInnerSeasonsInner}
     */
    RemoveItemsFromCollectionRequestShowsInnerSeasonsInner,

    /**
     * The RemoveItemsFromCollectionRequestShowsInnerSeasonsInnerEpisodesInner model constructor.
     * @property {module:model/RemoveItemsFromCollectionRequestShowsInnerSeasonsInnerEpisodesInner}
     */
    RemoveItemsFromCollectionRequestShowsInnerSeasonsInnerEpisodesInner,

    /**
     * The RemoveItemsFromHistoryRequest model constructor.
     * @property {module:model/RemoveItemsFromHistoryRequest}
     */
    RemoveItemsFromHistoryRequest,

    /**
     * The RemoveItemsFromPersonalListRequest model constructor.
     * @property {module:model/RemoveItemsFromPersonalListRequest}
     */
    RemoveItemsFromPersonalListRequest,

    /**
     * The RemoveItemsFromPersonalListRequestMoviesInner model constructor.
     * @property {module:model/RemoveItemsFromPersonalListRequestMoviesInner}
     */
    RemoveItemsFromPersonalListRequestMoviesInner,

    /**
     * The RemoveItemsFromPersonalListRequestShowsInner model constructor.
     * @property {module:model/RemoveItemsFromPersonalListRequestShowsInner}
     */
    RemoveItemsFromPersonalListRequestShowsInner,

    /**
     * The RemoveItemsFromPersonalRecommendationsRequest model constructor.
     * @property {module:model/RemoveItemsFromPersonalRecommendationsRequest}
     */
    RemoveItemsFromPersonalRecommendationsRequest,

    /**
     * The RemoveItemsFromPersonalRecommendationsRequestShowsInner model constructor.
     * @property {module:model/RemoveItemsFromPersonalRecommendationsRequestShowsInner}
     */
    RemoveItemsFromPersonalRecommendationsRequestShowsInner,

    /**
     * The ReorderAUserSListsRequest model constructor.
     * @property {module:model/ReorderAUserSListsRequest}
     */
    ReorderAUserSListsRequest,

    /**
     * The ReorderPersonallyRecommendedItemsRequest model constructor.
     * @property {module:model/ReorderPersonallyRecommendedItemsRequest}
     */
    ReorderPersonallyRecommendedItemsRequest,

    /**
     * The RevokeAnAccessTokenRequest model constructor.
     * @property {module:model/RevokeAnAccessTokenRequest}
     */
    RevokeAnAccessTokenRequest,

    /**
     * The StartWatchingInAMediaCenterRequest model constructor.
     * @property {module:model/StartWatchingInAMediaCenterRequest}
     */
    StartWatchingInAMediaCenterRequest,

    /**
     * The StopOrFinishWatchingInAMediaCenterRequest model constructor.
     * @property {module:model/StopOrFinishWatchingInAMediaCenterRequest}
     */
    StopOrFinishWatchingInAMediaCenterRequest,

    /**
     * The UpdateACommentOrReplyRequest model constructor.
     * @property {module:model/UpdateACommentOrReplyRequest}
     */
    UpdateACommentOrReplyRequest,

    /**
     * The UpdatePersonalListRequest model constructor.
     * @property {module:model/UpdatePersonalListRequest}
     */
    UpdatePersonalListRequest,

    /**
    * The AuthenticationDevicesApi service constructor.
    * @property {module:api/AuthenticationDevicesApi}
    */
    AuthenticationDevicesApi,

    /**
    * The AuthenticationOAuthApi service constructor.
    * @property {module:api/AuthenticationOAuthApi}
    */
    AuthenticationOAuthApi,

    /**
    * The CalendarsApi service constructor.
    * @property {module:api/CalendarsApi}
    */
    CalendarsApi,

    /**
    * The CertificationsApi service constructor.
    * @property {module:api/CertificationsApi}
    */
    CertificationsApi,

    /**
    * The CheckinApi service constructor.
    * @property {module:api/CheckinApi}
    */
    CheckinApi,

    /**
    * The CommentsApi service constructor.
    * @property {module:api/CommentsApi}
    */
    CommentsApi,

    /**
    * The CountriesApi service constructor.
    * @property {module:api/CountriesApi}
    */
    CountriesApi,

    /**
    * The EpisodesApi service constructor.
    * @property {module:api/EpisodesApi}
    */
    EpisodesApi,

    /**
    * The GenresApi service constructor.
    * @property {module:api/GenresApi}
    */
    GenresApi,

    /**
    * The LanguagesApi service constructor.
    * @property {module:api/LanguagesApi}
    */
    LanguagesApi,

    /**
    * The ListsApi service constructor.
    * @property {module:api/ListsApi}
    */
    ListsApi,

    /**
    * The MoviesApi service constructor.
    * @property {module:api/MoviesApi}
    */
    MoviesApi,

    /**
    * The NetworksApi service constructor.
    * @property {module:api/NetworksApi}
    */
    NetworksApi,

    /**
    * The PeopleApi service constructor.
    * @property {module:api/PeopleApi}
    */
    PeopleApi,

    /**
    * The RecommendationsApi service constructor.
    * @property {module:api/RecommendationsApi}
    */
    RecommendationsApi,

    /**
    * The ScrobbleApi service constructor.
    * @property {module:api/ScrobbleApi}
    */
    ScrobbleApi,

    /**
    * The SearchApi service constructor.
    * @property {module:api/SearchApi}
    */
    SearchApi,

    /**
    * The SeasonsApi service constructor.
    * @property {module:api/SeasonsApi}
    */
    SeasonsApi,

    /**
    * The ShowsApi service constructor.
    * @property {module:api/ShowsApi}
    */
    ShowsApi,

    /**
    * The SyncApi service constructor.
    * @property {module:api/SyncApi}
    */
    SyncApi,

    /**
    * The UsersApi service constructor.
    * @property {module:api/UsersApi}
    */
    UsersApi
};
