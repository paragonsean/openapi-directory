/**
 * Google Home
 * # Google Home Local API This is an unofficial documentation of the local API used by the Home app to communicate with GH devices. [GitHub Repo](https://github.com/rithvikvibhu/GHLocalApi)  [![GitHub stars](https://img.shields.io/github/stars/rithvikvibhu/GHLocalApi)](https://github.com/rithvikvibhu/GHLocalApi/stargazers) [![GitHub license](https://img.shields.io/github/license/rithvikvibhu/GHLocalApi)](https://github.com/rithvikvibhu/GHLocalApi/blob/master/LICENSE.md)  ## Getting Started  Requests must be made over HTTPS, port 8443, so the base URL for these endpoints is: `https://<google-home-ip>:8443/setup/`  Get the IP of Google Home from the Google Home app (Device Settings -> End of the list) or from your router.  GET requests are simple, in the browser kind.   POST requests need to set the header (when there's a body): `content-type: application/json`  ## Authentication  Since June 2019, most requests (with exceptions like `/setup/eureka_info`) need a local authorization token.  There are 3 kinds of tokens involved here:  ### Local Authorization Token This token must be sent in all requests in the header `cast-local-authorization-token`. It is short-lived (~1 day) and may change unexpectedly (with a sync, change in homegraph, etc.) ##### Get this token - With access to an android device, [get this token directly by either method](https://gist.github.com/rithvikvibhu/1a0f4937af957ef6a78453e3be482c1f). - Without a device, or to integrate it with a script, use an access token to get the homegraph and extract the token. To get an access token, read the next section. Check the example section for more info.  ### Access Token This is a standard google oauth2 access token. It is in the form `ya29.***`. This gives access to the Google Home Foyer API. These expire in an hour. Use this to get the homegraph (and then the local authorization token above). ##### Get this token To get this access token, either a Google account username/password or a Google Master Token is needed. More info in the gist. Use the script [from this gist](https://gist.github.com/rithvikvibhu/952f83ea656c6782fbd0f1645059055d).  ### Master Token This is in the form `aas_et/_***` and can be used to request access tokens. ##### Get this token The same [script in the gist](https://gist.github.com/rithvikvibhu/952f83ea656c6782fbd0f1645059055d) that gets the access token can also get the master token. Needs Google account creds.  ## Example  Here's the whole flow from just a pair of username/password to using the local API.  Prerequisites: - [grpcurl](https://github.com/fullstorydev/grpcurl) - [Proto files](https://drive.google.com/drive/folders/1RvnN3y-G23pd2SWHmfV_7sef8QU5GNF4?usp=sharing) (preserve folder structure)  ### 1. Get an access token with the script - Download get_tokens.py - Fill in username and password ```sh python3 get_tokens.py # Note down the access token printed. ```  ### 2. Use the access token and get home graph - This prints the json and uses jq to parse and filter out the fields deviceName and localAuthToken - This will give a list of all devices and their local auth tokens ```sh ./grpcurl -H 'authorization: Bearer ya29.a0Af****' \\  -import-path /path/to/protos \\  -proto /path/to/protos/google/internal/home/foyer/v1.proto \\  googlehomefoyer-pa.googleapis.com:443 \\  google.internal.home.foyer.v1.StructuresService/GetHomeGraph | jq '.home.devices[] | {deviceName, localAuthToken}' # Note down the local auth token for the device you want. ```  ### 3. Make the call to the local device using the local auth token ```sh curl -H \"cast-local-authorization-token: LOCAL_AUTH_TOKEN\" --verbose --insecure https://192.168.0.18:8443/setup/bluetooth/status ```
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDeviceInfoApi_H
#define OAI_OAIDeviceInfoApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAppDeviceIDRequest.h"
#include "OAICheckReadyStatusRequest.h"
#include "OAIExample1.h"
#include "OAIExample11.h"
#include "OAIExample12.h"
#include "OAIExample13.h"
#include "OAIExample14.h"
#include "OAIExample15.h"
#include "OAIExample16.h"
#include "OAITestInternetDownloadSpeedRequest.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDeviceInfoApi : public QObject {
    Q_OBJECT

public:
    OAIDeviceInfoApi(const int timeOut = 0);
    ~OAIDeviceInfoApi();

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
    * @param[in]  oai_app_device_id_request OAIAppDeviceIDRequest [required]
    */
    virtual void appDeviceID(const OAIAppDeviceIDRequest &oai_app_device_id_request);

    /**
    * @param[in]  oai_check_ready_status_request OAICheckReadyStatusRequest [required]
    */
    virtual void checkReadyStatus(const OAICheckReadyStatusRequest &oai_check_ready_status_request);

    /**
    * @param[in]  params QString [required]
    * @param[in]  options QString [required]
    * @param[in]  nonce qint32 [required]
    */
    virtual void eurekaInfo(const QString &params, const QString &options, const qint32 &nonce);


    virtual void locales();


    virtual void offer();

    /**
    * @param[in]  oai_test_internet_download_speed_request OAITestInternetDownloadSpeedRequest [required]
    */
    virtual void testInternetDownloadSpeed(const OAITestInternetDownloadSpeedRequest &oai_test_internet_download_speed_request);


    virtual void timezones();


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

    void appDeviceIDCallback(OAIHttpRequestWorker *worker);
    void checkReadyStatusCallback(OAIHttpRequestWorker *worker);
    void eurekaInfoCallback(OAIHttpRequestWorker *worker);
    void localesCallback(OAIHttpRequestWorker *worker);
    void offerCallback(OAIHttpRequestWorker *worker);
    void testInternetDownloadSpeedCallback(OAIHttpRequestWorker *worker);
    void timezonesCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void appDeviceIDSignal(OAIExample11 summary);
    void checkReadyStatusSignal(OAIExample13 summary);
    void eurekaInfoSignal(OAIExample1 summary);
    void localesSignal(QList<OAIExample15> summary);
    void offerSignal(OAIExample12 summary);
    void testInternetDownloadSpeedSignal(OAIExample16 summary);
    void timezonesSignal(QList<OAIExample14> summary);


    void appDeviceIDSignalFull(OAIHttpRequestWorker *worker, OAIExample11 summary);
    void checkReadyStatusSignalFull(OAIHttpRequestWorker *worker, OAIExample13 summary);
    void eurekaInfoSignalFull(OAIHttpRequestWorker *worker, OAIExample1 summary);
    void localesSignalFull(OAIHttpRequestWorker *worker, QList<OAIExample15> summary);
    void offerSignalFull(OAIHttpRequestWorker *worker, OAIExample12 summary);
    void testInternetDownloadSpeedSignalFull(OAIHttpRequestWorker *worker, OAIExample16 summary);
    void timezonesSignalFull(OAIHttpRequestWorker *worker, QList<OAIExample14> summary);

    Q_DECL_DEPRECATED_X("Use appDeviceIDSignalError() instead")
    void appDeviceIDSignalE(OAIExample11 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void appDeviceIDSignalError(OAIExample11 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use checkReadyStatusSignalError() instead")
    void checkReadyStatusSignalE(OAIExample13 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void checkReadyStatusSignalError(OAIExample13 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eurekaInfoSignalError() instead")
    void eurekaInfoSignalE(OAIExample1 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void eurekaInfoSignalError(OAIExample1 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use localesSignalError() instead")
    void localesSignalE(QList<OAIExample15> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void localesSignalError(QList<OAIExample15> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use offerSignalError() instead")
    void offerSignalE(OAIExample12 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void offerSignalError(OAIExample12 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use testInternetDownloadSpeedSignalError() instead")
    void testInternetDownloadSpeedSignalE(OAIExample16 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void testInternetDownloadSpeedSignalError(OAIExample16 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use timezonesSignalError() instead")
    void timezonesSignalE(QList<OAIExample14> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void timezonesSignalError(QList<OAIExample14> summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use appDeviceIDSignalErrorFull() instead")
    void appDeviceIDSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appDeviceIDSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use checkReadyStatusSignalErrorFull() instead")
    void checkReadyStatusSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void checkReadyStatusSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eurekaInfoSignalErrorFull() instead")
    void eurekaInfoSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void eurekaInfoSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use localesSignalErrorFull() instead")
    void localesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void localesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use offerSignalErrorFull() instead")
    void offerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void offerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use testInternetDownloadSpeedSignalErrorFull() instead")
    void testInternetDownloadSpeedSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void testInternetDownloadSpeedSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use timezonesSignalErrorFull() instead")
    void timezonesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void timezonesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
