/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAISharesApi_H
#define OAI_OAISharesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICreateDownloadShareRequest.h"
#include "OAICreateUploadShareRequest.h"
#include "OAIDeleteDownloadSharesRequest.h"
#include "OAIDeleteUploadSharesRequest.h"
#include "OAIDownloadShare.h"
#include "OAIDownloadShareLinkEmail.h"
#include "OAIDownloadShareList.h"
#include "OAIErrorResponse.h"
#include "OAIResetPassword_400_response.h"
#include "OAIUpdateDownloadShareRequest.h"
#include "OAIUpdateDownloadSharesBulkRequest.h"
#include "OAIUpdateUploadShareRequest.h"
#include "OAIUpdateUploadSharesBulkRequest.h"
#include "OAIUploadShare.h"
#include "OAIUploadShareLinkEmail.h"
#include "OAIUploadShareList.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAISharesApi : public QObject {
    Q_OBJECT

public:
    OAISharesApi(const int timeOut = 0);
    ~OAISharesApi();

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
    * @param[in]  oai_create_download_share_request OAICreateDownloadShareRequest [required]
    * @param[in]  x_sds_date_format QString [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void createDownloadShare(const OAICreateDownloadShareRequest &oai_create_download_share_request, const ::OpenAPI::OptionalParam<QString> &x_sds_date_format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_create_upload_share_request OAICreateUploadShareRequest [required]
    * @param[in]  x_sds_date_format QString [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void createUploadShare(const OAICreateUploadShareRequest &oai_create_upload_share_request, const ::OpenAPI::OptionalParam<QString> &x_sds_date_format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_delete_download_shares_request OAIDeleteDownloadSharesRequest [required]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void deleteDownloadShares(const OAIDeleteDownloadSharesRequest &oai_delete_download_shares_request, const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_delete_upload_shares_request OAIDeleteUploadSharesRequest [required]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void deleteUploadShares(const OAIDeleteUploadSharesRequest &oai_delete_upload_shares_request, const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  share_id qint64 [required]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void removeDownloadShare(const qint64 &share_id, const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  share_id qint64 [required]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void removeUploadShare(const qint64 &share_id, const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  share_id qint64 [required]
    * @param[in]  x_sds_date_format QString [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void requestDownloadShare(const qint64 &share_id, const ::OpenAPI::OptionalParam<QString> &x_sds_date_format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  share_id qint64 [required]
    * @param[in]  x_sds_date_format QString [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void requestDownloadShareQr(const qint64 &share_id, const ::OpenAPI::OptionalParam<QString> &x_sds_date_format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_sds_date_format QString [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void requestDownloadShares(const ::OpenAPI::OptionalParam<QString> &x_sds_date_format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  share_id qint64 [required]
    * @param[in]  x_sds_date_format QString [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void requestUploadShare(const qint64 &share_id, const ::OpenAPI::OptionalParam<QString> &x_sds_date_format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  share_id qint64 [required]
    * @param[in]  x_sds_date_format QString [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void requestUploadShareQr(const qint64 &share_id, const ::OpenAPI::OptionalParam<QString> &x_sds_date_format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_sds_date_format QString [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void requestUploadShares(const ::OpenAPI::OptionalParam<QString> &x_sds_date_format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  share_id qint64 [required]
    * @param[in]  oai_download_share_link_email OAIDownloadShareLinkEmail [required]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void sendDownloadShareLinkViaEmail(const qint64 &share_id, const OAIDownloadShareLinkEmail &oai_download_share_link_email, const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  share_id qint64 [required]
    * @param[in]  oai_upload_share_link_email OAIUploadShareLinkEmail [required]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void sendUploadShareLinkViaEmail(const qint64 &share_id, const OAIUploadShareLinkEmail &oai_upload_share_link_email, const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  share_id qint64 [required]
    * @param[in]  oai_update_download_share_request OAIUpdateDownloadShareRequest [required]
    * @param[in]  x_sds_date_format QString [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void updateDownloadShare(const qint64 &share_id, const OAIUpdateDownloadShareRequest &oai_update_download_share_request, const ::OpenAPI::OptionalParam<QString> &x_sds_date_format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_update_download_shares_bulk_request OAIUpdateDownloadSharesBulkRequest [required]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void updateDownloadShares(const OAIUpdateDownloadSharesBulkRequest &oai_update_download_shares_bulk_request, const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  share_id qint64 [required]
    * @param[in]  oai_update_upload_share_request OAIUpdateUploadShareRequest [required]
    * @param[in]  x_sds_date_format QString [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void updateUploadShare(const qint64 &share_id, const OAIUpdateUploadShareRequest &oai_update_upload_share_request, const ::OpenAPI::OptionalParam<QString> &x_sds_date_format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_update_upload_shares_bulk_request OAIUpdateUploadSharesBulkRequest [required]
    * @param[in]  x_sds_date_format QString [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void updateUploadShares(const OAIUpdateUploadSharesBulkRequest &oai_update_upload_shares_bulk_request, const ::OpenAPI::OptionalParam<QString> &x_sds_date_format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());


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

    void createDownloadShareCallback(OAIHttpRequestWorker *worker);
    void createUploadShareCallback(OAIHttpRequestWorker *worker);
    void deleteDownloadSharesCallback(OAIHttpRequestWorker *worker);
    void deleteUploadSharesCallback(OAIHttpRequestWorker *worker);
    void removeDownloadShareCallback(OAIHttpRequestWorker *worker);
    void removeUploadShareCallback(OAIHttpRequestWorker *worker);
    void requestDownloadShareCallback(OAIHttpRequestWorker *worker);
    void requestDownloadShareQrCallback(OAIHttpRequestWorker *worker);
    void requestDownloadSharesCallback(OAIHttpRequestWorker *worker);
    void requestUploadShareCallback(OAIHttpRequestWorker *worker);
    void requestUploadShareQrCallback(OAIHttpRequestWorker *worker);
    void requestUploadSharesCallback(OAIHttpRequestWorker *worker);
    void sendDownloadShareLinkViaEmailCallback(OAIHttpRequestWorker *worker);
    void sendUploadShareLinkViaEmailCallback(OAIHttpRequestWorker *worker);
    void updateDownloadShareCallback(OAIHttpRequestWorker *worker);
    void updateDownloadSharesCallback(OAIHttpRequestWorker *worker);
    void updateUploadShareCallback(OAIHttpRequestWorker *worker);
    void updateUploadSharesCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void createDownloadShareSignal(OAIDownloadShare summary);
    void createUploadShareSignal(OAIUploadShare summary);
    void deleteDownloadSharesSignal();
    void deleteUploadSharesSignal();
    void removeDownloadShareSignal();
    void removeUploadShareSignal();
    void requestDownloadShareSignal(OAIDownloadShare summary);
    void requestDownloadShareQrSignal(OAIDownloadShare summary);
    void requestDownloadSharesSignal(OAIDownloadShareList summary);
    void requestUploadShareSignal(OAIUploadShare summary);
    void requestUploadShareQrSignal(OAIUploadShare summary);
    void requestUploadSharesSignal(OAIUploadShareList summary);
    void sendDownloadShareLinkViaEmailSignal();
    void sendUploadShareLinkViaEmailSignal();
    void updateDownloadShareSignal(OAIDownloadShare summary);
    void updateDownloadSharesSignal();
    void updateUploadShareSignal(OAIUploadShare summary);
    void updateUploadSharesSignal();


    void createDownloadShareSignalFull(OAIHttpRequestWorker *worker, OAIDownloadShare summary);
    void createUploadShareSignalFull(OAIHttpRequestWorker *worker, OAIUploadShare summary);
    void deleteDownloadSharesSignalFull(OAIHttpRequestWorker *worker);
    void deleteUploadSharesSignalFull(OAIHttpRequestWorker *worker);
    void removeDownloadShareSignalFull(OAIHttpRequestWorker *worker);
    void removeUploadShareSignalFull(OAIHttpRequestWorker *worker);
    void requestDownloadShareSignalFull(OAIHttpRequestWorker *worker, OAIDownloadShare summary);
    void requestDownloadShareQrSignalFull(OAIHttpRequestWorker *worker, OAIDownloadShare summary);
    void requestDownloadSharesSignalFull(OAIHttpRequestWorker *worker, OAIDownloadShareList summary);
    void requestUploadShareSignalFull(OAIHttpRequestWorker *worker, OAIUploadShare summary);
    void requestUploadShareQrSignalFull(OAIHttpRequestWorker *worker, OAIUploadShare summary);
    void requestUploadSharesSignalFull(OAIHttpRequestWorker *worker, OAIUploadShareList summary);
    void sendDownloadShareLinkViaEmailSignalFull(OAIHttpRequestWorker *worker);
    void sendUploadShareLinkViaEmailSignalFull(OAIHttpRequestWorker *worker);
    void updateDownloadShareSignalFull(OAIHttpRequestWorker *worker, OAIDownloadShare summary);
    void updateDownloadSharesSignalFull(OAIHttpRequestWorker *worker);
    void updateUploadShareSignalFull(OAIHttpRequestWorker *worker, OAIUploadShare summary);
    void updateUploadSharesSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use createDownloadShareSignalError() instead")
    void createDownloadShareSignalE(OAIDownloadShare summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createDownloadShareSignalError(OAIDownloadShare summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createUploadShareSignalError() instead")
    void createUploadShareSignalE(OAIUploadShare summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createUploadShareSignalError(OAIUploadShare summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDownloadSharesSignalError() instead")
    void deleteDownloadSharesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDownloadSharesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteUploadSharesSignalError() instead")
    void deleteUploadSharesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteUploadSharesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use removeDownloadShareSignalError() instead")
    void removeDownloadShareSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void removeDownloadShareSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use removeUploadShareSignalError() instead")
    void removeUploadShareSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void removeUploadShareSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestDownloadShareSignalError() instead")
    void requestDownloadShareSignalE(OAIDownloadShare summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestDownloadShareSignalError(OAIDownloadShare summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestDownloadShareQrSignalError() instead")
    void requestDownloadShareQrSignalE(OAIDownloadShare summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestDownloadShareQrSignalError(OAIDownloadShare summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestDownloadSharesSignalError() instead")
    void requestDownloadSharesSignalE(OAIDownloadShareList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestDownloadSharesSignalError(OAIDownloadShareList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestUploadShareSignalError() instead")
    void requestUploadShareSignalE(OAIUploadShare summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestUploadShareSignalError(OAIUploadShare summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestUploadShareQrSignalError() instead")
    void requestUploadShareQrSignalE(OAIUploadShare summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestUploadShareQrSignalError(OAIUploadShare summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestUploadSharesSignalError() instead")
    void requestUploadSharesSignalE(OAIUploadShareList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestUploadSharesSignalError(OAIUploadShareList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sendDownloadShareLinkViaEmailSignalError() instead")
    void sendDownloadShareLinkViaEmailSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void sendDownloadShareLinkViaEmailSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sendUploadShareLinkViaEmailSignalError() instead")
    void sendUploadShareLinkViaEmailSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void sendUploadShareLinkViaEmailSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDownloadShareSignalError() instead")
    void updateDownloadShareSignalE(OAIDownloadShare summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDownloadShareSignalError(OAIDownloadShare summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDownloadSharesSignalError() instead")
    void updateDownloadSharesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void updateDownloadSharesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateUploadShareSignalError() instead")
    void updateUploadShareSignalE(OAIUploadShare summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateUploadShareSignalError(OAIUploadShare summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateUploadSharesSignalError() instead")
    void updateUploadSharesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void updateUploadSharesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use createDownloadShareSignalErrorFull() instead")
    void createDownloadShareSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createDownloadShareSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createUploadShareSignalErrorFull() instead")
    void createUploadShareSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createUploadShareSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDownloadSharesSignalErrorFull() instead")
    void deleteDownloadSharesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDownloadSharesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteUploadSharesSignalErrorFull() instead")
    void deleteUploadSharesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteUploadSharesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use removeDownloadShareSignalErrorFull() instead")
    void removeDownloadShareSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void removeDownloadShareSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use removeUploadShareSignalErrorFull() instead")
    void removeUploadShareSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void removeUploadShareSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestDownloadShareSignalErrorFull() instead")
    void requestDownloadShareSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestDownloadShareSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestDownloadShareQrSignalErrorFull() instead")
    void requestDownloadShareQrSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestDownloadShareQrSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestDownloadSharesSignalErrorFull() instead")
    void requestDownloadSharesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestDownloadSharesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestUploadShareSignalErrorFull() instead")
    void requestUploadShareSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestUploadShareSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestUploadShareQrSignalErrorFull() instead")
    void requestUploadShareQrSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestUploadShareQrSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestUploadSharesSignalErrorFull() instead")
    void requestUploadSharesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestUploadSharesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sendDownloadShareLinkViaEmailSignalErrorFull() instead")
    void sendDownloadShareLinkViaEmailSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sendDownloadShareLinkViaEmailSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sendUploadShareLinkViaEmailSignalErrorFull() instead")
    void sendUploadShareLinkViaEmailSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sendUploadShareLinkViaEmailSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDownloadShareSignalErrorFull() instead")
    void updateDownloadShareSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDownloadShareSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDownloadSharesSignalErrorFull() instead")
    void updateDownloadSharesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDownloadSharesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateUploadShareSignalErrorFull() instead")
    void updateUploadShareSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateUploadShareSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateUploadSharesSignalErrorFull() instead")
    void updateUploadSharesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateUploadSharesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
