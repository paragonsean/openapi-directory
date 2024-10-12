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

#include "OAIChecksApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIChecksApi::OAIChecksApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIChecksApi::~OAIChecksApi() {
}

void OAIChecksApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.truora.com"),
    "The main Truora API domain",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("createCheck", defaultConf);
    _serverIndices.insert("createCheck", 0);
    _serverConfigs.insert("getCheck", defaultConf);
    _serverIndices.insert("getCheck", 0);
    _serverConfigs.insert("getHealthDashboard", defaultConf);
    _serverIndices.insert("getHealthDashboard", 0);
    _serverConfigs.insert("listCheckDetails", defaultConf);
    _serverIndices.insert("listCheckDetails", 0);
    _serverConfigs.insert("listChecks", defaultConf);
    _serverIndices.insert("listChecks", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIChecksApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIChecksApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIChecksApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIChecksApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIChecksApi::setUsername(const QString &username) {
    _username = username;
}

void OAIChecksApi::setPassword(const QString &password) {
    _password = password;
}


void OAIChecksApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIChecksApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIChecksApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIChecksApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIChecksApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIChecksApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIChecksApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIChecksApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIChecksApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIChecksApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIChecksApi::getParamStylePrefix(const QString &style) {
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

QString OAIChecksApi::getParamStyleSuffix(const QString &style) {
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

QString OAIChecksApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIChecksApi::createCheck(const QString &country, const QString &type, const ::OpenAPI::OptionalParam<QString> &truora_priority, const ::OpenAPI::OptionalParam<QString> &birth_certificate, const ::OpenAPI::OptionalParam<QString> &company_name, const ::OpenAPI::OptionalParam<QDate> &date_of_birth, const ::OpenAPI::OptionalParam<QString> &diplomatic_id, const ::OpenAPI::OptionalParam<QString> &driver_license, const ::OpenAPI::OptionalParam<QString> &escrow, const ::OpenAPI::OptionalParam<QString> &first_name, const ::OpenAPI::OptionalParam<bool> &force_creation, const ::OpenAPI::OptionalParam<QString> &foreign_id, const ::OpenAPI::OptionalParam<QDate> &issue_date, const ::OpenAPI::OptionalParam<QString> &last_name, const ::OpenAPI::OptionalParam<QString> &license_plate, const ::OpenAPI::OptionalParam<QString> &national_id, const ::OpenAPI::OptionalParam<QString> &native_country, const ::OpenAPI::OptionalParam<QString> &owner_document_id, const ::OpenAPI::OptionalParam<QString> &owner_document_type, const ::OpenAPI::OptionalParam<QString> &passport, const ::OpenAPI::OptionalParam<QDate> &payment_date, const ::OpenAPI::OptionalParam<QString> &pep, const ::OpenAPI::OptionalParam<QString> &phone_number, const ::OpenAPI::OptionalParam<QString> &professional_card, const ::OpenAPI::OptionalParam<QString> &ptp, const ::OpenAPI::OptionalParam<QString> &region, const ::OpenAPI::OptionalParam<QString> &report_id, const ::OpenAPI::OptionalParam<QString> &state_id, const ::OpenAPI::OptionalParam<QString> &tax_id, const ::OpenAPI::OptionalParam<bool> &user_authorized, const ::OpenAPI::OptionalParam<QString> &vehicle_id, const ::OpenAPI::OptionalParam<QString> &verification_code, const ::OpenAPI::OptionalParam<QString> &watch) {
    QString fullPath = QString(_serverConfigs["createCheck"][_serverIndices.value("createCheck")].URL()+"/v1/checks");
    
    if (_apiKeys.contains("api-key")) {
        addHeaders("api-key",_apiKeys.find("api-key").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (birth_certificate.hasValue())
    {
        input.add_var("birth_certificate", ::OpenAPI::toStringValue(birth_certificate.value()));
    }
    if (company_name.hasValue())
    {
        input.add_var("company_name", ::OpenAPI::toStringValue(company_name.value()));
    }
    
    {
        input.add_var("country", ::OpenAPI::toStringValue(country));
    }
    if (date_of_birth.hasValue())
    {
        input.add_var("date_of_birth", ::OpenAPI::toStringValue(date_of_birth.value()));
    }
    if (diplomatic_id.hasValue())
    {
        input.add_var("diplomatic_id", ::OpenAPI::toStringValue(diplomatic_id.value()));
    }
    if (driver_license.hasValue())
    {
        input.add_var("driver_license", ::OpenAPI::toStringValue(driver_license.value()));
    }
    if (escrow.hasValue())
    {
        input.add_var("escrow", ::OpenAPI::toStringValue(escrow.value()));
    }
    if (first_name.hasValue())
    {
        input.add_var("first_name", ::OpenAPI::toStringValue(first_name.value()));
    }
    if (force_creation.hasValue())
    {
        input.add_var("force_creation", ::OpenAPI::toStringValue(force_creation.value()));
    }
    if (foreign_id.hasValue())
    {
        input.add_var("foreign_id", ::OpenAPI::toStringValue(foreign_id.value()));
    }
    if (issue_date.hasValue())
    {
        input.add_var("issue_date", ::OpenAPI::toStringValue(issue_date.value()));
    }
    if (last_name.hasValue())
    {
        input.add_var("last_name", ::OpenAPI::toStringValue(last_name.value()));
    }
    if (license_plate.hasValue())
    {
        input.add_var("license_plate", ::OpenAPI::toStringValue(license_plate.value()));
    }
    if (national_id.hasValue())
    {
        input.add_var("national_id", ::OpenAPI::toStringValue(national_id.value()));
    }
    if (native_country.hasValue())
    {
        input.add_var("native_country", ::OpenAPI::toStringValue(native_country.value()));
    }
    if (owner_document_id.hasValue())
    {
        input.add_var("owner_document_id", ::OpenAPI::toStringValue(owner_document_id.value()));
    }
    if (owner_document_type.hasValue())
    {
        input.add_var("owner_document_type", ::OpenAPI::toStringValue(owner_document_type.value()));
    }
    if (passport.hasValue())
    {
        input.add_var("passport", ::OpenAPI::toStringValue(passport.value()));
    }
    if (payment_date.hasValue())
    {
        input.add_var("payment_date", ::OpenAPI::toStringValue(payment_date.value()));
    }
    if (pep.hasValue())
    {
        input.add_var("pep", ::OpenAPI::toStringValue(pep.value()));
    }
    if (phone_number.hasValue())
    {
        input.add_var("phone_number", ::OpenAPI::toStringValue(phone_number.value()));
    }
    if (professional_card.hasValue())
    {
        input.add_var("professional_card", ::OpenAPI::toStringValue(professional_card.value()));
    }
    if (ptp.hasValue())
    {
        input.add_var("ptp", ::OpenAPI::toStringValue(ptp.value()));
    }
    if (region.hasValue())
    {
        input.add_var("region", ::OpenAPI::toStringValue(region.value()));
    }
    if (report_id.hasValue())
    {
        input.add_var("report_id", ::OpenAPI::toStringValue(report_id.value()));
    }
    if (state_id.hasValue())
    {
        input.add_var("state_id", ::OpenAPI::toStringValue(state_id.value()));
    }
    if (tax_id.hasValue())
    {
        input.add_var("tax_id", ::OpenAPI::toStringValue(tax_id.value()));
    }
    
    {
        input.add_var("type", ::OpenAPI::toStringValue(type));
    }
    if (user_authorized.hasValue())
    {
        input.add_var("user_authorized", ::OpenAPI::toStringValue(user_authorized.value()));
    }
    if (vehicle_id.hasValue())
    {
        input.add_var("vehicle_id", ::OpenAPI::toStringValue(vehicle_id.value()));
    }
    if (verification_code.hasValue())
    {
        input.add_var("verification_code", ::OpenAPI::toStringValue(verification_code.value()));
    }
    if (watch.hasValue())
    {
        input.add_var("watch", ::OpenAPI::toStringValue(watch.value()));
    }

    if (truora_priority.hasValue())
    {
        if (!::OpenAPI::toStringValue(truora_priority.value()).isEmpty()) {
            input.headers.insert("Truora-Priority", ::OpenAPI::toStringValue(truora_priority.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIChecksApi::createCheckCallback);
    connect(this, &OAIChecksApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIChecksApi::createCheckCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICheckOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createCheckSignal(output);
        Q_EMIT createCheckSignalFull(worker, output);
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

        Q_EMIT createCheckSignalE(output, error_type, error_str);
        Q_EMIT createCheckSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createCheckSignalError(output, error_type, error_str);
        Q_EMIT createCheckSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIChecksApi::getCheck(const QString &check_id) {
    QString fullPath = QString(_serverConfigs["getCheck"][_serverIndices.value("getCheck")].URL()+"/v1/checks/{check_id}");
    
    if (_apiKeys.contains("api-key")) {
        addHeaders("api-key",_apiKeys.find("api-key").value());
    }
    
    
    {
        QString check_idPathParam("{");
        check_idPathParam.append("check_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "check_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"check_id"+pathSuffix : pathPrefix;
        fullPath.replace(check_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(check_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIChecksApi::getCheckCallback);
    connect(this, &OAIChecksApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIChecksApi::getCheckCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICheckOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getCheckSignal(output);
        Q_EMIT getCheckSignalFull(worker, output);
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

        Q_EMIT getCheckSignalE(output, error_type, error_str);
        Q_EMIT getCheckSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getCheckSignalError(output, error_type, error_str);
        Q_EMIT getCheckSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIChecksApi::getHealthDashboard(const ::OpenAPI::OptionalParam<QString> &country, const ::OpenAPI::OptionalParam<QString> &unix_timestamp_seconds, const ::OpenAPI::OptionalParam<QString> &unixtimezone_offset_seconds) {
    QString fullPath = QString(_serverConfigs["getHealthDashboard"][_serverIndices.value("getHealthDashboard")].URL()+"/v1/checks/health");
    
    if (_apiKeys.contains("api-key")) {
        addHeaders("api-key",_apiKeys.find("api-key").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
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
    if (unix_timestamp_seconds.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "unixTimestampSeconds", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("unixTimestampSeconds")).append(querySuffix).append(QUrl::toPercentEncoding(unix_timestamp_seconds.stringValue()));
    }
    if (unixtimezone_offset_seconds.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "unixtimezoneOffsetSeconds", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("unixtimezoneOffsetSeconds")).append(querySuffix).append(QUrl::toPercentEncoding(unixtimezone_offset_seconds.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIChecksApi::getHealthDashboardCallback);
    connect(this, &OAIChecksApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIChecksApi::getHealthDashboardCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIDatabase> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIDatabase val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getHealthDashboardSignal(output);
        Q_EMIT getHealthDashboardSignalFull(worker, output);
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

        Q_EMIT getHealthDashboardSignalE(output, error_type, error_str);
        Q_EMIT getHealthDashboardSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getHealthDashboardSignalError(output, error_type, error_str);
        Q_EMIT getHealthDashboardSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIChecksApi::listCheckDetails(const QString &check_id, const ::OpenAPI::OptionalParam<QString> &start_key, const ::OpenAPI::OptionalParam<QString> &lang) {
    QString fullPath = QString(_serverConfigs["listCheckDetails"][_serverIndices.value("listCheckDetails")].URL()+"/v1/checks/{check_id}/details");
    
    if (_apiKeys.contains("api-key")) {
        addHeaders("api-key",_apiKeys.find("api-key").value());
    }
    
    
    {
        QString check_idPathParam("{");
        check_idPathParam.append("check_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "check_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"check_id"+pathSuffix : pathPrefix;
        fullPath.replace(check_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(check_id)));
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
    if (lang.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "lang", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("lang")).append(querySuffix).append(QUrl::toPercentEncoding(lang.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIChecksApi::listCheckDetailsCallback);
    connect(this, &OAIChecksApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIChecksApi::listCheckDetailsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICheckDetailsOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listCheckDetailsSignal(output);
        Q_EMIT listCheckDetailsSignalFull(worker, output);
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

        Q_EMIT listCheckDetailsSignalE(output, error_type, error_str);
        Q_EMIT listCheckDetailsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listCheckDetailsSignalError(output, error_type, error_str);
        Q_EMIT listCheckDetailsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIChecksApi::listChecks(const ::OpenAPI::OptionalParam<QString> &start_key, const ::OpenAPI::OptionalParam<QString> &report_id) {
    QString fullPath = QString(_serverConfigs["listChecks"][_serverIndices.value("listChecks")].URL()+"/v1/checks");
    
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
    if (report_id.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "report_id", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("report_id")).append(querySuffix).append(QUrl::toPercentEncoding(report_id.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIChecksApi::listChecksCallback);
    connect(this, &OAIChecksApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIChecksApi::listChecksCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIChecksOutput output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listChecksSignal(output);
        Q_EMIT listChecksSignalFull(worker, output);
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

        Q_EMIT listChecksSignalE(output, error_type, error_str);
        Q_EMIT listChecksSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listChecksSignalError(output, error_type, error_str);
        Q_EMIT listChecksSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIChecksApi::tokenAvailable(){

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
