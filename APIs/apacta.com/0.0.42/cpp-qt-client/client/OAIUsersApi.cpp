/**
 * Apacta
 * API for a tool to craftsmen used to register working hours, material usage and quality assurance. # Endpoint The endpoint `https://app.apacta.com/api/v1` should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https). # Authentication URL query authentication with an API key is used, so appending `?api_key={api_key}` to the URL where `{api_key}` is found within Apacta settings is used for authentication # Pagination If the endpoint returns a `pagination` object it means the endpoint supports pagination - currently it's only possible to change pages with `?page={page_number}` but implementing custom page sizes are on the road map.   # Search/filter Is experimental but implemented in some cases - see the individual endpoints' docs for further explanation. # Ordering Is currently experimental, but on some endpoints it's implemented on URL querys so eg. to order Invoices by `invoice_number` appending `?sort=Invoices.invoice_number&direction=desc` would sort the list descending by the value of `invoice_number`. # Associations Is currently implemented on an experimental basis where you can append eg. `?include=Contacts,Projects`  to the `/api/v1/invoices/` endpoint to embed `Contact` and `Project` objects directly. # Project Files Currently project files can be retrieved from two endpoints. `/projects/{project_id}/files` handles files uploaded from wall posts or forms. `/projects/{project_id}/project_files` allows uploading and showing files, not belonging to specific form or wall post. # Errors/Exceptions ## 422 (Validation) Write something about how the `errors` object contains keys with the properties that failes validation like: ```   {       \"success\": false,       \"data\": {           \"code\": 422,           \"url\": \"/api/v1/contacts?api_key=5523be3b-30ef-425d-8203-04df7caaa93a\",           \"message\": \"A validation error occurred\",           \"errorCount\": 1,           \"errors\": {               \"contact_types\": [ ## Property name that failed validation                   \"Contacts must have at least one contact type\" ## Message with further explanation               ]           }       }   } ``` ## Code examples Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form ### Swift ``` ``` ### Java #### OkHttp ```   OkHttpClient client = new OkHttpClient();    Request request = new Request.Builder()     .url(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .get()     .addHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .addHeader(\"accept\", \"application/json\")     .build();    Response response = client.newCall(request).execute(); ``` #### Unirest ```   HttpResponse<String> response = Unirest.get(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .header(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .header(\"accept\", \"application/json\")     .asString(); ``` ### Javascript #### Native ```   var data = null;    var xhr = new XMLHttpRequest();    xhr.addEventListener(\"readystatechange\", function () {     if (this.readyState === 4) {       console.log(this.responseText);     }   });    xhr.open(\"GET\", \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   xhr.setRequestHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   xhr.setRequestHeader(\"accept\", \"application/json\");    xhr.send(data); ``` #### jQuery ```   var settings = {     \"async\": true,     \"crossDomain\": true,     \"url\": \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\",     \"method\": \"GET\",     \"headers\": {       \"x-auth-token\": \"{INSERT_YOUR_TOKEN}\",       \"accept\": \"application/json\",     }   }    $.ajax(settings).done(function (response) {     console.log(response);   }); ``` #### NodeJS (Request) ```   var request = require(\"request\");    var options = { method: 'GET',     url: 'https://app.apacta.com/api/v1/forms',     qs:      { extended: 'true',        sort: 'Forms.created',        direction: 'DESC',        include: 'Products,CreatedBy',        limit: '5' },     headers:      { accept: 'application/json',        'x-auth-token': '{INSERT_YOUR_TOKEN}' } };    request(options, function (error, response, body) {     if (error) throw new Error(error);      console.log(body);   });  ``` ### Python 3 ```   import http.client    conn = http.client.HTTPSConnection(\"app.apacta.com\")    payload = \"\"    headers = {       'x-auth-token': \"{INSERT_YOUR_TOKEN}\",       'accept': \"application/json\",       }    conn.request(\"GET\", \"/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\", payload, headers)    res = conn.getresponse()   data = res.read()    print(data.decode(\"utf-8\")) ``` ### C# #### RestSharp ```   var client = new RestClient(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   var request = new RestRequest(Method.GET);   request.AddHeader(\"accept\", \"application/json\");   request.AddHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   IRestResponse response = client.Execute(request); ``` ### Ruby ```   require 'uri'   require 'net/http'    url = URI(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")    http = Net::HTTP.new(url.host, url.port)   http.use_ssl = true   http.verify_mode = OpenSSL::SSL::VERIFY_NONE    request = Net::HTTP::Get.new(url)   request[\"x-auth-token\"] = '{INSERT_YOUR_TOKEN}'   request[\"accept\"] = 'application/json'    response = http.request(request)   puts response.read_body ``` ### PHP (HttpRequest) ```   <?php    $request = new HttpRequest();   $request->setUrl('https://app.apacta.com/api/v1/forms');   $request->setMethod(HTTP_METH_GET);    $request->setQueryData(array(     'extended' => 'true',     'sort' => 'Forms.created',     'direction' => 'DESC',     'include' => 'Products,CreatedBy',     'limit' => '5'   ));    $request->setHeaders(array(     'accept' => 'application/json',     'x-auth-token' => '{INSERT_YOUR_TOKEN}'   ));    try {     $response = $request->send();      echo $response->getBody();   } catch (HttpException $ex) {     echo $ex;   } ``` ### Shell (cURL) ```    $ curl --request GET --url 'https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5' --header 'accept: application/json' --header 'x-auth-token: {INSERT_YOUR_TOKEN}'  ```
 *
 * The version of the OpenAPI document: 0.0.42
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUsersApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIUsersApi::OAIUsersApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIUsersApi::~OAIUsersApi() {
}

void OAIUsersApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://app.apacta.com/api/v1"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("usersBulkActivate", defaultConf);
    _serverIndices.insert("usersBulkActivate", 0);
    _serverConfigs.insert("usersBulkDeactivate", defaultConf);
    _serverIndices.insert("usersBulkDeactivate", 0);
    _serverConfigs.insert("usersGet", defaultConf);
    _serverIndices.insert("usersGet", 0);
    _serverConfigs.insert("usersPost", defaultConf);
    _serverIndices.insert("usersPost", 0);
    _serverConfigs.insert("usersResendWelcomeSmsGet", defaultConf);
    _serverIndices.insert("usersResendWelcomeSmsGet", 0);
    _serverConfigs.insert("usersUserIdDelete", defaultConf);
    _serverIndices.insert("usersUserIdDelete", 0);
    _serverConfigs.insert("usersUserIdGet", defaultConf);
    _serverIndices.insert("usersUserIdGet", 0);
    _serverConfigs.insert("usersUserIdIntegrationSettingsGet", defaultConf);
    _serverIndices.insert("usersUserIdIntegrationSettingsGet", 0);
    _serverConfigs.insert("usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete", defaultConf);
    _serverIndices.insert("usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete", 0);
    _serverConfigs.insert("usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet", defaultConf);
    _serverIndices.insert("usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet", 0);
    _serverConfigs.insert("usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut", defaultConf);
    _serverIndices.insert("usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut", 0);
    _serverConfigs.insert("usersUserIdIntegrationSettingsPost", defaultConf);
    _serverIndices.insert("usersUserIdIntegrationSettingsPost", 0);
    _serverConfigs.insert("usersUserIdPut", defaultConf);
    _serverIndices.insert("usersUserIdPut", 0);
    _serverConfigs.insert("usersUserIdUploadImagePost", defaultConf);
    _serverIndices.insert("usersUserIdUploadImagePost", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIUsersApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIUsersApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIUsersApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIUsersApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIUsersApi::setUsername(const QString &username) {
    _username = username;
}

void OAIUsersApi::setPassword(const QString &password) {
    _password = password;
}


void OAIUsersApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIUsersApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIUsersApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIUsersApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIUsersApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIUsersApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIUsersApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIUsersApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIUsersApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIUsersApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIUsersApi::getParamStylePrefix(const QString &style) {
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

QString OAIUsersApi::getParamStyleSuffix(const QString &style) {
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

QString OAIUsersApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIUsersApi::usersBulkActivate(const ::OpenAPI::OptionalParam<OAIBulkActionRequestBody> &oai_bulk_action_request_body) {
    QString fullPath = QString(_serverConfigs["usersBulkActivate"][_serverIndices.value("usersBulkActivate")].URL()+"/users/bulkActivate");
    
    if (_apiKeys.contains("api_key")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("api_key=").append(_apiKeys.find("api_key").value());
    }
    
    if (_apiKeys.contains("X-Auth-Token")) {
        addHeaders("X-Auth-Token",_apiKeys.find("X-Auth-Token").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_bulk_action_request_body.hasValue()){

        
        QByteArray output = oai_bulk_action_request_body.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIUsersApi::usersBulkActivateCallback);
    connect(this, &OAIUsersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIUsersApi::usersBulkActivateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIEmptySuccessResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT usersBulkActivateSignal(output);
        Q_EMIT usersBulkActivateSignalFull(worker, output);
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

        Q_EMIT usersBulkActivateSignalE(output, error_type, error_str);
        Q_EMIT usersBulkActivateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT usersBulkActivateSignalError(output, error_type, error_str);
        Q_EMIT usersBulkActivateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIUsersApi::usersBulkDeactivate(const ::OpenAPI::OptionalParam<OAIBulkActionRequestBody> &oai_bulk_action_request_body) {
    QString fullPath = QString(_serverConfigs["usersBulkDeactivate"][_serverIndices.value("usersBulkDeactivate")].URL()+"/users/bulkDeactivate");
    
    if (_apiKeys.contains("api_key")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("api_key=").append(_apiKeys.find("api_key").value());
    }
    
    if (_apiKeys.contains("X-Auth-Token")) {
        addHeaders("X-Auth-Token",_apiKeys.find("X-Auth-Token").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_bulk_action_request_body.hasValue()){

        
        QByteArray output = oai_bulk_action_request_body.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIUsersApi::usersBulkDeactivateCallback);
    connect(this, &OAIUsersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIUsersApi::usersBulkDeactivateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIEmptySuccessResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT usersBulkDeactivateSignal(output);
        Q_EMIT usersBulkDeactivateSignalFull(worker, output);
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

        Q_EMIT usersBulkDeactivateSignalE(output, error_type, error_str);
        Q_EMIT usersBulkDeactivateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT usersBulkDeactivateSignalError(output, error_type, error_str);
        Q_EMIT usersBulkDeactivateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIUsersApi::usersGet(const ::OpenAPI::OptionalParam<QString> &first_name, const ::OpenAPI::OptionalParam<QString> &last_name, const ::OpenAPI::OptionalParam<QString> &email, const ::OpenAPI::OptionalParam<QString> &stock_location_id, const ::OpenAPI::OptionalParam<bool> &is_active) {
    QString fullPath = QString(_serverConfigs["usersGet"][_serverIndices.value("usersGet")].URL()+"/users");
    
    if (_apiKeys.contains("api_key")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("api_key=").append(_apiKeys.find("api_key").value());
    }
    
    if (_apiKeys.contains("X-Auth-Token")) {
        addHeaders("X-Auth-Token",_apiKeys.find("X-Auth-Token").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (first_name.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "first_name", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("first_name")).append(querySuffix).append(QUrl::toPercentEncoding(first_name.stringValue()));
    }
    if (last_name.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "last_name", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("last_name")).append(querySuffix).append(QUrl::toPercentEncoding(last_name.stringValue()));
    }
    if (email.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "email", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("email")).append(querySuffix).append(QUrl::toPercentEncoding(email.stringValue()));
    }
    if (stock_location_id.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "stock_location_id", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("stock_location_id")).append(querySuffix).append(QUrl::toPercentEncoding(stock_location_id.stringValue()));
    }
    if (is_active.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "is_active", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("is_active")).append(querySuffix).append(QUrl::toPercentEncoding(is_active.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIUsersApi::usersGetCallback);
    connect(this, &OAIUsersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIUsersApi::usersGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_projects__project_id__users__get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT usersGetSignal(output);
        Q_EMIT usersGetSignalFull(worker, output);
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

        Q_EMIT usersGetSignalE(output, error_type, error_str);
        Q_EMIT usersGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT usersGetSignalError(output, error_type, error_str);
        Q_EMIT usersGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIUsersApi::usersPost(const ::OpenAPI::OptionalParam<OAI_users_post_request> &oai_users_post_request) {
    QString fullPath = QString(_serverConfigs["usersPost"][_serverIndices.value("usersPost")].URL()+"/users");
    
    if (_apiKeys.contains("api_key")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("api_key=").append(_apiKeys.find("api_key").value());
    }
    
    if (_apiKeys.contains("X-Auth-Token")) {
        addHeaders("X-Auth-Token",_apiKeys.find("X-Auth-Token").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_users_post_request.hasValue()){

        
        QByteArray output = oai_users_post_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIUsersApi::usersPostCallback);
    connect(this, &OAIUsersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIUsersApi::usersPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_clocking_records_post_201_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT usersPostSignal(output);
        Q_EMIT usersPostSignalFull(worker, output);
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

        Q_EMIT usersPostSignalE(output, error_type, error_str);
        Q_EMIT usersPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT usersPostSignalError(output, error_type, error_str);
        Q_EMIT usersPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIUsersApi::usersResendWelcomeSmsGet() {
    QString fullPath = QString(_serverConfigs["usersResendWelcomeSmsGet"][_serverIndices.value("usersResendWelcomeSmsGet")].URL()+"/users/resendWelcomeSms");
    
    if (_apiKeys.contains("api_key")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("api_key=").append(_apiKeys.find("api_key").value());
    }
    
    if (_apiKeys.contains("X-Auth-Token")) {
        addHeaders("X-Auth-Token",_apiKeys.find("X-Auth-Token").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIUsersApi::usersResendWelcomeSmsGetCallback);
    connect(this, &OAIUsersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIUsersApi::usersResendWelcomeSmsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_users_resendWelcomeSms_get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT usersResendWelcomeSmsGetSignal(output);
        Q_EMIT usersResendWelcomeSmsGetSignalFull(worker, output);
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

        Q_EMIT usersResendWelcomeSmsGetSignalE(output, error_type, error_str);
        Q_EMIT usersResendWelcomeSmsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT usersResendWelcomeSmsGetSignalError(output, error_type, error_str);
        Q_EMIT usersResendWelcomeSmsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIUsersApi::usersUserIdDelete(const QString &user_id) {
    QString fullPath = QString(_serverConfigs["usersUserIdDelete"][_serverIndices.value("usersUserIdDelete")].URL()+"/users/{user_id}");
    
    if (_apiKeys.contains("api_key")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("api_key=").append(_apiKeys.find("api_key").value());
    }
    
    if (_apiKeys.contains("X-Auth-Token")) {
        addHeaders("X-Auth-Token",_apiKeys.find("X-Auth-Token").value());
    }
    
    
    {
        QString user_idPathParam("{");
        user_idPathParam.append("user_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "user_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"user_id"+pathSuffix : pathPrefix;
        fullPath.replace(user_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(user_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIUsersApi::usersUserIdDeleteCallback);
    connect(this, &OAIUsersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIUsersApi::usersUserIdDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_clocking_records__clocking_record_id__put_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT usersUserIdDeleteSignal(output);
        Q_EMIT usersUserIdDeleteSignalFull(worker, output);
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

        Q_EMIT usersUserIdDeleteSignalE(output, error_type, error_str);
        Q_EMIT usersUserIdDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT usersUserIdDeleteSignalError(output, error_type, error_str);
        Q_EMIT usersUserIdDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIUsersApi::usersUserIdGet(const QString &user_id) {
    QString fullPath = QString(_serverConfigs["usersUserIdGet"][_serverIndices.value("usersUserIdGet")].URL()+"/users/{user_id}");
    
    if (_apiKeys.contains("api_key")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("api_key=").append(_apiKeys.find("api_key").value());
    }
    
    if (_apiKeys.contains("X-Auth-Token")) {
        addHeaders("X-Auth-Token",_apiKeys.find("X-Auth-Token").value());
    }
    
    
    {
        QString user_idPathParam("{");
        user_idPathParam.append("user_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "user_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"user_id"+pathSuffix : pathPrefix;
        fullPath.replace(user_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(user_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIUsersApi::usersUserIdGetCallback);
    connect(this, &OAIUsersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIUsersApi::usersUserIdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_projects__project_id__users__user_id__get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT usersUserIdGetSignal(output);
        Q_EMIT usersUserIdGetSignalFull(worker, output);
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

        Q_EMIT usersUserIdGetSignalE(output, error_type, error_str);
        Q_EMIT usersUserIdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT usersUserIdGetSignalError(output, error_type, error_str);
        Q_EMIT usersUserIdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIUsersApi::usersUserIdIntegrationSettingsGet(const QString &user_id) {
    QString fullPath = QString(_serverConfigs["usersUserIdIntegrationSettingsGet"][_serverIndices.value("usersUserIdIntegrationSettingsGet")].URL()+"/users/{user_id}/integration_settings");
    
    if (_apiKeys.contains("api_key")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("api_key=").append(_apiKeys.find("api_key").value());
    }
    
    if (_apiKeys.contains("X-Auth-Token")) {
        addHeaders("X-Auth-Token",_apiKeys.find("X-Auth-Token").value());
    }
    
    
    {
        QString user_idPathParam("{");
        user_idPathParam.append("user_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "user_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"user_id"+pathSuffix : pathPrefix;
        fullPath.replace(user_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(user_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIUsersApi::usersUserIdIntegrationSettingsGetCallback);
    connect(this, &OAIUsersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIUsersApi::usersUserIdIntegrationSettingsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_users__user_id__integration_settings_get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT usersUserIdIntegrationSettingsGetSignal(output);
        Q_EMIT usersUserIdIntegrationSettingsGetSignalFull(worker, output);
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

        Q_EMIT usersUserIdIntegrationSettingsGetSignalE(output, error_type, error_str);
        Q_EMIT usersUserIdIntegrationSettingsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT usersUserIdIntegrationSettingsGetSignalError(output, error_type, error_str);
        Q_EMIT usersUserIdIntegrationSettingsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIUsersApi::usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete(const QString &user_id, const QString &integration_settings_user_id) {
    QString fullPath = QString(_serverConfigs["usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete"][_serverIndices.value("usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete")].URL()+"/users/{user_id}/integration_settings/{integration_settings_user_id}");
    
    if (_apiKeys.contains("api_key")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("api_key=").append(_apiKeys.find("api_key").value());
    }
    
    if (_apiKeys.contains("X-Auth-Token")) {
        addHeaders("X-Auth-Token",_apiKeys.find("X-Auth-Token").value());
    }
    
    
    {
        QString user_idPathParam("{");
        user_idPathParam.append("user_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "user_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"user_id"+pathSuffix : pathPrefix;
        fullPath.replace(user_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(user_id)));
    }
    
    {
        QString integration_settings_user_idPathParam("{");
        integration_settings_user_idPathParam.append("integration_settings_user_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "integration_settings_user_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"integration_settings_user_id"+pathSuffix : pathPrefix;
        fullPath.replace(integration_settings_user_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(integration_settings_user_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIUsersApi::usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteCallback);
    connect(this, &OAIUsersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIUsersApi::usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIEmptySuccessResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteSignal(output);
        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteSignalFull(worker, output);
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

        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteSignalE(output, error_type, error_str);
        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteSignalError(output, error_type, error_str);
        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIUsersApi::usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet(const QString &user_id, const QString &integration_settings_user_id) {
    QString fullPath = QString(_serverConfigs["usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet"][_serverIndices.value("usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet")].URL()+"/users/{user_id}/integration_settings/{integration_settings_user_id}");
    
    if (_apiKeys.contains("api_key")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("api_key=").append(_apiKeys.find("api_key").value());
    }
    
    if (_apiKeys.contains("X-Auth-Token")) {
        addHeaders("X-Auth-Token",_apiKeys.find("X-Auth-Token").value());
    }
    
    
    {
        QString user_idPathParam("{");
        user_idPathParam.append("user_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "user_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"user_id"+pathSuffix : pathPrefix;
        fullPath.replace(user_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(user_id)));
    }
    
    {
        QString integration_settings_user_idPathParam("{");
        integration_settings_user_idPathParam.append("integration_settings_user_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "integration_settings_user_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"integration_settings_user_id"+pathSuffix : pathPrefix;
        fullPath.replace(integration_settings_user_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(integration_settings_user_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIUsersApi::usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetCallback);
    connect(this, &OAIUsersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIUsersApi::usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_users__user_id__integration_settings__integration_settings_user_id__get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetSignal(output);
        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetSignalFull(worker, output);
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

        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetSignalE(output, error_type, error_str);
        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetSignalError(output, error_type, error_str);
        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIUsersApi::usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut(const QString &user_id, const QString &integration_settings_user_id) {
    QString fullPath = QString(_serverConfigs["usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut"][_serverIndices.value("usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut")].URL()+"/users/{user_id}/integration_settings/{integration_settings_user_id}");
    
    if (_apiKeys.contains("api_key")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("api_key=").append(_apiKeys.find("api_key").value());
    }
    
    if (_apiKeys.contains("X-Auth-Token")) {
        addHeaders("X-Auth-Token",_apiKeys.find("X-Auth-Token").value());
    }
    
    
    {
        QString user_idPathParam("{");
        user_idPathParam.append("user_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "user_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"user_id"+pathSuffix : pathPrefix;
        fullPath.replace(user_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(user_id)));
    }
    
    {
        QString integration_settings_user_idPathParam("{");
        integration_settings_user_idPathParam.append("integration_settings_user_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "integration_settings_user_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"integration_settings_user_id"+pathSuffix : pathPrefix;
        fullPath.replace(integration_settings_user_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(integration_settings_user_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIUsersApi::usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutCallback);
    connect(this, &OAIUsersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIUsersApi::usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIEmptySuccessResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutSignal(output);
        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutSignalFull(worker, output);
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

        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutSignalE(output, error_type, error_str);
        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutSignalError(output, error_type, error_str);
        Q_EMIT usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIUsersApi::usersUserIdIntegrationSettingsPost(const QString &user_id, const ::OpenAPI::OptionalParam<OAI_companies__company_id__integration_settings_post_request> &oai_companies__company_id__integration_settings_post_request) {
    QString fullPath = QString(_serverConfigs["usersUserIdIntegrationSettingsPost"][_serverIndices.value("usersUserIdIntegrationSettingsPost")].URL()+"/users/{user_id}/integration_settings");
    
    if (_apiKeys.contains("api_key")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("api_key=").append(_apiKeys.find("api_key").value());
    }
    
    if (_apiKeys.contains("X-Auth-Token")) {
        addHeaders("X-Auth-Token",_apiKeys.find("X-Auth-Token").value());
    }
    
    
    {
        QString user_idPathParam("{");
        user_idPathParam.append("user_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "user_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"user_id"+pathSuffix : pathPrefix;
        fullPath.replace(user_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(user_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_companies__company_id__integration_settings_post_request.hasValue()){

        
        QByteArray output = oai_companies__company_id__integration_settings_post_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIUsersApi::usersUserIdIntegrationSettingsPostCallback);
    connect(this, &OAIUsersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIUsersApi::usersUserIdIntegrationSettingsPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateSuccessResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT usersUserIdIntegrationSettingsPostSignal(output);
        Q_EMIT usersUserIdIntegrationSettingsPostSignalFull(worker, output);
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

        Q_EMIT usersUserIdIntegrationSettingsPostSignalE(output, error_type, error_str);
        Q_EMIT usersUserIdIntegrationSettingsPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT usersUserIdIntegrationSettingsPostSignalError(output, error_type, error_str);
        Q_EMIT usersUserIdIntegrationSettingsPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIUsersApi::usersUserIdPut(const QString &user_id) {
    QString fullPath = QString(_serverConfigs["usersUserIdPut"][_serverIndices.value("usersUserIdPut")].URL()+"/users/{user_id}");
    
    if (_apiKeys.contains("api_key")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("api_key=").append(_apiKeys.find("api_key").value());
    }
    
    if (_apiKeys.contains("X-Auth-Token")) {
        addHeaders("X-Auth-Token",_apiKeys.find("X-Auth-Token").value());
    }
    
    
    {
        QString user_idPathParam("{");
        user_idPathParam.append("user_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "user_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"user_id"+pathSuffix : pathPrefix;
        fullPath.replace(user_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(user_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIUsersApi::usersUserIdPutCallback);
    connect(this, &OAIUsersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIUsersApi::usersUserIdPutCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_clocking_records__clocking_record_id__put_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT usersUserIdPutSignal(output);
        Q_EMIT usersUserIdPutSignalFull(worker, output);
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

        Q_EMIT usersUserIdPutSignalE(output, error_type, error_str);
        Q_EMIT usersUserIdPutSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT usersUserIdPutSignalError(output, error_type, error_str);
        Q_EMIT usersUserIdPutSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIUsersApi::usersUserIdUploadImagePost(const QString &user_id, const ::OpenAPI::OptionalParam<OAIHttpFileElement> &image) {
    QString fullPath = QString(_serverConfigs["usersUserIdUploadImagePost"][_serverIndices.value("usersUserIdUploadImagePost")].URL()+"/users/{user_id}/uploadImage");
    
    if (_apiKeys.contains("api_key")) {
        if (fullPath.indexOf("?") > 0)
            fullPath.append("&");
        else
            fullPath.append("?");
        fullPath.append("api_key=").append(_apiKeys.find("api_key").value());
    }
    
    if (_apiKeys.contains("X-Auth-Token")) {
        addHeaders("X-Auth-Token",_apiKeys.find("X-Auth-Token").value());
    }
    
    
    {
        QString user_idPathParam("{");
        user_idPathParam.append("user_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "user_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"user_id"+pathSuffix : pathPrefix;
        fullPath.replace(user_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(user_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (image.hasValue())
    {
        input.add_file("image", image.value().local_filename, image.value().request_filename, image.value().mime_type);
    }

    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIUsersApi::usersUserIdUploadImagePostCallback);
    connect(this, &OAIUsersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIUsersApi::usersUserIdUploadImagePostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateSuccessResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT usersUserIdUploadImagePostSignal(output);
        Q_EMIT usersUserIdUploadImagePostSignalFull(worker, output);
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

        Q_EMIT usersUserIdUploadImagePostSignalE(output, error_type, error_str);
        Q_EMIT usersUserIdUploadImagePostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT usersUserIdUploadImagePostSignalError(output, error_type, error_str);
        Q_EMIT usersUserIdUploadImagePostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIUsersApi::tokenAvailable(){

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
