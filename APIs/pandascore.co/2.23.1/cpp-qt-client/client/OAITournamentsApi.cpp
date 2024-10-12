/**
 * PandaScore REST API for All Videogames
 *  # Introduction  Whether you're looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home).  The API works over the HTTPS protocol, and is accessed from the `api.pandascore.co` domain.  - The current endpoint is [https://api.pandascore.co](https://api.pandascore.co). - All data is sent and received as JSON by default. - Blank fields are included with `null` values instead of being omitted. - All timestamps are returned in ISO-8601 format  ### About this documentation  Clicking on a query parameter like `filter` or `search` will show you the available options: ![filter](/doc/images/query_param_details.jpg)  You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg)  ## Events hierarchy  The PandaScore API allows you to access data about eSports events by using a certain structure detailed below.  **Leagues**  Leagues are the top level events. They don't have a date and represent a regular competition. A League is composed of one or several series.   Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._   Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._  **Series**  A Serie represents an occurrence of a league event.   The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._   Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._  **Tournaments**  Tournaments groups all the matches of a serie under \"stages\" and \"groups\".   The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._   Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._  **Matches**  Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match).   Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._   Matches of the group A in the ESL One, Genting tournamnet are: _Lower Round 1, Quarterfinal, Upper Final, etc._    **Please note that some matches may be listed as \"TBD vs TBD\" if the matchup is not announced yet, for example the date of the Final match is known but the quarterfinal is still being played.**   ![Structure](/doc/images/structure.png)  ## Formats  &lt;!-- The API currently supports the JSON format by default, as well as the XML format. Add the desired extension to your request URL in order to get that format. --&gt; The API currently supports the JSON format by default.  Other formats may be added depending on user needs.  ## Pagination  The Pandascore API paginates all resources on the index method.  Requests that return multiple items will be paginated to 50 items by default. You can specify further pages with the `page[number]` parameter. You can also set a custom page size (up to 100) with the `page[size]` parameter.  The `Link` HTTP response header contains pagination data with `first`, `previous`, `next` and `last` raw page links when available, under the format  ``` Link: &lt;https://api.pandascore.co/{Resource}?page=X+1&gt;; rel=\"next\", &lt;https://api.pandascore.co/{Resource}?page=X-1&gt;; rel=\"prev\", &lt;https://api.pandascore.co/{Resource}?page=1&gt;; rel=\"first\", &lt;https://api.pandascore.co/{Resource}?page=X+n&gt;; rel=\"last\" ```  There is also:  * A `X-Page` header field, which contains the current page. * A `X-Per-Page` header field, which contains the current pagination length. * A `X-Total` header field, which contains the total count of items across all pages.  ## Filtering  The `filter` query parameter can be used to filter a collection by one or several fields for one or several values. The `filter` parameter takes the field to filter as a key, and the values to filter as the value. Multiples values must be comma-separated (`,`).  For example, the following is a request for all the champions with a name matching Twitch or Brand exactly, but only with 21 armor:  ``` GET /lol/champions?filter[name]=Brand,Twitch&amp;filter[armor]=21&amp;token=YOUR_ACCESS_TOKEN ```  ## Range  The `range` parameter is a hash that allows filtering fields by an interval. Only values between the given two comma-separated bounds will be returned. The bounds are inclusive.  For example, the following is a request for all the champions with `hp` within 500 and 1000:  ``` GET /lol/champions?range[hp]=500,1000&amp;token=YOUR_ACCESS_TOKEN ```  ## Search  The `search` parameter is a bit like the `filter` parameter, but it will return all results where the values **contain** the given parameter.  Note: this only works on strings. Searching with integer values is not supported and `filter` or `range` parameters may be better suited for your needs here.  For example, to get all the champions with a name containing `\"twi\"`:  ``` $ curl -sg -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' 'https://api.pandascore.co/lol/champions?search[name]=twi' | jq -S '.[].name' \"Twitch\" \"Twisted Fate\" ```  ## Sorting  All index endpoints support multiple sort fields with comma-separation (`,`); the fields are applied in the order specified.  The sort order for each field is ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, “-“), in which case it is descending.  For example, `GET /lol/champions?sort=attackdamage,-name&amp;token=YOUR_ACCESS_TOKEN` will return all the champions sorted by attack damage. Any champions with the same attack damage will then be sorted by their names in descending alphabetical order.  ## Rate limiting  Depending on your current plan, you will have a different rate limit. Your plan and your current request count [are available on your dashboard](https://pandascore.co/settings).  With the **free plan**, you have a limit of 1000 requests per hour, others plans have a limit of 4000 requests per hour. The number of remaining requests is available in the `X-Rate-Limit-Remaining` response header.  Your API key is included in all the examples on this page, so you can test any example right away. **Only you can see this value.**  # Authentication  The authentication on the Pandascore API works with access tokens.  All developers need to [create an account](https://pandascore.co/users/sign_in) before getting started, in order to get an access token. The access token should not be shared.  **Your token can be found and regenerated from [your dashboard](https://pandascore.co/settings).**  The access token can be passed in the URL with the `token` query string parameter, or in the `Authorization: Bearer` header field.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt; 
 *
 * The version of the OpenAPI document: 2.23.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITournamentsApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAITournamentsApi::OAITournamentsApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAITournamentsApi::~OAITournamentsApi() {
}

void OAITournamentsApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.pandascore.co/"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("getTournaments", defaultConf);
    _serverIndices.insert("getTournaments", 0);
    _serverConfigs.insert("getTournamentsPast", defaultConf);
    _serverIndices.insert("getTournamentsPast", 0);
    _serverConfigs.insert("getTournamentsRunning", defaultConf);
    _serverIndices.insert("getTournamentsRunning", 0);
    _serverConfigs.insert("getTournamentsTournamentIdOrSlug", defaultConf);
    _serverIndices.insert("getTournamentsTournamentIdOrSlug", 0);
    _serverConfigs.insert("getTournamentsTournamentIdOrSlugBrackets", defaultConf);
    _serverIndices.insert("getTournamentsTournamentIdOrSlugBrackets", 0);
    _serverConfigs.insert("getTournamentsTournamentIdOrSlugMatches", defaultConf);
    _serverIndices.insert("getTournamentsTournamentIdOrSlugMatches", 0);
    _serverConfigs.insert("getTournamentsTournamentIdOrSlugPlayers", defaultConf);
    _serverIndices.insert("getTournamentsTournamentIdOrSlugPlayers", 0);
    _serverConfigs.insert("getTournamentsTournamentIdOrSlugRosters", defaultConf);
    _serverIndices.insert("getTournamentsTournamentIdOrSlugRosters", 0);
    _serverConfigs.insert("getTournamentsTournamentIdOrSlugStandings", defaultConf);
    _serverIndices.insert("getTournamentsTournamentIdOrSlugStandings", 0);
    _serverConfigs.insert("getTournamentsTournamentIdOrSlugTeams", defaultConf);
    _serverIndices.insert("getTournamentsTournamentIdOrSlugTeams", 0);
    _serverConfigs.insert("getTournamentsUpcoming", defaultConf);
    _serverIndices.insert("getTournamentsUpcoming", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAITournamentsApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAITournamentsApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAITournamentsApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAITournamentsApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAITournamentsApi::setUsername(const QString &username) {
    _username = username;
}

void OAITournamentsApi::setPassword(const QString &password) {
    _password = password;
}


void OAITournamentsApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAITournamentsApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAITournamentsApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAITournamentsApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAITournamentsApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAITournamentsApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAITournamentsApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAITournamentsApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAITournamentsApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAITournamentsApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAITournamentsApi::getParamStylePrefix(const QString &style) {
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

QString OAITournamentsApi::getParamStyleSuffix(const QString &style) {
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

QString OAITournamentsApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAITournamentsApi::getTournaments(const ::OpenAPI::OptionalParam<OAIFilter_over_ShortTournaments> &filter, const ::OpenAPI::OptionalParam<OAISearch_over_ShortTournaments> &search, const ::OpenAPI::OptionalParam<QList<QString>> &sort, const ::OpenAPI::OptionalParam<OAIRange_over_ShortTournaments> &range, const ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter> &page, const ::OpenAPI::OptionalParam<qint32> &per_page) {
    QString fullPath = QString(_serverConfigs["getTournaments"][_serverIndices.value("getTournaments")].URL()+"/tournaments");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    if (_apiKeys.contains("QueryToken")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("QueryToken=").append(_apiKeys.find("QueryToken").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (filter.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "filter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "filter"+querySuffix : "";
        QJsonObject parameter = filter.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (search.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "search", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "search"+querySuffix : "";
        QJsonObject parameter = search.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (sort.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : sort.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("sort=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (range.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "range", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "range"+querySuffix : "";
        QJsonObject parameter = range.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "page"+querySuffix : "";
        QJsonObject parameter = page.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (per_page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "per_page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("per_page")).append(querySuffix).append(QUrl::toPercentEncoding(per_page.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITournamentsApi::getTournamentsCallback);
    connect(this, &OAITournamentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITournamentsApi::getTournamentsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIShortTournament> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIShortTournament val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTournamentsSignal(output);
        Q_EMIT getTournamentsSignalFull(worker, output);
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

        Q_EMIT getTournamentsSignalE(output, error_type, error_str);
        Q_EMIT getTournamentsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTournamentsSignalError(output, error_type, error_str);
        Q_EMIT getTournamentsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITournamentsApi::getTournamentsPast(const ::OpenAPI::OptionalParam<OAIFilter_over_ShortTournaments> &filter, const ::OpenAPI::OptionalParam<OAISearch_over_ShortTournaments> &search, const ::OpenAPI::OptionalParam<QList<QString>> &sort, const ::OpenAPI::OptionalParam<OAIRange_over_ShortTournaments> &range, const ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter> &page, const ::OpenAPI::OptionalParam<qint32> &per_page) {
    QString fullPath = QString(_serverConfigs["getTournamentsPast"][_serverIndices.value("getTournamentsPast")].URL()+"/tournaments/past");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    if (_apiKeys.contains("QueryToken")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("QueryToken=").append(_apiKeys.find("QueryToken").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (filter.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "filter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "filter"+querySuffix : "";
        QJsonObject parameter = filter.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (search.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "search", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "search"+querySuffix : "";
        QJsonObject parameter = search.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (sort.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : sort.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("sort=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (range.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "range", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "range"+querySuffix : "";
        QJsonObject parameter = range.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "page"+querySuffix : "";
        QJsonObject parameter = page.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (per_page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "per_page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("per_page")).append(querySuffix).append(QUrl::toPercentEncoding(per_page.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITournamentsApi::getTournamentsPastCallback);
    connect(this, &OAITournamentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITournamentsApi::getTournamentsPastCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIShortTournament> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIShortTournament val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTournamentsPastSignal(output);
        Q_EMIT getTournamentsPastSignalFull(worker, output);
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

        Q_EMIT getTournamentsPastSignalE(output, error_type, error_str);
        Q_EMIT getTournamentsPastSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTournamentsPastSignalError(output, error_type, error_str);
        Q_EMIT getTournamentsPastSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITournamentsApi::getTournamentsRunning(const ::OpenAPI::OptionalParam<OAIFilter_over_ShortTournaments> &filter, const ::OpenAPI::OptionalParam<OAISearch_over_ShortTournaments> &search, const ::OpenAPI::OptionalParam<QList<QString>> &sort, const ::OpenAPI::OptionalParam<OAIRange_over_ShortTournaments> &range, const ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter> &page, const ::OpenAPI::OptionalParam<qint32> &per_page) {
    QString fullPath = QString(_serverConfigs["getTournamentsRunning"][_serverIndices.value("getTournamentsRunning")].URL()+"/tournaments/running");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    if (_apiKeys.contains("QueryToken")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("QueryToken=").append(_apiKeys.find("QueryToken").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (filter.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "filter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "filter"+querySuffix : "";
        QJsonObject parameter = filter.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (search.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "search", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "search"+querySuffix : "";
        QJsonObject parameter = search.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (sort.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : sort.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("sort=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (range.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "range", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "range"+querySuffix : "";
        QJsonObject parameter = range.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "page"+querySuffix : "";
        QJsonObject parameter = page.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (per_page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "per_page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("per_page")).append(querySuffix).append(QUrl::toPercentEncoding(per_page.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITournamentsApi::getTournamentsRunningCallback);
    connect(this, &OAITournamentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITournamentsApi::getTournamentsRunningCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIShortTournament> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIShortTournament val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTournamentsRunningSignal(output);
        Q_EMIT getTournamentsRunningSignalFull(worker, output);
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

        Q_EMIT getTournamentsRunningSignalE(output, error_type, error_str);
        Q_EMIT getTournamentsRunningSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTournamentsRunningSignalError(output, error_type, error_str);
        Q_EMIT getTournamentsRunningSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITournamentsApi::getTournamentsTournamentIdOrSlug(const OAITournamentIDOrSlug &tournament_id_or_slug) {
    QString fullPath = QString(_serverConfigs["getTournamentsTournamentIdOrSlug"][_serverIndices.value("getTournamentsTournamentIdOrSlug")].URL()+"/tournaments/{tournament_id_or_slug}");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    if (_apiKeys.contains("QueryToken")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("QueryToken=").append(_apiKeys.find("QueryToken").value());
    }
    
    
    {
        QString tournament_id_or_slugPathParam("{");
        tournament_id_or_slugPathParam.append("tournament_id_or_slug").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "tournament_id_or_slug", false);
        QString paramString = (pathStyle == "matrix" && false) ? pathPrefix : pathPrefix+"tournament_id_or_slug"+pathSuffix;
        QJsonObject parameter = tournament_id_or_slug.asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                pathDelimiter = (pathStyle == "matrix" && false) ? ";" : getParamStyleDelimiter(pathStyle, key, false);
                paramString.append(pathDelimiter);
            }
            QString assignOperator = (false) ? "=" : ",";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(key+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(key+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.replace(tournament_id_or_slugPathParam, QUrl::toPercentEncoding(paramString));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITournamentsApi::getTournamentsTournamentIdOrSlugCallback);
    connect(this, &OAITournamentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITournamentsApi::getTournamentsTournamentIdOrSlugCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAITournament output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTournamentsTournamentIdOrSlugSignal(output);
        Q_EMIT getTournamentsTournamentIdOrSlugSignalFull(worker, output);
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

        Q_EMIT getTournamentsTournamentIdOrSlugSignalE(output, error_type, error_str);
        Q_EMIT getTournamentsTournamentIdOrSlugSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTournamentsTournamentIdOrSlugSignalError(output, error_type, error_str);
        Q_EMIT getTournamentsTournamentIdOrSlugSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITournamentsApi::getTournamentsTournamentIdOrSlugBrackets(const OAITournamentIDOrSlug &tournament_id_or_slug, const ::OpenAPI::OptionalParam<OAIFilter_over_Brackets> &filter, const ::OpenAPI::OptionalParam<OAIRange_over_Brackets> &range, const ::OpenAPI::OptionalParam<QList<QString>> &sort, const ::OpenAPI::OptionalParam<OAISearch_over_Brackets> &search, const ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter> &page, const ::OpenAPI::OptionalParam<qint32> &per_page) {
    QString fullPath = QString(_serverConfigs["getTournamentsTournamentIdOrSlugBrackets"][_serverIndices.value("getTournamentsTournamentIdOrSlugBrackets")].URL()+"/tournaments/{tournament_id_or_slug}/brackets");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    if (_apiKeys.contains("QueryToken")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("QueryToken=").append(_apiKeys.find("QueryToken").value());
    }
    
    
    {
        QString tournament_id_or_slugPathParam("{");
        tournament_id_or_slugPathParam.append("tournament_id_or_slug").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "tournament_id_or_slug", false);
        QString paramString = (pathStyle == "matrix" && false) ? pathPrefix : pathPrefix+"tournament_id_or_slug"+pathSuffix;
        QJsonObject parameter = tournament_id_or_slug.asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                pathDelimiter = (pathStyle == "matrix" && false) ? ";" : getParamStyleDelimiter(pathStyle, key, false);
                paramString.append(pathDelimiter);
            }
            QString assignOperator = (false) ? "=" : ",";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(key+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(key+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.replace(tournament_id_or_slugPathParam, QUrl::toPercentEncoding(paramString));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (filter.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "filter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "filter"+querySuffix : "";
        QJsonObject parameter = filter.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (range.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "range", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "range"+querySuffix : "";
        QJsonObject parameter = range.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (sort.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : sort.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("sort=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (search.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "search", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "search"+querySuffix : "";
        QJsonObject parameter = search.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "page"+querySuffix : "";
        QJsonObject parameter = page.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (per_page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "per_page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("per_page")).append(querySuffix).append(QUrl::toPercentEncoding(per_page.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITournamentsApi::getTournamentsTournamentIdOrSlugBracketsCallback);
    connect(this, &OAITournamentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITournamentsApi::getTournamentsTournamentIdOrSlugBracketsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIBracket> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIBracket val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTournamentsTournamentIdOrSlugBracketsSignal(output);
        Q_EMIT getTournamentsTournamentIdOrSlugBracketsSignalFull(worker, output);
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

        Q_EMIT getTournamentsTournamentIdOrSlugBracketsSignalE(output, error_type, error_str);
        Q_EMIT getTournamentsTournamentIdOrSlugBracketsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTournamentsTournamentIdOrSlugBracketsSignalError(output, error_type, error_str);
        Q_EMIT getTournamentsTournamentIdOrSlugBracketsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITournamentsApi::getTournamentsTournamentIdOrSlugMatches(const OAITournamentIDOrSlug &tournament_id_or_slug, const ::OpenAPI::OptionalParam<OAIFilter_over_Matches> &filter, const ::OpenAPI::OptionalParam<OAISearch_over_Matches> &search, const ::OpenAPI::OptionalParam<QList<QString>> &sort, const ::OpenAPI::OptionalParam<OAIRange_over_Matches> &range, const ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter> &page, const ::OpenAPI::OptionalParam<qint32> &per_page) {
    QString fullPath = QString(_serverConfigs["getTournamentsTournamentIdOrSlugMatches"][_serverIndices.value("getTournamentsTournamentIdOrSlugMatches")].URL()+"/tournaments/{tournament_id_or_slug}/matches");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    if (_apiKeys.contains("QueryToken")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("QueryToken=").append(_apiKeys.find("QueryToken").value());
    }
    
    
    {
        QString tournament_id_or_slugPathParam("{");
        tournament_id_or_slugPathParam.append("tournament_id_or_slug").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "tournament_id_or_slug", false);
        QString paramString = (pathStyle == "matrix" && false) ? pathPrefix : pathPrefix+"tournament_id_or_slug"+pathSuffix;
        QJsonObject parameter = tournament_id_or_slug.asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                pathDelimiter = (pathStyle == "matrix" && false) ? ";" : getParamStyleDelimiter(pathStyle, key, false);
                paramString.append(pathDelimiter);
            }
            QString assignOperator = (false) ? "=" : ",";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(key+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(key+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.replace(tournament_id_or_slugPathParam, QUrl::toPercentEncoding(paramString));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (filter.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "filter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "filter"+querySuffix : "";
        QJsonObject parameter = filter.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (search.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "search", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "search"+querySuffix : "";
        QJsonObject parameter = search.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (sort.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : sort.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("sort=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (range.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "range", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "range"+querySuffix : "";
        QJsonObject parameter = range.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "page"+querySuffix : "";
        QJsonObject parameter = page.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (per_page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "per_page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("per_page")).append(querySuffix).append(QUrl::toPercentEncoding(per_page.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITournamentsApi::getTournamentsTournamentIdOrSlugMatchesCallback);
    connect(this, &OAITournamentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITournamentsApi::getTournamentsTournamentIdOrSlugMatchesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIMatch> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIMatch val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTournamentsTournamentIdOrSlugMatchesSignal(output);
        Q_EMIT getTournamentsTournamentIdOrSlugMatchesSignalFull(worker, output);
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

        Q_EMIT getTournamentsTournamentIdOrSlugMatchesSignalE(output, error_type, error_str);
        Q_EMIT getTournamentsTournamentIdOrSlugMatchesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTournamentsTournamentIdOrSlugMatchesSignalError(output, error_type, error_str);
        Q_EMIT getTournamentsTournamentIdOrSlugMatchesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITournamentsApi::getTournamentsTournamentIdOrSlugPlayers(const QString &tournament_id_or_slug, const ::OpenAPI::OptionalParam<OAIFilter_over_Players> &filter, const ::OpenAPI::OptionalParam<OAISearch_over_Players> &search, const ::OpenAPI::OptionalParam<QList<QString>> &sort, const ::OpenAPI::OptionalParam<OAIRange_over_Players> &range, const ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter> &page, const ::OpenAPI::OptionalParam<qint32> &per_page) {
    QString fullPath = QString(_serverConfigs["getTournamentsTournamentIdOrSlugPlayers"][_serverIndices.value("getTournamentsTournamentIdOrSlugPlayers")].URL()+"/tournaments/{tournament_id_or_slug}/players");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    if (_apiKeys.contains("QueryToken")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("QueryToken=").append(_apiKeys.find("QueryToken").value());
    }
    
    
    {
        QString tournament_id_or_slugPathParam("{");
        tournament_id_or_slugPathParam.append("tournament_id_or_slug").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "tournament_id_or_slug", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"tournament_id_or_slug"+pathSuffix : pathPrefix;
        fullPath.replace(tournament_id_or_slugPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(tournament_id_or_slug)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (filter.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "filter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "filter"+querySuffix : "";
        QJsonObject parameter = filter.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (search.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "search", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "search"+querySuffix : "";
        QJsonObject parameter = search.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (sort.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : sort.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("sort=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (range.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "range", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "range"+querySuffix : "";
        QJsonObject parameter = range.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "page"+querySuffix : "";
        QJsonObject parameter = page.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (per_page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "per_page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("per_page")).append(querySuffix).append(QUrl::toPercentEncoding(per_page.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITournamentsApi::getTournamentsTournamentIdOrSlugPlayersCallback);
    connect(this, &OAITournamentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITournamentsApi::getTournamentsTournamentIdOrSlugPlayersCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIPlayer> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIPlayer val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTournamentsTournamentIdOrSlugPlayersSignal(output);
        Q_EMIT getTournamentsTournamentIdOrSlugPlayersSignalFull(worker, output);
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

        Q_EMIT getTournamentsTournamentIdOrSlugPlayersSignalE(output, error_type, error_str);
        Q_EMIT getTournamentsTournamentIdOrSlugPlayersSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTournamentsTournamentIdOrSlugPlayersSignalError(output, error_type, error_str);
        Q_EMIT getTournamentsTournamentIdOrSlugPlayersSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITournamentsApi::getTournamentsTournamentIdOrSlugRosters(const OAITournamentIDOrSlug &tournament_id_or_slug) {
    QString fullPath = QString(_serverConfigs["getTournamentsTournamentIdOrSlugRosters"][_serverIndices.value("getTournamentsTournamentIdOrSlugRosters")].URL()+"/tournaments/{tournament_id_or_slug}/rosters");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    if (_apiKeys.contains("QueryToken")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("QueryToken=").append(_apiKeys.find("QueryToken").value());
    }
    
    
    {
        QString tournament_id_or_slugPathParam("{");
        tournament_id_or_slugPathParam.append("tournament_id_or_slug").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "tournament_id_or_slug", false);
        QString paramString = (pathStyle == "matrix" && false) ? pathPrefix : pathPrefix+"tournament_id_or_slug"+pathSuffix;
        QJsonObject parameter = tournament_id_or_slug.asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                pathDelimiter = (pathStyle == "matrix" && false) ? ";" : getParamStyleDelimiter(pathStyle, key, false);
                paramString.append(pathDelimiter);
            }
            QString assignOperator = (false) ? "=" : ",";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(key+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(key+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.replace(tournament_id_or_slugPathParam, QUrl::toPercentEncoding(paramString));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITournamentsApi::getTournamentsTournamentIdOrSlugRostersCallback);
    connect(this, &OAITournamentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITournamentsApi::getTournamentsTournamentIdOrSlugRostersCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAITournamentRosters output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTournamentsTournamentIdOrSlugRostersSignal(output);
        Q_EMIT getTournamentsTournamentIdOrSlugRostersSignalFull(worker, output);
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

        Q_EMIT getTournamentsTournamentIdOrSlugRostersSignalE(output, error_type, error_str);
        Q_EMIT getTournamentsTournamentIdOrSlugRostersSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTournamentsTournamentIdOrSlugRostersSignalError(output, error_type, error_str);
        Q_EMIT getTournamentsTournamentIdOrSlugRostersSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITournamentsApi::getTournamentsTournamentIdOrSlugStandings(const OAITournamentIDOrSlug &tournament_id_or_slug, const ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter> &page, const ::OpenAPI::OptionalParam<qint32> &per_page) {
    QString fullPath = QString(_serverConfigs["getTournamentsTournamentIdOrSlugStandings"][_serverIndices.value("getTournamentsTournamentIdOrSlugStandings")].URL()+"/tournaments/{tournament_id_or_slug}/standings");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    if (_apiKeys.contains("QueryToken")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("QueryToken=").append(_apiKeys.find("QueryToken").value());
    }
    
    
    {
        QString tournament_id_or_slugPathParam("{");
        tournament_id_or_slugPathParam.append("tournament_id_or_slug").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "tournament_id_or_slug", false);
        QString paramString = (pathStyle == "matrix" && false) ? pathPrefix : pathPrefix+"tournament_id_or_slug"+pathSuffix;
        QJsonObject parameter = tournament_id_or_slug.asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                pathDelimiter = (pathStyle == "matrix" && false) ? ";" : getParamStyleDelimiter(pathStyle, key, false);
                paramString.append(pathDelimiter);
            }
            QString assignOperator = (false) ? "=" : ",";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(key+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(key+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.replace(tournament_id_or_slugPathParam, QUrl::toPercentEncoding(paramString));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "page"+querySuffix : "";
        QJsonObject parameter = page.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (per_page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "per_page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("per_page")).append(querySuffix).append(QUrl::toPercentEncoding(per_page.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITournamentsApi::getTournamentsTournamentIdOrSlugStandingsCallback);
    connect(this, &OAITournamentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITournamentsApi::getTournamentsTournamentIdOrSlugStandingsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIStanding> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIStanding val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTournamentsTournamentIdOrSlugStandingsSignal(output);
        Q_EMIT getTournamentsTournamentIdOrSlugStandingsSignalFull(worker, output);
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

        Q_EMIT getTournamentsTournamentIdOrSlugStandingsSignalE(output, error_type, error_str);
        Q_EMIT getTournamentsTournamentIdOrSlugStandingsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTournamentsTournamentIdOrSlugStandingsSignalError(output, error_type, error_str);
        Q_EMIT getTournamentsTournamentIdOrSlugStandingsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITournamentsApi::getTournamentsTournamentIdOrSlugTeams(const OAITournamentIDOrSlug &tournament_id_or_slug, const ::OpenAPI::OptionalParam<OAIFilter_over_Teams> &filter, const ::OpenAPI::OptionalParam<OAISearch_over_Teams> &search, const ::OpenAPI::OptionalParam<QList<QString>> &sort, const ::OpenAPI::OptionalParam<OAIRange_over_Teams> &range, const ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter> &page, const ::OpenAPI::OptionalParam<qint32> &per_page) {
    QString fullPath = QString(_serverConfigs["getTournamentsTournamentIdOrSlugTeams"][_serverIndices.value("getTournamentsTournamentIdOrSlugTeams")].URL()+"/tournaments/{tournament_id_or_slug}/teams");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    if (_apiKeys.contains("QueryToken")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("QueryToken=").append(_apiKeys.find("QueryToken").value());
    }
    
    
    {
        QString tournament_id_or_slugPathParam("{");
        tournament_id_or_slugPathParam.append("tournament_id_or_slug").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "tournament_id_or_slug", false);
        QString paramString = (pathStyle == "matrix" && false) ? pathPrefix : pathPrefix+"tournament_id_or_slug"+pathSuffix;
        QJsonObject parameter = tournament_id_or_slug.asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                pathDelimiter = (pathStyle == "matrix" && false) ? ";" : getParamStyleDelimiter(pathStyle, key, false);
                paramString.append(pathDelimiter);
            }
            QString assignOperator = (false) ? "=" : ",";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(key+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(key+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.replace(tournament_id_or_slugPathParam, QUrl::toPercentEncoding(paramString));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (filter.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "filter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "filter"+querySuffix : "";
        QJsonObject parameter = filter.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (search.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "search", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "search"+querySuffix : "";
        QJsonObject parameter = search.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (sort.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : sort.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("sort=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (range.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "range", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "range"+querySuffix : "";
        QJsonObject parameter = range.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "page"+querySuffix : "";
        QJsonObject parameter = page.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (per_page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "per_page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("per_page")).append(querySuffix).append(QUrl::toPercentEncoding(per_page.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITournamentsApi::getTournamentsTournamentIdOrSlugTeamsCallback);
    connect(this, &OAITournamentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITournamentsApi::getTournamentsTournamentIdOrSlugTeamsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAITeam> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAITeam val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTournamentsTournamentIdOrSlugTeamsSignal(output);
        Q_EMIT getTournamentsTournamentIdOrSlugTeamsSignalFull(worker, output);
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

        Q_EMIT getTournamentsTournamentIdOrSlugTeamsSignalE(output, error_type, error_str);
        Q_EMIT getTournamentsTournamentIdOrSlugTeamsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTournamentsTournamentIdOrSlugTeamsSignalError(output, error_type, error_str);
        Q_EMIT getTournamentsTournamentIdOrSlugTeamsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITournamentsApi::getTournamentsUpcoming(const ::OpenAPI::OptionalParam<OAIFilter_over_ShortTournaments> &filter, const ::OpenAPI::OptionalParam<OAISearch_over_ShortTournaments> &search, const ::OpenAPI::OptionalParam<QList<QString>> &sort, const ::OpenAPI::OptionalParam<OAIRange_over_ShortTournaments> &range, const ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter> &page, const ::OpenAPI::OptionalParam<qint32> &per_page) {
    QString fullPath = QString(_serverConfigs["getTournamentsUpcoming"][_serverIndices.value("getTournamentsUpcoming")].URL()+"/tournaments/upcoming");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    if (_apiKeys.contains("QueryToken")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("QueryToken=").append(_apiKeys.find("QueryToken").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (filter.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "filter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "filter"+querySuffix : "";
        QJsonObject parameter = filter.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("filter").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (search.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "search", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "search"+querySuffix : "";
        QJsonObject parameter = search.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("search").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (sort.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : sort.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("sort=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    if (range.hasValue())
    {
        queryStyle = "deepObject";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "range", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "range"+querySuffix : "";
        QJsonObject parameter = range.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("range").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");
        QString paramString = (queryStyle == "form" && true) ? "" : (queryStyle == "form" && !(true)) ? "page"+querySuffix : "";
        QJsonObject parameter = page.value().asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                queryDelimiter =  ((queryStyle == "form" || queryStyle == "deepObject") && true) ? "&" : getParamStyleDelimiter(queryStyle, key, true);
                paramString.append(queryDelimiter);
            }
            QString assignOperator;
            if (queryStyle == "form")
                assignOperator = (true) ? "=" : ",";
            else if (queryStyle == "deepObject")
                assignOperator = (true) ? "=" : "none";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(((queryStyle == "form") ? key : QString("page").append("[").append(key).append("]"))+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.append(paramString);
            }
    if (per_page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "per_page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("per_page")).append(querySuffix).append(QUrl::toPercentEncoding(per_page.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAITournamentsApi::getTournamentsUpcomingCallback);
    connect(this, &OAITournamentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAITournamentsApi::getTournamentsUpcomingCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIShortTournament> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIShortTournament val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getTournamentsUpcomingSignal(output);
        Q_EMIT getTournamentsUpcomingSignalFull(worker, output);
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

        Q_EMIT getTournamentsUpcomingSignalE(output, error_type, error_str);
        Q_EMIT getTournamentsUpcomingSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getTournamentsUpcomingSignalError(output, error_type, error_str);
        Q_EMIT getTournamentsUpcomingSignalErrorFull(worker, error_type, error_str);
    }
}

void OAITournamentsApi::tokenAvailable(){

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
