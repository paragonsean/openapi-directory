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

#ifndef OAI_OAIDefaultApi_H
#define OAI_OAIDefaultApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIClip_response_object.h"
#include "OAIClips_response_object.h"
#include "OAICreateClip_request.h"
#include "OAICreateMedia_request.h"
#include "OAICreateWebhookSubscription_request.h"
#include "OAIDirect_upload_response_object.h"
#include "OAIMedia_response_object.h"
#include "OAIMedias_response_object.h"
#include "OAIPayment_required_error_response_object.h"
#include "OAIToo_many_requests_error_response_object.h"
#include "OAIUnauthorized_error_response_object.h"
#include "OAIUpdateClipById_request.h"
#include "OAIUpdateMediaById_request.h"
#include "OAIWebhook_subscription_response_object.h"
#include "OAIWebhook_subscriptions_response_object.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDefaultApi : public QObject {
    Q_OBJECT

public:
    OAIDefaultApi(const int timeOut = 0);
    ~OAIDefaultApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  oai_create_clip_request OAICreateClip_request [required]
    */
    virtual void createClip(const OAICreateClip_request &oai_create_clip_request);

    /**
    * @param[in]  oai_create_media_request OAICreateMedia_request [required]
    */
    virtual void createMedia(const OAICreateMedia_request &oai_create_media_request);

    /**
    * @param[in]  oai_create_webhook_subscription_request OAICreateWebhookSubscription_request [required]
    */
    virtual void createWebhookSubscription(const OAICreateWebhookSubscription_request &oai_create_webhook_subscription_request);

    /**
    * @param[in]  id QString [required]
    */
    virtual void deleteClipById(const QString &id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void deleteMediaById(const QString &id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void deleteWebhookSubscriptionById(const QString &id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void getClipById(const QString &id);

    /**
    * @param[in]  filter OAIObject [optional]
    * @param[in]  page OAIObject [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void getClips(const ::OpenAPI::OptionalParam<OAIObject> &filter = ::OpenAPI::OptionalParam<OAIObject>(), const ::OpenAPI::OptionalParam<OAIObject> &page = ::OpenAPI::OptionalParam<OAIObject>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void getMediaById(const QString &id);

    /**
    * @param[in]  filter OAIObject [optional]
    * @param[in]  page OAIObject [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void getMedias(const ::OpenAPI::OptionalParam<OAIObject> &filter = ::OpenAPI::OptionalParam<OAIObject>(), const ::OpenAPI::OptionalParam<OAIObject> &page = ::OpenAPI::OptionalParam<OAIObject>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());


    virtual void getUploadUrl();

    /**
    * @param[in]  id QString [required]
    */
    virtual void getWebhookSubscriptionById(const QString &id);

    /**
    * @param[in]  filter OAIObject [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void getWebhookSubscriptions(const ::OpenAPI::OptionalParam<OAIObject> &filter = ::OpenAPI::OptionalParam<OAIObject>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_update_clip_by_id_request OAIUpdateClipById_request [required]
    */
    virtual void updateClipById(const QString &id, const OAIUpdateClipById_request &oai_update_clip_by_id_request);

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_update_media_by_id_request OAIUpdateMediaById_request [required]
    */
    virtual void updateMediaById(const QString &id, const OAIUpdateMediaById_request &oai_update_media_by_id_request);


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void createClipCallback(OAIHttpRequestWorker *worker);
    void createMediaCallback(OAIHttpRequestWorker *worker);
    void createWebhookSubscriptionCallback(OAIHttpRequestWorker *worker);
    void deleteClipByIdCallback(OAIHttpRequestWorker *worker);
    void deleteMediaByIdCallback(OAIHttpRequestWorker *worker);
    void deleteWebhookSubscriptionByIdCallback(OAIHttpRequestWorker *worker);
    void getClipByIdCallback(OAIHttpRequestWorker *worker);
    void getClipsCallback(OAIHttpRequestWorker *worker);
    void getMediaByIdCallback(OAIHttpRequestWorker *worker);
    void getMediasCallback(OAIHttpRequestWorker *worker);
    void getUploadUrlCallback(OAIHttpRequestWorker *worker);
    void getWebhookSubscriptionByIdCallback(OAIHttpRequestWorker *worker);
    void getWebhookSubscriptionsCallback(OAIHttpRequestWorker *worker);
    void updateClipByIdCallback(OAIHttpRequestWorker *worker);
    void updateMediaByIdCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void createClipSignal(OAIClip_response_object summary);
    void createMediaSignal(OAIMedia_response_object summary);
    void createWebhookSubscriptionSignal(OAIWebhook_subscription_response_object summary);
    void deleteClipByIdSignal();
    void deleteMediaByIdSignal();
    void deleteWebhookSubscriptionByIdSignal();
    void getClipByIdSignal(OAIClip_response_object summary);
    void getClipsSignal(OAIClips_response_object summary);
    void getMediaByIdSignal(OAIMedia_response_object summary);
    void getMediasSignal(OAIMedias_response_object summary);
    void getUploadUrlSignal(OAIDirect_upload_response_object summary);
    void getWebhookSubscriptionByIdSignal(OAIWebhook_subscription_response_object summary);
    void getWebhookSubscriptionsSignal(OAIWebhook_subscriptions_response_object summary);
    void updateClipByIdSignal(OAIClip_response_object summary);
    void updateMediaByIdSignal(OAIMedia_response_object summary);


    void createClipSignalFull(OAIHttpRequestWorker *worker, OAIClip_response_object summary);
    void createMediaSignalFull(OAIHttpRequestWorker *worker, OAIMedia_response_object summary);
    void createWebhookSubscriptionSignalFull(OAIHttpRequestWorker *worker, OAIWebhook_subscription_response_object summary);
    void deleteClipByIdSignalFull(OAIHttpRequestWorker *worker);
    void deleteMediaByIdSignalFull(OAIHttpRequestWorker *worker);
    void deleteWebhookSubscriptionByIdSignalFull(OAIHttpRequestWorker *worker);
    void getClipByIdSignalFull(OAIHttpRequestWorker *worker, OAIClip_response_object summary);
    void getClipsSignalFull(OAIHttpRequestWorker *worker, OAIClips_response_object summary);
    void getMediaByIdSignalFull(OAIHttpRequestWorker *worker, OAIMedia_response_object summary);
    void getMediasSignalFull(OAIHttpRequestWorker *worker, OAIMedias_response_object summary);
    void getUploadUrlSignalFull(OAIHttpRequestWorker *worker, OAIDirect_upload_response_object summary);
    void getWebhookSubscriptionByIdSignalFull(OAIHttpRequestWorker *worker, OAIWebhook_subscription_response_object summary);
    void getWebhookSubscriptionsSignalFull(OAIHttpRequestWorker *worker, OAIWebhook_subscriptions_response_object summary);
    void updateClipByIdSignalFull(OAIHttpRequestWorker *worker, OAIClip_response_object summary);
    void updateMediaByIdSignalFull(OAIHttpRequestWorker *worker, OAIMedia_response_object summary);

    Q_DECL_DEPRECATED_X("Use createClipSignalError() instead")
    void createClipSignalE(OAIClip_response_object summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createClipSignalError(OAIClip_response_object summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createMediaSignalError() instead")
    void createMediaSignalE(OAIMedia_response_object summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createMediaSignalError(OAIMedia_response_object summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createWebhookSubscriptionSignalError() instead")
    void createWebhookSubscriptionSignalE(OAIWebhook_subscription_response_object summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createWebhookSubscriptionSignalError(OAIWebhook_subscription_response_object summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteClipByIdSignalError() instead")
    void deleteClipByIdSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteClipByIdSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteMediaByIdSignalError() instead")
    void deleteMediaByIdSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteMediaByIdSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteWebhookSubscriptionByIdSignalError() instead")
    void deleteWebhookSubscriptionByIdSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteWebhookSubscriptionByIdSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getClipByIdSignalError() instead")
    void getClipByIdSignalE(OAIClip_response_object summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getClipByIdSignalError(OAIClip_response_object summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getClipsSignalError() instead")
    void getClipsSignalE(OAIClips_response_object summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getClipsSignalError(OAIClips_response_object summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMediaByIdSignalError() instead")
    void getMediaByIdSignalE(OAIMedia_response_object summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMediaByIdSignalError(OAIMedia_response_object summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMediasSignalError() instead")
    void getMediasSignalE(OAIMedias_response_object summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMediasSignalError(OAIMedias_response_object summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUploadUrlSignalError() instead")
    void getUploadUrlSignalE(OAIDirect_upload_response_object summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getUploadUrlSignalError(OAIDirect_upload_response_object summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getWebhookSubscriptionByIdSignalError() instead")
    void getWebhookSubscriptionByIdSignalE(OAIWebhook_subscription_response_object summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getWebhookSubscriptionByIdSignalError(OAIWebhook_subscription_response_object summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getWebhookSubscriptionsSignalError() instead")
    void getWebhookSubscriptionsSignalE(OAIWebhook_subscriptions_response_object summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getWebhookSubscriptionsSignalError(OAIWebhook_subscriptions_response_object summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateClipByIdSignalError() instead")
    void updateClipByIdSignalE(OAIClip_response_object summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateClipByIdSignalError(OAIClip_response_object summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateMediaByIdSignalError() instead")
    void updateMediaByIdSignalE(OAIMedia_response_object summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateMediaByIdSignalError(OAIMedia_response_object summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use createClipSignalErrorFull() instead")
    void createClipSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createClipSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createMediaSignalErrorFull() instead")
    void createMediaSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createMediaSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createWebhookSubscriptionSignalErrorFull() instead")
    void createWebhookSubscriptionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createWebhookSubscriptionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteClipByIdSignalErrorFull() instead")
    void deleteClipByIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteClipByIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteMediaByIdSignalErrorFull() instead")
    void deleteMediaByIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteMediaByIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteWebhookSubscriptionByIdSignalErrorFull() instead")
    void deleteWebhookSubscriptionByIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteWebhookSubscriptionByIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getClipByIdSignalErrorFull() instead")
    void getClipByIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getClipByIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getClipsSignalErrorFull() instead")
    void getClipsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getClipsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMediaByIdSignalErrorFull() instead")
    void getMediaByIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMediaByIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMediasSignalErrorFull() instead")
    void getMediasSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMediasSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUploadUrlSignalErrorFull() instead")
    void getUploadUrlSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getUploadUrlSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getWebhookSubscriptionByIdSignalErrorFull() instead")
    void getWebhookSubscriptionByIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getWebhookSubscriptionByIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getWebhookSubscriptionsSignalErrorFull() instead")
    void getWebhookSubscriptionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getWebhookSubscriptionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateClipByIdSignalErrorFull() instead")
    void updateClipByIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateClipByIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateMediaByIdSignalErrorFull() instead")
    void updateMediaByIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateMediaByIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
