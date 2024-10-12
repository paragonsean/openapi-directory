/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIShipmentTrackApi_H
#define OAI_OAIShipmentTrackApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIError_response.h"
#include "OAISalesShipmentTrackRepositoryV1SavePost_request.h"
#include "OAISales_data_shipment_track_interface.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIShipmentTrackApi : public QObject {
    Q_OBJECT

public:
    OAIShipmentTrackApi(const int timeOut = 0);
    ~OAIShipmentTrackApi();

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
    * @param[in]  oai_sales_shipment_track_repository_v1_save_post_request OAISalesShipmentTrackRepositoryV1SavePost_request [optional]
    */
    virtual void salesShipmentTrackRepositoryV1SavePost(const ::OpenAPI::OptionalParam<OAISalesShipmentTrackRepositoryV1SavePost_request> &oai_sales_shipment_track_repository_v1_save_post_request = ::OpenAPI::OptionalParam<OAISalesShipmentTrackRepositoryV1SavePost_request>());


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

    void salesShipmentTrackRepositoryV1SavePostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void salesShipmentTrackRepositoryV1SavePostSignal(OAISales_data_shipment_track_interface summary);


    void salesShipmentTrackRepositoryV1SavePostSignalFull(OAIHttpRequestWorker *worker, OAISales_data_shipment_track_interface summary);

    Q_DECL_DEPRECATED_X("Use salesShipmentTrackRepositoryV1SavePostSignalError() instead")
    void salesShipmentTrackRepositoryV1SavePostSignalE(OAISales_data_shipment_track_interface summary, QNetworkReply::NetworkError error_type, QString error_str);
    void salesShipmentTrackRepositoryV1SavePostSignalError(OAISales_data_shipment_track_interface summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use salesShipmentTrackRepositoryV1SavePostSignalErrorFull() instead")
    void salesShipmentTrackRepositoryV1SavePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void salesShipmentTrackRepositoryV1SavePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
