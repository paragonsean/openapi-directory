/**
 * LH Partner API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIOffersApi_H
#define OAI_OAIOffersApi_H

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

class OAIOffersApi : public QObject {
    Q_OBJECT

public:
    OAIOffersApi(const int timeOut = 0);
    ~OAIOffersApi();

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
    * @param[in]  catalogues QString [required]
    * @param[in]  origin QString [required]
    * @param[in]  destination QString [required]
    * @param[in]  travel_date QString [required]
    * @param[in]  return_date QString [optional]
    * @param[in]  cabin_class QString [optional]
    * @param[in]  travelers QString [optional]
    * @param[in]  fare_family QString [optional]
    * @param[in]  trackingid QString [optional]
    * @param[in]  accept QString [optional]
    */
    virtual void all_Fares(const QString &catalogues, const QString &origin, const QString &destination, const QString &travel_date, const ::OpenAPI::OptionalParam<QString> &return_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &cabin_class = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &travelers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fare_family = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trackingid = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &accept = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  catalogues QString [required]
    * @param[in]  origin QString [required]
    * @param[in]  destination QString [required]
    * @param[in]  travel_date QString [required]
    * @param[in]  trip_duration QString [required]
    * @param[in]  range QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  cabin_class QString [optional]
    * @param[in]  country QString [optional]
    * @param[in]  trackingid QString [optional]
    * @param[in]  fare_family QString [optional]
    */
    virtual void best_Fares(const QString &catalogues, const QString &origin, const QString &destination, const QString &travel_date, const QString &trip_duration, const QString &range, const QString &accept, const ::OpenAPI::OptionalParam<QString> &cabin_class = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &country = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trackingid = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fare_family = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  catalogues QString [required]
    * @param[in]  trackingid QString [required]
    * @param[in]  country QString [required]
    * @param[in]  lang QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  origin QString [optional]
    * @param[in]  origin_name QString [optional]
    * @param[in]  destination QString [optional]
    * @param[in]  destination_name QString [optional]
    * @param[in]  travel_date QString [optional]
    * @param[in]  return_date QString [optional]
    * @param[in]  cabin_class QString [optional]
    * @param[in]  outbound_segments QString [optional]
    * @param[in]  return_segments QString [optional]
    * @param[in]  travelers QString [optional]
    * @param[in]  fare QString [optional]
    * @param[in]  net_fare QString [optional]
    * @param[in]  fare_currency QString [optional]
    * @param[in]  partnerid QString [optional]
    * @param[in]  encryption_key QString [optional]
    */
    virtual void deep_Links(const QString &catalogues, const QString &trackingid, const QString &country, const QString &lang, const QString &accept, const ::OpenAPI::OptionalParam<QString> &origin = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &origin_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &destination = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &destination_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &travel_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &return_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &cabin_class = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &outbound_segments = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &return_segments = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &travelers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fare = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &net_fare = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fare_currency = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &partnerid = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &encryption_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  catalogues QString [required]
    * @param[in]  segments QString [required]
    * @param[in]  carriers QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  travelers QString [optional]
    * @param[in]  fare_types QString [optional]
    */
    virtual void fares(const QString &catalogues, const QString &segments, const QString &carriers, const QString &accept, const ::OpenAPI::OptionalParam<QString> &travelers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fare_types = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  origin QString [required]
    * @param[in]  destination QString [required]
    * @param[in]  cabin_class QString [required]
    * @param[in]  trip_duration QString [required]
    * @param[in]  email QString [required]
    * @param[in]  lang QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  country QString [optional]
    * @param[in]  trackingid QString [optional]
    */
    virtual void fares_Subscriptions(const QString &origin, const QString &destination, const QString &cabin_class, const QString &trip_duration, const QString &email, const QString &lang, const QString &accept, const ::OpenAPI::OptionalParam<QString> &country = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &trackingid = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  catalogues QString [required]
    * @param[in]  origin QString [required]
    * @param[in]  destination QString [required]
    * @param[in]  travel_date QString [required]
    * @param[in]  trackingid QString [required]
    * @param[in]  country QString [required]
    * @param[in]  lang QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  return_date QString [optional]
    * @param[in]  cabin_class QString [optional]
    * @param[in]  travelers QString [optional]
    * @param[in]  partnerid QString [optional]
    * @param[in]  encryption_key QString [optional]
    */
    virtual void lH_Deep_Links__FFP(const QString &catalogues, const QString &origin, const QString &destination, const QString &travel_date, const QString &trackingid, const QString &country, const QString &lang, const QString &accept, const ::OpenAPI::OptionalParam<QString> &return_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &cabin_class = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &travelers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &partnerid = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &encryption_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  catalogues QString [required]
    * @param[in]  origin QString [required]
    * @param[in]  destination QString [required]
    * @param[in]  travel_date QString [required]
    * @param[in]  outbound_segments QString [required]
    * @param[in]  fare QString [required]
    * @param[in]  fare_currency QString [required]
    * @param[in]  trackingid QString [required]
    * @param[in]  country QString [required]
    * @param[in]  lang QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  return_date QString [optional]
    * @param[in]  cabin_class QString [optional]
    * @param[in]  return_segments QString [optional]
    * @param[in]  travelers QString [optional]
    * @param[in]  net_fare QString [optional]
    * @param[in]  partnerid QString [optional]
    * @param[in]  encryption_key QString [optional]
    */
    virtual void lH_Deep_Links__ITCO(const QString &catalogues, const QString &origin, const QString &destination, const QString &travel_date, const QString &outbound_segments, const QString &fare, const QString &fare_currency, const QString &trackingid, const QString &country, const QString &lang, const QString &accept, const ::OpenAPI::OptionalParam<QString> &return_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &cabin_class = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &return_segments = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &travelers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &net_fare = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &partnerid = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &encryption_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  catalogues QString [required]
    * @param[in]  origin QString [required]
    * @param[in]  destination QString [required]
    * @param[in]  travel_date QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  return_date QString [optional]
    * @param[in]  cabin_class QString [optional]
    * @param[in]  travelers QString [optional]
    * @param[in]  fare_family QString [optional]
    * @param[in]  country QString [optional]
    */
    virtual void lowest_Fares(const QString &catalogues, const QString &origin, const QString &destination, const QString &travel_date, const QString &accept, const ::OpenAPI::OptionalParam<QString> &return_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &cabin_class = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &travelers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fare_family = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &country = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  origin QString [required]
    * @param[in]  destination QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  catalogues QString [optional]
    * @param[in]  limit QString [optional]
    * @param[in]  offset QString [optional]
    */
    virtual void oND_Route(const QString &origin, const QString &destination, const QString &accept, const ::OpenAPI::OptionalParam<QString> &catalogues = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &limit = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &offset = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  accept QString [required]
    * @param[in]  catalogues QString [optional]
    * @param[in]  new_routes QString [optional]
    * @param[in]  old_routes QString [optional]
    */
    virtual void oND_Status(const QString &accept, const ::OpenAPI::OptionalParam<QString> &catalogues = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &new_routes = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &old_routes = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  accept QString [required]
    * @param[in]  catalogues QString [optional]
    * @param[in]  origin QString [optional]
    */
    virtual void top_OND(const QString &accept, const ::OpenAPI::OptionalParam<QString> &catalogues = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &origin = ::OpenAPI::OptionalParam<QString>());


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

    void all_FaresCallback(OAIHttpRequestWorker *worker);
    void best_FaresCallback(OAIHttpRequestWorker *worker);
    void deep_LinksCallback(OAIHttpRequestWorker *worker);
    void faresCallback(OAIHttpRequestWorker *worker);
    void fares_SubscriptionsCallback(OAIHttpRequestWorker *worker);
    void lH_Deep_Links__FFPCallback(OAIHttpRequestWorker *worker);
    void lH_Deep_Links__ITCOCallback(OAIHttpRequestWorker *worker);
    void lowest_FaresCallback(OAIHttpRequestWorker *worker);
    void oND_RouteCallback(OAIHttpRequestWorker *worker);
    void oND_StatusCallback(OAIHttpRequestWorker *worker);
    void top_ONDCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void all_FaresSignal(QString summary);
    void best_FaresSignal(QString summary);
    void deep_LinksSignal(QString summary);
    void faresSignal(QString summary);
    void fares_SubscriptionsSignal(QString summary);
    void lH_Deep_Links__FFPSignal(QString summary);
    void lH_Deep_Links__ITCOSignal(QString summary);
    void lowest_FaresSignal(QString summary);
    void oND_RouteSignal(QString summary);
    void oND_StatusSignal(QString summary);
    void top_ONDSignal(QString summary);


    void all_FaresSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void best_FaresSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void deep_LinksSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void faresSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void fares_SubscriptionsSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void lH_Deep_Links__FFPSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void lH_Deep_Links__ITCOSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void lowest_FaresSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void oND_RouteSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void oND_StatusSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void top_ONDSignalFull(OAIHttpRequestWorker *worker, QString summary);

    Q_DECL_DEPRECATED_X("Use all_FaresSignalError() instead")
    void all_FaresSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void all_FaresSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use best_FaresSignalError() instead")
    void best_FaresSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void best_FaresSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deep_LinksSignalError() instead")
    void deep_LinksSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deep_LinksSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use faresSignalError() instead")
    void faresSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void faresSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use fares_SubscriptionsSignalError() instead")
    void fares_SubscriptionsSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void fares_SubscriptionsSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lH_Deep_Links__FFPSignalError() instead")
    void lH_Deep_Links__FFPSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void lH_Deep_Links__FFPSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lH_Deep_Links__ITCOSignalError() instead")
    void lH_Deep_Links__ITCOSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void lH_Deep_Links__ITCOSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lowest_FaresSignalError() instead")
    void lowest_FaresSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void lowest_FaresSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use oND_RouteSignalError() instead")
    void oND_RouteSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void oND_RouteSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use oND_StatusSignalError() instead")
    void oND_StatusSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void oND_StatusSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use top_ONDSignalError() instead")
    void top_ONDSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void top_ONDSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use all_FaresSignalErrorFull() instead")
    void all_FaresSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void all_FaresSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use best_FaresSignalErrorFull() instead")
    void best_FaresSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void best_FaresSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deep_LinksSignalErrorFull() instead")
    void deep_LinksSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deep_LinksSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use faresSignalErrorFull() instead")
    void faresSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void faresSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use fares_SubscriptionsSignalErrorFull() instead")
    void fares_SubscriptionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void fares_SubscriptionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lH_Deep_Links__FFPSignalErrorFull() instead")
    void lH_Deep_Links__FFPSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void lH_Deep_Links__FFPSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lH_Deep_Links__ITCOSignalErrorFull() instead")
    void lH_Deep_Links__ITCOSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void lH_Deep_Links__ITCOSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lowest_FaresSignalErrorFull() instead")
    void lowest_FaresSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void lowest_FaresSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use oND_RouteSignalErrorFull() instead")
    void oND_RouteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void oND_RouteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use oND_StatusSignalErrorFull() instead")
    void oND_StatusSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void oND_StatusSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use top_ONDSignalErrorFull() instead")
    void top_ONDSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void top_ONDSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
