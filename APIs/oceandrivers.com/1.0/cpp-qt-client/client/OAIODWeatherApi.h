/**
 * ODWeather
 * This is the api to access the ODWeather API information
 *
 * The version of the OpenAPI document: 1.0
 * Contact: matiasbonet@oceandrivers.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIODWeatherApi_H
#define OAI_OAIODWeatherApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIODWeatherApi : public QObject {
    Q_OBJECT

public:
    OAIODWeatherApi(const int timeOut = 0);
    ~OAIODWeatherApi();

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
    * @param[in]  station_name QString [required]
    */
    virtual void compareStation(const QString &station_name);

    /**
    * @param[in]  station_name QString [required]
    * @param[in]  period QString [required]
    */
    virtual void getAemetStation(const QString &station_name, const QString &period);

    /**
    * @param[in]  easywind_id QString [required]
    * @param[in]  period QString [required]
    */
    virtual void getEasywind(const QString &easywind_id, const QString &period);

    /**
    * @param[in]  event_id QString [required]
    */
    virtual void getEventStations(const QString &event_id);

    /**
    * @param[in]  yatchclubid QString [required]
    * @param[in]  language QString [required]
    */
    virtual void getForecastPoints(const QString &yatchclubid, const QString &language);

    /**
    * @param[in]  latitude float [required]
    * @param[in]  longitude float [required]
    * @param[in]  weather QString [required]
    * @param[in]  inittime QString [optional]
    * @param[in]  endtime QString [optional]
    * @param[in]  days qint32 [optional]
    * @param[in]  hours qint32 [optional]
    * @param[in]  wave QString [optional]
    * @param[in]  entryid QString [optional]
    */
    virtual void getForecastTimeSeries(const float &latitude, const float &longitude, const QString &weather, const ::OpenAPI::OptionalParam<QString> &inittime = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &endtime = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &days = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &hours = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &wave = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &entryid = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  latitude float [required]
    * @param[in]  longitude float [required]
    * @param[in]  weather QString [required]
    * @param[in]  inittime QString [optional]
    * @param[in]  endtime QString [optional]
    * @param[in]  days qint32 [optional]
    * @param[in]  hours qint32 [optional]
    * @param[in]  wave QString [optional]
    * @param[in]  entryid QString [optional]
    */
    virtual void getForecastTimeSeriesWrf(const float &latitude, const float &longitude, const QString &weather, const ::OpenAPI::OptionalParam<QString> &inittime = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &endtime = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &days = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &hours = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &wave = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &entryid = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  station_name QString [required]
    * @param[in]  period QString [required]
    */
    virtual void getSocibWeatherStation(const QString &station_name, const QString &period);

    /**
    * @param[in]  station_name QString [required]
    * @param[in]  period QString [required]
    */
    virtual void getWeatherDisplay(const QString &station_name, const QString &period);


    virtual void getWebCams();


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

    void compareStationCallback(OAIHttpRequestWorker *worker);
    void getAemetStationCallback(OAIHttpRequestWorker *worker);
    void getEasywindCallback(OAIHttpRequestWorker *worker);
    void getEventStationsCallback(OAIHttpRequestWorker *worker);
    void getForecastPointsCallback(OAIHttpRequestWorker *worker);
    void getForecastTimeSeriesCallback(OAIHttpRequestWorker *worker);
    void getForecastTimeSeriesWrfCallback(OAIHttpRequestWorker *worker);
    void getSocibWeatherStationCallback(OAIHttpRequestWorker *worker);
    void getWeatherDisplayCallback(OAIHttpRequestWorker *worker);
    void getWebCamsCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void compareStationSignal();
    void getAemetStationSignal();
    void getEasywindSignal();
    void getEventStationsSignal();
    void getForecastPointsSignal();
    void getForecastTimeSeriesSignal();
    void getForecastTimeSeriesWrfSignal();
    void getSocibWeatherStationSignal();
    void getWeatherDisplaySignal();
    void getWebCamsSignal();


    void compareStationSignalFull(OAIHttpRequestWorker *worker);
    void getAemetStationSignalFull(OAIHttpRequestWorker *worker);
    void getEasywindSignalFull(OAIHttpRequestWorker *worker);
    void getEventStationsSignalFull(OAIHttpRequestWorker *worker);
    void getForecastPointsSignalFull(OAIHttpRequestWorker *worker);
    void getForecastTimeSeriesSignalFull(OAIHttpRequestWorker *worker);
    void getForecastTimeSeriesWrfSignalFull(OAIHttpRequestWorker *worker);
    void getSocibWeatherStationSignalFull(OAIHttpRequestWorker *worker);
    void getWeatherDisplaySignalFull(OAIHttpRequestWorker *worker);
    void getWebCamsSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use compareStationSignalError() instead")
    void compareStationSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void compareStationSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAemetStationSignalError() instead")
    void getAemetStationSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getAemetStationSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEasywindSignalError() instead")
    void getEasywindSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getEasywindSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEventStationsSignalError() instead")
    void getEventStationsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getEventStationsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getForecastPointsSignalError() instead")
    void getForecastPointsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getForecastPointsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getForecastTimeSeriesSignalError() instead")
    void getForecastTimeSeriesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getForecastTimeSeriesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getForecastTimeSeriesWrfSignalError() instead")
    void getForecastTimeSeriesWrfSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getForecastTimeSeriesWrfSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSocibWeatherStationSignalError() instead")
    void getSocibWeatherStationSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getSocibWeatherStationSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getWeatherDisplaySignalError() instead")
    void getWeatherDisplaySignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getWeatherDisplaySignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getWebCamsSignalError() instead")
    void getWebCamsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getWebCamsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use compareStationSignalErrorFull() instead")
    void compareStationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void compareStationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAemetStationSignalErrorFull() instead")
    void getAemetStationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAemetStationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEasywindSignalErrorFull() instead")
    void getEasywindSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getEasywindSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEventStationsSignalErrorFull() instead")
    void getEventStationsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getEventStationsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getForecastPointsSignalErrorFull() instead")
    void getForecastPointsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getForecastPointsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getForecastTimeSeriesSignalErrorFull() instead")
    void getForecastTimeSeriesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getForecastTimeSeriesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getForecastTimeSeriesWrfSignalErrorFull() instead")
    void getForecastTimeSeriesWrfSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getForecastTimeSeriesWrfSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getSocibWeatherStationSignalErrorFull() instead")
    void getSocibWeatherStationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getSocibWeatherStationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getWeatherDisplaySignalErrorFull() instead")
    void getWeatherDisplaySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getWeatherDisplaySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getWebCamsSignalErrorFull() instead")
    void getWebCamsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getWebCamsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
