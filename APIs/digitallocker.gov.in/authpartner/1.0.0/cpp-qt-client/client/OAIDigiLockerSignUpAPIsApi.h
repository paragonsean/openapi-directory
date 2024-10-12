/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDigiLockerSignUpAPIsApi_H
#define OAI_OAIDigiLockerSignUpAPIsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIDemoAuthResponse.h"
#include "OAIDemoAuthVerifyResponse.h"
#include "OAIGet_Device_Code_id_401_response.h"
#include "OAIHttpFileElement.h"
#include "OAISIGN_UP_id_400_response.h"
#include "OAIVerify_Account_id_500_response.h"
#include "OAIVerify_OTP_id_400_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDigiLockerSignUpAPIsApi : public QObject {
    Q_OBJECT

public:
    OAIDigiLockerSignUpAPIsApi(const int timeOut = 0);
    ~OAIDigiLockerSignUpAPIsApi();

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
    * @param[in]  clientid QString [optional]
    * @param[in]  consent QString [optional]
    * @param[in]  demoauth QString [optional]
    * @param[in]  dob qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  hmac OAIHttpFileElement [optional]
    * @param[in]  mobile qint32 [optional]
    * @param[in]  name QString [optional]
    * @param[in]  ts QString [optional]
    * @param[in]  uid qint32 [optional]
    * @param[in]  verification QString [optional]
    */
    virtual void sIGN_UP_id(const ::OpenAPI::OptionalParam<QString> &clientid = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &consent = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &demoauth = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &dob = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIHttpFileElement> &hmac = ::OpenAPI::OptionalParam<OAIHttpFileElement>(), const ::OpenAPI::OptionalParam<qint32> &mobile = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ts = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &uid = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &verification = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  clientid QString [optional]
    * @param[in]  hmac OAIHttpFileElement [optional]
    * @param[in]  mobile qint32 [optional]
    * @param[in]  otp qint32 [optional]
    * @param[in]  ts QString [optional]
    */
    virtual void verify_OTP_id(const ::OpenAPI::OptionalParam<QString> &clientid = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIHttpFileElement> &hmac = ::OpenAPI::OptionalParam<OAIHttpFileElement>(), const ::OpenAPI::OptionalParam<qint32> &mobile = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &otp = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &ts = ::OpenAPI::OptionalParam<QString>());


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

    void sIGN_UP_idCallback(OAIHttpRequestWorker *worker);
    void verify_OTP_idCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void sIGN_UP_idSignal(OAIDemoAuthResponse summary);
    void verify_OTP_idSignal(OAIDemoAuthVerifyResponse summary);


    void sIGN_UP_idSignalFull(OAIHttpRequestWorker *worker, OAIDemoAuthResponse summary);
    void verify_OTP_idSignalFull(OAIHttpRequestWorker *worker, OAIDemoAuthVerifyResponse summary);

    Q_DECL_DEPRECATED_X("Use sIGN_UP_idSignalError() instead")
    void sIGN_UP_idSignalE(OAIDemoAuthResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void sIGN_UP_idSignalError(OAIDemoAuthResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use verify_OTP_idSignalError() instead")
    void verify_OTP_idSignalE(OAIDemoAuthVerifyResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void verify_OTP_idSignalError(OAIDemoAuthVerifyResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use sIGN_UP_idSignalErrorFull() instead")
    void sIGN_UP_idSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sIGN_UP_idSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use verify_OTP_idSignalErrorFull() instead")
    void verify_OTP_idSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void verify_OTP_idSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
