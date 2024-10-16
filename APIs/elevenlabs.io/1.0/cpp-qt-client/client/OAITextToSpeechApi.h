/**
 * ElevenLabs API Documentation
 * This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAITextToSpeechApi_H
#define OAI_OAITextToSpeechApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBody_Text_to_speech_v1_text_to_speech__voice_id__post.h"
#include "OAIBody_Text_to_speech_v1_text_to_speech__voice_id__stream_post.h"
#include "OAIHTTPValidationError.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAITextToSpeechApi : public QObject {
    Q_OBJECT

public:
    OAITextToSpeechApi(const int timeOut = 0);
    ~OAITextToSpeechApi();

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
    * @param[in]  voice_id QString [required]
    * @param[in]  oai_body_text_to_speech_v1_text_to_speech__voice_id__post OAIBody_Text_to_speech_v1_text_to_speech__voice_id__post [required]
    * @param[in]  xi_api_key QString [optional]
    */
    virtual void textToSpeechV1TextToSpeechVoiceIdPost(const QString &voice_id, const OAIBody_Text_to_speech_v1_text_to_speech__voice_id__post &oai_body_text_to_speech_v1_text_to_speech__voice_id__post, const ::OpenAPI::OptionalParam<QString> &xi_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  voice_id QString [required]
    * @param[in]  oai_body_text_to_speech_v1_text_to_speech__voice_id__stream_post OAIBody_Text_to_speech_v1_text_to_speech__voice_id__stream_post [required]
    * @param[in]  xi_api_key QString [optional]
    */
    virtual void textToSpeechV1TextToSpeechVoiceIdStreamPost(const QString &voice_id, const OAIBody_Text_to_speech_v1_text_to_speech__voice_id__stream_post &oai_body_text_to_speech_v1_text_to_speech__voice_id__stream_post, const ::OpenAPI::OptionalParam<QString> &xi_api_key = ::OpenAPI::OptionalParam<QString>());


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

    void textToSpeechV1TextToSpeechVoiceIdPostCallback(OAIHttpRequestWorker *worker);
    void textToSpeechV1TextToSpeechVoiceIdStreamPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void textToSpeechV1TextToSpeechVoiceIdPostSignal();
    void textToSpeechV1TextToSpeechVoiceIdStreamPostSignal();


    void textToSpeechV1TextToSpeechVoiceIdPostSignalFull(OAIHttpRequestWorker *worker);
    void textToSpeechV1TextToSpeechVoiceIdStreamPostSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use textToSpeechV1TextToSpeechVoiceIdPostSignalError() instead")
    void textToSpeechV1TextToSpeechVoiceIdPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void textToSpeechV1TextToSpeechVoiceIdPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use textToSpeechV1TextToSpeechVoiceIdStreamPostSignalError() instead")
    void textToSpeechV1TextToSpeechVoiceIdStreamPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void textToSpeechV1TextToSpeechVoiceIdStreamPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use textToSpeechV1TextToSpeechVoiceIdPostSignalErrorFull() instead")
    void textToSpeechV1TextToSpeechVoiceIdPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void textToSpeechV1TextToSpeechVoiceIdPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use textToSpeechV1TextToSpeechVoiceIdStreamPostSignalErrorFull() instead")
    void textToSpeechV1TextToSpeechVoiceIdStreamPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void textToSpeechV1TextToSpeechVoiceIdStreamPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
