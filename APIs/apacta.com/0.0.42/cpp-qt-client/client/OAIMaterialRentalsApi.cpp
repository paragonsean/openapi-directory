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

#include "OAIMaterialRentalsApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIMaterialRentalsApi::OAIMaterialRentalsApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIMaterialRentalsApi::~OAIMaterialRentalsApi() {
}

void OAIMaterialRentalsApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://app.apacta.com/api/v1"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("materialsMaterialIdRentalsCheckoutPost", defaultConf);
    _serverIndices.insert("materialsMaterialIdRentalsCheckoutPost", 0);
    _serverConfigs.insert("materialsMaterialIdRentalsGet", defaultConf);
    _serverIndices.insert("materialsMaterialIdRentalsGet", 0);
    _serverConfigs.insert("materialsMaterialIdRentalsMaterialRentalIdDelete", defaultConf);
    _serverIndices.insert("materialsMaterialIdRentalsMaterialRentalIdDelete", 0);
    _serverConfigs.insert("materialsMaterialIdRentalsMaterialRentalIdGet", defaultConf);
    _serverIndices.insert("materialsMaterialIdRentalsMaterialRentalIdGet", 0);
    _serverConfigs.insert("materialsMaterialIdRentalsMaterialRentalIdPut", defaultConf);
    _serverIndices.insert("materialsMaterialIdRentalsMaterialRentalIdPut", 0);
    _serverConfigs.insert("materialsMaterialIdRentalsPost", defaultConf);
    _serverIndices.insert("materialsMaterialIdRentalsPost", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIMaterialRentalsApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIMaterialRentalsApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIMaterialRentalsApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIMaterialRentalsApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIMaterialRentalsApi::setUsername(const QString &username) {
    _username = username;
}

void OAIMaterialRentalsApi::setPassword(const QString &password) {
    _password = password;
}


void OAIMaterialRentalsApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIMaterialRentalsApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIMaterialRentalsApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIMaterialRentalsApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIMaterialRentalsApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIMaterialRentalsApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIMaterialRentalsApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIMaterialRentalsApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIMaterialRentalsApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIMaterialRentalsApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIMaterialRentalsApi::getParamStylePrefix(const QString &style) {
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

QString OAIMaterialRentalsApi::getParamStyleSuffix(const QString &style) {
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

QString OAIMaterialRentalsApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIMaterialRentalsApi::materialsMaterialIdRentalsCheckoutPost(const QString &material_id, const ::OpenAPI::OptionalParam<OAI_materials__material_id__rentals_checkout__post_request> &oai_materials__material_id__rentals_checkout__post_request) {
    QString fullPath = QString(_serverConfigs["materialsMaterialIdRentalsCheckoutPost"][_serverIndices.value("materialsMaterialIdRentalsCheckoutPost")].URL()+"/materials/{material_id}/rentals/checkout/");
    
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
        QString material_idPathParam("{");
        material_idPathParam.append("material_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "material_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"material_id"+pathSuffix : pathPrefix;
        fullPath.replace(material_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(material_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_materials__material_id__rentals_checkout__post_request.hasValue()){

        
        QByteArray output = oai_materials__material_id__rentals_checkout__post_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMaterialRentalsApi::materialsMaterialIdRentalsCheckoutPostCallback);
    connect(this, &OAIMaterialRentalsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMaterialRentalsApi::materialsMaterialIdRentalsCheckoutPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_clocking_records_post_201_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT materialsMaterialIdRentalsCheckoutPostSignal(output);
        Q_EMIT materialsMaterialIdRentalsCheckoutPostSignalFull(worker, output);
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

        Q_EMIT materialsMaterialIdRentalsCheckoutPostSignalE(output, error_type, error_str);
        Q_EMIT materialsMaterialIdRentalsCheckoutPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT materialsMaterialIdRentalsCheckoutPostSignalError(output, error_type, error_str);
        Q_EMIT materialsMaterialIdRentalsCheckoutPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMaterialRentalsApi::materialsMaterialIdRentalsGet(const QString &material_id) {
    QString fullPath = QString(_serverConfigs["materialsMaterialIdRentalsGet"][_serverIndices.value("materialsMaterialIdRentalsGet")].URL()+"/materials/{material_id}/rentals/");
    
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
        QString material_idPathParam("{");
        material_idPathParam.append("material_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "material_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"material_id"+pathSuffix : pathPrefix;
        fullPath.replace(material_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(material_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMaterialRentalsApi::materialsMaterialIdRentalsGetCallback);
    connect(this, &OAIMaterialRentalsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMaterialRentalsApi::materialsMaterialIdRentalsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_materials__material_id__rentals__get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT materialsMaterialIdRentalsGetSignal(output);
        Q_EMIT materialsMaterialIdRentalsGetSignalFull(worker, output);
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

        Q_EMIT materialsMaterialIdRentalsGetSignalE(output, error_type, error_str);
        Q_EMIT materialsMaterialIdRentalsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT materialsMaterialIdRentalsGetSignalError(output, error_type, error_str);
        Q_EMIT materialsMaterialIdRentalsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMaterialRentalsApi::materialsMaterialIdRentalsMaterialRentalIdDelete(const QString &material_id, const QString &material_rental_id) {
    QString fullPath = QString(_serverConfigs["materialsMaterialIdRentalsMaterialRentalIdDelete"][_serverIndices.value("materialsMaterialIdRentalsMaterialRentalIdDelete")].URL()+"/materials/{material_id}/rentals/{material_rental_id}/");
    
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
        QString material_idPathParam("{");
        material_idPathParam.append("material_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "material_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"material_id"+pathSuffix : pathPrefix;
        fullPath.replace(material_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(material_id)));
    }
    
    {
        QString material_rental_idPathParam("{");
        material_rental_idPathParam.append("material_rental_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "material_rental_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"material_rental_id"+pathSuffix : pathPrefix;
        fullPath.replace(material_rental_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(material_rental_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMaterialRentalsApi::materialsMaterialIdRentalsMaterialRentalIdDeleteCallback);
    connect(this, &OAIMaterialRentalsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMaterialRentalsApi::materialsMaterialIdRentalsMaterialRentalIdDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_expense_files__expense_file_id__put_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdDeleteSignal(output);
        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdDeleteSignalFull(worker, output);
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

        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdDeleteSignalE(output, error_type, error_str);
        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdDeleteSignalError(output, error_type, error_str);
        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMaterialRentalsApi::materialsMaterialIdRentalsMaterialRentalIdGet(const QString &material_id, const QString &material_rental_id) {
    QString fullPath = QString(_serverConfigs["materialsMaterialIdRentalsMaterialRentalIdGet"][_serverIndices.value("materialsMaterialIdRentalsMaterialRentalIdGet")].URL()+"/materials/{material_id}/rentals/{material_rental_id}/");
    
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
        QString material_idPathParam("{");
        material_idPathParam.append("material_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "material_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"material_id"+pathSuffix : pathPrefix;
        fullPath.replace(material_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(material_id)));
    }
    
    {
        QString material_rental_idPathParam("{");
        material_rental_idPathParam.append("material_rental_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "material_rental_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"material_rental_id"+pathSuffix : pathPrefix;
        fullPath.replace(material_rental_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(material_rental_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMaterialRentalsApi::materialsMaterialIdRentalsMaterialRentalIdGetCallback);
    connect(this, &OAIMaterialRentalsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMaterialRentalsApi::materialsMaterialIdRentalsMaterialRentalIdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_materials__material_id__rentals__material_rental_id___get_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdGetSignal(output);
        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdGetSignalFull(worker, output);
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

        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdGetSignalE(output, error_type, error_str);
        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdGetSignalError(output, error_type, error_str);
        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMaterialRentalsApi::materialsMaterialIdRentalsMaterialRentalIdPut(const QString &material_id, const QString &material_rental_id) {
    QString fullPath = QString(_serverConfigs["materialsMaterialIdRentalsMaterialRentalIdPut"][_serverIndices.value("materialsMaterialIdRentalsMaterialRentalIdPut")].URL()+"/materials/{material_id}/rentals/{material_rental_id}/");
    
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
        QString material_idPathParam("{");
        material_idPathParam.append("material_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "material_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"material_id"+pathSuffix : pathPrefix;
        fullPath.replace(material_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(material_id)));
    }
    
    {
        QString material_rental_idPathParam("{");
        material_rental_idPathParam.append("material_rental_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "material_rental_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"material_rental_id"+pathSuffix : pathPrefix;
        fullPath.replace(material_rental_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(material_rental_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMaterialRentalsApi::materialsMaterialIdRentalsMaterialRentalIdPutCallback);
    connect(this, &OAIMaterialRentalsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMaterialRentalsApi::materialsMaterialIdRentalsMaterialRentalIdPutCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_expense_files__expense_file_id__put_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdPutSignal(output);
        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdPutSignalFull(worker, output);
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

        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdPutSignalE(output, error_type, error_str);
        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdPutSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdPutSignalError(output, error_type, error_str);
        Q_EMIT materialsMaterialIdRentalsMaterialRentalIdPutSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMaterialRentalsApi::materialsMaterialIdRentalsPost(const QString &material_id, const ::OpenAPI::OptionalParam<OAI_materials__material_id__rentals__post_request> &oai_materials__material_id__rentals__post_request) {
    QString fullPath = QString(_serverConfigs["materialsMaterialIdRentalsPost"][_serverIndices.value("materialsMaterialIdRentalsPost")].URL()+"/materials/{material_id}/rentals/");
    
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
        QString material_idPathParam("{");
        material_idPathParam.append("material_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "material_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"material_id"+pathSuffix : pathPrefix;
        fullPath.replace(material_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(material_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_materials__material_id__rentals__post_request.hasValue()){

        
        QByteArray output = oai_materials__material_id__rentals__post_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIMaterialRentalsApi::materialsMaterialIdRentalsPostCallback);
    connect(this, &OAIMaterialRentalsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIMaterialRentalsApi::materialsMaterialIdRentalsPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_clocking_records_post_201_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT materialsMaterialIdRentalsPostSignal(output);
        Q_EMIT materialsMaterialIdRentalsPostSignalFull(worker, output);
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

        Q_EMIT materialsMaterialIdRentalsPostSignalE(output, error_type, error_str);
        Q_EMIT materialsMaterialIdRentalsPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT materialsMaterialIdRentalsPostSignalError(output, error_type, error_str);
        Q_EMIT materialsMaterialIdRentalsPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIMaterialRentalsApi::tokenAvailable(){

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
