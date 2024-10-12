/**
 * Checks API
 * **NOTE:** This is a preview of the API and it is not considered stable since refinements are still being made.  # Introduction  Welcome to the  **Truora Check** [**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) reference. You may also want to check out our [**Validations API docs**](https://docs.validations.truora.com/) or our [**Signals API docs**](https://docs.signals.truora.com/).  Truora Check API allows performing full background checks on people, vehicles and companies. There are three main types of background checks:  - **Personal background check**: Verifies national IDs in multiple databases of public and legal entities in the LATAM region. For every national ID, returns information on: personal identity, criminal records, international background check, and professional background.  - **Vehicle background check**: Verifies the vehicle documents and the owner identity in multiple databases of public and legal entities in the LATAM region. For every vehicle and owner type, returns information on: personal identity, driving records, criminal records, and vehicle information.    - **Company background check**: Verifies the tax ID or a company name in multiple databases of public and legal entities in the LATAM region. For every company, returns the associated: business status, legal and criminal records, and media reports.  # API Key V1 is live!  API key version 1 is now live. Users with version 0 API keys are not immediately required to upgrade to V1 but should plan to do so at their earliest convenience. The changes for integration with API keys v1 are as follows:  - The field ``user_authorized`` is now required to perform person checks. This field indicates the API user has authorization to perform the check in compliance with data protection law. - The field ``homonym_scores`` is no longer included in our person check response as its results are already included in the body of the check and keeping them duplicated is generating unnecessary confusion.   # API composition  ## Endpoints  - **Check endpoints**: Provide an easy way to create and search for a background check. They also allow inserting groups of checks into reports. Each check contains scores, datasets and databases.   ```plain https://api.truora.com/v1/checks ```  - **Report endpoints**: Support batch uploads and grouping multiple checks together. Excel and .csv files are supported for batch uploads.   ```plain https://api.truora.com/v1/reports ```  - **Configuration endpoints**: Allows personalizing data sets and scores for customized background checks.  ```plain https://api.truora.com/v1/config ```  - **Continuous check endpoints**: Allows creating recurring checks and get notified whenever a change in the check score occurs.  ```plain https://api.truora.com/v1/continuous_checks ```  - **Behavior endpoints**: Allows sharing anonymous feedback about a person behavior when interacting with the company.  ```plain https://api.truora.com/v1/behaviour ```  - **Hooks endpoints**: Allows sending notifications via requests to your service or another third-party service whenever certain events occur.  ```plain https://api.truora.com/v1/hooks ```  ## Datasets  Categories that group the resulting information for background checks from databases are called datasets. Datasets are divided in:  - **Personal identity**: Corroborates the existence and validates personal identity documents.   - **Criminal record**: Checks for crimes according to each country penal code or criminal code. Keep in mind that data aged less than 10 years is usually more consistent.  - **Legal background**: Checks for lawsuits filed. Keep in mind that data aged less than 10 years is usually more consistent.  - **International background**: Checks international lists for crimes related to identity theft, money laundering, terrorist financing, and high crimes.  - **Professional background**: Checks professional regulatory entities for relevant information.  - **Affiliations and insurances**: Checks the history and status of social security affiliations.  - **Alert in media**: Checks major media agencies for relevant news related to violent actions.      - **Vehicle information**: Checks for the physical characteristics of the vehicle, technical status, insurance history, and other relevant information.  - **Traffic fines**: Checks for outstanding traffic fines.  - **Driving licenses**: Shows information relevant to the driver. Such as license status and driver certificates.  - **Business background**: Checks for business status, legal and criminal history, and other relevant information.  - **Taxes and Finances**: Checks for the information related to personal finances, liabilities, and taxes.  ## Requests Format  The POST requests receive a body that must be encoded in `www-x-form-urlencoded`, for instance:  ```plain type=person&national_id=123456&country=CO ```  The responses are always encoded in `JSON` format.  ## Errors  Whenever there is an error, a JSON with the following format is returned:  ```json {     \"code\": <Truora error code>,     \"http_code\": <The HTTP status of the response>,     \"message\": <The error message> } ```  for instance:  ```json {     \"code\": 10404,     \"http_code\": 404,     \"message\": \"The Check was not found\" } ```  ## SDKs  If your favorite language was not on the next list, You can use our [OpenAPI 3 spec](https://docs.truora.com/openapi.json) to generate it using the [Open API Generator](https://openapi-generator.tech/docs/installation).  To download the SDK click on the desired programming language:  - [C# .Net Core](https://truora-sdk.s3.amazonaws.com/checks/checks_csharp-netcore_latest.zip)  - [Elixir](https://truora-sdk.s3.amazonaws.com/checks/checks_elixir_latest.zip)  - [Go](https://truora-sdk.s3.amazonaws.com/checks/checks_go_latest.zip)  - [Java](https://truora-sdk.s3.amazonaws.com/checks/checks_java_latest.zip)  - [JavaScript](https://truora-sdk.s3.amazonaws.com/checks/checks_javascript_latest.zip)  - [Objc](https://truora-sdk.s3.amazonaws.com/checks/checks_objc_latest.zip)  - [Php](https://truora-sdk.s3.amazonaws.com/checks/checks_php_latest.zip)  - [Python](https://truora-sdk.s3.amazonaws.com/checks/checks_python_latest.zip)  - [Ruby](https://truora-sdk.s3.amazonaws.com/checks/checks_ruby_latest.zip)  You can see the full list of supported platforms here:  https://openapi-generator.tech/docs/generators   
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: api@truora.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICustomTypeApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAICustomTypeApi::OAICustomTypeApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAICustomTypeApi::~OAICustomTypeApi() {
}

void OAICustomTypeApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.truora.com"),
    "The main Truora API domain",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("createScoreConfig", defaultConf);
    _serverIndices.insert("createScoreConfig", 0);
    _serverConfigs.insert("deleteCustomType", defaultConf);
    _serverIndices.insert("deleteCustomType", 0);
    _serverConfigs.insert("listScoreConfigs", defaultConf);
    _serverIndices.insert("listScoreConfigs", 0);
    _serverConfigs.insert("updateCustomType", defaultConf);
    _serverIndices.insert("updateCustomType", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAICustomTypeApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAICustomTypeApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAICustomTypeApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAICustomTypeApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAICustomTypeApi::setUsername(const QString &username) {
    _username = username;
}

void OAICustomTypeApi::setPassword(const QString &password) {
    _password = password;
}


void OAICustomTypeApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAICustomTypeApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAICustomTypeApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAICustomTypeApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAICustomTypeApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAICustomTypeApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAICustomTypeApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAICustomTypeApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAICustomTypeApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAICustomTypeApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAICustomTypeApi::getParamStylePrefix(const QString &style) {
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

QString OAICustomTypeApi::getParamStyleSuffix(const QString &style) {
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

QString OAICustomTypeApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAICustomTypeApi::createScoreConfig(const QString &country, const QString &type, const ::OpenAPI::OptionalParam<float> &dataset_affiliations_and_insurances, const ::OpenAPI::OptionalParam<float> &dataset_alert_in_media, const ::OpenAPI::OptionalParam<float> &dataset_business_background, const ::OpenAPI::OptionalParam<float> &dataset_criminal_record, const ::OpenAPI::OptionalParam<float> &dataset_driving_licenses, const ::OpenAPI::OptionalParam<float> &dataset_international_background, const ::OpenAPI::OptionalParam<float> &dataset_legal_background, const ::OpenAPI::OptionalParam<float> &dataset_personal_identity, const ::OpenAPI::OptionalParam<float> &dataset_professional_background, const ::OpenAPI::OptionalParam<float> &dataset_taxes_and_finances, const ::OpenAPI::OptionalParam<float> &dataset_traffic_fines, const ::OpenAPI::OptionalParam<float> &dataset_vehicle_information, const ::OpenAPI::OptionalParam<float> &dataset_vehicle_permits) {
    QString fullPath = QString(_serverConfigs["createScoreConfig"][_serverIndices.value("createScoreConfig")].URL()+"/v1/config");
    
    if (_apiKeys.contains("api-key")) {
        addHeaders("api-key",_apiKeys.find("api-key").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    
    {
        input.add_var("country", ::OpenAPI::toStringValue(country));
    }
    if (dataset_affiliations_and_insurances.hasValue())
    {
        input.add_var("dataset_affiliations_and_insurances", ::OpenAPI::toStringValue(dataset_affiliations_and_insurances.value()));
    }
    if (dataset_alert_in_media.hasValue())
    {
        input.add_var("dataset_alert_in_media", ::OpenAPI::toStringValue(dataset_alert_in_media.value()));
    }
    if (dataset_business_background.hasValue())
    {
        input.add_var("dataset_business_background", ::OpenAPI::toStringValue(dataset_business_background.value()));
    }
    if (dataset_criminal_record.hasValue())
    {
        input.add_var("dataset_criminal_record", ::OpenAPI::toStringValue(dataset_criminal_record.value()));
    }
    if (dataset_driving_licenses.hasValue())
    {
        input.add_var("dataset_driving_licenses", ::OpenAPI::toStringValue(dataset_driving_licenses.value()));
    }
    if (dataset_international_background.hasValue())
    {
        input.add_var("dataset_international_background", ::OpenAPI::toStringValue(dataset_international_background.value()));
    }
    if (dataset_legal_background.hasValue())
    {
        input.add_var("dataset_legal_background", ::OpenAPI::toStringValue(dataset_legal_background.value()));
    }
    if (dataset_personal_identity.hasValue())
    {
        input.add_var("dataset_personal_identity", ::OpenAPI::toStringValue(dataset_personal_identity.value()));
    }
    if (dataset_professional_background.hasValue())
    {
        input.add_var("dataset_professional_background", ::OpenAPI::toStringValue(dataset_professional_background.value()));
    }
    if (dataset_taxes_and_finances.hasValue())
    {
        input.add_var("dataset_taxes_and_finances", ::OpenAPI::toStringValue(dataset_taxes_and_finances.value()));
    }
    if (dataset_traffic_fines.hasValue())
    {
        input.add_var("dataset_traffic_fines", ::OpenAPI::toStringValue(dataset_traffic_fines.value()));
    }
    if (dataset_vehicle_information.hasValue())
    {
        input.add_var("dataset_vehicle_information", ::OpenAPI::toStringValue(dataset_vehicle_information.value()));
    }
    if (dataset_vehicle_permits.hasValue())
    {
        input.add_var("dataset_vehicle_permits", ::OpenAPI::toStringValue(dataset_vehicle_permits.value()));
    }
    
    {
        input.add_var("type", ::OpenAPI::toStringValue(type));
    }

    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICustomTypeApi::createScoreConfigCallback);
    connect(this, &OAICustomTypeApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICustomTypeApi::createScoreConfigCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIScoreConfigOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createScoreConfigSignal(output);
        Q_EMIT createScoreConfigSignalFull(worker, output);
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

        Q_EMIT createScoreConfigSignalE(output, error_type, error_str);
        Q_EMIT createScoreConfigSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createScoreConfigSignalError(output, error_type, error_str);
        Q_EMIT createScoreConfigSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICustomTypeApi::deleteCustomType(const QString &type, const ::OpenAPI::OptionalParam<QString> &country) {
    QString fullPath = QString(_serverConfigs["deleteCustomType"][_serverIndices.value("deleteCustomType")].URL()+"/v1/config");
    
    if (_apiKeys.contains("api-key")) {
        addHeaders("api-key",_apiKeys.find("api-key").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "type", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("type")).append(querySuffix).append(QUrl::toPercentEncoding(type));
    }
    if (country.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "country", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("country")).append(querySuffix).append(QUrl::toPercentEncoding(country.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICustomTypeApi::deleteCustomTypeCallback);
    connect(this, &OAICustomTypeApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICustomTypeApi::deleteCustomTypeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteCustomTypeSignal();
        Q_EMIT deleteCustomTypeSignalFull(worker);
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

        Q_EMIT deleteCustomTypeSignalE(error_type, error_str);
        Q_EMIT deleteCustomTypeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteCustomTypeSignalError(error_type, error_str);
        Q_EMIT deleteCustomTypeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICustomTypeApi::listScoreConfigs(const ::OpenAPI::OptionalParam<QString> &start_key) {
    QString fullPath = QString(_serverConfigs["listScoreConfigs"][_serverIndices.value("listScoreConfigs")].URL()+"/v1/config");
    
    if (_apiKeys.contains("api-key")) {
        addHeaders("api-key",_apiKeys.find("api-key").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (start_key.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "start_key", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("start_key")).append(querySuffix).append(QUrl::toPercentEncoding(start_key.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICustomTypeApi::listScoreConfigsCallback);
    connect(this, &OAICustomTypeApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICustomTypeApi::listScoreConfigsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIScoreConfigsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listScoreConfigsSignal(output);
        Q_EMIT listScoreConfigsSignalFull(worker, output);
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

        Q_EMIT listScoreConfigsSignalE(output, error_type, error_str);
        Q_EMIT listScoreConfigsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listScoreConfigsSignalError(output, error_type, error_str);
        Q_EMIT listScoreConfigsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICustomTypeApi::updateCustomType(const QString &country, const QString &type, const ::OpenAPI::OptionalParam<float> &dataset_affiliations_and_insurances, const ::OpenAPI::OptionalParam<float> &dataset_alert_in_media, const ::OpenAPI::OptionalParam<float> &dataset_business_background, const ::OpenAPI::OptionalParam<float> &dataset_criminal_record, const ::OpenAPI::OptionalParam<float> &dataset_driving_licenses, const ::OpenAPI::OptionalParam<float> &dataset_international_background, const ::OpenAPI::OptionalParam<float> &dataset_legal_background, const ::OpenAPI::OptionalParam<float> &dataset_personal_identity, const ::OpenAPI::OptionalParam<float> &dataset_professional_background, const ::OpenAPI::OptionalParam<float> &dataset_taxes_and_finances, const ::OpenAPI::OptionalParam<float> &dataset_traffic_fines, const ::OpenAPI::OptionalParam<float> &dataset_vehicle_information, const ::OpenAPI::OptionalParam<float> &dataset_vehicle_permits) {
    QString fullPath = QString(_serverConfigs["updateCustomType"][_serverIndices.value("updateCustomType")].URL()+"/v1/config");
    
    if (_apiKeys.contains("api-key")) {
        addHeaders("api-key",_apiKeys.find("api-key").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    
    {
        input.add_var("country", ::OpenAPI::toStringValue(country));
    }
    if (dataset_affiliations_and_insurances.hasValue())
    {
        input.add_var("dataset_affiliations_and_insurances", ::OpenAPI::toStringValue(dataset_affiliations_and_insurances.value()));
    }
    if (dataset_alert_in_media.hasValue())
    {
        input.add_var("dataset_alert_in_media", ::OpenAPI::toStringValue(dataset_alert_in_media.value()));
    }
    if (dataset_business_background.hasValue())
    {
        input.add_var("dataset_business_background", ::OpenAPI::toStringValue(dataset_business_background.value()));
    }
    if (dataset_criminal_record.hasValue())
    {
        input.add_var("dataset_criminal_record", ::OpenAPI::toStringValue(dataset_criminal_record.value()));
    }
    if (dataset_driving_licenses.hasValue())
    {
        input.add_var("dataset_driving_licenses", ::OpenAPI::toStringValue(dataset_driving_licenses.value()));
    }
    if (dataset_international_background.hasValue())
    {
        input.add_var("dataset_international_background", ::OpenAPI::toStringValue(dataset_international_background.value()));
    }
    if (dataset_legal_background.hasValue())
    {
        input.add_var("dataset_legal_background", ::OpenAPI::toStringValue(dataset_legal_background.value()));
    }
    if (dataset_personal_identity.hasValue())
    {
        input.add_var("dataset_personal_identity", ::OpenAPI::toStringValue(dataset_personal_identity.value()));
    }
    if (dataset_professional_background.hasValue())
    {
        input.add_var("dataset_professional_background", ::OpenAPI::toStringValue(dataset_professional_background.value()));
    }
    if (dataset_taxes_and_finances.hasValue())
    {
        input.add_var("dataset_taxes_and_finances", ::OpenAPI::toStringValue(dataset_taxes_and_finances.value()));
    }
    if (dataset_traffic_fines.hasValue())
    {
        input.add_var("dataset_traffic_fines", ::OpenAPI::toStringValue(dataset_traffic_fines.value()));
    }
    if (dataset_vehicle_information.hasValue())
    {
        input.add_var("dataset_vehicle_information", ::OpenAPI::toStringValue(dataset_vehicle_information.value()));
    }
    if (dataset_vehicle_permits.hasValue())
    {
        input.add_var("dataset_vehicle_permits", ::OpenAPI::toStringValue(dataset_vehicle_permits.value()));
    }
    
    {
        input.add_var("type", ::OpenAPI::toStringValue(type));
    }

    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICustomTypeApi::updateCustomTypeCallback);
    connect(this, &OAICustomTypeApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICustomTypeApi::updateCustomTypeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateCustomTypeSignal();
        Q_EMIT updateCustomTypeSignalFull(worker);
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

        Q_EMIT updateCustomTypeSignalE(error_type, error_str);
        Q_EMIT updateCustomTypeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateCustomTypeSignalError(error_type, error_str);
        Q_EMIT updateCustomTypeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICustomTypeApi::tokenAvailable(){

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
