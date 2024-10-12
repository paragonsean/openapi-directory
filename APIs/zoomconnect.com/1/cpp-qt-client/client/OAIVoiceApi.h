/**
 * www.zoomconnect.com
 * The world's greatest SMS API
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIVoiceApi_H
#define OAI_OAIVoiceApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIHttpFileElement.h"
#include "OAIWebServiceSendVoiceMessageResponse.h"
#include "OAIWebServiceVoiceMessage.h"
#include "OAIWebServiceVoiceMessageSendSingleTextRequest.h"
#include "OAIWebServiceVoiceMessages.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIVoiceApi : public QObject {
    Q_OBJECT

public:
    OAIVoiceApi(const int timeOut = 0);
    ~OAIVoiceApi();

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
    * @param[in]  page_size qint32 [optional]
    * @param[in]  page qint32 [optional]
    * @param[in]  status QString [optional]
    * @param[in]  from_date_time_sent QDateTime [optional]
    * @param[in]  to_date_time_sent QDateTime [optional]
    * @param[in]  to_number QString [optional]
    * @param[in]  message QString [optional]
    * @param[in]  campaign QString [optional]
    * @param[in]  data_field QString [optional]
    * @param[in]  deleted bool [optional]
    */
    virtual void apiRestV1VoiceAllGet(const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QDateTime> &from_date_time_sent = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &to_date_time_sent = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QString> &to_number = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &message = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &campaign = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &data_field = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &deleted = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  message_id QString [required]
    */
    virtual void apiRestV1VoiceMessageIdDelete(const QString &message_id);

    /**
    * @param[in]  message_id QString [required]
    */
    virtual void apiRestV1VoiceMessageIdGet(const QString &message_id);

    /**
    * @param[in]  recipient_number QString [required]
    * @param[in]  file OAIHttpFileElement [required]
    * @param[in]  campaign QString [optional]
    * @param[in]  data_field QString [optional]
    * @param[in]  retry_count qint32 [optional]
    * @param[in]  retry_minimum_interval qint32 [optional]
    * @param[in]  retry_maximum_interval qint32 [optional]
    */
    virtual void singleAudio(const QString &recipient_number, const OAIHttpFileElement &file, const ::OpenAPI::OptionalParam<QString> &campaign = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &data_field = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &retry_count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &retry_minimum_interval = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &retry_maximum_interval = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  body OAIWebServiceVoiceMessageSendSingleTextRequest [optional]
    */
    virtual void singleText(const ::OpenAPI::OptionalParam<OAIWebServiceVoiceMessageSendSingleTextRequest> &body = ::OpenAPI::OptionalParam<OAIWebServiceVoiceMessageSendSingleTextRequest>());


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

    void apiRestV1VoiceAllGetCallback(OAIHttpRequestWorker *worker);
    void apiRestV1VoiceMessageIdDeleteCallback(OAIHttpRequestWorker *worker);
    void apiRestV1VoiceMessageIdGetCallback(OAIHttpRequestWorker *worker);
    void singleAudioCallback(OAIHttpRequestWorker *worker);
    void singleTextCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void apiRestV1VoiceAllGetSignal(OAIWebServiceVoiceMessages summary);
    void apiRestV1VoiceMessageIdDeleteSignal();
    void apiRestV1VoiceMessageIdGetSignal(OAIWebServiceVoiceMessage summary);
    void singleAudioSignal(OAIWebServiceSendVoiceMessageResponse summary);
    void singleTextSignal(OAIWebServiceSendVoiceMessageResponse summary);


    void apiRestV1VoiceAllGetSignalFull(OAIHttpRequestWorker *worker, OAIWebServiceVoiceMessages summary);
    void apiRestV1VoiceMessageIdDeleteSignalFull(OAIHttpRequestWorker *worker);
    void apiRestV1VoiceMessageIdGetSignalFull(OAIHttpRequestWorker *worker, OAIWebServiceVoiceMessage summary);
    void singleAudioSignalFull(OAIHttpRequestWorker *worker, OAIWebServiceSendVoiceMessageResponse summary);
    void singleTextSignalFull(OAIHttpRequestWorker *worker, OAIWebServiceSendVoiceMessageResponse summary);

    Q_DECL_DEPRECATED_X("Use apiRestV1VoiceAllGetSignalError() instead")
    void apiRestV1VoiceAllGetSignalE(OAIWebServiceVoiceMessages summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiRestV1VoiceAllGetSignalError(OAIWebServiceVoiceMessages summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiRestV1VoiceMessageIdDeleteSignalError() instead")
    void apiRestV1VoiceMessageIdDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiRestV1VoiceMessageIdDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiRestV1VoiceMessageIdGetSignalError() instead")
    void apiRestV1VoiceMessageIdGetSignalE(OAIWebServiceVoiceMessage summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiRestV1VoiceMessageIdGetSignalError(OAIWebServiceVoiceMessage summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use singleAudioSignalError() instead")
    void singleAudioSignalE(OAIWebServiceSendVoiceMessageResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void singleAudioSignalError(OAIWebServiceSendVoiceMessageResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use singleTextSignalError() instead")
    void singleTextSignalE(OAIWebServiceSendVoiceMessageResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void singleTextSignalError(OAIWebServiceSendVoiceMessageResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use apiRestV1VoiceAllGetSignalErrorFull() instead")
    void apiRestV1VoiceAllGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiRestV1VoiceAllGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiRestV1VoiceMessageIdDeleteSignalErrorFull() instead")
    void apiRestV1VoiceMessageIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiRestV1VoiceMessageIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiRestV1VoiceMessageIdGetSignalErrorFull() instead")
    void apiRestV1VoiceMessageIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiRestV1VoiceMessageIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use singleAudioSignalErrorFull() instead")
    void singleAudioSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void singleAudioSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use singleTextSignalErrorFull() instead")
    void singleTextSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void singleTextSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
