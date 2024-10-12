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

#include "OAICompaniesApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAICompaniesApi::OAICompaniesApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAICompaniesApi::~OAICompaniesApi() {
}

void OAICompaniesApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://app.apacta.com/api/v1"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet", defaultConf);
    _serverIndices.insert("companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet", 0);
    _serverConfigs.insert("companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut", defaultConf);
    _serverIndices.insert("companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut", 0);
    _serverConfigs.insert("companiesCompanyIdCompaniesIntegrationFeatureSettingsGet", defaultConf);
    _serverIndices.insert("companiesCompanyIdCompaniesIntegrationFeatureSettingsGet", 0);
    _serverConfigs.insert("companiesCompanyIdCompaniesIntegrationFeatureSettingsPost", defaultConf);
    _serverIndices.insert("companiesCompanyIdCompaniesIntegrationFeatureSettingsPost", 0);
    _serverConfigs.insert("companiesCompanyIdFormTemplatesFormTemplateIdDelete", defaultConf);
    _serverIndices.insert("companiesCompanyIdFormTemplatesFormTemplateIdDelete", 0);
    _serverConfigs.insert("companiesCompanyIdFormTemplatesFormTemplateIdGet", defaultConf);
    _serverIndices.insert("companiesCompanyIdFormTemplatesFormTemplateIdGet", 0);
    _serverConfigs.insert("companiesCompanyIdFormTemplatesGet", defaultConf);
    _serverIndices.insert("companiesCompanyIdFormTemplatesGet", 0);
    _serverConfigs.insert("companiesCompanyIdGet", defaultConf);
    _serverIndices.insert("companiesCompanyIdGet", 0);
    _serverConfigs.insert("companiesCompanyIdIntegrationFeatureSettingsGet", defaultConf);
    _serverIndices.insert("companiesCompanyIdIntegrationFeatureSettingsGet", 0);
    _serverConfigs.insert("companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet", defaultConf);
    _serverIndices.insert("companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet", 0);
    _serverConfigs.insert("companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete", defaultConf);
    _serverIndices.insert("companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete", 0);
    _serverConfigs.insert("companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet", defaultConf);
    _serverIndices.insert("companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet", 0);
    _serverConfigs.insert("companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut", defaultConf);
    _serverIndices.insert("companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut", 0);
    _serverConfigs.insert("companiesCompanyIdIntegrationSettingsGet", defaultConf);
    _serverIndices.insert("companiesCompanyIdIntegrationSettingsGet", 0);
    _serverConfigs.insert("companiesCompanyIdIntegrationSettingsPost", defaultConf);
    _serverIndices.insert("companiesCompanyIdIntegrationSettingsPost", 0);
    _serverConfigs.insert("companiesCompanyIdPriceMarginsPriceMarginsIdDelete", defaultConf);
    _serverIndices.insert("companiesCompanyIdPriceMarginsPriceMarginsIdDelete", 0);
    _serverConfigs.insert("companiesCompanyIdPriceMarginsPriceMarginsIdGet", defaultConf);
    _serverIndices.insert("companiesCompanyIdPriceMarginsPriceMarginsIdGet", 0);
    _serverConfigs.insert("companiesCompanyIdPriceMarginsPriceMarginsIdPost", defaultConf);
    _serverIndices.insert("companiesCompanyIdPriceMarginsPriceMarginsIdPost", 0);
    _serverConfigs.insert("companiesGet", defaultConf);
    _serverIndices.insert("companiesGet", 0);
    _serverConfigs.insert("companiesSubscriptionSelfServiceGet", defaultConf);
    _serverIndices.insert("companiesSubscriptionSelfServiceGet", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAICompaniesApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAICompaniesApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAICompaniesApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAICompaniesApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAICompaniesApi::setUsername(const QString &username) {
    _username = username;
}

void OAICompaniesApi::setPassword(const QString &password) {
    _password = password;
}


void OAICompaniesApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAICompaniesApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAICompaniesApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAICompaniesApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAICompaniesApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAICompaniesApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAICompaniesApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAICompaniesApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAICompaniesApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAICompaniesApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAICompaniesApi::getParamStylePrefix(const QString &style) {
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

QString OAICompaniesApi::getParamStyleSuffix(const QString &style) {
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

QString OAICompaniesApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAICompaniesApi::companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet(const QString &company_id, const QString &c_integration_feature_setting_id) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet"][_serverIndices.value("companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet")].URL()+"/companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id}");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    
    {
        QString c_integration_feature_setting_idPathParam("{");
        c_integration_feature_setting_idPathParam.append("c_integration_feature_setting_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "c_integration_feature_setting_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"c_integration_feature_setting_id"+pathSuffix : pathPrefix;
        fullPath.replace(c_integration_feature_setting_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(c_integration_feature_setting_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_companies__company_id__companies_integration_feature_settings_get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetSignal(output);
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut(const QString &company_id, const QString &c_integration_feature_setting_id) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut"][_serverIndices.value("companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut")].URL()+"/companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id}");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    
    {
        QString c_integration_feature_setting_idPathParam("{");
        c_integration_feature_setting_idPathParam.append("c_integration_feature_setting_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "c_integration_feature_setting_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"c_integration_feature_setting_id"+pathSuffix : pathPrefix;
        fullPath.replace(c_integration_feature_setting_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(c_integration_feature_setting_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_companies__company_id__companies_integration_feature_settings_get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutSignal(output);
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdCompaniesIntegrationFeatureSettingsGet(const QString &company_id) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdCompaniesIntegrationFeatureSettingsGet"][_serverIndices.value("companiesCompanyIdCompaniesIntegrationFeatureSettingsGet")].URL()+"/companies/{company_id}/companies_integration_feature_settings");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdCompaniesIntegrationFeatureSettingsGetCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdCompaniesIntegrationFeatureSettingsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_companies__company_id__companies_integration_feature_settings_get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsGetSignal(output);
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsGetSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsGetSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsGetSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdCompaniesIntegrationFeatureSettingsPost(const QString &company_id, const ::OpenAPI::OptionalParam<OAI_companies__company_id__companies_integration_feature_settings_post_request> &oai_companies__company_id__companies_integration_feature_settings_post_request) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdCompaniesIntegrationFeatureSettingsPost"][_serverIndices.value("companiesCompanyIdCompaniesIntegrationFeatureSettingsPost")].URL()+"/companies/{company_id}/companies_integration_feature_settings");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_companies__company_id__companies_integration_feature_settings_post_request.hasValue()){

        
        QByteArray output = oai_companies__company_id__companies_integration_feature_settings_post_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdCompaniesIntegrationFeatureSettingsPostCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdCompaniesIntegrationFeatureSettingsPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateSuccessResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsPostSignal(output);
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsPostSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsPostSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsPostSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdCompaniesIntegrationFeatureSettingsPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdFormTemplatesFormTemplateIdDelete(const QString &company_id, const QString &form_template_id) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdFormTemplatesFormTemplateIdDelete"][_serverIndices.value("companiesCompanyIdFormTemplatesFormTemplateIdDelete")].URL()+"/companies/{company_id}/form_templates/{form_template_id}");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    
    {
        QString form_template_idPathParam("{");
        form_template_idPathParam.append("form_template_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "form_template_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"form_template_id"+pathSuffix : pathPrefix;
        fullPath.replace(form_template_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(form_template_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdFormTemplatesFormTemplateIdDeleteCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdFormTemplatesFormTemplateIdDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIEmptySuccessResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdFormTemplatesFormTemplateIdDeleteSignal(output);
        Q_EMIT companiesCompanyIdFormTemplatesFormTemplateIdDeleteSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdFormTemplatesFormTemplateIdDeleteSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdFormTemplatesFormTemplateIdDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdFormTemplatesFormTemplateIdDeleteSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdFormTemplatesFormTemplateIdDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdFormTemplatesFormTemplateIdGet(const QString &company_id, const QString &id, const QString &form_template_id) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdFormTemplatesFormTemplateIdGet"][_serverIndices.value("companiesCompanyIdFormTemplatesFormTemplateIdGet")].URL()+"/companies/{company_id}/form_templates/{form_template_id}");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    
    {
        QString form_template_idPathParam("{");
        form_template_idPathParam.append("form_template_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "form_template_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"form_template_id"+pathSuffix : pathPrefix;
        fullPath.replace(form_template_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(form_template_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "id", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("id")).append(querySuffix).append(QUrl::toPercentEncoding(id));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdFormTemplatesFormTemplateIdGetCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdFormTemplatesFormTemplateIdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_companies__company_id__form_templates__get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdFormTemplatesFormTemplateIdGetSignal(output);
        Q_EMIT companiesCompanyIdFormTemplatesFormTemplateIdGetSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdFormTemplatesFormTemplateIdGetSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdFormTemplatesFormTemplateIdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdFormTemplatesFormTemplateIdGetSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdFormTemplatesFormTemplateIdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdFormTemplatesGet(const QString &company_id, const QString &form_template_id) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdFormTemplatesGet"][_serverIndices.value("companiesCompanyIdFormTemplatesGet")].URL()+"/companies/{company_id}/form_templates/");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "form_template_id", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("form_template_id")).append(querySuffix).append(QUrl::toPercentEncoding(form_template_id));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdFormTemplatesGetCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdFormTemplatesGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_companies__company_id__form_templates__get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdFormTemplatesGetSignal(output);
        Q_EMIT companiesCompanyIdFormTemplatesGetSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdFormTemplatesGetSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdFormTemplatesGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdFormTemplatesGetSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdFormTemplatesGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdGet(const QString &company_id) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdGet"][_serverIndices.value("companiesCompanyIdGet")].URL()+"/companies/{company_id}");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdGetCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_companies__company_id__get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdGetSignal(output);
        Q_EMIT companiesCompanyIdGetSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdGetSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdGetSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdIntegrationFeatureSettingsGet(const QString &company_id) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdIntegrationFeatureSettingsGet"][_serverIndices.value("companiesCompanyIdIntegrationFeatureSettingsGet")].URL()+"/companies/{company_id}/integration_feature_settings");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdIntegrationFeatureSettingsGetCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdIntegrationFeatureSettingsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_companies__company_id__integration_feature_settings_get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdIntegrationFeatureSettingsGetSignal(output);
        Q_EMIT companiesCompanyIdIntegrationFeatureSettingsGetSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdIntegrationFeatureSettingsGetSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdIntegrationFeatureSettingsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdIntegrationFeatureSettingsGetSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdIntegrationFeatureSettingsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet(const QString &company_id, const QString &integration_feature_setting_id) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet"][_serverIndices.value("companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet")].URL()+"/companies/{company_id}/integration_feature_settings/{integration_feature_setting_id}");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    
    {
        QString integration_feature_setting_idPathParam("{");
        integration_feature_setting_idPathParam.append("integration_feature_setting_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "integration_feature_setting_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"integration_feature_setting_id"+pathSuffix : pathPrefix;
        fullPath.replace(integration_feature_setting_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(integration_feature_setting_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_companies__company_id__integration_feature_settings__integration_feature_setting_id__get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetSignal(output);
        Q_EMIT companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete(const QString &company_id, const QString &companies_integration_setting_id) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete"][_serverIndices.value("companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete")].URL()+"/companies/{company_id}/integration_settings/{companies_integration_setting_id}");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    
    {
        QString companies_integration_setting_idPathParam("{");
        companies_integration_setting_idPathParam.append("companies_integration_setting_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "companies_integration_setting_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"companies_integration_setting_id"+pathSuffix : pathPrefix;
        fullPath.replace(companies_integration_setting_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(companies_integration_setting_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIEmptySuccessResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteSignal(output);
        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet(const QString &company_id, const QString &companies_integration_setting_id) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet"][_serverIndices.value("companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet")].URL()+"/companies/{company_id}/integration_settings/{companies_integration_setting_id}");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    
    {
        QString companies_integration_setting_idPathParam("{");
        companies_integration_setting_idPathParam.append("companies_integration_setting_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "companies_integration_setting_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"companies_integration_setting_id"+pathSuffix : pathPrefix;
        fullPath.replace(companies_integration_setting_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(companies_integration_setting_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_companies__company_id__integration_settings__companies_integration_setting_id__get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetSignal(output);
        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut(const QString &company_id, const QString &companies_integration_setting_id) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut"][_serverIndices.value("companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut")].URL()+"/companies/{company_id}/integration_settings/{companies_integration_setting_id}");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    
    {
        QString companies_integration_setting_idPathParam("{");
        companies_integration_setting_idPathParam.append("companies_integration_setting_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "companies_integration_setting_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"companies_integration_setting_id"+pathSuffix : pathPrefix;
        fullPath.replace(companies_integration_setting_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(companies_integration_setting_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIEmptySuccessResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutSignal(output);
        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdIntegrationSettingsGet(const QString &company_id, const ::OpenAPI::OptionalParam<QString> &identifier) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdIntegrationSettingsGet"][_serverIndices.value("companiesCompanyIdIntegrationSettingsGet")].URL()+"/companies/{company_id}/integration_settings");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (identifier.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "identifier", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("identifier")).append(querySuffix).append(QUrl::toPercentEncoding(identifier.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdIntegrationSettingsGetCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdIntegrationSettingsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_companies__company_id__integration_settings_get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdIntegrationSettingsGetSignal(output);
        Q_EMIT companiesCompanyIdIntegrationSettingsGetSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdIntegrationSettingsGetSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdIntegrationSettingsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdIntegrationSettingsGetSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdIntegrationSettingsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdIntegrationSettingsPost(const QString &company_id, const ::OpenAPI::OptionalParam<OAI_companies__company_id__integration_settings_post_request> &oai_companies__company_id__integration_settings_post_request) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdIntegrationSettingsPost"][_serverIndices.value("companiesCompanyIdIntegrationSettingsPost")].URL()+"/companies/{company_id}/integration_settings");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdIntegrationSettingsPostCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdIntegrationSettingsPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateSuccessResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdIntegrationSettingsPostSignal(output);
        Q_EMIT companiesCompanyIdIntegrationSettingsPostSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdIntegrationSettingsPostSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdIntegrationSettingsPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdIntegrationSettingsPostSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdIntegrationSettingsPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdPriceMarginsPriceMarginsIdDelete(const QString &company_id, const QString &price_margin_id, const QString &price_margins_id) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdPriceMarginsPriceMarginsIdDelete"][_serverIndices.value("companiesCompanyIdPriceMarginsPriceMarginsIdDelete")].URL()+"/companies/{company_id}/price_margins/{price_margins_id}");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    
    {
        QString price_margins_idPathParam("{");
        price_margins_idPathParam.append("price_margins_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "price_margins_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"price_margins_id"+pathSuffix : pathPrefix;
        fullPath.replace(price_margins_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(price_margins_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "price_margin_id", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("price_margin_id")).append(querySuffix).append(QUrl::toPercentEncoding(price_margin_id));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdPriceMarginsPriceMarginsIdDeleteCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdPriceMarginsPriceMarginsIdDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIEmptySuccessResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdDeleteSignal(output);
        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdDeleteSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdDeleteSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdDeleteSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdPriceMarginsPriceMarginsIdGet(const QString &company_id, const QString &price_margins_id) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdPriceMarginsPriceMarginsIdGet"][_serverIndices.value("companiesCompanyIdPriceMarginsPriceMarginsIdGet")].URL()+"/companies/{company_id}/price_margins/{price_margins_id}");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    
    {
        QString price_margins_idPathParam("{");
        price_margins_idPathParam.append("price_margins_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "price_margins_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"price_margins_id"+pathSuffix : pathPrefix;
        fullPath.replace(price_margins_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(price_margins_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdPriceMarginsPriceMarginsIdGetCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdPriceMarginsPriceMarginsIdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_companies__company_id__price_margins__price_margins_id__get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdGetSignal(output);
        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdGetSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdGetSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdGetSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesCompanyIdPriceMarginsPriceMarginsIdPost(const QString &company_id, const QString &price_margins_id, const ::OpenAPI::OptionalParam<OAI_companies__company_id__price_margins__price_margins_id__post_request> &oai_companies__company_id__price_margins__price_margins_id__post_request) {
    QString fullPath = QString(_serverConfigs["companiesCompanyIdPriceMarginsPriceMarginsIdPost"][_serverIndices.value("companiesCompanyIdPriceMarginsPriceMarginsIdPost")].URL()+"/companies/{company_id}/price_margins/{price_margins_id}");
    
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
        QString company_idPathParam("{");
        company_idPathParam.append("company_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "company_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"company_id"+pathSuffix : pathPrefix;
        fullPath.replace(company_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(company_id)));
    }
    
    {
        QString price_margins_idPathParam("{");
        price_margins_idPathParam.append("price_margins_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "price_margins_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"price_margins_id"+pathSuffix : pathPrefix;
        fullPath.replace(price_margins_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(price_margins_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_companies__company_id__price_margins__price_margins_id__post_request.hasValue()){

        
        QByteArray output = oai_companies__company_id__price_margins__price_margins_id__post_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesCompanyIdPriceMarginsPriceMarginsIdPostCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesCompanyIdPriceMarginsPriceMarginsIdPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateSuccessResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdPostSignal(output);
        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdPostSignalFull(worker, output);
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

        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdPostSignalE(output, error_type, error_str);
        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdPostSignalError(output, error_type, error_str);
        Q_EMIT companiesCompanyIdPriceMarginsPriceMarginsIdPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesGet() {
    QString fullPath = QString(_serverConfigs["companiesGet"][_serverIndices.value("companiesGet")].URL()+"/companies");
    
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesGetCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_companies_get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesGetSignal(output);
        Q_EMIT companiesGetSignalFull(worker, output);
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

        Q_EMIT companiesGetSignalE(output, error_type, error_str);
        Q_EMIT companiesGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesGetSignalError(output, error_type, error_str);
        Q_EMIT companiesGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::companiesSubscriptionSelfServiceGet() {
    QString fullPath = QString(_serverConfigs["companiesSubscriptionSelfServiceGet"][_serverIndices.value("companiesSubscriptionSelfServiceGet")].URL()+"/companies/subscription_self_service");
    
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICompaniesApi::companiesSubscriptionSelfServiceGetCallback);
    connect(this, &OAICompaniesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICompaniesApi::companiesSubscriptionSelfServiceGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_companies_subscription_self_service_get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT companiesSubscriptionSelfServiceGetSignal(output);
        Q_EMIT companiesSubscriptionSelfServiceGetSignalFull(worker, output);
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

        Q_EMIT companiesSubscriptionSelfServiceGetSignalE(output, error_type, error_str);
        Q_EMIT companiesSubscriptionSelfServiceGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT companiesSubscriptionSelfServiceGetSignalError(output, error_type, error_str);
        Q_EMIT companiesSubscriptionSelfServiceGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICompaniesApi::tokenAvailable(){

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
