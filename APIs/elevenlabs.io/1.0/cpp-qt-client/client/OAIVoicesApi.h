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

#ifndef OAI_OAIVoicesApi_H
#define OAI_OAIVoicesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAddVoiceResponseModel.h"
#include "OAIGetVoicesResponseModel.h"
#include "OAIHTTPValidationError.h"
#include "OAIHttpFileElement.h"
#include "OAIVoiceResponseModel.h"
#include "OAIVoiceSettingsResponseModel.h"
#include <QJsonValue>
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIVoicesApi : public QObject {
    Q_OBJECT

public:
    OAIVoicesApi(const int timeOut = 0);
    ~OAIVoicesApi();

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
    * @param[in]  files QList<OAIHttpFileElement> [required]
    * @param[in]  name QString [required]
    * @param[in]  xi_api_key QString [optional]
    * @param[in]  description QString [optional]
    * @param[in]  labels QString [optional]
    */
    virtual void addVoiceV1VoicesAddPost(const QList<OAIHttpFileElement> &files, const QString &name, const ::OpenAPI::OptionalParam<QString> &xi_api_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &description = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &labels = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  voice_id QString [required]
    * @param[in]  xi_api_key QString [optional]
    */
    virtual void deleteVoiceV1VoicesVoiceIdDelete(const QString &voice_id, const ::OpenAPI::OptionalParam<QString> &xi_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  voice_id QString [required]
    * @param[in]  oai_voice_settings_response_model OAIVoiceSettingsResponseModel [required]
    * @param[in]  xi_api_key QString [optional]
    */
    virtual void editVoiceSettingsV1VoicesVoiceIdSettingsEditPost(const QString &voice_id, const OAIVoiceSettingsResponseModel &oai_voice_settings_response_model, const ::OpenAPI::OptionalParam<QString> &xi_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  voice_id QString [required]
    * @param[in]  name QString [required]
    * @param[in]  xi_api_key QString [optional]
    * @param[in]  description QString [optional]
    * @param[in]  files QList<OAIHttpFileElement> [optional]
    * @param[in]  labels QString [optional]
    */
    virtual void editVoiceV1VoicesVoiceIdEditPost(const QString &voice_id, const QString &name, const ::OpenAPI::OptionalParam<QString> &xi_api_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &description = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<OAIHttpFileElement>> &files = ::OpenAPI::OptionalParam<QList<OAIHttpFileElement>>(), const ::OpenAPI::OptionalParam<QString> &labels = ::OpenAPI::OptionalParam<QString>());


    virtual void getDefaultVoiceSettingsV1VoicesSettingsDefaultGet();

    /**
    * @param[in]  voice_id QString [required]
    * @param[in]  xi_api_key QString [optional]
    */
    virtual void getVoiceSettingsV1VoicesVoiceIdSettingsGet(const QString &voice_id, const ::OpenAPI::OptionalParam<QString> &xi_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  voice_id QString [required]
    * @param[in]  with_settings bool [optional]
    * @param[in]  xi_api_key QString [optional]
    */
    virtual void getVoiceV1VoicesVoiceIdGet(const QString &voice_id, const ::OpenAPI::OptionalParam<bool> &with_settings = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &xi_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  xi_api_key QString [optional]
    */
    virtual void getVoicesV1VoicesGet(const ::OpenAPI::OptionalParam<QString> &xi_api_key = ::OpenAPI::OptionalParam<QString>());


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

    void addVoiceV1VoicesAddPostCallback(OAIHttpRequestWorker *worker);
    void deleteVoiceV1VoicesVoiceIdDeleteCallback(OAIHttpRequestWorker *worker);
    void editVoiceSettingsV1VoicesVoiceIdSettingsEditPostCallback(OAIHttpRequestWorker *worker);
    void editVoiceV1VoicesVoiceIdEditPostCallback(OAIHttpRequestWorker *worker);
    void getDefaultVoiceSettingsV1VoicesSettingsDefaultGetCallback(OAIHttpRequestWorker *worker);
    void getVoiceSettingsV1VoicesVoiceIdSettingsGetCallback(OAIHttpRequestWorker *worker);
    void getVoiceV1VoicesVoiceIdGetCallback(OAIHttpRequestWorker *worker);
    void getVoicesV1VoicesGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void addVoiceV1VoicesAddPostSignal(OAIAddVoiceResponseModel summary);
    void deleteVoiceV1VoicesVoiceIdDeleteSignal(QJsonValue summary);
    void editVoiceSettingsV1VoicesVoiceIdSettingsEditPostSignal(QJsonValue summary);
    void editVoiceV1VoicesVoiceIdEditPostSignal(QJsonValue summary);
    void getDefaultVoiceSettingsV1VoicesSettingsDefaultGetSignal(OAIVoiceSettingsResponseModel summary);
    void getVoiceSettingsV1VoicesVoiceIdSettingsGetSignal(OAIVoiceSettingsResponseModel summary);
    void getVoiceV1VoicesVoiceIdGetSignal(OAIVoiceResponseModel summary);
    void getVoicesV1VoicesGetSignal(OAIGetVoicesResponseModel summary);


    void addVoiceV1VoicesAddPostSignalFull(OAIHttpRequestWorker *worker, OAIAddVoiceResponseModel summary);
    void deleteVoiceV1VoicesVoiceIdDeleteSignalFull(OAIHttpRequestWorker *worker, QJsonValue summary);
    void editVoiceSettingsV1VoicesVoiceIdSettingsEditPostSignalFull(OAIHttpRequestWorker *worker, QJsonValue summary);
    void editVoiceV1VoicesVoiceIdEditPostSignalFull(OAIHttpRequestWorker *worker, QJsonValue summary);
    void getDefaultVoiceSettingsV1VoicesSettingsDefaultGetSignalFull(OAIHttpRequestWorker *worker, OAIVoiceSettingsResponseModel summary);
    void getVoiceSettingsV1VoicesVoiceIdSettingsGetSignalFull(OAIHttpRequestWorker *worker, OAIVoiceSettingsResponseModel summary);
    void getVoiceV1VoicesVoiceIdGetSignalFull(OAIHttpRequestWorker *worker, OAIVoiceResponseModel summary);
    void getVoicesV1VoicesGetSignalFull(OAIHttpRequestWorker *worker, OAIGetVoicesResponseModel summary);

    Q_DECL_DEPRECATED_X("Use addVoiceV1VoicesAddPostSignalError() instead")
    void addVoiceV1VoicesAddPostSignalE(OAIAddVoiceResponseModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addVoiceV1VoicesAddPostSignalError(OAIAddVoiceResponseModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteVoiceV1VoicesVoiceIdDeleteSignalError() instead")
    void deleteVoiceV1VoicesVoiceIdDeleteSignalE(QJsonValue summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteVoiceV1VoicesVoiceIdDeleteSignalError(QJsonValue summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use editVoiceSettingsV1VoicesVoiceIdSettingsEditPostSignalError() instead")
    void editVoiceSettingsV1VoicesVoiceIdSettingsEditPostSignalE(QJsonValue summary, QNetworkReply::NetworkError error_type, QString error_str);
    void editVoiceSettingsV1VoicesVoiceIdSettingsEditPostSignalError(QJsonValue summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use editVoiceV1VoicesVoiceIdEditPostSignalError() instead")
    void editVoiceV1VoicesVoiceIdEditPostSignalE(QJsonValue summary, QNetworkReply::NetworkError error_type, QString error_str);
    void editVoiceV1VoicesVoiceIdEditPostSignalError(QJsonValue summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDefaultVoiceSettingsV1VoicesSettingsDefaultGetSignalError() instead")
    void getDefaultVoiceSettingsV1VoicesSettingsDefaultGetSignalE(OAIVoiceSettingsResponseModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDefaultVoiceSettingsV1VoicesSettingsDefaultGetSignalError(OAIVoiceSettingsResponseModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVoiceSettingsV1VoicesVoiceIdSettingsGetSignalError() instead")
    void getVoiceSettingsV1VoicesVoiceIdSettingsGetSignalE(OAIVoiceSettingsResponseModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVoiceSettingsV1VoicesVoiceIdSettingsGetSignalError(OAIVoiceSettingsResponseModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVoiceV1VoicesVoiceIdGetSignalError() instead")
    void getVoiceV1VoicesVoiceIdGetSignalE(OAIVoiceResponseModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVoiceV1VoicesVoiceIdGetSignalError(OAIVoiceResponseModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVoicesV1VoicesGetSignalError() instead")
    void getVoicesV1VoicesGetSignalE(OAIGetVoicesResponseModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVoicesV1VoicesGetSignalError(OAIGetVoicesResponseModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use addVoiceV1VoicesAddPostSignalErrorFull() instead")
    void addVoiceV1VoicesAddPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addVoiceV1VoicesAddPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteVoiceV1VoicesVoiceIdDeleteSignalErrorFull() instead")
    void deleteVoiceV1VoicesVoiceIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteVoiceV1VoicesVoiceIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use editVoiceSettingsV1VoicesVoiceIdSettingsEditPostSignalErrorFull() instead")
    void editVoiceSettingsV1VoicesVoiceIdSettingsEditPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void editVoiceSettingsV1VoicesVoiceIdSettingsEditPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use editVoiceV1VoicesVoiceIdEditPostSignalErrorFull() instead")
    void editVoiceV1VoicesVoiceIdEditPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void editVoiceV1VoicesVoiceIdEditPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDefaultVoiceSettingsV1VoicesSettingsDefaultGetSignalErrorFull() instead")
    void getDefaultVoiceSettingsV1VoicesSettingsDefaultGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDefaultVoiceSettingsV1VoicesSettingsDefaultGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVoiceSettingsV1VoicesVoiceIdSettingsGetSignalErrorFull() instead")
    void getVoiceSettingsV1VoicesVoiceIdSettingsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVoiceSettingsV1VoicesVoiceIdSettingsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVoiceV1VoicesVoiceIdGetSignalErrorFull() instead")
    void getVoiceV1VoicesVoiceIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVoiceV1VoicesVoiceIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVoicesV1VoicesGetSignalErrorFull() instead")
    void getVoicesV1VoicesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVoicesV1VoicesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
