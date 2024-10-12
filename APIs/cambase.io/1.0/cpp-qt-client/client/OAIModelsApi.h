/**
 * Cambase.io
 * Cambase.io is a project by Evercam.io in order to make it easier for software developers to have a reliable, up to date source of model hardware information available via a public API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIModelsApi_H
#define OAI_OAIModelsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIModelsApi : public QObject {
    Q_OBJECT

public:
    OAIModelsApi(const int timeOut = 0);
    ~OAIModelsApi();

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
    * @param[in]  vendor_id QString [required]
    * @param[in]  model_model QString [required]
    * @param[in]  model_shape QString [optional]
    * @param[in]  model_resolution QString [optional]
    * @param[in]  model_onvif QString [optional]
    * @param[in]  model_psia QString [optional]
    * @param[in]  model_ptz QString [optional]
    * @param[in]  model_infrared QString [optional]
    * @param[in]  model_varifocal QString [optional]
    * @param[in]  model_sd_card QString [optional]
    * @param[in]  model_upnp QString [optional]
    * @param[in]  model_audio_in QString [optional]
    * @param[in]  model_audio_out QString [optional]
    * @param[in]  model_default_username QString [optional]
    * @param[in]  model_default_password QString [optional]
    * @param[in]  model_jpeg_url QString [optional]
    * @param[in]  model_h264_url QString [optional]
    * @param[in]  model_mjpeg_url QString [optional]
    */
    virtual void apiV1ModelsCreate(const QString &vendor_id, const QString &model_model, const ::OpenAPI::OptionalParam<QString> &model_shape = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_resolution = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_onvif = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_psia = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_ptz = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_infrared = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_varifocal = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_sd_card = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_upnp = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_audio_in = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_audio_out = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_default_username = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_default_password = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_jpeg_url = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_h264_url = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_mjpeg_url = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  vendor_id QString [required]
    * @param[in]  model_model QString [optional]
    * @param[in]  model_shape QString [optional]
    * @param[in]  model_resolution QString [optional]
    * @param[in]  model_onvif QString [optional]
    * @param[in]  model_psia QString [optional]
    * @param[in]  model_ptz QString [optional]
    * @param[in]  model_infrared QString [optional]
    * @param[in]  model_varifocal QString [optional]
    * @param[in]  model_sd_card QString [optional]
    * @param[in]  model_upnp QString [optional]
    * @param[in]  model_audio_in QString [optional]
    * @param[in]  model_audio_out QString [optional]
    * @param[in]  model_default_username QString [optional]
    * @param[in]  model_default_password QString [optional]
    * @param[in]  model_jpeg_url QString [optional]
    * @param[in]  model_h264_url QString [optional]
    * @param[in]  model_mjpeg_url QString [optional]
    */
    virtual void apiV1ModelsIdJsonPatch(const QString &id, const QString &vendor_id, const ::OpenAPI::OptionalParam<QString> &model_model = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_shape = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_resolution = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_onvif = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_psia = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_ptz = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_infrared = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_varifocal = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_sd_card = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_upnp = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_audio_in = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_audio_out = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_default_username = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_default_password = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_jpeg_url = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_h264_url = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_mjpeg_url = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  vendor_id QString [required]
    * @param[in]  model_model QString [optional]
    * @param[in]  model_shape QString [optional]
    * @param[in]  model_resolution QString [optional]
    * @param[in]  model_onvif QString [optional]
    * @param[in]  model_psia QString [optional]
    * @param[in]  model_ptz QString [optional]
    * @param[in]  model_infrared QString [optional]
    * @param[in]  model_varifocal QString [optional]
    * @param[in]  model_sd_card QString [optional]
    * @param[in]  model_upnp QString [optional]
    * @param[in]  model_audio_in QString [optional]
    * @param[in]  model_audio_out QString [optional]
    * @param[in]  model_default_username QString [optional]
    * @param[in]  model_default_password QString [optional]
    * @param[in]  model_jpeg_url QString [optional]
    * @param[in]  model_h264_url QString [optional]
    * @param[in]  model_mjpeg_url QString [optional]
    */
    virtual void apiV1ModelsIdJsonPut(const QString &id, const QString &vendor_id, const ::OpenAPI::OptionalParam<QString> &model_model = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_shape = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_resolution = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_onvif = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_psia = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_ptz = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_infrared = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_varifocal = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_sd_card = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_upnp = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_audio_in = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_audio_out = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_default_username = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_default_password = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_jpeg_url = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_h264_url = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &model_mjpeg_url = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  order QString [optional]
    */
    virtual void apiV1ModelsIndex(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &order = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  q_model_cont QString [optional]
    * @param[in]  q_manufacturer_name_cont QString [optional]
    * @param[in]  q_shape_eq QString [optional]
    * @param[in]  q_resolution_eq QString [optional]
    * @param[in]  q_onvif_true QString [optional]
    * @param[in]  q_psia_true QString [optional]
    * @param[in]  q_ptz_true QString [optional]
    * @param[in]  q_infrared_true QString [optional]
    * @param[in]  q_varifocal_true QString [optional]
    * @param[in]  q_sd_card_true QString [optional]
    * @param[in]  q_upnp_true QString [optional]
    * @param[in]  q_audio_in_true QString [optional]
    * @param[in]  q_audio_out_true QString [optional]
    */
    virtual void apiV1ModelsSearch(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &q_model_cont = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_manufacturer_name_cont = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_shape_eq = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_resolution_eq = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_onvif_true = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_psia_true = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_ptz_true = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_infrared_true = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_varifocal_true = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_sd_card_true = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_upnp_true = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_audio_in_true = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_audio_out_true = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void apiV1ModelsShow(const qint32 &id);


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

    void apiV1ModelsCreateCallback(OAIHttpRequestWorker *worker);
    void apiV1ModelsIdJsonPatchCallback(OAIHttpRequestWorker *worker);
    void apiV1ModelsIdJsonPutCallback(OAIHttpRequestWorker *worker);
    void apiV1ModelsIndexCallback(OAIHttpRequestWorker *worker);
    void apiV1ModelsSearchCallback(OAIHttpRequestWorker *worker);
    void apiV1ModelsShowCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void apiV1ModelsCreateSignal();
    void apiV1ModelsIdJsonPatchSignal();
    void apiV1ModelsIdJsonPutSignal();
    void apiV1ModelsIndexSignal();
    void apiV1ModelsSearchSignal();
    void apiV1ModelsShowSignal();


    void apiV1ModelsCreateSignalFull(OAIHttpRequestWorker *worker);
    void apiV1ModelsIdJsonPatchSignalFull(OAIHttpRequestWorker *worker);
    void apiV1ModelsIdJsonPutSignalFull(OAIHttpRequestWorker *worker);
    void apiV1ModelsIndexSignalFull(OAIHttpRequestWorker *worker);
    void apiV1ModelsSearchSignalFull(OAIHttpRequestWorker *worker);
    void apiV1ModelsShowSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use apiV1ModelsCreateSignalError() instead")
    void apiV1ModelsCreateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1ModelsCreateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1ModelsIdJsonPatchSignalError() instead")
    void apiV1ModelsIdJsonPatchSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1ModelsIdJsonPatchSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1ModelsIdJsonPutSignalError() instead")
    void apiV1ModelsIdJsonPutSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1ModelsIdJsonPutSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1ModelsIndexSignalError() instead")
    void apiV1ModelsIndexSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1ModelsIndexSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1ModelsSearchSignalError() instead")
    void apiV1ModelsSearchSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1ModelsSearchSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1ModelsShowSignalError() instead")
    void apiV1ModelsShowSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1ModelsShowSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use apiV1ModelsCreateSignalErrorFull() instead")
    void apiV1ModelsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1ModelsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1ModelsIdJsonPatchSignalErrorFull() instead")
    void apiV1ModelsIdJsonPatchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1ModelsIdJsonPatchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1ModelsIdJsonPutSignalErrorFull() instead")
    void apiV1ModelsIdJsonPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1ModelsIdJsonPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1ModelsIndexSignalErrorFull() instead")
    void apiV1ModelsIndexSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1ModelsIndexSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1ModelsSearchSignalErrorFull() instead")
    void apiV1ModelsSearchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1ModelsSearchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1ModelsShowSignalErrorFull() instead")
    void apiV1ModelsShowSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1ModelsShowSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
