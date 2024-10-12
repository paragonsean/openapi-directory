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

#ifndef OAI_OAIGuestCartsCartIdGiftMessageApi_H
#define OAI_OAIGuestCartsCartIdGiftMessageApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIError_response.h"
#include "OAIGiftMessageCartRepositoryV1SavePost_request.h"
#include "OAIGift_message_data_message_interface.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIGuestCartsCartIdGiftMessageApi : public QObject {
    Q_OBJECT

public:
    OAIGuestCartsCartIdGiftMessageApi(const int timeOut = 0);
    ~OAIGuestCartsCartIdGiftMessageApi();

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
    * @param[in]  cart_id QString [required]
    */
    virtual void giftMessageGuestCartRepositoryV1GetGet(const QString &cart_id);

    /**
    * @param[in]  cart_id QString [required]
    * @param[in]  oai_gift_message_cart_repository_v1_save_post_request OAIGiftMessageCartRepositoryV1SavePost_request [optional]
    */
    virtual void giftMessageGuestCartRepositoryV1SavePost(const QString &cart_id, const ::OpenAPI::OptionalParam<OAIGiftMessageCartRepositoryV1SavePost_request> &oai_gift_message_cart_repository_v1_save_post_request = ::OpenAPI::OptionalParam<OAIGiftMessageCartRepositoryV1SavePost_request>());


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

    void giftMessageGuestCartRepositoryV1GetGetCallback(OAIHttpRequestWorker *worker);
    void giftMessageGuestCartRepositoryV1SavePostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void giftMessageGuestCartRepositoryV1GetGetSignal(OAIGift_message_data_message_interface summary);
    void giftMessageGuestCartRepositoryV1SavePostSignal(bool summary);


    void giftMessageGuestCartRepositoryV1GetGetSignalFull(OAIHttpRequestWorker *worker, OAIGift_message_data_message_interface summary);
    void giftMessageGuestCartRepositoryV1SavePostSignalFull(OAIHttpRequestWorker *worker, bool summary);

    Q_DECL_DEPRECATED_X("Use giftMessageGuestCartRepositoryV1GetGetSignalError() instead")
    void giftMessageGuestCartRepositoryV1GetGetSignalE(OAIGift_message_data_message_interface summary, QNetworkReply::NetworkError error_type, QString error_str);
    void giftMessageGuestCartRepositoryV1GetGetSignalError(OAIGift_message_data_message_interface summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use giftMessageGuestCartRepositoryV1SavePostSignalError() instead")
    void giftMessageGuestCartRepositoryV1SavePostSignalE(bool summary, QNetworkReply::NetworkError error_type, QString error_str);
    void giftMessageGuestCartRepositoryV1SavePostSignalError(bool summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use giftMessageGuestCartRepositoryV1GetGetSignalErrorFull() instead")
    void giftMessageGuestCartRepositoryV1GetGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void giftMessageGuestCartRepositoryV1GetGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use giftMessageGuestCartRepositoryV1SavePostSignalErrorFull() instead")
    void giftMessageGuestCartRepositoryV1SavePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void giftMessageGuestCartRepositoryV1SavePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
