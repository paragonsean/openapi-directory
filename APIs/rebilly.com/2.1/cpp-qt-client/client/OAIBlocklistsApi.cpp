/**
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBlocklistsApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIBlocklistsApi::OAIBlocklistsApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIBlocklistsApi::~OAIBlocklistsApi() {
}

void OAIBlocklistsApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api-sandbox.rebilly.com"),
    "Sandbox Server.",
    QMap<QString, OAIServerVariable>()));
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.rebilly.com"),
    "Live Server.",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("deleteBlocklist", defaultConf);
    _serverIndices.insert("deleteBlocklist", 0);
    _serverConfigs.insert("getBlocklist", defaultConf);
    _serverIndices.insert("getBlocklist", 0);
    _serverConfigs.insert("getBlocklistCollection", defaultConf);
    _serverIndices.insert("getBlocklistCollection", 0);
    _serverConfigs.insert("postBlocklist", defaultConf);
    _serverIndices.insert("postBlocklist", 0);
    _serverConfigs.insert("putBlocklist", defaultConf);
    _serverIndices.insert("putBlocklist", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIBlocklistsApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIBlocklistsApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIBlocklistsApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIBlocklistsApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIBlocklistsApi::setUsername(const QString &username) {
    _username = username;
}

void OAIBlocklistsApi::setPassword(const QString &password) {
    _password = password;
}


void OAIBlocklistsApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIBlocklistsApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIBlocklistsApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIBlocklistsApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIBlocklistsApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIBlocklistsApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIBlocklistsApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIBlocklistsApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIBlocklistsApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIBlocklistsApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIBlocklistsApi::getParamStylePrefix(const QString &style) {
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

QString OAIBlocklistsApi::getParamStyleSuffix(const QString &style) {
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

QString OAIBlocklistsApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIBlocklistsApi::deleteBlocklist(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id) {
    QString fullPath = QString(_serverConfigs["deleteBlocklist"][_serverIndices.value("deleteBlocklist")].URL()+"/blocklists/{id}");
    
    if (_apiKeys.contains("SecretApiKey")) {
        addHeaders("SecretApiKey",_apiKeys.find("SecretApiKey").value());
    }
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
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
    OAIHttpRequestInput input(fullPath, "DELETE");


    if (organization_id.hasValue())
    {
        if (!::OpenAPI::toStringValue(organization_id.value()).isEmpty()) {
            input.headers.insert("Organization-Id", ::OpenAPI::toStringValue(organization_id.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIBlocklistsApi::deleteBlocklistCallback);
    connect(this, &OAIBlocklistsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIBlocklistsApi::deleteBlocklistCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteBlocklistSignal();
        Q_EMIT deleteBlocklistSignalFull(worker);
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

        Q_EMIT deleteBlocklistSignalE(error_type, error_str);
        Q_EMIT deleteBlocklistSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteBlocklistSignalError(error_type, error_str);
        Q_EMIT deleteBlocklistSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIBlocklistsApi::getBlocklist(const QString &id, const ::OpenAPI::OptionalParam<QString> &organization_id) {
    QString fullPath = QString(_serverConfigs["getBlocklist"][_serverIndices.value("getBlocklist")].URL()+"/blocklists/{id}");
    
    if (_apiKeys.contains("SecretApiKey")) {
        addHeaders("SecretApiKey",_apiKeys.find("SecretApiKey").value());
    }
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
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


    if (organization_id.hasValue())
    {
        if (!::OpenAPI::toStringValue(organization_id.value()).isEmpty()) {
            input.headers.insert("Organization-Id", ::OpenAPI::toStringValue(organization_id.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIBlocklistsApi::getBlocklistCallback);
    connect(this, &OAIBlocklistsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIBlocklistsApi::getBlocklistCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIBlocklist output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getBlocklistSignal(output);
        Q_EMIT getBlocklistSignalFull(worker, output);
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

        Q_EMIT getBlocklistSignalE(output, error_type, error_str);
        Q_EMIT getBlocklistSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getBlocklistSignalError(output, error_type, error_str);
        Q_EMIT getBlocklistSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIBlocklistsApi::getBlocklistCollection(const ::OpenAPI::OptionalParam<QString> &organization_id, const ::OpenAPI::OptionalParam<qint32> &limit, const ::OpenAPI::OptionalParam<qint32> &offset, const ::OpenAPI::OptionalParam<QList<QString>> &sort, const ::OpenAPI::OptionalParam<QString> &filter, const ::OpenAPI::OptionalParam<QString> &q) {
    QString fullPath = QString(_serverConfigs["getBlocklistCollection"][_serverIndices.value("getBlocklistCollection")].URL()+"/blocklists");
    
    if (_apiKeys.contains("SecretApiKey")) {
        addHeaders("SecretApiKey",_apiKeys.find("SecretApiKey").value());
    }
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (limit.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "limit", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("limit")).append(querySuffix).append(QUrl::toPercentEncoding(limit.stringValue()));
    }
    if (offset.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "offset", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("offset")).append(querySuffix).append(QUrl::toPercentEncoding(offset.stringValue()));
    }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", false);
        if (sort.value().size() > 0) {
            if (QString("csv").indexOf("multi") == 0) {
                for (QString t : sort.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("sort=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("csv").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("sort").append(querySuffix);
                qint32 count = 0;
                for (QString t : sort.value()) {
                    if (count > 0) {
                        fullPath.append((false)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("csv").indexOf("tsv") == 0) {
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
            } else if (QString("csv").indexOf("csv") == 0) {
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
            } else if (QString("csv").indexOf("pipes") == 0) {
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
            } else if (QString("csv").indexOf("deepObject") == 0) {
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
    if (filter.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "filter", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("filter")).append(querySuffix).append(QUrl::toPercentEncoding(filter.stringValue()));
    }
    if (q.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "q", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("q")).append(querySuffix).append(QUrl::toPercentEncoding(q.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (organization_id.hasValue())
    {
        if (!::OpenAPI::toStringValue(organization_id.value()).isEmpty()) {
            input.headers.insert("Organization-Id", ::OpenAPI::toStringValue(organization_id.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIBlocklistsApi::getBlocklistCollectionCallback);
    connect(this, &OAIBlocklistsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIBlocklistsApi::getBlocklistCollectionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIBlocklist> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIBlocklist val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getBlocklistCollectionSignal(output);
        Q_EMIT getBlocklistCollectionSignalFull(worker, output);
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

        Q_EMIT getBlocklistCollectionSignalE(output, error_type, error_str);
        Q_EMIT getBlocklistCollectionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getBlocklistCollectionSignalError(output, error_type, error_str);
        Q_EMIT getBlocklistCollectionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIBlocklistsApi::postBlocklist(const OAIBlocklist &oai_blocklist, const ::OpenAPI::OptionalParam<QString> &organization_id) {
    QString fullPath = QString(_serverConfigs["postBlocklist"][_serverIndices.value("postBlocklist")].URL()+"/blocklists");
    
    if (_apiKeys.contains("SecretApiKey")) {
        addHeaders("SecretApiKey",_apiKeys.find("SecretApiKey").value());
    }
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_blocklist.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (organization_id.hasValue())
    {
        if (!::OpenAPI::toStringValue(organization_id.value()).isEmpty()) {
            input.headers.insert("Organization-Id", ::OpenAPI::toStringValue(organization_id.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIBlocklistsApi::postBlocklistCallback);
    connect(this, &OAIBlocklistsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIBlocklistsApi::postBlocklistCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIBlocklist output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT postBlocklistSignal(output);
        Q_EMIT postBlocklistSignalFull(worker, output);
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

        Q_EMIT postBlocklistSignalE(output, error_type, error_str);
        Q_EMIT postBlocklistSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT postBlocklistSignalError(output, error_type, error_str);
        Q_EMIT postBlocklistSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIBlocklistsApi::putBlocklist(const QString &id, const OAIBlocklist &oai_blocklist, const ::OpenAPI::OptionalParam<QString> &organization_id) {
    QString fullPath = QString(_serverConfigs["putBlocklist"][_serverIndices.value("putBlocklist")].URL()+"/blocklists/{id}");
    
    if (_apiKeys.contains("SecretApiKey")) {
        addHeaders("SecretApiKey",_apiKeys.find("SecretApiKey").value());
    }
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
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
    OAIHttpRequestInput input(fullPath, "PUT");

    {

        
        QByteArray output = oai_blocklist.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (organization_id.hasValue())
    {
        if (!::OpenAPI::toStringValue(organization_id.value()).isEmpty()) {
            input.headers.insert("Organization-Id", ::OpenAPI::toStringValue(organization_id.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIBlocklistsApi::putBlocklistCallback);
    connect(this, &OAIBlocklistsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIBlocklistsApi::putBlocklistCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIBlocklist output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT putBlocklistSignal(output);
        Q_EMIT putBlocklistSignalFull(worker, output);
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

        Q_EMIT putBlocklistSignalE(output, error_type, error_str);
        Q_EMIT putBlocklistSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT putBlocklistSignalError(output, error_type, error_str);
        Q_EMIT putBlocklistSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIBlocklistsApi::tokenAvailable(){

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
