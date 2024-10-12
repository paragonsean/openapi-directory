/**
 * Quick start - Telematics SDK
 * # Introduction We have prepared a set of APIs for quick start to integrate telematics SDK that powers mobile telematics inside 3rd party mobile applications.  * [CONTACT US](https://telematicssdk.com) * [SANDBOX](https://userdatahub.com) * [DEV.PORTAL](https://docs.telematicssdk.com) * [DEMO APP](https://raxeltelematics.com/telematics-app)   # Overview Datamotion provides telematics infrastructure for mobile applications.   Telematics SDK turns any smartphone into telematics data gathering device to collect Location, driving and behavior data. API services unlocks power of your mobile application  There are 3 groups of methods: * 1 - user management * 2 - statistics for mobile app * 3 - statistics for back-end(s)  in certain cases you will need SNS or any other notification services. read more [here](https://docs.telematicssdk.com/platform-features/sns) # Possible architecture  There are three common schemes that are used by our clients. These schemes can be combined * Collect, Process, Store (required: 1&2) * Collect, Process (required: 1& sns) * Collect (required 1&sns)   ## Collect, Process, Store ![Collect, Process, Store](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection%2C+processing%2C+storage)  ## Collect, Process ![Collect, Process](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection+and+processing)  ## Collect ![Collect](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection+only)  *** ![Telematic sdk](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Github/transportation_small.png)  # Common use-cases: * Safe and efficient driving * Usage-based insurance * Safe driving assessment * Driver assessment * Trip log * Geo-analysis * Accident monitoring * Driving engagements * Location based services * Realtime Tracking and beyond  # How to start * Register a [SANDBOX ACCOUNT](https://userdatahub.com) * Get [CREDENTIALS](https://docs.userdatahub.com/sandbox/credentials)  * Follow the guide from [DEVELOPER POERTAL](https://docs.telematicssdk.com)  # Authentication To create a user on datamotion platform, you require to use InstanceID and InstanceKEY. You can get it in Datahub -> management -> user-service credentials  Once you create a user, you will get Device token, JWT token and refresh token. then, you will use it for APIs
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIClass2ForMobileAppOptionalApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIClass2ForMobileAppOptionalApi::OAIClass2ForMobileAppOptionalApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIClass2ForMobileAppOptionalApi::~OAIClass2ForMobileAppOptionalApi() {
}

void OAIClass2ForMobileAppOptionalApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.telematicssdk.com"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://mobilesdk.telematicssdk.com"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("tripsTripDetails", defaultConf);
    _serverIndices.insert("tripsTripDetails", 0);
    _serverConfigs.insert("userSafeScoringAccumulatedValueV1_scorings_individual", defaultConf);
    _serverIndices.insert("userSafeScoringAccumulatedValueV1_scorings_individual", 0);
    _serverConfigs.insert("userSafeScoringDailyValue_v1_scorings_individual_daily", defaultConf);
    _serverIndices.insert("userSafeScoringDailyValue_v1_scorings_individual_daily", 0);
    _serverConfigs.insert("userStatisticeDailyValueV1_statistics_individual_daily", defaultConf);
    _serverIndices.insert("userStatisticeDailyValueV1_statistics_individual_daily", 0);
    _serverConfigs.insert("userStatisticsAccumulatedValue_v1_statistics_individual", defaultConf);
    _serverIndices.insert("userStatisticsAccumulatedValue_v1_statistics_individual", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIClass2ForMobileAppOptionalApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIClass2ForMobileAppOptionalApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIClass2ForMobileAppOptionalApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIClass2ForMobileAppOptionalApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIClass2ForMobileAppOptionalApi::setUsername(const QString &username) {
    _username = username;
}

void OAIClass2ForMobileAppOptionalApi::setPassword(const QString &password) {
    _password = password;
}


void OAIClass2ForMobileAppOptionalApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIClass2ForMobileAppOptionalApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIClass2ForMobileAppOptionalApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIClass2ForMobileAppOptionalApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIClass2ForMobileAppOptionalApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIClass2ForMobileAppOptionalApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIClass2ForMobileAppOptionalApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIClass2ForMobileAppOptionalApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIClass2ForMobileAppOptionalApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIClass2ForMobileAppOptionalApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIClass2ForMobileAppOptionalApi::getParamStylePrefix(const QString &style) {
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

QString OAIClass2ForMobileAppOptionalApi::getParamStyleSuffix(const QString &style) {
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

QString OAIClass2ForMobileAppOptionalApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIClass2ForMobileAppOptionalApi::tripsTripDetails(const ::OpenAPI::OptionalParam<QString> &track_token) {
    QString fullPath = QString(_serverConfigs["tripsTripDetails"][_serverIndices.value("tripsTripDetails")].URL()+"/mobilesdk/stage/track/get_track/v1");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (track_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "trackToken", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("trackToken")).append(querySuffix).append(QUrl::toPercentEncoding(track_token.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIClass2ForMobileAppOptionalApi::tripsTripDetailsCallback);
    connect(this, &OAIClass2ForMobileAppOptionalApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIClass2ForMobileAppOptionalApi::tripsTripDetailsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAITripsTripDetails_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT tripsTripDetailsSignal(output);
        Q_EMIT tripsTripDetailsSignalFull(worker, output);
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

        Q_EMIT tripsTripDetailsSignalE(output, error_type, error_str);
        Q_EMIT tripsTripDetailsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT tripsTripDetailsSignalError(output, error_type, error_str);
        Q_EMIT tripsTripDetailsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIClass2ForMobileAppOptionalApi::userSafeScoringAccumulatedValueV1_scorings_individual(const ::OpenAPI::OptionalParam<QString> &start_date, const ::OpenAPI::OptionalParam<QString> &end_date) {
    QString fullPath = QString(_serverConfigs["userSafeScoringAccumulatedValueV1_scorings_individual"][_serverIndices.value("userSafeScoringAccumulatedValueV1_scorings_individual")].URL()+"/statistics/v1/Scorings/individual/");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (start_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "startDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("startDate")).append(querySuffix).append(QUrl::toPercentEncoding(start_date.stringValue()));
    }
    if (end_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "endDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("endDate")).append(querySuffix).append(QUrl::toPercentEncoding(end_date.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIClass2ForMobileAppOptionalApi::userSafeScoringAccumulatedValueV1_scorings_individualCallback);
    connect(this, &OAIClass2ForMobileAppOptionalApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIClass2ForMobileAppOptionalApi::userSafeScoringAccumulatedValueV1_scorings_individualCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT userSafeScoringAccumulatedValueV1_scorings_individualSignal(output);
        Q_EMIT userSafeScoringAccumulatedValueV1_scorings_individualSignalFull(worker, output);
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

        Q_EMIT userSafeScoringAccumulatedValueV1_scorings_individualSignalE(output, error_type, error_str);
        Q_EMIT userSafeScoringAccumulatedValueV1_scorings_individualSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT userSafeScoringAccumulatedValueV1_scorings_individualSignalError(output, error_type, error_str);
        Q_EMIT userSafeScoringAccumulatedValueV1_scorings_individualSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIClass2ForMobileAppOptionalApi::userSafeScoringDailyValue_v1_scorings_individual_daily(const ::OpenAPI::OptionalParam<QString> &tag, const ::OpenAPI::OptionalParam<QString> &start_date, const ::OpenAPI::OptionalParam<QString> &end_date) {
    QString fullPath = QString(_serverConfigs["userSafeScoringDailyValue_v1_scorings_individual_daily"][_serverIndices.value("userSafeScoringDailyValue_v1_scorings_individual_daily")].URL()+"/statistics/v1/Scorings/individual/daily");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (tag.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "Tag", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("Tag")).append(querySuffix).append(QUrl::toPercentEncoding(tag.stringValue()));
    }
    if (start_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "StartDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("StartDate")).append(querySuffix).append(QUrl::toPercentEncoding(start_date.stringValue()));
    }
    if (end_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "EndDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("EndDate")).append(querySuffix).append(QUrl::toPercentEncoding(end_date.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIClass2ForMobileAppOptionalApi::userSafeScoringDailyValue_v1_scorings_individual_dailyCallback);
    connect(this, &OAIClass2ForMobileAppOptionalApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIClass2ForMobileAppOptionalApi::userSafeScoringDailyValue_v1_scorings_individual_dailyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUserSafeScoringDailyValue_v1_scorings_individual_daily_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT userSafeScoringDailyValue_v1_scorings_individual_dailySignal(output);
        Q_EMIT userSafeScoringDailyValue_v1_scorings_individual_dailySignalFull(worker, output);
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

        Q_EMIT userSafeScoringDailyValue_v1_scorings_individual_dailySignalE(output, error_type, error_str);
        Q_EMIT userSafeScoringDailyValue_v1_scorings_individual_dailySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT userSafeScoringDailyValue_v1_scorings_individual_dailySignalError(output, error_type, error_str);
        Q_EMIT userSafeScoringDailyValue_v1_scorings_individual_dailySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIClass2ForMobileAppOptionalApi::userStatisticeDailyValueV1_statistics_individual_daily(const ::OpenAPI::OptionalParam<QString> &start_date, const ::OpenAPI::OptionalParam<QString> &end_date) {
    QString fullPath = QString(_serverConfigs["userStatisticeDailyValueV1_statistics_individual_daily"][_serverIndices.value("userStatisticeDailyValueV1_statistics_individual_daily")].URL()+"/statistics/v1/Statistics/individual/daily/");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (start_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "startDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("startDate")).append(querySuffix).append(QUrl::toPercentEncoding(start_date.stringValue()));
    }
    if (end_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "endDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("endDate")).append(querySuffix).append(QUrl::toPercentEncoding(end_date.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIClass2ForMobileAppOptionalApi::userStatisticeDailyValueV1_statistics_individual_dailyCallback);
    connect(this, &OAIClass2ForMobileAppOptionalApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIClass2ForMobileAppOptionalApi::userStatisticeDailyValueV1_statistics_individual_dailyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUserStatisticeDailyValueV1_statistics_individual_daily_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT userStatisticeDailyValueV1_statistics_individual_dailySignal(output);
        Q_EMIT userStatisticeDailyValueV1_statistics_individual_dailySignalFull(worker, output);
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

        Q_EMIT userStatisticeDailyValueV1_statistics_individual_dailySignalE(output, error_type, error_str);
        Q_EMIT userStatisticeDailyValueV1_statistics_individual_dailySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT userStatisticeDailyValueV1_statistics_individual_dailySignalError(output, error_type, error_str);
        Q_EMIT userStatisticeDailyValueV1_statistics_individual_dailySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIClass2ForMobileAppOptionalApi::userStatisticsAccumulatedValue_v1_statistics_individual(const ::OpenAPI::OptionalParam<QString> &start_date, const ::OpenAPI::OptionalParam<QString> &end_date) {
    QString fullPath = QString(_serverConfigs["userStatisticsAccumulatedValue_v1_statistics_individual"][_serverIndices.value("userStatisticsAccumulatedValue_v1_statistics_individual")].URL()+"/statistics/v1/Statistics/individual/");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (start_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "startDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("startDate")).append(querySuffix).append(QUrl::toPercentEncoding(start_date.stringValue()));
    }
    if (end_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "endDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("endDate")).append(querySuffix).append(QUrl::toPercentEncoding(end_date.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIClass2ForMobileAppOptionalApi::userStatisticsAccumulatedValue_v1_statistics_individualCallback);
    connect(this, &OAIClass2ForMobileAppOptionalApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIClass2ForMobileAppOptionalApi::userStatisticsAccumulatedValue_v1_statistics_individualCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT userStatisticsAccumulatedValue_v1_statistics_individualSignal(output);
        Q_EMIT userStatisticsAccumulatedValue_v1_statistics_individualSignalFull(worker, output);
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

        Q_EMIT userStatisticsAccumulatedValue_v1_statistics_individualSignalE(output, error_type, error_str);
        Q_EMIT userStatisticsAccumulatedValue_v1_statistics_individualSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT userStatisticsAccumulatedValue_v1_statistics_individualSignalError(output, error_type, error_str);
        Q_EMIT userStatisticsAccumulatedValue_v1_statistics_individualSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIClass2ForMobileAppOptionalApi::tokenAvailable(){

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
