/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIPredictionsApiApi_H
#define OAI_OAIPredictionsApiApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICustomVisionError.h"
#include "OAIHttpFileElement.h"
#include "OAIImagePrediction.h"
#include "OAIImageUrl.h"
#include "OAIPredictionQueryResult.h"
#include "OAIPredictionQueryToken.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIPredictionsApiApi : public QObject {
    Q_OBJECT

public:
    OAIPredictionsApiApi(const int timeOut = 0);
    ~OAIPredictionsApiApi();

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
    * @param[in]  project_id QString [required]
    * @param[in]  ids QList<QString> [required]
    */
    virtual void deletePrediction(const QString &project_id, const QList<QString> &ids);

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  oai_prediction_query_token OAIPredictionQueryToken [required]
    */
    virtual void queryPredictions(const QString &project_id, const OAIPredictionQueryToken &oai_prediction_query_token);

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  image_data OAIHttpFileElement [required]
    * @param[in]  iteration_id QString [optional]
    * @param[in]  store bool [optional]
    */
    virtual void quickTestImage(const QString &project_id, const OAIHttpFileElement &image_data, const ::OpenAPI::OptionalParam<QString> &iteration_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &store = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  oai_image_url OAIImageUrl [required]
    * @param[in]  iteration_id QString [optional]
    * @param[in]  store bool [optional]
    */
    virtual void quickTestImageUrl(const QString &project_id, const OAIImageUrl &oai_image_url, const ::OpenAPI::OptionalParam<QString> &iteration_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &store = ::OpenAPI::OptionalParam<bool>());


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

    void deletePredictionCallback(OAIHttpRequestWorker *worker);
    void queryPredictionsCallback(OAIHttpRequestWorker *worker);
    void quickTestImageCallback(OAIHttpRequestWorker *worker);
    void quickTestImageUrlCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void deletePredictionSignal();
    void queryPredictionsSignal(OAIPredictionQueryResult summary);
    void quickTestImageSignal(OAIImagePrediction summary);
    void quickTestImageUrlSignal(OAIImagePrediction summary);


    void deletePredictionSignalFull(OAIHttpRequestWorker *worker);
    void queryPredictionsSignalFull(OAIHttpRequestWorker *worker, OAIPredictionQueryResult summary);
    void quickTestImageSignalFull(OAIHttpRequestWorker *worker, OAIImagePrediction summary);
    void quickTestImageUrlSignalFull(OAIHttpRequestWorker *worker, OAIImagePrediction summary);

    Q_DECL_DEPRECATED_X("Use deletePredictionSignalError() instead")
    void deletePredictionSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deletePredictionSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use queryPredictionsSignalError() instead")
    void queryPredictionsSignalE(OAIPredictionQueryResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void queryPredictionsSignalError(OAIPredictionQueryResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use quickTestImageSignalError() instead")
    void quickTestImageSignalE(OAIImagePrediction summary, QNetworkReply::NetworkError error_type, QString error_str);
    void quickTestImageSignalError(OAIImagePrediction summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use quickTestImageUrlSignalError() instead")
    void quickTestImageUrlSignalE(OAIImagePrediction summary, QNetworkReply::NetworkError error_type, QString error_str);
    void quickTestImageUrlSignalError(OAIImagePrediction summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use deletePredictionSignalErrorFull() instead")
    void deletePredictionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deletePredictionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use queryPredictionsSignalErrorFull() instead")
    void queryPredictionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void queryPredictionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use quickTestImageSignalErrorFull() instead")
    void quickTestImageSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void quickTestImageSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use quickTestImageUrlSignalErrorFull() instead")
    void quickTestImageUrlSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void quickTestImageUrlSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
