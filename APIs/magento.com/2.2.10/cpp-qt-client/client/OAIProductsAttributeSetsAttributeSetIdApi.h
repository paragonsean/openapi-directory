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

#ifndef OAI_OAIProductsAttributeSetsAttributeSetIdApi_H
#define OAI_OAIProductsAttributeSetsAttributeSetIdApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIEavAttributeSetRepositoryV1SavePut_request.h"
#include "OAIEav_data_attribute_set_interface.h"
#include "OAIError_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIProductsAttributeSetsAttributeSetIdApi : public QObject {
    Q_OBJECT

public:
    OAIProductsAttributeSetsAttributeSetIdApi(const int timeOut = 0);
    ~OAIProductsAttributeSetsAttributeSetIdApi();

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
    * @param[in]  attribute_set_id qint32 [required]
    */
    virtual void catalogAttributeSetRepositoryV1DeleteByIdDelete(const qint32 &attribute_set_id);

    /**
    * @param[in]  attribute_set_id qint32 [required]
    */
    virtual void catalogAttributeSetRepositoryV1GetGet(const qint32 &attribute_set_id);

    /**
    * @param[in]  attribute_set_id QString [required]
    * @param[in]  oai_eav_attribute_set_repository_v1_save_put_request OAIEavAttributeSetRepositoryV1SavePut_request [optional]
    */
    virtual void catalogAttributeSetRepositoryV1SavePut(const QString &attribute_set_id, const ::OpenAPI::OptionalParam<OAIEavAttributeSetRepositoryV1SavePut_request> &oai_eav_attribute_set_repository_v1_save_put_request = ::OpenAPI::OptionalParam<OAIEavAttributeSetRepositoryV1SavePut_request>());


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

    void catalogAttributeSetRepositoryV1DeleteByIdDeleteCallback(OAIHttpRequestWorker *worker);
    void catalogAttributeSetRepositoryV1GetGetCallback(OAIHttpRequestWorker *worker);
    void catalogAttributeSetRepositoryV1SavePutCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void catalogAttributeSetRepositoryV1DeleteByIdDeleteSignal(bool summary);
    void catalogAttributeSetRepositoryV1GetGetSignal(OAIEav_data_attribute_set_interface summary);
    void catalogAttributeSetRepositoryV1SavePutSignal(OAIEav_data_attribute_set_interface summary);


    void catalogAttributeSetRepositoryV1DeleteByIdDeleteSignalFull(OAIHttpRequestWorker *worker, bool summary);
    void catalogAttributeSetRepositoryV1GetGetSignalFull(OAIHttpRequestWorker *worker, OAIEav_data_attribute_set_interface summary);
    void catalogAttributeSetRepositoryV1SavePutSignalFull(OAIHttpRequestWorker *worker, OAIEav_data_attribute_set_interface summary);

    Q_DECL_DEPRECATED_X("Use catalogAttributeSetRepositoryV1DeleteByIdDeleteSignalError() instead")
    void catalogAttributeSetRepositoryV1DeleteByIdDeleteSignalE(bool summary, QNetworkReply::NetworkError error_type, QString error_str);
    void catalogAttributeSetRepositoryV1DeleteByIdDeleteSignalError(bool summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use catalogAttributeSetRepositoryV1GetGetSignalError() instead")
    void catalogAttributeSetRepositoryV1GetGetSignalE(OAIEav_data_attribute_set_interface summary, QNetworkReply::NetworkError error_type, QString error_str);
    void catalogAttributeSetRepositoryV1GetGetSignalError(OAIEav_data_attribute_set_interface summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use catalogAttributeSetRepositoryV1SavePutSignalError() instead")
    void catalogAttributeSetRepositoryV1SavePutSignalE(OAIEav_data_attribute_set_interface summary, QNetworkReply::NetworkError error_type, QString error_str);
    void catalogAttributeSetRepositoryV1SavePutSignalError(OAIEav_data_attribute_set_interface summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use catalogAttributeSetRepositoryV1DeleteByIdDeleteSignalErrorFull() instead")
    void catalogAttributeSetRepositoryV1DeleteByIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void catalogAttributeSetRepositoryV1DeleteByIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use catalogAttributeSetRepositoryV1GetGetSignalErrorFull() instead")
    void catalogAttributeSetRepositoryV1GetGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void catalogAttributeSetRepositoryV1GetGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use catalogAttributeSetRepositoryV1SavePutSignalErrorFull() instead")
    void catalogAttributeSetRepositoryV1SavePutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void catalogAttributeSetRepositoryV1SavePutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
