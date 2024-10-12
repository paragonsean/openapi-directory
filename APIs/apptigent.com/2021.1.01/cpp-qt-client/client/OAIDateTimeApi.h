/**
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDateTimeApi_H
#define OAI_OAIDateTimeApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIInputDateTimeConversion.h"
#include "OAIInputDateTimeDifference.h"
#include "OAIInputDateTimeFormat.h"
#include "OAIInputDateTimeInfo.h"
#include "OAIOutputDateDifference.h"
#include "OAIOutputDateInfo.h"
#include "OAIOutputString.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDateTimeApi : public QObject {
    Q_OBJECT

public:
    OAIDateTimeApi(const int timeOut = 0);
    ~OAIDateTimeApi();

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
    * @param[in]  date_time_difference OAIInputDateTimeDifference [optional]
    */
    virtual void dateTimeDifference(const ::OpenAPI::OptionalParam<OAIInputDateTimeDifference> &date_time_difference = ::OpenAPI::OptionalParam<OAIInputDateTimeDifference>());

    /**
    * @param[in]  date_time_info OAIInputDateTimeInfo [optional]
    */
    virtual void dateTimeInfo(const ::OpenAPI::OptionalParam<OAIInputDateTimeInfo> &date_time_info = ::OpenAPI::OptionalParam<OAIInputDateTimeInfo>());

    /**
    * @param[in]  date_time_format OAIInputDateTimeFormat [optional]
    */
    virtual void formatDateTime(const ::OpenAPI::OptionalParam<OAIInputDateTimeFormat> &date_time_format = ::OpenAPI::OptionalParam<OAIInputDateTimeFormat>());

    /**
    * @param[in]  date_time_conversion OAIInputDateTimeConversion [optional]
    */
    virtual void worldTime(const ::OpenAPI::OptionalParam<OAIInputDateTimeConversion> &date_time_conversion = ::OpenAPI::OptionalParam<OAIInputDateTimeConversion>());


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

    void dateTimeDifferenceCallback(OAIHttpRequestWorker *worker);
    void dateTimeInfoCallback(OAIHttpRequestWorker *worker);
    void formatDateTimeCallback(OAIHttpRequestWorker *worker);
    void worldTimeCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void dateTimeDifferenceSignal(OAIOutputDateDifference summary);
    void dateTimeInfoSignal(OAIOutputDateInfo summary);
    void formatDateTimeSignal(OAIOutputString summary);
    void worldTimeSignal(OAIOutputString summary);


    void dateTimeDifferenceSignalFull(OAIHttpRequestWorker *worker, OAIOutputDateDifference summary);
    void dateTimeInfoSignalFull(OAIHttpRequestWorker *worker, OAIOutputDateInfo summary);
    void formatDateTimeSignalFull(OAIHttpRequestWorker *worker, OAIOutputString summary);
    void worldTimeSignalFull(OAIHttpRequestWorker *worker, OAIOutputString summary);

    Q_DECL_DEPRECATED_X("Use dateTimeDifferenceSignalError() instead")
    void dateTimeDifferenceSignalE(OAIOutputDateDifference summary, QNetworkReply::NetworkError error_type, QString error_str);
    void dateTimeDifferenceSignalError(OAIOutputDateDifference summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use dateTimeInfoSignalError() instead")
    void dateTimeInfoSignalE(OAIOutputDateInfo summary, QNetworkReply::NetworkError error_type, QString error_str);
    void dateTimeInfoSignalError(OAIOutputDateInfo summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use formatDateTimeSignalError() instead")
    void formatDateTimeSignalE(OAIOutputString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void formatDateTimeSignalError(OAIOutputString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use worldTimeSignalError() instead")
    void worldTimeSignalE(OAIOutputString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void worldTimeSignalError(OAIOutputString summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use dateTimeDifferenceSignalErrorFull() instead")
    void dateTimeDifferenceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void dateTimeDifferenceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use dateTimeInfoSignalErrorFull() instead")
    void dateTimeInfoSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void dateTimeInfoSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use formatDateTimeSignalErrorFull() instead")
    void formatDateTimeSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void formatDateTimeSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use worldTimeSignalErrorFull() instead")
    void worldTimeSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void worldTimeSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
