/**
 * ContentGroove API
 * # Overview  The ContentGroove Developer API enables you to add the power of ContentGroove's video AI to your own applications and workflows.  Webhooks are a way for ContentGroove to send video information to your application, to update your system and/or trigger other business processes.  You can use Webhooks and the Developer API separately or together.  # Getting Started with Webhooks  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Read \"Using Webhooks\" on the [API Reference page](https://developers.contentgroove.com/api_reference) - Visit the [Webhooks page](https://app.contentgroove.com/webhook_subscriptions) and create a new webhook  # Using Webhooks  Webhooks, also known as callbacks, are a way for ContentGroove to notify your application as soon as possible after an event has occurred in ContentGroove. For example after a media completes processing, ContentGroove can use a webhook to notify your application with information about the video: Suggested clips, transcription, and so on. You can use the information sent to update your system and/or use the webhook to trigger other business processes.  The webhook request is sent as an HTTP POST containing a payload of JSON-formatted data. For the details of the payload format see the \"CALLBACKS\" sections below.  When your application receives the webhook request, it must respond with a 200 HTTP status code (success). If a 200 HTTP status code is not returned, ContentGroove will assume that the webhook was not delivered and will retry a limited number of times, using an exponential backoff algorithm.  ContentGroove makes a best effort to attempt to send the webhook at least once. Applications receiving webhooks must tolerate the possibility of a single webhook payload being sent more than once (idempotent behavior). Applications receiving webhooks should tolerate the possibility that a webhook could not be delivered (for example your application was down when delivery was attempted).  # Getting Started with the Developer API  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Visit the [API Keys page](https://app.contentgroove.com/api_keys)   - Create a new API Key then copy and save the value.     > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️ - View all available endpoints, and try the API, on our [API Reference page](https://developers.contentgroove.com/api_reference)  # Using the Developer API  - Create a new media (video or audio) in ContentGroove   - If the video or audio is available from a URL, you can create a media by providing the `source_url` parameter. ContentGroove will fetch the video or audio from the URL if possible.   - Or, you can create a media from a video or audio file which you upload directly to ContentGroove (see File Uploading section below). - After the new media is created, at first it will be in a \"processing\" state.   Depending on the size and duration of the video or audio file, it will take some time for processing to complete.   - You can use ContentGroove Webhooks to be notified immediately when processing has completed. (Details coming soon.)   - You can also use the API to read the state of the media, to determine if the media has completed processing yet. - After the media has completed processing, you can access all of these details about the media:   - The media name and description   - The transcription of spoken words   - Topics and keywords which were discussed in the transcription   - Suggested video clips are automatically created - In addition to the automatically created video clips, you can create more video clips from the media  # Response Codes  The following is a comprehensive list of the status codes you may receive while using the ContentGroove API:  - 200 \"Ok\"   - The request was valid - 400 \"Bad Request   - This is returned when there was a problem parsing the JSON body of your request if you supplied the 'Content-Type': 'application/json' header, or if your request is missing the 'Content-Type' header altogether - 401 \"Unauthorized\"   - This is returned when you are attempting to perform an action on a resource that you are not authorized to do - 402 \"Payment Required\"   - This is returned when you are attempting to perform an action that would push your account above a usage limit. You can view your usage at: https://app.contentgroove.com/quota_usage - 404 \"Not Found\"   - This is returned when the resource you are trying to view does not exist - 429 \"Too Many Requests\"   - This is returned when you have performed too many requests within a given period of time - 500 \"Internal Server Error\"   - This is returned when your request was valid but there was a problem on our end  # File Uploading  - Step 1: Make a GET request to the direct uploads URL endpoint (/api/v1/direct_uploads) to receive an upload URL to upload the file to and an upload id. - Step 2: Make a PUT request with the file as the body to the upload URL received in step 1. The response will have a 200 status with no body if the upload is successful.   ```   curl -T /path/to/file upload_url   ``` - Step 3: After uploading the file to the upload URL, make a POST request to the create medias endpoint (/api/v1/medias), with the upload id and optionally a name and description for the new media.   > At this time, file uploads are limited to 5gb per file.  # Allowed media types  Video:  - Supported: Most common video formats and codecs are supported. - Recommended: mp4  Audio:  - Supported: aac, mp3, flac, ogg, wav, and wma - Recommended: aac  # Authentication  You can use the API Key to authenticate your API requests using any of these methods. (Replace abc123 with your actual API Key.)  - Request header `Authorization: Bearer abc123` - Request header `X-API-KEY: abc123` - Query parameter `api_key=abc123`   > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️  # Link to openapi.json spec  - https://api.contentgroove.com/api-docs/v1/openapi.json 
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDefaultApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIDefaultApi::OAIDefaultApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIDefaultApi::~OAIDefaultApi() {
}

void OAIDefaultApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.contentgroove.com/api/v1"),
    "V1 API server",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("createClip", defaultConf);
    _serverIndices.insert("createClip", 0);
    _serverConfigs.insert("createMedia", defaultConf);
    _serverIndices.insert("createMedia", 0);
    _serverConfigs.insert("createWebhookSubscription", defaultConf);
    _serverIndices.insert("createWebhookSubscription", 0);
    _serverConfigs.insert("deleteClipById", defaultConf);
    _serverIndices.insert("deleteClipById", 0);
    _serverConfigs.insert("deleteMediaById", defaultConf);
    _serverIndices.insert("deleteMediaById", 0);
    _serverConfigs.insert("deleteWebhookSubscriptionById", defaultConf);
    _serverIndices.insert("deleteWebhookSubscriptionById", 0);
    _serverConfigs.insert("getClipById", defaultConf);
    _serverIndices.insert("getClipById", 0);
    _serverConfigs.insert("getClips", defaultConf);
    _serverIndices.insert("getClips", 0);
    _serverConfigs.insert("getMediaById", defaultConf);
    _serverIndices.insert("getMediaById", 0);
    _serverConfigs.insert("getMedias", defaultConf);
    _serverIndices.insert("getMedias", 0);
    _serverConfigs.insert("getUploadUrl", defaultConf);
    _serverIndices.insert("getUploadUrl", 0);
    _serverConfigs.insert("getWebhookSubscriptionById", defaultConf);
    _serverIndices.insert("getWebhookSubscriptionById", 0);
    _serverConfigs.insert("getWebhookSubscriptions", defaultConf);
    _serverIndices.insert("getWebhookSubscriptions", 0);
    _serverConfigs.insert("updateClipById", defaultConf);
    _serverIndices.insert("updateClipById", 0);
    _serverConfigs.insert("updateMediaById", defaultConf);
    _serverIndices.insert("updateMediaById", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIDefaultApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIDefaultApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIDefaultApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIDefaultApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIDefaultApi::setUsername(const QString &username) {
    _username = username;
}

void OAIDefaultApi::setPassword(const QString &password) {
    _password = password;
}


void OAIDefaultApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIDefaultApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIDefaultApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIDefaultApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIDefaultApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIDefaultApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIDefaultApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIDefaultApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIDefaultApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIDefaultApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIDefaultApi::getParamStylePrefix(const QString &style) {
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

QString OAIDefaultApi::getParamStyleSuffix(const QString &style) {
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

QString OAIDefaultApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIDefaultApi::createClip(const OAICreateClip_request &oai_create_clip_request) {
    QString fullPath = QString(_serverConfigs["createClip"][_serverIndices.value("createClip")].URL()+"/clips");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_clip_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createClipCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createClipCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIClip_response_object output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createClipSignal(output);
        Q_EMIT createClipSignalFull(worker, output);
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

        Q_EMIT createClipSignalE(output, error_type, error_str);
        Q_EMIT createClipSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createClipSignalError(output, error_type, error_str);
        Q_EMIT createClipSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createMedia(const OAICreateMedia_request &oai_create_media_request) {
    QString fullPath = QString(_serverConfigs["createMedia"][_serverIndices.value("createMedia")].URL()+"/medias");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_media_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createMediaCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createMediaCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIMedia_response_object output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createMediaSignal(output);
        Q_EMIT createMediaSignalFull(worker, output);
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

        Q_EMIT createMediaSignalE(output, error_type, error_str);
        Q_EMIT createMediaSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createMediaSignalError(output, error_type, error_str);
        Q_EMIT createMediaSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createWebhookSubscription(const OAICreateWebhookSubscription_request &oai_create_webhook_subscription_request) {
    QString fullPath = QString(_serverConfigs["createWebhookSubscription"][_serverIndices.value("createWebhookSubscription")].URL()+"/webhook_subscriptions");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_webhook_subscription_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createWebhookSubscriptionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createWebhookSubscriptionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIWebhook_subscription_response_object output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createWebhookSubscriptionSignal(output);
        Q_EMIT createWebhookSubscriptionSignalFull(worker, output);
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

        Q_EMIT createWebhookSubscriptionSignalE(output, error_type, error_str);
        Q_EMIT createWebhookSubscriptionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createWebhookSubscriptionSignalError(output, error_type, error_str);
        Q_EMIT createWebhookSubscriptionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteClipById(const QString &id) {
    QString fullPath = QString(_serverConfigs["deleteClipById"][_serverIndices.value("deleteClipById")].URL()+"/clips/{id}");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
    }
    
    
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


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteClipByIdCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteClipByIdCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteClipByIdSignal();
        Q_EMIT deleteClipByIdSignalFull(worker);
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

        Q_EMIT deleteClipByIdSignalE(error_type, error_str);
        Q_EMIT deleteClipByIdSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteClipByIdSignalError(error_type, error_str);
        Q_EMIT deleteClipByIdSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteMediaById(const QString &id) {
    QString fullPath = QString(_serverConfigs["deleteMediaById"][_serverIndices.value("deleteMediaById")].URL()+"/medias/{id}");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
    }
    
    
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


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteMediaByIdCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteMediaByIdCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteMediaByIdSignal();
        Q_EMIT deleteMediaByIdSignalFull(worker);
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

        Q_EMIT deleteMediaByIdSignalE(error_type, error_str);
        Q_EMIT deleteMediaByIdSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteMediaByIdSignalError(error_type, error_str);
        Q_EMIT deleteMediaByIdSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteWebhookSubscriptionById(const QString &id) {
    QString fullPath = QString(_serverConfigs["deleteWebhookSubscriptionById"][_serverIndices.value("deleteWebhookSubscriptionById")].URL()+"/webhook_subscriptions/{id}");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
    }
    
    
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


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteWebhookSubscriptionByIdCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteWebhookSubscriptionByIdCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteWebhookSubscriptionByIdSignal();
        Q_EMIT deleteWebhookSubscriptionByIdSignalFull(worker);
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

        Q_EMIT deleteWebhookSubscriptionByIdSignalE(error_type, error_str);
        Q_EMIT deleteWebhookSubscriptionByIdSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteWebhookSubscriptionByIdSignalError(error_type, error_str);
        Q_EMIT deleteWebhookSubscriptionByIdSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getClipById(const QString &id) {
    QString fullPath = QString(_serverConfigs["getClipById"][_serverIndices.value("getClipById")].URL()+"/clips/{id}");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
    }
    
    
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


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getClipByIdCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getClipByIdCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIClip_response_object output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getClipByIdSignal(output);
        Q_EMIT getClipByIdSignalFull(worker, output);
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

        Q_EMIT getClipByIdSignalE(output, error_type, error_str);
        Q_EMIT getClipByIdSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getClipByIdSignalError(output, error_type, error_str);
        Q_EMIT getClipByIdSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getClips(const ::OpenAPI::OptionalParam<OAIObject> &filter, const ::OpenAPI::OptionalParam<OAIObject> &page, const ::OpenAPI::OptionalParam<QString> &sort) {
    QString fullPath = QString(_serverConfigs["getClips"][_serverIndices.value("getClips")].URL()+"/clips");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
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
    if (page.hasValue())
    {
        queryStyle = "deepObject";
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
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("sort")).append(querySuffix).append(QUrl::toPercentEncoding(sort.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getClipsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getClipsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIClips_response_object output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getClipsSignal(output);
        Q_EMIT getClipsSignalFull(worker, output);
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

        Q_EMIT getClipsSignalE(output, error_type, error_str);
        Q_EMIT getClipsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getClipsSignalError(output, error_type, error_str);
        Q_EMIT getClipsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getMediaById(const QString &id) {
    QString fullPath = QString(_serverConfigs["getMediaById"][_serverIndices.value("getMediaById")].URL()+"/medias/{id}");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
    }
    
    
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


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getMediaByIdCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getMediaByIdCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIMedia_response_object output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getMediaByIdSignal(output);
        Q_EMIT getMediaByIdSignalFull(worker, output);
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

        Q_EMIT getMediaByIdSignalE(output, error_type, error_str);
        Q_EMIT getMediaByIdSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getMediaByIdSignalError(output, error_type, error_str);
        Q_EMIT getMediaByIdSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getMedias(const ::OpenAPI::OptionalParam<OAIObject> &filter, const ::OpenAPI::OptionalParam<OAIObject> &page, const ::OpenAPI::OptionalParam<QString> &sort) {
    QString fullPath = QString(_serverConfigs["getMedias"][_serverIndices.value("getMedias")].URL()+"/medias");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
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
    if (page.hasValue())
    {
        queryStyle = "deepObject";
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
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("sort")).append(querySuffix).append(QUrl::toPercentEncoding(sort.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getMediasCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getMediasCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIMedias_response_object output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getMediasSignal(output);
        Q_EMIT getMediasSignalFull(worker, output);
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

        Q_EMIT getMediasSignalE(output, error_type, error_str);
        Q_EMIT getMediasSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getMediasSignalError(output, error_type, error_str);
        Q_EMIT getMediasSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getUploadUrl() {
    QString fullPath = QString(_serverConfigs["getUploadUrl"][_serverIndices.value("getUploadUrl")].URL()+"/direct_uploads");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getUploadUrlCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getUploadUrlCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDirect_upload_response_object output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getUploadUrlSignal(output);
        Q_EMIT getUploadUrlSignalFull(worker, output);
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

        Q_EMIT getUploadUrlSignalE(output, error_type, error_str);
        Q_EMIT getUploadUrlSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getUploadUrlSignalError(output, error_type, error_str);
        Q_EMIT getUploadUrlSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getWebhookSubscriptionById(const QString &id) {
    QString fullPath = QString(_serverConfigs["getWebhookSubscriptionById"][_serverIndices.value("getWebhookSubscriptionById")].URL()+"/webhook_subscriptions/{id}");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
    }
    
    
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


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getWebhookSubscriptionByIdCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getWebhookSubscriptionByIdCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIWebhook_subscription_response_object output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getWebhookSubscriptionByIdSignal(output);
        Q_EMIT getWebhookSubscriptionByIdSignalFull(worker, output);
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

        Q_EMIT getWebhookSubscriptionByIdSignalE(output, error_type, error_str);
        Q_EMIT getWebhookSubscriptionByIdSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getWebhookSubscriptionByIdSignalError(output, error_type, error_str);
        Q_EMIT getWebhookSubscriptionByIdSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getWebhookSubscriptions(const ::OpenAPI::OptionalParam<OAIObject> &filter, const ::OpenAPI::OptionalParam<QString> &sort) {
    QString fullPath = QString(_serverConfigs["getWebhookSubscriptions"][_serverIndices.value("getWebhookSubscriptions")].URL()+"/webhook_subscriptions");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
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
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("sort")).append(querySuffix).append(QUrl::toPercentEncoding(sort.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getWebhookSubscriptionsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getWebhookSubscriptionsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIWebhook_subscriptions_response_object output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getWebhookSubscriptionsSignal(output);
        Q_EMIT getWebhookSubscriptionsSignalFull(worker, output);
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

        Q_EMIT getWebhookSubscriptionsSignalE(output, error_type, error_str);
        Q_EMIT getWebhookSubscriptionsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getWebhookSubscriptionsSignalError(output, error_type, error_str);
        Q_EMIT getWebhookSubscriptionsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateClipById(const QString &id, const OAIUpdateClipById_request &oai_update_clip_by_id_request) {
    QString fullPath = QString(_serverConfigs["updateClipById"][_serverIndices.value("updateClipById")].URL()+"/clips/{id}");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
    }
    
    
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

        
        QByteArray output = oai_update_clip_by_id_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateClipByIdCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateClipByIdCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIClip_response_object output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateClipByIdSignal(output);
        Q_EMIT updateClipByIdSignalFull(worker, output);
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

        Q_EMIT updateClipByIdSignalE(output, error_type, error_str);
        Q_EMIT updateClipByIdSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateClipByIdSignalError(output, error_type, error_str);
        Q_EMIT updateClipByIdSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateMediaById(const QString &id, const OAIUpdateMediaById_request &oai_update_media_by_id_request) {
    QString fullPath = QString(_serverConfigs["updateMediaById"][_serverIndices.value("updateMediaById")].URL()+"/medias/{id}");
    
    if (_apiKeys.contains("BearerHeader")) {
        addHeaders("BearerHeader",_apiKeys.find("BearerHeader").value());
    }
    
    
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

        
        QByteArray output = oai_update_media_by_id_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateMediaByIdCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateMediaByIdCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIMedia_response_object output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateMediaByIdSignal(output);
        Q_EMIT updateMediaByIdSignalFull(worker, output);
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

        Q_EMIT updateMediaByIdSignalE(output, error_type, error_str);
        Q_EMIT updateMediaByIdSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateMediaByIdSignalError(output, error_type, error_str);
        Q_EMIT updateMediaByIdSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::tokenAvailable(){

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
