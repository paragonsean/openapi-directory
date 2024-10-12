/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAISeriesTypesApi_H
#define OAI_OAISeriesTypesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAISeriestype.h"
#include "OAISeriestyperule.h"
#include "OAISeriestyperuleattribute.h"
#include "OAISeriestypeupdatestatus.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAISeriesTypesApi : public QObject {
    Q_OBJECT

public:
    OAISeriesTypesApi(const int timeOut = 0);
    ~OAISeriesTypesApi();

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
    * @param[in]  startindex qint64 [optional]
    * @param[in]  count qint64 [optional]
    */
    virtual void seriestypesGet(const ::OpenAPI::OptionalParam<qint64> &startindex = ::OpenAPI::OptionalParam<qint64>(), const ::OpenAPI::OptionalParam<qint64> &count = ::OpenAPI::OptionalParam<qint64>());

    /**
    * @param[in]  id qint64 [required]
    */
    virtual void seriestypesIdDelete(const qint64 &id);

    /**
    * @param[in]  id qint64 [required]
    */
    virtual void seriestypesIdPut(const qint64 &id);

    /**
    * @param[in]  series_type OAISeriestype [optional]
    */
    virtual void seriestypesPost(const ::OpenAPI::OptionalParam<OAISeriestype> &series_type = ::OpenAPI::OptionalParam<OAISeriestype>());

    /**
    * @param[in]  seriestypeid qint64 [required]
    */
    virtual void seriestypesRulesGet(const qint64 &seriestypeid);

    /**
    * @param[in]  id qint64 [required]
    */
    virtual void seriestypesRulesIdAttributesGet(const qint64 &id);

    /**
    * @param[in]  id qint64 [required]
    * @param[in]  series_type_rule_attribute OAISeriestyperuleattribute [optional]
    */
    virtual void seriestypesRulesIdAttributesPost(const qint64 &id, const ::OpenAPI::OptionalParam<OAISeriestyperuleattribute> &series_type_rule_attribute = ::OpenAPI::OptionalParam<OAISeriestyperuleattribute>());

    /**
    * @param[in]  id qint64 [required]
    */
    virtual void seriestypesRulesIdDelete(const qint64 &id);

    /**
    * @param[in]  series_type_rule OAISeriestyperule [optional]
    */
    virtual void seriestypesRulesPost(const ::OpenAPI::OptionalParam<OAISeriestyperule> &series_type_rule = ::OpenAPI::OptionalParam<OAISeriestyperule>());

    /**
    * @param[in]  rule_id qint64 [required]
    * @param[in]  attribute_id qint64 [required]
    */
    virtual void seriestypesRulesRuleIdAttributesAttributeIdDelete(const qint64 &rule_id, const qint64 &attribute_id);


    virtual void seriestypesRulesUpdatestatusGet();


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

    void seriestypesGetCallback(OAIHttpRequestWorker *worker);
    void seriestypesIdDeleteCallback(OAIHttpRequestWorker *worker);
    void seriestypesIdPutCallback(OAIHttpRequestWorker *worker);
    void seriestypesPostCallback(OAIHttpRequestWorker *worker);
    void seriestypesRulesGetCallback(OAIHttpRequestWorker *worker);
    void seriestypesRulesIdAttributesGetCallback(OAIHttpRequestWorker *worker);
    void seriestypesRulesIdAttributesPostCallback(OAIHttpRequestWorker *worker);
    void seriestypesRulesIdDeleteCallback(OAIHttpRequestWorker *worker);
    void seriestypesRulesPostCallback(OAIHttpRequestWorker *worker);
    void seriestypesRulesRuleIdAttributesAttributeIdDeleteCallback(OAIHttpRequestWorker *worker);
    void seriestypesRulesUpdatestatusGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void seriestypesGetSignal(QList<OAISeriestype> summary);
    void seriestypesIdDeleteSignal();
    void seriestypesIdPutSignal();
    void seriestypesPostSignal(OAISeriestype summary);
    void seriestypesRulesGetSignal(QList<OAISeriestyperule> summary);
    void seriestypesRulesIdAttributesGetSignal(QList<OAISeriestyperuleattribute> summary);
    void seriestypesRulesIdAttributesPostSignal(OAISeriestyperuleattribute summary);
    void seriestypesRulesIdDeleteSignal();
    void seriestypesRulesPostSignal(OAISeriestyperule summary);
    void seriestypesRulesRuleIdAttributesAttributeIdDeleteSignal();
    void seriestypesRulesUpdatestatusGetSignal(OAISeriestypeupdatestatus summary);


    void seriestypesGetSignalFull(OAIHttpRequestWorker *worker, QList<OAISeriestype> summary);
    void seriestypesIdDeleteSignalFull(OAIHttpRequestWorker *worker);
    void seriestypesIdPutSignalFull(OAIHttpRequestWorker *worker);
    void seriestypesPostSignalFull(OAIHttpRequestWorker *worker, OAISeriestype summary);
    void seriestypesRulesGetSignalFull(OAIHttpRequestWorker *worker, QList<OAISeriestyperule> summary);
    void seriestypesRulesIdAttributesGetSignalFull(OAIHttpRequestWorker *worker, QList<OAISeriestyperuleattribute> summary);
    void seriestypesRulesIdAttributesPostSignalFull(OAIHttpRequestWorker *worker, OAISeriestyperuleattribute summary);
    void seriestypesRulesIdDeleteSignalFull(OAIHttpRequestWorker *worker);
    void seriestypesRulesPostSignalFull(OAIHttpRequestWorker *worker, OAISeriestyperule summary);
    void seriestypesRulesRuleIdAttributesAttributeIdDeleteSignalFull(OAIHttpRequestWorker *worker);
    void seriestypesRulesUpdatestatusGetSignalFull(OAIHttpRequestWorker *worker, OAISeriestypeupdatestatus summary);

    Q_DECL_DEPRECATED_X("Use seriestypesGetSignalError() instead")
    void seriestypesGetSignalE(QList<OAISeriestype> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesGetSignalError(QList<OAISeriestype> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesIdDeleteSignalError() instead")
    void seriestypesIdDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesIdDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesIdPutSignalError() instead")
    void seriestypesIdPutSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesIdPutSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesPostSignalError() instead")
    void seriestypesPostSignalE(OAISeriestype summary, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesPostSignalError(OAISeriestype summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesRulesGetSignalError() instead")
    void seriestypesRulesGetSignalE(QList<OAISeriestyperule> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesRulesGetSignalError(QList<OAISeriestyperule> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesRulesIdAttributesGetSignalError() instead")
    void seriestypesRulesIdAttributesGetSignalE(QList<OAISeriestyperuleattribute> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesRulesIdAttributesGetSignalError(QList<OAISeriestyperuleattribute> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesRulesIdAttributesPostSignalError() instead")
    void seriestypesRulesIdAttributesPostSignalE(OAISeriestyperuleattribute summary, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesRulesIdAttributesPostSignalError(OAISeriestyperuleattribute summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesRulesIdDeleteSignalError() instead")
    void seriestypesRulesIdDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesRulesIdDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesRulesPostSignalError() instead")
    void seriestypesRulesPostSignalE(OAISeriestyperule summary, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesRulesPostSignalError(OAISeriestyperule summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesRulesRuleIdAttributesAttributeIdDeleteSignalError() instead")
    void seriestypesRulesRuleIdAttributesAttributeIdDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesRulesRuleIdAttributesAttributeIdDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesRulesUpdatestatusGetSignalError() instead")
    void seriestypesRulesUpdatestatusGetSignalE(OAISeriestypeupdatestatus summary, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesRulesUpdatestatusGetSignalError(OAISeriestypeupdatestatus summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use seriestypesGetSignalErrorFull() instead")
    void seriestypesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesIdDeleteSignalErrorFull() instead")
    void seriestypesIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesIdPutSignalErrorFull() instead")
    void seriestypesIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesPostSignalErrorFull() instead")
    void seriestypesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesRulesGetSignalErrorFull() instead")
    void seriestypesRulesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesRulesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesRulesIdAttributesGetSignalErrorFull() instead")
    void seriestypesRulesIdAttributesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesRulesIdAttributesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesRulesIdAttributesPostSignalErrorFull() instead")
    void seriestypesRulesIdAttributesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesRulesIdAttributesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesRulesIdDeleteSignalErrorFull() instead")
    void seriestypesRulesIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesRulesIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesRulesPostSignalErrorFull() instead")
    void seriestypesRulesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesRulesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesRulesRuleIdAttributesAttributeIdDeleteSignalErrorFull() instead")
    void seriestypesRulesRuleIdAttributesAttributeIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesRulesRuleIdAttributesAttributeIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seriestypesRulesUpdatestatusGetSignalErrorFull() instead")
    void seriestypesRulesUpdatestatusGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void seriestypesRulesUpdatestatusGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
