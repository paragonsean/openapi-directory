/**
 * Moon API
 * # Moon-API.com Postman Collection  Welcome to the Moon Phase API Postman Collection! This collection contains a set of pre-configured API requests to interact with the Moon Phase API endpoints provided by [moon-api.com](https://moon-api.com). Explore the enchanting world of the moon and its ever-changing phases with ease using this collection.  ## Getting Started  To start using this Postman collection, follow these steps:  1. [Download and install Postman](https://www.postman.com/downloads/) if you haven't already. 2. Import the Moon API Postman Collection into your Postman app. 3. Set your RapidAPI key in the collection's environment variables. 4. Begin making requests to explore the moon phase data and retrieve lunar information.       ## Collection Structure  The Moon-API.com Postman Collection consists of the following requests:  - **Basic Moon Phase**: Retrieve the main moon phase data. - **Advanced Moon Phase**: Get detailed moon phase data based on a specific timezone and coordinates. - **Plain Text Moon Phase**: Get a plain text description of the current moon phase. - **Emoji Moon Phase**: Get the relevant emoji of the current moon phase. - **Lunar Calender**: Get the current year's moon phases in a markdown calender.       ## Environment Variables  The collection uses environment variables to store your RapidAPI key. To use this collection effectively, ensure you set the `X-Rapidapi-Key` variable in the collection's environment with your actual RapidAPI key.  ## How to Use  1. Select the desired request from the Moon API collection. 2. Click on the request to open it. 3. Send the request and view the response to retrieve the moon phase data.       ## Documentation  For more information on the Moon Phase API endpoints and their response formats, refer to the [official Moon API documentation](https://rapidapi.com/MoonAPIcom/api/moon-phase/details). Visit [moon-api.com](https://moon-api.com) to learn more about the Moon Phase API and the services provided.  Happy moon exploration with the Moon Phase API Postman Collection provided by [moon-api.com](https://moon-api.com)!
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDefaultApi_H
#define OAI_OAIDefaultApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGetAdvancedMoonPhaseData_200_response.h"
#include "OAIGetBasicMoonPhaseData_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDefaultApi : public QObject {
    Q_OBJECT

public:
    OAIDefaultApi(const int timeOut = 0);
    ~OAIDefaultApi();

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
    * @param[in]  filters QString [optional]
    * @param[in]  x_rapidapi_key QString [optional]
    */
    virtual void getAdvancedMoonPhaseData(const ::OpenAPI::OptionalParam<QString> &filters = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_rapidapi_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_rapidapi_key QString [optional]
    */
    virtual void getBasicMoonPhaseData(const ::OpenAPI::OptionalParam<QString> &x_rapidapi_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_rapidapi_key QString [optional]
    */
    virtual void getEmojiOfMoonPhase(const ::OpenAPI::OptionalParam<QString> &x_rapidapi_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  filters QString [optional]
    * @param[in]  x_rapidapi_key QString [optional]
    */
    virtual void getLunarCalendar(const ::OpenAPI::OptionalParam<QString> &filters = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_rapidapi_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_rapidapi_key QString [optional]
    */
    virtual void getPlainTextMoonPhaseData(const ::OpenAPI::OptionalParam<QString> &x_rapidapi_key = ::OpenAPI::OptionalParam<QString>());


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

    void getAdvancedMoonPhaseDataCallback(OAIHttpRequestWorker *worker);
    void getBasicMoonPhaseDataCallback(OAIHttpRequestWorker *worker);
    void getEmojiOfMoonPhaseCallback(OAIHttpRequestWorker *worker);
    void getLunarCalendarCallback(OAIHttpRequestWorker *worker);
    void getPlainTextMoonPhaseDataCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getAdvancedMoonPhaseDataSignal(OAIGetAdvancedMoonPhaseData_200_response summary);
    void getBasicMoonPhaseDataSignal(OAIGetBasicMoonPhaseData_200_response summary);
    void getEmojiOfMoonPhaseSignal();
    void getLunarCalendarSignal();
    void getPlainTextMoonPhaseDataSignal();


    void getAdvancedMoonPhaseDataSignalFull(OAIHttpRequestWorker *worker, OAIGetAdvancedMoonPhaseData_200_response summary);
    void getBasicMoonPhaseDataSignalFull(OAIHttpRequestWorker *worker, OAIGetBasicMoonPhaseData_200_response summary);
    void getEmojiOfMoonPhaseSignalFull(OAIHttpRequestWorker *worker);
    void getLunarCalendarSignalFull(OAIHttpRequestWorker *worker);
    void getPlainTextMoonPhaseDataSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use getAdvancedMoonPhaseDataSignalError() instead")
    void getAdvancedMoonPhaseDataSignalE(OAIGetAdvancedMoonPhaseData_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getAdvancedMoonPhaseDataSignalError(OAIGetAdvancedMoonPhaseData_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getBasicMoonPhaseDataSignalError() instead")
    void getBasicMoonPhaseDataSignalE(OAIGetBasicMoonPhaseData_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getBasicMoonPhaseDataSignalError(OAIGetBasicMoonPhaseData_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEmojiOfMoonPhaseSignalError() instead")
    void getEmojiOfMoonPhaseSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getEmojiOfMoonPhaseSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLunarCalendarSignalError() instead")
    void getLunarCalendarSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getLunarCalendarSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPlainTextMoonPhaseDataSignalError() instead")
    void getPlainTextMoonPhaseDataSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getPlainTextMoonPhaseDataSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getAdvancedMoonPhaseDataSignalErrorFull() instead")
    void getAdvancedMoonPhaseDataSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAdvancedMoonPhaseDataSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getBasicMoonPhaseDataSignalErrorFull() instead")
    void getBasicMoonPhaseDataSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getBasicMoonPhaseDataSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEmojiOfMoonPhaseSignalErrorFull() instead")
    void getEmojiOfMoonPhaseSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getEmojiOfMoonPhaseSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLunarCalendarSignalErrorFull() instead")
    void getLunarCalendarSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLunarCalendarSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPlainTextMoonPhaseDataSignalErrorFull() instead")
    void getPlainTextMoonPhaseDataSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPlainTextMoonPhaseDataSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
