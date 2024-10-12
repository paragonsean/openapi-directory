/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIRegistrationWithMobileNumberApi_H
#define OAI_OAIRegistrationWithMobileNumberApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICreateAccountByVerifiedMobileRequest.h"
#include "OAICreateAccountJwtResponse.h"
#include "OAIGenerateMobileOTPRequest.h"
#include "OAIMobileVerificationToken.h"
#include "OAIResendOTPRequest.h"
#include "OAITxnResponse.h"
#include "OAIVerifyMobileRequest.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIRegistrationWithMobileNumberApi : public QObject {
    Q_OBJECT

public:
    OAIRegistrationWithMobileNumberApi(const int timeOut = 0);
    ~OAIRegistrationWithMobileNumberApi();

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
    * @param[in]  generate_otp_request OAIGenerateMobileOTPRequest [required]
    * @param[in]  accept_language QString [optional]
    */
    virtual void generateMobileOTPUsingPOST1(const OAIGenerateMobileOTPRequest &generate_otp_request, const ::OpenAPI::OptionalParam<QString> &accept_language = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  resend_request OAIResendOTPRequest [required]
    * @param[in]  accept_language QString [optional]
    */
    virtual void resentOtpUsingPOST(const OAIResendOTPRequest &resend_request, const ::OpenAPI::OptionalParam<QString> &accept_language = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  verify_otp_request OAIVerifyMobileRequest [required]
    * @param[in]  accept_language QString [optional]
    */
    virtual void verifyMobileOTPUsingPOST(const OAIVerifyMobileRequest &verify_otp_request, const ::OpenAPI::OptionalParam<QString> &accept_language = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  create_account_request OAICreateAccountByVerifiedMobileRequest [required]
    * @param[in]  accept_language QString [optional]
    */
    virtual void verifyUserViaMobileUsingPOST(const OAICreateAccountByVerifiedMobileRequest &create_account_request, const ::OpenAPI::OptionalParam<QString> &accept_language = ::OpenAPI::OptionalParam<QString>());


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

    void generateMobileOTPUsingPOST1Callback(OAIHttpRequestWorker *worker);
    void resentOtpUsingPOSTCallback(OAIHttpRequestWorker *worker);
    void verifyMobileOTPUsingPOSTCallback(OAIHttpRequestWorker *worker);
    void verifyUserViaMobileUsingPOSTCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void generateMobileOTPUsingPOST1Signal(OAITxnResponse summary);
    void resentOtpUsingPOSTSignal(bool summary);
    void verifyMobileOTPUsingPOSTSignal(OAIMobileVerificationToken summary);
    void verifyUserViaMobileUsingPOSTSignal(OAICreateAccountJwtResponse summary);


    void generateMobileOTPUsingPOST1SignalFull(OAIHttpRequestWorker *worker, OAITxnResponse summary);
    void resentOtpUsingPOSTSignalFull(OAIHttpRequestWorker *worker, bool summary);
    void verifyMobileOTPUsingPOSTSignalFull(OAIHttpRequestWorker *worker, OAIMobileVerificationToken summary);
    void verifyUserViaMobileUsingPOSTSignalFull(OAIHttpRequestWorker *worker, OAICreateAccountJwtResponse summary);

    Q_DECL_DEPRECATED_X("Use generateMobileOTPUsingPOST1SignalError() instead")
    void generateMobileOTPUsingPOST1SignalE(OAITxnResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void generateMobileOTPUsingPOST1SignalError(OAITxnResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resentOtpUsingPOSTSignalError() instead")
    void resentOtpUsingPOSTSignalE(bool summary, QNetworkReply::NetworkError error_type, QString error_str);
    void resentOtpUsingPOSTSignalError(bool summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use verifyMobileOTPUsingPOSTSignalError() instead")
    void verifyMobileOTPUsingPOSTSignalE(OAIMobileVerificationToken summary, QNetworkReply::NetworkError error_type, QString error_str);
    void verifyMobileOTPUsingPOSTSignalError(OAIMobileVerificationToken summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use verifyUserViaMobileUsingPOSTSignalError() instead")
    void verifyUserViaMobileUsingPOSTSignalE(OAICreateAccountJwtResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void verifyUserViaMobileUsingPOSTSignalError(OAICreateAccountJwtResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use generateMobileOTPUsingPOST1SignalErrorFull() instead")
    void generateMobileOTPUsingPOST1SignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void generateMobileOTPUsingPOST1SignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resentOtpUsingPOSTSignalErrorFull() instead")
    void resentOtpUsingPOSTSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void resentOtpUsingPOSTSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use verifyMobileOTPUsingPOSTSignalErrorFull() instead")
    void verifyMobileOTPUsingPOSTSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void verifyMobileOTPUsingPOSTSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use verifyUserViaMobileUsingPOSTSignalErrorFull() instead")
    void verifyUserViaMobileUsingPOSTSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void verifyUserViaMobileUsingPOSTSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
